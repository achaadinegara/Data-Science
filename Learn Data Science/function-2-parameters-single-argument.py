def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    excalmation marks at the end of string"""

    echo_word = word1 * echo

    shout_word = echo_word + '!!!'

    return shout_word

no_echo = shout_echo('hello beib')

with_echo = shout_echo('hellobeibih ', 5)

print(no_echo)
print(with_echo)