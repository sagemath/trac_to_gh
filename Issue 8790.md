# Issue 8790: improve doctest coverage of logic/logic.py

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-04-28 04:35:34

Assignee: mvngu

CC:  rws

As the subject says. Currently, the coverage of `sage/logic/logic.py` in Sage 4.4 is:

```
[mvngu`@`sage sage-4.4]$ ./sage -coverage devel/sage-main/sage/logic/logic.py 
----------------------------------------------------------------------
devel/sage-main/sage/logic/logic.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage-main/sage/logic/logic.py: 16% (3 of 18)

Missing documentation:
	 * combine(self, statement1, statement2):
	 * simplify(self, table):
	 * prove(self, statement):


Missing doctests:
	 * get_bit(x, c):
	 * eval(toks):
	 * eval_ltor_toks(lrtoks):
	 * reduce_bins(lrtoks):
	 * reduce_monos(lrtoks):
	 * eval_mon_op(args):
	 * eval_bin_op(args):
	 * eval_and_op(lval, rval):
	 * eval_or_op(lval, rval):
	 * eval_ifthen_op(lval, rval):
	 * eval_iff_op(lval, rval):
	 * tokenize(s, toks):
```



---

Comment by knsam created at 2013-03-09 07:24:12

Changing keywords from "" to "beginner doctest documentation".


---

Comment by riccardomurri created at 2013-08-25 11:09:28

Add docstring to functions `combine`, `simplify` and `prove`.


---

Attachment

Functions `simplify`, `combine` and `prove` are actually not implemented: the code is a stub. Patch ` sage-issue-8790-not-implemented.diff` provides a docstring stating that.

I'm not sure how doctests should be provided here: one could probably change the code to raise a `NotImplemented` exception and look for that in the doctest.


---

Comment by riccardomurri created at 2013-08-25 11:46:10

Rename internal functions to start with an underscore


---

Attachment

The `get_bits`, `eval_*`, `reduce_*` and `tokenize` functions are
explictly described as "for internal use only".  It is inconvenient to
provide a doctest for them, as arguments are the internal
data structures used in the `SymbolicLogic` class.  

Patch ` sage-issue-8790-module-private-funcs.diff​`
renames the functions to begin with an underscore to make their
non-public nature more evident, in the hope to silence the coverage
warning.


---

Comment by LostPw created at 2013-10-07 17:20:24

fix for the combine function #15262


---

Comment by aapitzsch created at 2014-06-22 14:27:26

I get

```
./sage --coverage src/sage/logic/logic.py 
------------------------------------------------------------------------
SCORE src/sage/logic/logic.py: 100.0% (18 of 18)
------------------------------------------------------------------------
```



---

Comment by aapitzsch created at 2014-06-22 14:27:26

Changing status from new to needs_review.


---

Comment by rws created at 2014-06-22 14:36:07

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-06-23 19:16:25

Resolution: fixed
