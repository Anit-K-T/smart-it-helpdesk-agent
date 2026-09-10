#hello
# --- Tools / Actions Module (tools.py) ---
from memory import get_user
def password_help():
    """Tool for password reset using multi-step security verification."""
    print("\n[IT Tool: Password Helper]")
    print("-> Action: Initiating identity verification protocol...")
    
    # Step 1: Employee ID
    
 
    


   
            
    # Step 2: Date of Birth
    dob = input("2. Enter your Date of Birth (YYYY-MM-DD): ").strip()
    if dob != user["dob"]:  # Simulated valid DOB
        print("-> Verification failed: Date of birth does not match records.")
        return False
        
    print("-> Security verification passed successfully.")
    print("-> Action: Temporary password generated: TempPass#2026")
    
    success = input("Were you able to log in with this temporary password? (yes/no): ").strip().lower()
    return success == "yes"


def network_help():
    """Tool for network troubleshooting."""
    print("\n[IT Tool: Network Troubleshooter]")
    print("-> Action: Running automated diagnostic script on your local network interface...")
    print("-> Instruction: Please disconnect from VPN, toggle your Wi-Fi off and on, and reconnect.")
    
    success = input("Did this resolve your internet issue? (yes/no): ").strip().lower()
    return success == "yes"


def performance_help():
    """Tool for slow laptop optimization."""
    print("\n[IT Tool: Performance Optimizer]")
    print("-> Action: Clearing temporary system cache and analyzing background resource hogs.")
    print("-> Instruction: Please close unused browser tabs and save your work for a quick system restart.")
    
    success = input("Did this resolve your laptop speed issue? (yes/no): ").strip().lower()
    return success == "yes"


# --- Escalation Tool ---

def escalate_to_human(issue_type, attempts):
    """Escalation path when automated tools fail."""
    print("\n[IT Support System - Escalation Triggered]")
    print(f"⚠️ Automated tools could not resolve your '{issue_type}' issue after {attempts} attempts.")
    print("-> Action: Creating high-priority support ticket #9941 and notifying the On-Call IT Helpdesk.")
    print("-> Notice: A human support technician will reach out to you via chat or phone shortly.")


# --- Comprehensive Test Block ---

if __name__ == "__main__":
    print("=== STARTING IT TOOLS TEST SUITE ===\n")
    
    print("--- 1. Testing Password Tool ---")
    pw_result = password_help()
    print(f">> Password Tool Result Returned: {pw_result}\n")
    
    print("--- 2. Testing Network Tool ---")
    net_result = network_help()
    print(f">> Network Tool Result Returned: {net_result}\n")
    
    print("--- 3. Testing Performance Tool ---")
    perf_result = performance_help()
    print(f">> Performance Tool Result Returned: {perf_result}\n")
    
    print("--- 4. Testing Escalation Tool ---")
    escalate_to_human("network", 2)
    
    print("\n=== ALL TESTS COMPLETED ===")