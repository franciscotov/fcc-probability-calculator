import random
import copy
class Hat:
    contents = list()
    def __init__(self, **data):
        #print(dir(self.l))
        li = list()
        for k,v in data.items():
            for i in range(v):
                #print(k)
                #self.l.insert(len(self.l)+1,k)
                li.append(k)
        li.sort(reverse= True)
        self.contents = li
        #print(self.l)
    
    def draw(self, num):
        #print('there are these balls: ', self.contents)
        if num > len(self.contents): return self.contents
        else:
            e = list()
            #newList = copy.deepcopy(self.contents)
            while num > 0:
                #ele = random.choice(newList)
                #newList.remove(ele)
                ele = random.choice(self.contents)
                self.contents.remove(ele)
                e.append(ele)
                num -= 1
            #print(newList)
            return e
#hat, expected_balls, num_balls_drawn, num_experiments
def experiment(**args):
    expected = list()
    balls = list()
    M = 0
    num_exp = args['num_experiments']
    '''
    for k,v in args['expected_balls'].items():
        for i in range(v):
            expected.append(k)
    '''
    d = dict()
    #print(d['h'] > 0, 'oooooo')
    while(args['num_experiments'] > 0):
        new_hat = copy.deepcopy(args['hat'])
        balls = new_hat.draw(args['num_balls_drawn'])
        #print('received this balls: ', balls)
        newdic = dict()
        for k,v in args['expected_balls'].items():
            for ball in balls:
                if(len(newdic) > 1 ):
                    try:
                        if(newdic[k] >= v): continue
                    except: pass
                if ball == k:
                    try: newdic[k] += 1
                    except: newdic[k] = 1
                else: continue
        #print(newdic, 'get this dictionary')
        boolean = True
        for k,v in args['expected_balls'].items():
            try:
                val = newdic[k]
                if val < v: boolean = False
            except: boolean = False
        if boolean == True: M += 1
        #if len(newdic) == len(args['expected_balls']):
        #print('this is value m: ', M)
        args['num_experiments'] -= 1
    #print('this is value m: ', M, num_exp)
    return M/num_exp