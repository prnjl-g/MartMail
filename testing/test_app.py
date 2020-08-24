import json
import os
import unittest
from io import BytesIO
from app import app, db
from app.models import CustomerDetails, EmailTemplates
from config import basedir


class TestCustomer(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_customer(self):
        c = CustomerDetails("bobby", "bobby@hashedin.com", 1189)
        db.session.add(c)
        db.session.commit()
        c = CustomerDetails.query.all()
        self.assertEqual(c[0].customer_name, "bobby")

    def test_update_customer_details(self):
        data = {
            "customer_name": "bobby",
            "new_customer_name": "boby",
            "new_total_shopping_by_customer": "200"
        }
        response = self.app.put('/customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'No user found with given name')

    def test_get_customer_details(self):
        data = {
            "customer_name": "boby"
        }
        response = self.app.get('/customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'No user found with given name')

    def test_delete_customer_details(self):
        data = {
            "customer_email": "bobby@hashdedin.com"
        }
        response = self.app.delete('/customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'customer deleted with email: bobby@hashdedin.com')

    def test_customer_api(self):
        data = {
            "customer_name": "bobby",
            "customer_email": "bobby@hashdedin.com",
            "total_shopping_by_customer": "10000"
        }
        response = self.app.post('/customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Created new user with name bobby')

        data = {
            "customer_name": "bobby"
        }
        response = self.app.get('/customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,
                         b'{\n  "customer_email": "bobby@hashdedin.com", \n  "customer_name": "bobby", \n  "customer_unique_id": 1, \n  "total_shopping_by_customer": 10000\n}\n')

        data = {
            "customer_name": "bobby",
            "new_customer_name": "boby",
            "new_total_shopping_by_customer": "200"
        }
        response = self.app.put('/customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'customer_name updated from bobby to boby. and shopping value updated to 200')

        data = {
            "customer_email": "bobby@hashdedin.com"
        }
        response = self.app.delete('/customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'customer deleted with email: bobby@hashdedin.com')

        data = {
            "custoer_name": "bobby",
            "customer_email": "bobby@hashdedin.com",
            "total_shopping_by_customer": "10000"
        }
        response = self.app.post('/customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Some Error occurred')

        data = {
            "customer_name": "bobby"
        }
        response = self.app.get('/customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'No user found with given name')

        data = {
            "customer_name": "bobby",
            "new_customer_name": "boby",
            "new_total_shopping_by_customer": "200"
        }
        response = self.app.put('/customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'No user found with given name')


class TestSendEmail(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_send_email_to_customer(self):
        data = {
            "email_type": "static",
            "title": "Thank you"
        }
        response = self.app.post('/sendemail', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Some error occurred')
        data = {
            "email_type": "dynamic",
            "title": "Thank you"
        }
        response = self.app.post('/sendemail', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Some error occurred')

    def test_send_mail_api(self):
        data = {
            "email_type": "static",
            "title": "Thank you"
        }
        response = self.app.post('/sendemail', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Some error occurred')
        data = {
            "email_type": "dynamic",
            "title": "Thank you"
        }
        response = self.app.post('/sendemail', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Some error occurred')


class TestEmailTemplate(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_email_template(self):
        c = EmailTemplates("static", "Thank you", True,
                           "<html><body><h1>Thank You</h1><p>Hi, <br/>Thank you for being a part of our family. Hope you will have a nice experience with us. <br/> For any queries visit our site.<br/> Thank You <br/>HU2K20.com</p></body></html>")
        db.session.add(c)
        db.session.commit()
        c = EmailTemplates.query.all()
        self.assertEqual(c[0].email_type, "static")

    def test_get_email_template(self):
        data = {
            "email_type": "static",
            "title": "Thank you"
        }
        response = self.app.get('/email', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'No email template found with given email type')

    def test_update_email_template(self):
        data = {
            "email_type": "static",
            "title": "Thank you",
            "email_content": "<html><body><h1>Thank</h1><p>Hi, <br/>Thank you for being a part of our family. Hope you will have a nice experience with us. <br/> For any queries visit our site.<br/> Thank You <br/>HU2K20.com</p></body></html>"
        }
        response = self.app.put('/email', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Some Error occurred')

    def test_delete_email_template(self):
        data = {
            "email_type": "static",
            "title": "Thank you"
        }
        response = self.app.delete('/email', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Template of type static with title Thank you is deleted')

    def test_email_template_api(self):
        data = {
            "email_type": "static",
            "title": "Thank you",
            "email_content": "<html><body><h1>Thank You</h1><p>Hi, <br/>Thank you for being a part of our family. Hope you will have a nice experience with us. <br/> For any queries visit our site.<br/> Thank You <br/>HU2K20.com</p></body></html>"
        }
        response = self.app.post('/email', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = {
            "email_type": "static",
            "title": "Thank you"
        }
        response = self.app.get('/email', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = {
            "email_type": "static",
            "title": "Thank you",
            "email_content": "<html><body><h1>Thank</h1><p>Hi, <br/>Thank you for being a part of our family. Hope you will have a nice experience with us. <br/> For any queries visit our site.<br/> Thank You <br/>HU2K20.com</p></body></html>"
        }
        response = self.app.put('/email', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = {
            "email_type": "static",
            "title": "Thank you"
        }
        response = self.app.delete('/email', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = {
            "emai_type": "static",
            "title": "Thank you",
            "email_content": "<html><body><h1>Thank You</h1><p>Hi, <br/>Thank you for being a part of our family. Hope you will have a nice experience with us. <br/> For any queries visit our site.<br/> Thank You <br/>HU2K20.com</p></body></html>"
        }
        response = self.app.post('/email', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Some error occurred')

        data = {
            "email_type": "static",
            "title": "Thank you"
        }
        response = self.app.get('/email', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'No email template found with given email type')

        data = {
            "email_type": "static",
            "title": "Thank you",
            "email_content": "<html><body><h1>Thank</h1><p>Hi, <br/>Thank you for being a part of our family. Hope you will have a nice experience with us. <br/> For any queries visit our site.<br/> Thank You <br/>HU2K20.com</p></body></html>"
        }
        response = self.app.put('/email', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Some Error occurred')


class TestFilterCustomer(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_using_first_name(self):
        data = {
            "filter_column": "first_name",
            "contain": "a"
        }
        response = self.app.get('/filter_customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_using_gender(self):
        data = {
            "filter_column": "gender",
            "gender": "Male"
        }
        response = self.app.get('/filter_customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_using_email(self):
        data = {
            "filter_column": "email",
            "email_end": "net"
        }
        response = self.app.get('/filter_customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_using_age(self):
        data = {
            "filter_column": "age",
            "upto_age": "25"
        }
        response = self.app.get('/filter_customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_using_state(self):
        data = {
            "filter_column": "state",
            "state": "Kansas"
        }
        response = self.app.get('/filter_customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_filter_customer_api(self):
        data = {
            "filter_column": "first_name",
            "contain": "ab"
        }
        response = self.app.get('/filter_customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = {
            "filter_column": "gender",
            "gender": "Male"
        }
        response = self.app.get('/filter_customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = {
            "filter_column": "state",
            "state": "Kansas"
        }
        response = self.app.get('/filter_customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = {
            "filter_column": "email",
            "email_end": "net"
        }
        response = self.app.get('/filter_customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = {
            "filter_column": "age",
            "upto_age": "25"
        }
        response = self.app.get('/filter_customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = {
            "filter_column": "firt_name",
            "contain": "ab"
        }
        response = self.app.get('/filter_customer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Please enter valid filter')


class TestCSVFile(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_customer_csv(self):
        data = {
            'field': 'value',
            'file': (BytesIO(b'FILE CONTENT'), 'customer.csv')
        }

        rv = self.app.post('/csv_file/customers', buffered=True, content_type='multipart/form-data', data=data)
        assert rv.status_code == 200
        self.assertEqual(rv.data, b'CSV data populated into database successfully')

    def test_order_csv(self):
        data = {
            'field': 'value',
            'file': (BytesIO(b'FILE CONTENT'), 'order.csv')
        }

        rv = self.app.post('/csv_file/order', buffered=True, content_type='multipart/form-data', data=data)
        assert rv.status_code == 200
        self.assertEqual(rv.data, b'CSV data populated into database successfully')

    def test_product_csv(self):
        data = {
            'field': 'value',
            'file': (BytesIO(b'FILE CONTENT'), 'product.csv')
        }

        rv = self.app.post('/csv_file/product', buffered=True, content_type='multipart/form-data', data=data)
        assert rv.status_code == 200
        self.assertEqual(rv.data, b'CSV data populated into database successfully')

    def test_review_csv(self):
        data = {
            'field': 'value',
            'file': (BytesIO(b'FILE CONTENT'), 'reviews.csv')
        }

        rv = self.app.post('/csv_file/reviews', buffered=True, content_type='multipart/form-data', data=data)
        assert rv.status_code == 200
        self.assertEqual(rv.data, b'CSV data populated into database successfully')

    def test_user_product_list_csv(self):
        data = {
            'field': 'value',
            'file': (BytesIO(b'FILE CONTENT'), 'userproductlist.csv')
        }

        rv = self.app.post('/csv_file/userproductlist', buffered=True, content_type='multipart/form-data', data=data)
        assert rv.status_code == 200
        self.assertEqual(rv.data, b'CSV data populated into database successfully')


    def test_csv_file_api(self):
        data = {
            'field': 'value',
            'file': (BytesIO(b'FILE CONTENT'), 'customer.csv')
        }

        rv = self.app.post('/csv_file/customers', buffered=True, content_type='multipart/form-data', data=data)
        assert rv.status_code == 200
        self.assertEqual(rv.data, b'CSV data populated into database successfully')

        data = {
            'field': 'value',
            'file': (BytesIO(b'FILE CONTENT'), 'order.csv')
        }

        rv = self.app.post('/csv_file/order', buffered=True, content_type='multipart/form-data', data=data)
        assert rv.status_code == 200
        self.assertEqual(rv.data, b'CSV data populated into database successfully')

        data = {
            'field': 'value',
            'file': (BytesIO(b'FILE CONTENT'), 'product.csv')
        }

        rv = self.app.post('/csv_file/product', buffered=True, content_type='multipart/form-data', data=data)
        assert rv.status_code == 200
        self.assertEqual(rv.data, b'CSV data populated into database successfully')

        data = {
            'field': 'value',
            'file': (BytesIO(b'FILE CONTENT'), 'reviews.csv')
        }

        rv = self.app.post('/csv_file/reviews', buffered=True, content_type='multipart/form-data', data=data)
        assert rv.status_code == 200
        self.assertEqual(rv.data, b'CSV data populated into database successfully')

        data = {
            'field': 'value',
            'file': (BytesIO(b'FILE CONTENT'), 'userproductlist.csv')
        }

        rv = self.app.post('/csv_file/userproductlist', buffered=True, content_type='multipart/form-data', data=data)
        assert rv.status_code == 200
        self.assertEqual(rv.data, b'CSV data populated into database successfully')
        self.assertEqual(self.app.post('/csv_file').status_code, 404)

        data = {
            'field': 'value',
            'file': (BytesIO(b'FILE CONTENT'), 'customer.csv')
        }

        rv = self.app.post('/csv_file/customer', buffered=True, content_type='multipart/form-data', data=data)
        assert rv.status_code == 200
        self.assertEqual(rv.data, b'Please enter correct file name')


if __name__ == "__main__":
    unittest.main()
