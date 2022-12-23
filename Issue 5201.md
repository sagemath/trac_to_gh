# Issue 5201: make solve understand matrix equations

Issue created by migration from https://trac.sagemath.org/ticket/5201

Original creator: jason

Original creation time: 2009-02-07 19:18:01

Assignee: burcin

I think it would be a great thing if solve could recognize matrices and that two matrices are equal if each entry is equal.  I believe MMA does this (but it's easier there; matrices are nothing more than nested lists).  It'd certainly make certain things I do more natural if I could do:

`solve(matrixA==matrixB)`

and that was equivalent to:

`solve([i==j for i,j in zip(matrixA.list(), matrixB.list())]) `


Okay, so now that I've written my piece, I suppose the next step is to open a trac ticket, write a patch to implement it, and post it for review :).


---

Comment by mabshoff created at 2009-02-07 19:23:11

Which part of no non-ReST tickets against 3.4 is hard to understand? :p

Cheers,

Michael


---

Comment by jason created at 2009-02-07 19:29:47

argh!  I looked at the list and thought "the first item is the ReST transition, so I have to pick the second item".  Apparently I was thinking that the next release was already out and 3.3 was the ReST transition.


---

Comment by jason created at 2010-05-26 15:15:32

Changing keywords from "" to "beginner".


---

Comment by ryan created at 2011-04-14 03:37:39

Could this be accomplished by overriding the comparison operator for the matrix class?

for example


```python
def __richcmp__(self, other_matrix, cmptype):
  if cmptype == 2:  #this is the '==' operator
    if is_Matrix(other_matrix):
      if False in [i==j for i,j in zip(self.list(), other_matrix.list())]:
        return False
      else: return True
```


I'm just not sure where the 'matrix class' is.  This would allow comparisons like


```
sage: matrixA == matrixB
True
```



---

Comment by jason created at 2011-04-14 03:50:19

You bring up a good point, and make me doubt whether the feature request is even feasible.  Certainly it's probably not a beginner ticket after all.  The problem is that we already have an == operator:


```
sage: a=matrix(SR,2,[x,x^2,x+1,x+4])
sage: b=matrix(SR,2,[4,3,2,1])
sage: a==b
False
```


That means that all solve will see is False.  Instead, we want something like:


```

sage: SR(a)==SR(b)
([    x   x^2]
[x + 1 x + 4]) == ([4 3]
[2 1])
```

 
(i.e., we want the == in the solve to construct an equation, which it does for symbolic objects.  One of the issues at heart here is that a symbolic object wrapping a Sage matrix is different from a Sage matrix containing symbolic objects.

So I'm going to take off beginner status for this ticket here.  It would still be nice if solve(SR(a)==SR(b)) worked in the above example.


---

Comment by jason created at 2011-04-14 03:50:19

Changing keywords from "beginner" to "".
