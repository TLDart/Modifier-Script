from os import listdir, path
from os.path import isfile, join
from tkinter import *
or_dir = path.dirname(__file__)
file_dir = str(or_dir)
onlyfiles = [f for f in listdir(file_dir) if isfile(join(file_dir, f))]

#Time Engine
import datetime
import time
ts = time.time()
time_stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d %H_%M_%S')

import argparse
import sys
try:
    from tkinter import *
except:
    try:
        from Tkinter import *
    except:
        # If no versions of tkinter exist (most likely linux) provide a message
        if sys.version_info.major < 3:
            print ("Error: Tkinter not found")
            print ('For linux, you can install Tkinter by executing: "sudo apt-get install python-tk"')
            sys.exit(1)
        else:
            print ("Error: tkinter not found")
            print('For linux, you can install tkinter by executing: "sudo apt-get install python3-tk"')
            sys.exit(1)
#Dictionary Engine
def Dictionary():
    ab_dict = {}
    value = dictionary.get()
    try:
        with open(onlyfiles[value]) as f:
            for line in f:
               (key, val) = line.split()
               ab_dict[key] = val
        return ab_dict
    except FileNotFoundError:
        print('Please provide a dictionary and reload a Script')


#Make a list of all the words
def file_modifier(read_file, write_file):
    ab_dict = Dictionary()
    words = read_file.read()
    word_list = words.split()
    #Replace all the abbreviations with their respetive word
    new_list = []
    for word in word_list:
        for key in ab_dict:
            if word == key:
                new_list.append(ab_dict[key])
        new_list.append(word)
    for word in new_list:
        for key in ab_dict:
            if key == word:
                new_list.remove(word)
    print(new_list)
    final_string = ' '.join(new_list)
    write_file.write(final_string)


def RadialCommand():
    value = v.get()
    onlyfiles = [f for f in listdir(file_dir) if isfile(join(file_dir, f))]

    if value == int('-1'):
        onlyfiles = [f for f in listdir(file_dir) if isfile(join(file_dir, f))]
        value = filevar.get()
        for file in onlyfiles:
            if file[-3:] == 'txt':
                final_filename = file[:-4] + ' ' + time_stamp +'.txt'
                abb_file = open(file, 'r')
                final_file = open(final_filename, 'w')
                file_modifier(abb_file, final_file)
                #output.insert(END, final_filename + '\n')

    else:
                final_filename = onlyfiles[value][:-4] + ' ' + time_stamp +'.txt'
                abb_file = open(onlyfiles[value], 'r')
                final_file = open(final_filename, 'w')
                file_modifier(abb_file, final_file)
                Label(window, text=final_filename, fg='black', font= 'Candara 12 bold', background='grey') .pack(anchor=W)
                #output.insert(END, final_filename + '\n')

        #output.insert(END, 'All done')
# Main Script
#Handling user input
window = Tk()
v = IntVar()
dictionary = IntVar()
window.title('Modifier Script')
#Create a bigger window if it was
window.geometry("270x500") #You want the size of the app to be 500x500
window.resizable(0, 0) #Don't allow resizing in the x or y direction

Label(window, text='Welcome to the File Modifier', fg='black', font= 'Candara 12 bold') .pack(anchor=N)
Label(window, text=' Plase select your dictionary', fg='black', font= 'Candara 12 bold') .pack(anchor=N)

for file in onlyfiles:
    if file[-3:] == 'txt':
        Radiobutton(window,
                      text=file,
                      font= 'Candara 12',
                      padx = 20,
                      variable=dictionary,
                      value=onlyfiles.index(file)).pack(anchor=N)

Label(window, text='Multi File Options',font= 'Candara 12 bold', fg='black') .pack(anchor=N)
#Entry Box
Radiobutton(window,
              text="All files",
              padx = 20,
              font= 'Candara 12',
              variable=v,
              value=-1).pack(anchor=N)

Label(window, text='Single File Options', fg='black', font= 'Candara 12 bold') .pack(anchor=N)
#Button
for file in onlyfiles:
    if file[-3:] == 'txt':
        Radiobutton(window,
                      text=file,
                      padx = 20,
                      font= 'Candara 12',
                      variable=v,
                      value=onlyfiles.index(file)).pack(anchor=N)

Button(window, text='MODIFY', font= 'Candara 12', width=6, command = RadialCommand) .pack(anchor=N)
Label(window, text='File output', fg='black', font= 'Candara 12 bold') .pack(anchor=W)
#output = Text(window, width=50, height= 6, wrap=WORD, background='grey',  font='Candara 12')
#output.pack(anchor=W)


window.mainloop()
