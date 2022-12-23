# Issue 8429: Split word.py file into 4 files

Issue created by migration from https://trac.sagemath.org/ticket/8429

Original creator: slabbe

Original creation time: 2010-03-03 18:18:23

Assignee: sage-combinat

CC:  abmasse

The file `word.py` is getting very huge and forces one to create new classes inside of it (see below for explanation) which will get the file `word.py` even more huge in the future...

If a file contains the following :


```
#file1.py
class A:
    #huge class
    pass
class C(A):
    #huge class
    pass
}}} 

one can not create a new class between A and C in another file (because of loops of import) :

{{{
#file1.py
class A:
    #huge class
    pass
from file2 import B
class C(B):
    #huge class
    pass
}}} 

{{{
#file2.py
from file1 import A
class B(A)
    #large intermediate class
    pass
}}}

So the solution is either to put everything in the same file or to put everything in different files. In this case, I choose the last solution because `word.py` is getting huge.

This ticket removes `Word_class`, `FiniteWord_class` and `InfiniteWord_class` from `word.py` and put them in new files called respectively `abstrac_word.py`, `finite_word.py` and `infinite_word.py`.



---

Comment by slabbe created at 2010-03-03 18:19:47

I will post a patch as soon as #8418 gets a positive review, because the patch will depend on it.


---

Comment by slabbe created at 2010-03-06 13:12:33

Changing status from new to needs_review.


---

Attachment

Depends on many tickets already merged in 4.3.4.alpha1


---

Comment by abmasse created at 2010-03-08 10:46:08

I tested Sébastien's patch after having applied many tickets of the sage-combinat server. Here is the list

#7420 #7420 #7421 #7976 #7976 #7921 #7921 #7938 #8028 #8001 #8001 #5524 #8095 #8200 #8044 #8093 #8093 #8140 #8140 #8140 #6775 #8186 #8186 #8120 #7978 #8127 #8127 #8215 #8154 #8250 #8250 #8224 #8223 #8232 #8259 #8259 #8187 #8187 #8227 #8227 #8268 #8268 #8289 #8289 #8318 #8313 #7520 #7619 #8294 #8276 #8276 #8276 #8273 #8273 #8367 #8266 #8266 #8266 #8233 #8353 #8353 #8418 #8418 #8418 #8296 #7448 #8475 #8422 #8429

All tests passed, and the documentation buils correctly.


---

Comment by abmasse created at 2010-03-08 10:46:08

Changing assignee from sage-combinat to abmasse.


---

Comment by abmasse created at 2010-03-08 10:48:14

There seems to be three patches that have not been merged to sage-4.3.4 yet, but I don't think they are needed for #8429. Here is the list:

#8475, #8313, #8296.

I shouldn't have included #8429 as it is this current patch. I'll check for the three above patches if they are a problem.


---

Comment by abmasse created at 2010-03-08 10:53:49

Sorry, remove #8313 from the list, that was a typo. So the only tickets to look at are #8475 and #8296.


---

Comment by slabbe created at 2010-03-08 11:30:39

Replying to [comment:5 abmasse]:
> Sorry, remove #8313 from the list, that was a typo. So the only tickets to look at are #8475 and #8296.

Alexandre, I just moved the patch `trac_8429_split_word-sl.patch` before #8475 and #8296 in the sage-combinat tree. I can confirm that they commute so that this ticket doesn't "mercurialy" depend on #8296 and #8475.


---

Comment by abmasse created at 2010-03-08 13:29:44

I restested the patch after having applied all above listed patches except #8296 and #8475 and all tests passed ! The documentation builds fine too, so I give this patch a positive review. It is very unlikely that another patch could be in conflict with this one.


---

Comment by abmasse created at 2010-03-08 13:29:44

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:55:29

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 23:55:29

Merged "trac_8429_split_word-sl.patch" into 4.4.alpha0.
