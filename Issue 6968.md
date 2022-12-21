# Issue 6968: improve _vector_times_matrix

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-09-20 20:30:00

Assignee: was

Very small patch avoiding multiple copies


---

Attachment


---

Comment by ylchapuy created at 2009-09-20 20:33:58

for the record:

before:

```
sage: m=identity_matrix(1000,sparse=True)
sage: v=vector([1]*1000,sparse=True)
sage: time p = v*m
CPU times: user 2.26 s, sys: 0.00 s, total: 2.26 s
Wall time: 2.26 s 
```


after:

```
sage: m=identity_matrix(1000,sparse=True)
sage: v=vector([1]*1000,sparse=True) 
sage: time p = v*m 
CPU times: user 0.20 s, sys: 0.00 s, total: 0.20 s
Wall time: 0.21 s
```



---

Comment by was created at 2009-09-20 21:55:46

Nice!!


---

Comment by mvngu created at 2009-09-24 16:45:51

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:24:47

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
