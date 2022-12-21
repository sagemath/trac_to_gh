# Issue 4068: determinants for matrices over multivariate polynomial rings slow

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-09-05 17:16:22

Assignee: malb

phil <fongpwf__AT__gmail.com> wrote on [sage-devel]
> I have a matrix that is composed of multivariant polynomial
> entries.  I want to compute its determinant.  The problem is that it
> is very slow or runs out of memory.  For example,
> R.<x,y> = QQ[]
> C = random_matrix(R,10,10)
> Cdet = C.determinant()   # this line takes a long time

If you have more variables, it will run out of memory instead (on a 32
bit installation).


---

Comment by malb created at 2008-09-05 17:16:56

Here's a workaround:


```
sage: R.<x,y> = QQ[]
sage: C = random_matrix(R,8,8)
sage: %time d = C.determinant()
CPU times: user 2.64 s, sys: 0.00 s, total: 2.65 s
Wall time: 2.67 s
```



```
sage: %time d2 = R(C._singular_().det())
CPU times: user 0.04 s, sys: 0.01 s, total: 0.05 s
Wall time: 0.15 s
```



```
sage: d2 == d
True
```


So we need to call Singular instead of using the native code.


---

Attachment


---

Comment by mhansen created at 2008-09-05 19:58:41

Looks good to me.


---

Comment by mabshoff created at 2008-09-06 00:07:43

Merged in Sage 3.1.2.rc0


---

Comment by mabshoff created at 2008-09-06 00:07:43

Resolution: fixed
