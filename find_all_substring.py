def find_all(string, substr):
    '''Find all the indexs of substring in string.'''
    
    #Initialize start index
    i = -1

    #Creat a empty list to store result
    result = []

    while True:
        i = string.find(substr, i+1)
        if i < 0:
            break
        result.append(i)

    return result

if __name__ == '__main__':

    string = input('Please input your string : ')
    substr = input("Please input your substring : ")

    print('Result : ', find_all(string, substr))
