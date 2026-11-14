import json

class Contact_Book:

    def __init__ (self):
        self.name = " "
        self.number =" "

    def get_input(self):
        self.name = input("Enter the name: ")
        self.number = int(input("Enter the number: ")) 

class Store_data:
        
        def add_contact(self,Contact):

            #Reads "data.json" file and writes existing data into python object
            with open ("Contact_Book\\data.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            data.append({
                 "Name" : Contact.name,
                 "Number" : Contact.number
            })

            #Save updated data into "data.json"
            with open("Contact_Book\\data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

User = Contact_Book()
User.get_input()

Contact = Store_data()
Contact.add_contact(User)