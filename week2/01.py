def score_avg():
    #### Your Code Here ####
    # input list of scores
    scores = list(map(float, input("Input score: ").split(" ")))
    print(scores)
    # if input is 'q', return None
    if scores[0] == 'q':
        return None
    # if input is not float "%% Type Error %%"
    for score in scores:
        if type(score) != float or score != 'q':
            return "%% Type Error %%"
        # if input is over 100 or under 0, "%% Range Error %%"
        if score > 100 or score < 0:
            return "%% Range Error %%"
    avg = sum(scores) / len(scores)
    
    return f"Final term average for {len(scores)} courses is: {avg:.2f}"

score_avg()


#    scores = list(map(float, input("Input score: ").split(" ")))