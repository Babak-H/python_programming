# Working with files

# writing and reading from text file:
fw = open('Files/sample.txt', 'w')
fw.write('writing some stuff on my text file\n')
fw.write('i like bacon and eggs')
fw.close()

fr = open('Files/sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

# how to read a text file into a python list
lines = fr.read().split(',')
#or
lines = fr.read().split('\n')

#=======================================
# with context manager
with open('test.txt', 'r') as f:
    pass

print(f.closed)

# How can I open multiple files using “with open” in Python?
with open('a.txt', 'w') as a, open('b.txt', 'w') as b:
    print(a.name, b.name)


with open("./Files/sample.txt", 'r') as f:
    #  this is most efficient way, because it doesnt read all lines of file at once
    for line in f:
        print(line, end='')

    # print(f.read())   # reads the whole text (if files are too big do not do this!!)

    # print(f.readline()) # reads each line of file
    # print(f.readline())

    # print(f.readlines())  # reads all lines at once and puts them inside a list


with open('./Files/sample.txt', 'r') as f:
    contents = f.read(100)
    print(contents)

    # this will read from characters 100 to 200
    size_to_read = 100
    contents = f.read(size_to_read)   

# =========================== 
# optimized way for large files:

with open('./Files/sample.txt', 'r') as f:
    size_to_read = 20
    contents = f.read(size_to_read)

    while len(contents) > 0:
        print(contents)
        contents = f.read(size_to_read)

        print(f.tell())   # shows current position of reading

# =========================== 
# if file doesnt exist, it will create it, but if it does, this method overwrites the file!!
# if file exists, use 'a' instead of 'w' to append to file

with open('./Files/sample.txt', 'w') as f:
    f.write("Test")
    f.write("Test")
    f.writelines("\nHello this is a test")


# working with two files, read from one and write in the other
with open('./Files/test.txt', 'r') as rf:
    with open('./Files/test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# working with non-text files, we use binary instead of string
with open('./Files/apple.jpg', 'rb') as rf:
    with open('./Files/apple_copy_1.jpg', 'wb') as wf:
        chunk_size= 4096
        rf_chunk = rf.read(chunk_size)
        
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


# ==========================
# CSV File
import csv

# read from file
with open("./Files/Salaries.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # skip the first line
    next(csv_reader)

    for line in csv_reader:
        print(line)
        print(line[2])


# read from file and save to new file
with open("./Files/Salaries.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    with open('./Files/Salaries_copy.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)


# DictReader considers first line as keys of dictionary and turns each line into a dictionary
with open("./Files/Salaries.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    idx = 0

    for line in csv_reader:
        print(line['EmployeeName'])
        print()
        idx += 1
        if idx > 2 : break


# to remove a column: 1- remove it from list of headers  2- remove it from dictionary when writing it
with open("./Files/Salaries.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    with open('./Files/Salaries_copy.csv', 'w') as new_file:
        fieldNames = ['Id','EmployeeName','JobTitle','BasePay','OvertimePay','OtherPay','Benefits','TotalPay','TotalPayBenefits','Year','Notes','Agency']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldNames, delimiter='\t')
        csv_writer.writeheader()
        
        for line in csv_reader:
            del line['Status']  # delete specific column and write the rest of the row
            csv_writer.writerow(line)


# parsing a tab-separated file in Python
with open("tab_separated_values") as tsv:
    for line in csv.reader(tsv, dialect='excel-tab'):
        #You can also use delimiter="\t" rather than giving a dialect.
        pass
