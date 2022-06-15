
testlst = [0, 1, 2]

def test(lst):
    lst[1] = 3
    return lst

test(testlst)

print(testlst)