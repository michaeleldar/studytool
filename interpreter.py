import random
from sys import argv
from spellchecker import SpellChecker

# file = open(argv[1], 'r').read().splitlines()
file = open('example.sd', 'r').read().splitlines()

autocorrect = False
autocorrect_language = "english"
case_sensitive = False
mode = "elimination" # elimination is once u get one right it is removed, repeat all is that it all items are repeated until all are right, never repeat is where everything is asked once
feedback = True # Gives what the correct answer was if user gets wrong
answer = True # Tells user if they got it wrong or right
log = False

x = 1
part = 1
items = []
for line in file:
    if part == 2:
        if line == "":
            x += 1
            continue
        try:
            line.split(":")[1]
            items.append(line.split(":"))
        except:
            print(f"Error in line {x}")
            quit()

    elif line == "start":
        part = 2
        x += 1
        continue
    elif line == "autocorrect":
        autocorrect = True
    elif line == "spanish" or line == "french" or line == "portuguese" or line == "german" or line == "italian" or line == "russian" or line == "arabic" or line == "basque" or line == "latvian" or line == "dutch" or line == "persian":
        autocorrect_language = line
        autocorrect = True
    elif line == "case sensitive":
        case_sensitive = True
    elif line == "repeat all":
        mode = "repeat all"
    elif line == "no repeat":
        mode = "never repeat"
    elif line == "no feedback":
        feedback = False
    elif line == "no answer":
        feedback = False
        answer = False
    elif line == "log":
        log = True
        logfile = open(argv[2], 'w')
    elif line == "":
        x += 1
        continue
    else:
        print(f"Error in line {x}")
        quit()
    x += 1


if autocorrect_language == "arabic":
    spell = SpellChecker(language='ar')
elif autocorrect_language == "basque":
    spell = SpellChecker(language='eu')
elif autocorrect_language == "dutch":
    spell = SpellChecker(language='nl')
elif autocorrect_language == "english":
    spell = SpellChecker(language='en')
elif autocorrect_language == "french":
    spell = SpellChecker(language='fr')
elif autocorrect_language == "german":
    spell = SpellChecker(language='de')
elif autocorrect_language == "italian":
    spell = SpellChecker(language='it')
elif autocorrect_language == "latvian":
    spell = SpellChecker(language='lv')
elif autocorrect_language == "persian":
    spell = SpellChecker(language='fa')
elif autocorrect_language == "portuguese":
    spell = SpellChecker(language='pt')
elif autocorrect_language == "russian":
    spell = SpellChecker(language='ru')
elif autocorrect_language == "spanish":
    spell = SpellChecker(language='es')
else:
    spell = SpellChecker()


def report(string):
    if log:
        logfile.write(string)


original = [*items]
random.shuffle(items)

if mode == "elimination":
    x = 0
    wrong_answers = items
    while not wrong_answers == []:
        new_wrong_answers = []
        for item in wrong_answers:
            og_response = ""
            x += 1
            response = input(f"Q{x} {item[0]}: ")
            report(f"User response: {response}\n")
            if autocorrect == True:
                new_response = response.split(" ")
                og_response = response
                response = ""
                for word in new_response:
                    if response == "":
                       response = spell.correction(word)
                    else:
                       response = response + " " + spell.correction(word)
                report(f"User response autocorrected to: {response}\n")
            correct_answer = item[1]

            if not case_sensitive:
                response = response.lower()
                correct_answer = correct_answer.lower()

            if response == correct_answer or og_response == correct_answer:
                if answer:
                    print("Correct answer!")
                report("The user was correct\n\n\n")
            else:
                if answer:
                    print("Wrong answer")
                if feedback:
                    print(f"The correct answer was: {correct_answer}")
                report(f"The user was incorrect. The correct answer was: {correct_answer}\n\n\n")
                new_wrong_answers.append(item)
        random.shuffle(new_wrong_answers)
        wrong_answers = [*new_wrong_answers]

elif mode == "repeat all":
    x = 0
    wrong_answers = items
    correct = 0
    while not correct == wrong_answers.__len__():
        new_wrong_answers = []
        correct = 0
        for item in wrong_answers:
            og_response = ""
            x += 1
            response = input(f"Q{x} {item[0]}: ")
            report(f"User response: {response}\n")
            if autocorrect == True:
                new_response = response.split(" ")
                og_response = response
                response = ""
                for word in new_response:
                    if response == "":
                       response = spell.correction(word)
                    else:
                       response = response + " " + spell.correction(word)
                report(f"User response autocorrected to: {response}\n")
            correct_answer = item[1]

            if not case_sensitive:
                response = response.lower()
                correct_answer = correct_answer.lower()

            if response == correct_answer or og_response == correct_answer:
                if answer:
                    print("Correct answer!")
                report("The user was correct\n\n\n")
                new_wrong_answers.append(item)
                correct += 1
            else:
                if answer:
                    print("Wrong answer")
                if feedback:
                    print(f"The correct answer was: {correct_answer}")
                report(f"The user was incorrect. The correct answer was: {correct_answer}\n\n\n")
                new_wrong_answers.append(item)
        random.shuffle(new_wrong_answers)
        wrong_answers = [*new_wrong_answers]


elif mode == "never repeat":
    x = 0
    wrong_answers = items
    correct = 0
    while not wrong_answers == []:
        new_wrong_answers = []
        correct = 0
        for item in wrong_answers:
            og_response = ""
            x += 1
            response = input(f"Q{x} {item[0]}: ")
            report(f"User response: {response}\n")
            if autocorrect == True:
                new_response = response.split(" ")
                og_response = response
                response = ""
                for word in new_response:
                    if response == "":
                       response = spell.correction(word)
                    else:
                       response = response + " " + spell.correction(word)
                report(f"User response autocorrected to: {response}\n")
            correct_answer = item[1]

            if not case_sensitive:
                response = response.lower()
                correct_answer = correct_answer.lower()

            if response == correct_answer or og_response == correct_answer:
                if answer:
                    print("Correct answer!")
                report("The user was correct\n\n\n")
                correct += 1
            else:
                if answer:
                    print("Wrong answer")
                if feedback:
                    print(f"The correct answer was: {correct_answer}")
                report(f"The user was incorrect. The correct answer was: {correct_answer}\n\n\n")
        random.shuffle(new_wrong_answers)
        wrong_answers = [*new_wrong_answers]