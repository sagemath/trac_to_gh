# Issue 1062: gp interface help should use extended help text (from "??")

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-11-02 01:31:09

Assignee: was

CC:  vdelecroix jdemeyer slelievre


```
<wstein> 
 The new ?? help looks quite nice. It would
 be good for gp.foo? to use it.
```


The idea is that

```
sage: foo = gp(x)
sage: foo.polroots?
```


should use the help text from the gp command `??polroots`.

The obvious approach is to change '?%s' to '??%s' in gp.py's help() method.  This doesn't quite work, for two reasons:

1) gphelp carefully formats the text to fit in the current line width, and then Sage displays this text indented; so almost every line wraps.

2) gphelp uses control characters to make words bold, underlined, etc.; when the help is viewed from the notebook, these control codes are visible in the output, and look very ugly.


---

Comment by mmezzarobba created at 2015-04-13 13:45:48

See #17860 for a possible strategy.


---

Comment by slelievre created at 2018-11-23 08:30:42

Changing keywords from "" to "pari/gp, help".


---

Comment by vdelecroix created at 2020-02-17 13:11:33

This works in `cypari2` which is de facto the way to use PARI in Sage

```
sage: x.polroots?
Signature:      x.polroots(precision)
Docstring:     
   Complex roots of the given polynomial using Schonhage's method, as
   modified by Gourdon.
```



---

Comment by vdelecroix created at 2020-02-17 13:11:33

Changing status from new to needs_review.


---

Comment by mjo created at 2020-04-04 22:30:06

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-06-20 06:21:41

I do not agree that this works. We currently display only the short documentation, for pari() objects as well as for gp() objects.

The complete doc is much longer.


---

Comment by chapoton created at 2020-06-20 06:21:41

Changing status from positive_review to needs_info.
