# Issue 8374: Numerical noise in devel/sage/sage/symbolic/constants_c.pyx

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-02-26 08:56:12

Assignee: drkirkby

## The computer hardware & software
 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM 
 * Solaris 10 03/2005 - the first release of Solaris 10. 

 == The Sage software ==
Sage 4.3.3 with various patches to get it to compile on Solaris. (The notebook is not working properly though). 

 == The test failure == 

```
****************************************************************
File "/export/home/drkirkby/sage-4.3.3/devel/sage/sage/symbolic/constants_c.pyx", line 197:
    sage: e.__float__()
Expected:
    2.7182818284590451
Got:
    2.7182818284590455
****************************************************************
}}} 
 
This failure on SPARC when displaying E has been seen before.


---

Comment by drkirkby created at 2010-02-26 15:28:12

The attached patch fixes these two failures. 


```
kirkby`@`redstart:~/sage-4.3.3$ ./sage -t devel/sage/sage/symbolic/constants_c.p
sage -t  "devel/sage/sage/symbolic/constants_c.pyx"
         [65.4 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 65.4 seconds
drkirkby`@`redstart:~/sage-4.3.3$
yxkirkby`@`redstart:~/sage-4.3.3$ ./sage -t devel/sage/sage/symbolic/constants_c.py
sage -t  "devel/sage/sage/symbolic/constants_c.pyx"
         [77.5 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 77.5 seconds
```


An optional test, which currently expoects the same value of e has also been changed.

The patch, which will be attached shortly, also has some notes showing

 * A high precision value of e
 * The IEEE 754 value
 * The correctly rounded result
 * The value given on a Sun Blade 1000 with SPARC processors.

Dave


---

Comment by drkirkby created at 2010-02-26 15:39:20

Mercurial patch


---

Attachment


---

Comment by drkirkby created at 2010-02-26 15:40:18

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-03-03 09:25:23

I've left a [comment:ticket:8375:2 review comment] at #8375.


---

Attachment


---

Comment by drkirkby created at 2010-03-03 12:04:52

I've addressed the spelling & grammar errors in 8374-numerical-noise.2.patch  I forgot to overwrite the old one, so there is now a second patch. 

See also comments at #8375


---

Comment by jsp created at 2010-03-03 20:34:23

Replying to [comment:5 drkirkby]:
> I've addressed the spelling & grammar errors in 8374-numerical-noise.2.patch  I forgot to overwrite the old one, so there is now a second patch. 
> 
> See also comments at #8375

So a positive review.

Jaap


---

Comment by jsp created at 2010-03-03 20:34:23

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 08:25:12

Resolution: fixed
