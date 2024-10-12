#Program to check if th nth bit is set or not
def setornot(number,n):
    #make a variable by left shifting 1(k-1)times and check if(n AND mask)=1 or 0
    if number &(1<<(n-1)):
        print('\nSET')
    else:
        print('\nNotSet')
number=int(input('Enter number'))
n=int(input('Enter the bit number'))
setornot(number,n)