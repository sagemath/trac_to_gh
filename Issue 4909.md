# Issue 4909: convert sage.dsage.* docstrings to Sphinx

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-01 22:50:29

Assignee: tba




---

Attachment


---

Attachment


---

Comment by hivert created at 2009-02-24 17:42:44

A little problem:

```
Note that configuration files will be stored in the  
    directory \code{\$DOT\_SAGE/dsage}.
```

Is replaced now by

```
Note that configuration files will be stored in the directory 
``$DOT 
Sage/dsage``. 
}}} 
the "_" must be kept. 

Otherwise this is correct. 

Cheers,

Florent


---

Comment by mabshoff created at 2009-02-24 18:33:39

Merged in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 18:33:39

Resolution: fixed
