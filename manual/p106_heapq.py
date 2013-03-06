# Example from Pi Educational Manual v1.0 P. 106
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

import tempfile, heapq
# this is a generator (notice the yield)
def linesFromFile(sortedFile):
    while True:
        element = sortedFile.readline().strip()
        if not element:  # no element, so file is empty
            break
        yield element

# open the filmlist (this doesn't read anything yet)
films = open('p091_filmlist', 'r')
generatorList = [] 
while True:
    # read up-to 10 lines into an array
    elementsToSort = []
    for i in range(10):
        film = films.readline() # just reads one line
        if not film:
            break
        elementsToSort.append(film)
    # if no lines were read, we're done reading the very large file
    if not elementsToSort:
        break
    # create a temporary file and sort the 10 items into that file
    sortedFile = tempfile.TemporaryFile()
    for item in sorted(elementsToSort):
        sortedFile.write(bytes(item.encode()))
    # return this file to the start ready for
    # reading back by the heapq
    sortedFile.seek(0)
    # put the generator into the generatorList array;
    # remember this function isn't executed
    # until a loop requests the next value.
    generatorList.append(linesFromFile(sortedFile))

# use the magical heapq merge, which will merge two sorted lists 
# together but it will only pull the data in as it is needed
for element in heapq.merge(*generatorList):
    print(element.decode())
