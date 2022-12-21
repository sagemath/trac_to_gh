# Issue 3731: [with patch, needs review] missing some derivatives in wester

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-07-27 15:32:24

Assignee: gfurnish

Keywords: wester, calculus

There is an example in sage.calculus.wester starting like this:

```
sage: # (YES) Expand (1+x)^20, take derivative and factorize. 
```

The ensuing calculation involves no derivatives, just expanding and factoring (1+x)^20.

The patch adds in some derivative calculations.




---

Attachment


---

Attachment


---

Comment by jhpalmieri created at 2008-07-29 20:33:03

I'm not sure why there are two patches here; when submitting the second one, I must have forgotten to check the box about replacing patches with the same name.  Ignore the first patch.


---

Comment by ncalexan created at 2008-08-11 06:12:47

Fine by me.


---

Comment by mabshoff created at 2008-08-11 07:42:06

Merged 3731.2.patch in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-11 07:42:06

Resolution: fixed
