# Issue 2977: [with patch, needs review] wronskian is broken on constants

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-04-21 00:35:15

Assignee: was

Hi,

Here's something unpleasant that occurs in sage-3.0.rc0:


```
sage: wronskian(1, e^(-x), e^(2*x))
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/root/<ipython console> in <module>()

/opt/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/calculus/functions.py in wronskian(*args)
     80             # if the last argument isn't a variable, just run
     81             # .derivative on everything 
     82             fs = args
     83             row = lambda n: map(lambda f: f.derivative(n), fs)
---> 84         return matrix(map(row, range(len(fs)))).determinant()

/opt/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/calculus/functions.py in <lambda>(n)
     80             # if the last argument isn't a variable, just run
     81             # .derivative on everything 
     82             fs = args
---> 83             row = lambda n: map(lambda f: f.derivative(n), fs)
     84         return matrix(map(row, range(len(fs)))).determinant()

/opt/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/calculus/functions.py in <lambda>(f)
     80             # if the last argument isn't a variable, just run
     81             # .derivative on everything 
     82             fs = args
---> 83             row = lambda n: map(lambda f: f.derivative(n), fs)
     84         return matrix(map(row, range(len(fs)))).determinant()

<type 'exceptions.AttributeError'>: 'sage.rings.integer.Integer' object has no attribute 'derivative'
```


There is an easy fix, see the patch.  I have also removed "differentiate" as an alias for "derivative", since I seem to remember that the consensus on sage-devel was to keep only "derivative" and "diff".



---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-04-21 02:48:24

Merged in Sage 3.0.rc1


---

Comment by mabshoff created at 2008-04-21 02:48:24

Resolution: fixed
