dict={"Adithya":23,"Kumar":25,"Ravi":22}
print("Original Dictionary:",dict)

student={"name":"Adithya","age":22,"course":"Engineering"}
print(student["name"])
student["age"]=23
student["city"]="Delhi"
print(student)

marks={"Maths":80,"Science":75,"English":85}
print(marks.get("Maths"))
print(marks.get("History",0))
for subject,score in marks.items():
    print(subject,score)
marks.update({"History":70})
print(marks)
marks.pop("Science")
print(marks)

purchases={"Alice":250,"Bob":400,"Charlie":150}
for name,amount in purchases.items():
    print(f"{name} made a purchase of ₹{amount}")

print("Total Customers:",len(purchases))
print("Customer Names:",purchases.keys())

print("Alice's purchases",purchases.get("Alice",0))

n=int(input("Enter number of customers:"))
user_purchases={}
for _ in range(n):
    name=input("Enter customer name:")
    amount=int(input(f"Enter purchase amount for {name}:"))
    user_purchases[name]=amount
print("Customer Purchase Data:",user_purchases)

top_customer=max(purchases,key=purchases.get)
print("Top Spending Customer:",top_customer)

lowest_customer=min(purchases,key=purchases.get)
print("Lowest Spending Customer:",lowest_customer)

A={1,2,3}
B={3,4,5}
print("Union:",A|B)
print("Intersection:",A&B)
print(3 in A)