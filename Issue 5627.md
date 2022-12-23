# Issue 5627: Trivial typo in quadratic_nonresidue

archive/issues_005627.json:
```json
{
    "body": "Assignee: justin\n\nCC:  jonhanke\n\nAn \"l\" was missing.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/5627\n\n",
    "created_at": "2009-03-29T02:58:53Z",
    "labels": [
        "quadratic forms",
        "trivial",
        "bug"
    ],
    "title": "Trivial typo in quadratic_nonresidue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5627",
    "user": "kcrisman"
}
```
Assignee: justin

CC:  jonhanke

An "l" was missing.  

Issue created by migration from https://trac.sagemath.org/ticket/5627





---

archive/issue_comments_043931.json:
```json
{
    "body": "Attachment\n\nBased on 3.4",
    "created_at": "2009-03-29T02:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43931",
    "user": "kcrisman"
}
```

Attachment

Based on 3.4



---

archive/issue_comments_043932.json:
```json
{
    "body": "While fixing this, I also changed the TypeErrors to more appropriate ValueErrors, added a catch for non-primeness that is just slightly more informative (since no longer from legendre_symbol, but from the function itself), and added a doctest of one of these ValueErrors.",
    "created_at": "2009-03-29T03:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43932",
    "user": "kcrisman"
}
```

While fixing this, I also changed the TypeErrors to more appropriate ValueErrors, added a catch for non-primeness that is just slightly more informative (since no longer from legendre_symbol, but from the function itself), and added a doctest of one of these ValueErrors.



---

archive/issue_comments_043933.json:
```json
{
    "body": "Here's a trivial observation on performance. Look at the line\n\n```\n247\t        for r in range(2,p):\n```\n\nWith the patch as is, on sage.math I get the following timings:\n\n```\n# BEFORE\nsage: p = 179424673\nsage: time quadratic_nonresidue(p)\nCPU times: user 9.07 s, sys: 4.37 s, total: 13.44 s\nWall time: 13.44 s\n5\nsage: timeit(\"quadratic_nonresidue(p)\")\n5 loops, best of 3: 19.3 s per loop\n```\n\nNow if I change the said line to\n\n```\n247\t        for r in xrange(2,p):\n```\n\nI get some performance improvement:\n\n```\n# AFTER\nsage: p = 179424673\nsage: time quadratic_nonresidue(p)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n5\nsage: timeit(\"quadratic_nonresidue(p)\")\n625 loops, best of 3: 36.6 \u00b5s per loop\n```\n\nHowever, in both cases whether we use `range()` or `xrange()`, if p is say 88462514817229869523, then I get the following error for `range()`:\n\n```\nsage: p = 88462514817229869523\nsage: quadratic_nonresidue(p)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/mvngu/.sage/temp/sage.math.washington.edu/14179/_home_mvngu__sage_init_sage_0.py in <module>()\n\n/scratch/mvngu/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/quadratic_forms/extras.pyc in quadratic_nonresidue(p)\n    245     ## Find the smallest non-residue mod p\n    246     try:\n--> 247         for r in range(2,p):\n    248             if legendre_symbol(r, p) == -1:\n    249                 return r\n\nTypeError: range() integer end argument expected, got sage.rings.integer.Integer.\n```\n\nAnd for `xrange()`, I get a similar error, but this time it's an `OverflowError`:\n\n```\nsage: p = 88462514817229869523\nsage: quadratic_nonresidue(p)\n---------------------------------------------------------------------------\nOverflowError                             Traceback (most recent call last)\n\n/home/mvngu/.sage/temp/sage.math.washington.edu/14262/_home_mvngu__sage_init_sage_0.py in <module>()\n\n/scratch/mvngu/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/quadratic_forms/extras.pyc in quadratic_nonresidue(p)\n    245     ## Find the smallest non-residue mod p\n    246     try:\n--> 247         for r in xrange(2,p):\n    248             if legendre_symbol(r, p) == -1:\n    249                 return r\n\nOverflowError: long int too large to convert to int\n```\n",
    "created_at": "2009-03-31T06:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43933",
    "user": "mvngu"
}
```

Here's a trivial observation on performance. Look at the line

```
247	        for r in range(2,p):
```

With the patch as is, on sage.math I get the following timings:

```
# BEFORE
sage: p = 179424673
sage: time quadratic_nonresidue(p)
CPU times: user 9.07 s, sys: 4.37 s, total: 13.44 s
Wall time: 13.44 s
5
sage: timeit("quadratic_nonresidue(p)")
5 loops, best of 3: 19.3 s per loop
```

Now if I change the said line to

```
247	        for r in xrange(2,p):
```

I get some performance improvement:

```
# AFTER
sage: p = 179424673
sage: time quadratic_nonresidue(p)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
5
sage: timeit("quadratic_nonresidue(p)")
625 loops, best of 3: 36.6 µs per loop
```

However, in both cases whether we use `range()` or `xrange()`, if p is say 88462514817229869523, then I get the following error for `range()`:

```
sage: p = 88462514817229869523
sage: quadratic_nonresidue(p)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/14179/_home_mvngu__sage_init_sage_0.py in <module>()

