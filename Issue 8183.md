# Issue 8183: French PDF tutorial and tour don't build

Issue created by migration from https://trac.sagemath.org/ticket/8183

Original creator: mpatel

Original creation time: 2010-02-04 07:34:34

Assignee: AlexGhitza

CC:  mvngu jhpalmieri

Likely follow-up to #8036.


---

Comment by mpatel created at 2010-02-04 07:36:22

Seems to work.


---

Comment by mpatel created at 2010-02-04 07:38:25

Changing status from new to needs_review.


---

Attachment


---

Comment by mpatel created at 2010-02-04 07:38:25

Changing component from algebra to documentation.


---

Comment by mpatel created at 2010-02-04 07:42:57

I'm not sure if `\usepackage[utf8x]{inputenc}` subsumes `\DeclareUnicodeCharacter{00A0}{\nobreakspace}`.


---

Comment by jhpalmieri created at 2010-02-04 16:36:08

Patch depends on #8036 and #8146.  Positive review.


---

Comment by jhpalmieri created at 2010-02-04 16:36:08

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-05 00:30:29

Ticket #8034 reports the same issue for the French version of "A Tour of Sage".


---

Comment by mpatel created at 2010-02-11 14:29:32

Resolution: fixed
