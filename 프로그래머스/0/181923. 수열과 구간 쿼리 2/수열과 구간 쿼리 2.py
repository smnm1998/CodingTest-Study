def solution(arr, queries):
    results = []
    
    for s, e, k in queries:
        valid = [
            x for x in arr[s:e+1] if x > k
        ]
        
        if valid:
            results.append(min(valid))
        else:
            results.append(-1)
            
    return results