# Issue 3698: [with patch; needs review] add multinomial_coefficients and binomial_coefficients to sage.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-21 21:28:22

Assignee: somebody

Pearu Peterson (sympycore guy) wrote some really fast pure python code for computing multinomial coefficients, e.g.,

```
14:20 < wstein> sage: R.<x,y,z> = QQ[]
14:20 < wstein> sage: timeit('(x+y+z)^50')
14:20 < wstein> 25 loops, best of 3: 20.8 ms per loop
14:20 < wstein> sage: timeit('w = multinomial_coefficients(3r,50r)')
14:20 < wstein> 25 loops, best of 3: 10.3 ms per loop
```




---

Attachment


---

Comment by certik created at 2008-07-21 21:32:15

+1 from me, nice docstrings and a simple test for each method.


---

Attachment


---

Comment by was created at 2008-07-21 22:00:03


```
14:56 < wstein> pearu -- ar eyou giving 3698 a positive review?
14:57 < pearu> wstein, yes, it looks good, I presume you have tested that the code works:)
14:57 < wstein> yes
```



---

Comment by mabshoff created at 2008-07-31 00:04:12

Merged both patches in Sage 3.1.alpha0


---

Comment by mabshoff created at 2008-07-31 00:04:12

Resolution: fixed
