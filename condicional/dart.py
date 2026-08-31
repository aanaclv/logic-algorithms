'''
In the javelin throw, the athlete has three chances to throw the javelin as far as possible.
You must write a program that, given the distances of the three attempts, determines which
one was the farthest.
'''
distance1 = float(input("Distance 1: "))
distance2 = float(input("Distance 2: "))
distance3 = float(input("Distance 3: "))

if distance1 > distance2:
     if distance1 > distance3:
          print(distance1)
elif distance2 > distance3:
     print(distance2)

else:
     print(distance3)
    