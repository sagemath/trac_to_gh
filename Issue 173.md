# Issue 173: mathematica raises matrices / QQ to large powers much more quickly than SAGE

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-12-01 01:08:37

Assignee: somebody

If you make a messy 3x3 matrix over QQ and raise it to a large power
in SAGE it is WAY faster in Mathematica. 



```
sage: time m = matrix(QQ,3,range(9)); m[0,0] =20; n=m^(-1)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.05
sage: time k=n^20000
CPU times: user 0.56 s, sys: 0.00 s, total: 0.56 s
Wall time: 0.57
sage: nm = magma(n)
sage: time l=nm^20000
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.40
sage: nm = mathematica(n)
sage: time a=nm^20000
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.03
```


SAGE should do whatever mathematica is doing...


---

Comment by was created at 2006-12-01 01:08:44

Changing priority from major to minor.


---

Comment by was created at 2007-12-03 18:35:57

It turns out that this is invalid.  I was misusing Mathematica.  See
this thread

 http://groups.google.com/group/sage-devel/browse_thread/thread/27d0cde4628cac48


---

Comment by was created at 2007-12-03 18:35:57

Resolution: invalid


---

Comment by was created at 2007-12-03 19:04:42


```
"The computer allows you to make mistakes faster than any other invention, with the possible exception of handguns and tequila."
```



---

Comment by was created at 2007-12-03 19:05:12

"The computer allows you to make mistakes faster than any other invention, with the possible exception of handguns and tequila."
