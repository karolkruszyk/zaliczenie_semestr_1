import json

def show_question(question, points):
    print(question["pytanie"])
    print("a. " + question["a"])
    print("b. " + question["b"])
    print("c. " + question["c"])
    print("d. " + question["d"])
    guess = validate()
    if guess == question["poprawna_odpowiedz"]:
        print("Dobrze!")
        points += 1
    else:
        print("ŹLE!")
        print("Poprawna odpowiedź to " + question["poprawna_odpowiedz"])
    return points
def give_mark(points, max_score):
    if points < max_score * 41/100:
        mark = "niedostateczna"
    elif points < max_score * 51/100:
        mark = "dopusczająca"
    elif points < max_score * 71/100:
        mark = "dostateczna"
    elif points < max_score * 86/100:
        mark = "dobra"
    elif points < max_score * 98/100:
        mark = "bardzo dobra"
    elif points <= max_score * 100/100:
        mark = "celująca"
    return mark
def validate():
    guess = input("Wybierz: ")
    guess = guess.lower()
    while len(guess) != 1 or (guess != "a" and guess != "b" and guess != "c" and guess != "d"):
        if len(guess) != 1:
            guess = input("Podaj jedną literę: ")
            guess = guess.lower()
        else:
            guess = input("Wybierz opcję od 'a' do 'd': ")
            guess = guess.lower()
    return guess

points = 0
max_score = 0
with open("test.json") as q_file:
    questions = json.load(q_file)

for i in range(0, len(questions)):
    points = show_question(questions[i], points)
    max_score += 1

print("Zdobyłeś", points, "punktów i uzyskałeś ocenę", give_mark(points, max_score))



