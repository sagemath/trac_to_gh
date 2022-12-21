# Issue 2608: Sequence(ZZ) should fail gracefully

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-03-20 05:12:50

Assignee: was

Sequence(ZZ) should fail immediately in the first place. In the session below, I entered the command, waited some time and pressed CTRL+C many times. The computation was not only interrupted, but my sage session also crashed. Output below:
 

```
sage: Sequence(ZZ)
(CTRL+C pressed repeatedly)
ERROR: Internal Python error in the inspect module.
Below is the traceback from this internal error.

Traceback (most recent call last):
  File "/home/dfdeshom/custom/sage/local/lib/python2.5/site-packages/IPython/ultraTB.py", line 491, in text
    records = _fixed_getinnerframes(etb, context,self.tb_offset)
  File "/home/dfdeshom/custom/sage/local/lib/python2.5/site-packages/IPython/ultraTB.py", line 124, in _fixed_
getinnerframes
    records  = inspect.getinnerframes(etb, context)
  File "/home/dfdeshom/custom/sage/local/lib/python2.5/inspect.py", line 877, in getinnerframes
    framelist.append((tb.tb_frame,) + getframeinfo(tb, context))
  File "/home/dfdeshom/custom/sage/local/lib/python2.5/inspect.py", line 841, in getframeinfo
    lines, lnum = findsource(frame)
  File "/home/dfdeshom/custom/sage/local/lib/python2.5/inspect.py", line 462, in findsource

[...]

  File "/home/dfdeshom/custom/sage/local/lib/python2.5/site-packages/sage/interfaces/get_sigs.py", line 9, in my_sigint
    raise KeyboardInterrupt
KeyboardInterrupt

Unfortunately, your original traceback can not be constructed.

dfdeshom`@`sage:~/custom/sage/devel/sage-2577$

```



---

Comment by jdemeyer created at 2010-09-28 21:31:05

With sage-4.6.alpha1, I cannot reproduce the crashes anymore.  Doing `Sequence(ZZ)` or `list(ZZ)` will still take forever, but I don't think this is a big problem (`ZZ` is infinite, after all).


---

Comment by jdemeyer created at 2010-09-28 21:31:05

Changing status from new to needs_review.


---

Comment by dfdeshom created at 2010-11-03 00:55:19

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-03 08:20:25

Resolution: worksforme


---

Comment by jdemeyer created at 2010-11-03 08:20:25

dfdeshom: please add your real name to [Account Names mapped to Real Names](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames).
