# Issue 163: plot hypergeometric_U fails

Issue created by migration from https://trac.sagemath.org/ticket/163

Original creator: wdj

Original creation time: 2006-10-29 22:51:31

Assignee: was

Keywords: pari, hyperu

This is funny:


```
P = plot(hypergeometric_U(1.0,1.0,x),0.1,0.9)
```

fails (hangs, actually) but 

```
sage: f = lambda x: gp.eval("hyperu(1,1,%s)"%x)
sage: P = plot(f,0,1)
sage: show(P)
```


hypergeometric_U is in functions/special.py. The error
may have something to do with the pari class.

works fine.


---

Comment by mabshoff created at 2007-08-28 18:43:41

With Sage 2.8.2 I get:

```
[mabshoff@m940 sage-2.8.2]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.2, Release Date: 2007-08-22                       |
| Type notebook() for the GUI, and license() for information.        |
sage: P = plot(hypergeometric_U(1.0,1.0,x),0.1,0.9)
---------------------------------------------------------------------------
<class 'gen.PariError'>                   Traceback (most recent call last)

/tmp/Work2/sage-2.8.2/<ipython console> in <module>()

/tmp/Work2/sage-2.8.2/local/lib/python2.5/site-packages/sage/functions/special.py in hypergeometric_U(alpha, beta, x, prec)
    570     from sage.libs.pari.all import pari
    571     R,a = _setup(prec)
--> 572     b = R(pari(x).hyperu(alpha,beta))
    573     pari.set_real_precision(a)
    574     return b

/tmp/Work2/sage-2.8.2/gen.pyx in gen._pari_trap()

<class 'gen.PariError'>: incorrect type (20)
```

Maybe this is something for Sage Bug Day 2.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-28 18:43:41

Changing component from interfaces to number theory.


---

Comment by mabshoff created at 2007-09-23 14:53:46

Changing type from task to defect.


---

Comment by was created at 2007-10-21 01:55:04

Resolution: fixed


---

Comment by was created at 2007-10-21 01:55:04

This now gives a type error, as it should.  The right thing to do is:

```
sage: P = plot(lambda x: hypergeometric_U(1.0,1.0,x),0.1,0.9)
sage: show(P)
```

