# Issue 2267: [with patch, needs review] Sage 2.10.2: fix latex errors when generating the documentation

Issue created by migration from https://trac.sagemath.org/ticket/2267

Original creator: mabshoff

Original creation time: 2008-02-22 21:54:45

Assignee: was

As a last step after merging all the patches we need to regenerate the documentation. That does involve fixing a bunch of LaTeX errors from the docstrings.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-22 21:55:22

Changing component from algebraic geometry to documentation.


---

Comment by mabshoff created at 2008-02-22 21:55:22

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-22 21:55:22

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-02-22 21:55:22

Changing assignee from was to mabshoff.


---

Attachment


---

Comment by malb created at 2008-02-22 22:29:55

`$hnf(transpose(A))^(-1)*A$` that looks wrong and probably should be: `$hnf(transpose(A))^{-1} * A$`


---

Comment by mabshoff created at 2008-02-22 23:28:23

Replying to [comment:2 malb]:
> `$hnf(transpose(A))^(-1)*A$` that looks wrong and probably should be: `$hnf(transpose(A))^{-1} * A$`

Are you sure that makes a difference? I think in math mode all spaces will be eaten by the TeX parser anyway.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-22 23:29:59

Merged in Sage 2.10.2.final


---

Comment by mabshoff created at 2008-02-22 23:29:59

Resolution: fixed


---

Comment by malb created at 2008-02-22 23:40:14

Yes my comment makes a difference because `^{-1`} is different from `^(-1)` :-)


---

Comment by mabshoff created at 2008-02-22 23:44:33

Replying to [comment:6 malb]:
> Yes my comment makes a difference because `^{-1`} is different from `^(-1)` :-) 

D'oh - I will fix it in the sources. Maybe I should get new glasses and sleep more. Thanks malb.

Cheers,

Michael
