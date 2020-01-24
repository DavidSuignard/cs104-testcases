CXX = g++
CXXFLAGS = -g3 -O0 -Wall --std=c++11

all: play_reversi

play_reversi: reversi.cpp test-reversi.cpp 
	$(CXX) $(CXXFLAGS) reversi.cpp test-reversi.cpp -o test-reversi

test: test_game1

test_game1: play_reversi
	@echo "******************************************************************"
	@echo "                   Testing reversi Board Size 4"
	@echo "******************************************************************"
	@echo ""
	./test-reversi 4 < reversi4-game1.txt > reversi4-game1-out.tmp
	@diff -s  reversi4-game1.check reversi4-game1-out.tmp
	@echo ""
	@echo "******************************************************************"
	@echo "                   Testing reversi Board Size 8"
	@echo "******************************************************************"
	@echo ""
	./test-reversi 8 < reversi8-game1.txt > reversi8-game1-out.tmp
	@diff -s  reversi8-game1.check reversi8-game1-out.tmp

	./test-reversi 8 < reversi8-perfectgame.txt > reversi8-perfectgame-out.tmp
	@diff -s  reversi8-perfectgame.check reversi8-perfectgame-out.tmp

	@echo ""
	@echo "Passed all tests!"
	@echo ""
	@echo "Cleaning up temporary files!"
	rm -rf reversi*.tmp

clean: 
	rm -rf reversi*.tmp test-reversi

.PHONY: test test_game1 clean