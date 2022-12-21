# Issue 9735: Numerical noise on sage/stats/hmm/chmm.pyx on both Solaris x86 and OpenSolaris x86

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-12 16:55:29

Assignee: mvngu

The following test failure seen on both a Sun Ultra 27 running OpenSolaris 06/2009 and a Dell Optiplex 755 running Solaris 10 on the x86 processor. 

## On a Sun Ultra 27 running OpenSolaris
 * Sun Ultra 27 
 * 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 
 * 12 GB RAM
 * OpenSolaris 2009.06 snv_134b X86
 * Sage 4.5.3.alpha0
 * gcc 4.5.0

```
sage -t  -long devel/sage/sage/stats/hmm/chmm.pyx
**********************************************************************
File "/export/home/drkirkby/32/sage-4.5.3.alpha0/devel/sage-main/sage/stats/hmm/chmm.pyx", line 570:
    sage: m.viterbi([0,1,10,10,1])
Expected:
    ([0, 0, 1, 1, 0], -9.0604285688230899)
Got:
    ([0, 0, 1, 1, 0], -9.0604285688230917)
**********************************************************************
File "/export/home/drkirkby/32/sage-4.5.3.alpha0/devel/sage-main/sage/stats/hmm/chmm.pyx", line 132:
    sage: m.baum_welch(obs)
Expected:
    (-10.610333495739708, 14)
Got:
    (-10.61033349573971, 14)
**********************************************************************
File "/export/home/drkirkby/32/sage-4.5.3.alpha0/devel/sage-main/sage/stats/hmm/chmm.pyx", line 134:
    sage: m.log_likelihood(obs)
Expected:
    -10.610333495739708
Got:
    -10.61033349573971
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_15
   2 of  12 in __main__.example_2
***Test Failed*** 3 failures.
For whitespace errors, see the file /export/home/drkirkby/.sage//tmp/.doctest_chmm.py
	 [2.9 s]
```


## On a Dell Optiplex 755 running Solaris 10 x86
 * Dell Optiplex 755
 * 2.4 GHz Quad-Core Intel Core Q6600 
 * 8 GB RAM
 * Solaris 10 x86 (update 5, 5/08)
 * gcc 4.5.1 configured to use the Sun linker and GNU assembler from binutils-2.20.1. 
 * 32-bit build. 
 * Using sage-4.5.2.rc1

```
sage -t  -long devel/sage/sage/stats/hmm/chmm.pyx
**********************************************************************
File "/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/devel/sage-main/sage/stats/hmm/chmm.pyx", line 570:
    sage: m.viterbi([0,1,10,10,1])
Expected:
    ([0, 0, 1, 1, 0], -9.0604285688230899)
Got:
    ([0, 0, 1, 1, 0], -9.0604285688230917)
**********************************************************************
File "/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/devel/sage-main/sage/stats/hmm/chmm.pyx", line 132:
    sage: m.baum_welch(obs)
Expected:
    (-10.610333495739708, 14)
Got:
    (-10.61033349573971, 14)
**********************************************************************
File "/home/palmieri/fulvia/32bit/sage-4.5.2.rc1/devel/sage-main/sage/stats/hmm/chmm.pyx", line 134:
    sage: m.log_likelihood(obs)
Expected:
    -10.610333495739708
Got:
    -10.61033349573971
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_15
   2 of  12 in __main__.example_2
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/palmieri/.sage_fulvia/tmp/.doctest_chmm.py
	 [11.4 s]
```



---

Comment by jhpalmieri created at 2010-08-12 22:04:05

Changing status from new to needs_review.


---

Attachment

Here's a patch.  This fixes the problem for me on fulvia, and test still pass on sage.math (for example).


---

Comment by drkirkby created at 2010-08-13 04:46:04

Thanks for writing the doctest John. 

Here's a couple of things worth noting

 == Comments by others about this issue ==



```
FWIW, here is the exact expected result in (obtained from my own
implementation, no proof but seems to be the same):
([0, 0, 1, 1, 0], -5/2*log(pi) - 15/2*log(2) - 1)

and in high precision:
([0, 0, 1, 1, 0],
-9.0604285688230902559878092893189710396844880399901933346892)

       Yann
```


and another from William Stein that:


```
I'm the upstream author of 100% of this code, and know precisely what
it does, which is a sequence of floating point ops and calls to the
math library, which *of course* can be machine dependent.

Put in dots.

 -- William
```


 == Test results on my Sun Ultra 27 ==

Prior to adding your patch I got a failure recorded in ptestlong.log, as noted in the ticket's description. After adding your patch, this passes. 


```
drkirkby`@`hawk:~/32/sage-4.5.3.alpha0$ ./sage -t  -long devel/sage/sage/stats/hmm/chmm.pyx
sage -t -long "devel/sage/sage/stats/hmm/chmm.pyx"          
	 [11.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 11.2 seconds
```


So positive review. 

Dave


---

Comment by drkirkby created at 2010-08-13 04:46:04

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-16 21:50:10

Changing priority from major to blocker.


---

Comment by leif created at 2010-08-23 14:55:26

Sage 4.6.prealpha3, which includes this ticket, passed all tests (`ptestlong`) on 64-bit Fedora 13 (Core2, gcc 4.4.4), see also http://trac.sagemath.org/sage_trac/ticket/9343#comment:308 .


---

Comment by mpatel created at 2010-08-24 02:49:37

Resolution: fixed
