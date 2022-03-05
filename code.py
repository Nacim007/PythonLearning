# HackerRank useful project
# --------------------------
print('Hello  world')

def permutations(x, y, z, n):
    res = list()
    for i in range(x + 1):
        for j in range(y + 1):
            res.append(j)
    return res

#print(permutations())


def sommation():
    x = int(input("Enter a value for x:"))
    y = int(input("Enter a value for y:"))
    z = int(input("Enter a value for z:"))
    n = int(input("Enter a value for n:"))
    res = list()
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if k + j + i != n:
                    res.append([i, j, k])
    return res

#print(sommation())


def runnerUp():
    n = int(input())
    arr = map(int, input().split())
    liste = list(arr)
    sort = sorted(liste,reverse=True)
    res = list()
    for i in range(n):
        if sort[0] != sort[i]:
            res.append(sort[i])
    return max(res)

#print(runnerUp())


def score():
    name = list()
    score = list()
    n = int(input("Enter the number of participant:"))
    for i in range(n):
        name.append(input("Enter his name:"))
        score.append(float(input("Enter his score:")))

    d = dict(zip(name, score))

    score_ordered = sorted(score)
    res = 0
    for i in range(n):
        if score_ordered[0] < score_ordered[i]:
            res = score_ordered[i]
            break
    found_key = [key for key, value in d.items() if value == res]
    found_key_ord = sorted(found_key)
    for el in found_key_ord:
        return el

#print(score())


def moyenne():
    n = int(input("Enter the n° of participant:"))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Name and score in a single line:").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter the name that you want:")
    moyenne = sum(student_marks.get(query_name))/len(student_marks.get(query_name))

    return '%.2f' % moyenne

#print(moyenne())

def liste():
    N = int(input())
    res=list()
    for i in range(N):
        command, *line = input().split()
        value = list(map(int, line))
        if command == 'print':
            print(res)
        elif command == 'append':
            res.append(value[0])
        elif command == 'insert':
            res.insert(value[0],value[1])
        elif command == 'remove':
            res.remove(value[0])
        elif command == 'pop':
            res.pop(-1)
        elif command == 'sort':
            res.sort()
        elif command == 'reverse':
            res.reverse()


def hashing():
    """
    map():Returns a list of the results after applying the given function
    to each item of a given iterable (list, tuple etc.)
    """
    n = int(input("Enter a number:"))
    integer_list = map(int,input("Enter n number:").split())
    integer_list = tuple(integer_list)
    return integer_list

#print(hashing())

"""import numpy

def arrays(arr):
    arr = list(reversed(arr))
    arr_array = numpy.array(arr, float)
    return (arr_array)

#arr = input("Enter a serie of number:").strip().split(' ')
#result = arrays(arr)
#print(result)

def matrix():
    ls = list(map(int, input("Enter a serie of number:").split()))
    my_array = numpy.array(ls)
    return(numpy.reshape(my_array, (3, 3)))

#print(matrix())"""

def swap_case():
    s = input("Enter the phrase:")
    res = list()
    for letter in s:
        if letter.isupper():
            res.append(letter.lower())
        elif letter.islower():
            res.append(letter.upper())
        elif letter == ' ':
            res.append(' ')
        else:
            res.append(letter)
    return "".join(res)

#print(swap_case())

def split_join():
    line = input("Enter a phrase:")
    res = list()
    for letter in line:
        if letter == " ":
            res.append('-')
        else:
            res.append(letter)
    return "".join(res)

#print(split_join())

def name():
    prenom = input("Prenom:")
    nom = input("Nom:")
    return ('Hello %s %s! You just delved into python.' %(prenom,nom))

#print(name())

def mutations():
    word = input("Enter a word:")
    n = int(input("Enter a number:"))
    letter = input("Enter a letter:")
    string = word[:n] + letter + word[n+1:]
    return string

#print(mutations())


def median():
    arr = list(map(int, input("Enter a serie of n°:").rstrip().split()))
    arr_sorted =sorted(arr)
    mid = int((len(arr_sorted)+1)/2)
    return arr_sorted[mid-1]

print(median())

