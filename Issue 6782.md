# Issue 6782: Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/calculus.rst

Issue created by migration from https://trac.sagemath.org/ticket/6782

Original creator: drkirkby

Original creation time: 2009-08-20 21:29:19

Assignee: burcin

On Solaris (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1


```

----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
<SNIP>

```
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/calculus.rst", line 117:
    sage: maxima(f).powerseries(x,0)
Expected:
    ('sum((-1)^i2*2^(2*i2)*bern(2*i2)*x^(2*i2)/(i2*(2*i2)!),i2,1,inf))/2
Got:
    'sum((-1)^i2*2^(2*i2-1)*bern(2*i2)*x^(2*i2)/(i2*(2*i2)!),i2,1,inf)

```




---

Comment by AlexGhitza created at 2009-08-20 23:08:47

Changing assignee from burcin to AlexGhitza.


---

Comment by AlexGhitza created at 2009-08-20 23:08:47

This one is trivial; see attached patch.


---

Comment by AlexGhitza created at 2009-08-20 23:08:47

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-08-20 23:08:47

Changing keywords from "" to "maxima".


---

Attachment

apply after spkg's at #6564 and #6699


---

Comment by drkirkby created at 2009-08-21 05:41:57

The log was generated with Maxima 5.19.1, not 5.19.0, so I'm changing the title slightly to reflect this.


---

Comment by drkirkby created at 2009-08-21 07:50:02

Are these mathematically equivalent? It seems to me the factor in the numerator has changed from (2*i2) to (2*i2-1) and denominator from 2 to 1. That seems a different result to me. 

I tried what I *think* the test is doing in Mathematica and got:


```
In[7]:= f=Log[Sin[x]/x]

            Sin[x]
Out[7]= Log[------]
              x

In[8]:=  Series[f,{x,0,12}]

          2    4      6      8       10           12
        -x    x      x      x       x        691 x           13
Out[8]= --- - --- - ---- - ----- - ------ - ---------- + O[x]
         6    180   2835   37800   467775   3831077250

In[9]:=
```


I've no idea what's right or not. 

Dave


---

Comment by AlexGhitza created at 2009-08-21 09:26:38

The difference is `2^(2*i2)/2` versus `2^(2*i2-1)`.  Yes, they are the same.


---

Comment by mvngu created at 2009-09-02 10:56:09

Resolution: fixed


---

Comment by mvngu created at 2009-09-02 10:56:09

This is fixed by #6699.
