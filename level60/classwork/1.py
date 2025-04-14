def max_possible_score(points, seen): 
    score = 0
    
    for i in points:
        if i in seen:
            score += points[i] * 2
        else: 
            score += points[i]
    return score