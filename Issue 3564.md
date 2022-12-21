# Issue 3564: [with patch; needs review] optimize sage startup: don't import sympy by default

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-06 19:02:13

Assignee: gfurnish

The attached patch works and speeds up the sage import from between 0.1 and 0.5 seconds, depending on caching. 

NOTE: It is necessary to fix a bug in sympy first.  


```
11:57 < wstein> The fix would be to change line 99 of printing/pretty/pretty_symbology.py to
11:57 < wstein>             try:
11:57 < wstein>                encoding = sys.stdout.encoding
11:57 < wstein>             except AttributeError: return
11:58 < wstein> Yep, that 100% fixes the problem.
11:58 < ondrej> ok, I'll commit it. thanks
11:58 < wstein> Maybe you already did that?
11:58 < wstein> It is right, I think, since you do almost the same thing 2 lines later.
```



---

Comment by was created at 2008-07-06 19:03:26

To verify that this indeed fixes the "sympy gets imported" problem, do this:

teragon-2:calculus was$ sage -startuptime |grep sympy
teragon-2:calculus was$ 

after applying the startuptime patch: #3559


---

Attachment

This bug is fixed in the new version of sympy:


```
12:01 < ondrej> now it is not
12:01 < ondrej> we fixed that in 0.5.15
12:01 < ondrej> bug I fixed important bug in our hg
12:01 < ondrej> and I am releasing the whole weekend...
12:02 < ondrej> (important sage<-> sympy bug)
12:02 < ondrej> so when I release, I'll create a spkg
```



---

Comment by certik created at 2008-07-06 19:07:55

Thanks for the bug report. This is fixed in sympy 0.5.15. Sympy 0.5.16 that is about to be released tomorrow fixes another important bug with sympy matrices in Sage, so I'll create a new spkg tomorrow, or on Tuesday the latest.


---

Comment by certik created at 2008-07-07 22:39:46

A new sympy-0.6.0.spkg together with a patch for sage was attached to #3592.


---

Comment by mabshoff created at 2008-07-16 06:07:01

The does what it advertises, "testall long" passes with the patch applied. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-16 06:07:19

Resolution: fixed


---

Comment by mabshoff created at 2008-07-16 06:07:19

Merged in Sage 3.0.6.alpha1
