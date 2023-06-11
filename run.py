from data import *
from generator import generate_password

password_length = int(input("\n How long should the password be : "))

data = alphabet + numbers + special_characters
password = generate_password(password_length, data)
print("\n your password => {}\n".format(password))
