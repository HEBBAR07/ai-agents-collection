
packages = [
    {
        "destination": "Goa",
        "days": 4,
        "price": 12000,
        "available": True
    },
    {
        "destination": "Kerala",
        "days": 5,
        "price": 15000,
        "available": True
    },
    {
        "destination": "Manali",
        "days": 6,
        "price": 18000,
        "available": False
    },
    {
        "destination": "Jaipur",
        "days": 3,
        "price": 10000,
        "available": True
    },
    {
        "destination": "Ooty",
        "days": 3,
        "price": 8000,
        "available": False
    }
]

print("================================")
print("   WELCOME TO TRAVEL AGENT")
print("================================")
print("Ask about travel packages.")
print("Type 'exit' to stop the chatbot.")

while True:
    question = input("\nYou: ").strip().lower()

    if question == "exit":
        print("Thank you for using Travel Agent!")
        break

    if question in ["hi", "hello", "hey"]:
        print("Travel Agent: Hello! Where would you like to travel?")
        continue

    if "all packages" in question or "all destinations" in question:
        print("\nAvailable Travel Packages:")

        for package in packages:
            status = "Available" if package["available"] else "Unavailable"
            print(
                package["destination"],
                "-", package["days"], "days,",
                "Price: Rs.", package["price"],
                "-", status
            )
        continue

    found = False

    for package in packages:
        destination = package["destination"].lower()

        if destination in question:
            found = True

            print("\n--- Travel Package Details ---")
            print("Destination:", package["destination"])
            print("Duration:", package["days"], "days")
            print("Price: Rs.", package["price"])

            if package["available"]:
                print("Status: Package is available.")
            else:
                print("Status: Package is currently unavailable.")

            break

    if not found:
        print(
            "Travel Agent: Sorry, this destination "
            "is not available in our packages."
        )
