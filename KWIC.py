сharacters = ""
index = list()
alphabetized_index = list()

id_start_line = list() # list of start postions of lines
id_end_line = list()   # list of end position of lines


def input_strings():
    global characters, id_start_line, id_end_line

    with open("input.txt") as file:
        characters = file.read()
    
    # add to the list starting index of the first line
    id_start_line.append(0)

    # add to the line_index starting indexes of all the lines
    for i in range(len(characters)):
        if(characters[i] == '\n'):
            id_start_line.append(i+1)

    # create a list of end indexes of each line
    id_end_line = id_start_line[1:]
    id_end_line.append(len(characters))


def circular_shift():
    global index

    line_id = 0

    # add location of the first word in the first line
    index.append((0, 0))

    # create index - list of tuples (line_id, char_id)    
    for char_id in range(len(characters)):
        if(characters[char_id] == ' '):  # word is found
            index.append((line_id, char_id + 1))
        if(characters[char_id] == '\n'): # new line is found
            line_id += 1
            index.append((line_id, char_id + 1))


# create shifited phrases from index:
# shift = static_part + shift_part 
# shift_part | static_part 
# | mom and dad --> mom and dad (all the line - static_part)
# mom | and dad --> and dad mom 
# mom and | dad --> dad mom and 

def create_shift_from_index(_index, _id):
    static_part_start = _index[_id][1]
    static_part_end = id_end_line[_index[_id][0]]

    shift_part_start = id_start_line[_index[_id][0]]
    shift_part_end = _index[_id][1]

    static_part = characters[static_part_start : static_part_end]
    shift_part = characters[shift_part_start : shift_part_end]
    
    if(_index[_id][0] == len(id_end_line) - 1):
        static_part += ' '
    
    shift = static_part + shift_part

    return shift
    

def alphabetizing():
    global characters, alphabetized_index, id_end_line

    # replace '\n' in lines to create one-line shifted phrase
    characters = characters.replace('\n', ' ')

    # create dict({index : shift}) for further sorting indexes by values
    alph_dict = dict()
    for i in range(len(index)):
        alph_dict[index[i]] = create_shift_from_index(index, i)

    # sort dict by values(shifted phrases) in the alphabetical order
    sorted_shifts = dict(sorted(alph_dict.items(), key=lambda item: item[1]))
    
    # consists of a list of sorted indexes
    alphabetized_index = list(sorted_shifts.keys()) 
    

def output():
    for i in range(len(alphabetized_index)):
        shift = create_shift_from_index(alphabetized_index, i)
        print(shift)
    

def main():
    input_strings()
    circular_shift()
    alphabetizing()
    output()


if __name__ == "__main__":
    main()