/scratch/mvngu/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/quadratic_forms/extras.pyc in quadratic_nonresidue(p)
    245     ## Find the smallest non-residue mod p
    246     try:
--> 247         for r in range(2,p):
    248             if legendre_symbol(r, p) == -1:
    249                 return r

TypeError: range() integer end argument expected, got sage.rings.integer.Integer.
```

And for `xrange()`, I get a similar error, but this time it's an `OverflowError`:

```
sage: p = 88462514817229869523
sage: quadratic_nonresidue(p)
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/14262/_home_mvngu__sage_init_sage_0.py in <module>()

/scratch/mvngu/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/quadratic_forms/extras.pyc in quadratic_nonresidue(p)
    245     ## Find the smallest non-residue mod p
    246     try:
--> 247         for r in xrange(2,p):
    248             if legendre_symbol(r, p) == -1:
    249                 return r

OverflowError: long int too large to convert to int
```




---

archive/issue_comments_043934.json:
```json
{
    "body": "Those are very interesting remarks!  Unfortunately, I didn't write it, I just used it, as they say.  \n\nWhat I would say is that you should definitely review this, based of course on whether it fixes the typo and whether the new error checks and doctest are wrong (and of course whether it makes performance WORSE, which is possible since IANAP [I am not a programmer!]).  \n\nThen you should open a different ticket for the performance issue and implement whatever you think is best.  (Maybe srange would allow your other example to work?)  I feel like this is what mabshoff would say, anyway :)  I'm not really sure whether this function has non-pedagogical uses in real life, but it's always worth looking at improvements that dramatic!",
    "created_at": "2009-03-31T17:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43934",
    "user": "kcrisman"
}
```

Those are very interesting remarks!  Unfortunately, I didn't write it, I just used it, as they say.  

What I would say is that you should definitely review this, based of course on whether it fixes the typo and whether the new error checks and doctest are wrong (and of course whether it makes performance WORSE, which is possible since IANAP [I am not a programmer!]).  

Then you should open a different ticket for the performance issue and implement whatever you think is best.  (Maybe srange would allow your other example to work?)  I feel like this is what mabshoff would say, anyway :)  I'm not really sure whether this function has non-pedagogical uses in real life, but it's always worth looking at improvements that dramatic!



---

archive/issue_comments_043935.json:
```json
{
    "body": "Attachment\n\nreferee patch",
    "created_at": "2009-04-02T05:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43935",
    "user": "mvngu"
}
```

Attachment

referee patch



---

archive/issue_comments_043936.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch `quad-nonres.patch` applies OK against Sage 3.4.1.alpha0; all doctests passed with the options\n\n```\n-t -long\n```\n\nI'm also adding the patch `trac_5627-referee.patch` which adds another test case in addition to kcrisman's test case. This patch should be applied on top of kcrisman's patch. So positive review for kcrisman's patch. Only my patch needs to be reviewed.\n\n\n\nAs for my observation on performance improvement, I agree with kcrisman that the issue should definitely be addressed in another ticket. That issue should not prevent kcrisman's patch from being applied, since kcrisman's patch only deals with exception handling, adding a test case, and fixing a typo.",
    "created_at": "2009-04-02T05:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43936",
    "user": "mvngu"
}
```

