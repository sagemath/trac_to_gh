# Issue 9420: SubgraphSearch class instead of a method, digraphs fixed

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-07-03 11:52:09

Assignee: jason, ncohen, rlm

CC:  rlm

Hello !!

This patch implements the class SubgraphSearch, which enables one to look for copies of a small graph in a larger one, which is exactly what the method subgraph_search previously did (#8922).

The code is simply inserted inside a new class, with a few other methods to iterate over the occurences, or to count them !

This could have been done with a simple "yield" in Cython, though we may not want to wait until they are implemented ;-)

Nathann


---

Attachment


---

Comment by ncohen created at 2010-07-03 11:53:17

Changing status from new to needs_review.


---

Comment by dimpase created at 2010-09-19 06:57:40

OK, tested on Debian Linux amd64, and on MacOSX PPC with gcc4.2.
The change seems to be more ideological than adding more functionality/bugfixing.
It would be nice if someone more versed in Sage had a look, whether this is not something 
alien ideologically...


---

Comment by dimpase created at 2010-09-19 06:57:40

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-09-19 08:32:10

indeed... and most importantly, it may have consisted in replacing "return" by "yield", if only those were available in Cython `:-p`

Nathann


---

Comment by mpatel created at 2010-09-29 08:39:28

Resolution: fixed
