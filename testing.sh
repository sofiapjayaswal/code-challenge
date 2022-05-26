# !/bin/bash
#
# testing.sh - test showtimes_generator.py
#
# input: none
# output: Error messages and schedules for movies
#
# usage: ./testing.sh (./testing.sh &> testing.out if you want to put output in a file rather than stdout)
# Note: remember to do chmod +x testing.sh, and output may vary depending on day you run (opening+closing times differ)
# Sofia Jayaswal, 05/25/2022

# TEST 1: Testing invalid number of arguments
echo "TEST 1: invalid number of arguments"
echo "showtimes_generator.py test1.txt wrong_argument"
python showtimes_generator.py test1.txt wrong_argument
echo

# TEST 2: Testing with test1.txt (Many movies with average runtimes)
echo "TEST 2: testing with test1.txt"
python showtimes_generator.py test1.txt
echo

# TEST 3: Testing with test2.txt (short films)
echo "TEST 3: testing with test2.txt"
python showtimes_generator.py test2.txt

# TEST 4: Testing with test3.txt (movies with long runtimes)
echo "TEST 4: testing with test3.txt"
python showtimes_generator.py test3.txt