REFEREE REPORT



The patch `quad-nonres.patch` applies OK against Sage 3.4.1.alpha0; all doctests passed with the options

```
-t -long
```

I'm also adding the patch `trac_5627-referee.patch` which adds another test case in addition to kcrisman's test case. This patch should be applied on top of kcrisman's patch. So positive review for kcrisman's patch. Only my patch needs to be reviewed.



As for my observation on performance improvement, I agree with kcrisman that the issue should definitely be addressed in another ticket. That issue should not prevent kcrisman's patch from being applied, since kcrisman's patch only deals with exception handling, adding a test case, and fixing a typo.



---

archive/issue_comments_043937.json:
```json
{
    "body": "I have added another patch after looking carefully at this, which does the following:\n\n1. I removed hilbert_symbol_rational(), making a trivial change to hilbert_symbol() so that it already works on rationals.  I think this will useful outside the quadratic forms module.\n2. I moved IsPadicSquare() to a member function for rationals, so you now say r.is_padic_square(p) instead of IsPadicSquare(r,p), while at the same time making the function simpler and cleaner.  I think this will also be useful outside the quadratic forms module.\n3. I removed random_int_upto(n) since it does the same as ZZ.random_element(n).\n4. I simplified quadratic_nonresidue() (and changed its name to least_quadratic_nonresidue()) -- by putting in three simple tests for when the answer is 2, 3 or 5 the loop is avoided in 7/8 of the cases.   I also changed the loop to \"for r in xsrange(7,p)\", in response to the discussion earlier on this ticket:  adding the x gives an iterator instead of making the whole list and iterating through it (bad for large p!), and adding the s makes the iterator yield Sage integers (so it works for p too large to fit into a python int).  I also added an is_prime() test on p, since otherwise if you give it a huge composite number there seemed to be a danger that it would run through a loop of length p before realising that the input was invalid.\n\nAll tests in sage/quadratic_forms pass, as do those in arith.py and rational.py which were also touched.\n\nIf one of the origianl posters can ok my patch then the whole lot can be merged, I hope.",
    "created_at": "2009-04-08T11:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43937",
    "user": "cremona"
}
```

I have added another patch after looking carefully at this, which does the following:

1. I removed hilbert_symbol_rational(), making a trivial change to hilbert_symbol() so that it already works on rationals.  I think this will useful outside the quadratic forms module.
2. I moved IsPadicSquare() to a member function for rationals, so you now say r.is_padic_square(p) instead of IsPadicSquare(r,p), while at the same time making the function simpler and cleaner.  I think this will also be useful outside the quadratic forms module.
3. I removed random_int_upto(n) since it does the same as ZZ.random_element(n).
4. I simplified quadratic_nonresidue() (and changed its name to least_quadratic_nonresidue()) -- by putting in three simple tests for when the answer is 2, 3 or 5 the loop is avoided in 7/8 of the cases.   I also changed the loop to "for r in xsrange(7,p)", in response to the discussion earlier on this ticket:  adding the x gives an iterator instead of making the whole list and iterating through it (bad for large p!), and adding the s makes the iterator yield Sage integers (so it works for p too large to fit into a python int).  I also added an is_prime() test on p, since otherwise if you give it a huge composite number there seemed to be a danger that it would run through a loop of length p before realising that the input was invalid.

All tests in sage/quadratic_forms pass, as do those in arith.py and rational.py which were also touched.

If one of the origianl posters can ok my patch then the whole lot can be merged, I hope.



---

archive/issue_comments_043938.json:
```json
{
    "body": "I hate to be a wet blanket, but probably two things should be done:\n\n1) Change the summary - this is no longer about a trivial typo\n\n2) (possibly) leave in the no-longer-useful or moved functions with standard 6-month deprecation warning, including of course leaving in the import statements in other files like all.py.  Of course these would now just call the \"better\" functions instead of leaving in their old code.  Unless deprecation does not apply to these sort of functions?  That policy is still not completely clear to me.",
    "created_at": "2009-04-08T14:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43938",
    "user": "kcrisman"
}
```

