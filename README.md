# cspp-1-project
Plagiarism detector project for CSPP-1.

22-August-2017.

By Srikanth Kavuri, 20176001.

This project uses the following methods to, when given two documents, try and determine whether there could have been plagiarism between the two:
1. Bag of Words (Document distance)
2. Longest Common Subsequence

This document is intended to serve as a user guide.


PROGRAM STRUCTURE:
The program is divided into the following files:
1. files.py - Handles file operations required for the project.
2. ui.py - Serves as the User Interface for the project. This file contains the main program.
3. common.py - Contains the programs (only one, as of 22-08-17) that are used by all modules of the project.
4. bag_of_words.py - Contains the implementation of the Bag of Words algorithm.
5. lsc.py - Contains the implementation of the Longest Common Subsequence algorithm.



STARTING THE PROGRAM:
The execution of the program starts in 'ui.py'. You need to run this file. This will fire off the main program and start the execution.
The program expects you to enter the directory location where your files are present.

!!! NOTE: THE PROGRAM ONLY SEARCHES THE DIRECTORY THAT YOU PROVIDE. SUBDIRECTORIES ARE NOT SEARCHED.
!!! NOTE: THE PROGRAM ONLY CONSIDERS .TXT FILES. ALL OTHER FORMATS ARE IGNORED.
!!! NOTE: EMPTY FILES ARE IGNORED.

Once you start the main program, the program considers the present working directory as default. You are first asked if your files are present there with the following text:
"Default directory is <PWD>. Continue? "
If you press 'y' (case insensitive), the program will proceed to look for text files in the present directory.
If you enter 'n' (case insensitive), the program will prompt you to enter the directory where your files are present.
For any other input, the program will ask you again.



BAG OF WORDS EXPLANATION:
This algorithm proceeds as follows:
1. Read the files. All of the words in the file are arranged into a single line.
2. Construct a Counter dictionary (also called a vector in this context) from the lines in the files.
3. Calculate the document distance for every two files.
4. Construct a 2-dimensional array based on the document distances.
This 2-D array is returned to ui.py.

The document distance is the equivalent of taking the dot product of the two vectors and dividing the result by the lengths of both vectors.

Doc dis = (D1 . D2)/(|D1| * |D2|)

This value is essentially a cosine of an angle. So its value is between 0 and 1. This value is multiplied by 100 and stored into the 2-D array.
!!! NOTE: SINCE IT DOESN'T REALLY MAKE SENSE TO COMPARE A FILE WITH ITSELF, THE ANGLE BETWEEN A FILE AND ITSELF IS TAKEN AS -1. SO, THE DIAGONAL           OF THE 2-D ARRAY WILL BE -1.

Before the Bag of Words module completes, a list of file numbers along with corresponding file names is printed for your reference. If the printout is the following, for instance,

"
For your reference:
File number 0 corresponds to file abc.txt
File number 1 corresponds to file text.txt
"

then, in the matrix (arr), arr[0][1] would be the bag of words result of comparing File 0 (abc.txt) with File 1 (text.txt).

If the percentage distance between two documents is greater than or equal to 70 (design choice), then a printout is given saying that the two files are similar enough to each other (to suspect plagiarism).



LONGEST COMMON SUBSEQUENCE:
This algorithm proceeds as follows:
1. Read the files.
2. For each pair of strings, find the longest common substring.
3. The percentage match is calculated as
%match = (length of LCS) * 2 * 100 / (length of string one + length of string two)

Just like for Bag of Words, a 2-D matrix is returned.
Also, the percentages that are above 70 are displayed as similar enough to warrant plagiarism.


LOG FILE:
Every time you run the program, you are asked whether or not logging should be enabled for this program. If you choose to enable logging, a log file is created in the location that you picked at the start of the program.
Everything that is printed is also written to this file.