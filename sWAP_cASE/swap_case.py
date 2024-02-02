def swap_case(s):
    me = ''
    for ch in s:
        if ch.isupper():
            me += ch.lower()
        else:
            me += ch.upper()
            
    return me

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
