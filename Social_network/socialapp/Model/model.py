from mongoengine import  Document, StringField, DateTimeField , ListField, ReferenceField
from flask_mongoengine import MongoEngine
from bson.objectid import ObjectId
import datetime ,json
db = MongoEngine()


class User(db.Document):
    username = StringField(required=True, max_length=100, unique=True)
    friends = ListField()
    created_on = db.DateTimeField(default=datetime.datetime.now)


    def fetch_friend_list(self, user_id):
        friend_list = []
        data = User.objects(id=user_id).get().to_json()
        data = json.loads(data)
        for id in data['friends']:
            friend = User.objects(id=id).get().to_json()
            friend = json.loads(friend)
            friend_list.append(friend['username'])
        return friend_list


class Post(db.Document):
    title = StringField(required=True, max_length=100,)
    content = StringField(required=True)
    posted_on = DateTimeField(default=datetime.datetime.now)
    user_id = ReferenceField(User)


class Comments(db.Document):
    commented_by = ReferenceField(User)
    comments = StringField(required=True, max_length=100,)
    post_id = ReferenceField(Post)


    


