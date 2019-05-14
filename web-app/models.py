from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name=db.Column(db.String(200), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(200), unique=False, nullable=False)
    address=db.Column(db.Text, unique=False, nullable=False)
    mobile_no=db.Column(db.String(20), unique=False, nullable=False)
    # birthday=db.Column(db.Date, unique=False, nullable=False)
    gender=db.Column(db.String(10), unique=False, nullable=False)

    def __init__(self, username, name, email, password, address, mobile_no, gender):
        self.username=username;
        self.email=email
        self.password=password
        self.name=name
        self.gender=gender
        self.address=address
        self.mobile_no=mobile_no
        # self.birthday=birthday
    def __repr__(self):
        return '<User %r>' % self.username


class Articles(db.Model):
    def __init__(self, art_username, article_title, article_body):
        self.art_username=art_username
        self.article_title=article_title
        self.article_body=article_body
    def __getitem__(self, item):
        return getattr(self, item)
    id = db.Column(db.Integer, primary_key=True)
    art_username = db.Column(db.String(80), db.ForeignKey('user.username'))
    article_title=db.Column(db.String(500), unique=False, nullable=False)
    article_body=db.Column(db.Text, unique=False, nullable=True)
    created_date =db.Column(db.DateTime(timezone=True), primary_key=False, nullable=False, default=time_now)
