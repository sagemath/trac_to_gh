# Issue 7353: French documentation should use Sphinx's French localization

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2009-10-30 01:38:46

Assignee: mvngu

The text on the left bar in Sphinx-generated documents has phrases like "Table of content", "quick search", and so on. Sphinx includes translations of these phrases, so we should use that for our French documentation.

This is very easy: just put `language = 'fr'` in conf.py.


---

Attachment


---

Comment by ddrake created at 2009-10-30 01:49:06

I originally thought that the tutorial also needed this, but it doesn't. So maybe I should have just posted this micro-patch at #7190, but since I already opened the ticket, I uploaded the patch here.


---

Comment by ddrake created at 2009-10-30 01:49:06

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-17 07:56:26

Looks good to me.


---

Comment by mhansen created at 2009-11-17 07:56:26

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-17 07:56:42

Resolution: fixed
