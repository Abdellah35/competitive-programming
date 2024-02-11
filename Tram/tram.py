import sys

class TraineCapacity:
    
    def minimumCapacity(self,k) -> int:
        minCapacity = 0
        previusPass = 0
        for i in range(k):
            exits, enters = map(int, sys.stdin.readline().split())
            currently = previusPass - exits + enters
            if currently > minCapacity:
                minCapacity = currently
            previusPass = currently

        
        return minCapacity
        
if __name__=='__main__':
    
    k = int(sys.stdin.readline())
    
    trc = TraineCapacity()
    
    print(trc.minimumCapacity(k))
