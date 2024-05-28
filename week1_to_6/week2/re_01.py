# def score_avg():
#     scores = input("Input score: ").split(" ") 
#     if scores[0] == 'q':
#         return None
#     for score in scores:
#         if not score.isdigit():
#             return "%% Type Error %%"
#         if int(score) > 100 or int(score) < 0:
#             return "%% Range Error %%"
#     avg = sum(map(int, scores)) / len(scores)
#     return f"Final term average for {len(scores)} courses is: {avg:.2f}"

# print(score_avg())

def score_avg():
    scores = input("Input score: ").split(" ")
    if scores[0].lower() == 'q':
        return None
    
    for score in scores:
        try:
            score_float = float(score)
        except ValueError:
            return "%% Type Error %%"
        
        if score_float > 100 or score_float < 0:
            return "%% Range Error %%"
    
    avg = sum(map(float, scores)) / len(scores)
    return f"Final term average for {len(scores)} courses is: {avg:.2f}"

print(score_avg())