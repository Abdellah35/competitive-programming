if __name__ == '__main__':
    N = int(input())
    myList = []
    for i in range(1,N + 1):
        comand = input()
        command = comand.split(' ')
        if 'append' in command:
            myList.append(int(command[1]))
        elif 'insert' in command:
            myList.insert(int(command[1]), int(command[2]))
        elif 'remove' in command:
            myList.remove(int(command[1]))
        elif 'sort' in command:
            myList.sort()
        elif 'pop' in command:
            myList.pop()
        elif 'reverse' in command:
            myList.reverse()
        else:
            print(myList)
