


def read_file(file_name):

    file = open(file_name, "r")
    
    content = file.read()
    file.close()
    
    
    print(content)
    
    prefix = "F="
    line_new = content.removeprefix(prefix)
    print("Before: ", content, content.count(prefix))
    print("After:    ", line_new, line_new.count(prefix))

    nb_ant = line_new[0]
    print("Number of ants:", nb_ant)
read_file('fourmiliere_un.txt')






    
