# Issue 5094: Delete/Change SageX references to Cython

Issue created by migration from https://trac.sagemath.org/ticket/5094

Original creator: kcrisman

Original creation time: 2009-01-25 03:45:34

Assignee: tba

In 3.3.alpha0, there is still a reference to SageX in COPYING.txt.  Any others should also be reported here.


---

Comment by kcrisman created at 2009-01-25 03:51:00

This is not a duplicate of #857; the reference is in the second line of the document.


---

Attachment

This is a one-word change of SageX to Cython from the 3.3.alpha0 version of this file.


---

Comment by kcrisman created at 2009-01-29 15:54:42

Here are the others I have found.  Most would be trivial to fix, but I don't know if all these files are long for this world.

misc/cython.py
	In addition to one that should be there, there is one that it not!

rings/integer_mod_ring.py
	An author credit should have Cython added

rings/padics/tutorial.py
	Brief ref

calculus/var.pyx
	Two references at G = globals()

graphs/graph_fast.pyx
	The title refers to it

misc/reset.pyx
	Two references at G = globals()

misc/sagex_ds.pyx 
	Includes references but of course is NAMED after it
	It appears to be used in misc/all.py and rings/polynomial/polynomial_compiled.pyx/.pxd, so need to change those in theory

rings/integer.pyx
	Again a couple

rings/laurent_series_ring_element.pyx
	Brief ref

rings/power_series_ring_element.pyx
	Brief ref

rings/polynomial/polynomial_element.pyx
	A couple references

ext/python.pxi
	Quite a few references at the top

rings/real_rqdf.pyx
	One ref, if this is even being kept

structure/parent_old.pyx
	Several references, is this worth fixing?

libs/pari/gen.pyx
	Brief ref

There were some in docs, but presumably that is not worth changing until after the Sphinx change:
ref/module-sage.rings.integer-mod-ring.html
ref/module-sage.rings.laurent-series-ring-element.html
ref/module-sage.rings.padics.tutorial.html
ref/module-sage.rings.polynomial.polynomial-element.html
ref/module-sage.rings.power-series-ring-element.html
ref/node343.html
tut/node53.html (two examples, in SAGE_ROOT/examples/programming/sagex - should that directory be renamed as well?)


---

Comment by kcrisman created at 2009-02-02 16:38:39

Based on 3.3.alpha0


---

Attachment


---

Comment by mabshoff created at 2009-02-02 17:27:47

Positive review. That it touches python.pxi is rather unfortunate, but oh well ....

I guess in the long term we need to convert python.pxi to a pxd.

One last thing: The "[with patch, needs review]" goes to the front of the summary.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 17:48:37

Merged in Sage 3.3.alpha4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 17:48:37

Resolution: fixed
