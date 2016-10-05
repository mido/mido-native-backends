# test: test.c
# 	gcc -Wall -o test test.c

test.so: test.c
	gcc -Wall --shared -fPIC -o test.so test.c

clean:
	rm -f test test.so
