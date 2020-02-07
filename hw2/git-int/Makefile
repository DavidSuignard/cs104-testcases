CXX = g++
CXXFLAGS = -g3 -O0 -Wall --std=c++11

all: compile_gitint

compile_gitint: gitint.cpp gitint-shell.cpp 
	$(CXX) $(CXXFLAGS) gitint.cpp gitint-shell.cpp -o gitint-shell

test: test_game1

test_game1: compile_gitint
	@echo "******************************************************************"
	@echo "                   Testing using HW2 writeup example"
	@echo "******************************************************************"
	@echo ""
	./gitint-shell < testcase1.txt > testcase1-out.tmp
	@diff -s  testcase1-out.check testcase1-out.tmp
	@echo "Cleaning up temporary file!"
	rm -rf testcase1-out.tmp
run_shell: compile_gitint
	valgrind --tool=memcheck --leak-check=yes ./gitint-shell


clean: 
	rm -rf reversi*.tmp test-reversi

.PHONY: test test_game1 clean