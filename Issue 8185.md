# Issue 8185: numerical noise + crash on sage/calculus/functional.py

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-02-04 16:05:54

Assignee: drkirkby

## Build environment
This was built on a very old / low spec SPARC. But there are some interesting results when built on newer hardware - see later. 

 * Sun Netra T1 UltraSPARC IIe `@` 500 MHz. 
 * Solaris 10 03/05 (first Solaris release of Solaris 10)
 * Sage 4.3.0.1 (special build by Minh for Solaris SPARC. 4.3.0 source, but with #6595 added)
 * gcc 4.4.2 configured with Sun linker and Sun assembler.
 * 32-bit mode - SAGE64 was *not* set to 'yes'

## The problem

drkirkby`@`kestrel:~/sage-4.3.0.1$ ./sage -t  "devel/sage-main/build/sage/calculus/functional.py"
init.sage does not exist ... creating
sage -t  "devel/sage-main/build/sage/calculus/functional.py"

```
**********************************************************************
File "/export/home/drkirkby/sage-4.3.0.1/devel/sage-main/build/sage/calculus/functional.py", line 195:
    sage: float(area)
Expected:
    0.85914091422952255
Got:
    0.85914091422952277
********************************************************************
```


This in itself looks easy to fix. 

## Interesting side notes
 * Copying the binary to 't2' results in the same problem - no great surprise there. 
 * Building this test on a Sun Blade 2000 with gcc 4.4.1 and running it on the Sun Blade 2000, results in not just numerical noise, but a complete crash 


```
drkirkby`@`swan:[~/sage-4.3.0.1] $ ./sage -t  "devel/sage-main/build/sage/calculus/functional.py"
sage -t  "devel/sage-main/build/sage/calculus/functional.py"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [3.1 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:
```


## Conclusions
 * There is definitely an issue with numerical noise on this test due no doubt to SPARC processor having slightly different to those of an Intel. That is observed both on the Netra T1 and the T5240.
 * A crash is occurring whilst running this test on the Sun Blade 2000. This could potentially be the use of a slightly older compiler (gcc 4.4.1). The RAM is a lot more (8 GB) than on the Sun Netra T1 (1.5 GB) where there is just numerical noise, so it's not a lack of RAM causing this. 
 * Copying this from a very old SPARC to the Sun T5240 results in no crashes - only the numerical noise issue. 




---

Comment by drkirkby created at 2010-02-04 19:51:13

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-02-04 19:51:13

Here's a Mercurial patch, which fixes the issue 


```
drkirkby`@`kestrel:~/sage-4.3.0.1$ ./sage -t devel/sage-main/build/sage/calculus/functional.py
sage -t  "devel/sage-main/build/sage/calculus/functional.py"
         [65.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 65.0 seconds
```



---

Attachment


---

Comment by robertwb created at 2010-02-04 20:55:36

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:02:24

Resolution: fixed
