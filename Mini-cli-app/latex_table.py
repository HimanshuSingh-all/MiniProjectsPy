from argparse import ArgumentParser, Namespace

def read_txtfile(fname:str, outfile:str, **kwargs):

    if kwargs is None or 'delim' not in kwargs:
        delim = None
    # For Future Reference:
    # https://stackoverflow.com/questions/225337/how-to-split-a-string-with-any-whitespace-chars-as-delimiters
    with open(outfile,'w+') as outhand:
        
        with open(fname) as fhand:
            elems = None

            for line in fhand:
                if delim is None:
                    line_elems = line.split() 
                else:
                    line_elems = line.split(delim)

                if elems in None:
                    elems = len(line_elems) 

                if len(line_elems)< elems:
                    line_elems += [' '] * ( elems - len(line_elems)) 
                
                
                outstr = '&'.join(line_elems)
                outfile.write(outstr)
                outfile.write('\\ \n')



init_arguments = ArgumentParser()
init_arguments.usage = " Reads a file(.txt) and gives it in a tex latex format. \n\
                        If the table in the file is uneven, the numer of elements rows is determined by the first row"


init_arguments.add_argument("File_Name", help = "Enter the name of the file that you want to create a table with ", type = str)

#init_arguments.add_argument()

