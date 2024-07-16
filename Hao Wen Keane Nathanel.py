your_cart = []

def menu():
    print("1.Show the sales available")
    print("2.Add item to cart")
    print("3.Show the cart")
    print("4.Edit ")
    print("5.Check out and Purchase")
    print("6.Exit")

def edit_cart():
    while True:
        for i, item in enumerate(your_cart):
            name = item['name']
            # price = item['price']
            qty = item['qty']
            print(f''' {i+1}. {name}   x{qty}  ''' )
        item_id = input('Which item to change: ')
        if not item_id.isdigit():
            print('\nInvalid input.\n')
            continue
        item_id = int(item_id)
        if item_id <=0:
            print('\nInvalid item choice.\n')
            continue
        rem_red = input("Remove the item or reduce quantity: 0/1:")
        if not rem_red.isdigit():
            print('\nInvalid input.\n')
            continue
        rem_red =int(rem_red)
        if rem_red == 0:
            del your_cart[item_id-1]
        elif rem_red == 1:
            red_qty = (input('How many pieces to reduce: '))
            if not red_qty.isdigit():
                print('\nInvalid input.\n')
                continue
            red_qty = int(red_qty)
            if red_qty <= 0:
                print('\nInvalid item choice.\n')
                continue
            if red_qty > your_cart[item_id - 1]['qty']:
                del your_cart[item_id - 1]
            else:
                your_cart[item_id - 1]['qty'] = your_cart[item_id - 1]['qty'] - red_qty
        while True:
            option = input('Enter 1 to edit more or 0 to go back main menu: ')
            if not option.isdigit():
                print('\nInvalid input.\n')
                continue
            else:
                break
        option = int(option)
        if option == 1:
            continue
        elif option == 0:
            break



def show_cart():
    print("     === SHOPPING LIST ===     ")

    list_length = len(your_cart)

    if list_length == 0:
        print("\nThe shopping list is empty.\n")

    else:
        print("No.          Item           Price")


        for i in range(list_length):
            item = your_cart[i]
            print(f"{i + 1}{item}")

def sale():
    print('''!!!!GUNDAM For Sale!!!!''')
    print(''' 
              ------------------------------
              |  No  |   |     Category    |
              |  1.  |   |  Perfect Grade  |
              |  2.  |   |   Real Grade    |
              |  3.  |   |   Master Grade  |
              |  4.  |   |  Mecha Girl     |
              |  5.  |   |   Motorized     |
              ------------------------------                        
    ''')
    items = []
    category_choice = input("Enter the category number to view items (or 'q' to quit): ")

    if category_choice == "q":
        return

    if category_choice == "1":
        print("\n==== Perfect Grade ====")

        items = [
            '''GUNDAM RAISER          $315.0''',
            '''Gundam SEED Astray     $320.0''',
            '''Wing Gundam            $350.0''',
            '''Freedom Gundam         $410.0''',
        ]

    elif category_choice == "2":
        print("\n==== Real Grade ====")

        items = [
            '''RG GoldyMarg           $52.00''',
            '''RG Gao Gai Gar         $78.00''',
            '''God Gundam             $58.00''',
            '''Wing Gundam Astray     $38.00''',


        ]

    elif category_choice == "3":
        print("\n==== Master Grade ====")

        items = [
            '''Eclipse Gundam      $195.00''',
            '''Full Saber          $72.00    ''',
            '''Unicorn Gundam      $64.00''',
            '''Gundam Dynames      $56.00''',
        ]

    elif category_choice == "4":
        print("\n==== Mecha Girl ====")

        items = [
            '''Messiah Ranka Lee    $95.0''',
            '''Ganesa               $20.0''',
            '''Arcanadea Lumitea    $75.0''',
            '''Tsubasa Kazanari     $90.0''',
        ]

    elif category_choice == "5":
        print("\n==== Motorized ====")

        items = [
            '''Little Ryan       $30.0''',
            '''Elephant Racer    $17.0''',
            '''Zoids Stylaser    $148.0''',
            '''Cannon Bull       $35.0''',
        ]

    else:
        print("Invalid choice.")
        return

    while True:
        print("\n!!!!GUNDAM For Sale!!!!")

        print('''|No|  |  Item   |    |  Price  |
-----------------------------------''')

        for i in range(len(items)):
            item = items[i]
            print(f"{i + 1}\t{item}")
        print()
        item_number = input("Enter the item number by id or 'q' to quit or 'b' to go back to toy catergories: ").lower()
        if item_number == '' and item_number != 'q' and item_number != 'b' and (not item_number.isdigit()):
            continue
        if "q" == item_number:
            return
        elif "b" == item_number:
            return sale()
        if int(item_number) > 4:
            print('Invalid item choice.')
            continue
        elif int(item_number) <=0:
            print ("Invalid item choice.")
            continue



        qty = int(input('How many pieces: '))
        if qty <=0:
            print('Invalid input')
        else:
            item_number = int(item_number)
            if item_number >=1 and item_number <=4:
                price = items[item_number - 1].split('$')[1]
                if len(your_cart)>0:
                    found = 0
                    found_id = -1
                    for i, item in enumerate(your_cart):
                        if items[item_number - 1].split('$')[0] == item['name'].split('$')[0]:
                            #your_cart[i]['qty'] = your_cart[i]['qty']  + qty
                            found = 1
                            found_id = i
                            break
                    if found == 0:
                        your_cart.append({'name': items[item_number - 1], 'qty': qty})
                    elif found == 1:
                        your_cart[found_id]['qty'] = your_cart[i]['qty'] + qty


                else:
                    your_cart.append({'name': items[item_number - 1], 'qty': qty})
                show_cart()

            else:
                print(f"Invalid item number: {item_number}")


