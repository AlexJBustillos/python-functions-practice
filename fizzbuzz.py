n = int(input("enter a number please: "))
def fizzbuzz(n):
    n = list(range(n + 1))
    for i in range(len(n)):
        if i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        else:
            print(i)
            
fizzbuzz(n)