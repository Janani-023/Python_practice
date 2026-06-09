import random
from datetime import datetime
from pypdf import PdfReader
import re

def load_pdf(pdf_path):
    # Initialize a structured dictionary to hold quiz topics
    # Added "Fundamentals" to match your select_topics configuration
    quiz_data = {"Fundamentals": []}
    full_text = ""
    
    with open(pdf_path, "rb") as p:
        reader = PdfReader(p)
        # Loop through and extract text from all pages
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
    
    # Split text by question numbering pattern like "1)", "2)"
    pa = re.split(r"\n(?=\d+\))", full_text)
    
    for ps in pa:
        ps = ps.strip()
        if not ps:
            continue
            
        # Basic parsing: assumes first line is the question, last line contains the answer
        lines = [line.strip() for line in ps.split("\n") if line.strip()]
        if len(lines) >= 2:
            question_text = lines[0]
            # Try to identify an answer line, or fallback to the last line
            answer_text = lines[-1]
            for line in lines:
                if "answer" in line.lower() or "ans:" in line.lower():
                    answer_text = line
                    break
            
            # Appending to the "Fundamentals" topic as an example
            quiz_data["Fundamentals"].append({
                "question": ps, # Gives the user the full block (question + choices)
                "answer": answer_text
            })
            
    return quiz_data
    
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
        return "Fundamentals" # Must return a string matching the dictionary key
    else:
        print("Invalid choice or topic not built yet!")
        return None

def start_test(topic):
    global score, tot_q
    score = 0
    tot_q = 0
    
    # Validation check
    if not topic or topic not in questions or not questions[topic]:
        print("Cannot start test. Topic missing or contains no questions.")
        return False

    print(f"\nStarting the test on '{topic}'...")
    
    # Randomize question order safely
    select_que = random.sample(questions[topic], len(questions[topic]))

    for q in select_que:
        print(f"\n{q['question']}")
        user_answer = input("Enter your answer: ").lower().strip()
        tot_q += 1
        
        # Strip identifiers like "Answer: " out of the evaluation string
        clean_ans = re.sub(r'^(answer|ans):\s*', '', q['answer'], flags=re.IGNORECASE).lower().strip()
        
        if clean_ans in user_answer or user_answer in clean_ans:
            print("-> Correct!")
            score += 1
        else:
            print(f"-> Need improvement. (Correct Answer: {q['answer']})")
    return True

def report(studentname):
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
# Added 'r' prefix to treat backslashes as literal characters
pdf = r"C:\Users\Live wire\Downloads\Python Programming_Livewire Course_questions_9_6_2026_12_30_00_PM.pdf"
questions = load_pdf(pdf)

welcome()
studentname = input("Enter the student name: ")
topic = select_topics()

if topic:
    test_completed = start_test(topic)
    if test_completed:
        report(studentname)
