from Three_Tools import (
    password_help,
    network_help,
    performance_help,
    escalate_to_human
)
from classifier import classify_issue
from memory import (
    add_ticket,
    update_ticket,
    get_ticket
)
import json
import random

MAX_ATTEMPTS = 2


def create_ticket(user_id, issue_type, description):
    """
    Create a new IT support ticket and store it in memory.
    """

    ticket = {
        "ticket_id": "TKT001",
        "user_id": user_id,
        "problem_type": issue_type,
        "description": description,
        "status": "Open",
        "severity": "Medium",
        "actions_taken": [],
        "solution": None,
        "escalated": False
    }

    add_ticket(ticket)

    return ticket["ticket_id"]


def generate_ticket_id():
    # Open memory.json
    with open("memory.json", "r") as file:
        memory = json.load(file)

    # Get existing ticket IDs
    existing_ids = []

    for ticket in memory["tickets"]:
        existing_ids.append(ticket["ticket_id"])

    # Generate a random ticket ID
    while True:
        number = random.randint(1, 999)
        ticket_id = f"TKT{number:03d}"

        # Check whether ID already exists
        if ticket_id not in existing_ids:
            return ticket_id


def select_tool(issue_type):
    """
    Decide which IT tool should be used.
    """

    if issue_type == "password":
        return password_help

    elif issue_type == "network":
        return network_help

    elif issue_type == "performance":
        return performance_help

    else:
        return None


def run_agent(user_id, issue_type, description):

    print("\n===================================")
    print("       SMART IT HELPDESK AGENT")
    print("===================================")

    print(f"\nProblem detected: {issue_type}")

    # Create ticket
    ticket_id = create_ticket(
        user_id,
        issue_type,
        description
    )

    print(f"Ticket created: {ticket_id}")

    tool = select_tool(issue_type)

    if tool is None:
        print("\nSorry, I don't have a tool for this problem.")
        return "unknown"

    # -------------------------
    # ATTEMPT 1
    # -------------------------

    print("\n--- Attempt 1 ---")

    result = tool()

    actions = [
        f"{tool.__name__} - Attempt 1"
    ]

    update_ticket(
        ticket_id,
        {
            "actions_taken": actions
        }
    )

    if result:

        update_ticket(
            ticket_id,
            {
                "status": "Resolved",
                "solution": "Issue resolved during first troubleshooting attempt."
            }
        )

        print("\n✓ Issue resolved successfully.")

        return "resolved"

    # -------------------------
    # ATTEMPT 2
    # -------------------------

    print("\n--- Attempt 1 was not successful ---")

    print("Let's try another approach.")

    print("\n--- Attempt 2 ---")

    result = tool()

    actions.append(
        f"{tool.__name__} - Attempt 2"
    )

    update_ticket(
        ticket_id,
        {
            "actions_taken": actions
        }
    )

    if result:

        update_ticket(
            ticket_id,
            {
                "status": "Resolved",
                "solution": "Issue resolved during second troubleshooting attempt."
            }
        )

        print("\n✓ Issue resolved successfully.")

        return "resolved"

    # -------------------------
    # ESCALATION
    # -------------------------

    print("\n--- Automatic Resolution Failed ---")

    escalate_to_human(
        issue_type,
        MAX_ATTEMPTS
    )

    update_ticket(
        ticket_id,
        {
            "status": "Escalated",
            "escalated": True,
            "solution": None
        }
    )

    return "escalated"