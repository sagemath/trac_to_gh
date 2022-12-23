# Issue 3275: [with patch, needs review] Make SL2Z distinct

Issue created by migration from https://trac.sagemath.org/ticket/3275

Original creator: craigcitro

Original creation time: 2008-05-23 07:58:31

Assignee: craigcitro

This patch changes `SL2Z` to be a distinct object, as opposed to a class. The following error was brought up on `sage-support`:


```
sage: S = SL2Z()([0,-1,1,0])
sage: T = SL2Z()([1,1,0,1])
sage: S*T
...
<type 'exceptions.RuntimeError'>: There is a bug in the coercion code in SAGE.
```


The issue (as the poster pointed out) is that the parents of S and T are distinct copies of `SL2Z`, when they don't need to be. Indeed, I don't see any difference between this and other distinct rings in Sage (such as `ZZ`, `QQ`, etc), so I've made it distinct.

Now the above becomes:

```
sage: S = SL2Z.([0,-1,1,0])
sage: T = SL2Z.([1,1,0,1])
sage: S*T
[ 0 -1]
[ 1  1]
```





---

Attachment


---

Comment by rlm created at 2008-05-23 08:01:18

looks good to me, but i haven't tried applying the patch or testing...


---

Comment by mabshoff created at 2008-05-23 08:20:41

Resolution: fixed


---

Comment by mabshoff created at 2008-05-23 08:20:41

Merged in Sage 3.0.2.rc0. Testall long passes.
