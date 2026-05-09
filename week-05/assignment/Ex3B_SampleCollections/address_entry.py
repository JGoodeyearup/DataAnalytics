contact_info = {
    "name": "Michael Jackson", 
    "street": "2300 Jackson Street", 
    "city": "Gary", 
    "state": "Indiana",
    "zip": "46303" 
    }

full_name = {
    "first_name": "Michael",
    "last_name": "Jackson"
}

full_name.update({"honorific": "Mr."})

print(f"Hello special fan, \nif you would like to send a letter to {full_name['honorific']} {full_name['first_name']} {full_name['last_name']}, \nyou can mail it to: \n{contact_info['street']}, \n{contact_info['city']}, \n{contact_info['state']}, \n{contact_info['zip']}.")

