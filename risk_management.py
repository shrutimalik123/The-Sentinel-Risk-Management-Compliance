import random

def risk_management_game():
    # 1. Hospital Stats
    compliance_score = 100
    hospital_reputation = 80
    legal_fund = 50000
    
    # Potential Incidents
    incidents = [
        {"event": "Wrong-site surgery on a patient's knee.", "type": "Surgical"},
        {"event": "Medication error: 10x dose of insulin administered.", "type": "Pharmacy"},
        {"event": "Patient fall resulting in a hip fracture.", "type": "Safety"},
        {"event": "Data breach: 500 patient records leaked.", "type": "HIPAA"}
    ]

    print("--- ⚖️ THE SENTINEL: RISK & COMPLIANCE ⚖️ ---")
    print("Mission: Protect patients and the hospital from systemic failures.")
    print("Goal: Maintain Compliance and Reputation through Root Cause Analysis (RCA).")

    # 2. Game Loop
    for round in range(1, 4):
        incident = random.choice(incidents)
        print(f"\n🚨 ALERT: A Sentinel Event has occurred!")
        print(f"INCIDENT: {incident['event']}")
        
        # Immediate Impact
        compliance_score -= 15
        hospital_reputation -= 10
        
        # 3. Root Cause Analysis (RCA) Decision
        print("\nCHOOSE YOUR INVESTIGATION FOCUS:")
        print("1) Blame the Individual (Disciplinary action for the staff member)")
        print("2) Analyze the System (Check protocols, checklists, and equipment)")
        print("3) Suppress the Event (Minimize reporting to avoid bad PR)")
        
        choice = input("Select Action (1-3): ")

        if choice == "1":
            print("⚠️ DISCIPLINE ISSUED. The staff member was fired.")
            print("Result: Staff morale dropped. The underlying process error remains.")
            compliance_score -= 5
            hospital_reputation -= 5
            
        elif choice == "2":
            print("✅ SYSTEM IMPROVED. You identified a lack of 'Time-Out' protocols.")
            print("Result: New safety checklists implemented. Regorters are satisfied.")
            compliance_score += 20
            hospital_reputation += 10
            legal_fund -= 5000 # Cost of training
            
        elif choice == "3":
            print("🚫 COVER-UP ATTEMPTED. Regulators discovered the non-disclosure.")
            print("Result: HEAVY FINES and 'Immediate Jeopardy' status.")
            compliance_score -= 40
            legal_fund -= 20000

    # 4. Final Audit
    print(f"\n--- 📋 JOINT COMMISSION AUDIT REPORT ---")
    print(f"Final Compliance Score: {compliance_score}")
    print(f"Remaining Legal Fund: ${legal_fund}")
    
    if compliance_score >= 90:
        print("🏆 GOLD SEAL: Your hospital is a leader in patient safety!")
    elif compliance_score >= 60:
        print("📋 PROBATION: Improvements needed. Expect follow-up surveys.")
    else:
        print("❌ DECERTIFIED: Your facility has lost its accreditation.")

risk_management_game()
