questions = ("1. Which one of the following is asynchronous in message communication ?",
             "2. What will be the output of the following JavaScript statement? Math.sqrt(36)",
             "3. What will be the output of the following JavaScript statement? Math.floor(5.9)",
             "4. In a tree data structure, if a node has no parent node, then the node is________.",
             "5. What is the time complexity order of Quick sort algorithm? ",
             "6. Which one of the following is the smallest heading tag?",
             "7. Which network type is the largest as compared to the rest?",
             "8. Which one of the following is not a single level ordered index?",
             "9. Which one of the following is used for the purpose of syntax analysis?",
             "10. A database management system (DBMS) has________to control locks.")

options = (("A. Blocking receive", "B. Blocking send", "C. Direct message", "D. Non-block receive"),
           ("A. 6", "B. 3", "C. 36", "D. 1"),
           ("A. 9", "B. 5", "C. 7", "D. 6"),
           ("A. Root node", "B. Parent node", "C. Internal node", "D. External node"),
           ("A. O(n²)", "B. O(2ñ)", "C. O(n)", "D. O(nlog2n)"),
           ("A. <H3>", "B. <H1>", "C. <H4>", "D. <H6>"),
           ("A. Metropolitan Area Network", "B. Wide Area Network", "C. The Internet", "D. Local Area Network"),
           ("A. Multilevel index", "B. Primary index", "C. Clustering index", "D. Secondary index"),
           ("A. Loader", "B. Scanner", "C. Linker", "D. parser"),
           ("A. Query Processor", "B. Lock Manager", "C. Lock Table", "D. Query Optimizer"))
answers = ("D", "A", "D", "A", "D", "D", "C", "A", "D", "B")
guesses = []
score = 0

for question_num, question in enumerate(questions):
    print("--------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter Your Answer From : A To D : ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[question_num]}.")

print("--------------------------------")
print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
