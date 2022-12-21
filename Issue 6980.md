# Issue 6980: add _nonzero_positions_by_column to sparse integer matrices

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-09-21 22:20:34

Assignee: was

we still use the dense version:

```
sage: time matrix(ZZ,5000,sparse=True)._nonzero_positions_by_column()
CPU times: user 5.12 s, sys: 0.01 s, total: 5.14 s
Wall time: 5.19 s
[]
```



---

Attachment

After patching, we obtain what is expected:

```
sage: time matrix(ZZ,5000,sparse=True)._nonzero_positions_by_column()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
[]
```



---

Comment by mvngu created at 2009-09-25 06:32:20

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:28:46

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
