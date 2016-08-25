#Now we want to add variables to simplify makefile
#Use $(variable) to reference variable
OBJS = HW1.o
CPPFLAGS = -std=c++11 -Wall
PROG = HW1
CC = g++
FILE = HW1.cpp

$(PROG): $(OBJS)
	$(CC) -o $(PROG) $(OBJS)

#-c is complile only
eigen.o: $(FILE)
	$(CC) $(CPPFLAGS) -c $(FILE)

clean:
	$(RM) $(PROG) $(OBJS)
#RM is a built in variable
