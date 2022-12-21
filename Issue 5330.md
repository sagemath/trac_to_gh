# Issue 5330: Move the docs over to the main repository

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-02-21 19:29:23

Assignee: mhansen




---

Comment by mhansen created at 2009-02-21 19:30:17

This patch should be applied before any of the ReST patches.


---

Comment by cwitty created at 2009-02-21 20:56:15

I'm starting to review the Python code and the reference manual parts of this patch.  I'm not planning to review doc/en/* or doc/fr/*, except for the reference manual; so somebody else should do those.


---

Comment by cwitty created at 2009-02-22 02:51:00

OK, this is going to be a long and complicated review :)

I'm attaching a reviewer patch that fixes a few problems (makes doctests in builder.py pass, gives builder.py a better help message than "Help message", removes a module reference from the documentation that was in there twice (which was actually a carryover from the old documentation)).

With this patch, I give a positive review to doc/common (the python code behind "sage -docbuild").

I believe that the non-automatically-generated portions of the new reference manual are essentially the same as the corresponding parts of the old reference manual, with some very important exceptions. (I did notice some errors that were carried over from the original manual, but I'll file separate tickets for those, with patches, so as not to cloud the issue on this ticket.)

The exceptions are that several sections (and one entire chapter) got (accidentally?) omitted from the new reference manual.  These include:

the GPL

sage/schemes/readme.py

and the entire Structures chapter (sage/structure/{sage_object,parent_gens,formal_sum,factorization,element,mutability,sequence,
parent,coerce,coerce_actions,coerce_maps}, sage/sets/{set,primes}).

I'd still vote in favor of applying this patch (and the rest of the sphinxification patches), under the assumption that these missing sections will get re-added to the reference manual quickly.  So: positive review for doc/en/reference.  Except:

There's a lot of junk in doc/en/reference/utils included in this patch (perhaps accidentally?).  Mixed in with the junk are, I think, the tools mhansen used to convert the reference manual.  It would be nice to have the junk at least minimally sorted (remove the files that are totally useless, add a four- or five-line comment at the top of each useful file explaining what it does and how to use it).  With the junk mixed in, that lowers the value of the directory considerably.  But still, it's nice to have mhansen's tools, so a weak positive review on doc/en/reference/utils even in its current state.

And as I mentioned in my previous comment, I did not review doc/fr/*, or doc/en/* except for the reference manual.  I did notice, though, that doctests in some of the not-previously-doctested files fail:

```
The following tests failed:


        sage -t  "devel/sage/doc/en/bordeaux_2008/nf_introduction.rst"
        sage -t  "devel/sage/doc/en/tutorial/distributed.rst"
        sage -t  "devel/sage/doc/fr/tutorial/tour_rings.rst"
        sage -t  "devel/sage/doc/fr/tutorial/tour_numtheory.rst"
```

I did not look into the problems at all.


---

Comment by mhansen created at 2009-02-22 18:34:11

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-22 18:34:11

I've posted a patch which does the following:


```
1. Remove reference/utils for now
2. Fix failing doctests
3. Added macros.tex and fixed sage.misc.latex to work with the new doc location
4. Added schemes/readme back into the reference manual
5. Added the history and license back into the manual
```


These should not be merged individually, but should be folded together.  I'll post a folded version when it's ready to go in.

I'll try to do sage.structure later today.


---

Comment by mhansen created at 2009-02-23 00:03:11

I've added a patch which adds the structure chapter back into the manual


---

Comment by jhpalmieri created at 2009-02-23 21:01:48

A few comments: 

in matrices.rst, ```sage/matrix/matrixrealdoubledense.py``` should be ```sage/matrix/matrix_real_double_dense.pyx```.  (Note the trailing 'x', as well as the underscores.)

in databases.rst: this is a pre-existing condition, but in these lines:

```
Supports databases up to 2 tebibytes (241 bytes) in size.

Strings and BLOBs up to 2 gibibytes (231 bytes) in size.
```

I think the numbers should be `2^41` and `2^31`, respectively.

in interfaces.rst: I think that paragaphs 2 and 3 (the two indented paragraphs) should be denoted by `.. note::`, or whatever the ReST syntax is.

in interfaces.rst: another pre-existing condition: change "esp., useful" to "especially useful"

in interfaces.rst: I think that at least the html version would look better if `Chapter :ref:`ch:libraries`` were changed to just `:ref:`ch:libraries``.  This occurs twice in the file.

Oh dear, I can't find intro.rst here.  Well, wherever the file which used to be 'ref/intro.tex' is, it has a similar issue: in the html, "Chapter The Sage Command Line" would look better as "The Sage Command Line", and the same for "Chapter The Sage Notebook".


(This is only a review of the files which used to be 'ref/blah.tex' -- I didn't look at any other parts of the various patches here.)


---

Comment by mhansen created at 2009-02-24 14:05:00

I've updated trac_5330-3.patch and structure.patch.


---

Comment by mhansen created at 2009-02-24 14:17:49

Replying to [comment:6 jhpalmieri]:
> A few comments: 
> 
> in matrices.rst, ```sage/matrix/matrixrealdoubledense.py``` should be ```sage/matrix/matrix_real_double_dense.pyx```.  (Note the trailing 'x', as well as the underscores.)
> 
> in databases.rst: this is a pre-existing condition, but in these lines:
> {{{
> Supports databases up to 2 tebibytes (241 bytes) in size.
> 
> Strings and BLOBs up to 2 gibibytes (231 bytes) in size.
> }}}
> I think the numbers should be `2^41` and `2^31`, respectively.
> 
> in interfaces.rst: I think that paragaphs 2 and 3 (the two indented paragraphs) should be denoted by `.. note::`, or whatever the ReST syntax is.
> 
> in interfaces.rst: another pre-existing condition: change "esp., useful" to "especially useful"
> 
> in interfaces.rst: I think that at least the html version would look better if `Chapter :ref:`ch:libraries`` were changed to just `:ref:`ch:libraries``.  This occurs twice in the file.

Taken care of.

> Oh dear, I can't find intro.rst here.  Well, wherever the file which used to be 'ref/intro.tex' is, it has a similar issue: in the html, "Chapter The Sage Command Line" would look better as "The Sage Command Line", and the same for "Chapter The Sage Notebook".

I moved the information in info.tex to the main page of the reference manual.  I've removed the leading "Chapter"s.

These are in trac_5330-4.patch.  Note when these are ready to be merged, I'll provided a single folded patch.


---

Attachment


---

Comment by mhansen created at 2009-02-24 18:16:20

All of the above changes are reference.patch and fixes.patch.


---

Comment by mabshoff created at 2009-02-24 19:24:24

Merged both patches in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 19:24:24

Resolution: fixed