def checkout():
    # memebership: Gold: 3, Silver: 2, Bronze: 1
    print("Checkout and Purchase")
    show_cart()
    subtotal = calculate_total_price()
    while True:
        membership_type= input('Do you have membership(y or n):').lower()
        if membership_type == 'y':
            membership_level= int(input('Key in your membership level(1,2,3):'))
            if membership_level ==  3:
                discount = subtotal*0.15
                print("Membership Status: Gold, You are entitled to a 15% discount at checkout")
                break
            elif membership_level == 2:
                discount =subtotal*0.1
                print("Membership Status: Silver, You are entitled to a 10% discount at checkout")
                break
            elif membership_level == 1:
                discount = subtotal * 0.05
                print("Membership Status: Bronze, You are entitled to a 5% discount at checkout")
                break
        elif membership_type == 'n':
            discount = 0
            print ("You do not have a membership. Would you like to purchase one?")
            break
        else:
            print('Invalid choice.')
            continue
    total_amount_after_discount = subtotal - discount
    gst = total_amount_after_discount*0.08
    total_price = total_amount_after_discount + gst
    print(f"Subtotal before discount: ${subtotal}")
    print(f"GST (8%): ${gst}")
    print(f'Discount amount: ${discount}')
    print(f"Subtotal after discount(excluding GST: ${total_amount_after_discount}")
    print(f"Total Price after discount(including GST): ${total_price}")
    print("Thank you for your purchase!")



def calculate_total_price():
    subtotal = 0.0
    for item in your_cart:
        price = float(item['name'].split('$')[1])
        qty = item['qty']
        subtotal += price * qty
    return subtotal


def main():
    print('''
                      -------------------------------------
                         Welcome to the GUNDAM toy store!!!
                      -------------------------------------
 ''')
    while True:
        menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            print('''
         -------------------------------------------------------------------
         |  Cart   |   Category    | Item ID  |       Item       |  Price  |
         ------------------------------------------------------------------- 
         |    1    | Perfect Grade |    1     |  GUNDAM RAISER   | $315.00 |   
         |    1    | Perfect Grade |    2     |Gundam SEED Astray| $320.00 |    
         |    1    | Perfect Grade |    3     |    Wing Gundam   | $350.00 |    
         |    1    | Perfect Grade |    4     |  Freedom Gundam  | $410.00 |  
         -------------------------------------------------------------------          
         |    2    |  Real Grade   |    1     |   RG GoldyMarg   |  $52.00 |    
         |    2    |  Real Grade   |    2     |  RG Gao Gai Gar  |  $78.00 |     
         |    2    |  Real Grade   |    3     |    God Gundam    |  $58.00 |  
         |    2    |  Real Grade   |    4     |    Wing Gundam   |  $38.00 | 
         -------------------------------------------------------------------        
         |    3    | Master Grade  |    1     |  Eclipse Gundam  | $195.00 |   
         |    3    | Master Grade  |    2     |    Full Saber    |  $72.00 |  
         |    3    | Master Grade  |    3     |  Unicorn Gundam  |  $64.00 |    
         |    3    | Master Grade  |    4     |  Gundam Dynames  |  $56.00 |  
         -------------------------------------------------------------------          
         |    4    |  Mecha Girl   |    1     | Messiah Ranka Lee|  $95.00 |  
         |    4    |  Mecha Girl   |    2     |      Ganesa      |  $20.00 |  
         |    4    |  Mecha Girl   |    3     | Arcanadea Lumitea|  $75.00 |  
         |    4    |  Mecha Girl   |    4     | Tsubasa Kazanari |  $90.00 |
         -------------------------------------------------------------------
         |    5    |   Motorized   |    1     |   Little Ryan    |  $30.00 |  
         |    5    |   Motorized   |    2     |  Elephant Racer  |  $17.00 | 
         |    5    |   Motorized   |    3     |  Zoids Stylaser  | $148.00 |
         |    5    |   Motorized   |    4     |   Cannon Bull    |  $35.00 | 
         -------------------------------------------------------------------
          ''')
        elif choice == "2":
            sale()
        elif choice == "3":
            show_cart()
        elif choice == "4":
            edit_cart()
        elif choice == "5":
            if len(your_cart) == 0:
                print("Your cart is empty. Please add items before checking out.")
            else:
                checkout()


                break

        elif choice=="6":
            break



        else:
            print("\nInvalid choice!!!\n")




if __name__ == "__main__":
    main()
