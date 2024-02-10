import sys

class WrongSubstraction:
    
    def substraction(self,number,k) -> int:
        for i in range(k):
            if number % 10 == 0:
                number //= 10
            else:
                number -= 1
        return number
        
if __name__=='__main__':
    
    number, k = map(int, sys.stdin.readline().split())
    
    sbc = WrongSubstraction()
    
    print(sbc.substraction(number, k))
