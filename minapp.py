import random
from datetime import datetime

# FIX 1: Structured as a dictionary of LISTS containing dictionaries
questions = {
    "fundamentals": [
        {"question": "What is Python?", "answer": "high-level"}
    ],
    "Control flow": [
        {"question": "What is a loop?", "answer": "for"}
    ],
    "Data Structures": [
        {"question": "Name a built-in sequence type.", "answer": "list"}
    ],
    "Functions": [
        {"question": "What keyword defines a function?", "answer": "def"}
    ],
    "Modules": [
        {"question": "How do you bring in a module?", "answer": "import"}
    ]
}

def welcome():
    print("\n=====================")
    print("     AI Test App     ")
    print("=====================")

def select_topics():
    print("\nAvailable topics:")
    print("1. Fundamentals")
    print("2. Control flow")
    print("3. Data Structures")
    print("4. Functions")
    print("5. Modules")

    choice = input("\nSelect topic (1-5): ")
    if choice == '1':
        return "fundamentals"
    elif choice == '2':
        return "Control flow"
    elif choice == '3':
        return "Data Structures"
    elif choice == '4':
        return "Functions"
    elif choice == '5':
        return "Modules"
    else:
        print("Invalid choice!")
        return None

def start_test(topic):
    # Use global keywords so variables are accessible in report()
    global score, tot_q
    score = 0
    tot_q = 0
    
    if not topic or topic not in questions:
        print("Cannot start test without a valid topic.")
        return False

    print(f"\nStarting the test on '{topic}'...")
    
    # FIX 2: random.sample now correctly pulls from a list of questions
    select_que = random.sample(questions[topic], len(questions[topic]))

    for q in select_que:
        print(f"\nQuestion: {q['question']}")
        user_answer = input("Enter your answer: ").lower()
        tot_q += 1
        
        if q['answer'].lower() in user_answer:
            print("-> Correct!")
            score += 1
        else:
            print("-> Need improvement.")
    return True

def report(studentname):
    # Avoid zero division error if no questions were asked
    if tot_q == 0:
        return
    p = (score / tot_q) * 100
    print("\n=====================")
    print("     TEST REPORT     ")
    print("=====================")
    print(f"Student Name: {studentname}")
    print(f"Score       : {score}/{tot_q}")
    print(f"Percentage  : {p:.2f}%")
    print(f"Date        : {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# --- Main Execution Flow ---
welcome()
studentname = input("Enter the student name: ")
topic = select_topics()

# FIX 3: Actually trigger the test and report functions
if topic:
    test_completed = start_test(topic)
    if test_completed:
        report(studentname)
