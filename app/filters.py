# ----------to filter customer data on the basis of different columna and passed value-------------------

from flask import jsonify
from app.models import CustomersCSV


class FilterCustomerList:

    # function to filter using first name of user
    def using_first_name(self):
        try:
            contain = self.get('contain')
            print(contain)
            filtered_data = CustomersCSV.query.filter(CustomersCSV.first_name.ilike(f'%{contain}%')).all()
            return jsonify([i.serialize() for i in filtered_data])
        except Exception:
            return 'Some Error Occurred'

    # function to filter using gender column of customer table
    def using_gender(self):
        try:
            filtered_data = CustomersCSV.query.filter_by(gender=self.get('gender'))
            return jsonify([i.serialize() for i in filtered_data])
        except Exception:
            return 'Some error Occurred'

    # function to filter using email column of customer table
    def using_email(self):
        try:
            filtered_data = CustomersCSV.query.all()
            filtered_data_final = []
            for email in filtered_data:
                flag = email.email.endswith(self.get('email_end'))
                if flag:
                    filtered_data_final.append(email)
            return jsonify([i.serialize() for i in filtered_data_final])
        except Exception:
            return 'Some Error Occurred'

    # function to filter using age column of customer table
    def using_age(self):
        try:
            filtered_data = CustomersCSV.query.all()
            filtered_data_final = []
            for age in filtered_data:
                age_ = int(age.age)
                if age_ <= int(self.get('upto_age')):
                    filtered_data_final.append(age)
            return jsonify([i.serialize() for i in filtered_data_final])
        except Exception:
            return 'Some Error Occurred'

    # function to filter using state column of customer table
    def using_state(self):
        try:
            filtered_data = CustomersCSV.query.filter_by(state=self.get('state'))
            return jsonify([i.serialize() for i in filtered_data])
        except Exception:
            return 'Some error Occurred'
