# Issue 1992: Loading and attaching spyx/pyx files -- automatic compilation and nsf locking

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-31 04:28:15

Assignee: was

When

```
 sage: load filename.spyx
```

is done repeatedly on a specific single file filename.spyx, after about 3-4
tries Sage tries to delete some files.  On some NFS mounted filesystems, there
are lock files, and these can't be deleted for permissions reasons.  Instead of 
sage gracefully continuing on it fails at this point, and bombs out.  This makes
loading cython files fail henceforth, making spyx files completely useless.

The fix is probably just to put a try/except block around any code that deletes files that is related to attaching and loading [s]pyx files.





---

Comment by mabshoff created at 2008-01-31 04:31:32

This is a dupe of #1559 - so which one should we close?

Cheers,

Michael


---

Comment by was created at 2008-01-31 04:53:37

closed as a dupe


---

Comment by was created at 2008-01-31 04:53:44

Resolution: duplicate
