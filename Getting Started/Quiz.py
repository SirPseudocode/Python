questions = (
    "How many elements are in the periodic table?: ", 
    "Which animal lays the largest eggs?: ", 
    "What is the most abundant gas in Earth's atmosphere?: ", 
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"), 
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), 
    ("A. 206", "B. 207", "C. 208", "D. 209"), 
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

answers = ("C", "D", "A", "A", "B")

score = 0

for q, opts, ans in zip(questions, options, answers):
    print("------------------")
    print(q)

    for o in opts:
        print(o)

    guess = input("Type your answer: ").upper()
    
    if guess == ans:
        score += 1
        print("CORRECT!!!")
    else:
        print(f"WRONG! {ans} is the correct answer")

print("\n----- RESULT -----")
print(f"Your score is {score} / {len(questions)}")
print("------------------")