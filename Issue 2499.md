# Issue 2499: cython -- issues with cython-ing on the fly (fix one instance of lame code; also fix a bug)

Issue created by migration from https://trac.sagemath.org/ticket/2499

Original creator: was

Original creation time: 2008-03-12 16:25:55

Assignee: was

The attached patch (1) cleans up some ugly code, and (2) Fixes a bug that occurs on some NFS mounted filesystems.  

The (2) uses except: since I don't know the exact exception that occurs.  This could be fixed later.


---

Attachment


---

Comment by wjp created at 2008-03-14 16:57:10

The exception that occurs when trying to unlink .nfsXXX files is an OSError. I'm attaching a second (incremental) patch to change `except:` into `except OSError:` (and made sure it still fixes the problem).

Positive review, in any case.


---

Attachment


---

Comment by mabshoff created at 2008-03-14 17:12:01

wjp's incremental patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-14 17:13:59

Resolution: fixed


---

Comment by mabshoff created at 2008-03-14 17:13:59

Merged in Sage 2.10.4.alpha0
