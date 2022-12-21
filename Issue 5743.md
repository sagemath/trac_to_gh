# Issue 5743: Solaris 10/Sparc: Fix numerical noise issues in doctests

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-11 01:25:26

Assignee: mabshoff

There are a couple doctests on Solaris 10/Sparc that fail due to numerical noise. Fix it. 

A patch is coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-11 01:25:31

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2009-04-16 10:06:22

This patch fixes the following two doctest failures on Solaris 10/Sparc:

```
sage -t  "devel/sage/sage/modules/free_module_element.pyx"  
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/modules/free_module_element.pyx", line 505:
    sage: vector(RDF, {1:pi, 1000:e})._sage_input_(SageInputBuilder(), False)
Expected:
    {call: {atomic:vector}({atomic:RDF}, {dict: {{atomic:1}:{atomic:3.1415926535897931}, {atomic:1000}:{atomic:2.7182818284590451}}})}
Got:
    {call: {atomic:vector}({atomic:RDF}, {dict: {{atomic:1}:{atomic:3.1415926535897931}, {atomic:1000}:{atomic:2.7182818284590455}}})}
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_8
```

and

```
sage -t  "devel/sage/sage/rings/real_double.pyx"            
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/rings/real_double.pyx", line 727:
    sage: sage_input(RDF(-e), verify=True, preparse=False)
Expected:
    # Verified
    -RDF(2.7182818284590451)
Got:
    # Verified
    -RDF(2.7182818284590455)
**********************************************************************
```


Cheers,

Michael


---

Comment by craigcitro created at 2009-04-16 10:07:50

Yep, that's some numerical noise.


---

Comment by mabshoff created at 2009-04-16 10:21:25

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 10:21:25

Resolution: fixed
