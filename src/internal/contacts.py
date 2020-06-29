import csv
from internal.models import Contact
from recruiter.models import Recruiter
from io import TextIOWrapper

class ContactsCSVHandler:
    file = None
    encoding = None

    def __init__(self, file, encoding):
        self.file = file
        self.encoding = encoding

    #function to cleanly format the phone number
    def clean_phone_number(self, phone_number):
        phone_number = phone_number.replace(' ', '')
        phone_number = phone_number.replace('-', '')
        phone_number = phone_number.replace('+', '')
        if phone_number.startswith('91'):
            phone_number = phone_number[2:]

        return phone_number

    def get_header_idx_from_key_words(self, header, included_keywords, excluded_header_indices=None):
        for header_idx, header_item in enumerate(header):
            #check if any of the excluded keywords are there in this header_item
            if excluded_header_indices!=None and header_idx in excluded_header_indices:
                continue

            for include_keyword in included_keywords:
                if include_keyword.lower() in header_item.lower():
                    return header_idx
        return None

    def check_approval(self, contact_obj):
        similar_first_name_exists = Contact.objects.filter(first_name__iexact=contact_obj['first_name']).exists()
        recruiter_exists = Recruiter.objects.filter(name__iexact=contact_obj['recruiter']).exists()
        if similar_first_name_exists==False and recruiter_exists==True:
            return True
        else: return False

    def get_recruiter_obj(self, recuiter_name):
        try:
            recruiter = Recruiter.objects.get(name=recuiter_name)
            return recruiter
        except:
            return None

    
    def import_from_file(self):
        f = TextIOWrapper(self.file.file, encoding=self.encoding)
        contacts = csv.reader(f)
        #identify the correct columns indices form the header row

        for row_idx, row in enumerate(contacts, 0):
            if row_idx==0:
                first_name_idx = self.get_header_idx_from_key_words(row, ['first'])
                last_name_idx = self.get_header_idx_from_key_words(row, ['last'], excluded_header_indices=[first_name_idx])
                suffix_idx = self.get_header_idx_from_key_words(row, ['suffix'], excluded_header_indices=[first_name_idx, last_name_idx])
                job_title_idx = self.get_header_idx_from_key_words(row, ['job', 'title'], excluded_header_indices=[first_name_idx, last_name_idx, suffix_idx])
                email_idx = self.get_header_idx_from_key_words(row, ['email'], excluded_header_indices=[
                    first_name_idx, last_name_idx, suffix_idx, job_title_idx, 
                ])
                
                recruiter_idx = self.get_header_idx_from_key_words(row, ['company'], excluded_header_indices=[
                    first_name_idx, last_name_idx, suffix_idx, job_title_idx, email_idx,
                ])
                phone_one_idx = self.get_header_idx_from_key_words(row, ['phone'],  excluded_header_indices=[
                    first_name_idx, last_name_idx, suffix_idx, job_title_idx, email_idx, recruiter_idx,
                ])
                phone_two_idx = self.get_header_idx_from_key_words(row, ['phone'],  excluded_header_indices=[
                    first_name_idx, last_name_idx, suffix_idx, job_title_idx, email_idx, recruiter_idx, phone_one_idx
                ])

            else:
                curr_contact = {}
                curr_contact['first_name'] = row[first_name_idx] if first_name_idx!=None else  None
                curr_contact['last_name'] = row[last_name_idx] if last_name_idx!=None else  None
                curr_contact['suffix'] = row[suffix_idx] if suffix_idx!=None else  None
                curr_contact['job_title'] = row[job_title_idx] if job_title_idx!=None else  None
                curr_contact['email'] = row[email_idx] if email_idx!=None else  None
                curr_contact['recruiter'] = row[recruiter_idx] if recruiter_idx!=None else  None
                curr_contact['phone_one'] = self.clean_phone_number(row[phone_one_idx]) if phone_one_idx!=None else  None
                curr_contact['phone_two'] = self.clean_phone_number(row[phone_two_idx]) if phone_two_idx!=None else  None

                print(curr_contact)

                approved = self.check_approval(curr_contact)

                print(approved)

                contact_db_obj = Contact(
                    first_name=curr_contact['first_name'],
                    last_name=curr_contact['last_name'],
                    suffix=curr_contact['suffix'],
                    job_title=curr_contact['job_title'],
                    phone_one = curr_contact['phone_one'],
                    phone_two = curr_contact['phone_two'], 
                    email = curr_contact['email'],
                    approved = approved,
                    recruiter = self.get_recruiter_obj(curr_contact['recruiter'])
                )
                
                contact_db_obj.save()
            
