# Issue 8686: gettext related bug in _ (history)

Issue created by migration from Trac.

Original creator: logix

Original creation time: 2010-04-14 13:01:16

Assignee: itolkov, jason

CC:  was timdumol

Keywords: gettext history documentation

In versions of Sage up to 4.3.2, the following worked as expected:


```
>./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: _?
[...]
sage: _
''
sage: _
''
```

| Sage Version 4.3.2, Release Date: 2010-02-06                       |
| Type notebook() for the GUI, and license() for information.        |
However, with Sage 4.3.3, it has stopped working:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: _?
[...]
sage: _
''
sage: _
<bound method NullTranslations.ugettext of <gettext.NullTranslations instance at 0x4b1a680>>
```

| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
For some things, the history works as expected, but for others it does not.  To me it appears that it is "simple" things, e.g. above, the empty expression, or simple expressions like "3+4" where it does not work anymore, but for more complex things (e.g. if you call a function that returns something), "_" still does what you would expect it to do.

This bug still exists in Sage 4.3.5.


---

Comment by logix created at 2010-04-14 13:08:09

Changing assignee from itolkov, jason to was.


---

Comment by logix created at 2010-04-14 13:08:09

Changing component from interact to user interface.


---

Comment by mhansen created at 2010-05-03 22:01:35

Changing status from new to needs_review.


---

Attachment


---

Comment by mhansen created at 2010-05-03 22:01:48

Changing component from user interface to notebook.


---

Comment by timdumol created at 2010-05-04 04:31:32

Nice debugging. Works as advertised.


---

Comment by timdumol created at 2010-05-04 04:31:32

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-07-11 06:02:25

Resolution: fixed
