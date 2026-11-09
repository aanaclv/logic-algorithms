'''
Read an integer N, then display the multiplication table for N from 1 to 10 on the screen.
'''

n = int(input("For what number do you want the multiplication table? "))
for i in range(1,11):
    print (f"{n} x {i} = {n*i}")
    


