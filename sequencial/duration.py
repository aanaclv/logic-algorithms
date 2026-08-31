'''
Write a program to read a duration in seconds and then display that duration on the screen in the
format hours:minutes:seconds.
'''

duration = int(input("Enter duration in seconds: "))
hours = duration/3600
rest = duration%3600
min = rest/60
sec = rest%60

print(f"{hours:.0f}:{min:.0f}:{sec:.0f}")