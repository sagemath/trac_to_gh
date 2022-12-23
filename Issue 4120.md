# Issue 4120: New code for binary quadratic forms

Issue created by migration from https://trac.sagemath.org/ticket/4120

Original creator: justin

Original creation time: 2008-09-14 19:31:00

Assignee: tbd

CC:  justin jonhanke tornaria@math.utexas.edu

The code supporting binary quadratic forms, in quadratic_forms/binary_qf.py, is missing some functionality, and relies on Magma and Pari.  The patch in this ticket provides the following changes:
 - tests for equivalence, normal, positive and negative definite, indefinite, primitive forms
 - normalize a form
 - action of matrix on a form
 - find content; factor indefinite forms
In addition: 
 - reduce() no longer calls Pari
 - some cleanup: is_reduced() is rewritten; polynomial() replaced with an instance variable (poly)

Doctests are in place for the new code, so the file remains at 100% coverage.


---

Comment by justin created at 2008-09-14 19:32:11

Context diff of new, old versions of quadratic_forms/binary_qf.py


---

Attachment


---

Comment by mabshoff created at 2008-09-14 19:59:39

Justin,

the diff is inverse and you should also add an extension patch to the file.

Cheers,

Michael


---

Attachment


---

Comment by justin created at 2008-09-24 02:59:01

Updated patch, works with 3.1.1 and 3.1.2.  Needs review.  And maybe testing :-}  Also incorporated performance changes from Holdsworth's changes.


---

Comment by cremona created at 2008-09-24 13:53:13

I am planning to review this, which looks pretty good.  First, some preliminary questions/comments:
    * I see that we now have some, but not all, support for indefinite forms.  (e.g. no equivalence testing, no class number).  Why not use pari interface for those, at least until we do our own?  (I would have thought that pari was pretty efficient for these things).
    * Your action of 2x2 matrices is a left action.  Do we want to allow users to use a right action (say, by having RMul and LMul with Mul an alias for one of them)?
    * Your action includes multiplication by det(A).  Now there are lots of application for this code, some will like that and some will want something else.  So why don't we have another parameter for Mul() which is the power of the determinant to be used.  Personally I would set the default to 0 but if you wanted it to be 1 (as in your code) I could live with that.
    * I still think that quite a lot of the functionality could be factored out into a more general binary form class, but that can be done later by someone (e.g. me) who uses higher degree forms.


---

Comment by justin created at 2008-09-24 21:01:55

The patch also works with 3.1.3.alpha1.  Doctests succeed.


---

Comment by justin created at 2008-10-03 06:05:57

Here's a second patch, to be applied on top of sage-4120.patch.

This one fixes some bugs and typos in the first, cleans up some code, and adds more support for indefinite forms (equivalence checking, in particular).  Probably adds a few bugs as well, but that's just a by-product.


---

Comment by justin created at 2008-10-03 06:06:51

To be applied on top of sage-4120.patch


---

Attachment

This is a third patch, applied on sage-4120-2.patch.

This one extends support for indefinite forms and fixes a few bugs (both in code and in the Buchmann/Vollmer algorithms).

One change in particular deserves discussion: I have changed the normalization and reduction procedures to return both the form in question and the transformation matrix used to derive that form.  This makes things a bit more awkward in the code, so there are two questions: is this really useful, and if yes, is there a better way to do it?

Also, I assigned this to me :-}.


---

Comment by justin created at 2008-10-07 04:22:34

Changing assignee from tbd to justin.


---

Comment by justin created at 2008-10-07 04:23:12

To be applied on top of sage-4120-2.patch


---

Attachment

Applied all three patches against 3.1.3.rc0, one at a time, running the doctests each time.  All doctests succeeded.  No problems noted.


---

Attachment

REPLACES earlier patches


---

Comment by cremona created at 2008-10-28 20:53:02

My patch sage-trac4120new.patch combines the three earlier ones and adds the following:
    * Fixing various bugs and typos
    * Sorting out a lot of formatting issues in doctests
    * Adds some new functions
    * Renames Mul to `__mul__` so one can say Q*M to apply matrix M to form Q

