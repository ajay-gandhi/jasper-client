
import re

WORDS = ["+", "-", "X", "DIVIDED"]

def handle(text, mic, profile):
    # Find all the numbers and which operations to do
    ops = re.findall(r'\b(\+|\-|X|divided)\b', text, re.IGNORECASE)    
    numbers = re.findall(r'\b\d+\b', text, re.IGNORECASE)

    result = int(numbers.pop(0))
    for i in range(len(ops)):
        next_num = int(numbers.pop(0))
        next_op  = ops.pop(0)

        result = {
            '+':   lambda x: result + x,
            '-':   lambda x: result - x,
            'X':   lambda x: result * x,
            'divided': lambda x: result / x
        }[next_op](next_num)

    mic.say("The result is %d." % result)

def isValid(text):
    # Valid if contains a math word
    return bool(re.search(r'\b(\+|\-|X|divided)\b', text, re.IGNORECASE))

