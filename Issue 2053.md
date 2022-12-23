# Issue 2053: creating symbolic matrices is insanely slow

Issue created by migration from https://trac.sagemath.org/ticket/2053

Original creator: was

Original creation time: 2008-02-05 14:28:48

Assignee: was

On the fastest modern hardware we have:


```
sage: time m = matrix(SR, 20, [1..20^2])
CPU times: user 0.34 s, sys: 0.12 s, total: 0.45 s
Wall time: 1.05
```

which is frickin' slow.  And the time isn't just in coercion, since

```
sage: time v = [SR(a) for a in [1..20^2]]
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01
```



---

Comment by was created at 2008-02-05 14:47:30

The attached patch fixes this problem.  Now the following works and speeds
up the above benchmark by a huge amount:

```
sage: time m = matrix(SR, 20, [1..20^2])
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.07
sage: time m = matrix(SR, 50, [1..50^2])
CPU times: user 0.07 s, sys: 0.02 s, total: 0.09 s
Wall time: 0.46
sage: time m = matrix(SR, 100, [1..100^2])
CPU times: user 0.26 s, sys: 0.02 s, total: 0.27 s
Wall time: 0.49
```


Even a 500x500 matrix is possible, which used to be out
of the question. 

```
sage: time m = matrix(SR, 500, [1..500^2])
CPU times: user 6.79 s, sys: 0.39 s, total: 7.17 s
Wall time: 13.32
```



---

Attachment


---

Comment by mhansen created at 2008-02-06 04:08:33

I cannot apply this due to a failed hunk with the docstring in set_from_list.


---

Attachment

apply this *INSTEAD*!


---

Comment by mhansen created at 2008-02-07 07:59:47

Looks good to me.


---

Comment by mabshoff created at 2008-02-07 10:10:31

Resolution: fixed


---

Comment by mabshoff created at 2008-02-07 10:10:31

Merged the second patch only in Sage 2.10.2.alpha2
