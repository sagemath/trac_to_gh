# Issue 2610: emacs -- fix typo in sagemath.org website

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-20 10:34:06

Assignee: tba


```
Hello,

I think on
http://www.sagemath.org/emacs/
a line, which connects the ".sage" file-extension with python-mode,
like

(setq auto-mode-alist (cons '("\\.sage\\'" . python-mode) auto-mode-
alist))

is missing.

With best regards,
Lars Fischer
```



---

Comment by mabshoff created at 2008-03-20 11:10:00

Done - can somebody confirm this, so it can be closed?

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-20 11:10:00

Changing assignee from tba to mabshoff.


---

Comment by mabshoff created at 2008-03-20 11:10:00

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-20 11:11:30

Fix confirmed


---

Comment by mabshoff created at 2008-03-20 11:13:12

Resolution: fixed


---

Comment by mabshoff created at 2008-03-20 11:13:12

Ok, I can close this now since it has been confirmed.

Cheers,

Michael