Regarding the latter I relented and removed the scale parameter;  since the det is either +1 or -1 I am happy with multiplying (or dividing) by the determinant.

Issues do remain:
    * The various transform function which return a new form Q and a transform T really must satisfy self.T==Q, but they don't.  Hence the commented out assertions.
    * We must decide whether we are talking about weak or strict equivalence (GL or SL(2,ZZ)).  At the moment it is hard to tell which.
    * For indefinite forms there are several different notions of "reduced".  OK to to stick to one, but we should make this explicit.
    * The class number function looks inefficient to me, it should be replaced by the fast code by Skoruppa to list reduced forms (in the definite case at least).

That's all I can remember, but this will need more work before it can go in.


---

Comment by mabshoff created at 2008-11-08 21:30:45

See also #4470 for Jon Hanke's work on quadratic forms.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-08 21:32:23

Changing component from algebra to quadratic forms.


---

Comment by mabshoff created at 2008-11-28 22:40:44

To comment on the relationship with #4470:

```
AFAIK the binary quadratic forms are untouched by Jon's work. We
should rename the file to bring it more in line with what is coming
from Jon, i.e. all I have left to do to post a patch is to rename
various files to qf_ from quadratic_forms_, fix the imports and rebase
the extensions to module_list.py. All trivial, it just needs to be
done :p
```


Cheers,

Michael


---

Comment by tornaria created at 2009-02-24 02:36:29

I've reviewed the code from the last patch as submitted by John Cremona (sage-trac4120.new.patch). It applies cleanly on 3.3 and also on top of the first two patches in #4470.

