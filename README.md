# DirMake
An API to create directories in python, automatically numbering duplicate directories.

DirMake is a simple tool I created to help with managing names of folders when dynamically creating directories. Where normally you would need to check whether a directory exists first, this short script instead finds the next available unique name in the pattern of DIRNAME(x). It returns the name of the directory it created so you can use the dynamically created directory in your programm successfully.

This tool helps simplify managing directories when saving the outputs of a program to a new directory each time the program is exectued.

Usage:

Assuming the folder test exists in the current directory:

dirname = "test" <br/>
print(dirname) <br/>
  "test" <br/>
dirname = dirmake(test) <br/>
print(dirname) <br/>
  "test1" <br/>

In the example above, dirmake(dirname) found that a folder called test already exists, therefore it add a number 1 to the end of the name (test -> test1) and created a new directory, returning the name of the newly created directory.
