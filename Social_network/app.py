from flask import Flask,request,jsonify
from socialapp.Model.model import db ,User

app = Flask(__name__)

app.secret_key = "|ZWszK=T:T;B|qW@"
app.config['MONGODB_SETTINGS'] = {
    'db': 'socialnetwork',
    'host': 'localhost',
    'port': 27017
}
db.init_app(app)

@app.route("/fetch_friends/<user_id>")
def fetch_friends(user_id): 
    friend_list = User().fetch_friend_list(user_id)
    return jsonify({"friends":friend_list})

if __name__ == '__main__':
    app.run(port=5000,debug=True)