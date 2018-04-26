
# Default Python version:
PYVER=2.7

CC=gcc
LEX = flex
YACC = bison
CFLAGS = -Wall -std=c99
NOWARN = -Wno-unused -Wno-sign-compare

LFLAGS = --outfile=lex.yy.c  
YFLAGS = -vtd 

OBJS = main.o parse.tab.o lex.yy.o

front-end: clean run-${PYVER}

run-${PYVER}: $(OBJS)
	$(CC) $(CCFLAGS) -o run-${PYVER} $(OBJS)

main.o: main.c parsers/${PYVER}.y scanners/${PYVER}.l parse.tab.c lex.yy.c
	$(CC) $(CCFLAGS) -c main.c


parse.tab.c: makeparser
parse.tab.h: makeparser

makeparser: parsers/${PYVER}.y
	$(YACC) $(YFLAGS) --file-prefix=parse parsers/${PYVER}.y

parse.tab.o: parse.tab.c
	$(CC) $(CCFLAGS) -c parse.tab.c

lex.yy.c: scanners/${PYVER}.l parse.tab.h
	$(LEX) $(LFLAGS) scanners/${PYVER}.l

lex.yy.o: lex.yy.c
	$(CC) $(CCFLAGS) $(NOWARN) -c lex.yy.c

clean:
	$(RM) lex.yy.c
	$(RM) parse.tab.c parse.tab.h parse.output
	$(RM) *.o *.log

dist: clean
	$(RM) run-* 
