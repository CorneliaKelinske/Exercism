def latest(scores : list):
    return scores.pop()

def personal_best(scores : list):
    return max(scores)

def personal_top_three(scores : list):
    scores = sorted(scores)
    return scores[len(scores): -4 : -1]

print(personal_best((1, 3, 5)))