# Issue 9325: Bugs concerning coding comments and docstrings in sage-preparse

Issue created by migration from Trac.

Original creator: dpoetzsch

Original creation time: 2010-06-24 10:02:02

Assignee: ncalexan

Keywords: preparse docstring

I found (and fixed) a few Bugs in the file local/bin/sage-preparse.

These are the things I fixed:

* The module docstrings disappeared when preparsing because the
preparse_file function inserted those numeric_literals definitions before
the docstrings.

* Now also unicode-docstrings (e.g. u"""foo""") are recognized as
docstrings. Also raw docstrings may now use an upper case R as string
modifier (R"""foo""" would work now) which is allowed in Python.

* Now all coding-comments as specified by Python are found and excluded
from preparsing.

* I did not fix a bug that occurs when a statement is on the same line
where the docstring ends (e.g. """foo"""; print 2^5). It will not be
preparsed! I added a TODO-comment on the according line. 

greetings,
David Poetzsch-Heffter


---

Comment by dpoetzsch created at 2010-06-24 10:15:26

Changing assignee from ncalexan to jason.


---

Comment by dpoetzsch created at 2010-06-24 10:15:26

Changing component from sage-mode to misc.


---

Comment by dpoetzsch created at 2010-06-24 10:26:22

Bugfixes


---

Attachment


---

Comment by nthiery created at 2010-07-01 09:42:21

Thanks for creating this ticket and working on it! I was about just to create one to suggest that the encoding lines "# -*- coding: utf-8 -*-" would not be stripped away.


---

Comment by nthiery created at 2010-07-01 09:47:35

Replying to [comment:3 nthiery]:
> Thanks for creating this ticket and working on it! I was about just to create one to suggest that the encoding lines "# -*- coding: utf-8 -*-" would not be stripped away.

Oops, never mind. This line is already propagated properly. Mine had a double # at the beginning.