I hate to be a wet blanket, but probably two things should be done:

1) Change the summary - this is no longer about a trivial typo

2) (possibly) leave in the no-longer-useful or moved functions with standard 6-month deprecation warning, including of course leaving in the import statements in other files like all.py.  Of course these would now just call the "better" functions instead of leaving in their old code.  Unless deprecation does not apply to these sort of functions?  That policy is still not completely clear to me.



---

archive/issue_comments_043939.json:
```json
{
    "body": "You are probably right, I got a bit carried away when I saw functions I knew I would like to use but rather hidden away.\n\nI think that for functions which are only used in this module (i.e. quadratic_forms/*) we do not need to go through the deprecation procedure, especially as this stuff has not been in Sage long anyway.\n\nA suitable new Summary would be something like \"Tidy up utility functions for quadratic forms\", but I'll leave that to you as it is your patch.\n\nBy the way, the extend_to_primitive() function will be extremely useful too, and I would like to see it mvoed to somewhere like matrix/matrix_integer_dense.pyx (where smith_form is) but I thought I had wreaked enough havoc as it was.\n\nAny comment from mvngu who did the original refereeing?",
    "created_at": "2009-04-08T14:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43939",
    "user": "cremona"
}
```

You are probably right, I got a bit carried away when I saw functions I knew I would like to use but rather hidden away.

