int = 4
intArr = [1,9,8,90,400,4]

def main(int,intArr):
    exists = existsIntegerInArray(int,intArr)
    if exists != True:
        print(-1)
    else:
        index = getIndex(int,intArr)
        print(index)
    
def existsIntegerInArray(i,arr):
    if i in arr:
        return True

def getIndex(i,arr):
    for x,v in enumerate(arr):
        if v == i:
            return x


main(int,intArr)