class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.dictVal = {}
        self.outId = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        posibleChunk = []
        if idKey == self.outId + 1:
            posibleChunk.append(value)
            self.outId += 1
        else:
            self.dictVal[idKey] = value

        for i in range(self.outId, self.n):
            if i + 1 in self.dictVal:
                    posibleChunk.append(self.dictVal[i + 1])
                    self.outId += 1
            else:
                break
                
        return posibleChunk





# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
