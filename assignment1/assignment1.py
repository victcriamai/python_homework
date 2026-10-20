# Write your code here.
# pytest -v -x assignment1-test.py

print()

#Task 1: Hello
def hello():
    return("Hello!")

hello()

#Task 2: Greet with a Formatted String
def greet(name):
    return(f"Hello, " + name + "!")

greet("Name")

#Task 3: Calculator

def calc(num1, num2, operation = "multiply"):
    try:
        if operation == "add":
            return(num1+num2)
        if operation == "subtract":
            return(num1-num2)
        if operation == "divide":
            return(num1/num2)
        if operation == "modulo":
            return(num1%num2)
        if operation == "int_divide":
            return(num1//num2)
        if operation == "power":
            return(num1**num2)
        else:
            return(num1*num2)
    
    except ZeroDivisionError:
        return("You can't divide by 0!")
    except TypeError:
        return("You can't multiply those values!")


#Task 4: Data Type Conversion
def data_type_conversion(value, type_name):
    try:
        if type_name == "str":
            value = str(value)
            return(value)
        
        if type_name == "int":
            value = int(value)
            return(value)

        if type_name == "float":
            value = float(value)
            return(value)


    except ValueError:
        return(f"You can't convert {value} into a {type_name}.")
    

#Task 5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args)/len(args)
        if average >= 90:
            return("A")
        if average <= 89 and average >= 80:
            return("B")
        if average <= 79 and average >= 70:
            return("C")
        if average <= 69 and average >= 60:
            return ("D")
        if average < 60:
            return ("F")
    except TypeError:
        return("Invalid data was provided.")


#Task 6: Use a For Loop with a Range
def repeat(string, count):
    for i in range(int(count +1)):
        new_string = string*i
    return(new_string)

#Task 7: Student Scores, Using **kwargs
def student_scores(*args, **kwargs):
    if "mean" in args:
        mean = sum(kwargs.values())/len(kwargs)
        return mean
    if "best" in args:
        best = max(kwargs.values())
        for key, value in kwargs.items():
            if value == best:
                return key


#Task 8: Titleize, with String and List Operations
def titleize(string):
    words = string.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    new_words = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1:
            new_words.append(word.capitalize())
        elif word in little_words:
            new_words.append(word.lower())
        else:
            new_words.append(word.capitalize())
    return " ".join(new_words)

#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = []
    for letter in secret:
        if letter in guess:
            result.append(letter)
        else:
            result.append("_")
    return "".join(result)



#Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    new_words = []
    vowels = ["a","e","i","o", "u"]
    split_sentence = sentence.split()

    for word in split_sentence:
        for i, letter in enumerate(word):
            if word[i:i+2] == "qu":
                translated = word[i+2: ]+word[:i+2] + "ay"
                new_words.append(translated)
                break
            if letter in vowels:
                translated = word[i:] + word[:i] + "ay"
                new_words.append(translated)
                break
    return " ".join(new_words)


