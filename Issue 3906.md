# Issue 3906: symbolic plotting bug

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2008-08-20 01:16:20

Assignee: gfurnish

No response on sage-support, so I deem this a bug, not a feature:


```
sage: plot(sin,0,pi)
<plots fine>
sage: plot(2*sin,0,pi)
<boom>

Although I suppose we should always include variables -

sage: plot(2*sin(x),0,pi)
<plots fine>

- for consistency's (and ease of use's) sake both of the above should
work. 
```



---

Comment by rlm created at 2008-09-05 19:41:46

Resolution: duplicate


---

Attachment

This patch is found also at #3907.
