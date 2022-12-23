# Issue 9720: Add random echelonizable matrices to matrix/constructor.py

Issue created by migration from https://trac.sagemath.org/ticket/9720

Original creator: bwonderly

Original creation time: 2010-08-10 18:51:32

Assignee: jason, was

CC:  rbeezer jason

Adds two routines.  One creates random matrices in echelon form to be used in other routines to be added later.  The other creates random matrices whose echelon form has desirable properties, with the help of the first routine.  These routines are designed as educational tools, generating exam and homework problems, and problem generating interacts.


---

Comment by bwonderly created at 2010-08-10 19:11:10

Changing status from new to needs_review.


---

Attachment


---

Comment by wdj created at 2010-08-11 11:12:26

Applies fine to 4.5.2.rc0.

Two extremely minor comments off the top of my head:

1. "Generate a matrix of a desired size and rank, over a desired field,
       whose reduced row-echelon form has only whole values."
IMHO, "integral" sounds better than "whole".
2. It seems to me that, from the point of view of the functionality,
using base_ring = ZZ returns the same result as base_ring = QQ.
(I understand that over QQ the rref algorithm might be different than over
ZZ, but it seems to me that for the matrices you compute in the 
random_echelonizable_matrix function, the rref algorithm(s) yield
the same result either way. Correct?


---

Attachment

stand-alone version 2 patch, same patch with one revision


---

Comment by bwonderly created at 2010-08-11 23:05:43

Replying to [comment:2 wdj]:
> Applies fine to 4.5.2.rc0.
> 
> Two extremely minor comments off the top of my head:
> 
> 1. "Generate a matrix of a desired size and rank, over a desired field,
>        whose reduced row-echelon form has only whole values."
> IMHO, "integral" sounds better than "whole".

I agree completely and have made the change in the v2 patch.

> 2. It seems to me that, from the point of view of the functionality,
> using base_ring = ZZ returns the same result as base_ring = QQ.
> (I understand that over QQ the rref algorithm might be different than over
> ZZ, but it seems to me that for the matrices you compute in the 
> random_echelonizable_matrix function, the rref algorithm(s) yield
> the same result either way. Correct?
> 

Yes, the rref algorithm yields the same result with base_ring as ZZ or QQ.  However, as these matrices are going to be used primarily as student example problems I think it would be better to keep the default as QQ.  Although there should be a series of row operations without introducing fractions that achieves rref, a student will likely want to use fractions as they row-reduce an output matrix, and the rescale_row or add_multiple_of_row functions will complain if fractions are introduced working with a matrix over ZZ.  
> 
>


---

Comment by wdj created at 2010-08-11 23:21:45

I am ready to give this patch a positive review. However, although it aplies fine to 4.5.2.rc0, it does not pass sage -testall on a 10.6.4 mac pro. The problems seem to be in some mysterious (to me) failures in 


```
sage -t  "local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py"./sage -t  "local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py"
-bash: sage: command not found
hera:sage-4.5.2.rc0 davidjoyner$ ./sage -t  "local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py"sage -t  "local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py"
**********************************************************************
File "/Volumes/Bay2/sagefiles2/sage-4.5.2.rc0/local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py", line 951:
    sage: sage_getsourcelines(matrix, True)[1]
Expected:
    34
Got:
    35
```

and a similar failure in


```
sage -t  "devel/sage/sage/misc/sageinspect.py"
```

I'll try investigating this using an ubuntu machine, but this seems to possibly be an issue.


---

Comment by rbeezer created at 2010-08-11 23:44:51

Appears to me that the test that fails is testing an actual line number of source code from the file defining the `matrix` constructor.  Billy added an import statement at the top of the module, so the line numbers will increment by one?

Rather than patching sagenb, I'm going to do some tests - maybe adding the import of QQ to the same line as the import of ZZ will be a solution.

Rob


---

Comment by rbeezer created at 2010-08-12 00:11:46

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2010-08-12 00:11:46

Billy,

Make a v3 patch and replace the two import statements for ZZ and QQ by the statement


```
from sage.rings.all import ZZ, QQ
```


and subsequent line numbers will return to "normal" and this very technical test should pass.  Do the very complete tests


```
./sage -testall
```


overnight and then post the patch.

I've tested this change on matrix/constructor.py and the two files David has failing.

David - nice catch!

Rob


---

Comment by jason created at 2010-08-12 03:11:40

In the first line of the docstring for the second function, you say:

Generate a matrix of a desired size and rank, over a desired field,

Should that say "desired ring"?


---

Comment by bwonderly created at 2010-08-12 07:13:22

stand-alone version 3 of the same patch, with import statement change  and documentation revision


---

Attachment

Replying to [comment:7 jason]:
> In the first line of the docstring for the second function, you say:
> 
> Generate a matrix of a desired size and rank, over a desired field,
> 
> Should that say "desired ring"?

Absolutely, I've made that change and the import statement change, and all tests passed.


---

Comment by rbeezer created at 2010-08-12 17:02:09

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-08-12 17:02:09

I think this means you are ready to have the reviewing proceed, so I'll change the status to "needs review".


---

Comment by wdj created at 2010-08-12 18:12:23

The latest patch applies fine to 4.5.2.rc0 and passes sage -testall on a 10.6.4 mac pro.

This is a well-documented addition and I definitely will use it teaching linear algebra this semester. Thanks for coding this up!


---

Comment by wdj created at 2010-08-12 18:12:23

Changing status from needs_review to positive_review.


---

Comment by bwonderly created at 2010-08-15 19:55:43

Thanks everyone for the suggestions and the expeditious review!

Release manager:  apply only v3 patch.


---

Comment by mhansen created at 2010-08-25 20:00:35

Changing status from positive_review to needs_info.


---

Comment by mhansen created at 2010-08-25 20:00:35

I think that these should really just be options to the random_matrix function so that we don't have a ton of `random_*_matrix` commands floating around in the global namespace.


---

Comment by wdj created at 2010-08-25 20:17:43

Replying to [comment:13 mhansen]:
> I think that these should really just be options to the random_matrix function so that we don't have a 
> ton of `random_*_matrix` commands floating around in the global namespace.

Though this is logical, I personally vote -1 as it will be somewhat harder
to use for those who need it (teachers not necessarily expert in Sage
but needing it for a quick computation for an example or 2 in a lecture note).

In any case, I hope this will be approved as I am teaching this *right now*:-)


---

Comment by rbeezer created at 2010-08-25 20:22:08

There won't be tons, just four I think.  ;-)  But I agree entirely.

Would you pass some sort of selector in `*args`, then make these methods of some class of matrices?  How would the documentation be immediately or easily accessible?  Is there a model we can follow someplace else in Sage?

If you'd be able to suggest a course of action, I can work with Billy to make this happen.  He's finished posting all his routines (there aren't any more planned) and classes begin Monday, so it'd be nice to get this going quickly so he can wrap up his summer project.

Thanks again, I'd had the same reservations about adding to the global namespace, but hadn't hit on this option.

Rob


---

Comment by rbeezer created at 2010-08-25 20:24:07

I agree with David's comments about documentation - maybe we can make that happen smoothly and logically, but its not coming to me right at the moment.


---

Comment by mhansen created at 2010-08-25 20:34:11

Replying to [comment:15 rbeezer]:
> Would you pass some sort of selector in `*args`, then make these methods of some class of matrices?  How would the documentation be immediately or easily accessible?  Is there a model we can follow someplace else in Sage?

You can leave the functions as they are -- just don't import them into the global namespace.  Then, if you do,


```
sage: a = random_matrix(QQ, 3, 3, rref=True)
sage: b = random_matrix(QQ, 3, 3, echelonizable=True)
```


which just delegate to the appropriate function.  You can add a reference to those functions in the docstring of `random_matrix`.
 
Also, the documentation is not clear on why there is special casing for ZZ and QQ, and that these methods don't work for inexact rings.  Although, you could argue that if you have one of these matrices over `ZZ` you could just convert all the entries to `RR` and things "should" be fine.


---

Comment by rbeezer created at 2010-08-25 20:49:54

Mike -

OK, that makes sense - thanks.

We also have "diagonalizable", "unimodular" and "subspaceable", so I think something like a single keyword type/category/class/method/algorithm (I don't really like any of those too much) that defaults to the current "randomize" behavior would be better.  Is "algorithm" the policy these days for this type of thing?  Some constructors must be square so we would have to check for that first.  (And we can address the ZZ, QQ, inexact situation.)

Thanks for the suggestion and quick help.

David - I think I can make the HTML docs work well, and can include the necessary import/qualified statement in the tab-completion documentation to make the notebook/command-line docs relatively easy to access.  We'd include at least one full example in the docs for random_matrix() so it could be discovered that way.  Does that sound OK?

Billy - I'll try to set things up to make current patch work.  It won't be too hard then for you to adjust the other two that are outstanding.  Sound OK?

Rob


---

Comment by wdj created at 2010-08-25 20:55:15

Replying to [comment:18 rbeezer]:
> Mike -
> 

...

> 
> David - I think I can make the HTML docs work well, and can include the necessary import/qualified 
> statement in the tab-completion documentation to make the notebook/command-line docs relatively 
> easy to access.  We'd include at least one full example in the docs for random_matrix() so it could be 
> discovered that way.  Does that sound OK?


Sounds good - thanks Rob (and Mike)!!


> 
> Rob


---

Comment by rbeezer created at 2010-08-25 21:13:15

Changing status from needs_info to needs_work.


---

Comment by jason created at 2010-08-25 21:25:45

To take care of the namespace issue, what about making it work like graphs does? In other words, "random_matrix" behaves like it always has, and "random_matrix.echelonizable(...)", "random_matrix.unimodular()", etc., do the specialized functions?

I'm a slight -1 on making random_matrix take a ton of options, a lot of which may be mutually exclusive.  For example, if I ask for a random echelonizable matrix over ZZ, with a specific range of entries, will it work?


---

Attachment

Same as v3, but removed routines from global namespace


---

Comment by rbeezer created at 2010-08-25 21:38:32

v4 patch is identical to v3, except the two new routines are not imported into the global namespace, and therefore two import commands are needed in the doctests.

sage/matrix/constructor.py passes randomized testing (-randorder) with these changes.  Full testing later.  Upcoming patch will have `random_matrix()` delegate to these two routines.

Billy's name should still be on this patch as the author.

Rob


---

Comment by rbeezer created at 2010-08-25 22:02:56

Replying to [comment:21 jason]:
> To take care of the namespace issue, what about making it work like graphs does? In other words, "random_matrix" behaves like it always has, and "random_matrix.echelonizable(...)", "random_matrix.unimodular()", etc., do the specialized functions?
> 
> I'm a slight -1 on making random_matrix take a ton of options, a lot of which may be mutually exclusive.  For example, if I ask for a random echelonizable matrix over ZZ, with a specific range of entries, will it work?

Right now I'm thinking:


```
random_matrix(RR, 6, 4, algorithm='randomize')

random_matrix(ZZ, 6, 4, algorithm='echelon_form')

random_matrix(ZZ, 3, 4, algorithm='echelonizable')

random_matrix(ZZ, 8, 8, algorithm='diagonalizable')
```


etc.  `random_matrix()` would be a big switch on the value of `algorithm`.  Default would be 'randomize' and preserve current behavior.  `random_matrix()` would throw errors for "wrong" rings, or "wrong" shapes.

`random_matrix()` would have one good example of each type, with link to actual routine's documentation for PDF & HTL version.  For notebook or CL docs, the documentation would say "use sage.constructor.random_echelonizable_matrix?" for more detailed documentation right after the example (not tested).

`random_matrix()` already takes lots of options - anything the randomize function of the entry type accepts.  I think the new functions only accept `upper_bound` as an option, as a type of what Billy calls "size control".  Currently, the possibilities for arguments is not handled very well:


```
sage: random_matrix(QQ, 3, 4, num_bound = 4, den_bound = 10)
[-3/8 -3/5    1 -4/7]
[ 3/2  2/3   -2 -1/2]
[-1/8  1/2  1/8 -3/8]
sage: random_matrix(ZZ, 3, 4, num_bound = 4, den_bound = 10)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/sage/dev/devel/sage-main/<ipython console> in <module>()

/sage/dev/local/lib/python2.6/site-packages/sage/matrix/constructor.pyc in random_matrix(R, nrows, ncols, sparse, density, *args, **kwds)
    829         A.randomize(density=float(1), nonzero=False, *args, **kwds)
    830     else:
--> 831         A.randomize(density=density, nonzero=True, *args, **kwds)
    832     return A
    833

/sage/dev/local/lib/python2.6/site-packages/sage/matrix/matrix_integer_dense.so in sage.matrix.matrix_integer_dense.Matrix_integer_dense.randomize (sage/matrix/matrix_integer_dense.c:23941)()

TypeError: randomize() got an unexpected keyword argument 'num_bound'
```


I'm -1 to implementing the whole graphs-dot infrastructure for just five or six functions right as Billy is trying to wrap this up.  (And possibly having to deprecate any current behavior.)  I do want to (but have not found the time yet) to implement the dot-syntax for groups.

Just a thought - we could implement a whole random-dot hierarchy: matrices, primes, graphs,....


---

Comment by jason created at 2010-08-25 22:09:37

The algorithm keyword seems natural enough for me.  What I was opposed to was 5 different True/False keyword options, each mutually exclusive for the others.


---

Comment by rbeezer created at 2010-08-25 22:12:49

Replying to [comment:24 jason]:
> The algorithm keyword seems natural enough for me.  What I was opposed to was 5 different True/False keyword options, each mutually exclusive for the others.

Good - I didn't want that either.  I'm going to start on the above shortly.


---

Comment by rbeezer created at 2010-08-26 00:36:10

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-08-26 00:36:10

Into the `random_matrix` routine and I've never been happy with the documentation, and I may even change the code now that I've dipped into it.  So I'm going to do that work on a new ticket along with allowing for integrating the new constructions.  See #9803.

That means that the v4 patch makes this ready to go.  It'll be left hidden until #9803 is done, but at least David J can import it as needed until then.

So if Billy or David want to check-off on my changes from v3 to v4 (undid changes in all.py and added two imports to doctests) then this can go to positive review.  I'll add interested parties to #9803 once I have a patch up, so no need to add yourself yet unless you have more comments.

This also allows Billy to be sole author on this.


---

Comment by wdj created at 2010-08-26 12:01:04

Replying to [comment:26 rbeezer]:

...

> 
> So if Billy or David want to check-off on my changes from v3 to v4 (undid changes in all.py and added two imports to doctests) then this can go to positive review.  I'll add interested parties to #9803 once I have a patch up, so no need to add yourself yet unless you have more comments.
> 


This looks good to me (I even tested it again for safety's sake:-).

> This also allows Billy to be sole author on this.


---

Comment by rbeezer created at 2010-08-26 22:23:15

Thanks, David.  I'm going to move this back to positive review.  Patch up at #9803 to reflect discussion above.

# Release manager

Apply only the v4 patch and please merge with #9803 once it is ready - the calling syntax changes, so both tickets should go in together.


---

Comment by rbeezer created at 2010-08-26 22:23:15

Changing status from needs_review to positive_review.


---

Comment by bwonderly created at 2010-09-03 06:27:56

## Release Manager

#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this
order.


---

Comment by mpatel created at 2010-09-15 09:52:32

Resolution: fixed
