def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Machine Learning Exercises")
        txt = open(fname)
        print(txt.read())
file_read('aa.txt')
