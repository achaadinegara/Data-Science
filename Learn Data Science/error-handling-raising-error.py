def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string"""

    if echo < 0:
        raise ValueError('echo must be greater than 0')
    
    echo_word = word1 * echo

    shout_word = echo_word + '!!!'

    return shout_word

print(shout_echo("paticle", 6))
