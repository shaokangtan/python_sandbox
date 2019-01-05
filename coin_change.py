
"""
coin changes is a integer partition question
reference :
https://www.youtube.com/watch?v=ZaVM057DuzE
https://www.youtube.com/watch?v=PafJOaMzstY
tips for integer partition :
1. exlude new coin
2. include  new coin
3. 1 + 2

time complexity is target * coins

"""
import time, datetime

changes = []
changes_list = []
memoization_used = 0
iterations = 0
def test_rec_coin_dynam(target,coins,known_results):
    saved = 0
    iterations = 0
    changes.clear()
    changes_list.clear()
    start_time = time.time()
    num =  rec_coin_dynam(target,coins,known_results)
    end_time = time.time()

    uptime = end_time - start_time

    print ("{}, {}".format(datetime.timedelta(seconds=int(uptime)),uptime))
    return num

def rec_coin_dynam(target,coins,known_results):
    '''
    INPUT: This funciton takes in a target amount and a list of possible coins to use.
    It also takes a third parameter, known_results, indicating previously calculated results.
    The known_results parameter shoud be started with [0] * (target+1)

    OUTPUT: Minimum number of coins needed to make the target.
    '''

    # Default output to target
    global changes, changes_list,memoization_used, iterations
    iterations += 1
    min_coins = target
    old_changes_list = len(changes_list)
    # Base Case
    if target in coins:
        known_results[target] = 1
        changes.append(target)
        print ("{}".format(changes))
        changes_list.append(changes[:]) # must do real copy!
        changes.pop()
        return 1

    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        memoization_used += 1
        return known_results[target]

    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:

            # Recursive call, note how we include the known results!
            changes.append(i)
            num_coins = 1 + rec_coin_dynam(target-i,coins,known_results)
            changes.pop()
            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins

                # Reset the known result
                known_results[target] = min_coins
    if len(changes_list) == old_changes_list :
        print ("no changes found in this iteration for {}:{}".format(target, [c for c in coins if c <= target]))
    return min_coins


def make_change_top_bottom(coins, n):
    t = [[0 for x in range(n+1)] for y in range(len(coins)+1)]
    coins = sorted (coins)
    iterations = 0;
    for i in range(0, len(coins)+1):
        for j in range(n+1):
            iterations += 1
            if j == 0 and i == 0:
                t[i][j] = 1
            else:
                if i == 0:
                    t[i][j] = 0
                else:
                    if coins[i-1] > j:
                        t[i][j] = t[i-1][j]
                    else:
                        t[i][j] = t[i-1][j] + t[i][j-coins[i-1]]
    print("iteratinss={}".format(iterations))
    return t[len(coins)][n]



def make_change(coins, n):
    results = [0 for _ in range(n + 1)]
    results[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            results[i] += results[i - coin]
        print (results)
    return results[n]
iterations = 0
mem = {} # mem[(n,c)] = nb of ways to get n, using coins <=c
def make_change_top_bottom_1(coins, n):
    coins = sorted(coins, reverse=True)
    global iterations
    iterations = 0
    def dp(n,c): # = nb of ways to get n, using coins <=c
        global iterations
        if n<0: return 0
        if n==0: return 1

        #if (n,c) in mem: return mem[(n,c)]

        smaller_coins = list(filter(lambda coin: coin<c, coins))
        if len(smaller_coins)==0: return 1 if n%c==0 else 0
        next_coin = smaller_coins[0]

        ret = 0; remain = n
        while remain >= 0:
            iterations += 1
            ret += dp(remain, next_coin)
            remain -= c
        mem[(n,c)] = ret
        return ret
    result =  dp(n,coins[0])
    print ("iterations={}".format(iterations))
    return result
target = 25
#coins = [1,5,10,25,100]
coins = [1,5,10,25,100]
result = make_change(coins,target)
print ("make_change return {}".format(result))
known_results = [0]*(target+1)
result = make_change_top_bottom(coins, target)
print ("make_change_top_bottom return {}".format(result))
result = make_change_top_bottom_1(coins, target)
print ("make_change_top_bottom_1 return {}".format(result))



"""
number = test_rec_coin_dynam(target,coins,known_results)
print ("change/target: {}, type of coins: {}, time complexity({}x{}={}".format(target, len(coins), target, len(coins), target * len(coins)))
print ("Total changes found {}\nThe smallest number of chnages is {}".format(changes_list, number))
print ("found {} changes combinations".format(len(changes_list)))
print("iterations: {} memoization utilization: {}".format(iterations, memoization_used))

#list can use "==" to compare
if ["3:5", "4:7" ] == ["3:5", "4:71"]:
    print ("T")
else:
    print ("F")

lists = [
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
[5, 5, 5, 5, 5, 25],
[5, 5, 5, 5, 25, 5],
[5, 5, 5, 25, 5, 5],
[5, 5, 25, 5, 5, 5],
[5, 25, 5, 5, 5, 5],
[25, 5, 5, 5, 5, 5],
[25, 25]]

list_set = set()

dict = {}
for li in lists:
    for n in li:
        if n in dict:
            dict[n] +=1
        else:
            dict[n] =1
    string_list = []
    for k,v in dict.items():
        string_list.append(str(k)+":"+str(v))
    list_set.add(string_list) # set can not hash on dict, list

print("{}".format(dict))
"""