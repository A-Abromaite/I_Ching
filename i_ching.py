from random import randint

results = []
trigram1 = []
trigram2 = []

# heads or tails
def toss():
    result = randint(0, 1)
    if result == 0:
        return "Heads"
    else:
        return "Tails"

# tossing 3 coins
def generate_results():
    results.clear()
    for i in range(3):
        results.append(toss())
    cast_results()
    # print(results)

# casting results
def cast_results():
    global results
    if results in [["Heads", "Heads", "Tails"], ["Heads", "Tails", "Heads"], ["Tails", "Heads", "Heads"]]:
        return ("_____")
    elif results in [["Tails", "Tails", "Heads"], ["Tails", "Heads", "Tails"], ["Heads", "Tails", "Tails"]]:
        return ("__ __")
    elif results == ["Heads", "Heads", "Heads"]:
        return ("_____.")
    else:
        return ("__ __.")

# building trigram 1
def build_trigram1():
    # trigram = []
    i = 0
    while i < 3:
        if input("Press enter to toss coins...") == "":
            results = generate_results()
            trigram1.append(cast_results())
            i += 1
        print(trigram1)

# building trigram 2
def build_trigram2():
    i = 0
    while i < 3:
        if input("Press enter to toss coins...") == "":
            results = generate_results()
            trigram2.append(cast_results())
            i += 1
        print(trigram2)


# determining changes
def change(line):
    if line == "_____.":
        return "__ __"
    elif line == "__ __.":
        return "_____"
    else:
        return line

# displaying the final hexagram
def display_hexagram():
    print("Full Trigram 2: ", end="")
    print(*trigram2, sep=" ")
    print("Full Trigram 1: ", end="")
    print(*trigram1, sep=" ")

    if "_____." in trigram2 or "__ __." in trigram2 or "_____." in trigram1 or "__ __." in trigram1:
        modified_trigram2 = [change(line) for line in trigram2]
        modified_trigram1 = [change(line) for line in trigram1]
        print("Your situation will change soon")
        print("Modified Trigram 2: ", end="")
        print(*modified_trigram2, sep=" ")
        print("Modified Trigram 1: ", end="")
        print(*modified_trigram1, sep=" ")

build_trigram1()
build_trigram2()

display_hexagram()