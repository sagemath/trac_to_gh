# Issue 9766: Cliquer has no spkg-check file, but there is a small test suite with the program

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-19 15:05:00

Assignee: drkirkby

CC:  ncohen leif

There's a test suite which can be run easily - see below. 


```
drkirkby`@`hawk:~/cliquer-1.2.p6/src$ make testcases
gcc -Wall -O3 -fomit-frame-pointer -funroll-loops   -c -o testcases.o testcases.c
gcc  -o testcases testcases.o cliquer.o graph.o reorder.o
drkirkby`@`hawk:~/cliquer-1.2.p6/src$ ./testcases

Running testcases:  ELEMENTSIZE=32, sizeof(setelement)=4  (OK)

Testing small: graph_test...OK
Testing large: graph_test...OK
Testing wlarge: graph_test...OK

Testing small: single maximum clique...OK
Testing large: single maximum clique...OK
Testing small: single 3-sized clique...OK
Testing large: single 8-sized clique...OK

Testing small: all maximum cliques...OK
Testing large: all maximum cliques...OK
Testing small: all min 3-sized cliques...OK
Testing large: all min 8-sized cliques...OK
Testing large: all exactly 8-sized cliques...OK

Testing large: max clique size...OK
Testing weighted large: max clique weight...OK

Testing large: user_function w/ abort for 8-sized cliques...OK
Testing large: too small array for all maximum cliques...OK

Testing weighted large: single max weighted clique...OK (w=66)
Testing weighted large: single min 60 weighted clique...OK (w=63)
Testing weighted large: single exactly 62 weighted clique...OK (w=62)
Testing weighted large: all max weighted cliques...OK
Testing weighted large: all min 60 weighted cliques...OK
Testing weighted large: all 60...64 weighted maximal cliques...OK

Testing re-entrance...OK
drkirkby`@`hawk:~/cliquer-1.2.p6/src$ 
```



---

Comment by leif created at 2010-09-04 04:29:13

Dave, be warned: You'll hate me if I should review this (`spkg-install`, `patches/Makefile`).


---

Comment by leif created at 2010-09-04 05:23:55

Also note that the upstream directory (`src/`) is *not vanilla*.


---

Comment by drkirkby created at 2010-09-04 07:51:18

I realise this is a duplicate of #9521


---

Comment by drkirkby created at 2010-09-04 07:51:18

Resolution: duplicate
