import json

points = 0


def succes(points):
    print("To dobra odpowiedź, brawo! Masz już", points, "punktów.")
def wrong_answer(correct_answer):
    print("To zła odpowiedź, prawidłowa odpowiedź to " + correct_answer + ".")

def show_question(question):
    global points

    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    answer = input("Ktorą odpowiedź wybierasz? ")

    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        succes(points)
    else:
        wrong_answer(question["prawidłowa_odpowiedź"])


with open("quiz.json", encoding="utf-8") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        show_question(questions[i])

print()
print("Zdobyłeś/aś liczba punktów to " + str(points) + ".")
