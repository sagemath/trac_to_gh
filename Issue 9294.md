# Issue 9294: wrong usage of except

Issue created by migration from Trac.

Original creator: hemmecke

Original creation time: 2010-06-21 09:36:28

Assignee: jason, was

CC:  hemmecke

sagenb-0.8.p2/src/sagenb/sagenb/notebook/js.py

says

try:
    from sage.misc.misc import SAGE_ROOT
    from pkg_resources import Requirement, working_set
    sagenb_path = working_set.find(Requirement.parse('sagenb')).location
    debug_mode = SAGE_ROOT not in os.path.realpath(sagenb_path)
except AttributeError, ImportError:
    debug_mode = False

But according to what I cite below, it should rather be

except (AttributeError, ImportError):

http://docs.python.org/tutorial/errors.html



---

Attachment


---

Comment by hemmecke created at 2010-06-21 09:38:41

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-07-05 10:06:07

Nice catch! Positive review.


---

Comment by timdumol created at 2010-07-05 10:06:07

Changing status from needs_review to positive_review.


---

Comment by hemmecke created at 2010-07-05 11:05:22

See also

http://groups.google.com/group/sage-notebook/msg/e74a7366f9f50f3c

The bug seems to be fixed already.


---

Comment by timdumol created at 2010-07-05 11:12:23

Didn't seem to be the case when I applied the patch. The boxen.math url is just giving me a 500 error.


---

Comment by timdumol created at 2010-07-11 05:57:35

Resolution: fixed
