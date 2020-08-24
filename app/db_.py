#--------To perform operation on customer details and email template table--------------------

from flask_mail import Message
from flask import jsonify
from random import randint
from app.models import CustomerDetails, EmailTemplates
from app import db, mail


class Customers:

    # function to add new customer in the list
    def add_customer(self):
        try:
            name = self.get('customer_name')
            email = self.get('customer_email')
            cost = self.get('total_shopping_by_customer')
            cus = CustomerDetails(name, email, cost)
            db.session.add(cus)
            db.session.commit()
            return "Created new user with name {}".format(name)
        except Exception:
            return "Some Error occurred"

    # function to get details of any customer by customer name
    def get_customer_details(self):
        try:
            user = CustomerDetails.query.filter_by(customer_name=self.get('customer_name')).first()
            return jsonify(user.serialize())
        except Exception:
            return 'No user found with given name'

    # function to update details of any customer
    def update_customer_details(self):
        try:
            customer_name = self.get('customer_name')
            new_customer_name = self.get('new_customer_name')
            new_totol_shopping_by_customer = self.get('new_total_shopping_by_customer')
            user = CustomerDetails.query.filter_by(customer_name=customer_name).first()
            statement = ""
            user.customer_name = new_customer_name
            statement += 'customer_name updated from {} to {}. '.format(customer_name, new_customer_name)
            assert isinstance(new_totol_shopping_by_customer, object)
            user.total_shopping_by_customer = (int(new_totol_shopping_by_customer))
            db.session.commit()
            statement += 'and shopping value updated to {}'.format(new_totol_shopping_by_customer)
            return statement
        except Exception:
            return 'No user found with given name'

    # function to delete customer with given email
    def delete_customer_details(self):
        try:
            customer_email = self.get('customer_email')
            CustomerDetails.query.filter_by(customer_email=customer_email).delete()
            db.session.commit()
            return 'customer deleted with email: {}'.format(customer_email)
        except Exception:
            return 'No user found with given email'


class EmailTemplate:

    # function to add new email template
    def add_email_template(self):
        try:
            email_type = self.get('email_type')
            title = self.get('title')
            email_content = self.get('email_content')
            is_template_approved = True
            email_template = EmailTemplates(email_type, title, is_template_approved, email_content)
            db.session.add(email_template)
            db.session.commit()
            return "Created new email template"
        except Exception:
            return "Some error occurred"

    # function to get email template of given email type
    def get_email_template(self):
        try:
            email_template = EmailTemplates.query.filter_by(email_type=self.get('email_type')).filter_by(
                title=self.get('title')).first()
            return email_template.email_content
        except Exception:
            return 'No email template found with given email type'

    # function to update email template of given email type
    def update_email_template(self):
        try:
            email_type = self.get('email_type')
            title = self.get('title')
            new_email_content = self.get('new_email_content')
            email_template = EmailTemplates.query.filter_by(email_type=email_type).filter_by(title=title).first()
            statement = ""
            email_template.email_content = new_email_content
            statement += 'Template of email type - {} is updated'.format(email_type)
            db.session.commit()
            return statement
        except Exception:
            return 'Some Error occurred'

    # function to delete email template
    def delete_email_template(self):
        try:
            email_type = self.get('email_type')
            title = self.get('title')
            EmailTemplates.query.filter_by(email_type=email_type).filter_by(title=title).delete()
            db.session.commit()
            return 'Template of type {} with title {} is deleted'.format(email_type, title)
        except Exception:
            return 'Some Error Occurred'


class SendEmail:

    # function to send mail to the customers
    def send_email_to_customer(self):
        try:
            email_type = self.get('email_type')
            title = self.get('title')
            email_template = EmailTemplates.query.filter_by(email_type=email_type).filter_by(title=title).first()
            email_content = email_template.email_content
            emails = CustomerDetails.query.with_entities(CustomerDetails.customer_email).all()
            # for sending dynamic mails
            if email_type == 'dynamic':
                customer_names = CustomerDetails.query.with_entities(CustomerDetails.customer_name).all()
                total_shopping_by_customer = CustomerDetails.query.with_entities(
                    CustomerDetails.total_shopping_by_customer).all()
                email_name_dict = dict(zip(emails, customer_names))
                email_cost_dict = dict(zip(emails, total_shopping_by_customer))
                for email in emails:
                    customer_name = email_name_dict.get(email)
                    cost = email_cost_dict.get(email)
                    coupan_code = randint(1000000, 1000000000)
                    email_content = email_template.email_content
                    email_content = email_content.format(customer_name[0], str(cost[0]), str(coupan_code))
                    msg = Message(sender="markmail@hashedin.com", recipients=[email[0]], html=email_content)
                    mail.send(msg)
            # for sending static mails
            else:
                email_list = []
                for email in emails:
                    email_list.append(email[0])
                msg = Message(sender="markmail@hashedin.com", recipients=email_list, html=email_content)
                mail.send(msg)
            return "Mail Sent"
        except Exception:
            return "Some error occurred"




