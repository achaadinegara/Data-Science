# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry',
              'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [member if len(member) >=7 else member.replace(member, ' ') for member in fellowship]

print(new_fellowship)