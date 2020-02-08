CXX = g++
CXXFLAGS = -g3 -O0 -Wall --std=c++11

all: compile_gitint

compile_gitint: gitint.cpp gitint-shell.cpp 
	$(CXX) $(CXXFLAGS) gitint.cpp gitint-shell.cpp -o gitint-shell

test: test_case1 basic_tags stress_test_tags

test_case1: compile_gitint
	@echo "******************************************************************"
	@echo "                   Testing using HW2 writeup example"
	@echo "******************************************************************"
	@echo ""
	./gitint-shell < testcase1.txt > testcase1-out.tmp
	@diff -s  testcase1.check testcase1-out.tmp
	@echo "Cleaning up temporary file!"
	rm -rf testcase1-out.tmp
	@echo "Passed!"
	@echo ""

basic_tags: compile_gitint
	@echo "******************************************************************"
	@echo "                 Testing basic tag functionality"
	@echo "******************************************************************"
	@echo ""
	./gitint-shell < tag-basic.txt > tag-basic-out.tmp
	@diff -s  tag-basic.check tag-basic-out.tmp
	@echo "Cleaning up temporary file!"
	rm -rf tag-basic-out.tmp
	@echo "Passed!"
	@echo ""

stress_test_tags: compile_gitint
	@echo "******************************************************************"
	@echo "                   Stress testing tags"
	@echo "        If you get an error, check out this post on piazza:"
	@echo "           https://piazza.com/class/k4psr3w9692vr?cid=551"
	@echo "******************************************************************"
	@echo ""
	./gitint-shell < tag-stresstest.txt > tag-stresstest-out.tmp
	@diff -s  tag-stresstest.check tag-stresstest-out.tmp
	@echo "Cleaning up temporary file!"
	rm -rf tag-stresstest-out.tmp
	@echo "Passed!"
	@echo ""

#written by CP Jamie
run_shell: compile_gitint
	valgrind --tool=memcheck --leak-check=yes ./gitint-shell


clean: 
	rm -rf reversi*.tmp test-reversi

.PHONY: test test_game1 clean