Below are some comments about the code in `binary_qf.py`. I didn't make a difference between old code and code in the patch, since most of the code is in the patch, anyway.

 - Constructor:
   - BinaryQF([1,2,3], 4, 5) should raise an error
   - I would like to suggest an additional constructor:
     {{{
        sage: BinaryQF(2, 1, disc = -23)
        2*x^2 + x*y + 3*y^2
     }}}
     this is handy when the discriminant is fixed and one knows the first two coefficients
     of a form

 - `__repr__`:
   
   I don't like the fact that a quadratic form is represented by a polynomial, may lead
   to potential confusion. What about something like:
   "`Binary quadratic form over Integer Ring with coefficients [a, b, c]`"
   ?

 - polynomial:
   - the variables for the polynomial are hardcoded... 'x' and 'y'... not very important (I rather not have a "polynomial" function... I'd replace it by a `__call__` function which works for elements in any ring, then one can call e.g. `Q(x,y)` where x and y are in `ZZ['x,y']`, etc.

 - action by matrices:
   - Q * M is a left action --> more natural to be right action!!
     I.e. right now
     {{{
        sage: Q = BinaryQF(4,-4,15)
        sage: M = matrix(ZZ, 2, [1, 1, 0, 1])
        sage: M1 = matrix(ZZ, 2, [1, 0, 1, 1])
        sage: Q * M * M1 == Q * (M * M1)
        False
        sage: Q * M * M1 == Q * (M1 * M)
        True
     }}}
   - I like the notation `Q(M)` for the action of matrices -- this is consitent with the
     notation for general quadratic forms and representation by vectors or sublattices (#4470)
     

     Maybe * should be reserved for composition?

 - is_normal: he doctest doesn't explain what it is

 - is_equivalent
  - IMO should return True or False
  - have extra parameter to request transformation matrix
  - needs more doctests (in particular indefinite, etc)
  - sage: Q * Q.is_equivalent(Q1)[1].transpose() == Q1 /// should be True
    this is just an issue with the action of matrices being left action
  - for indefinite: should not compute the cycle for every form!!
    instead, compute `self * other^(-1)`  (in the class group), and check if it is in the
    principal cycle, which should of course be cached once for each discriminant. This is
    helpful since one will probably use many forms of the same discriminant together.
    

    Not sure about how to do memory management though: it'd be nice if every indefinite
    form of discriminant D holds a reference to the principal cycle of discriminant D, so
    the cycle is deleted when the last indefinite form of discriminant D is deleted ???
    

    ALSO: IMO the caching of the cycle should be done by the function Cycle() itself, not by
    is_equivalent.
    

    Moreover, the cycle needs to cache the transformation matrix as well, so we can
    actually figure out the correct transformation matrix.

 - matrix: should be the Hessian for consistency with the rest of the code ???
   the advantage is that it makes the matrix over ZZ (with even diagonal)

 - is_zero: should not need a gcd to decide if it is 0

 - s and ss: internal, should be prepended with `__` ???

 - class number computation should use pari

 - implement conversions between pari <--> sage   for BinaryQF and Qfb
   maybe try to wrap around pari functionality as much as possible, for speed ??? (both
   runtime and development!!) E.g. composition, etc.


---

Attachment

New patch; replaces previous patches.


---

Comment by justin created at 2011-03-24 22:56:34

New patch.  Primary content is support for indefinite binary forms.


---

Comment by justin created at 2011-03-24 22:57:02

Changing status from needs_work to needs_review.


---

Comment by justin created at 2011-03-24 23:12:10

Forgot to make this explicit: Previous patches include a lot more changes than are in the new one, but to simplify the review process (and my life), I've decided to break it up into smaller chunks.  More changes will be forthcoming (new trac tickets).


---

Comment by justin created at 2011-03-24 23:21:58

NOTE: And another thing: this patch should be applied against Sage 4.7.alpha2 or later (the release with the patch from #10741).


---

Comment by cremona created at 2011-03-25 19:24:13

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2011-03-25 19:24:13

Patch applies and tests pass.

My only suggestion is that for invalid input you should raise an appropriate error (ValueError) rather than printing something and returning [].  And all integers =0,1(mod 4) should be allowed, even squares?  The docstring should specify exactly what valid inputs are, in any case.


---

Comment by justin created at 2011-03-25 20:35:42

I will make the changes to raise errors rather than return unexpected values; that makes sense.

There may be cases where restrictions on discriminants make sense.  For example, I don't think that reduction for a degenerate form makes sense, and there are cases where we don't have an implementation for for a specific class of forms (indefinite, say).  Thoughts?


---

Comment by cremona created at 2011-03-25 21:59:19

Replying to [comment:23 justin]:
> I will make the changes to raise errors rather than return unexpected values; that makes sense.

Good!  Thanks.

> 
> There may be cases where restrictions on discriminants make sense.  For example, I don't think that reduction for a degenerate form makes sense, and there are cases where we don't have an implementation for for a specific class of forms (indefinite, say).  Thoughts?

OK by me to restrict to B which are 0 or 1 mod 4 and not squares.


---

Comment by pbruin created at 2014-02-26 17:32:07

I tried to do some computations with binary quadratic forms of positive discriminant, discovered that a lot of functionality was missing, and then found this ticket, which has been inactive for 3 years...  Is anyone planning to work on it?

See also #6106.


---

Comment by pbruin created at 2014-02-26 21:13:07

Converted the patch to a Git branch; small fixes to make everything compile and pass tests.

Still `needs_work` in view of comment:22.


---

Comment by git created at 2014-02-26 23:18:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-02-27 14:28:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-02-27 14:29:29

Changing status from needs_work to needs_review.


---

Comment by git created at 2014-04-25 00:02:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-11-27 23:32:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-11-27 23:40:50

I guess my commits can count as reviewer patches.  However, I haven't reviewed all the new code in detail, so the branch should probably still be reviewed as a whole.


---

Comment by chapoton created at 2015-03-27 08:18:38

This ticket currently confuses the patchbot. Temporarily putting to *needs info* to stop the bot loop-testing it.


---

Comment by chapoton created at 2015-03-27 08:18:38

Changing status from needs_review to needs_info.


---

Comment by pbruin created at 2015-06-04 11:12:52

Replying to [comment:38 chapoton]:
> This ticket currently confuses the patchbot. Temporarily putting to *needs info* to stop the bot loop-testing it.
It seems that at least the patchbot "eddy" is testing this ticket without adverse effects.  Let's see what happens if I set it back to "needs_review".  (There was a failure in the last patchbot run, but it seems to be unrelated to this ticket.)


---

Comment by pbruin created at 2015-06-04 11:12:52

Changing status from needs_info to needs_review.


---

Comment by git created at 2016-01-22 20:34:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dimpase created at 2016-11-21 10:41:07

[qfbcompraw](http://doc.sagemath.org/html/en/reference/libs/sage/libs/pari/gen.html#sage.libs.pari.gen.gen_auto.qfbcompraw) is now wrapped, so calling pari directly to use it is no longer necessary, and should be fixed.

cf. the patch part:

```
+            # There could be more elegant ways, but qfbcompraw isn't
+            # wrapped yet in the PARI C library.  We may as well settle
+            # for the below, until somebody simply implements composition
+            # from scratch in Cython.
+            v = list(pari('qfbcompraw(%s,%s)'%(self._pari_init_(),
+                                            right._pari_init_())))
```



---

Comment by dimpase created at 2016-11-21 11:30:14

and the same for `qfbred`, which is now also wrapped.


---

Comment by git created at 2016-11-21 13:51:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-09-08 05:42:22

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2017-09-13 15:52:44

(added the accent to Gonzalo Tornaría's name; maybe this will also convince the patchbot to test this ticket)


---

Comment by git created at 2017-09-19 05:46:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2018-05-15 07:34:24

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2018-05-15 07:34:24

branch does not apply, needs rebase


---

Comment by git created at 2018-05-21 12:16:28

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2018-05-21 12:17:16

Changing status from needs_work to needs_review.


---

Comment by git created at 2018-06-03 17:12:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by sbrandhorst created at 2018-06-03 17:21:04

Some changes I made:
- removed ``@`cached_method` in `polynomial` as we already cache in `_poly`
- `reduced_form(self, matrix=False, implementation=None):` `matrix` seems missleading to me. 
  changed the keywords to `transformation` and `algorithm` to stay consistent with other 
  parts of sage (for example .`hermite_form`)   
- used long names for methods like `is_indef` but keep the short alias
- ``_RhoTau(self, proper=False)``
  removed the `proper` keyword as it is not used.
- use a better bound for `a` in BinaryQF_reduced_representatives from the Buchmann/Vollmer book
- added a keyword proper for is_equivalent as for indefinite forms we only test improper 
  equivalence, we check if the form is in the cycle of the other form but that cycle is improper

Question:
- This requires a deprecation - do we really want to change it? This ticket changes so much   
  already I would vote against it:
  {{{
  -def BinaryQF_reduced_representatives(D, primitive_only=False):
  +def BinaryQF_reduced_representatives(D, primitive_only=True):
  }}}


---

Comment by sbrandhorst created at 2018-06-03 17:22:36

The ticket is not perfect but I think it is okay.
As the perfect is the enemy of the good - positive review on my part if you are happy with my changes and resolve the issue with the primitive_only keyword.


---

Comment by sbrandhorst created at 2018-06-03 17:23:45

Note on my machine tests pass, doc builds and looks reasonable.


---

Comment by cremona created at 2018-06-04 21:20:16

I agree with the decision not to change the default for the primitive-only parameter.


---

Comment by pbruin created at 2018-06-04 21:20:46

I agree too.


---

Comment by git created at 2018-06-05 06:53:05

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2018-06-05 06:54:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by sbrandhorst created at 2018-06-05 06:55:28

Then let us finally get this reviewed :)


---

Comment by pbruin created at 2018-06-12 05:43:32

Changing status from needs_review to positive_review.


---

Comment by pbruin created at 2018-06-12 05:43:32

Fixed a SEEALSO block (causing docbuild to fail) and two pyflakes complaints.  Let's get this ticket in before its 10-year anniversary.


---

Comment by vbraun created at 2018-06-14 07:41:15

Resolution: fixed
