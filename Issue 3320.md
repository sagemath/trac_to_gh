# Issue 3320: Gap <-> Sage interface for Dense Matrices over GF(2)

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-05-28 13:26:33

Assignee: was

Keywords: gap, linear algebra

This should be much faster:

```
sage: A = random_matrix(GF(2),200,200)
sage: time Am = magma(A)
CPU times: user 0.03 s, sys: 0.01 s, total: 0.04 s
Wall time: 0.50
sage: time Ag = gap(A) #<-------------
CPU times: user 10.35 s, sys: 0.63 s, total: 10.98 s
Wall time: 11.76
```



---

Comment by tscrim created at 2013-02-22 23:30:14

This seems to have been fixed at some point:

```
sage: A = random_matrix(GF(2), 200, 200)
sage: %time Ag = gap(A)
CPU times: user 0.38 s, sys: 0.12 s, total: 0.50 s
Wall time: 1.26 s
sage: %time Ag = gap(A)
CPU times: user 0.37 s, sys: 0.02 s, total: 0.40 s
Wall time: 0.58 s
sage: %time Ag = gap(A)
CPU times: user 0.39 s, sys: 0.02 s, total: 0.41 s
Wall time: 0.62 s
```

I can't do a comparison on my system with magma since it refuses to start for me (I'm running `5.7.beta3`).


---

Comment by tscrim created at 2013-02-22 23:30:14

Changing status from new to needs_review.


---

Comment by ncohen created at 2013-03-24 20:38:01

Same here !

Nathann


---

Comment by ncohen created at 2013-03-24 20:38:01

Changing status from needs_review to positive_review.


---

Comment by malb created at 2013-03-24 23:03:06

This should be duplicate/wontfix not postive_review, there's no patch.


---

Comment by ncohen created at 2013-03-25 09:15:55

> This should be duplicate/wontfix not postive_review, there's no patch.

Oh ? But I thought we had to set the to positive_review so that Jeroen seens them and closes them ?... `O_o`

Nathann


---

Comment by tscrim created at 2013-03-25 13:26:13

From my understanding, we need to do both since we have to verify that it is a duplicate (or wontfix/etc.).


---

Comment by jdemeyer created at 2013-03-29 18:58:36

Resolution: worksforme
