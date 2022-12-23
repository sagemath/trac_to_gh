# Issue 4841: Update Maxima to 5.17.x (new upstream)

Issue created by migration from https://trac.sagemath.org/ticket/4841

Original creator: mabshoff

Original creation time: 2008-12-20 22:24:20

Assignee: burcin

CC:  mhansen certik

There is a new Maxima spgk at

http://sage.math.washington.edu/home/mabshoff/maxima-5.17.1.spkg

but there are issues. It will probably (hopefully?) not be the final stable release of 5.17.x.

Issues coming up in the comment section next.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-20 22:28:09

Limits and assumption problems in functional.py:

```
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/functional.py", line 19:
    sage: limit(a*sin(x)/x, x=0)
    <SNIP>
    Is  a  positive, negative, or zero?
```

Limit regression, reported to maxima-dev already:

```
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/functional.py", line 301:
    sage: lim(1/x, x=0)
Expected:
    und
Got:
    +Infinity
```

This is also a limits+assumption issue, but WTF would that fail in sympy_test:

```
sage -t -long devel//sage/sage/calculus/test_sympy.py
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/test_sympy.py", line 60:
    : limit((tan(x+y) - tan(x))/y, y=0)
    TypeError: Computation failed since Maxima requested additional constraints (use assume):
    Is  tan(x)  positive, negative, or zero?
```

Not sure what happens here, i.e whether this is Maxima's or Sage's fault:

```
sage -t -long devel//sage/sage/functions/special.py
**********************************************************************
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/functions/special.py", line 847:
    sage: spherical_harmonic(3,2,x,y)
    TypeError: Error executing code in Maxima
    CODE:
    	sage5 : spherical_harmonic(3,2,x,y)$
    Maxima ERROR:
    	
    Bad argument to `genfact'
```

Version failures, trivial to fix, but also erf seems to have improved:

```
sage -t -long devel//sage/sage/interfaces/maxima.py
**********************************************************************
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/interfaces/maxima.py", line 999:
    sage: maxima.version()
Expected:
    '5.16.3'
Got:
    '5.17.1'
**********************************************************************
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/interfaces/maxima.py", line 1689:
    sage: f.numer()         # I wonder how to get a real number (~1.463)??
Expected:
    -.8862269254527579*%i*erf(%i)
Got:
    -.8862269254527579*%i*(1.650425758797543*%i+1.110223024625156E-16)
**********************************************************************
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/interfaces/maxima.py", line 2300:
    sage: maxima_version()
Expected:
    '5.16.3'
Got:
    '5.17.1'
**********************************************************************
```


Issue in calculus.py:

```
File "/home/mabshoff/build-3.2.2/sage-3.2.2-eno/devel/sage-main/sage/calculus/calculus.py", line 6618:
    sage: complex(erf(3*I))
Expected:
    Traceback (most recent call last):
    ...
    TypeError: unable to simplify to complex approximation
Got:
    (1.110223024625156e-16+1629.9946226005709j)


Trying:
    p1 = plot(xt,Integer(0),Integer(1)/Integer(2),rgbcolor=(Integer(1),Integer(0),Integer(0)))###line 2452:_sage_    >>> p1 = plot(xt,0,1/2,rgbcolor=(1,0,0))
Expecting nothing
Exception exceptions.RuntimeError: RuntimeError('maximum recursion depth exceeded',) in  ignored
<Repeated indefinitely>

The following doctest causes this:

        Next we form the augmented matrix of the above system:
            sage: A = matrix([[s, 16, 270],[1, s, 90+1/s]])
            sage: E = A.echelon_form()
            sage: xt = E[0,2].inverse_laplace(s,t)
            sage: yt = E[1,2].inverse_laplace(s,t)
            sage: print xt
                                4 t         - 4 t
                           91  e      629  e
                         - -------- + ----------- + 1
                              2            2
            sage: print yt
                                 4 t         - 4 t
                            91  e      629  e
                            -------- + -----------
                               8            8
            sage: p1 = plot(xt,0,1/2,rgbcolor=(1,0,0))
            sage: p2 = plot(yt,0,1/2,rgbcolor=(0,1,0))
            sage: (p1+p2).save()
```


There are likely more issues in calculus.py

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-20 22:28:54

Changing assignee from burcin to mabshoff.


---

Comment by mabshoff created at 2008-12-20 22:28:54

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-26 18:13:45

Resolution: wontfix


---

Comment by mabshoff created at 2008-12-26 18:13:45

Wontfix since there are regressions with assumptions that are too much of a problem compared with the benefit of upgrading. If someone disagrees feel free to reopen the ticket.

Cheers,

Michael
