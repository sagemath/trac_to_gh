# Issue 2790: very annoying output of new "sage -tp"

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-03 04:19:57

Assignee: failure

The new sage -tp has output like this:

```

The following tests failed:

	sage -t  devel/sage-modabvar/sage/modular/modform/space.py: 8 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/modform/eisenstein_submodule.py: 1 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/modform/element.py: 1 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/abvar/morphism.py: 8 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/abvar/homspace.py: 8 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1586.7 seconds
teragon:sage was$ 
```


This is very annoying because I typically *paste* in the output in order to rerun broken doctests.

Easy fix insert a #, i.e., change : x doctests failed to # : x doctests failed.


---

Comment by mabshoff created at 2008-04-03 14:52:04

Patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-03 14:52:04

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-03 14:52:04

Changing assignee from failure to mabshoff.


---

Attachment


---

Comment by dfdeshom created at 2008-04-03 15:29:38

Patch looks good.


---

Comment by mabshoff created at 2008-04-03 15:35:37

Resolution: fixed


---

Comment by mabshoff created at 2008-04-03 15:35:37

Merged in Sage 3.0.alpha1
