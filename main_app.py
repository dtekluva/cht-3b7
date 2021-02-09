from database_manager import DBMan # IMPORT THE CLASS CREATED FOR DB INTERACTION

def login(username, password):
    user = database.read_from_db(f"SELECT * FROM member WHERE username = '{username}' and password = '{password}'", fetchall= False) # USE DB CLASS TO DEND QUERY TO DATABASE 

    if user:
        print("LOGIN SUCCESSFUL. !!!\n\n")
        print(f'Welcome {user["name"]}, \nyou are {user["age"]} years old. Please continue. \n\n')
        return user
    else:
        print("LOGIN FAILED. !!!\n\n")
        return False

def read_and_display_note(member_id):

    entries = database.read_from_db(f"select * from entry where memberid = {member_id}", fetchall= True) # USE DB CLASS TO DEND QUERY TO DATABASE NOTE THE FACT THAT FETCHALL IS TRUE WHICH WILL GIVE BACK ALL THE RESULTS FOUND

    print("######################")
    print("###### NOTES #########")
    print("######################\n\n")

    for index, entry in enumerate(entries):
        print(index, " - ", entry.get("title").upper())

    action = input("Please enter note index to read : ")

    for index, entry in enumerate(entries):

        if index == int(action):
            print("Title : ", entry.get("title").upper(), "\n")
            print("Created on : ", str(entry.get("dateadded")), "\n\n")
            print(entry.get("body"))
    

database = DBMan("localhost", "root", "", "journal")

username = input("Please enter username > ")
password = input("Please enter password > ")

user_details = login(username, password)

action = input("Please what would you like to do : ")

if action == "read":
    read_and_display_note(user_details["id"])
else:
    print("NO VALID ACTION SELECTED.")

print("END OF PROGRAM")