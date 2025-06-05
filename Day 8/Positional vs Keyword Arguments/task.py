# Functions with input

def greet_with_name(name, location):
    print(f"Hello {name}, who lives in {location}")
    print(f"How do you do {name}?")


# greet_with_name("Jack Bauer", "London")
# greet_with_name(location="Mumbai", name="Alto")

def calculate_love_score(name1, name2):
    name = (name1 + name2).lower()
    # print(name)
    count1, count2 = 0, 0
    # count2 = 0
    # print(f"{count1}{count2}")
    for i in "true":
        # print(i)
        if i in name:
            count1 += name.count(i)
            # print(count1)
    for i in "love":
        if i in name:
            count2 += name.count(i)

    print(f"Love Score = {count1}{count2}")

calculate_love_score(name1="Angela Yu", name2="Jack Bauer")
