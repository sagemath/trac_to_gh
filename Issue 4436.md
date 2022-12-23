# Issue 4436: Sage 3.2.a2: numerical noise in sage/calculus/calculus.py

Issue created by migration from https://trac.sagemath.org/ticket/4436

Original creator: mabshoff

Original creation time: 2008-11-04 13:52:39

Assignee: mabshoff

On an Itanium:

```
sage -t  devel/sage/sage/calculus/calculus.py              
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-iras/tmp/calculus.py", line 7533:
    sage: float(sinh(pi))
Expected:
    11.548739357257748
Got:
    11.548739357257746
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-iras/tmp/calculus.py", line 7642:
    sage: float(csch(pi))
Expected:
    0.086589537530046945
Got:
    0.086589537530046959
**********************************************************************
```

On an x86:

```
sage -t  devel/sage/sage/calculus/calculus.py               
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/calculus.py", line 120:
    sage: float(f(pi))
Expected:
    6.1232339957367663e-16
Got:
    6.1230317691118863e-16
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/calculus.py", line 7533:
    sage: float(sinh(pi))
Expected:
    11.548739357257748
Got:
    11.548739357257746
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/calculus.py", line 7642:
    sage: float(csch(pi))
Expected:
    0.086589537530046945
Got:
    0.086589537530046959
**********************************************************************
```



---

Comment by mabshoff created at 2008-11-04 13:53:09

The is also an issue in a G4:

```
    sage -t  devel/sage/sage/calculus/calculus.py 
         this has been reported, but I just noticed that there is   
"significant bit noise", not insignificant bit noise: 
            Expected: 
                6.1232339957367663e-16 
            Got: 
                6.1230317691118863e-16 
```



---

Comment by mabshoff created at 2008-11-04 13:53:09

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-11-05 22:08:26

Looks fine.


---

Comment by mabshoff created at 2008-11-05 23:12:41

Resolution: fixed


---

Comment by mabshoff created at 2008-11-05 23:12:41

Merged in Sage 3.2.alpha3
