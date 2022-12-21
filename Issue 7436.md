# Issue 7436: frobby optional spkg doesn't build on a lot of machines

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-12 04:35:18

Assignee: tbd

On many Linux boxes, building the frobby-0.7.6 spkg fails as follows:


```
gcc version 4.4.1 (Ubuntu 4.4.1-4ubuntu8) 
****************************************************
mkdir -p bin/release/ 
g++ -Wall -ansi -pedantic -Wextra -Wno-uninitialized -Wno-unused-parameter -Werror -isystem /tmp/wstein/farm/sage-4.2.1.alpha0/loc
al/include -O3 -c src/main.cpp -o bin/release/main.o
src/main.cpp: In function ‘int main(int, const char**)’:
src/main.cpp:30: error: ‘srand’ was not declared in this scope
make: *** [bin/release/main.o] Error 1
Error building Frobby.

real    0m2.271s
user    0m0.320s
sys     0m0.410s
sage: An error occurred while installing frobby-0.7.6
```


I ran the command "sage -i frobby-0.7.6" on the build farm and it fails on:

  * debian32/64
  * fedora32/64
  * mandriva32/64
  * opensuse32/64
  * ubuntu32/64

It works on centos (=REDHAT).    It works on sage.math.   Basically it works with gcc <= 4.2 and fails with newer GCC's. 


---

Comment by drkirkby created at 2009-11-12 04:54:44

I get the same problem on Solaris, with gcc 4.4.2

dave


---

Comment by drkirkby created at 2009-11-12 21:57:35

Also fail on Solaris 10 (SPARC) with gcc 4.4.2


---

Comment by drkirkby created at 2009-11-12 21:58:13

Oops, I appear to have put the same comment twice!


---

Comment by benjaminfjones created at 2012-05-26 01:10:48

Changing status from new to needs_review.


---

Comment by benjaminfjones created at 2012-05-26 01:10:55

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-05-26 01:13:29

Resolution: duplicate


---

Comment by drkirkby created at 2012-05-26 21:20:59

As a matter of interest, what was the reason for not fixing it? I thought optional packages were supposed to build on all supported machines. So the only logical things to me were to either 

1) Fix it 
2) Make it experimental and not optional. 

It this bug report a duplicate, as the resolution is set to? 

I appreciate the fact this has remained like this for 3 years probably means nobody cares too much, but the concept of closing a ticket without fixing an issue seems wrong to me. 

Dave


---

Comment by benjaminfjones created at 2012-05-27 00:02:09

This was closed because #13007 does fix the problem on the platforms in the ticket description. I did not test the new spkg there on solaris though.
