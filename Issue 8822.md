# Issue 8822: Bug in Family constructor

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2010-04-29 12:25:31

Assignee: sage-combinat

CC:  sage-combinat

Keywords: combinat, family


```
sage: f = Family(Zmod(3), lambda i: 2*i, lazy=False)
sage: f
Lazy family (<lambda>(i))_{i in Ring of integers modulo 3}
```


Should we really just silently ignore the intent here, or should

`Family(S, f, lazy=False)` always return `Family([i for i in S], f)`

(I guess the default for lazy should then be made 'None' so that 'True',
'False' and 'None' could all have different behaviors.)



---

Comment by hivert created at 2010-05-13 22:40:29

Changing assignee from sage-combinat to hivert.


---

Comment by hivert created at 2010-05-13 22:40:29

I'm working on this one

Florent


---

Comment by mkoeppe created at 2021-02-13 20:51:01

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.
