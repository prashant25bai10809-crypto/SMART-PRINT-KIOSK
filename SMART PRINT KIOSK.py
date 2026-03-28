# Smart Print Kiosk - Beginner Friendly Code

print("------ SMART PRINT KIOSK ------")

pages = int(input("Enter number of pages: "))

print("\nChoose Print Type")
print("1. Black & White")
print("2. Color")
ptype = int(input("Enter choice (1 or 2): "))

print("\nChoose Page Quality")
print("1. Normal Paper")
print("2. Thick Paper")
quality = int(input("Enter choice (1 or 2): "))

if ptype == 1:
    price_per_page = 2        # ₹2 per page
    print_type = "Black & White"
else:
    price_per_page = 5        # ₹5 per page
    print_type = "Color"

if quality == 1:
    extra = 0
    paper_type = "Normal Paper"
else:
    extra = 2                 # ₹2 extra per page
    paper_type = "Thick Paper"

total_price = pages * (price_per_page + extra)

print("\n------ BILL ------")
print("Pages:", pages)
print("Print Type:", print_type)
print("Paper Type:", paper_type)
print("Total Amount = ₹", total_price)

print("\nPlease pay ₹", total_price,"To the given QR Code")
print("\n Printing Started...")


