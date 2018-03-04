import pyrebase
import base64

config = {
    "apiKey": "AIzaSyBwP1c6e5N4W8k3dl2tNJYROMCA7iIyODo",
    "authDomain": "eye-room.firebaseapp.com",
    "databaseURL": "https://eye-room.firebaseio.com",
    "storageBucket": "eye-room.appspot.com",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("brian.carlson1@uky.edu", "123456")
userIDToken = user['idToken']

with open("a.png", "rb") as imageFile:
    f = imageFile.read()
    ids = db.child("unanalyzed_images").push({"code": str(base64.urlsafe_b64encode(f)), "people": "Skeletor", "number": 1}, userIDToken)
with open("b.png", "wb") as newFile:
    r = db.child("unanalyzed_images").order_by_key().limit_to_last(1).get().val()
    p = list(r.keys())[0]
    newFile.write(base64.urlsafe_b64decode(eval(r[p]["code"])))