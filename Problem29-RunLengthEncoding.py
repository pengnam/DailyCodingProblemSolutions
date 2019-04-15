"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""

def solution(string):
    letter = None
    count = None
    result = []

    for c in string:
        if c != letter:
            if letter:
                result.append("%d%s"%(count, letter))
            letter = c
            count = 1
        else:
            count += 1
    if letter:
        result.append("%d%s"%(count, letter))
    return "".join(result)

print(solution("AAABBCD"))


