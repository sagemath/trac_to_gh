# Issue 9371: Implement E.two_torsion_rank() over number fields

Issue created by migration from Trac.

Original creator: weigandt

Original creation time: 2010-06-29 04:12:52

Assignee: weigandt

CC:  cremona

Keywords: elliptic curves, two torsion rank

The function E.two_torsion_rank() can easily be made to work over number fields. The current implementation over QQ calls E.torsion_subgroup() and makes nontrivial use of Mazur's torsion theorem. This should be more efficient and more general by considering the 2-division polynomial.


---

Comment by weigandt created at 2010-07-01 18:36:41

Extend E.two_torsion_rank() method to number fields. Applies to 4.4.4


---

Comment by weigandt created at 2010-07-01 18:37:27

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2010-07-05 16:47:04

Looks good: a better method and more general.   However:  why not move the function all the way up to ell_field?  There's no reason at all why the same code would not work over any field of char. not 2, and even in char. 2 (where the result is at most 0 or 1 for supersingular/ordinary curves, but so what).

If you do that, add extra doctests over (say) finite fields.
While you are at it, one thing about the docstring could be improved:  the short description should fit on one line, so cut it after E(K), and put the rest into a separate ALGORITHM block.
 
"Needs work" sounds negative, so let me elaborate: this is good and with a tiny amount of work would be very good!


---

Comment by cremona created at 2010-07-05 16:47:04

Changing status from needs_review to needs_work.


---

Comment by weigandt created at 2011-03-23 01:41:00

new patch, replaced old one, applies to 4.6.2


---

Comment by weigandt created at 2011-03-23 01:42:01

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by gagansekhon created at 2011-03-23 16:29:09

I think there should be at least 2 more different examples like you had before. Either you can add then I can review or I can add and we will need to find a new reviewer


---

Comment by aly.deines created at 2011-03-23 17:17:14

added documentation, replaces previous patch


---

Attachment

it initially failed sage/interface/r.py, but once I ran it separately and it worked.


---

Comment by gagansekhon created at 2011-03-23 22:06:25

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-12 08:04:54

Resolution: fixed
