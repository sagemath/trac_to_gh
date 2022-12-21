# Issue 362: str --> basestring

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-05-10 16:58:33

Assignee: was

Type this

```
  sage: search_src(", str)")
```

In most cases change isinstance(..., str) to isinstance(..., basestring),
since unicode is getting more and more standard, and things break otherwise. 



---

Comment by was created at 2007-05-31 15:10:41

Resolution: fixed
