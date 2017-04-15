CC=gcc
CXX = g++
LEX = flex
YACC = bison
CFLAGS = -Wall -std=c99
CXXFLAGS = -Wall -std=c++11
NOWARN = -Wno-unused -Wno-sign-compare

LFLAGS = # -d
YFLAGS = -vtd

OBJS = main.o parse.tab.o lex.yy.o

run: $(OBJS)
	$(CXX) $(CXXFLAGS) -o run $(OBJS)

main.o: main.c parse.y scan.l parse.tab.c lex.yy.c
	$(CXX) $(CXXFLAGS) -c main.c

parse.tab.c: parse.y
	$(YACC) $(YFLAGS) parse.y

parse.tab.o: parse.tab.c
	$(CXX) $(CXXFLAGS) -c parse.tab.c

lex.yy.c: scan.l parse.tab.h
	$(LEX) $(LFLAGS) scan.l

lex.yy.o: lex.yy.c
	$(CXX) $(CXXFLAGS) $(NOWARN) -c lex.yy.c
	
clean:
	$(RM) pycomply-* *.o parse.tab.c lex.yy.c
	$(RM) parse.tab.h
	$(RM) parse.output
