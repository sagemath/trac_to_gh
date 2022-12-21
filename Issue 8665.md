# Issue 8665: __future__ imports not respected in notebook %python mode

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-04-09 09:02:07

Assignee: jason, was

CC:  chapoton


```
On Apr 8, 2010, at 2:48 PM, msafiri wrote:

Hi all,
ticket #7207 is closed. However, using python mode,

from __future__ import division
1/2

yields 0. (This is using Sage 4.3.4 on the sagenb.org server.)
```



---

Comment by kcrisman created at 2014-12-10 21:09:21

Confirmed.  See https://github.com/sagemath/sagenb/issues/300


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by chapoton created at 2020-09-03 08:59:01

Resolution: invalid
