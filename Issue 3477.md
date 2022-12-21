# Issue 3477: clisp spkg-install has bad hard-coded error message

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-06-19 22:16:39

Assignee: mabshoff

The following code from the clisp spkg-install is confusing:

```
    echo "If you already have clisp, you can type touch spkg/installed/clisp-2.38"
    echo "(or whatever the current version is) from SAGE_ROOT, and continue the"
    echo "install.  This tells SAGE that you already have clisp-2.38 installed."
```

It should either use the current version, or not give a version at all.


---

Comment by mabshoff created at 2008-06-27 04:11:15

Changing priority from major to critical.


---

Comment by was created at 2008-07-07 21:58:29

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 22:04:49

Merged in Sage 3.0.4.rc0
