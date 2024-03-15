import timeit

def find_coins_greedy(nominals, sum):
    result = {}
    nominals.sort(reverse = True)
    for nominal in nominals:
        if nominal <= sum:
            result.update({nominal : sum // nominal})
            sum -= nominal * (sum // nominal)

    return result

nominals = [25, 10, 5, 2]
sum = 1113

print(find_coins_greedy(nominals, sum))

execution_time = timeit.timeit(lambda: find_coins_greedy(nominals, sum), number = 1)

print("Execution time:", execution_time, 'seconds') 