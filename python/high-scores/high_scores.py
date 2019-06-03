def latest(scores):
    return scores.pop()

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    scores = sorted(scores)
    return scores[len(scores): -4 : -1]
  

