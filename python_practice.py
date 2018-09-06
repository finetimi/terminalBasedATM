from bank import *
from accounts import *
from atm import *

def main():
    manager = ManagerPanel()
    return manager.processing()

main()

# dict = {"Name" : "Cristiano", "Age": 24, "Phone Number": "802-456-1234"}
#
# for key, value in dict.items():
#     header = key
#     value = value
#     print(value)
