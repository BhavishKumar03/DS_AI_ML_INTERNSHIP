contacts = {
    "Bhavish": 9876543210,
    "Dilan": 9123456780,
    "Adithya": 9988776655
}
contacts["Karthik"] = 9011223344
contacts["Bhavish"] = 9998887776
existing_contact = contacts.get("Dilan", "Contact not found")
missing_contact = contacts.get("Rohan", "Contact not found")

print("Safe Lookup Results:")
print("Dilan:", existing_contact)
print("Rohan:", missing_contact)
print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")