# Issue 1757: implement Coppersmith's method for finding small roots of univariate polynomials modulo an integer

Issue created by migration from https://trac.sagemath.org/ticket/1757

Original creator: malb

Original creation time: 2008-01-11 18:36:46

Assignee: somebody

From the MAGMA 2.14 changelog: "Coppersmith's method for finding small roots of univariate polynomials modulo an integer has been implemented. This implementation uses the new fpLLL package of Damien Stehlé." ( http://magma.maths.usyd.edu.au/magma/htmlhelp/rel/node2.htm )


---

Comment by malb created at 2008-03-03 22:27:16

Changing priority from major to minor.


---

Comment by malb created at 2008-03-03 22:31:28

The MAGMA documentation for this function is here `SmallRoots`:

  http://magma.maths.usyd.edu.au/magma/htmlhelp/text300.htm

Coppersmith's algorithm is described and discussed in Alexander May's PhD thesis:

  http://www.informatik.tu-darmstadt.de/KP/publications/03/bp.ps

A first naive implementation would look like this:

```
def small_roots(f, X=None):
  d = f.degree()
  K = f.base_ring()
  M = K.characteristic()
  f.change_ring(ZZ)
  if X is None:
    X =  M.nth_root(d*(d+1)/2)
  A = Matrix(ZZ,d+1,d+1)
  for i in range(d):
    A[i,i] = M*X^i
  for i in range(d+1):
    A[d,i] = ZZ(f[i])*X^i
  A = A.LLL()
  x = ZZ['x'].gen(0)
  g = 0
  for i in range(d+1):
    g+= A[0,i]/X^i * x^i
  return map(lambda (x,y):(K(x),y), g.roots())
```


We can do slightly better though.


---

Comment by malb created at 2008-03-20 14:11:09

duplicate of #2424


---

Comment by malb created at 2008-03-20 14:11:09

Resolution: duplicate
