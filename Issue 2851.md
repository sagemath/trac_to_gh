# Issue 2851: clean binary install of sage followed by "sage -br" is broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-07 22:36:34

Assignee: mabshoff

Get any binary of sage, type "sage -br", and it is broken.
The workaround is to touch any pyx file.  This should have been fixed but hasn't, and is a _major_ problem.  This *must* be fixed for 3.0. 


---

Comment by mabshoff created at 2008-04-07 22:52:54

This is caused by the sage directory is symlink fix from a while back. We need to invalidate the cache when files are moved.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-04-15 01:00:18

Patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-15 01:00:32

Merged in Sage 3.0.alpha5


---

Comment by mabshoff created at 2008-04-15 01:00:32

Resolution: fixed


---

Comment by yi created at 2008-04-15 16:53:24

Resolution changed from fixed to 


---

Comment by yi created at 2008-04-15 16:53:24

This still doesn't seem to be fixed. I just untared the sage-3.0.alpha5 binary from mabshoff's home directory and did a ./sage -br and got the following:

...
copying sage/dsage/dist_functions/tests/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/dist_functions/tests
creating build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/countrefs.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/misc.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/constants.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/hostinfo.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/config.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/nodoctest.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
creating build/lib.linux-x86_64-2.5/sage/dsage/misc/tests
copying sage/dsage/misc/tests/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc/tests
creating build/lib.linux-x86_64-2.5/sage/dsage/web
copying sage/dsage/web/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/web
copying sage/dsage/web/web_server.py -> build/lib.linux-x86_64-2.5/sage/dsage/web
creating build/lib.linux-x86_64-2.5/sage/dsage/scripts
copying sage/dsage/scripts/dsage_worker.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts
copying sage/dsage/scripts/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts
copying sage/dsage/scripts/dsage_setup.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts
copying sage/dsage/scripts/nodoctest.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts
running build_ext
building 'sage.modules.free_module_element' extension
error: unknown file type '.pyx' (from 'sage/modules/free_module_element.pyx')
sage: There was an error installing modified sage library code.


---

Comment by yi created at 2008-04-15 16:53:24

Changing status from closed to reopened.


---

Attachment

new patch (we want both) -- this to the SCRIPTS repo.


---

Comment by mabshoff created at 2008-04-15 18:20:59

scripts-2851.patch fixes the problem and this time I actually did test it :). Shame on me of rubber stamping this the first time around :|

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-15 18:21:14

Resolution: fixed


---

Comment by mabshoff created at 2008-04-15 18:21:14

Merged scripts-2851.patch in Sage 3.0.alpha6
