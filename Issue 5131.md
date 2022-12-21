# Issue 5131: regression in free modules -- who broke my __mul__

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-29 23:05:17

Assignee: was

If A is a free module and r a ring element then r*A and A*r used to work fine. But somebody broke them.

In the good ol days:

```
wstein`@`sage:/disk/scratch/mabshoff-sage-releases/sage-0.10.0$ ./sage
[...]
sage: A = ZZ^3
sage: A
 _5 = Ambient free module of rank 3 over the principal ideal domain Integer Ring
sage: 2*A
 _6 = 
Free module of degree 3 and rank 3 over Integer Ring
Echelon basis matrix:
[2 0 0]
[0 2 0]
[0 0 2]
```


Now:

```
sage: A = ZZ^3
sage: 2*A
Traceback (most recent call last):
...
TypeError: unsupported operand parent(s) for '*': 'Integer Ring' and '<class 'sage.modules.free_module.FreeModule_ambient_pid'>'
```



---

Comment by tscrim created at 2014-07-18 02:17:16

Now also works for matrices:

```
sage: A = ZZ^3
sage: m = matrix(3, range(9))
sage: A * m
Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[1 1 1]
[0 3 6]
sage: m * A
Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[ 3  0 -3]
[ 0  1  2]
```

----
New commits:


---

Comment by tscrim created at 2014-07-18 02:17:16

Changing status from new to needs_review.


---

Comment by git created at 2014-07-20 17:00:56

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jkeitel created at 2014-07-20 17:49:24

Changing status from needs_review to positive_review.


---

Comment by jkeitel created at 2014-07-20 17:49:24

Hi Travis, the patch looks good to me.


---

Comment by vbraun created at 2014-07-21 17:38:08

Resolution: fixed
