
from agent import run_agent
from memory import get_user
from classifier import classify_issue


print("======================================")
print("       SMART IT HELPDESK AGENT")
print("======================================")

print("\nWelcome to the Smart IT Helpdesk.")

while True:

    print("\n--------------------------------------")

    # -----------------------------
    # GET USER ID
    # -----------------------------
    user_id = input(
        "Enter your USER ID (or type 'exit'): "
    ).strip()

    # Check EXIT immediately
    if user_id.lower() == "exit":
        print("\nThank you. Goodbye!")
        break

    # -----------------------------
    # CHECK USER
    # -----------------------------
    user = get_user(user_id)

    while not user:

        print("\nUser not found.")
        print("Please enter a valid USER ID.")

        user_id = input(
            "Enter your USER ID (or type 'exit'): "
        ).strip()

        # If user enters exit inside the validation loop
        if user_id.lower() == "exit":
            print("\nThank you. Goodbye!")
            exit()

        user = get_user(user_id)

    print("\nUser found successfully!")

    # -----------------------------
    # GET PROBLEM
    # -----------------------------
    description = input(
        "Describe your IT problem: "
    ).strip()

    if not description:
        print("Please enter a problem.")
        continue

    # -----------------------------
    # SEND TO AGENT
    # -----------------------------
    issue_type = classify_issue(description)
    result = run_agent(
        user_id,
        issue_type,
        description
    )

    # -----------------------------
    # HANDLE AGENT RESULT
    # -----------------------------
    if result == "resolved":

        print("\n✓ Ticket completed successfully.")

    elif result == "escalated":

        print("\n⚠ Your ticket has been sent to human IT support.")

    elif result == "unknown":

        print("\nSorry, I could not identify your problem.")
        print("Please describe the problem in more detail.")


