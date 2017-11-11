import itertools

stuff = [1, 2, 3,4]
#for L in range(0, len(stuff)+1):
for subset in itertools.permutations(stuff, 4):
    print(subset)