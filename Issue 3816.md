# Issue 3816: [with patch; needs review] notebook -- SyntaxWarning in twist.py

Issue created by migration from https://trac.sagemath.org/ticket/3816

Original creator: was

Original creation time: 2008-08-12 13:16:44

Assignee: boothby

this was in there forever, but for some reason it causes a warning...

From Cremona:

```

I have a successful build of 3.1.alpha1.  When I make a clone, the
*first* time I run sage (by typing ./sage in SAGE_ROOT right after the
sage -clone) I get this message after the banner and before the first
prompt:

/home/john/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/server/notebook/twist.py:1762:
SyntaxWarning: name 'notebook' is used prior to global declaration
 global notebook

But if I then quit and restart, the message does not recur.

What gives?

John

```



---

Attachment


---

Comment by mabshoff created at 2008-08-13 06:38:26

Positive review. Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-13 06:39:15

Resolution: fixed


---

Comment by mabshoff created at 2008-08-13 06:39:15

Merged in Sage 3.1.alpha2
