# Issue 276: clisp/maxima dies with "invalid byte" on non-ASCII filename characters

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-02-22 20:06:21

Assignee: was

Keywords: clisp maxima

When clisp (and hence maxima) starts, it tries to load ~/.clisprc; this involves reading the names of all files in my home directory.  If I have no locale-related environment variables set, and I have a non-ASCII character in some filename in my home directory (in my case, an 'ñ'), then clisp prints out the following error message:

```
*** - invalid byte #xF1 in CHARSET:ASCII conversion
The following restarts are available:
ABORT          :R1      ABORT
ABORT          :R2      ABORT
Break 1 [3]>
```

(If I abort from here, then clisp/maxima continues to start up, and apparently runs correctly.)

Evidently, the clisp people don't consider this a bug; it is documented here:
http://clisp.cons.org/impnotes/faq.html#faq-enc-err

I suggest that SAGE should either set locale environment variables or use the -E flag to set encodings when it runs maxima (as suggested in the above-linked FAQ entry).  (For now, I have worked around the problem by moving this file out of my home directory.)


---

Attachment


---

Comment by was created at 2007-10-21 02:17:46

Resolution: fixed
