import sys
def read_file(path):
    data = []
    try:
        with open(path) as file:
            data = file.read().strip().split('\n')
            return data
    except:
        return data
def validate_structure(data):
    try:
        if int(data[0]) != len(data[1:]):            
            return False,"Number of missing words"
    except Exception as err:
        return False, "First line is not a number or " +err
    return True,""

def count_words_dis(data):
    return len(list(set(data[1:])))

def count_words(data):
    def second_pos(d):        
        return d[1]
    result = []
    for w in list(set(data)):
        result.append((w,data.count(w)))
    if result:
        result.sort(key=second_pos, reverse=True)
    return result
def write_data(path_out,data):
    try:
        with open(path_out,'w') as file:
            file.write(data[0])     
            file.write('\n')                 
            file.writelines(data[1:])
    except Exception as err:
        return False,err
    return True,""

if __name__ == "__main__":
    print("Point A")
    path = "./primerliteral.txt"
    data = read_file(path)
    if not data:
        print("No data on file or no found file")
        sys.exit()
    validate,msg = validate_structure(data)
    if not validate:
        print(msg)
        sys.exit()
    data.pop(0)
    words_dis = count_words_dis(data)
    print("Distinctive Words")
    print(words_dis)
    print("Count Words")
    count_words = count_words(data)
    print(count_words)
    print("Save information...")
    path_out="./primerliteral_out.txt"
    data_out = [str(words_dis)]
    data_out += [str(i[1]) for i in count_words]
    write,err = write_data(path_out,data_out)
    if not write:
        print("No save information in file",err)
        sys.exit()
    print("Information save successfully")
    sys.exit()