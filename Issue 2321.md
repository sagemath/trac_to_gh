# Issue 2321: remove dsage_server.py

Issue created by migration from https://trac.sagemath.org/ticket/2321

Original creator: yi

Original creation time: 2008-02-26 17:47:20

Assignee: was

dsage switched from using dsage_server.py to using a .tac located in .sage/dsage. When we roll out the next version of sage (2.10.3) we need to remove SAGE_ROOT/local/bin/dsage_server.py.


---

Comment by mabshoff created at 2008-02-26 17:58:59

Yi: Does this depend on any patches still getting merged for 2.10.3 from your end or can I nuke the file now? A patch for this is obviously trivial.

Cheers,

Michael


---

Comment by yi created at 2008-02-26 18:09:38

Yes, we should not nuke dsage_server.py until we've successfully merged in the huge dsage changes for 2.10.3.


---

Comment by mabshoff created at 2008-04-14 00:04:25

The file has been removed, probably in 2.11. Ergo it is fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-14 00:04:25

Resolution: fixed
