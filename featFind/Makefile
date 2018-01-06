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
	$(CC) $(CFLAGS) -o run $(OBJS)

main.o: main.c parse.y scan.l parse.tab.c lex.yy.c
	$(CC) $(CFLAGS) -c main.c

parse.tab.c: parse.y
	$(YACC) $(YFLAGS) parse.y

parse.tab.o: parse.tab.c
	$(CC) $(CFLAGS) -c parse.tab.c

lex.yy.c: scan.l parse.tab.o
	$(LEX) $(LFLAGS) scan.l

lex.yy.o: lex.yy.c
	$(CC) $(CCFLAGS) $(NOWARN) -c lex.yy.c
	
clean:
	$(RM) run run-* *.o parse.tab.c lex.yy.c
	$(RM) parse.tab.h
	$(RM) parse.output
