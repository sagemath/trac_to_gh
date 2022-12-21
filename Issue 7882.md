# Issue 7882: Macaulay2 interface breaks on examples

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2010-01-09 20:02:02

Assignee: was

Present version of Macaulay2 interface breaks on


```
macaulay2("help matrix")
```


although


```
macaulay2.help("matrix")
```


does work fine.

The problem is that pexpect detects input prompts inside of examples. The patch changes the input prompt to get matches only in the beginning of lines.

The interface still breaks if you try to print input prompts at the beginning of the line, but that is probably a rare situation...


---

Attachment


---

Comment by novoselt created at 2010-01-09 20:02:48

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-01-11 20:58:42

Resolution: duplicate


---

Comment by novoselt created at 2010-01-11 20:58:42

Ticket #7897 fixes this in a better way.
