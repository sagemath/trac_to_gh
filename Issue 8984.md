# Issue 8984: Implementation of the Lenart--Postnikov alcove path crystal

Issue created by migration from Trac.

Original creator: brant.c.jones

Original creation time: 2010-05-18 00:26:22

Assignee: sage-combinat

CC:  sage-combinat brant@math.ucdavis.edu rlm

This is an implementation of the Lenart--Postnikov alcove path model as described in:

A combinatorial model for crystals of Kac-Moody algebras. Trans. Amer. Math. Soc.  360  (2008).

It also implements to_coroot_lattice_morphism() and associated_coroot() in root_lattice_realization.py.


---

Comment by brant.c.jones created at 2010-05-18 00:38:50

Changing status from new to needs_review.


---

Comment by aschilling created at 2010-05-18 00:43:31

Test whether Brant gets this message.


---

Comment by aschilling created at 2010-06-06 16:56:45

Changing status from needs_review to needs_work.


---

Comment by aschilling created at 2010-06-06 16:56:45

Changing keywords from "" to "combinat, crystals".


---

Comment by aschilling created at 2010-06-06 16:56:45

Thank you for implementing the alcove path model by Lenart and Postnikov.
This will be a useful addition to sage.

It might be useful to add a few more words about the model you implemented
in the documentation of ClassicalCrystalOfAlcovePaths. For example, you could
add that these are highest weight crystals for classical types
`A_n`, `B_n`, `C_n`, `D_n` and the exceptional types `F_4`, `G_2`, `E_6`,
`E_7`, `E_8`.

Also, for the user it would be helpful to say how precisely one should
enter the input data. For example, you could say

INPUT:
  
   - ``cartan_type`` is the Cartan type of a classical Dynkin diagram 
   - ``highest_weight`` is a dominant weight as a list of coefficients of 
      the fundamental weights `Lambda_i`

It might also be good to briefly describe how the crystal elements
are represented so that the user can interpret the output.

Some technical comments:

(1) In combinat/crystals/alcove_path.py, it might be safer to only 
import the methods/classes that you really need for:

from sage.rings.integer import * (which appears twice, so please remove one!)
from sage.misc.misc import *
from sage.calculus.calculus import *

(2) All methods need EXAMPLES or TESTS. Please add them to the following
methods in combinat/crystals/alcove_path.py for

__classcall__
get_initial_chain
fold
compare_graphs

(3) Perhaps remove the commented out lines by # in

__init__
list

(4) Add extra line after EXAMPLES:: get_chain_from_subset

(5) Remove the commented out `weight` function

(6) You need TESTS or EXAMPLES to_coroot_lattice_morphism in 
sage/combinat/root_system/root_lattice_realization.py


---

Comment by brant.c.jones created at 2010-06-08 00:23:53

Changing status from needs_work to needs_review.


---

Attachment

I have implemented all of the suggestions given by the reviewer above.

Please review the new version.


---

Comment by aschilling created at 2010-06-09 03:49:02

Changing status from needs_review to positive_review.


---

Comment by aschilling created at 2010-06-09 03:49:02

This patch implements the Lenart-Postnikov model for highest weight crystals for finite-dimensional Lie algebras. There are extensive tests to test that this gives the same crystal graph as other models.

All tests pass with sage-4.4.2 and the sage-combinat queue applied to this patch.


---

Comment by mhansen created at 2010-06-09 03:58:54

Resolution: fixed


---

Comment by mhansen created at 2010-06-09 19:18:37

Resolution changed from fixed to 


---

Comment by mhansen created at 2010-06-09 19:18:37

I had to backout this change from 4.4.4 for now.  I was getting weird failures with random_element in matrix_group.py.  I'm trying to figure out why this patch was causing it.


---

Comment by mhansen created at 2010-06-09 19:18:37

Changing status from closed to new.


---

Comment by mhansen created at 2010-06-09 19:18:46

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-06-09 19:18:53

Changing status from needs_review to positive_review.


---

Comment by aschilling created at 2010-06-13 22:39:33

Replying to [comment:12 mhansen]:

Hi Mike,

What is the status on this now? Do you know why there were the strange failures in random_element in matrix_group.py?

Anne


---

Comment by drkirkby created at 2010-06-22 22:39:05

See #9310


---

Comment by aschilling created at 2010-06-25 02:58:51

Replying to [comment:14 drkirkby]:
> See #9310

Is this patch the cause of the failure in #9310 though? It was not
merged into sage-4.4.4 and still the error is there.


---

Comment by nthiery created at 2010-07-10 01:50:46

Hi Robert!

Any chances to merge this patch, since it does not seem any more related to the failures than any other?

Thanks!


---

Comment by rlm created at 2010-07-11 21:08:59

sage-4.5 is in feature freeze mode. Nothing but essential fixes will be merged until final release. I am strongly suggesting that the next release be patches to the sage library only (other than essential spkg fixes), and tickets like these deserve to go in then. (I would have had an alpha for such tickets in the 4.5 series, but the spkg issues are already holding things up long enough.)


---

Comment by mpatel created at 2010-07-21 01:55:28

Resolution: fixed
