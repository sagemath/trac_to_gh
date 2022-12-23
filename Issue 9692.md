# Issue 9692: Doctest failure of sage/symbolic/expression.pyx on Solaris 10 x86

Issue created by migration from https://trac.sagemath.org/ticket/9692

Original creator: drkirkby

Original creation time: 2010-08-05 23:11:43

Assignee: mvngu

CC:  jhpalmieri

An almost complete 32-bit port of Sage 4.5.2 to Solaris 10 on x86 processors had been done on the following hardware:

 * Dell OptiPlex 755
 * 2.40 GHz Intel Quad-Core Core2 Q6600 CPU
 * 8 GB RAM, 8 GB swap. 
 * Solaris 10 update 5 (5/08) on x86 
 * gcc 4.5.0 configured to use the Sun linker and GNU assembler
 * sage-4.5.2.rc1 with several changes. 

The following doctest failed. 


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
```


Some of these look like numerical rounding errors:


```
Expected:
    ([0, 0, 1, 1, 0], -9.0604285688230899)
Got:
    ([0, 0, 1, 1, 0], -9.0604285688230917)
```


but in other cases the number of digits being displayed is less than the expected value. 


```
Expected:
    -10.610333495739708
Got:
    -10.61033349573971
```

The "Got:" value is a correctly rounded version of the "Expected:" value, but I'm not sure if printing less digits is acceptable.

I personally like to see these numerical results being computed to high precision by another method if possible. I've got no idea how to compute these values, so have no idea if these are are anywhere near correct. 



---

Comment by jhpalmieri created at 2010-08-16 21:44:55

I think this ticket is a duplicate of #9735, #9689, and/or #9693.  Is that right?  Can it be closed?

(The ticket summary talks about symbolic/expression.pyx, which is covered by #9689 and #9693, while the description talks about chmm.pyx, which is covered by #9735.)


---

Comment by drkirkby created at 2010-08-16 22:09:18

Resolution: duplicate


---

Comment by drkirkby created at 2010-08-16 22:09:18

Yes, it can. 

I've no idea why the title says one ticket and the description another. But I think we are clear about what the issues are.
