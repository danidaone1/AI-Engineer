#1. Contact Book (Dict + Lists)
#Use a dictionary where keys are names (strings) and values are lists of phone numbers.
#- Add, update, delete contacts.
#- Search by name (case insensitive).
#- Print all contacts sorted by name.
contact= {
    "alice":["1234"],
    "bob":["789"],
    "faraz":["456","000"],
    "cat":["1234","55667"]



        }
def add(name,phone):
    contact[name]=phone
def update(name,phone):
    contact.update({name:phone})
    
def delete(key):
    contact.pop(key)
    
def search(user_input):
    for x in contact:
        if user_input==x.lower() or x:
            return 
        

    pass
def display():
    for x,y in sorted(contact.items()):
        print(f"Name: {x} | Contact: {y} ")
update("bob",["567","352435"])
display()