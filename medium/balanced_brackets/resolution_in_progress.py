def balancedBrackets(string):
    openingBrackets = "([{"
    closingBrackets = ")]}"
    complementBrackets = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == complementBrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


# Predefined input
if __name__ == "__main__":
    predefined_input = "([{}])"  # Example input
    if balancedBrackets(predefined_input):
        print(f"The brackets in '{predefined_input}' are balanced!")
    else:
        print(f"The brackets in '{predefined_input}' are not balanced.")
