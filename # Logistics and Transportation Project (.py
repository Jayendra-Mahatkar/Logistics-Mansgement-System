# Logistics and Transportation Project (Beginner Level)
# written in a simple way for understanding

all_shipments = []   # will store all shipment info here


# function to add shipment
def addShipment():
    print("---- Add New Shipment ----")
    senderName = input("Enter sender name: ")
    recName = input("Enter receiver name: ")
    wt = float(input("Enter weight in kg: "))
    dist = float(input("Enter distance in km: "))

    # simple formula for cost (not real cost)
    delivery_cost = (wt * 12) + (dist * 4)

    data = {}
    data["sender"] = senderName
    data["receiver"] = recName
    data["weight"] = wt
    data["distance"] = dist
    data["cost"] = delivery_cost
    data["status"] = "Pending"

    all_shipments.append(data)
    print("Shipment Added!\n")


# function to update status
def updateStatus():
    print("\n---- Update Shipment ----")
    if len(all_shipments) == 0:
        print("No shipments yet!\n")
        return

    for i in range(len(all_shipments)):
        s = all_shipments[i]
        print(str(i+1) + ". " + s["sender"] + " -> " + s["receiver"] + " (" + s["status"] + ")")

    num = int(input("Select shipment number: "))
    if num <= 0 or num > len(all_shipments):
        print("Invalid number!")
        return

    newst = input("Enter new status (In Transit / Delivered): ")
    all_shipments[num-1]["status"] = newst
    print("Status Updated!\n")


# function to view shipments
def viewAll():
    print("\n---- All Shipments ----")
    if len(all_shipments) == 0:
        print("No shipment data found.\n")
        return

    for i in range(len(all_shipments)):
        s = all_shipments[i]
        print("Shipment", i+1)
        print(" Sender:", s["sender"])
        print(" Receiver:", s["receiver"])
        print(" Weight:", s["weight"], "kg")
        print(" Distance:", s["distance"], "km")
        print(" Cost: Rs.", s["cost"])
        print(" Status:", s["status"])
        print("---------------------------")


# main program loop
while True:
    print("\n======= Logistics Management System =======")
    print("1. Add Shipment")
    print("2. Update Shipment Status")
    print("3. View Shipments")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        addShipment()
    elif ch == "2":
        updateStatus()
    elif ch == "3":
        viewAll()
    elif ch == "4":
        print("Exiting... Thank you!")
        break
    else:
        print("Wrong option! Try again.")