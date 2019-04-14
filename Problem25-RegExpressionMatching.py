"""
Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element
"""

def solution(reg, string):
    if not reg:
        return not string

    front_match = string and (reg[0] == string[0] or reg[0] == ".")

    if len(reg) > 2 and reg[1] == "*":
        return solution(reg[2:], string) or (front_match and solution(reg, string[1:]))
    else:
        return front_match and solution(reg[1:], string[1:])

assert solution("ra.", "ray")
assert not solution("ra.", "raymond")
assert solution(".*at", "chat")
assert not solution(".*at", "chats")



"""
if not reg:
    return not string

# reg not empty

front_match
have *


"""
