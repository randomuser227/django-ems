from django.contrib.auth import authenticate

user = authenticate(username="admin", password="asd")

if user is not None:
   print("approved")
else:
    print("not authenticated")