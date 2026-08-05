def is_leap(n):
    n=int(input())
    if n%4==0 or n%400==0 and n%100!=0:
       return true
    else:
        return false