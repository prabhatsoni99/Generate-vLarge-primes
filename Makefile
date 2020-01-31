all: generate1Prime.cpp
	g++ -g -Wall -o generate1Prime generate1Prime.cpp

clean:
	$(RM) generate1Prime
