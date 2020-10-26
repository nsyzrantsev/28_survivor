# https://skillsmart.ru/algo/lvl1/cb0f.html

def MassVote(N, votes):
    max_vote = max(votes)
    votes_dict = dict()
    percent = max_vote/(sum(votes))*100
    for i in votes:
        if i in votes_dict:
            votes_dict[i] += 1
        else:
            votes_dict[i] = 1
    if votes_dict[max_vote] > 1:
        return 'no winner'
    elif percent > 50:
        return f'majority winner {votes.index(max_vote)+1}'
    elif percent <= 50:
        return f'minority winner {votes.index(max_vote)+1}'
