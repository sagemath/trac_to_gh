# Issue 6630: The empty species exists !!!

Issue created by migration from https://trac.sagemath.org/ticket/6630

Original creator: hivert

Original creation time: 2009-07-26 20:49:01

Assignee: hivert

Keywords: species zero

I'm writing a patch which create the empty species. Before the patch I didn't find any way to create it...
It is the species which contains no structure at all and as such does not seems very useful. However, it is the zero of the semi-ring of the species and may be needed when you do computation on species, for example to give the default value for the function sum()...

And this is yet another patch from me about empty objects :)

Florent



---

Comment by hivert created at 2009-07-26 21:54:30

The attached patch should solve the problem. I didn't address the question of making the empty species an actual neutral and zero element with respect to the sum and the product of the semi-ring of species. This means that if you add the empty species with another species you get a different species (an instance of the class `SumSpecies_class`), and the same with the product. This should be solved in a patch which actually create the semi-ring of species...

Florent


---

Comment by hivert created at 2009-07-26 21:54:30

Changing status from new to assigned.


---

Comment by saliola created at 2009-08-24 21:19:26

The patch applies cleanly to sage-4.1.1, passes doctests, and is very nicely written. Positive review.


---

Comment by mvngu created at 2009-08-24 23:20:30

The patch `trac_6630-reviewer.patch` fixes a number of typos found in `empty_species-fh-6630.patch`. It also adds the new module `sage/combinat/species/empty_species.py` to the reference manual; the module is too good to be buried among the source files of the Sage library! In adding the module to the reference manual, the patch fixes some ReST formatting typos. The docstring of the function `EmptySpecies()` has been moved to the class `EmptySpecies_class`. This is so that docstrings for empty species show up in the reference manual. 



The following private methods have doctests, but no docstrings:
 
 1. `__init__()`
 1. `_gs()`
 1. `_structures()`

This lack of docstring would come back to haunt the documentation writer and user because when #6586 is merged then private methods would show up in the reference manual. So two things remain to be done:

 1. Someone needs to review the patch `trac_6630-reviewer.patch`.
 1. Add docstrings to the above private methods. One easy way to do so is to first apply `empty_species-fh-6630.patch`, followed by `trac_6630-reviewer.patch`. Then write docstrings based upon those two patches and upload another patch. I'm marking this ticket as "needs work".


---

Comment by mvngu created at 2009-08-25 00:19:36

And here is another reason why this ticket needs work: the docstring coverage is not 100%:

```
[mvngu@sage sage-4.1.1]$ ./sage -coverage devel/sage-main/sage/combinat/species/empty_species.py 
----------------------------------------------------------------------
devel/sage-main/sage/combinat/species/empty_species.py
SCORE devel/sage-main/sage/combinat/species/empty_species.py: 83% (5 of 6)

Missing documentation:
	 * __init__(self, min=None, max=None, weight=None):


Possibly wrong (function name doesn't occur in doctests):
	 * _gs(self, series_ring, base_ring):
	 * _structures(self, structure_class, labels):

----------------------------------------------------------------------
```

Docstring coverage must be 100% for any new module.


---

Attachment

New version of the patch with mgnvu's one folded.


---

Comment by hivert created at 2009-09-11 15:25:41

Dear Franco and Minh,

I just uploaded the hopefully final version of the patch with full doctests coverage. I reviewed positively mvngu's patch and folded into mine. Please rereview.

Note: There are two slight change in the code:
 - I corrected the output of the species (I never tried to print an empty species).
 - The internal function _structure should never be called. I let it raise an error rather than pass and update the doc accordingly.

Note: for the release manager: use only `empty_species-fh-6630-v2.patch`.

Cheers,

Florent


---

Comment by mhansen created at 2009-09-26 04:22:03

Everything looks good to me.  I will delete the other old patches.


---

Comment by mvngu created at 2009-09-26 05:10:38

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:43:46

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
