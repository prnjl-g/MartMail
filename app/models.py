from app import db


class CustomerDetails(db.Model):
    customer_unique_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), index=True, nullable=False)
    customer_email = db.Column(db.String(200), index=True, unique=True, nullable=False)
    total_shopping_by_customer = db.Column(db.Integer, index=True, nullable=False)

    __tablename__ = 'customer_details'

    def __init__(self, customer_name, customer_email, total_shopping_by_customer):
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.total_shopping_by_customer = total_shopping_by_customer

    def serialize(self):
        return {
            'customer_unique_id': self.customer_unique_id,
            'customer_name': self.customer_name,
            'customer_email': self.customer_email,
            'total_shopping_by_customer': self.total_shopping_by_customer
        }

    def __repr__(self):
        return '<CustomerDetails {}>'.format(self.customer_name)


class EmailTemplates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_type = db.Column(db.String(30), index=True, nullable=False)
    title = db.Column(db.String(30), index=True, nullable=False, unique=True)
    is_template_approved = db.Column(db.Boolean, index=True, nullable=False)
    email_content = db.Column(db.String(5000), index=True, nullable=False)

    __tablename__ = 'email_templates'

    def __init__(self, email_type, title, is_template_approved, email_content):
        self.email_type = email_type
        self.title = title
        self.is_template_approved = is_template_approved
        self.email_content = email_content

    def __repr__(self):
        return '<EmailTemplates {}>'.format(self.email_type)


class CustomersCSV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), index=True, nullable=False)
    last_name = db.Column(db.String(30), index=True, nullable=False)
    gender = db.Column(db.String(30), index=True, nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    age = db.Column(db.Integer, index=True, nullable=False)
    address = db.Column(db.String(500), index=True, nullable=False)
    state = db.Column(db.String(30), index=True, nullable=False)
    zipcode = db.Column(db.Integer, index=True, nullable=False)
    phone_number = db.Column(db.String(30), index=True, nullable=False)
    registration_date = db.Column(db.String(30), nullable=False)

    __tablename__ = 'customer_csv'

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'email': self.email,
            'age': self.age,
            'address': self.address,
            'state': self.state,
            'zipcode': self.zipcode,
            'phone_number': self.phone_number,
            'registration_date': self.registration_date
        }


class OrderCSV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.String(30), index=True, nullable=False)
    total_price = db.Column(db.Integer, index=True, nullable=False)

    __tablename__ = 'order_csv'


class ProductCSV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(30), index=True, nullable=False)
    product_name = db.Column(db.String(100), index=True, nullable=False)
    brand = db.Column(db.String(30), index=True, nullable=False)
    product_description = db.Column(db.String(10000), index=True, nullable=False)
    color = db.Column(db.String(30), index=True, nullable=False)
    unit_price = db.Column(db.Integer, index=True, nullable=False)

    __tablename__ = 'product_csv'


class ReviewsCSV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_product_id = db.Column(db.Integer, index=True, nullable=False)
    product_rating = db.Column(db.Integer, index=True, nullable=False)
    review_title = db.Column(db.String(30), index=True, nullable=False)
    review_details = db.Column(db.String(300), index=True, nullable=False)

    __tablename__ = 'review_csv'


class UserProductList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True, nullable=False)
    product_id = db.Column(db.Integer, index=True, nullable=False)
    quantity = db.Column(db.Integer, index=True, nullable=False)
    orderid = db.Column(db.Integer, index=True, nullable=False)

    __tablename__ = 'user_product_list_csv'
