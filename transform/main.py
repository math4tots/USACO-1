def in_list(chara_line):
    '''
    chara_line is one line of a whole chara pattern

    '''
    temp = []
    for chara in chara_line:
        temp.append(chara)
    return temp



def convert(chara_pattern):
    '''
        Takes '@' and converts it to 1
        Takes '-' and converts it to 0

    '''


    converted = []
    for row in chara_pattern:
        line = []
        for chara in row:
            if chara == '@':
                line.append(1)
            else:
                line.append(0)
        converted.append(line)

    return converted

# print(convert([['@', '-', '@'], ['-', '-', '-'], ['@', '@', '-']]))

def check(pattern, real, N):
    '''
    if the new pattern and the real pattern are the same then it
    returns True. Else, it will return False

    '''
    if pattern == real:
        return True

def lst_maker(N):
    '''
    Creates an empty list of N lists

    '''
    lst = []
    for x in range(N):
        lst.append([])
    return lst

def ninetydegrees(pattern, N):
    '''
    Pattern is a list of lists
    N is the number of rows/columns

    Creates list of lists that have been transformed
    90 degrees

    Returns T if this pattern is the same as the real product


    '''
    temp = lst_maker(N)
    for row in pattern:
        for i in range(len(row)):
            temp[i].append(row[i])
    # print(temp)
    new = []
    for t in temp:
        # print(f"New row {t}")
        new.append(t[::-1])

    return new

def one_eighty(pattern, N):
    '''
    Does an additional 90 degrees to ninetydegrees(pattern, N)
    '''
    return ninetydegrees(ninetydegrees(pattern, N), N)

def two_seventy(pattern, N):
    return ninetydegrees(one_eighty(pattern, N), N)

def reflection(pattern, N):
    new = []
    for row in pattern:
        new.append(list(reversed(row)))
    return new

def combination(pattern, N):
    '''
    It takes the pattern and reflects it horizontally. Then it returns
    a new pattern that has been subjected to other transformation

    However, problem- There are three possible patterns that combination
    may produce.

    IDEA:
    Have a list that contains all of that. When at solve function, split this up
    specifically for combination
        -) Doesn't feel very efficient

    '''
    all_patterns = []
    new = reflection(pattern, N)
    all_patterns.append(ninetydegrees(new, N))
    all_patterns.append(one_eighty(new, N))
    all_patterns.append(two_seventy(new, N))

    return all_patterns

def solve(pattern, real, N):
    '''
    Checks to see if any of the combination creates
    an identical image as the real image.
    If so, return the corresponding pattern number
    Else, return invalid transtormation (#7)

    '''
    possible = []
    # print(reflection(pattern, N))
    if pattern == real:
        return 6
    if check(ninetydegrees(pattern, N), real, N):
        possible.append(1)

    if check(one_eighty(pattern, N), real, N):
        possible.append(2)

    if check(two_seventy(pattern, N), real, N):
        possible.append(3)

    if check(reflection(pattern, N), real, N):
        possible.append(4)

    for pat in combination(pattern, N):
        if check(pat, real, N):
            possible.append(5)
    if not possible:
        return 7
    # print(possible)
    return min(possible)



N = int(input())
chara_pattern1 = []
for n in range(N):
    chara_pattern1.append(in_list(input()))

#Remember when doing send.py I need to specify that it's a string

pattern = convert(chara_pattern1)

chara_pattern2 = []
for x in range(N):
    chara_pattern2.append(in_list(input()))

real = convert(chara_pattern2)

print(solve(pattern, real, N))










# assert solve([[1, 0, 1], [1, 1, 0], [1, 0, 1]], [[1, 1, 0], [1, 1, 0], [1, 1, 0]], 3) == 7, solve([[1, 0, 1], [1, 1, 0], [1, 0, 1]], [[1, 1, 0], [1, 1, 0], [1, 1, 0]], 3)
# assert solve([[1, 0], [0, 0]], [[0, 1], [0, 0]], 2) == 1, solve([[1, 0], [0, 0]], [[0, 1], [0, 0]], 2)
#^^^ For whateve reason possible is not giving me the expected
# assert solve([[1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]], [[1, 0, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 0]], 4) == 4, solve([[1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]], [[1, 0, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 0]], 4)
# assert solve([[1, 0], [0, 1]], [[1, 1,], [1, 1]], 2) == 7
# assert solve([[1, 1, 0], [0, 1, 0], [1, 0, 0]], [[0, 0, 0], [0, 1, 1], [1, 0, 1]], 3) == 5, solve([[1, 1, 0], [0, 1, 0], [1, 0, 0]], [[0, 0, 0], [0, 1, 1], [1, 0, 1]], 3)
# assert solve([[1, 0], [0, 1]], [[1, 1], [1, 1]], 2) == 7, solve([[1, 0], [0, 1]], [[1, 1], [1, 1]], 2)






# assert solve([[1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]], [[1, 0, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 1]], 4) == 2, solve([[1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]], [[1, 0, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 1]], 4)
# assert solve([[0]], [[0]], 1) == 6, solve([[0]], [[0]], 1)
# assert solve([[1, 0, 1], [0, 0, 0], [1, 1, 0]], [[1, 0, 1], [1, 0, 0], [0, 0, 1]], 3) == 1, solve([[1, 0, 1], [0, 0, 0], [1, 1, 0]], [[1, 0, 1], [1, 0, 0], [0, 0, 1]], 3)
# assert solve([[1, 0, 1], [0, 0, 0], [1, 1, 0]], [[1, 1, 0], [0, 0, 0], [1, 0, 1]], 3) == 4, solve([[1, 0, 1], [0, 0, 0], [1, 1, 0]], [[1, 1, 0], [0, 0, 0], [1, 0, 1]], 3)















