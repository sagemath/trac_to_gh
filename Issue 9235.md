# Issue 9235: Doctest coverage for sage.categories.homset

Issue created by migration from https://trac.sagemath.org/ticket/9235

Original creator: SimonKing

Original creation time: 2010-06-14 09:59:42

Assignee: nthiery

CC:  niles

Keywords: doctest coverage homset

The doctest coverage for sage.categories.homset was

```
SCORE devel/sage-main/sage/categories/homset.py: 52% (13 of 25)
```


My patch covers all but two methods:

 * get_action_c
 * coerce_map_from_c

These two return (by default) None. Is there a good _indirect_ doctest for these two? I am not familiar with `get_action`, and I don't know what `coerce_map_from_c` does, compared with `_coerce_map_from_`. Perhaps the reviewer can explain it to me, so that I or s/he can add the two missing tests?


---

Comment by SimonKing created at 2010-06-14 10:03:38

Changing status from new to needs_review.


---

Comment by SimonKing created at 2011-03-08 20:52:33

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-03-08 20:52:33

I can not reproduce the error that the patchbot recently found. I don't know how I can push it to test the patch again.

So, I'll change into needs-work and then immediately into needs-review - hope that triggers another attempt of the bot...


---

Comment by SimonKing created at 2011-03-08 20:52:59

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-04-09 07:12:22

It seems to me that the doctest error found by the patchbot is unrelated with my patch: After all, the patch is a just adding documentation and tests.

Is anybody inclined to review it?


---

Comment by SimonKing created at 2011-05-28 09:18:24

-- bump --

The patch is in need of a review since _one year_. I think it would not be difficult to review a pure doctest patch. But having full doctest coverage in yet another part of Sage would be good to have.

I hope that the patch still applies.


---

Comment by niles created at 2011-05-29 06:47:10

deprecation warnings for get_action_c and coerce_map_from_c


---

Comment by niles created at 2011-05-29 06:59:58

Changing status from needs_review to needs_work.


---

Attachment

You're right -- this shouldn't have to wait so long!  I've looked through all the changes, and they look good!  All tests pass, and the documentation builds cleanly, without warnings.  

I used `search_src` to look for other places in Sage where `get_action_c` and `coerce_map_from_c` are used.  The only places they appear are in `structure/parent_old`, so I think these in Homset should be deprecated and (later) removed.  I've added a reviewer patch which adds deprecation warnings and corresponding tests, raising the coverage to 100%.

The only issue I have with `9235_doctest_homset.patch` is the following block:


```
    if category is None:
        if cat_X.is_subcategory(cat_Y):
            category = cat_Y
        elif cat_Y.is_subcategory(cat_X):
            # NT: this "category is None" test is useless and could be removed
            # SK: Indeed! For that reason, the ValueError would never be raised
            # NT: why is there an assymmetry between X and Y?
            # SK: I see no reason. In particular, I don't see why an error should
            #     be raised if cat_X is not cat_Y. So, I uncomment the following
            #     two lines.
##             if not (category is None) and not (cat_X is cat_Y):
##                 raise ValueError, "No unambiguous category found for Hom from %s to %s."%(X,Y)
            category = cat_X
        else:
            # Search for the lowest common super category
            subcats_X = cat_X.all_super_categories(proper = True)
            subcats_Y = set(cat_Y.all_super_categories(proper = True))
            category = None
            for c in subcats_X:
                if c in subcats_Y:
                    category = c
                    break

            if category is None:
                raise TypeError, "No suitable category found for Hom from %s to %s."%(X,Y)
```


If there's no reason to include the second "`category is None`" test, then it and the previous comments should simply be deleted.  And there is a third "`category is None`" test in this block which also looks redundant.


---

Comment by niles created at 2011-05-31 03:57:09

I see that issuing the deprecation warning causes some failures in `modular/abvar/homspace.py`, because the deprecation message is printed.  A minimal example to produce the message is:


```
sage: J = J0(37)
sage: E = J.endomorphism_ring()
sage: x = -1*E.gens()[0]
```


But I don't understand any more about this, so maybe it's better not to include the deprecation warning.  One could simply include tests of the form


```
sage: H = Hom(ZZ^2, ZZ^3)
sage: H.get_action_c(ZZ,operator.add,ZZ) is None
True

sage: H = Hom(ZZ^2, ZZ^3)
sage: H.coerce_map_from_c(ZZ) is None
True
```


without a deprecation warning.

Note that *removing* the methods `get_action_c` and `coerce_map_from_c` causes all tests in `modular/abvar/homspace.py` to pass (of course it should, since these don't do anything anyway).  No other bit of Sage code even caused the deprecation warning to be raised, so perhaps removing them really is a good idea (in which case a deprecation warning would be the first step).  But maybe this should be left for another ticket -- I'll leave it up to you at this point, Simon.


---

Comment by niles created at 2011-05-31 03:57:54

patchbot: apply 9235_doctest_homset.patch


---

Comment by SimonKing created at 2013-02-14 07:51:39

Again, a long time has passed, and meanwhile the patch doesn't apply (3 out of 8 hunks fail). I'll see what I can do about it.


---

Comment by SimonKing created at 2013-02-14 08:03:49

Almost full doctest coverage for homset.py


---

Comment by SimonKing created at 2013-02-14 08:06:44

Changing status from needs_work to needs_review.


---

Attachment

The patch is updated. I think that introducing a deprecation warning for the two survivors of the old coercion model should be the subject of a new ticket. This here should be "doctests only".

Therefore:

Apply 9235_doctest_homset.patch


---

Comment by tscrim created at 2013-02-16 04:42:33

Changing keywords from "doctest coverage homset" to "doctest coverage homset, days45".


---

Comment by tscrim created at 2013-02-16 04:42:33

Hey Simon,

I've uploaded a review patch which goes through and brings the rest of the documentation up to current standards and added the tests to the old coercion model methods with nice warning blocks. Otherwise looks good and I think we should push the actual deprecations to when we completely remove the old coercion model. If you agree with my changes, feel free to set this to positive review.

Thanks,

Travis


---

Comment by SimonKing created at 2013-02-16 09:16:36

The patchbot has correctly applied both patches (I just checked) and finds that all tests pass. Since the patch changes formatting ("EXAMPLE:" becomes "EXAMPLES::" with double colon), I built the documentation. 

I apologize for some misformatting that my patch has introduced (e.g., in codomain()). This is not fixed yet.

What shall we do? Shall I fix the misformattings in my patch? Or shall you fix it by updating the reviewer patch?


---

Attachment

Fixed formatting


---

Comment by tscrim created at 2013-02-16 14:28:16

Can't believe I missed that...this is why one should never read over a doc for errors past midnight :P

I've updated my review patch; thanks for catching that.


---

Comment by SimonKing created at 2013-02-16 18:14:43

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2013-02-16 18:14:43

The reviewer patch looks fine to me!

Apply 9235_doctest_homset.patch trac_9235-doctest_homset-review-ts.patch


---

Comment by jdemeyer created at 2013-02-19 06:48:23

Resolution: fixed
