# Issue 2021: SR eigenvalues and eigenvectors returns nonsense in both cases in the simplest example

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-01 03:29:51

Assignee: was


```
sage: a = matrix(SR, 2, [1,2,3,4])
sage: a.eigenspaces()
Traceback (most recent call last):
...
TypeError: 'SymbolicArithmetic' object is not iterable
sage: a.eigenvalues()
[]
```



---

Comment by was created at 2008-02-01 03:32:56

The problems go on:


```
sage: a.eigenvalues(SR)
Traceback (most recent call last):
...
NotImplementedError
sage: a.eigenvalues(CC)
Traceback (most recent call last):
...
TypeError: len() of unsized object
sage: a.eigenvalues?
Docstring: [nothing]
```



---

Comment by jason created at 2008-02-01 15:29:55

Something *very* weird is going on here.  Here is something that I think is causing the problem with a.eigenvalues above:


```
sage: from sage.calculus.calculus import SymbolicVariable
sage: tmp=SymbolicVariable('tmp_var')
sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(tmp).expand().solve(tmp)
[]
sage: (tmp^2+2*tmp).solve(tmp)
[]
sage: tmp=SymbolicVariable('tmp_var')
sage: (tmp^2+2*tmp).solve(tmp)
[tmp_var == -2, tmp_var == 0]
sage:
Exiting SAGE (CPU time 0m0.13s, Wall time 0m46.43s).
Exiting spawned Maxima process.
Exiting spawned Maxima process.
```


The suspicious thing is the *two* maxima processes that are exiting when I exit sage.


---

Comment by jason created at 2008-02-01 15:42:27

More data below.  When calling a.charpoly(y).expand().solve(y) first, things are messed up.  When calling it after solving an equation with y, things work fine


```
sage: from sage.calculus.calculus import SymbolicVariable
sage: y=SymbolicVariable('y')
sage: a=matrix(SR,[[1,2],[3,4]])
sage: # First solve an equation, then solve a.charpoly
sage: (y+1).solve(y)
[y == -1]
sage: a.charpoly(y).expand().solve(y)
[y == (5 - sqrt(33))/2, y == (sqrt(33) + 5)/2]
sage: y=SymbolicVariable('y')
sage: # Now solve a.charpoly, then solve an equation
sage: a.charpoly(y).expand().solve(y)
[]
sage: (y+1).solve(y)
[]
```



---

Comment by jason created at 2008-02-01 15:48:16

This is a complete shot in the dark, but does the problem have to do with asking one maxima instance a question that only makes sense to the other maxima instance?  In which instance is the symbolic variable kept and in which instance is the matrix kept?


---

Comment by gfurnish created at 2008-02-01 18:26:52

The key part here seems to be that 
sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(x).solve(x)
[]
while
sage: x._maxima_()
x
sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(x).solve(x)
[x == (5 - sqrt(33))/2, x == (sqrt(33) + 5)/2]

In fact, we may manually reproduce this behavior by 
sage: x._maxima_(maxima)sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(x).solve(x)
[]

It follows the likely cause is then not importing maxima from calculus somewhere and using instead the global maxima for a calculation involving charpoly.


---

Comment by gfurnish created at 2008-02-01 18:29:49

The key part here seems to be that 


```
sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(x).solve(x) []
```

while 


```
sage: x._maxima_() 
x 
sage: a=matrix(SR,[[1,2],[3,4]])
sage: a.charpoly(x).solve(x) 
[x == (5 - sqrt(33))/2, x == (sqrt(33) + 5)/2]
```


In fact, we may manually reproduce this behavior by


```
sage: x._maxima_(maxima)
x
sage: a=matrix(SR,[[1,2],[3,4]]) 
sage: a.charpoly(x).solve(x) []
```


It follows the likely cause is then not importing maxima from calculus somewhere and using instead the global maxima for a calculation involving charpoly.  Sorry about the double post but this at least is readable.


---

Comment by gfurnish created at 2008-02-01 18:57:30

changing the import in matrix_symbolic_dense from from


```
from sage.interfaces.maxima import maxima
```

to 

```
from sage.calculus.calculus import maxima
```

appears to fix the problem.  However, it appears that this issue is unrelated to the original eigenspaces issue.


---

Attachment

Thanks to gfurnish's brilliance, we found a sticky maxima issue corrected in the first patch (with an added doctest to make sure something like that doesn't happen again!)


---

Comment by jason created at 2008-02-01 19:20:12

Illustrating the eigenspaces issue:


```
sage: a=matrix(SR,[[1,2],[3,4]])
sage: b=matrix(QQ,[[1,2],[3,4]])
sage: [i for i in a.fcp()]
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/matrix/<ipython console> in <module>()

<type 'exceptions.TypeError'>: 'SymbolicArithmetic' object is not iterable
sage: [i for i in b.fcp()]
[(x^2 - 5*x - 2, 1)]
```



---

Comment by jason created at 2008-02-01 19:24:34

And another note:


```
sage: a=matrix(SR,[[1,2],[3,4]])
sage: [i for i in a.fcp().factor_list()]
[(x^2 - 5*x - 2, 1)]
```


So apparently we need to somehow call factor_list() when we have a symbolic matrix or we need to change SymbolicArithmetic to iterate through factor_list() when we ask for an iterator.


---

Comment by was created at 2008-02-01 22:52:19

[positive review] for symbolic-matrix-maxima.patch.  This is a serious bug fix that should be included ASAP.


---

Comment by jason created at 2008-02-01 22:57:12

don't close this issue yet, though.  A second patch should be coming along to fix the eigenspaces issue.


---

Comment by mabshoff created at 2008-02-02 03:08:29

Replying to [comment:12 jason]:
> don't close this issue yet, though.  A second patch should be coming along to fix the eigenspaces issue.

Jason, please open another ticket for that issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 03:11:19

Resolution: fixed


---

Comment by mabshoff created at 2008-02-02 03:11:19

Merged in Sage 2.10.1.rc5
