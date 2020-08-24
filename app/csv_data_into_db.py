# ----------- To receive CSV file, read the data from CSV file and populate the data into Database-----------
import codecs
import csv
from app import db
from app.models import CustomersCSV, OrderCSV, ProductCSV, ReviewsCSV, UserProductList


class CSVDataIntoDb:

    # function for customer_csv
    def customers_csv(self):
        try:
            stream = codecs.iterdecode(self.stream, 'utf-8')
            row_count = 0
            for row in csv.reader(stream, dialect=csv.excel):
                if row_count == 0:
                    row_count += 1
                else:
                    id = row[0]
                    first_name = row[1]
                    last_name = row[2]
                    gender = row[3]
                    email = row[4]
                    age = row[5]
                    address = row[6]
                    state = row[7]
                    zipcode = row[8]
                    phone_number = row[9]
                    registration_date = row[10]
                    data = CustomersCSV(id=int(id), first_name=first_name, last_name=last_name, gender=gender,
                                        email=email,
                                        age=int(age), address=address, state=state, zipcode=int(zipcode),
                                        phone_number=phone_number, registration_date=registration_date)
                    db.session.add(data)
                    db.session.commit()
            return 'CSV data populated into database successfully'
        except Exception:
            return 'Some Error Occurred'

    # function for order_csv
    def order_csv(self):
        try:
            stream = codecs.iterdecode(self.stream, 'utf-8')
            row_count = 0
            for row in csv.reader(stream, dialect=csv.excel):
                if row_count == 0:
                    row_count += 1
                else:
                    id = row[0]
                    purchase_date = row[1]
                    total_price = row[2]
                    data = OrderCSV(id=int(id), purchase_date=purchase_date, total_price=int(total_price))
                    db.session.add(data)
                    db.session.commit()
            return 'CSV data populated into database successfully'
        except Exception:
            return 'Some Error Occurred'

    # function for product_csv
    def product_csv(self):
        try:
            stream = codecs.iterdecode(self.stream, 'utf-8')
            row_count = 0
            for row in csv.reader(stream, dialect=csv.excel):
                if row_count == 0:
                    row_count += 1
                else:
                    id = row[0]
                    sku = row[1]
                    product_name = row[2]
                    brand = row[3]
                    product_description = row[4]
                    color = row[5]
                    unit_price = row[6]
                    data = ProductCSV(id=int(id), sku=int(sku), product_name=product_name, brand=brand,
                                      product_description=product_description, color=color, unit_price=int(unit_price))
                    db.session.add(data)
                    db.session.commit()
            return 'CSV data populated into database successfully'
        except Exception:
            return 'Some Error Occurred'

    # function for review_csv
    def reviews_csv(self):
        try:
            stream = codecs.iterdecode(self.stream, 'utf-8')
            row_count = 0
            for row in csv.reader(stream, dialect=csv.excel):
                if row_count == 0:
                    row_count += 1
                else:
                    id = row[0]
                    user_product_id = row[1]
                    product_rating = row[2]
                    review_title = row[3]
                    review_details = row[4]
                    data = ReviewsCSV(id=int(id), user_product_id=int(user_product_id),
                                      product_rating=int(product_rating),
                                      review_title=review_title, review_details=review_details)
                    db.session.add(data)
                    db.session.commit()
            return 'CSV data populated into database successfully'
        except Exception:
            return 'Some Error Occurred'

    # function for user_product_list_csv
    def user_product_list_csv(self):
        try:
            stream = codecs.iterdecode(self.stream, 'utf-8')
            row_count = 0
            for row in csv.reader(stream, dialect=csv.excel):
                if row_count == 0:
                    row_count += 1
                else:
                    id = row[0]
                    user_id = row[1]
                    product_id = row[2]
                    quantity = row[3]
                    orderid = row[4]
                    data = UserProductList(id=int(id), user_id=int(user_id), product_id=int(product_id),
                                           quantity=int(quantity), orderid=int(orderid))
                    db.session.add(data)
                    db.session.commit()
            return 'CSV data populated into database successfully'
        except Exception:
            return 'Some Error Occurred'
