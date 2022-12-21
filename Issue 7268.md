# Issue 7268: GLPK : named constraints and variables, export functions ...

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-23 15:26:10

Assignee: tbd

Hello everybody !

This is an update of the GLPK package to match the changes in ``numerical.mip``. Here is the list of changes :

    * Names for the objective function, the whole problem, variables and constraints can be set through the newly exposed GLPK functions
    * A problem can be exported to MPS or LP files
    * GLPK now returns Exceptions when it fails ( it used to silently return the 0 solution ).
    * As solveGLPK, write_mps and write_lp all need the problem to be built as a GLPK structure, a new function  ``build_glp_prob`` does this job and is used by the three of them.

Comments have also been added when felt necessary. The code should be more efficient (and Cythonized) in this version ( this was the whole purpose of redefining the structure of ``numerical.mip`` )

The spkg is available on sagemath at : ~ncohen/glpk-4.38.p3.spkg

Nathann


---

Comment by ncohen created at 2009-10-23 15:28:34

Changing status from new to needs_review.


---

Comment by mvngu created at 2009-11-25 03:58:03

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-11-25 03:58:03

The package installs OK on Sage 4.3.alpha0. Here are some documentation issues in the file `patch/mipGlpk.pyx` that I think need to be addressed:

 1. the function `solve_glpk()` --- document the input `log` and `objective_only`, and explain the expected output (if any).
 1. the function `write_mps()` --- document the input `filename`  and `modern`, and explain the expected output (if any).
 1. the function `write_lp()` --- document what this function does. Also document the input `filename` and explain the expected output (if any).


---

Comment by ncohen created at 2009-11-25 07:33:45

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-11-25 07:33:45

Sorry !! :-)

I wrote these in the wrappers for these functions in class MixedIntegerLinearProgram but forgot to copy them there.... Both files updated ! :-)


---

Comment by malb created at 2009-12-01 17:04:59

A new SPKG is available at

   http://sage.math.washington.edu/home/malb/spkgs/glpk-4.38.p4.spkg

I give Nathan's SPKG a positive review if my referee patch is accepted. The referee patch fixes a mem leak and makes some of the code in the Cython wrapper more Pythonic (I also reverted some pre-mature optimisation which wouldn't speed things up)

I am attaching the patch here for convenience (it is applied in p4 linked above).


---

Comment by ncohen created at 2009-12-01 17:35:55

Your new spkg file contains a build/ directory and a file .cpp in the patch/ directory ( it seems you installed the patch then packaged it without removing these temporary files ). Coild you update it ?

Besides, is there any way for me to get the diff files since the last version ? I am still not that used to mercurial :-)

Thank youuuuuuuuuu !!!

Nathann


---

Comment by ncohen created at 2009-12-01 17:35:55

Changing status from needs_review to needs_work.


---

Comment by malb created at 2009-12-01 17:43:40

I've updated the SPKG and I'll attach the diff.


---

Attachment


---

Comment by ncohen created at 2009-12-01 17:56:53

Looks good :-)

Two questions though :

    * Why do you replace == and != by is and is not ?
    * is enumerating range(500) faster than 0<= i< 500 or is there another reason ?
    * Why did you remove the leading 'r' before the docstrings ? I was under the impression they were requried for the docstring to display correctly...

I knew nothing about enumerate()... I'll remember this one ! :-)

Nathann


---

Comment by ncohen created at 2009-12-01 17:56:53

Changing status from needs_work to needs_info.


---

Comment by malb created at 2009-12-01 18:02:41

> Why do you replace == and != by is and is not ?

False and None are unique objects thus it is sufficient to compare by checking identities. Feel free to change it back, though.

>     * is enumerating range(500) faster than 0<= i< 500 or is there another reason ?

Cython will write 0<= i < 500 automatically, so you can just write proper Python code and Cython will optimise it for you.

>  Why did you remove the leading 'r' before the docstrings ? I was under the impression they were requried for the docstring to display correctly...

Only if they contain a backslash.


---

Comment by ncohen created at 2009-12-01 18:07:34

Then.... Positive review ! And thank you for your answers and your help ! :-)

Nathann


---

Comment by ncohen created at 2009-12-01 18:07:34

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2009-12-01 18:07:39

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-12-01 18:09:32

Depends on #7270 !!!!!!!!!!!!!!!


---

Comment by mhansen created at 2009-12-02 07:32:21

Resolution: fixed


---

Comment by mhansen created at 2009-12-02 07:32:21

Merged in the with the optional packages.


---

Comment by jason created at 2009-12-03 14:39:13

FYI: enumerate is now recognized and sped up by Cython (in version 0.12, which will be in the next version of Sage).  See http://trac.cython.org/cython_trac/ticket/316

So hooray!


---

Comment by ncohen created at 2009-12-03 14:41:17

Thank you    !! :-)

If you are interested by (shorter) reviews, I am splitting the big Flow patch into small ones... The flow is already available, the matching will be available soon too, and the others ( less important ) will follow.
