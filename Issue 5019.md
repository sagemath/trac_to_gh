# Issue 5019: sage -gdb is broken on OSX when using branches

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-19 02:05:15

Assignee: cwitty

This is a followup to #4991: When running `sage -gdb` on OSX with branches the following failure occurs:

```
...
. done
Reading symbols for shared libraries warning: Could not find object file "/Users/wstein/sage-3.2.3/devel/sage-main/build/temp.macosx-10.3-i386-2.5/sage/ext/interactive_constructors_c.o" - no debug information available for "sage/ext/interactive_constructors_c.c".

. done
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Users/wstein/sage/local/lib/python2.5/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/Users/wstein/ipy_profile_sage.py in <module>()
     14     from sage.misc.interpreter import attached_files
     15 
---> 16     branch = sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg())
     17     if branch:
     18         print branch

/Users/wstein/sage/local/lib/python2.5/site-packages/sage/misc/misc.pyc in branch_current_hg()
   1502     i = s.rfind('->')
   1503     if i == -1:
-> 1504         raise RuntimeError, "unable to determine branch?!"
   1505     s = s[i+2:]
   1506     i = s.find('-')

RuntimeError: unable to determine branch?!
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.

sage: 
```


Cheers,

Michael


---

Comment by mmezzarobba created at 2015-04-13 14:36:06

No longer relevant?


---

Comment by mmezzarobba created at 2015-04-13 14:36:06

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-11-04 14:35:34

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-11-04 22:18:20

Resolution: fixed
