# Issue 7081: sage -c "..." runs from the local/bin/ directory.  ugh

Issue created by migration from https://trac.sagemath.org/ticket/7081

Original creator: was

Original creation time: 2009-09-30 09:10:31

Assignee: cwitty

This is not good:


```
flat:sagenb wstein$ pwd
/Users/wstein/sage/nb/sagenb
flat:sagenb wstein$ sage -c "print os.path.abspath('.')"
/Users/wstein/sage/build/64bit/sage/local/bin
```


It should be when one runs "sage -c" that it runs in the *current* directory.  The actual behavior is very confusing.


---

Attachment

Apply to scripts repo.


---

Comment by timdumol created at 2009-09-30 09:17:20

Editing $SAGE_LOCAL/bin/sage-eval to os.chdir(os.getenv('CUR')) before evalutation fixes the problem.


---

Comment by mhansen created at 2009-10-15 08:57:16

Resolution: fixed
