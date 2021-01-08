def tripler(array):
    result = []

    for i in range(len(array)):
        num = array[i]
        multiple = num * 3
        result.append(multiple)

    return result

print(tripler([1,5, 7, 8, 89]))

def odd_range(end):
    arr = []
    for i in range(1, end, 2):
        arr.append(i)
    return arr



print(odd_range(32))

def cat_builer(name, color, toys):
    return {
        "name": name,
        "color": color,
        "toys": toys
    }

print(cat_builer('pebs', 'blue', ['bone', 'stick']))

def value_pair(dict1, dict2, key):
    return [dict1[key], dict2[key]]
dict1 = {"name": "Kaida", "age": 1}
dict2 = {"name": "Pebs", "age": 5}

print(value_pair(dict1, dict2, "name"))
print(value_pair(dict1, dict2, "age"))

def  does_key_exist(dict, key):
    return key in dict

dict1 = {'anime': 'MHA', 'game': 'OW'}
print(does_key_exist(dict1, "anime"))
print(does_key_exist(dict1, "ga"))

def adult(people):
    names = []
    for i in range(len(people)):
        person = people[i]
        if person['age'] >= 18:
            names.append(person)

    return names

ppl = [
    {'name': 'El profesor', 'age': 40},
    {'name': 'Nairobi', 'age': 20},
    {'name': 'Tokyo', 'age': 15},
    {'name': 'Marseille', 'age': 35},
]

print(adult(ppl))

def is_prime(num):
    if (num < 2): return False
    if (num == 2): return True
    
    for i in range(2, int((num/2)+1)):
            if (num % i == 0):
                return False
    return True

def first_n_primes(n):
    primes = []
    num = 2
    while (len(primes) < n):
        if (is_prime(num)):
            primes.append(num)
        num += 1
    return primes

print(first_n_primes(1))
print(first_n_primes(2))
print(first_n_primes(3))

def sum_of_n_primes(n):
    sum = 0
    primes = first_n_primes(n)
    for i in range(len(primes)):
        sum += primes[i]
    return sum

print(sum_of_n_primes(1))
print(sum_of_n_primes(2))
print(sum_of_n_primes(3))

def count_scores(people):
    scoresObj = {}
    for i in range(len(people)):
        personObj = people[i]
        name = personObj["name"]
        score = personObj["score"]
        if (name in scoresObj): scoresObj[name] += score
        else: scoresObj[name] = score
    return scoresObj

peeps = [
  {"name": "Pete", "score": 2},
  {"name": "Dexter", "score": 2},
  {"name": "Mike", "score": 2},
  {"name": "Dexter", "score": 2},
  {"name": "Mike", "score": 2},
  {"name": "Pete", "score": 2},
  {"name": "Dexter", "score": 2}
]

print(count_scores(peeps))

ppl = [ {"name": "Pete", "score": 10},
            {"name": "Mike", "score" : 10},
            {"name": "Pete", "score": -8},
            {"name": "Dexter", "score": 12}]

print(count_scores(ppl))