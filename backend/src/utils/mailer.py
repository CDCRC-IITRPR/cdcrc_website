import os
from django.core.mail import EmailMultiAlternatives


class Mailer:
    sender_name = None
    sender_email = None

    def __init__(self):
        '''
        Instantiating the sender email and sender name from env variables
        '''
        self.sender_name = os.environ.get('SENDER_NAME')
        self.sender_email = os.environ.get('SENDER_EMAIL')

    def send_email(self, to, subject,  body, cc=None, bcc=None,):
        '''
        Function to send email. It supports miltiple clients, and email body can be an HTML message
        '''
        # convert TO into list if string
        if type(to) is not list:
            to = to.split()

        message = EmailMultiAlternatives(
            subject=subject,
            from_email=self.sender_email,
            to=to,
        )
        message.attach_alternative(body, "text/html")

        try:
            message.send(fail_silently=False)
            return 'ok'
        except Exception as e:
            print("Some error occured in mail service")
            print(str(e))
            return 'fail'


    def send_issue_create_alert_to_assignee(self, to_list, concerned_name, subject, issue_title, issue_priority, issue_detail_url):
        print(issue_detail_url)
        message_body = """
            <h3>CDCRC System Generated Alert</h3>
            <hr>
            <h1>An issue has been assigned to you {}</h1>
            <p>Title: {}</p>
            <p>Priority: {}</p>
            <button><a href="{}">Detail Here</a></button>
            <br>""".format(concerned_name, issue_title, issue_priority, issue_detail_url)
        self.send_email(to_list, subject, message_body)

    def send_issue_create_alert_to_creator(self, to_list, concerned_name, subject, issue_title, issue_priority, issue_detail_url):
        print(issue_detail_url)
        message_body = """
            <h3>CDCRC System Generated Alert</h3>
            <hr>
            <h1>An issue has been created by you {}</h1>
            <p>Title: {}</p>
            <p>Priority: {}</p>
            <button><a href="{}">Detail Here</a></button>
            <br>""".format(concerned_name, issue_title, issue_priority, issue_detail_url)
        self.send_email(to_list, subject, message_body)

    def send_issue_close_alert_to_creator(self, to_list, creator_name, closer_name, subject, issue_title, issue_detail_url):
        print(issue_detail_url)
        message_body = """
            <h3>CDCRC System Generated Alert</h3>
            <hr>
            <h1>Issue created by you {} has been closed by {}</h1>
            <p>Title: {}</p>
            <button><a href="{}">Detail Here</a></button>
            <br>""".format(creator_name, closer_name, issue_title, issue_detail_url)
        self.send_email(to_list, subject, message_body)

    def send_issue_open_alert_to_creator(self, to_list, creator_name, opener_name, subject, issue_title, issue_detail_url):
        print(issue_detail_url)
        message_body = """
            <h3>CDCRC System Generated Alert</h3>
            <hr>
            <h1>Issue created by you {} has been opened by {}</h1>
            <p>Title: {}</p>
            <button><a href="{}">Detail Here</a></button>
            <br>""".format(creator_name, opener_name, issue_title, issue_detail_url)
        self.send_email(to_list, subject, message_body)

    def send_issue_close_alert_to_closer(self, to_list, closer_name, subject, issue_title, issue_detail_url):
        print(issue_detail_url)
        message_body = """
            <h3>CDCRC System Generated Alert</h3>
            <hr>
            <h1>Issue has been closed by you {}</h1>
            <p>Title: {}</p>
            <button><a href="{}">Detail Here</a></button>
            <br>""".format(closer_name, issue_title, issue_detail_url)
        self.send_email(to_list, subject, message_body)

    def send_issue_followup_alert_to_assignee(self, to_list, assignee_name, subject, issue_title, followup_comment, issue_detail_url):
        print(issue_detail_url)
        message_body = """
            <h3>CDCRC System Generated Alert</h3>
            <hr>
            <h1>Issue Follow Up has been assigned to you {}</h1>
            <p>Issue Title: {}</p>
            <p>Comment: {}</p>
            <button><a href="{}">Detail Here</a></button>
            <br>""".format(assignee_name, issue_title, followup_comment, issue_detail_url)

        self.send_email(to_list, subject, message_body)

    def send_issue_followup_alert_to_follower(self, to_list, follower_name, subject, issue_title, followup_comment, issue_detail_url):
        print(issue_detail_url)
        message_body = """
            <h3>CDCRC System Generated Alert</h3>
            <hr>
            <h1>You {} followed up on an Issue</h1>
            <p>Issue Title: {}</p>
            <p>Comment: {}</p>
            <button><a href="{}">Detail Here</a></button>
            <br>""".format(follower_name, issue_title, followup_comment, issue_detail_url)

        self.send_email(to_list, subject, message_body)

    def send_issue_followup_alert_to_creator(self, to_list, follower_name, subject, issue_title, followup_comment, issue_detail_url):
        message_body = """
            <h3>CDCRC System Generated Alert</h3>
            <hr>
            <h1>{} followed up on an Issue Created By You</h1>
            <p>Issue Title: {}</p>
            <p>Comment: {}</p>
            <button><a href="{}">Detail Here</a></button>
            <br>""".format(follower_name, issue_title, followup_comment, issue_detail_url)

        self.send_email(to_list, subject, message_body)
