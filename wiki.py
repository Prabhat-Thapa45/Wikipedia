import random
import wikipedia


def get_wiki_info(value):
    try:
        print(wikipedia.summary(value, auto_suggest=True))
    except wikipedia.exceptions.DisambiguationError as e:
        s = random.choice(e.options)
        for i, j in zip(range(1, 11), e.options[:10]):
            print(i, j)
        value = input("Enter the number beside the option or new word:\n")
        try:
            value = int(value)
            print(wikipedia.summary(e.options[value-1]))
        except ValueError as err:
            print(wikipedia.summary(value))
while True:
    search_value = input("Enter name for search:\n")
    get_wiki_info(search_value)
    yes_no = input("Type Y/y for next search.\n")
    if yes_no.upper() != "Y":
        break
