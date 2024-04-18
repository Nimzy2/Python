contacts = []

with open("names.csv", "r") as file:
    lines = file.readlines()
    for line in lines:
        name,phone = line.rstrip().split(",")
        contact = {
            "Name": name,
            "Phone": phone  
        }
        contacts.append(contact)

contacts_sort = sorted(contacts, key=lambda x: x['Name'])
# print(contacts_sort)
for contact in contacts_sort:
    # name = contact["Name"]
    # phone = contact["Phone"]
    print(f'Hi {contact["Name"]}, Your phone number is {contact["Phone"]}')