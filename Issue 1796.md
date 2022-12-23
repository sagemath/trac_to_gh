# Issue 1796: initial entry of Admin password

Issue created by migration from https://trac.sagemath.org/ticket/1796

Original creator: pgrinber

Original creation time: 2008-01-16 21:45:07

Assignee: mabshoff

the very first time a user runs sage, they are asked for the Admin password. It would be nice is there was a programmatic approach to setting that password from the command line. This would greatly simplify the installation of SAGE from an RPM (or a DEB) package.


---

Comment by robertwb created at 2008-01-17 00:25:18

I'm not sure an admin password ever needs to even be set now. Having a default admin password is certainly a security risk in some cases.


---

Comment by @Shlokatadistance created at 2020-03-03 15:12:53

It would be nice if there was some basic feature , such as the one that allows to access administrator rights. The way the installation from command line works can be not very intuitive for a basic user, so I think if not a default admin password, a better mechanism, atleast through sage application can be considered


---

Comment by mkoeppe created at 2021-10-10 20:33:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2021-10-10 20:33:35

outdated, should close


---

Comment by mkoeppe created at 2021-10-10 20:33:35

Changing component from distribution to notebook.


---

Comment by chapoton created at 2021-10-11 07:02:20

Resolution: invalid
