# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phoneDict = {}
for i in range(n):
    receive = input()
    name_phone = receive.split(' ')
    phoneDict[name_phone[0]] = name_phone[1]

while True:
    try:
        name = input()
        if name in phoneDict:
            print(name, '=', phoneDict[name], sep='')
        else:
            print('Not found')
    except EOFError:
        break
