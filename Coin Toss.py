import CoinClass as c  # importing file, dont import it as .py


# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'
# my coin is a instance of the object coin
    # Display the side of the coin that is facing up.
    # notice you do not have to supply the argument/parameter
    print('This side is up:', my_coin.get_sideup())
# calling the get side up method from instance - shows what is head and what is tails
    # Toss the coin.
    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()

        # Display the side of the coin that is facing up.
        print('This side is up:', my_coin.get_sideup())


# Call the main function.
main()
