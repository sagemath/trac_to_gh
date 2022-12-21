# Issue 8796: clean up documentation of logic/propcalc.py

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-04-28 06:53:13

Assignee: mvngu

As the subject says.


---

Comment by mvngu created at 2010-05-03 02:50:50

Changing status from new to needs_review.


---

Attachment

Changes in the patch include:

 * Add `sage/logic/propcalc.py` to the reference manual.
 * Remove tab characters.
 * Clean-ups in accordance with [PEP 008](http://www.python.org/dev/peps/pep-0008/).


---

Comment by ncohen created at 2010-05-19 20:08:57

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-05-19 20:08:57

Nice patch. Nothing to complain about :-)

Nathann


---

Comment by leif created at 2010-05-21 03:56:38

_"Parentheses may be used to explicitly *show* order of operation."_

I usually use brackets to *express* (i.e. force) [desired/intended] "order of operation", too. ;-)

_"... variables that consist of a leading letter and trailing underscores and alphanumerics"_ sounds a bit strange.

I'd say _"... whose names can be made up of alphanumerics and underscores but must start with a letter"_ or something like that.

[Haven't applied the patch yet.]


---

Comment by mhansen created at 2010-06-06 08:39:10

Resolution: fixed
