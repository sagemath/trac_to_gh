# Issue 8462: Numerical noise in /sage/sage/plot/colors.py on Solairs SPARC

Issue created by migration from https://trac.sagemath.org/ticket/8462

Original creator: drkirkby

Original creation time: 2010-03-06 22:29:21

Assignee: was

CC:  kcrisman robertwb wcauchois

Running Solaris 10 on a SPARC, I get some numerical noise on this. Since these are RGB values. 


```
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/plot/colors.py", line 660:
    sage: gold / pi + yellow * e
Expected:
    RGB color (0.51829585732141792, 0.49333037605210095, 0.0)
Got:
    RGB color (0.51829585732141814, 0.49333037605210117, 0.0)
**********************************************************************
```


The test makes use of 'e'. As has been shown on various other trac tickets (e.g. #8374, #8375), the value of 'e' returned by the SPARC processor is less accurate then the Intel/ADM chips. 

Dave 




---

Comment by drkirkby created at 2010-03-06 22:34:50

The Mercurial patch I am about to attach fixes this. Tested on a Sun Blade 1000 with a pair of 900 MYHz UltraSPARC III+ processors. 


```
drkirkby@redstart:~/32/sage-4.3.4.alpha0$ ./sage -t  "devel/sage/sage/plot/colors.py"
sage -t  "devel/sage/sage/plot/colors.py"                   
         [13.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 13.2 seconds
```



---

Comment by drkirkby created at 2010-03-06 22:34:50

Changing status from new to needs_review.


---

Attachment

Mercurial patch to fix numerical noise on SPARC processor


---

Comment by mhansen created at 2010-03-06 23:15:11

Looks good to me.


---

Comment by mhansen created at 2010-03-06 23:15:11

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 23:47:51

Resolution: fixed
