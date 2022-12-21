# Issue 5533: Recompiling .spyx files changes class

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2009-03-16 19:41:11

Assignee: cwitty

CC:  cwitty

Apparently, recompiling a .spyx file creates a new module and/or creates a new dummy class.  This gets in the way of pickling.  For example, start from a command prompt and follow the instructions using the attached junk7.spyx.

```
sage  # at the command prompt, start Sage
sage: load 'junk7.spyx'
sage: # make an insignificant change to junk7.spyx so it will recompile...
sage: load 'junk7.spyx'
sage: MyClass().greet()
Greetings!
sage: import pickle
sage: fi = file('junk7.pjr', 'w')
sage: pickle.dump(MyClass(), fi)
sage: fi.close()
sage: exit  # returns to the command line

sage  # now restart sage from the command line
sage: load 'junk7.spyx'
sage: import pickle
sage: fi = file('junk7.pjr', 'r')
sage: tmp = pickle.load(fi)
---------------------------------------------------------------------------
ImportError
...
ImportError: No module named _home_ryan_uva_prng_well_sage_junk7_spyx_1
```

So the error is trying to import the module.  Apparently compiling a .spyx file creates a new Python module each time?  Other than exiting Sage every time I want to recompile, I don't see a way around this problem -- or a way to fix it.


---

Comment by rhinton created at 2009-03-16 19:42:46

Defines a dummy class for pickling/unpickling test


---

Attachment
