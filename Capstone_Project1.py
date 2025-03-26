#Menu display can be changed however you see fit
def menu():
    print("Big Jim & Co.'s Car Rental\n======================================\n")
    print("1. Show Auto Products")
    print("2. Rent Auto Products")
    print("3. Add New Product")
    print("4. Update Existing Product")
    print("5. Delete Product")
    print("0. Exit")
    print("\n")

List_Barang = ["Chevrolet Cruze","Nissan Altima","Toyota Corolla","Toyota Camry","Chrysler 200"] #Insert product name here
List_Stok = [5,10,7,3,8] #Insert available stock here
List_Harga = [44.99,40.75,47.99,67.33,84.99] #Insert prices here

def productlist():
    print("\n")
    print("    No. | Vehicle Name\t\t| Stock\t| Rate/day\n")
    for i,option in enumerate(List_Barang):
        print("{:5}\t| {:15}\t| {:<3}\t| ${} /day.".format(i+1,option,List_Stok[i],List_Harga[i])) #You may change your product list display here

menu()
option = int(input("Select Option: "))

while option !=0:
    if option == 1:
        productlist()
    elif option == 2:
        Rent_CustomerName = input("Your Name: ")
        Rent_CustomerNumber = input("Your Contact Information (Phone Number): ")
        productlist()
        Rent_ProductName = int(input("Select Product Index Choice: "))-1
        Rent_ProductTime = int(input("Select Amount of Days to Rent: "))

        print(f"You will be renting {List_Barang[Rent_ProductName]} for {Rent_ProductTime} days")
        print("Confirm?")
        Confirmation = input("Type (Yes) to confirm, Type (No) to cancel ")
        if Confirmation.upper() == "YES":
            print(f"Thank You {Rent_CustomerName}, we shall contact {Rent_CustomerNumber} for confirmation within 3 business days during business hour")
        else:
            print("Rental Cancelled")
    elif option == 3:
        Password = input("Enter Password: ")
        if Password == "BigJim4499": #Change Password here
            New_ProductName = input("Insert Product Here: ")
            List_Barang.append(New_ProductName)
            New_ProductName_Stock = int(input("Insert Number of Product Here: "))
            List_Stok.append(New_ProductName_Stock)
            New_ProductName_Price = float(input("Insert New Product Price Here: "))
            List_Harga.append(New_ProductName_Price)
            productlist()
        else:
            print("Incorrect Password")
    elif option == 4:
        Password = input("Enter Password: ")
        if Password == "BigJim4499": #Change Password here
            ChooseUpdate_Product = int(input("Insert Product Index Choice to Update: "))-1
            Update_ProductStock = input("Insert Stock Update (If no update, insert'-'): ")
            if Update_ProductStock != "-":
                List_Stok[(ChooseUpdate_Product)]=int(Update_ProductStock)
            Update_ProductPrice = (input("Insert Price Update (If no update, insert'-'): "))
            if Update_ProductPrice != "-":
                List_Harga[(ChooseUpdate_Product)]=float(Update_ProductPrice)
            productlist()
        else:
            print("Incorrect Password")
    elif option == 5:
        Password = input("Enter Password: ")
        if Password == "BigJim4499": #Change Password here
            Remove_ProductName = int(input("Insert Product Index Choice to Delete: "))-1
            del List_Barang[Remove_ProductName]
            del List_Stok[Remove_ProductName]
            del List_Harga[Remove_ProductName]
            productlist()
        else:
            print("Incorrect Password")
    else:
        print("\nInvalid input")
    
    print()
    menu()
    option = int(input("Select Option: "))
print("Operation Concluded, Goodbye")
