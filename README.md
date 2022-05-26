# Movie Theater Show Time Scheduler
### Sofia Jayaswal, 5/25/2022

### General Description
*showtimes_generator.py* is a program that a theater can run to get a schedule of show times for the day given a text 
file containing movies showing and their information (runtime, etc.).

### Implementation
For my implementation, I chose to create an easy-to-read and user-friendly file called *showtimes_generator.py*, a file containing helper 
functions called *showtimes_funcs.py*, and a Movie class called *movie.py*. The *showtimes_generator.py* file is the one that 
the user calls, and it calls functions and contains all the key variables used to produce show times, including opening and closing times, 
setup and cleanup times, and more. The *showtimes_funcs.py* function contains the main functions that help to produce and 
print the schedule. Lastly, *movie.py* is a class that creates objects representing a movie and its key information 
(name, release year, MPAA rating, runtime, showtimes).

### Design Choices
I attempted to make *showtimes_generator.py* as user-friendly as possible so the manager of the theater can 
update the opening and closing times and other 'subject to change' information regarding the theater. To make 
it more user-friendly, I put all complex functions within *showtimes_funcs.py*, making the main program that the user is 
running less cluttered. I also decided to create a Movie class because I had to keep track of multiple pieces of information
about a singular movie and creating an object for each movie seemed to be the most straightforward way to do this. 

### Usage
To use the generator, the user needs to call `python showtimes_generator.py moviesfile` on the command line. This movie
text file should contain movies showing, each movie on a new line. Each line should contain the movie's name, release year, 
MPAA rating, and runtime. These components should be separated by a comma. Further, there needs to be a header on the first
line of the text files. For example, "Movie Title, Release Year, MPAA Rating, Run Time".

Example of usage:
```bash
python showtimes_generator.py moviesfile.txt
```
If you would like to redirect output to a file:
```bash
python showtimes_generator.py moviesfile.txt &> output_file
```

### Assumptions
The program assumes that the text files passed in on the command line have a header on the first line. Further, it also 
assumes that runtimes are given in either 'hours:minutes' format or simply just 'minutes' if the movie is not an hour 
or more. Further, *showtime_generator.py* relies on *showtimes_funcs.py* and *movie.py*, so these files must either be 
in same directory or import statements in *showtime_generator.py* should be updated to reflect the directories in which the 
other two files are in.

### Testing
*testing.sh* provides some test cases testing *showtimes_generator.py*. The program is tested using invalid number 
of arguments passed on the command line, several movies, short movies, and long movies. These movies are in *test1.txt*, 
*test2.txt*, and *test3.txt*. *testing.out* is the output of *testing.sh*.

To test and have output in stdout, call line below on command line:
```bash
./testing.sh 
```
If you want output in another file, do:
```bash
./testing.sh &> testing.out
```
Note: if *testing.sh* is not running, ensure that you have given executable permission to the file through calling line
below on command line:
```bash
chmod +x testing.sh
```