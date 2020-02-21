'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"***
occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    result = []
    if len(word) < 2:
        return 0

    def helper(val):
        if len(val) < 2:
            return

        word_list = list(val)
        th = word_list[0] + word_list[1]
        if th == 'th':
            result.append(1)
        word_list.pop(0)
        new_word = ''.join(word_list)

        helper(word_list)

    helper(word)

    return len(result)
