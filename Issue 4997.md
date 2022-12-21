# Issue 4997: OSX64/Cygwin: fix memory.so import issue during doctesting

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-17 15:41:29

Assignee: mabshoff

When doctesting a 64 bit OSX build of Sage we have these failures for every doctest:

```
sage -t  "devel/sage/sage/rings/complex_interval_field.py"  
Traceback (most recent call last):
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/tmp/complex_interval_field.py", line 2, in <module>
    from sage.all_cmdline import *; 
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/all.py", line 56, in <module>
    from sage.rings.memory import pmem_malloc
ImportError: dlopen(/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/rings/memory.so, 2): Symbol not found: _rand_n
  Referenced from: /Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/rings/memory.so
  Expected in: dynamic lookup
```

The fix is to link the first library to be imported against libcsage:

```
--- a/module_list.py    Mon Jan 05 23:03:45 2009 -0800
+++ b/module_list.py    Tue Jan 06 17:13:03 2009 -0800
`@``@` -854,7 +854,7 `@``@`
 
     Extension('sage.rings.memory',
               sources = ['sage/rings/memory.pyx'],
-              libraries=['gmp','stdc++']),
+              libraries=['csage','ntl','gmp','stdc++']),
 
     Extension('sage.rings.morphism',
               sources = ['sage/rings/morphism.pyx']),
```

This fix is also needed on Cygwin.

A proper patch is coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-17 15:41:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-06 23:22:39

This is not needed, I am not sure what happened. Either way: invalid.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-06 23:22:39

Resolution: invalid
