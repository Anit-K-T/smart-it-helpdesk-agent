
'''------------------------------------------------
A. USER ADD, EDIT, UPDATE OR DELETE CODE HELP SECTION
|
|
|
V
---------------------------------------------------'''


'''====================================
A.1) 
How to add user'''

#  from memory import add_user

# user = {
#     "user_id": "USR001",
#     "name": "Arun",
#     "email": "arun@example.com",
#     "department": "Accounts",
#     "role": "Staff"
# }

# add_user(user)
#======================================


'''=====================================
A.2)
How to get user'''

# from memory import get_user

# user = get_user("USR001")


# if user:
#     print(user)
#     print(user["name"])
# else:
#     print("User not found")

# ========================================



'''========================================
A.3)
How to update user'''

# from memory import update_user

# update_user(
#     "USR001",
#     {
#         "department": "IT",
#         "role": "IT Support"
#     }
# )

# =============================================




'''==============================================
A.4)
 How to delete user'''

# from memory import delete_user

# delete_user("USR001")
# ================================================


'''------------------------------------------------
B. TICKET(complaint) RAISING CODE HELP SECTION
|
|
|
V
---------------------------------------------------'''



'''================================================
B.1) Add new complaint or Ticket'''


# from memory import add_ticket

# ticket = {
#     "ticket_id": "TKT001",
#     "user_id": "USR001",
#     "problem_type": "Internet Issue",
#     "description": "Internet is not working",
#     "status": "Open",
#     "severity": "Medium",
#     "actions_taken": [],
#     "solution": None,
#     "escalated": False
# }

# add_ticket(ticket)

#==================================================


'''================================================
B.2) Update Ticket after diagnosis'''

# from memory import update_ticket

# update_ticket(
#     "TKT001",
#     {
#         "status": "Resolved",
#         "actions_taken": [
#             "Checked Wi-Fi",
#             "Checked IP address",
#             "Restarted network adapter"
#         ],
#         "solution": "Restarting network adapter fixed the problem",
#         "escalated": False
#     }
# )

# =================================================


'''================================================
B.3) How to get Ticket Data'''

# from memory import get_ticket

# ticket = get_ticket("TKT001")

# print(ticket)

# =================================================


'''================================================
B.3) How to delete Ticket Data'''

from memory import delete_ticket

delete_ticket("TKT001")

