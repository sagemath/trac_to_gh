# Issue 3656: log_repr and log on finite field with prime order fails,

Issue created by migration from Trac.

Original creator: syazdani

Original creation time: 2008-07-15 04:22:58

Assignee: tbd

The following code fails in sage,

```
F=GF(5)
r=F.multiplicative_generator()
r.log_repr() 
log(r,r)
```

The error seems to be because SAGE is treating GF(p) as integer mod ring, rather than a field.





---

Comment by syazdani created at 2008-07-15 04:27:11

Resolution: invalid


---

Comment by syazdani created at 2008-07-15 04:27:35

I was an idiot. The base was wrong.
