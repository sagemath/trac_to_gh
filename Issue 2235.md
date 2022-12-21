# Issue 2235: doctest issue -- combining # long and # 32-bit / # 64-bit

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-02-20 20:29:27

Assignee: failure

CC:  ncalexander@gmail.com

So I ran into some weird issue earlier with a doctest, and the problem seems to be this: combining # long with # 32-bit / # 64-bit seems to completely ignore the # long directive. Nick can probably tell me more about why it fails, or if his new stuff should fix it.


---

Comment by craigcitro created at 2008-02-21 18:11:01

Note: there's a long doctest in sage/rings/number_field/totallyreal_rel.py that is what caused me to notice this; I've made that a # no doctest for now, because it was causing timeouts on some machines. When this bug is fixed, that needs to be changed into a # long.


---

Comment by jdemeyer created at 2013-03-07 09:45:56

Just need to add a doctest that this works now.


---

Attachment


---

Comment by jdemeyer created at 2013-03-13 10:38:19

Changing status from new to needs_review.


---

Comment by roed created at 2013-03-14 20:24:14

Changing status from needs_review to positive_review.


---

Comment by roed created at 2013-03-14 20:24:14

Looks good to me.


---

Comment by jdemeyer created at 2013-03-17 15:31:52

Resolution: fixed


---

Comment by roed created at 2013-03-28 22:41:36

Changing component from doctest to doctest framework.
