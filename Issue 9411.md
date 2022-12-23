# Issue 9411: Given points on an elliptic curve, this finds a LLL reduced ZZ-independent set

Issue created by migration from https://trac.sagemath.org/ticket/9411

Original creator: aly.deines

Original creation time: 2010-07-02 20:18:16

Assignee: cremona

CC:  jeremywest cremona

Keywords: LLL, rank

This is based on magma code from Cremona.  It takes a set of points on an elliptic curve and uses LLL to return a ZZ-independent set with the same ZZ-span.


---

Attachment


---

Comment by cremona created at 2010-07-05 16:39:10

Aly, would it not have been simpler to move the code of the function lll_reduce(self, points, height_matrix=None) from ell_rational_field to ell_number_field?  That function was written when we only had heights over Q but it does the same thing, essentially.

Apologies if I should have told you about that function earlier...

There may well be other functions which can similarly be moved up;  someone should go systematically through ell_rational_field functions to see which others there are.

On your patch, I see the following:  (1) no tests over fields other than Q; (2) in defining E why not just E=self?;  (3) better to use the pari library than the gp interface (when there's a choice).  Otherwise it applies and builds fine.


---

Comment by cremona created at 2010-07-05 16:39:10

Changing status from new to needs_work.


---

Comment by aly.deines created at 2011-01-12 06:09:17

Knowing about the lll_reduce function and finally getting back to this ticket, I've just created a patch which simply moves the function lll_reduce to ell_number_field.  I've also included doctests over quadratic number fields.  

One note, this code isn't very robust.  For example, in many cases the height pairing matrix is *not* positive definite.  In this case 
"the output depends on the undocumented behaviour of PARI's ``lllgram()``  function", which means there is a divide by zero error.  Here's an example:


```
            sage: Qrt5.<rt5>=NumberField(x^2-5)
            sage: E = EllipticCurve([0,5-rt5,0,rt5,0])
            sage: QuadraticForm(E.height_pairing_matrix(E.gens())).is_positive_definite()
            False
            sage: E.lll_reduce(E.gens())
            Exception raised:
            Traceback (most recent call last):
            File "/Users/aly/Desktop/sage-4.6.1.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
            self.run_one_example(test, example, filename, compileflags)
            File "/Users/aly/Desktop/sage-4.6.1.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
            OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
            File "/Users/aly/Desktop/sage-4.6.1.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
            compileflags, 1) in test.globs
            File "<doctest __main__.example_39[8]>", line 1, in <module>
            E.lll_reduce(E.gens())###line 2106:
            sage: E.lll_reduce(E.gens())
            File "/Users/aly/Desktop/sage-4.6.1.rc1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 2117, in lll_reduce
            U = pari(height_matrix).lllgram().python()
            File "gen.pyx", line 7749, in sage.libs.pari.gen.gen.lllgram (sage/libs/pari/gen.c:34364)
            File "gen.pyx", line 9851, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:46022)
            PariError: division by zero (27)
```



---

Attachment

This replaces the previous patch.  It applies to sage-4.6.1.rc1


---

Comment by cremona created at 2011-01-12 09:36:02

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2011-01-12 09:36:02

Thanks for putting more work into this.  I have not time to re-review right now, but I do intend to.

About the robustness,  a better long term solution would be to separate out two different aspects:  (1) give some points, return a maximal independent subset (or, return an independent set which has the same ZZ-span, which is not the same thing);  (2) given independent points, LLL-reduce them.  

But for this ticket I suggest that we just do the best we can using the pari function and sufficient precision.


---

Comment by cremona created at 2011-04-22 17:24:00

I'm working on this now.  First, I deleted the duplicate function still in ell_rational_field.py (but moved the examples there to ell_number_field.py).  I also added a precision parameter to be passed to the height pairing matrix call, and am trying to make an example where it makes a difference!


---

Comment by cremona created at 2011-05-03 16:34:42

I uploaded my patch which is a revision of Aly's, since I did not want it to get lost.  It's fine for testing but I have not yet included an example where the precision parameter makes a difference.


---

Comment by davidloeffler created at 2011-12-30 17:47:49

What's the status of this ticket? It's marked as "needs review", but the last comment suggests that more work is needed.


---

Comment by cremona created at 2011-12-30 18:40:03

Well, I think it is ready for review.  I certainly think that in principle the function ought to allow the user to set the precision which is used to compute the height-pairing matrix (which was not the case before).  Secondly, we now have one function in ell_number_field instead of just one function on ell_rational_field, or two functions.  So Sage is certainly enhanced by this!

Of course, the reviewer might insist on seeing an example where higher precision makes a difference....but I don't and I am listed as a reviewer though the latest patch was by me so we need a third party to have a look.


---

Comment by zimmerma created at 2012-01-11 15:21:40

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2012-01-11 15:21:40

Changing keywords from "LLL, rank" to "LLL, rank, sd35.5".


---

Comment by zimmerma created at 2012-01-11 15:21:40

all doctests pass on top of sage-4.8.alpha6.

However I suggest adding an example checking the relation between the input points, `newpoints`
and the output matrix `U`:

```
sage: E = EllipticCurve([0, 1, 1, -2, 42])
sage: Pi = E.gens()
sage: Qi, U = E.lll_reduce(Pi)
sage: all(sum(U[i,j]*Pi[i] for i in range(4)) == Qi[j] for j in range(4))
True
```


And please add an example where an `height_matrix` is given, for example
(this also gives an example where the precision matters):

```
sage: E = EllipticCurve([0, 1, 1, -2, 42])
sage: Pi = E.gens()
sage: H=E.height_pairing_matrix(Pi,3)
sage: E.lll_reduce(Pi,height_matrix=H)
([(-4 : 1 : 1), (-3 : 5 : 1), (-2 : 6 : 1), (1 : -7 : 1)], [1 0 0 1]
[0 1 0 1]
[0 0 0 1]
[0 0 1 1])
```


Also, I guess "number of bits of precision of result" should read "number of bits of precision of intermediate computations" (in fact the precision of the height matrix computation, which is
given as input to Pari).

Paul

PS: the doctest coverage could be 100% if we could remove the deprecate function
`local_information`. Can this be done?


---

Comment by chapoton created at 2013-08-20 13:55:25

apply only trac_9411_lll_reduce_number_field.2.patch


---

Comment by chapoton created at 2013-08-20 13:59:43

this needs to be rebased


---

Comment by cremona created at 2013-08-20 14:06:08

I volunteer to do that since I wrote the current patch.  I think we can now remove that deprecated function too (if it is still there).


---

Comment by cremona created at 2013-08-21 14:47:01

I did the rebasing but am now also adding the tests suggested by Paul Zimmermann's comment 9.


---

Attachment

rebased on 5.12.beta1 and added 2 new doctests


---

Comment by cremona created at 2013-08-21 15:00:37

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2013-08-21 15:00:37

Replying to [comment:13 cremona]:
> I did the rebasing but am now also adding the tests suggested by Paul Zimmermann's comment 9.
Done, so back to "needs review".


---

Comment by chapoton created at 2013-08-29 07:52:12

apply only trac_9411_lll_reduce_number_field.2.patch


---

Comment by chapoton created at 2013-09-11 20:09:47

looks good to me.

I have made a review patch, mainly about details of the doc, but also removing the deprecated function `local_information`.

If the minor changes in my review patch are ok, this can be set to positive review

for the bot:

apply trac_9411_lll_reduce_number_field.2.patch, trac_9411_review.patch


---

Attachment

rebased. Once again, if my minor changes are ok, you can set this to positive review


---

Comment by cremona created at 2013-11-25 19:29:14

OK, I am happy to give chapoton's reviewer's patch +1 and set this to positive review.  Since there have been other elliptic curve patches already merged into 5.14.beta4 I hope the rebasing is sufficient!


---

Comment by cremona created at 2013-11-25 19:29:14

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-12-05 08:02:12

Resolution: fixed
