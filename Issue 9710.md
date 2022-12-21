# Issue 9710: Assumptions not passed to differential equation solver

Issue created by migration from Trac.

Original creator: kedlaya

Original creation time: 2010-08-09 14:27:20

Assignee: burcin

CC:  robert.marik kcrisman jdemeyer

Keywords: differential equations, assumptions

The assume function doesn't seem to work with the differential equation solver, despite what the documentation for desolve suggests. This returns an error:

```
sage: x = var('x')
sage: k = var('k')
sage: y = function('y',x)
sage: assume(k>0)
sage: print desolve(diff(y,x,x)+k*y-exp(-k*x),[y,x])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_25.py", line 10, in <module>
    exec compile(u'open("___code___.py","w").write("# -*- coding: utf-8 -*-\\n" + _support_.preparse_worksheet_cell(base64.b64decode("eCA9IHZhcigneCcpCmsgPSB2YXIoJ2snKQp5ID0gZnVuY3Rpb24oJ3knLHgpCmFzc3VtZShrPjApCnByaW50IGRlc29sdmUoZGlmZih5LHgseCkrayp5LWV4cCgtayp4KSxbeSx4XSk="),globals())+"\\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpyNFGr0/___code___.py", line 7, in <module>
    exec compile(u'print desolve(diff(y,x,x)+k*y-exp(-k*x),[y,x])
  File "", line 1, in <module>
    
  File "/home/kedlaya/sage-complete/local/lib/python2.6/site-packages/sage/calculus/desolvers.py", line 340, in desolve
    soln = maxima(cmd)
  File "/home/kedlaya/sage-complete/local/lib/python2.6/site-packages/sage/interfaces/expect.py", line 1032, in __call__
    return cls(self, x, name=name)
  File "/home/kedlaya/sage-complete/local/lib/python2.6/site-packages/sage/interfaces/expect.py", line 1451, in __init__
    raise TypeError, x
TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(k>0)' before integral or limit evaluation, for example):
Is  k  positive, negative, or zero?
```

Found by Praveen N. and Aashita during Sage Days 25 coding sprint.



---

Comment by kedlaya created at 2010-08-10 02:58:22

Observed later: ticket #8931 is similar, possibly enough so for this to be considered a duplicate. Also, I misread the documentation:

```
       This equation can be solved within Maxima but not within Sage. It
       needs assumptions assume(x>0,y>0) and works in Maxima, but not in
       Sage:
    
          sage: assume(x>0) # not tested
          sage: assume(y>0) # not tested
          sage: desolve(x*diff(y,x)-x*sqrt(y^2+x^2)-y,y,show_method=True) # not tested
```

So no promise is being made, but nonetheless I think this needs to be fixed.


---

Comment by robert.marik created at 2010-09-21 20:12:24

with #9961:


```
marik`@`um-bc107:/opt/sage$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x=var('x'); f=function('f',x); k=var('k'); assume(k>0)
sage: desolve(diff(f,x,2)/f==k,f,ivar=x)
k1*e^(sqrt(k)*x) + k2*e^(-sqrt(k)*x)
```



---

Comment by robert.marik created at 2010-09-21 20:20:01

In fact, #9835 is sufficient to solve this problem. The patch #9961 which is on the top of #9835 is not necessary. For the problem from the description we have with #9835:

```
marik`@`um-bc107:/opt/sage$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x = var('x')
sage: k = var('k')
sage: y = function('y',x)
sage: assume(k>0)
sage: desolve(diff(y,x,x)+k*y-exp(-k*x),[y,x])
k1*sin(sqrt(k)*x) + k2*cos(sqrt(k)*x) + e^(-k*x)/(k^2 + k)
sage:
| Sage Version 4.5.3, Release Date: 2010-09-04                       |
| Type notebook() for the GUI, and license() for information.        |
```



---

Comment by kcrisman created at 2011-03-14 20:45:45

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-03-14 20:45:45

Yup, and still works.  Definitely same issue as #8931, which now has positive review.  

We could add yet another doctest, but in this case there are already so many tests of it, with another one coming at #8931, that it seems appropriate to simply say this is a dup.  

To release manager: please close this ticket.


---

Comment by kcrisman created at 2011-03-14 20:46:33

> We could add yet another doctest, but in this case there are already so many tests of it, with another one coming at #8931, that it seems appropriate to simply say this is a dup.  

The other tests being from #9961 and #9835.


---

Comment by kcrisman created at 2011-03-14 20:46:33

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-03-14 21:04:12

Sorry, forgot to actually cc: the release manager.


---

Comment by jdemeyer created at 2011-03-17 09:46:56

Resolution: duplicate
