'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    result = []
    if len(word) < 2:
        return 0
    
    # result = 0
    
        
    def helper(val):
        if len(val) < 2:
            return

        l = list(val)
        th = l[0] + l[1]
        if th == 'th':
            # result += 1
            print('yes')
            result.append(1)
        l.pop(0)
        new_word = ''.join(l)

        helper(l)
 
    helper(word)


    
    return  len(result)


print(count_th('ththth'))
