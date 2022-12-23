# Issue 8000: Add # -*- coding: utf-8 -*- to the top of all SageNB .py files

Issue created by migration from https://trac.sagemath.org/ticket/8000

Original creator: mpatel

Original creation time: 2010-01-19 16:26:52

Assignee: was

CC:  timdumol mvngu

Adding the pragma now to all Python files in SageNB should prevent the increasingly common docbuild errors 

```
reading sources... [ 99%] sagenb/notebook/worksheet
Sphinx error:
'utf8' codec can't decode bytes in position 420-422: invalid data
```

raised when we build the reference manual.

This is partly a followup to #7249, I think.


---

Comment by mpatel created at 2010-01-19 16:29:41

Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?


---

Comment by mpatel created at 2010-01-19 16:31:00

Replying to [comment:1 mpatel]:
> Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?
In particular, post-#7249, we've got non-ASCII Unicode characters in _doctests._


---

Comment by mvngu created at 2010-01-19 16:44:43

Replying to [comment:1 mpatel]:
> Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?
I'm not sure about this, although I can clearly see the benefit of it. On the one hand, this could be further discouragement to people who want to start with Sage development. Could you send an email to sage-devel polling people about this issue? I mean something along the line of, "Should each source file have the character encoding preamble # -*- coding: utf-8 -*- ?". Also see #7999 relating to one file in the Sage library.


---

Comment by mpatel created at 2010-01-19 16:59:19

Actually, it seems that `# -*- coding: utf-8 -*-` was already at the top of `worksheet.py`.


---

Comment by mpatel created at 2010-01-19 17:01:33

Perhaps a different coding slipped in?


---

Comment by mpatel created at 2010-01-19 19:22:03

Replying to [comment:5 mpatel]:
> Perhaps a different coding slipped in?
It turns out that we could fix this problem (cf. #7249) by making the docstring a unicode or raw string (e.g., `"""` --> u`"""` or r`"""`).


---

Comment by timdumol created at 2010-01-19 21:05:05

This adds the coding directive


---

Attachment

This patch should do the trick.


---

Comment by timdumol created at 2010-01-19 21:05:33

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-20 03:46:00

Replying to [comment:7 timdumol]:
> This patch should do the trick.
It does, indeed.  V2 also fixes a failed doctest in `sagenb.misc.sageinspect.`


---

Comment by mpatel created at 2010-01-20 03:46:00

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-20 03:46:40

Fix failed doctest.  Replaces previous.  sagenb repo.


---

Attachment

Rebased for SageNB 0.6 + queue in comment.  Replaces previous.


---

Comment by mpatel created at 2010-01-25 00:47:08

V3 is rebased for this queue (patch version numbers may be off by one):

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
trac_8000-utf-8-coding-directive.2.patch
```



---

Comment by mpatel created at 2010-01-25 00:53:14

Resolution: fixed
