# Issue 1753: install_scripts() conflict with make install

Issue created by migration from https://trac.sagemath.org/ticket/1753

Original creator: pgrinber

Original creation time: 2008-01-10 22:19:51

Assignee: cwitty

When trying to run install_scripts()  (i.e. installing from an RPM), the desired installation directory is /usr/bin so that when the files are installed, they are available in the $PATH. This causes problems with the kash and M2 scripts. Since in order for the install_scripts() to detect those executables they have to be in the path (usually /usr/bin also), install_scripts() will try to overwrite those files with the script version. This is a problem. A possible improvement is to install the kash and M2 scripts as sage.kash or sage.M2 if install_scripts() detects that it will be overwriting the respective executables.


---

Comment by mabshoff created at 2008-09-15 20:56:50

Ok, this should be easy enough to fix. Axiom should probably also be installed as sage.axiom or something similar.

Cheers,

Michael


---

Comment by jdemeyer created at 2016-05-20 08:22:02

`make install` is no longer supported, see #1792.


---

Comment by jdemeyer created at 2016-05-20 08:22:02

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-05-20 08:22:07

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed
