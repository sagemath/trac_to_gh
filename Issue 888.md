# Issue 888: 2.8.7-alpha0: doctest failure in dsage/tests/testdoc.py (requires previous dsage setup)

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-13 20:36:32

Assignee: was


```
File "testdoc.py", line 12:
    age: d = DSage(port=port, ssl=False)
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/pre-sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        d = DSage(port=port, ssl=False)###line 12:
    age: d = DSage(port=port, ssl=False)
      File "/home/cwitty/pre-sage/local/lib/python/site-packages/sage/dsage/all.py", line 52, in DSage
        ssl=ssl)
      File "/home/cwitty/pre-sage/local/lib/python/site-packages/sage/dsage/interface/dsage_interface.py", line 392, in __init__
        self.pubkey_str = keys.getPublicKeyString(filename=self.pubkey_file)
      File "/home/cwitty/pre-sage/local/lib/python2.5/site-packages/twisted/conch/ssh/keys.py", line 48, in getPublicKeyString
        lines = open(filename).readlines()
    IOError: [Errno 2] No such file or directory: '/home/cwitty/.sage/dsage/dsage_key.pub'
```


(The last line is the most interesting.)


---

Comment by was created at 2007-10-14 05:12:57

Changing priority from blocker to major.


---

Comment by was created at 2007-10-14 05:12:57

I've disabled dsage doctesting for that file for sage-2.8.7, and moved this to 2.8.8.


---

Comment by yi created at 2007-10-19 06:41:07

I reassigned this bug to me so I don't lose track of it.  I will fix this one ASAP.  
Please reassign DSAGE related bugs to me in the future so they will show up under "My Active Tickets" for me.


---

Comment by yi created at 2007-10-19 06:41:07

Changing assignee from was to yi.


---

Comment by was created at 2007-11-07 05:24:35

I've turned off doctesting of this file until Yi's resolve the issue.

William


---

Comment by was created at 2007-11-07 05:30:37

WAIT -- requiring that dsage.setup() has been run is *not* an unreasonable requirement
before doctesting.    How else can we expect to truly doctest that dsage work and have
it eventually appear in examples all over the place, etc.?

To resolve this ticket, we just need to require dsage setup has been run, say at the
beginning of doing "make test".


---

Comment by was created at 2007-11-07 05:32:45

By the way, I think dsage.setup() should either fail completely or print a huge warning if the openssl Linux package isn't installed, since then it takes *minutes* to generate a key (using gnutls).  It might be that the new gpl v3 only gnutls fixes this crap.  But we have to wait for singular to update their license first to find out.


---

Comment by was created at 2007-11-07 05:37:08

Just for clarity -- I *have* turned doctesting this file off in this sage release.
But I think the right solution is to require dsage.setup(), and to make it clear
to the user how to do that...


---

Comment by mabshoff created at 2007-12-29 17:40:24

Since we will update to GNUTLS 2.2.0 (see #1622) soon we should revisit this issue.

Cheers,

Michael


---

Comment by yi created at 2007-12-30 00:06:45

Ok, it's easy enough to check that dsage.setup() has been run (i.e. check that DOT_SAGE/dsage exists).  Where should this check go?


---

Comment by mabshoff created at 2008-03-21 23:39:49

According to yi the issue has been fixed:

```
[00:09] <mabshoff> yi: what is the status of #888 - is that fixed by any chance?
[00:09] <yi> mabshoff: yes, please close it
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-03-21 23:39:49

Resolution: fixed
