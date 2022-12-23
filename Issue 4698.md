# Issue 4698: [with patch, needs review] a single make_element function for pickling is hard to maintain

Issue created by migration from https://trac.sagemath.org/ticket/4698

Original creator: burcin

Original creation time: 2008-12-04 23:04:26

Assignee: burcin

CC:  robertwb was

All subclasses of `sage.structure.element.Element` end up using `sage.structure.element.make_element` for unpickling. This design is very hard to maintain, especially when trying to keep backward compatibility with older pickles. 

Python's pickling protocol via `__getstate__()` and `__setstate__()` moves the implementation of pickling/unpickling to the subclasses. [1] Attached patch changes sage.structure.element.Element to use this protocol.

[1] http://www.python.org/doc/2.5/lib/pickle-inst.html


---

Attachment

I fully doctested this on sage.math and it worked perfectly. 

I read the code and it looks good, and like a nice solution.  Bravo.


---

Comment by mabshoff created at 2008-12-07 08:07:15

Merged in Sage 3.2.2.alpha1


---

Comment by mabshoff created at 2008-12-07 08:07:15

Resolution: fixed
