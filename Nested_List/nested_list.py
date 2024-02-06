if __name__ == '__main__':
    
    records = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.add(score)
    second = sorted(scores)[1]
    result = sorted([record[0] for record in records if record[1] == second]) 
    for name in result:
        print(name)
