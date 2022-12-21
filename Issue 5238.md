# Issue 5238: remove qsieve.spkg and replace it by mpQS (part of FLINT)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-11 23:20:59

Assignee: mabshoff

This ought to be doable in the 3.4 release once the ReST patches are in:

```
FLINT ships with a much improved version of qsieve. It is now called mpQS.

If you do make mpQS in the main directory of  FLINT (make all also
builds it) it will build a program which replaces the old qsieve.
However this program will deal with much smaller integers, and is much
faster overall.

It should have far fewer issues than the old code.

It also handles numbers with small factors, but still won't handle
integers which are perfect powers or primes. These should be scanned
for before running mpQS.

The new program actually uses FLINT for some parts of the computation,
so it cannot be built standalone (it doesn't link against libflint, it
just includes the files it needs). I have just verified this program
still builds (and works) on sage.math.

Bill.
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 02:26:28

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by mvngu created at 2010-06-16 02:09:36

Close as fixed:


```
[mvngu`@`sage flint-1.5.0.p4]$ pwd
/dev/shm/mvngu/sage-4.4.4.alpha0/spkg/standard/flint-1.5.0.p4
[mvngu`@`sage flint-1.5.0.p4]$ find src/ | grep 'mpQS'
src/QS/mpQS.h
src/QS/mpQS.c
[mvngu`@`sage flint-1.5.0.p4]$ find src/ | grep 'qsieve'
<no-output>
```



---

Comment by mvngu created at 2010-06-16 02:09:36

Resolution: fixed
