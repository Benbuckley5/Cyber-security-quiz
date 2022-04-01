import random

number_of_questions = 20

input_text = open("Quiz input.txt", "r")

raw_text = input_text.read()
l1 = raw_text.split("\n")
l2 = []
#print(l1)
for i in l1:
    if ":" in i:
        l2.append(i.split(":"))
dict1 = {}
for a in range(len(l2)):
    dict1[l2[a][0]] = l2[a][1]



def quiz_body():
    correct = 0
    incorrect = 0
    random.shuffle(l2)
    unused_indexes = list(range(number_of_questions))
    for i in unused_indexes:
        print(f"Please define {l2[i][0]}: ")
        answer_set = [l2[i][1]]
        while True:
            wrong_answer1 = random.choice(l2)
            if wrong_answer1[1] != l2[i][1]:
                answer_set.append(wrong_answer1[1])
                break
        while True:
            wrong_answer2 = random.choice(l2)
            if wrong_answer2[1] != l1[i][1]:
                if wrong_answer2[1] != wrong_answer1[1]:
                    answer_set.append(wrong_answer2[1])
                    break
        random.shuffle(answer_set)
        print(f"\n A: {answer_set[0]}\n\n B: {answer_set[1]}\n\n C: {answer_set[2]}\n\n")
        answer = input()
        if answer == "A":
            if answer_set[0] == l2[i][1]:
                print("\nCorrect!\n")
                correct += 1
                continue
        if answer == "B":
            if answer_set[1] == l2[i][1]:
                print("Correct!")
                correct += 1
                continue
        if answer == "C":
            if answer_set[2] == l2[i][1]:
                print("Correct!")
                correct += 1
                continue
        else:
            print("incorrect :(")
            incorrect += 1
    score = number_of_questions - incorrect
    print(f"\n\n Finished! \n\nYour total score is {score}!")

quiz_body()

input_text.close()