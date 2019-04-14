"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def solution(expression):
    s = []
    closing = {")":"(","}":"{","]":"["}

    for c in expression:
        if c in closing:
            if not s or s.pop() != closing[c]:
                return False
        else:
            s.append(c)
    return True

assert solution("([])[]({})")
assert not solution("([)]")


