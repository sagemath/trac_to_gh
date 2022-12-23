# Issue 4789: numerically stable computation of nullspace of RDF/CDF matrices

Issue created by migration from https://trac.sagemath.org/ticket/4789

Original creator: jason

Original creation time: 2008-12-14 01:57:58

Assignee: tbd

CC:  cpernet slelievre

I think this message might be useful:

http://projects.scipy.org/pipermail/scipy-user/2008-December/019064.html




---

Comment by jason created at 2008-12-14 01:58:08

Changing component from algebra to linear algebra.


---

Comment by jason created at 2008-12-14 01:58:08

Changing assignee from tbd to jason.


---

Comment by jason created at 2008-12-14 01:58:08

Changing status from new to assigned.


---

Comment by was created at 2009-12-11 23:36:53

Example:

```
sage: a = matrix(RDF,4,[1..16])*1.293949599304953485; a
[ 1.2939495993 2.58789919861 3.88184879791 5.17579839722]
[6.46974799652 7.76369759583 9.05764719513 10.3515967944]
[11.6455463937  12.939495993 14.2334455924 15.5273951917]
[ 16.821344791 18.1152943903 19.4092439896 20.7031935889]
sage: a.kernel()
Vector space of degree 4 and dimension 0 over Real Double Field
Basis matrix:
[]
```

Define this from the email linked to above:

```
import scipy
import scipy.linalg

def null(A, eps=1e-15):
    """
    computes the null space of the real matrix A
    """
    n, m = scipy.shape(A)
    if n > m :
        return scipy.transpose(null(scipy.transpose(A), eps))
        return null(scipy.transpose(A), eps)
    u, s, vh = scipy.linalg.svd(A)
    s=scipy.append(s,scipy.zeros(m))[0:m]
    null_mask = (s <= eps)
    null_space = scipy.compress(null_mask, vh, axis=0)
    return scipy.transpose(null_space)
```


Then:


```
sage: null(a.numpy(),eps=1e-13)
array([[-0.29797676,  0.45957573],
       [ 0.73984987, -0.39066887],
       [-0.58576946, -0.59738944],
       [ 0.14389635,  0.52848258]])
```



---

Comment by embray created at 2019-06-14 14:54:19

As the Sage-8.8 release milestone is pending, we should delete the sage-8.8 milestone for tickets that are not actively being worked on or that still require significant work to move forward.  If you feel that this ticket should be included in the next Sage release at the soonest please set its milestone to the next release milestone (sage-8.9).
