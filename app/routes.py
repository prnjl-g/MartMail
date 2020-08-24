from app import app
from flask import request
from app.db_ import Customers, EmailTemplate, SendEmail
from app.filters import FilterCustomerList
from app.csv_data_into_db import CSVDataIntoDb


# ------- API for CRUD operation on customer_details table------------
@app.route('/customer', methods=['POST', 'GET', 'PUT', 'DELETE'])
def customer():
    content = request.json
    if request.method == 'POST':
        statement = Customers.add_customer(content)
        return statement

    elif request.method == 'GET':
        statement = Customers.get_customer_details(content)
        return statement

    elif request.method == 'PUT':
        statement = Customers.update_customer_details(content)
        return statement

    elif request.method == 'DELETE':
        statement = Customers.delete_customer_details(content)
        return statement


# ------------API to Store new email template and perform CRUD operation on email template table------------
@app.route('/email', methods=['POST', 'GET', 'PUT', 'DELETE'])
def email_template():
    content = request.json
    if request.method == 'POST':
        statement = EmailTemplate.add_email_template(content)
        return statement

    elif request.method == 'GET':
        statement = EmailTemplate.get_email_template(content)
        return statement

    elif request.method == 'PUT':
        statement = EmailTemplate.update_email_template(content)
        return statement

    elif request.method == 'DELETE':
        statement = EmailTemplate.delete_email_template(content)
        return statement

# -------API to send emails to the list of Customers-------------
@app.route('/sendemail', methods=['POST'])
def send_email():
    content = request.json
    statement = SendEmail.send_email_to_customer(content)
    return statement

#-------API to accept CSV file and populate the data of CSV into Database------------
@app.route('/csv_file/<file_name>', methods=['POST'])
def csv_file(file_name):
    csv = request.files['file']
    if not csv:
        return 'Please upload CSV file'
    if file_name == 'customers':
        return CSVDataIntoDb.customers_csv(csv)

    elif file_name == 'order':
        return CSVDataIntoDb.order_csv(csv)

    elif file_name == 'product':
        return CSVDataIntoDb.product_csv(csv)

    elif file_name == 'reviews':
        return CSVDataIntoDb.reviews_csv(csv)

    elif file_name == 'userproductlist':
        return CSVDataIntoDb.user_product_list_csv(csv)

    else:
        return "Please enter correct file name"

# -----------API to get the list of filtered customer on the basis of different parameters--------------
@app.route('/filter_customer', methods=['GET'])
def filter_customer():
    content = request.json
    if content.get('filter_column') == 'first_name':
        return FilterCustomerList.using_first_name(content)
    elif content.get('filter_column') == 'gender':
        return FilterCustomerList.using_gender(content)
    elif content.get('filter_column') == 'state':
        return FilterCustomerList.using_state(content)
    elif content.get('filter_column') == 'email':
        return FilterCustomerList.using_email(content)
    elif content.get('filter_column') == 'age':
        return FilterCustomerList.using_age(content)
    else:
        return "Please enter valid filter"
