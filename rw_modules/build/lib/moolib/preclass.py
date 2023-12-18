def askq():
    print('Please answer the following questions honestly for the best recommendation. These questions are selected based on significant research. The answers are never stored or used beyond the functioning of this app. :)')
    q1 = 'How is your day going?'
    q2 = 'Does your favorite food seem appealing to you right now?'
    q3 = 'How does thinking about your favorite color(s) make you feel at the moment?'
    a1 = str(input(q1))
    a2 = str(input(q2))
    a3 = str(input(q3))
    qas = a1 + '\n' + a2 + '\n' + a3
    
    return qas

def askqnr(qnr:list):
    ans = []
    for i in range(len(qnr)):
        ai = str(input(qnr[i]))
        ans.append(ai)
    return ans

def prepqnr(qnrpath):
    with open(qnrpath, r) as qnrf:
        return qnrf.readlines()

def prepdata(data):
    with open('./data/emot.txt', w) as dafi:
        dafi.writelines(data)

if __name__ == '__main__':
    print('preclass')