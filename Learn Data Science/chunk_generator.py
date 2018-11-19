def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    while True :
        data = file_object.readline()

        if not data: 
            break

        yield data
        
counts_dict = {}

with open('world_ind_pop_data.csv') as file:

    for line in read_large_file(file):
        
        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else :
            counts_dict[first_col] = 1

print(counts_dict)