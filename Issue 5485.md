# Issue 5485: issue with dimension of ideals in polynomial rings

archive/issues_005485.json:
```json
{
    "body": "Assignee: @malb\n\nConsider this:\n\n\n```\nsage: R.<x, y> = ZZ[]\nsage: I = R.ideal(0)\nsage: I.dimension()\nverbose 0 (794: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.\n1\n```\n\n\nBut judging from the docstring of I.dimension(),this should be the Krull dimension of R/I, which is 3 since R/I is (canonically isomorphic to) R:\n\n\n```\nsage: R.krull_dimension()\n3\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5485\n\n",
    "created_at": "2009-03-11T08:25:23Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "issue with dimension of ideals in polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5485",
    "user": "https://github.com/aghitza"
}
```
Assignee: @malb

Consider this:


```
sage: R.<x, y> = ZZ[]
sage: I = R.ideal(0)
sage: I.dimension()
verbose 0 (794: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
1
```


But judging from the docstring of I.dimension(),this should be the Krull dimension of R/I, which is 3 since R/I is (canonically isomorphic to) R:


```
sage: R.krull_dimension()
3
```



Issue created by migration from https://trac.sagemath.org/ticket/5485





---

archive/issue_comments_042487.json:
```json
{
    "body": "Out of curiosity, isn't the Krull dimension 2? How can the dimension of the variety be larger than the number of variables? Apparently there are two bugs at work here.",
    "created_at": "2009-03-18T00:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42487",
    "user": "https://github.com/johnperry-math"
}
```

Out of curiosity, isn't the Krull dimension 2? How can the dimension of the variety be larger than the number of variables? Apparently there are two bugs at work here.



---

archive/issue_comments_042488.json:
```json
{
    "body": "Looking up a little bit about Krull dimension, I think I see the problem: ZZ has Krull dimension 1, whereas fields have Krull dimenson 0. The given code assumes that the ground ring is a field. This is assumed by the source material in Cox, Little, and O'Shea, so the old code almost works as it is supposed to.\n\nThere was also an issue with the implementation so that even the zero ideal in a field would be wrong. This is now fixed, so the code works \"as it is supposed to\", by which I mean that it works in fields, per the source material.\n\nHowever, Alex is right that this is not quite the same as what the documentation promises, since the documentation talks as if the ring is arbitrary. So, it doesn't **really** work the way it is supposed to. I have an idea for a fix for the case where the ground ring is not a field: add the Krull dimension of the ground ring to whatever is computed by the current code.\n\nBut is this correct? If so, the fix is trivial. If not, this will require a lot more work, since all my references assume fields.",
    "created_at": "2009-03-18T01:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42488",
    "user": "https://github.com/johnperry-math"
}
```

Looking up a little bit about Krull dimension, I think I see the problem: ZZ has Krull dimension 1, whereas fields have Krull dimenson 0. The given code assumes that the ground ring is a field. This is assumed by the source material in Cox, Little, and O'Shea, so the old code almost works as it is supposed to.

There was also an issue with the implementation so that even the zero ideal in a field would be wrong. This is now fixed, so the code works "as it is supposed to", by which I mean that it works in fields, per the source material.

However, Alex is right that this is not quite the same as what the documentation promises, since the documentation talks as if the ring is arbitrary. So, it doesn't **really** work the way it is supposed to. I have an idea for a fix for the case where the ground ring is not a field: add the Krull dimension of the ground ring to whatever is computed by the current code.

But is this correct? If so, the fix is trivial. If not, this will require a lot more work, since all my references assume fields.



---

archive/issue_comments_042489.json:
```json
{
    "body": "Hi John,\n\nI've learned the hard way not to expect dimension to behave coherently when the base ring is not a field.  This being said, I have just spent some quality time with EGA IV and found something that we can use: Corollary 5.5.4 (page 95 in volume 2 of EGA IV) says that if the ring A is noetherian, then the dimension of A[x_1,...,x_n] is equal to n + dim(A).\n\nThere are examples due to Nagata of non-noetherian rings A such that dim(A)=1 but dim(A[x])=3.\n\nSo here's what we need to do for polynomial rings: check whether the base ring is noetherian; if not, raise a NotImplementedError.  If yes, return the Krull dimension of the base ring plus the number of generators.\n\nIf you want to go ahead and do this, that's great.  If not I can probably get around to it sometime before this weekend.",
    "created_at": "2009-03-18T06:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42489",
    "user": "https://github.com/aghitza"
}
```

Hi John,

I've learned the hard way not to expect dimension to behave coherently when the base ring is not a field.  This being said, I have just spent some quality time with EGA IV and found something that we can use: Corollary 5.5.4 (page 95 in volume 2 of EGA IV) says that if the ring A is noetherian, then the dimension of A[x_1,...,x_n] is equal to n + dim(A).

There are examples due to Nagata of non-noetherian rings A such that dim(A)=1 but dim(A[x])=3.

So here's what we need to do for polynomial rings: check whether the base ring is noetherian; if not, raise a NotImplementedError.  If yes, return the Krull dimension of the base ring plus the number of generators.

If you want to go ahead and do this, that's great.  If not I can probably get around to it sometime before this weekend.



---

archive/issue_comments_042490.json:
```json
{
    "body": "Hi Alex,\n\nWhat is EGA IV? If my university's library has it, I'd be glad to take a look at it.\n\nYou wrote,\n\n> I have just spent some quality time with EGA IV and found\n> something that we can use: Corollary 5.5.4 (page 95 in\n> volume 2 of EGA IV) says that if the ring A is noetherian,\n> then the dimension of A[x_1,...,x_n] is equal to n + dim(A).\n> ...\n> \n> So here's what we need to do for polynomial rings: check\n> whether the base ring is noetherian; if not, raise a\n> NotImplementedError.  If yes, return the Krull dimension of\n> the base ring plus the number of generators.\n\n\nHold on: `dimension()` is a method of an ideal, not of a ring. I can see that this would work with (0), but will it work with other ideals? i.e., can I assume that if R is Noetherian, then I should add the affine dimension? (I'm not sure that *affine dimension* is the right term, probably not, but I hope you get the idea.)\n\nFor example:\n\n\n```\nsage: R.<x,y> = ZZ[]\nsage: I = R.ideal(x+y)\nsage. I.dimension()\n```\n\n\n\nShould the answer be 1 (current) or 2 (my wholly uninformed guess, dim ZZ + affine dim of ideal) or something else?",
    "created_at": "2009-03-18T15:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42490",
    "user": "https://github.com/johnperry-math"
}
```

Hi Alex,

What is EGA IV? If my university's library has it, I'd be glad to take a look at it.

You wrote,

> I have just spent some quality time with EGA IV and found
> something that we can use: Corollary 5.5.4 (page 95 in
> volume 2 of EGA IV) says that if the ring A is noetherian,
> then the dimension of A[x_1,...,x_n] is equal to n + dim(A).
> ...
> 
> So here's what we need to do for polynomial rings: check
> whether the base ring is noetherian; if not, raise a
> NotImplementedError.  If yes, return the Krull dimension of
> the base ring plus the number of generators.


Hold on: `dimension()` is a method of an ideal, not of a ring. I can see that this would work with (0), but will it work with other ideals? i.e., can I assume that if R is Noetherian, then I should add the affine dimension? (I'm not sure that *affine dimension* is the right term, probably not, but I hope you get the idea.)

For example:


```
sage: R.<x,y> = ZZ[]
sage: I = R.ideal(x+y)
sage. I.dimension()
```



Should the answer be 1 (current) or 2 (my wholly uninformed guess, dim ZZ + affine dim of ideal) or something else?



---

archive/issue_comments_042491.json:
```json
{
    "body": "EGA is Grothendieck's Elements de Geometrie Algebrique.  Here is a better reference: Eisenbud's \"Commutative algebra with a view toward algebraic geometry\", more precisely chapter 8 \"Introduction to dimension theory\".  I think we can get a lot of mileage even just out of the axioms that he gives for dimension (which turn out to uniquely characterise Krull dimension).",
    "created_at": "2009-03-28T02:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42491",
    "user": "https://github.com/aghitza"
}
```

EGA is Grothendieck's Elements de Geometrie Algebrique.  Here is a better reference: Eisenbud's "Commutative algebra with a view toward algebraic geometry", more precisely chapter 8 "Introduction to dimension theory".  I think we can get a lot of mileage even just out of the axioms that he gives for dimension (which turn out to uniquely characterise Krull dimension).



---

archive/issue_comments_042492.json:
```json
{
    "body": "OK, so there are several issues here.\n\nOne is that we're not sure that the naive algorithm implemented in dimension() works over base rings that are not fields.  The most interesting instance of this (in my opinion) is when the base ring is ZZ.  We are currently returning wrong answers, so even raising a `NotImplementedError` would be preferable.  Of course, it would be nice if we could get it to work -- but note that Singular 3.1.0 will have support for polynomial rings over ZZ, so in the worst case we can wait until they release.\n\nThe more pressing issue is that the naive algorithm returns wrong answers even if you run it over QQ.  To see this, try the following as it is now:\n\n\n```\nsage: R.<x, y> = QQ[]\nsage: I = R.ideal(0)\nsage: I.dimension()\n2\n```\n\n\nThis is the correct answer, and it's coming directly from Singular.  However, we can force Sage to use the naive algorithm by inserting `raise TypeError` on line 977 of `multi_polynomial_ideal.py`.  Run `sage -br` and try the same computation again:\n\n\n```\nsage: R.<x, y> = QQ[]\nsage: I = R.ideal(0)\nsage: I.dimension()\nverbose 0 (932: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.\n1\n```\n\n\nThis is wrong and should be our main priority.  In fact, I think it would be ok to just fix this for this ticket and open enhancement tickets for dimension() over tricky base rings.",
    "created_at": "2009-03-29T02:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42492",
    "user": "https://github.com/aghitza"
}
```

OK, so there are several issues here.

One is that we're not sure that the naive algorithm implemented in dimension() works over base rings that are not fields.  The most interesting instance of this (in my opinion) is when the base ring is ZZ.  We are currently returning wrong answers, so even raising a `NotImplementedError` would be preferable.  Of course, it would be nice if we could get it to work -- but note that Singular 3.1.0 will have support for polynomial rings over ZZ, so in the worst case we can wait until they release.

The more pressing issue is that the naive algorithm returns wrong answers even if you run it over QQ.  To see this, try the following as it is now:


```
sage: R.<x, y> = QQ[]
sage: I = R.ideal(0)
sage: I.dimension()
2
```


This is the correct answer, and it's coming directly from Singular.  However, we can force Sage to use the naive algorithm by inserting `raise TypeError` on line 977 of `multi_polynomial_ideal.py`.  Run `sage -br` and try the same computation again:


```
sage: R.<x, y> = QQ[]
sage: I = R.ideal(0)
sage: I.dimension()
verbose 0 (932: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
1
```


This is wrong and should be our main priority.  In fact, I think it would be ok to just fix this for this ticket and open enhancement tickets for dimension() over tricky base rings.



---

archive/issue_comments_042493.json:
```json
{
    "body": "The patch I uploaded 11 days ago *should* fix the problem you identified. Unfortunately, I wrote it using an earlier version of Sage (not 3.4). I'll upload a new version tomorrow.",
    "created_at": "2009-03-29T12:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42493",
    "user": "https://github.com/johnperry-math"
}
```

The patch I uploaded 11 days ago *should* fix the problem you identified. Unfortunately, I wrote it using an earlier version of Sage (not 3.4). I'll upload a new version tomorrow.



---

archive/issue_comments_042494.json:
```json
{
    "body": "previous fix rewritten for sage 3.4, with Alex's recommendation on a NotImplementedError",
    "created_at": "2009-03-30T22:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42494",
    "user": "https://github.com/johnperry-math"
}
```

previous fix rewritten for sage 3.4, with Alex's recommendation on a NotImplementedError



---

archive/issue_comments_042495.json:
```json
{
    "body": "Attachment [dimension_zero_ideal.patch](tarball://root/attachments/some-uuid/ticket5485/dimension_zero_ideal.patch) by @johnperry-math created at 2009-03-30 22:40:18\n\nThe current patch raises a NotImplementedError over rings that are not fields. (Tested with ZZ[x,y].) Over rings that Singular can't handle, this now works with the given problem. I added a docstring that tests it over PolynomialRing(GF(2147483659),order='lex'), and it returns the correct result.",
    "created_at": "2009-03-30T22:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42495",
    "user": "https://github.com/johnperry-math"
}
```

Attachment [dimension_zero_ideal.patch](tarball://root/attachments/some-uuid/ticket5485/dimension_zero_ideal.patch) by @johnperry-math created at 2009-03-30 22:40:18

The current patch raises a NotImplementedError over rings that are not fields. (Tested with ZZ[x,y].) Over rings that Singular can't handle, this now works with the given problem. I added a docstring that tests it over PolynomialRing(GF(2147483659),order='lex'), and it returns the correct result.



---

archive/issue_comments_042496.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-04-03T10:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42496",
    "user": "https://github.com/aghitza"
}
```

Looks good to me.



---

archive/issue_comments_042497.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-03T23:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42497",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042498.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-03T23:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5485#issuecomment-42498",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael
