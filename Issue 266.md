# Issue 266: sloane functions -- get rid of any pre-initialization

Issue created by migration from https://trac.sagemath.org/ticket/266

Original creator: was

Original creation time: 2007-02-16 07:21:21

Assignee: was

CC:  sage-combinat

Do some standard python trickier so that the sloane sequence objects are not created until they are used.   According to this, just importing sloane_sequences.py is now a nontrivial part of the SAGE startup time, which is ridiculous:


```
   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.070    0.070    0.093    0.093 functional.py:9(<module>)
       30    0.049    0.002    1.224    0.041 all.py:1(<module>)
 1575/274    0.046    0.000    0.087    0.000 ro.py:58(_flatten)
     5284    0.039    0.000    0.039    0.000 :0(append)
        1    0.038    0.038    0.038    0.038 matrix_space.py:15(<module>)
        8    0.036    0.005    0.495    0.062 all.py:3(<module>)
        2    0.036    0.018    1.284    0.642 all.py:4(<module>)
        1    0.027    0.027    0.049    0.049 sloane_functions.py:42(<module>)
```


Of course, the sloane_functions.py module needs to be broken up a lot. 


---

Comment by ncalexan created at 2007-02-18 21:08:23

Changing assignee from was to ncalexan.


---

Comment by ncalexan created at 2007-02-18 21:09:30

Resolution: fixed


---

Comment by ncalexan created at 2007-02-18 21:09:30

Fixed for 2.1.5.  Sloane now computes and caches trait_names() and __getattribute__ to pull SloaneSequence objects starting with 'A' from sage.combinat.sloane_functions.
