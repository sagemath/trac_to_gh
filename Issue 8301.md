# Issue 8301: segfault in m4ri

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-02-19 02:21:08

Assignee: was

CC:  malb boothby

Type in

```
sage: b = random_matrix(GF(2),4,200); b[3] = b[0]; b.rank()
```

and get an absolutely stupendous segfault!

For the first time ever I finally get to use GF(2) matrix algebra for some actually interesting number theory research.  So I wrote a program that creates some fairly simple GF(2) matrices (using modular symbols), and tried the first somewhat nontrivial thing (computing the rank of a 4xn matrix) and got segfaults.  This is on 64-bit Ubuntu Linux.  Yikes.   So:

  1. These need to get fixed, obviously.

  2. Is there an easy way to completely turn off m4ri?  Seeing how easily it fell over, I don't trust it, and though it is fast I definitely want to rerun all my calculations m4ri free once I have everything setup.  These are calculations for a published paper that will play a key role in a "proof by computer" of a potentially important result in number theory.  

Regarding 2, here is a way that I seem to be able to get a matrix mod n dense, and I can then compute the rank, which in this case uses linbox, and is probably fast enough for my application:

```
sage: c = sage.matrix.matrix_modn_dense.Matrix_modn_dense(b.parent(),b.list(),False,True)
sage: c.rank()
3
sage: timeit('c.rank()')
625 loops, best of 3: 534 ns per loop
sage: timeit('c._clear_cache(); c.rank()')
625 loops, best of 3: 161 µs per loop
```




---

Comment by malb created at 2010-02-19 11:49:49

I will take a look ASAP.


---

Comment by malb created at 2010-02-19 15:22:23

Changing status from new to needs_work.


---

Comment by malb created at 2010-02-19 15:22:23

I can confirm the bug. A fix is available:

  http://bitbucket.org/malb/m4ri/changeset/dfdd4bce3eac/

I will make a new SPKG tomorrow-ish.


---

Comment by malb created at 2010-02-21 13:15:05

A new SPKG is available at:

   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100221.spkg

FWIW, I just ran

```python
sage: for i in range(10^4):
    b = random_matrix(GF(2),4,200); b[3] = b[0]
    c = sage.matrix.matrix_modn_dense.Matrix_modn_dense(b.parent(),b.list(),False,True)
    assert(b.rank() == c.rank())
....:
```

without errors.


---

Comment by malb created at 2010-02-21 13:15:05

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-02-21 13:16:07

Time comparisons:


```python
sage: timeit('c._clear_cache(); c.rank()')
625 loops, best of 3: 181 µs per loop

sage: timeit('b._clear_cache(); b.rank()')
625 loops, best of 3: 8 µs per loop
```



---

Comment by was created at 2010-02-23 18:41:45

Tom Boothby will referee this...


---

Comment by malb created at 2010-03-20 12:54:25

Tom, do think you can referee this for the next release? I've linked to the *only* changeset above for this new SPKG everything else is identical to the current one. So it should be an easy review


---

Comment by boothby created at 2010-03-21 15:16:41

Changing status from needs_review to positive_review.


---

Comment by boothby created at 2010-03-21 15:16:41

Sorry this took so long.  Works for me.


---

Comment by jhpalmieri created at 2010-04-20 20:26:24

I can't build this on one of the skynet machines:

```
iras     ia64-Linux-suse

$ uname -a
Linux iras 2.6.16.46-0.12-default #1 SMP Thu May 17 14:00:09 UTC 2007 ia64 ia64 ia64 GNU/Linux
```

I get this:

```
make[2]: Entering directory `/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/li\
bm4ri-20100221/src'
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/sh /home/palmieri/iras/sage-4.4.alph\
a1x/spkg/build/libm4ri-20100221/src/missing --run aclocal-1.11
/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-20100221/src/missing: l\
ine 54: aclocal-1.11: command not found
WARNING: `aclocal-1.11' is missing on your system.  You should only need it if
         you modified `acinclude.m4' or `configure.ac'.  You might want
         to install the `Automake' and `Perl' packages.  Grab them from
         any GNU archive site.
 cd . && /bin/sh /home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-201002\
21/src/missing --run automake-1.11 --gnu
/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-20100221/src/missing: l\
ine 54: automake-1.11: command not found
WARNING: `automake-1.11' is missing on your system.  You should only need it if
         you modified `Makefile.am', `acinclude.m4' or `configure.ac'.
         You might want to install the `Automake' and `Perl' packages.
         Grab them from any GNU archive site.
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/sh /home/palmieri/iras/sage-4.4.alph\
a1x/spkg/build/libm4ri-20100221/src/missing --run autoconf
/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-20100221/src/missing: l\
ine 54: autoconf: command not found
WARNING: `autoconf' is missing on your system.  You should only need it if
         you modified `configure.ac'.  You might want to install the
         `Autoconf' and `GNU m4' packages.  Grab them from any GNU
         archive site.
/bin/sh ./config.status --recheck
running CONFIG_SHELL=/bin/sh /bin/sh ./configure --prefix=/home/palmieri/iras/s\
age-4.4.alpha1x/local --includedir=/home/palmieri/iras/sage-4.4.alpha1x/local/i\
nclude/ CC=gcc CFLAGS= -I/home/palmieri/iras/sage-4.4.alpha1x/local/include/ -L\
/home/palmieri/iras/sage-4.4.alpha1x/local/lib -g -fPIC -Wall -pedantic  -O2 LD\
FLAGS= CPPFLAGS=-I/home/palmieri/iras/sage-4.4.alpha1x/local/include/ --no-crea\
te --no-recursion
checking build system type... ia64-unknown-linux-gnu
checking host system type... ia64-unknown-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... configure: error: newly created f\
ile is older than distributed files!
Check your system clock
make[2]: *** [config.status] Error 1
make[2]: Leaving directory `/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/lib\
m4ri-20100221/src'
Error building libm4ri
```

I haven't seen this on any other platform.


---

Comment by jhpalmieri created at 2010-04-20 20:26:24

Changing status from positive_review to needs_work.


---

Comment by malb created at 2010-04-20 20:53:29

I fixed the issue, tested it on iras and provided a new SPKG (replacing the old one), at:

 http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100221.spkg


---

Comment by malb created at 2010-04-20 20:53:37

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-04-20 20:54:18

All I did was to run 'make' and 'make distclean' on a different machine to fix the timestamps etc.


---

Comment by was created at 2010-05-07 23:59:39

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 22:02:34

Resolution: fixed


---

Comment by mvngu created at 2010-05-08 22:02:34

Merged [libm4ri-20100221.spkg](http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100221.spkg) in the standard spkg repository.
