import os

def csv_separate(line):
    array = []
    j = 0
    for i in range (len(line)):
        if ',' == line[i]:
            array.append(line[j:i])
            j = i + 1
    array.append(line[j:])
    return array


def csv_to_array(folder, file):
    path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)), 'data', folder, file)
    user_file = open(path, 'r')

    arr = []
    
    for line in user_file:
        inp_arr = csv_separate(line.replace('n', ''))
        arr.append(inp_arr)
    
    return arr