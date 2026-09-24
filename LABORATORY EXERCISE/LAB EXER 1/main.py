# IT Automation Incident Ticket Manager
# Linear Data Structure: List

# The list that stores all the tickets
tickets = []

# Add the 10 sample tickets
tickets.append({"id": "INC1392939", "bot": "BOT-Inventory", "desc": "Failed to generate the daily report"})
tickets.append({"id": "INC1392940", "bot": "BOT-Email", "desc": "Failed to send the scheduled notification"})
tickets.append({"id": "INC1392941", "bot": "BOT-DataSync", "desc": "Encountered an error during data transfer"})
tickets.append({"id": "INC1392942", "bot": "BOT-Invoice", "desc": "Failed to process an invoice"})
tickets.append({"id": "INC1392943", "bot": "BOT-Report", "desc": "Failed to generate the weekly report"})
tickets.append({"id": "INC1392944", "bot": "BOT-FileTransfer", "desc": "Failed to upload the required file"})
tickets.append({"id": "INC1392945", "bot": "BOT-DataEntry", "desc": "Encountered an error while entering records"})
tickets.append({"id": "INC1392946", "bot": "BOT-Backup", "desc": "Failed to complete the scheduled backup"})
tickets.append({"id": "INC1392947", "bot": "BOT-Validation", "desc": "Failed to validate the submitted records"})
tickets.append({"id": "INC1392948", "bot": "BOT-Notification", "desc": "Failed to send the system alert"})


# 1. ADD a new ticket
def add_ticket():
    inc_id = input("Enter Incident ID: ")
    bot = input("Enter Bot: ")
    desc = input("Enter Short Description: ")

    tickets.append({"id": inc_id, "bot": bot, "desc": desc})
    print("Ticket added!")


# 2. DISPLAY all tickets
def display_tickets():
    if len(tickets) == 0:
        print("No active tickets.")
    else:
        print("\n--- ACTIVE INCIDENT TICKETS ---")
        for ticket in tickets:
            print(ticket["id"], "|", ticket["bot"], "|", ticket["desc"])


# 3. SEARCH for a ticket
def search_ticket():
    inc_id = input("Enter Incident ID to search: ")

    for ticket in tickets:
        if ticket["id"] == inc_id:
            print("Ticket found!")
            print("Incident ID:", ticket["id"])
            print("Bot:", ticket["bot"])
            print("Description:", ticket["desc"])
            return

    print("Ticket not found.")


# 4. REMOVE a resolved ticket
def remove_ticket():
    inc_id = input("Enter Incident ID to remove: ")

    for ticket in tickets:
        if ticket["id"] == inc_id:
            tickets.remove(ticket)
            print("Ticket removed!")
            return

    print("Ticket not found.")


# 5. COUNT active tickets
def count_tickets():
    print("Total active tickets:", len(tickets))


# MENU
while True:
    print("\n===== INCIDENT TICKET MANAGER =====")
    print("1. Add Ticket")
    print("2. Display Tickets")
    print("3. Search Ticket")
    print("4. Remove Ticket")
    print("5. Count Tickets")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_ticket()
    elif choice == "2":
        display_tickets()
    elif choice == "3":
        search_ticket()
    elif choice == "4":
        remove_ticket()
    elif choice == "5":
        count_tickets()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")