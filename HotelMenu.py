#Define the menu of restaurent
menu= {
    'Chay':30,
    'Biryani':120,
    'Pizza':50,
    'Pasta':40,
    'Burgur':60,
    'salad':30,
    'Coffee':80,
}
#Greet
print("Welcom to IES Restaurent!")
print("Chay: 30\nBiryani: 120\nPizza: 50\nPasta: 40\nBurgur: 60\nsalad: 30\nCoffee: 80")

order_Total=0
item1 =input("Enter the name of item You want to order :")

if item1 in menu:

    order_Total += menu[item1]
    print(f"Your item {item1} has  been added to your order:")

else:

    print("Ordered item {item1} is not available please order something else!!")

Another_Item=input( "Do you want to add another item:    (Yes/No) " ) 

if Another_Item == "Yes":

    item_2=input("Enter the Name of second item : ")

    if item_2 in menu:

        order_Total += menu[item_2]
        print("Item {item2 } has been added in order!")

    else:
        print(f"item {item_2}is not available!")

print(f"The total Amount of the items to pay is {order_Total}")
print("ThankYou!")
