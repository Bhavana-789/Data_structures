from stack import Stack


def is_balanced(exp):
    s = Stack()
    bracket = {'(': ')', '{': '}', '[': ']'}

    for char in exp:
        if char in ['(', '{', '[']:
            s.push(char)
        else:
            if s.is_empty():
                return 'False'
            else:
                top = s.pop()
                if bracket[top] != char:
                    return 'False'

    if s:
        print("Expression is correctly parenthesized")
    else:
        print("Expression is not correctly parenthesized")


if __name__ == "__main__":
    print(is_balanced("()"))
