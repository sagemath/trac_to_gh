# Issue 777: sign function

Issue created by migration from Trac.

Original creator: kedlaya

Original creation time: 2007-10-02 00:40:40

Assignee: somebody

CC:  mhansen

Keywords: sign

Should the following function exist globally?

```
def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0
```

I'm not sure if this is identical to

```
def sign(x):
    return x.__cmp__(0)
```

I'm also ambivalent as to whether this function is called "sign", "signum", or "sgn".


---

Comment by kcrisman created at 2009-08-26 15:16:31

To release manager: note that this should be closed - see comment in #6803.


---

Comment by kcrisman created at 2009-11-10 15:31:13

To clarify: we already have:

```
sage: sgn(1)
1
sage: sgn(-4)
-1
```

so this ticket should be closed, presumably as a duplicate.


---

Comment by mhansen created at 2009-11-10 16:17:40

Resolution: invalid
