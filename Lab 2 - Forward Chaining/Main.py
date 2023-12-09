facts = []
rules = []

def read_facts():
    with open("FactsDB.txt", "r") as f:
        lines = f.read().splitlines()
        facts.extend(lines)

def read_rules():
    with open("RulesDB.txt", "r") as f:
        lines = f.read().splitlines()
        rules.extend(lines)

read_rules()
read_facts()

def input_fact(input_string):
    str1 = parseString(input_string)
    if str1 not in facts:
        facts.append(str1)
        file_name = "FactsDB.txt"
        with open(file_name, "a") as f:
            f.write(str1 + "\n")
    else:
        print("Fact already exist in the database.")

    print_f_and_r()

def input_rules(input_string):
    str1 = parseString(input_string)
    if str1 not in rules:
        rules.append(str1)
        file_name = "RulesDB.txt"
        with open(file_name, "a") as f:
            f.write(str1 + "\n")
    else:
        print("Rule already exist in the database.")

    print_f_and_r()

def generate_new_fact():
    new_facts = []
    for rule in rules:
        if "then" in rule:
            conditions, consequent = rule.split(", then ")
            list_of_conditions = conditions.replace("if ", "").split(" and ")

            if all(fact in facts for fact in list_of_conditions) and consequent not in facts:
                new_facts.append(consequent)
        else:
            print("Please input a valid format!")
            
    print("\n")
    if new_facts:
        facts.extend(new_facts)
        print("Newly generated facts: ", new_facts)
        with open("FactsDB.txt", "a") as f:
            for fact in new_facts:
                f.write(fact + "\n")

        generate_new_fact()
    else:
        print("No facts can be generated anymore.")

def parseString(input_string):
	str1 = input_string.lower()
	return str1

def print_f_and_r():
    print("\nFacts: ", facts)
    print("\nRules: ", rules)

while True:
    print("\n[1]Input fact\t[2]Input rules\t[3]Generate new facts\t[4]Print Facts and Rules\t[5]Exit")
    user_input = input("\nInput: ")

    try:
        user_input_as_int = int(user_input)  # Convert the input to an integer

        if user_input_as_int == 5:
            break
        elif user_input_as_int == 1:
            input_string_fact = input("Input the fact: ")
            input_fact(input_string_fact)
        elif user_input_as_int == 2:
            input_string_rules = input("Input the rules: ")
            input_rules(input_string_rules )
        elif user_input_as_int == 3:
            generate_new_fact()
        elif user_input_as_int == 4:
            print_f_and_r()
        else:
            print("\nInvalid input. Please enter a valid option (1, 2, 3, or 4).")

    except ValueError:
        print("\nInvalid input. Please enter a valid integer (1, 2, 3, or 4).")
