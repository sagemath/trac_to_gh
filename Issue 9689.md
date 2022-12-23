# Issue 9689: Numerical noise on devel/sage-main/sage/symbolic/expression.pyx

Issue created by migration from https://trac.sagemath.org/ticket/9689

Original creator: drkirkby

Original creation time: 2010-08-05 08:27:45

Assignee: mvngu

CC:  jhpalmieri

Whilst there is no complete 64-bit build of Sage on Solaris x86, a sufficiently large part of Sage does build (with a few changes) on Solaris 10 x86. When built on 'fulvia', a Dell Optiplex with Xeon processors, there was a numerical noise issue - see #9099


```
sage -t  -long devel/sage/sage/symbolic/expression.pyx
**********************************************************************
File "/home/palmieri/fulvia/sage-4.5.2.rc0/devel/sage-main/sage/symbolic/expression.pyx", line 498\
3:
    sage: maxima('sinh(1.0)')
Expected:
    1.175201193643801
Got:
    1.175201193643802
```


A computation with Mathematica, using 60 digits of precision gives 


```
In[2]:= N[Sinh[1],60]

Out[2]= 1.17520119364380145688238185059560081515571798133409587022957
```


The absolute error on Solaris x86 is slighly higher than seen on some other systems, but this is still a perfectly acceptable result.

This should be fairly easy to fix. I'll make a patch later today

Dave


---

Comment by drkirkby created at 2010-08-05 17:10:53

I just realise the second failure shown on #9099


```
Expected:
    0.881373587019543
Got:
    .8813735870195429
```


is the same file (devel/sage-main/sage/symbolic/expression.pyx) as this simple numerical noise issue. Hopefully be solved too. That's a less obvious problem to solve though. 

Any ideas anyone?


---

Comment by drkirkby created at 2010-08-05 22:38:12

Changing status from new to needs_review.


---

Attachment

Solves the numerical noise issue computing sinh(1.0). The archsinh case is more complex, and will be on another ticket.


---

Comment by jhpalmieri created at 2010-08-05 23:03:24

It's not very pretty, but 

```
abs(float(maxima('asinh(1.0)')) - 0.881373587019543) < 1e-15
```

or

```
maxima('abs(asinh(1.0) - 0.881373587019543)') < 1e-15
```

work for the other test.  Or:

```
sage: float(maxima('asinh(1.0)'))
0.8813735870195429...
```



---

Comment by jhpalmieri created at 2010-08-05 23:03:59

Or replace "float" with "RR", etc.


---

Comment by drkirkby created at 2010-08-05 23:19:57

Yes, we can get this to pass, but that is just covering up a bug, as the number should never be printed as `.8813735870195429` It is a numerically correct result, but it is not printed the way one would expect a piece of software to print the number. 
 	 	
Carl Witty is of the opinion this is either a Maxima or ECL bug

http://groups.google.com/group/sage-devel/msg/aa318e11e84afe8d?hl=en

I think its better to leave the `asinh(1.0)` case failing. It will be a constant reminder we need to get a real solution, not hack the doctest to get it to pass. 

Ultimately, I feel the doctest has discovered a bug, which is what a good test should do. 

Dave


---

Comment by drkirkby created at 2010-08-05 23:48:12

I created #9693 to resolve the leading zero problem and are going to copy the problem to the ECL and Maxima mailing lists, to see if we get any response. 

Dave


---

Comment by cremona created at 2010-08-12 17:49:49

This looks fine to me and passed tests (in that file) on both 32-bit and 64-bit ubuntu.


---

Comment by cremona created at 2010-08-12 17:49:49

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-08-12 18:22:15

Replying to [comment:8 cremona]:
> This looks fine to me and passed tests (in that file) on both 32-bit and 64-bit ubuntu.

Thank you for the review John. 

Dave


---

Comment by mpatel created at 2010-08-16 21:49:51

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-08-24 02:51:17

Resolution: fixed
