# Issue 8375: Numerical noise in devel/sage/sage/symbolic/pynac.pyx

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-02-26 09:00:54

Assignee: drkirkby

*== The computer hardware & software ==
 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM 
 * Solaris 10 03/2005 - the first release of Solaris 10. 

 == The Sage software ==
Sage 4.3.3 with various patches to get it to compile on Solaris. (The notebook is not working properly though). 

 == The test failure == 


```
**********************************************************************
File "/export/home/drkirkby/sage-4.3.3/devel/sage/sage/symbolic/pynac.pyx", line 1282:
    sage: py_exp(float(1))
Expected:
    2.7182818284590451
Got:
    2.7182818284590455
**********************************************************************
```



---

Comment by drkirkby created at 2010-02-26 14:53:11

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-02-26 14:53:11

The attached patch fixes this. It also has some notes showing 

 * A high precision value of e
 * The IEEE 754 value 
 * The correctly rounded result
 * The value given on the SPARC processor. 


```
drkirkby`@`redstart:~/sage-4.3.3$ ./sage -t devel/sage/sage/symbolic/pynac.pyx
sage -t  "devel/sage/sage/symbolic/pynac.pyx"
         [156.7 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 156.7 seconds
sage/sage/symbolic/pynac.pyx.3$ drkirkby`@`redstart:~/sage-4.3.3$ ./sage -t devel/
-bash: drkirkby`@`redstart:~/sage-4.3.3$: No such file or directory
sage -t  "devel/sage/sage/symbolic/pynac.pyx"
         [156.7 s]

```



---

Comment by mpatel created at 2010-03-03 09:23:22

The patches at #8374 and here fix the corresponding doctest failures in 4.3.0.1 on t2 and still pass in 4.3.3 on sage.math.

Just to check: Did "sage-devel" agree that this was the best approach to the problem? 

I'm not sure if Minh is already reviewing these tickets.  To the extent it counts, my review is positive, provided that you fix the [minor, admittedly] spelling / grammatical errors.


---

Attachment

With grammer/spelling corrections.


---

Comment by drkirkby created at 2010-03-03 11:57:08

There was only one comment from Robert as to whether there was another way to get the SPARC processor to produce the same output as Intel. I mentioned there was, but it would require  very significant changes. 

The exact same correction for 'e' was made once before for the SPARC processor. It has been implemented numerous time for other processors. 

I've corrected the grammar/spelling.


---

Comment by jsp created at 2010-03-03 20:29:07

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-03-03 20:29:07

Replying to [comment:3 drkirkby]:
> There was only one comment from Robert as to whether there was another way to get the SPARC processor to produce the same output as Intel. I mentioned there was, but it would require  very significant changes. 
> 
> The exact same correction for 'e' was made once before for the SPARC processor. It has been implemented numerous time for other processors. 
> 
> I've corrected the grammar/spelling. 


From me a positive review.

Jaap


---

Comment by mhansen created at 2010-03-06 08:24:15

Resolution: fixed
