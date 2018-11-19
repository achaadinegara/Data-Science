def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string"""

    echo_word = ""
    shout_word = ""

    try : 
        echo_word = word1 * echo
        
        shout_word = echo_word + '!!!'
    except:
        print("word1 must be a string and echo must be an integer")

    return shout_word

shout_echo("love ya", echo = "baby you got me")