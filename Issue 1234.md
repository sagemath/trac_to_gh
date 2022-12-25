# Issue 1234: analytic_rank crashes

archive/issues_001234.json:
```json
{
    "body": "Assignee: @williamstein\n\nMaybe the following is not feasible, but analytic_rank could crash smoothly.\n\n\n```\nsage: d=100032426715415089/251987961355200625\nsage: E = EllipticCurve([0, -d^3+5*d^2, 0, -8*d^5+8*d^4, 4*d^8-8*d^7+4*d^6])\nsage: F = E.minimal_model()\nsage: F.analytic_rank(algorithm='cremona')\n<type 'exceptions.RuntimeError'>: Error: '  *** elltors: precision too low in torsell.\n\nsage: F.analytic_rank(algorithm='rubinstein')\n<type 'exceptions.TypeError'>: unable to convert x (= 6.90579e+20 and is too large) to an integer\n\nsage: F.analytic_rank(algorithm='sympow')\nsympow 1.018 RELEASE  (c) Mark Watkins --- see README and COPYING for details\n**ERROR** c4 invariant is too large\n```\n\n\nFrom John Cremona: the \"cremona\" version just wraps a gp script, which\nneeds to have sufficient precision even for ellinit() to work ok here.\nUnfortunately this call will run in its own gp session, and it is not\npossible for the user to set the precision.  (I found the same while\nrunning a lot of examples through Denis Simon's gp scripts).  The\nsolution is to change the wrapper to have a precision parameter, with\nsome reasonable default for backwards compatibility, which gets passes\nthrough to gp.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1234\n\n",
    "created_at": "2007-11-21T14:04:25Z",
    "labels": [
        "component: algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "analytic_rank crashes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1234",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @williamstein

Maybe the following is not feasible, but analytic_rank could crash smoothly.


```
sage: d=100032426715415089/251987961355200625
sage: E = EllipticCurve([0, -d^3+5*d^2, 0, -8*d^5+8*d^4, 4*d^8-8*d^7+4*d^6])
sage: F = E.minimal_model()
sage: F.analytic_rank(algorithm='cremona')
<type 'exceptions.RuntimeError'>: Error: '  *** elltors: precision too low in torsell.

sage: F.analytic_rank(algorithm='rubinstein')
<type 'exceptions.TypeError'>: unable to convert x (= 6.90579e+20 and is too large) to an integer

sage: F.analytic_rank(algorithm='sympow')
sympow 1.018 RELEASE  (c) Mark Watkins --- see README and COPYING for details
**ERROR** c4 invariant is too large
```


From John Cremona: the "cremona" version just wraps a gp script, which
needs to have sufficient precision even for ellinit() to work ok here.
Unfortunately this call will run in its own gp session, and it is not
possible for the user to set the precision.  (I found the same while
running a lot of examples through Denis Simon's gp scripts).  The
solution is to change the wrapper to have a precision parameter, with
some reasonable default for backwards compatibility, which gets passes
through to gp.


Issue created by migration from https://trac.sagemath.org/ticket/1234





---

archive/issue_comments_007670.json:
```json
{
    "body": "NB I think that all functions which wrap gp scripts should have the ability to set various gp defaults before the scripts are run.  Notably the real precision (which is the culprit above), but also in other cases.\n\nThis should be easy but tedious -- is there anywhere a list of which functions operate by running a gp script?\n\njec",
    "created_at": "2007-11-21T14:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7670",
    "user": "https://github.com/JohnCremona"
}
```

NB I think that all functions which wrap gp scripts should have the ability to set various gp defaults before the scripts are run.  Notably the real precision (which is the culprit above), but also in other cases.

This should be easy but tedious -- is there anywhere a list of which functions operate by running a gp script?

jec



---

archive/issue_comments_007671.json:
```json
{
    "body": "Still an issue with Sage 2.10.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T22:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Still an issue with Sage 2.10.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_007672.json:
```json
{
    "body": "I can only speak for the first of these, begin responsible for the gp script which computes analytic rank.\n\nThis curve has conductor N=690579402364042119390 which is vastly too big for the analytic rank algorithm anyway (it requires the computation of O(sqrt(N)) terms of the L-series).\n\nAlso relevant here is that my analytic rank gp code is *old*.  When Magma adopted it, it was vastly improved (by Mark Watkins), which means that for several years I have not used my own gp program at all, let alone developed it.  For this curve, I don't think even Magma would succeed in computing its analytic rank.",
    "created_at": "2008-02-16T10:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7672",
    "user": "https://github.com/JohnCremona"
}
```

I can only speak for the first of these, begin responsible for the gp script which computes analytic rank.

This curve has conductor N=690579402364042119390 which is vastly too big for the analytic rank algorithm anyway (it requires the computation of O(sqrt(N)) terms of the L-series).

Also relevant here is that my analytic rank gp code is *old*.  When Magma adopted it, it was vastly improved (by Mark Watkins), which means that for several years I have not used my own gp program at all, let alone developed it.  For this curve, I don't think even Magma would succeed in computing its analytic rank.



---

archive/issue_comments_007673.json:
```json
{
    "body": "What shall we do about this ticket?\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-06-26T06:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7673",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What shall we do about this ticket?

Thoughts?

Cheers,

Michael



---

archive/issue_comments_007674.json:
```json
{
    "body": "Replying to [comment:5 mabshoff]:\n> What shall we do about this ticket?\n> \n> Thoughts?\n> \n> Cheers,\n> \n> Michael\n\nGiven the fundamental problem that computing the analytic rank increases rapidly with the conductor N (I think it is sqrt(N)), one solution would be to impose a (carefully-chosen but necessarily somewhat arbitrary) cutoff N_max, so that asking for the analytic rank of a curve of conductor>N_max would result in an error.\n\nOne way to implement this would be to have N_max a parameter to the analytic rank function, with a default value of (say) `10^6` or `10^7`.  (I would have to do some experiments to decide on a sensible value).  The docstring could explain that the user is allowed to increase this but warn that it may take (effectively) for ever.",
    "created_at": "2008-06-26T08:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7674",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:5 mabshoff]:
> What shall we do about this ticket?
> 
> Thoughts?
> 
> Cheers,
> 
> Michael

Given the fundamental problem that computing the analytic rank increases rapidly with the conductor N (I think it is sqrt(N)), one solution would be to impose a (carefully-chosen but necessarily somewhat arbitrary) cutoff N_max, so that asking for the analytic rank of a curve of conductor>N_max would result in an error.

One way to implement this would be to have N_max a parameter to the analytic rank function, with a default value of (say) `10^6` or `10^7`.  (I would have to do some experiments to decide on a sensible value).  The docstring could explain that the user is allowed to increase this but warn that it may take (effectively) for ever.



---

archive/issue_comments_007675.json:
```json
{
    "body": "PS The vale of N_max would presumably be different for the different algorithms supported (sympow, lcalc, etc).  I was only thing of the \"cremona\" algorithm.  I also note that the docstring claims that lcalc is the most efficient, but cremona is the default -- that was not my decision!",
    "created_at": "2008-06-26T08:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7675",
    "user": "https://github.com/JohnCremona"
}
```

PS The vale of N_max would presumably be different for the different algorithms supported (sympow, lcalc, etc).  I was only thing of the "cremona" algorithm.  I also note that the docstring claims that lcalc is the most efficient, but cremona is the default -- that was not my decision!



---

archive/issue_comments_007676.json:
```json
{
    "body": "Attachment [trac_1234.patch](tarball://root/attachments/some-uuid/ticket1234/trac_1234.patch) by @williamstein created at 2009-01-22 08:20:11",
    "created_at": "2009-01-22T08:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7676",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_1234.patch](tarball://root/attachments/some-uuid/ticket1234/trac_1234.patch) by @williamstein created at 2009-01-22 08:20:11



---

archive/issue_comments_007677.json:
```json
{
    "body": "The attached patch cleans up the exceptions raised, as requested.  Also, in the (default) case where Cremona's gp script is used, the precision is automatically doubled until it doesn't fail.  I also start the precision at 16 rather than the default, since it will get automatically double if necessary, and it's about 3 times faster usually by using this smaller precision to start:\n\n\n```\nBEFORE:\nsage: E = EllipticCurve('5077a')\nsage: time E.analytic_rank()\nCPU times: user 0.01 s, sys: 0.01 s, total: 0.02 s\nWall time: 0.21 s\n\n\nAFTER:\nsage: E = EllipticCurve('5077a')\nsage: time E.analytic_rank()\nCPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s\nWall time: 0.06 s\n\n\nand another\n\nBEFORE:\nsage: time elliptic_curves.rank(4)[0].analytic_rank()\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.50 s\n4\n\nAFTER:\nsage: time elliptic_curves.rank(4)[0].analytic_rank()\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.33 s\n4\n```\n",
    "created_at": "2009-01-22T08:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7677",
    "user": "https://github.com/williamstein"
}
```

The attached patch cleans up the exceptions raised, as requested.  Also, in the (default) case where Cremona's gp script is used, the precision is automatically doubled until it doesn't fail.  I also start the precision at 16 rather than the default, since it will get automatically double if necessary, and it's about 3 times faster usually by using this smaller precision to start:


```
BEFORE:
sage: E = EllipticCurve('5077a')
sage: time E.analytic_rank()
CPU times: user 0.01 s, sys: 0.01 s, total: 0.02 s
Wall time: 0.21 s


AFTER:
sage: E = EllipticCurve('5077a')
sage: time E.analytic_rank()
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.06 s


and another

BEFORE:
sage: time elliptic_curves.rank(4)[0].analytic_rank()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.50 s
4

AFTER:
sage: time elliptic_curves.rank(4)[0].analytic_rank()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.33 s
4
```




---

archive/issue_comments_007678.json:
```json
{
    "body": "Review:  excellent and well done.  Applies cleanly to 3.3.alpha0 and all tests in elliptic_curves pass.\n\nSuggestion:  I see that for EllipticCurve([1234567,89101112]) which has conductor 61928339435779485920, sympow and rubinstein know they are beaten and quit, while cremona just takes a long time (I did not wait).  It might be a good idea to work out a sensible conductor limit for my gp script and have sage only call the script if under that (perhaps with a parameter to allow users to override it).  But that would depend on many factors (speed of machine etc), and this patch should not be delayed because of that.\n\nPass!",
    "created_at": "2009-01-22T09:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7678",
    "user": "https://github.com/JohnCremona"
}
```

Review:  excellent and well done.  Applies cleanly to 3.3.alpha0 and all tests in elliptic_curves pass.

Suggestion:  I see that for EllipticCurve([1234567,89101112]) which has conductor 61928339435779485920, sympow and rubinstein know they are beaten and quit, while cremona just takes a long time (I did not wait).  It might be a good idea to work out a sensible conductor limit for my gp script and have sage only call the script if under that (perhaps with a parameter to allow users to override it).  But that would depend on many factors (speed of machine etc), and this patch should not be delayed because of that.

Pass!



---

archive/issue_comments_007679.json:
```json
{
    "body": "I also was testing the patch, but John was faster than me. Just a comment: it would be better to capitalize\npeople names (rubinstein -> Rubinstein, weierstrass -> Weierstrass), at least in the documentation\n(for the options, it might involve too much work).",
    "created_at": "2009-01-22T09:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7679",
    "user": "https://github.com/zimmermann6"
}
```

I also was testing the patch, but John was faster than me. Just a comment: it would be better to capitalize
people names (rubinstein -> Rubinstein, weierstrass -> Weierstrass), at least in the documentation
(for the options, it might involve too much work).



---

archive/issue_comments_007680.json:
```json
{
    "body": "Replying to [comment:10 zimmerma]:\n> I also was testing the patch, but John was faster than me. Just a comment: it would be better to capitalize\n> people names (rubinstein -> Rubinstein, weierstrass -> Weierstrass), at least in the documentation\n> (for the options, it might involve too much work).\n\nI agree with capitalization in documentation;  for parameters it would probably be best to allow either.",
    "created_at": "2009-01-22T10:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7680",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:10 zimmerma]:
> I also was testing the patch, but John was faster than me. Just a comment: it would be better to capitalize
> people names (rubinstein -> Rubinstein, weierstrass -> Weierstrass), at least in the documentation
> (for the options, it might involve too much work).

I agree with capitalization in documentation;  for parameters it would probably be best to allow either.



---

archive/issue_comments_007681.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7681",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1

Cheers,

Michael



---

archive/issue_events_001372.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-23T10:26:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1234#event-1372"
}
```



---

archive/issue_comments_007682.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T10:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1234#issuecomment-7682",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
