# Issue 3854: interact needs to use "notruncate"

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-08-14 18:32:40

Assignee: itolkov

Too many controls results in output truncated errors, but it's the length of the generated html that's tripping the warning... this should be trivial, just add "<!--notruncate-->" to the generated html.


---

Attachment


---

Comment by malb created at 2008-08-23 23:24:45

looks good, and from what I can see it does what it is supposed to do. I suppose, that it would be kinda hard to write a doctest for it.


---

Comment by rlm created at 2008-08-23 23:29:09

Doctesting could be easy: simply render the html, cut off the initial <html> and ending </html>, and put "...notruncate..." as the output...


---

Comment by malb created at 2008-08-24 11:11:02

Sure, but it wouldn't test the feature that is in discussion, i.e. that notruncate works as expected.


---

Comment by mabshoff created at 2008-08-25 02:33:15

As is the patch does not apply:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/devel/sage$ patch -p1 --dry-run < trac_3854_sage.patch 
patching file sage/server/notebook/interact.py
Hunk #1 FAILED at 1397.
1 out of 1 hunk FAILED -- saving rejects to file sage/server/notebook/interact.py.rej
```

It should be trivial to rebase.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-08-27 00:38:44

The new patch should apply.


---

Comment by mabshoff created at 2008-08-27 00:48:22

Merged in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-27 00:48:22

Resolution: fixed


---

Attachment

Trivial patch to fix two doctest failures


---

Comment by mabshoff created at 2008-08-29 00:41:28

For the future: please make dependencies between tickets clear. This ticket should have been applied after #3823. We ended up applying them in reverse order and had to rebase them each because the order was inverse.

Please also name the patches properly, i.e. trac_XXXX_description is that is expected.

Cheers,

Michael


---

Comment by malb created at 2008-08-29 10:57:43

Replying to [comment:8 mabshoff]:
> Please also name the patches properly, i.e. trac_XXXX_description is that is expected.

Hi there, did we definitely agree on this? I hardly use it and feel stupid if I've missed the point where I was supposed to switch.
