#X Green Bottles

def bottles(n):
    if n == 1:
        b = 'bottle'
    else:
        b = 'bottles'
    return b

def were_was(n):
    if n == 1:
        w = 'was'
    else:
        w = 'were'
    return w

def line(n):
    
    lyric = '''There %s %d green %s, hanging on the wall...
%d green %s, hanging on the wall...
and if one green bottle, should accidentally fall...
there'll be %d green %s, hanging on the wall!

''' % (were_was(n),
        n, bottles(n),
        n, bottles(n),
        n-1, bottles(n-1))
    return lyric              

#Here's where the magic happens
def play(n):
    while not n:
        try:
            n = int(input('How many bottles are on the wall? > '))
        except ValueError:
            print('You have to type a number!')
            
    for i in range(n):
        print(line(n - i))



