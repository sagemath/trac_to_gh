# Issue 9467: p-adic l-series associated to modular Jacobians

Issue created by migration from https://trac.sagemath.org/ticket/9467

Original creator: jen

Original creation time: 2010-07-09 20:15:29

Assignee: was

This is a first attempt at merging the code William and I wrote during Sage Days 22 to compute p-adic L-series associated to modular Jacobians.

Below is an example of a p-adic L-series associated to the rank 2 Jacobian of a curve (level N = 188) in 
"Empirical evidence for the Birch and Swinnerton-Dyer conjectures for modular Jacobians of genus 2 curves" (Flynn, Leprevost, Schaefer, Stein, Stoll, Wetherell).

I realize the naming isn't quite right (this is the L-series of a
curve whose Jacobian is a certain quotient of J_0(N) ...), but here's the main function:

```

sage: J = J0(188)
sage: L = J.padic_lseries(7)
sage: f = L.series(5)
```



---

Attachment


---

Attachment


---

Comment by chapoton created at 2018-08-19 16:11:51

New commits:


---

Comment by git created at 2018-08-19 16:57:46

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2018-08-20 07:32:07

Changing keywords from "" to "lseries".


---

Comment by chapoton created at 2018-08-20 07:32:23

Changing keywords from "lseries" to "L-series".


---

Comment by git created at 2018-11-28 09:55:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2019-03-09 07:32:40

Changing keywords from "L-series" to "lseries".
