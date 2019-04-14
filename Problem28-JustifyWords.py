"""
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
"""

def solution(words, k):
    sentences = []
    sentence = []
    count = k
    for word in words:
        #import pdb;pdb.set_trace()
        n = len(word) if len(sentence) == 0 else len(word) + 1
        if count - n <= 0:
            sentences.append(sentence)
            count = k
            sentence = []
        count = count - n
        sentence.append(word)
    # Add at end
    if sentence:
        sentences.append(sentence)
    new_sentences = []

    for sentence in sentences:
        spaces = k - sum(map(lambda x:len(x), sentence))

        slots = len(sentence) - 1
        if slots == 0:
            print("HERE")
            new_sentences.append(sentence[0] + " "*spaces)
            continue

        min_space = spaces//slots
        num_larger_space = spaces % slots
        new_sentence = []
        for word in sentence[:-1]:

            new_sentence.append(word)
            space = " " * (min_space+1) if num_larger_space else " "*min_space
            new_sentence.append(space)
            if num_larger_space:
                num_larger_space -= 1
        new_sentence.append(sentence[-1])
        new_sentences.append("".join(new_sentence))
    return new_sentences

print(solution( ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16))
print(solution( ["this", "is", "therapeutic"], 13))
