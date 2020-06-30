import sys
import os
import json
import smtplib
# Import the email modules


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# CREDS = 


# sender_name = 'Dr. Somitra Sanadhya'
# gmail_user = 'somitra@iitrpr.ac.in'
# gmail_pwd = 'enter_password_here' #CHANGE HERE
# subject = "Pre-Endsem Marks for ToC"   #CHANGE HERE

def send_email(to, rec_name, class_participation, quiz, midterm, pmt,  cc=None, bcc=None, subject=None, server=None):
    ''' sends email using a Jinja HTML template '''

    # convert TO into list if string
    if type(to) is not list:
        to = to.split()

    to_list = to  # remove null emails

    msg = MIMEMultipart('alternative')
    msg['From'] = sender_name+' <'+gmail_user+'>'
    msg['Subject'] = subject
    msg['To'] = ','.join(to)
    msg['Cc'] = cc
    msg['Bcc'] = bcc

    body = "Dear "+rec_name+"<br><br>"
    body += "You have received the following marks in ToC-<br>"
    body += "<br>Quiz --> " + str(quiz) + "/15"
    body += "<br>Class Participation --> " + str(class_participation)+"/10"
    body += "<br>Midterm --> " + str(midterm)+"/45"
    body += "<br><strong>PMT --> " + str(pmt)+"/70</strong>"
    body += "<br><br>Regards<br>Dr. Somitra" #COULD CHANGE HERE
    msg.attach(MIMEText(body, 'html'))

    try:
        server.sendmail(gmail_user, to_list, msg.as_string())
        print('sending email to', to_list)
        return 'ok'
    except Exception as e:
        print('Error sending email')
        print(str(e))
        return 'fail'

# ------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    server = smtplib.SMTP('smtp.gmail.com', 587)  # or your smtp server
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)

    wb = xlrd.open_workbook('data.xlsx')#CHANGE HERE
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 

    for i in range(sheet.nrows):
        if i>0:
            to_list = [sheet.cell_value(i, 3)]
            rec_name = sheet.cell_value(i, 2)
            class_participation = sheet.cell_value(i, 4)
            quiz = sheet.cell_value(i, 5)
            midterm = sheet.cell_value(i, 6)
            pmt = sheet.cell_value(i, 7)

            print(to_list, class_participation, quiz, midterm, pmt)

            # send email to a list of email addresses
            send_email(to_list,  rec_name, class_participation, quiz, midterm, pmt, cc=None, bcc=None, subject=subject,  server=server)

    server.quit()
