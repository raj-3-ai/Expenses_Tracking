expenses=[]
def add_expenses():
    name=input("Enter the expenses:")
    amount=float(input("Enter the amount:"))
    catogory=input("Enter the catogory:")
    
    expense={
        "Name":name,
        "Amount":amount,
        "Catogory":catogory
    }

    expenses.append(expense)
    print("expenses added")

def veiw_expenses():
    for e in expenses:
        print(e["Name"],e["Amount"],e["Catogory"])
def Total_expenses():
    total=0
    for a in expenses:
        total+=a["Amount"]
    print("Total Amount:",total)
def Category_summary():
    summary={}
    for i in expenses:
        cat=i["Catogory"]
        amo=i["Amount"]
        if cat in summary:
            summary[cat]+=amo
        else:
            summary[cat]=amo
    print(summary)        
while True:
    print("\n Expenses Tracking")
    print("1.Add Expenses")
    print("2.Veiw Expenses")
    print("3.Total Spending")
    print("4.category summary")
    print("5.Exit")
    choice=input("choose:")
    if choice=="1":
        add_expenses()
    elif choice=="2":
        veiw_expenses()
    elif choice=="3":
        Total_expenses()
    elif choice=="4":
        Category_summary()
    elif choice=="5":
        break    