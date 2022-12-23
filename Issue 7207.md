# Issue 7207: from __future__ import <anything> results in a Syntax Error

Issue created by migration from https://trac.sagemath.org/ticket/7207

Original creator: timdumol

Original creation time: 2009-10-14 11:42:07

Assignee: boothby

CC:  mpatel was

`from __future__ import *` statements must be the first statements in a file. However, the old Sage Notebook inserts synchronization code before the file, and the new SageNB inserts prompt changing code first. Both of the aforementioned changes break the code.


---

Comment by timdumol created at 2009-10-16 11:01:58

Fixed formatting to relocate future imports to the top of the file.


---

Comment by timdumol created at 2009-10-16 11:03:17

Changing status from new to needs_review.


---

Attachment


---

Comment by timdumol created at 2009-12-05 09:59:42

Would anyone mind reviewing this? It just moves the `displayhook_hack` to another file, and adds some tests and a tad of refactoring.


---

Comment by was created at 2009-12-08 20:18:55

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-12-08 20:18:55

Needs work, since this has a subtle bug, which I bet you can easily fix.  See below.

Using regular expressions is unfortunately not rock solid.  For example, this input "mysteriously" gives a SyntaxError:

```
print """
from __future__ import division"""
```

outputs:

```
Syntax Error:
    from __future__ import division"""
```

whereas the similar

```
print """
from __xfuture__ import division"""
```

works fine.  

I think the right fix is to require that the even in the notebook the `from __future__ import ...` lines appear at the very top.  This would make it possible to use the same method you already used.


---

Comment by timdumol created at 2009-12-10 16:13:32

Uses stdlib's `ast` to parse the file instead of regexp's.


---

Comment by timdumol created at 2009-12-10 16:14:30

Changing status from needs_work to needs_review.


---

Attachment

This version of the patch uses `ast` (from stdlib). It should prevent errors such as what you described.


---

Attachment

Rebased on #7650 and its dependencies.


---

Attachment

Missed an import on the rebase.


---

Attachment

Rebased to ~0.60


---

Comment by acleone created at 2010-01-20 07:18:42

Changing status from needs_review to positive_review.


---

Comment by acleone created at 2010-01-20 07:18:42

Rebased to a bit after 0.60 (see trac_7207-sagenb-future-import.3.patch). Other than that LGTM.


---

Comment by mpatel created at 2010-01-25 00:38:05

V4 is rebased for this queue:

```
sagenb-0.6
trac_7249-jinja2_v9.5.patch
trac_7962-link-worksheets-zip-file.patch
trac_7969-escaped-backslash.patch
trac_4217-html-system-formatting.3.patch
trac_3083-print-documentation.5.patch
trac_6182-double-quotes-ws.2.patch
trac_5263-publish-url.patch
trac_7631-republish-name.patch
trac_6353-cookies-diff-ports.patch
trac_7207-sagenb-future-import.3.patch
```



---

Comment by mpatel created at 2010-01-25 00:39:32

Rebased for SageNB 0.6 + queue in comment.  Replaces previous.


---

Attachment


---

Comment by mpatel created at 2010-01-25 00:52:54

Resolution: fixed
