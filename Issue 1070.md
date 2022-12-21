# Issue 1070: the build system should rebuild Cython modules if the static libraries they depend on change

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-11-02 21:35:57

Assignee: cwitty

CC:  craigcitro

For instance, if local/lib/libmpfi.a changes, then sage/rings/real_mpfi.pyx should be rebuilt.  

Most of the information to do this is in setup.py; the missing piece is knowing which libraries are static-only, which can presumably be determined by looking in local/lib/ for libraries with ".a" files and without corresponding ".so" files.


---

Comment by mabshoff created at 2008-12-17 14:28:44

This has been fixed during Sage 3.2 or so with the new build system. For example the following change makes the ecm extension depend on libecm.a:

```
--- a/module_list.py    Tue Dec 16 16:52:43 2008 +0000
+++ b/module_list.py    Wed Dec 17 06:23:47 2008 -0800
`@``@` -339,7 +339,8 `@``@`
     
     Extension('sage.libs.libecm',
               sources = ['sage/libs/libecm.pyx'],
-              libraries = ['ecm', 'gmp']),
+              libraries = ['ecm', 'gmp'],
+              depends = [SAGE_ROOT + "/local/lib/libecm.a"]),
      
     Extension('sage.libs.mwrank.mwrank',
               sources = ["sage/libs/mwrank/mwrank.pyx",
```

Touching libecm.a now leads to a rebuild of the ecm extension.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-17 14:28:44

Resolution: fixed
