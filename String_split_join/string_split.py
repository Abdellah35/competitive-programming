def split_and_join(line):
    # write your code here
    lineList = line.split(" ")
    
    return "-".join(lineList)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
