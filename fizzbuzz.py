num=100
for i in range(1,num):
	if(i%3==0 and i%5==0):
		i="FizzBuzz"
		print(i)
	elif(i%3==0):
		i="Fizz"
		print(i)
	elif(i%5==0):
		i="Buzz"
		print(i)
	else:
		print(i)

for num in range(1,num):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print("primes are:",num)
			
