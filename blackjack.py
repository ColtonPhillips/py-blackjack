PREAMBLE = """
Welcome to...

Colton Phillips' Blackjack!

The coolest console game in the Universe.

Here are the rules:

1) You play it.
2) You enjoy it. 
3) You decide whether or not you would like to continue playing.

Any questions? Of course not. Have fun playing Blackjack, kiddo!

"""

EPILOGUE = """
Well, we've all had some fun. You laughed, you cried. Remember 
when the blackjack dealer tried to trick you into buying him a
drink? That was pretty funny. 

I hope you enjoyed this experience. I'm sure you've learned a lot from it.

Cheers,
C

"""

TABLE_INTRO = """
You find yourself at a blackjack table. The dealer yells at you:

"Hey! You look like a rube! Prove your worth, you plebian."

"Huh", you think. But it's too late. Thousands of ghost tendrils
are pulling you in closer to the table. You are certainly going to
play a game of Blackjack. 

Like it not, that's what's in store for you today.

"""

def game_loop():
    print TABLE_INTRO

    active_game = True
    while active_game: 
        print """
        TODO: MAKE A GAME 
        HAR HAR
        HAR 
        
        """
        active_game = False

def main():
    print PREAMBLE
    raw_input("Press Enter Key to play.")
    game_loop()
    print EPILOGUE

if __name__ == "__main__":
    main()