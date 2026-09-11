# #hello
# # --- Tools / Actions Module (tools.py) ---
# from memory import get_user
# def password_help():
#     """Tool for password reset using multi-step security verification."""
#     print("\n[IT Tool: Password Helper]")
#     print("-> Action: Initiating identity verification protocol...")
    
#     dob = input("2. Enter your Date of Birth (YYYY-MM-DD): ").strip()
#     if dob != user["dob"]:  # Simulated valid DOB
#         print("-> Verification failed: Date of birth does not match records.")
#         return False
        
#     print("-> Security verification passed successfully.")
#     print("-> Action: Temporary password generated: TempPass#2026")
    
#     success = input("Were you able to log in with this temporary password? (yes/no): ").strip().lower()
#     return success == "yes"


# # def network_help():
# #    """Tool for network troubleshooting."""
# #     print("\n[IT Tool: Network Troubleshooter]")
# #     print("-> Action: Running automated diagnostic script on your local network interface...")
# #     print("-> Instruction: Please disconnect from VPN, toggle your Wi-Fi off and on, and reconnect.")
    
# #     success = input("Did this resolve your internet issue? (yes/no): ").strip().lower()
# #     return success == "yes"

# def network_help():
#     """Tool for multi-step network troubleshooting."""
#     print("\n[IT Tool: Network Troubleshooter]")
#     print("-> Action: Running automated diagnostic script on your local network interface...")
    
#     # --- Step 1: Initial Troubleshooting Instruction ---
#     print("-> Instruction 1: Please disconnect from VPN, toggle your Wi-Fi off and on, and reconnect.")
#     success = input("Did this resolve your internet issue? (yes/no): ").strip().lower()
    
#     if success == "yes":

#         return True
#   else:
        
#     # --- Step 2: Secondary Instruction (Triggered if Step 1 fails) ---
#     print("\n[IT Tool: Network Troubleshooter - Advanced Step]")
#     print("-> Action: Initial step failed. Applying secondary diagnostic fix...")
#     print("-> Instruction 2: Please open your terminal/command prompt, run 'ipconfig /flushdns', and restart your computer's network adapter.")
    
#     success_second = input("Did this secondary step resolve your internet issue? (yes/no): ").strip().lower()
#     return success_second == "yes"




# # def performance_help():
# #     """Tool for slow laptop optimization."""
# #     print("\n[IT Tool: Performance Optimizer]")
# #     print("-> Action: Clearing temporary system cache and analyzing background resource hogs.")
# #     print("-> Instruction: Please close unused browser tabs and save your work for a quick system restart.")
    
# #     success = input("Did this resolve your laptop speed issue? (yes/no): ").strip().lower()
# #     return success == "yes"


# def performance_help():
#     """Tool for multi-step slow laptop optimization."""
#     print("\n[IT Tool: Performance Optimizer]")
#     print("-> Action: Analyzing background resource hogs and system memory...")
    
#     # --- Step 1: Initial Troubleshooting Instruction ---
#     print("-> Instruction 1: Please close unused browser tabs and save your work for a quick system restart.")
#     success = input("Did this resolve your laptop speed issue? (yes/no): ").strip().lower()
    
#     if success == "yes":
#         return True
        
#     # --- Step 2: Secondary Instruction (Triggered if Step 1 fails) ---
#     print("\n[IT Tool: Performance Optimizer - Advanced Step]")
#     print("-> Action: Initial step failed. Applying secondary resource management fix...")
#     print("-> Instruction 2: Please open Task Manager (or Activity Monitor), identify processes consuming high CPU or RAM, and end those tasks.")
    
#     success_second = input("Did this secondary step resolve your laptop speed issue? (yes/no): ").strip().lower()
#     return success_second == "yes"



# # --- Escalation Tool ---

# def escalate_to_human(issue_type, attempts):
#     """Escalation path when automated tools fail."""
#     print("\n[IT Support System - Escalation Triggered]")
#     print(f"⚠️ Automated tools could not resolve your '{issue_type}' issue after {attempts} attempts.")
#     print("-> Action: Creating high-priority support ticket #9941 and notifying the On-Call IT Helpdesk.")
#     print("-> Notice: A human support technician will reach out to you via chat or phone shortly.")


