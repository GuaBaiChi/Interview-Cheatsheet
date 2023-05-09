stack = []

source = """
function test() {
    for (let i = 0; i < 4; i++) {
        console.log(i);
    } 
}
"""
counter = 0

for char in source:
    print(counter)
    counter += 1
    if char == "{" or char == "(":
        stack.append(char)
    elif char == "}":
        lastItem = stack.pop()
        if lastItem != "{":
            raise Exception("INVALID SYNTAX")

    elif char == ")":
        # lastItem = stack.pop(source[char])
        lastItem = stack.pop()
        if lastItem != "(":
            raise Exception("INVALID SYNTAX")
    print(stack)
