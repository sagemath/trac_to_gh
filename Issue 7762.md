# Issue 7762: `conf.py` for Sage documentation hardcodes sagenb path

Issue created by migration from https://trac.sagemath.org/ticket/7762

Original creator: timdumol

Original creation time: 2009-12-24 17:25:05

Assignee: mvngu

jhpalmieri on sage-devel:

```
As of 4.3.rc0, it looks like sagenb is perhaps being installed in the
wrong place, resulting in failures when building the documentation
with the "-j" option (it can't find some of the relevant javascript):

copying static files... WARNING: static directory '/Applications/sage/
local/lib/python/site-packages/sagenb/data/jsmath/' does not exist

In 4.3.alpha1, sagenb was installed in SAGE_ROOT/local/lib/python/site-
packages/.

In 4.3.rc0 and 4.3.rc1, sagenb is installed in SAGE_ROOT/local/lib/
python/site-packages/sagenb-0.4.7-py2.6.egg/

[...]
```



---

Attachment

Uses `sagenb.misc.misc.DATA` instead.


---

Comment by timdumol created at 2009-12-24 17:28:06

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-12-24 18:34:01

Resolution: duplicate


---

Comment by timdumol created at 2009-12-24 18:34:29

This is a duplicate of #7755.