# ============================================================
# SMART IT HELPDESK AGENT
# THREE TOOLS / ACTIONS
# ============================================================
#
# INDEX
# ------------------------------------------------------------
# 1. Password Help Tool
# 2. Network Help Tool
# 3. Performance Help Tool
# 4. Human Escalation Tool
# ============================================================


# ============================================================
# 1. PASSWORD HELP TOOL
# ============================================================

def password_help(user):
    """
    Tool for solving password/login problems.
    """

    print("\n[IT TOOL: PASSWORD HELPER]")

    # Ask the user for their Date of Birth
    dob = input(
        "Enter your Date of Birth (YYYY-MM-DD): "
    ).strip()

    # Check whether the entered DOB matches the user's record
    if dob == user["dob"]:

        print("\n✓ Identity verification successful.")
        print("-> Temporary password generated.")
        print("-> Please use the temporary password to log in.")

        # Ask whether the problem is solved
        success = input(
            "Were you able to log in? (yes/no): "
        ).strip().lower()

        if success == "yes":
            return True
        else:
            return False

    else:

        print("\n✗ Verification failed.")
        print("-> Date of Birth does not match our records.")

        return False


# ============================================================
# 2. NETWORK HELP TOOL
# ============================================================

def network_help():
    """
    Tool for solving Wi-Fi and internet problems.
    """

    print("\n[IT TOOL: NETWORK TROUBLESHOOTER]")

    # -----------------------------
    # STEP 1
    # -----------------------------

    print("\nStep 1: Basic Network Troubleshooting")

    print("-> Turn Wi-Fi OFF and ON.")
    print("-> Disconnect from VPN.")
    print("-> Reconnect to the Wi-Fi network.")

    success = input(
        "Did this resolve your internet issue? (yes/no): "
    ).strip().lower()

    if success == "yes":
        solution= "Basic network troubleshooting was successful."

        return True, solution

    else:

        # -----------------------------
        # STEP 2
        # -----------------------------

        print("\nStep 1 was not successful.")
        print("\nStep 2: Advanced Network Troubleshooting")

        print("-> Restart the network adapter.")
        print("-> Forget and reconnect to Wi-Fi.")
        print("-> Restart the computer.")

        success = input(
            "Did this resolve your internet issue? (yes/no): "
        ).strip().lower()

        if success == "yes":
            solution= "Advanced network troubleshooting was successful."
            return True, solution
        else:
            return False


# ============================================================
# 3. PERFORMANCE HELP TOOL
# ============================================================

def performance_help():
    """
    Tool for solving slow laptop problems.
    """

    print("\n[IT TOOL: PERFORMANCE OPTIMIZER]")

    # -----------------------------
    # STEP 1
    # -----------------------------

    print("\nStep 1: Basic Performance Troubleshooting")

    print("-> Close unused applications.")
    print("-> Close unnecessary browser tabs.")
    print("-> Restart the laptop.")

    success = input(
        "Did this improve your laptop performance? (yes/no): "
    ).strip().lower()

    if success == "yes":
        solution= "Basic performance troubleshooting was successful."

        return True, solution
    

    else:

        # -----------------------------
        # STEP 2
        # -----------------------------

        print("\nStep 1 was not successful.")
        print("\nStep 2: Advanced Performance Troubleshooting")

        print("-> Open Task Manager.")
        print("-> Check applications using high CPU or RAM.")
        print("-> Close unnecessary applications.")

        success = input(
            "Did this resolve your laptop speed issue? (yes/no): "
        ).strip().lower()

        if success == "yes":
            solution= "Advanced performance troubleshooting was successful."
            return True, solution
        else:
            return False


# ============================================================
# 4. HUMAN ESCALATION TOOL
# ============================================================

def escalate_to_human(issue_type, attempts):
    """
    Escalate the problem to human IT support
    when automated troubleshooting fails.
    """

    print("\n======================================")
    print("       HUMAN SUPPORT ESCALATION")
    print("======================================")

    print(
        f"Automated troubleshooting could not resolve "
        f"the '{issue_type}' problem."
    )

    print(f"Number of attempts: {attempts}")

    print("\n-> Escalating the issue to human IT support.")
    print("-> A support technician will contact the employee.")