I think that for functions which are only used in this module (i.e. quadratic_forms/*) we do not need to go through the deprecation procedure, especially as this stuff has not been in Sage long anyway.

A suitable new Summary would be something like "Tidy up utility functions for quadratic forms", but I'll leave that to you as it is your patch.

By the way, the extend_to_primitive() function will be extremely useful too, and I would like to see it mvoed to somewhere like matrix/matrix_integer_dense.pyx (where smith_form is) but I thought I had wreaked enough havoc as it was.

Any comment from mvngu who did the original refereeing?



---

archive/issue_comments_043940.json:
```json
{
    "body": "Replying to [comment:7 cremona]: \n> Any comment from mvngu who did the original refereeing?\n\n\nIt looks like this ticket has reached a stage where it's more difficult to merge, as is the case with #545, although not as difficult. The original idea was to fix a typo and add some test cases. Since cremona now adds more quadratic forms stuff, I don't feel confident to review the technical maths content of his patch. Further enhancements should have been addressed in another ticket, where it would be easier to review and merge. Some quadratic forms experts to the rescue? :-)",
    "created_at": "2009-04-17T02:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43940",
    "user": "mvngu"
}
```

Replying to [comment:7 cremona]: 
> Any comment from mvngu who did the original refereeing?


It looks like this ticket has reached a stage where it's more difficult to merge, as is the case with #545, although not as difficult. The original idea was to fix a typo and add some test cases. Since cremona now adds more quadratic forms stuff, I don't feel confident to review the technical maths content of his patch. Further enhancements should have been addressed in another ticket, where it would be easier to review and merge. Some quadratic forms experts to the rescue? :-)



---

archive/issue_comments_043941.json:
```json
{
    "body": "OK, this is all my fault.  the original patches which fix the typo should be allowed to go ahead.  I will open a different ticket to do the thinks which my patch does, called something like \"Move useful algebraic utilities out of the quadratic forms module\".\n\nUpshot: merge the first two patches ONLY.  On that basis I have retagged this \"positive review\".",
    "created_at": "2009-04-17T08:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43941",
    "user": "cremona"
}
```

OK, this is all my fault.  the original patches which fix the typo should be allowed to go ahead.  I will open a different ticket to do the thinks which my patch does, called something like "Move useful algebraic utilities out of the quadratic forms module".

Upshot: merge the first two patches ONLY.  On that basis I have retagged this "positive review".



---

archive/issue_comments_043942.json:
```json
{
    "body": "John,\n\ncan you please open another patch for the issues you observed and attach the patch at the new ticket? I will then delete the patch here.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-19T02:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43942",
    "user": "mabshoff"
}
```

John,

can you please open another patch for the issues you observed and attach the patch at the new ticket? I will then delete the patch here.

Cheers,

Michael



---

archive/issue_comments_043943.json:
```json
{
    "body": "Replying to [comment:10 mabshoff]:\n> John,\n> \n> can you please open another patch for the issues you observed and attach the patch at the new ticket? I will then delete the patch here.\n\nDone at #5834.  The patch there is the same as the 3rd one here (rebased and checked), and it relies on the first two patches here being applied first.  The third patch here can now be deleted.\n\nNext time I feel inspired to do something similar I'll do so in a new ticket in the first place.\n\n> \n> Cheers,\n> \n> Michael",
    "created_at": "2009-04-20T10:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43943",
    "user": "cremona"
}
```

Replying to [comment:10 mabshoff]:
> John,
> 
> can you please open another patch for the issues you observed and attach the patch at the new ticket? I will then delete the patch here.

Done at #5834.  The patch there is the same as the 3rd one here (rebased and checked), and it relies on the first two patches here being applied first.  The third patch here can now be deleted.

Next time I feel inspired to do something similar I'll do so in a new ticket in the first place.

> 
> Cheers,
> 
> Michael



---

archive/issue_comments_043944.json:
```json
{
    "body": "Merged both patches in Sage 3.4.2.alpha0.\n\nJohn: This is touching quadratic forms code, so I am CCing you. You really ought to get rid of the \"Oops!\" bit when throwing exceptions :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T09:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43944",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.2.alpha0.

John: This is touching quadratic forms code, so I am CCing you. You really ought to get rid of the "Oops!" bit when throwing exceptions :)

Cheers,

Michael



---

archive/issue_comments_043945.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T09:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43945",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043946.json:
```json
{
    "body": "Replying to [comment:12 mabshoff]:\n> Merged both patches in Sage 3.4.2.alpha0.\n> \n> John: This is touching quadratic forms code, so I am CCing you. You really ought to get rid of the \"Oops!\" bit when throwing exceptions :)\n> \n> Cheers,\n> \n> Michael\n\nThey were not my \"oops\"s, and I agree with you.  I just did not remove them.  If we do this now with a new ticket/ patch then it will interfere with #5834 but I think I could live with that.",
    "created_at": "2009-04-24T10:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43946",
    "user": "cremona"
}
```

Replying to [comment:12 mabshoff]:
> Merged both patches in Sage 3.4.2.alpha0.
> 
> John: This is touching quadratic forms code, so I am CCing you. You really ought to get rid of the "Oops!" bit when throwing exceptions :)
> 
> Cheers,
> 
> Michael

They were not my "oops"s, and I agree with you.  I just did not remove them.  If we do this now with a new ticket/ patch then it will interfere with #5834 but I think I could live with that.



---

archive/issue_comments_043947.json:
```json
{
    "body": "Replying to [comment:13 cremona]:\n\n> They were not my \"oops\"s, and I agree with you.  I just did not remove them.  If we do this now with a new ticket/ patch then it will interfere with #5834 but I think I could live with that.\n\nSorry John, I meant to alert Jon Hanke (But I misspelled his name :(). Jon Hanke is supposed to get coverage up to 100% for the quadratic forms code by the end of the month, so I wanted him to be aware of all patches that touch quadratic forms. We might still get #5834 in before that happens, so we will see. So far there is no patch from Jon to merge AFAIK :(\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T10:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5627#issuecomment-43947",
    "user": "mabshoff"
}
```

Replying to [comment:13 cremona]:

> They were not my "oops"s, and I agree with you.  I just did not remove them.  If we do this now with a new ticket/ patch then it will interfere with #5834 but I think I could live with that.

Sorry John, I meant to alert Jon Hanke (But I misspelled his name :(). Jon Hanke is supposed to get coverage up to 100% for the quadratic forms code by the end of the month, so I wanted him to be aware of all patches that touch quadratic forms. We might still get #5834 in before that happens, so we will see. So far there is no patch from Jon to merge AFAIK :(

Cheers,

Michael
