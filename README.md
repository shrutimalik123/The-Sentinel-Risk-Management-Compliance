# ⚖️ The Sentinel: Risk Management & Compliance Sim

A strategic simulation designed for health administration students to practice the principles of Patient Safety and Regulatory Compliance. As the Chief Quality Officer (CQO), you must navigate the aftermath of medical errors. Your decisions will determine whether the hospital learns from its mistakes through Root Cause Analysis (RCA) or faces decertification from regulatory bodies like The Joint Commission.

This project focuses on teaching:
* **Root Cause Analysis (RCA):** Shifting the focus from individual "human error" to systemic "process failure."
* **Regulatory Compliance:** Managing a "Compliance Score" that reflects the hospital's standing with accrediting bodies.
* **The Swiss Cheese Model:** Illustrating how multiple layers of defense must fail for a sentinel event to occur.
* **Resource Impact:** Balancing a "Legal Fund" used for training and settlements against the need for organizational transparency.

---

## ✨ Features

* **Sentinel Event Scenarios:** Randomized incidents ranging from surgical errors and medication overdoses to HIPAA data breaches.
* **Just Culture Logic:** Rewards players who analyze systems (long-term safety) and penalizes those who merely seek to assign blame or hide errors.
* **Accreditation Stakes:** A dynamic scoring system where falling below a certain threshold results in "Immediate Jeopardy" or loss of accreditation.
* **Financial Modeling:** Simulates the real-world costs of corrective action plans and regulatory fines.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `risk_management.py`.
2.  **Open Terminal:** Navigate to the folder containing the file.
3.  **Run the Script:**
    ```bash
    python risk_management.py
    ```

### 3. Gameplay Instructions
1.  **Review the Incident:** Read the alert carefully (e.g., "Wrong-site surgery").
2.  **Conduct the Investigation:** * **Individual Blame (1):** High staff turnover and low morale; doesn't fix the root problem.
    * **System Analysis (2):** Invests in training and checklists; the "Gold Standard" for safety.
    * **Suppression (3):** High risk of massive fines and total loss of reputation.
3.  **Survive the Audit:** Maintain a compliance score of 90 or higher to receive the "Gold Seal" of approval.

[attachment_0](attachment)

---

## 🧠 Code Structure Highlights

### System-Level Mitigation
The core "Winning" logic is found in the System Analysis choice. It demonstrates that while training has an immediate financial cost (`legal_fund -= 5000`), it is the only way to recover `compliance_score` points.

```python
elif choice == "2":
    # The 'Root Cause Analysis' approach
    compliance_score += 20
    hospital_reputation += 10
    print("✅ SYSTEM IMPROVED. Corrective Action Plan (CAP) implemented.")

