from addflipper import flipaddition

@flipaddition
def addtester( x ):
    for i in range( 10 ):
        print x + i, x - i
    return x + 1

if __name__ == "__main__":
    print addtester( 2 )
