# Issue 1188: unexpected results after LLL?

archive/issues_001188.json:
```json
{
    "body": "Assignee: @williamstein\n\nConsider this example from the Magma handbook:\n\n```\n# n integers which's GCD we are interested in\nsage: Q = [ 67015143, 248934363018, 109210, 25590011055, 74631449, 10230248, 709487, 68965012139, 972065, 864972271 ]\nsage: n = len(Q)\nsage: S = 100 \nsage: X = Matrix(IntegerRing(), n, n + 1)\nsage: for i in xrange(n):\n...     X[i,i + 1] = 1\nsage: for i in xrange(n): \n...     X[i,0] = S*Q[i]\nsage: L = X.LLL()\nsage: show(L)\nsage: M = L[n-1].list()[1:]\nsage: add([Q[i]*M[i] for i in range(n)])\n864972271\n```\n\n\nwhich isn't quite right, we expect:\n\n```\n# n integers which's GCD we are interested in\nsage: Q = [ 67015143, 248934363018, 109210, 25590011055, 74631449, 10230248, 709487, 68965012139, 972065, 864972271 ]\nsage: n = len(Q)\nsage: S = 100 \nsage: X = Matrix(IntegerRing(), n, n + 1)\nsage: for i in xrange(n):\n...     X[i,i + 1] = 1\nsage: for i in xrange(n): \n...     X[i,0] = S*Q[i]\nsage: L = X.LLL(algorithm='NTL:LLL')\nsage: show(L)\nsage: M = L[n-1].list()[1:]\nsage: add([Q[i]*M[i] for i in range(n)])\n-1\n```\n\n\nIs this my lack of understanding of LLL reduction or is this a bug?\n\nIssue created by migration from https://trac.sagemath.org/ticket/1188\n\n",
    "created_at": "2007-11-16T21:48:40Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "unexpected results after LLL?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1188",
    "user": "@malb"
}
```
Assignee: @williamstein

Consider this example from the Magma handbook:

```
# n integers which's GCD we are interested in
sage: Q = [ 67015143, 248934363018, 109210, 25590011055, 74631449, 10230248, 709487, 68965012139, 972065, 864972271 ]
sage: n = len(Q)
sage: S = 100 
sage: X = Matrix(IntegerRing(), n, n + 1)
sage: for i in xrange(n):
...     X[i,i + 1] = 1
sage: for i in xrange(n): 
...     X[i,0] = S*Q[i]
sage: L = X.LLL()
sage: show(L)
sage: M = L[n-1].list()[1:]
sage: add([Q[i]*M[i] for i in range(n)])
864972271
```


which isn't quite right, we expect:

```
# n integers which's GCD we are interested in
sage: Q = [ 67015143, 248934363018, 109210, 25590011055, 74631449, 10230248, 709487, 68965012139, 972065, 864972271 ]
sage: n = len(Q)
sage: S = 100 
sage: X = Matrix(IntegerRing(), n, n + 1)
sage: for i in xrange(n):
...     X[i,i + 1] = 1
sage: for i in xrange(n): 
...     X[i,0] = S*Q[i]
sage: L = X.LLL(algorithm='NTL:LLL')
sage: show(L)
sage: M = L[n-1].list()[1:]
sage: add([Q[i]*M[i] for i in range(n)])
-1
```


Is this my lack of understanding of LLL reduction or is this a bug?

Issue created by migration from https://trac.sagemath.org/ticket/1188





---

archive/issue_comments_007337.json:
```json
{
    "body": "I get -1 with both X.LLL() and X.LLL(algorithm='NTL:LLL') on a Pentium M with sage-2.8.12.\nMaybe a processor-specific problem?",
    "created_at": "2007-11-16T22:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7337",
    "user": "@zimmermann6"
}
```

I get -1 with both X.LLL() and X.LLL(algorithm='NTL:LLL') on a Pentium M with sage-2.8.12.
Maybe a processor-specific problem?



---

archive/issue_comments_007338.json:
```json
{
    "body": "My processor is a Core2Duo which I use in 64-bit mode (Debian/testing AMD64). I can also reproduce this bug on sage.math (64-bit Opteron). So I assume this is an issue with 64-bit architectures.",
    "created_at": "2007-11-17T13:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7338",
    "user": "@malb"
}
```

My processor is a Core2Duo which I use in 64-bit mode (Debian/testing AMD64). I can also reproduce this bug on sage.math (64-bit Opteron). So I assume this is an issue with 64-bit architectures.



---

archive/issue_comments_007339.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-17T14:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7339",
    "user": "@malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007340.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-11-17T14:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7340",
    "user": "@malb"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_007341.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2007-11-17T14:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7341",
    "user": "@malb"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_007342.json:
```json
{
    "body": "I upgraded this bug to a blocker as it is a bug which leads to wrong results without raising an error.",
    "created_at": "2007-11-17T14:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7342",
    "user": "@malb"
}
```

I upgraded this bug to a blocker as it is a bug which leads to wrong results without raising an error.



---

archive/issue_comments_007343.json:
```json
{
    "body": "One quick point is at least the result is still a basis for the correct lattice:\n\n\n```\nA = X.row_module()\nB = L.row_module()\nA == B\n///\nTrue\n```\n\n\nso it's returning something that is a basis for the correct lattice.  But maybe it's not LLL reduced. \n\nWe should write a function to determine whether or not a matrix is LLL reduced, i.e., use the LLL criterion, as described in Section 2.6 of Cohen's book. \n\nIf the output isn't LLL reduced, then there is definitely a bug.  \n\nAnyway, I am going to attempt to implement this criterion right now, and see what\nhappens.",
    "created_at": "2007-11-18T20:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7343",
    "user": "@williamstein"
}
```

One quick point is at least the result is still a basis for the correct lattice:


```
A = X.row_module()
B = L.row_module()
A == B
///
True
```


so it's returning something that is a basis for the correct lattice.  But maybe it's not LLL reduced. 

We should write a function to determine whether or not a matrix is LLL reduced, i.e., use the LLL criterion, as described in Section 2.6 of Cohen's book. 

If the output isn't LLL reduced, then there is definitely a bug.  

Anyway, I am going to attempt to implement this criterion right now, and see what
happens.



---

archive/issue_comments_007344.json:
```json
{
    "body": "OK, I wrote a program to compute Gramm-schmidt form, in order to check the LLL criterion.  I tried it on the above output L (I will post this elsewhere when I finish documenting it: http://trac.sagemath.org/sage_trac/ticket/1201).  It is DEFINITELY THE CASE THAT NTL is getting things *wrong* here.  When transforming the rows of L into orthogonal form using LLL a coefficient mu_ij of 68719476736.0213 appears, which is > 1/2, so the resulting matrix is not LLL reduced.  This this is still thus a major blocker.  \n\nOne \"fix\" would be to have it print a big warning no matter what on 64-bit, which\nwould at least allow us to release.  But this really needs to get fixed / understood.",
    "created_at": "2007-11-18T21:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7344",
    "user": "@williamstein"
}
```

OK, I wrote a program to compute Gramm-schmidt form, in order to check the LLL criterion.  I tried it on the above output L (I will post this elsewhere when I finish documenting it: http://trac.sagemath.org/sage_trac/ticket/1201).  It is DEFINITELY THE CASE THAT NTL is getting things *wrong* here.  When transforming the rows of L into orthogonal form using LLL a coefficient mu_ij of 68719476736.0213 appears, which is > 1/2, so the resulting matrix is not LLL reduced.  This this is still thus a major blocker.  

One "fix" would be to have it print a big warning no matter what on 64-bit, which
would at least allow us to release.  But this really needs to get fixed / understood.



---

archive/issue_comments_007345.json:
```json
{
    "body": "Correction to the above comment: fpLLL gets things wrong, not NTL.\n\nCurrently Sage doesn't check the return value of the LLL() calls in fplll.pyx (zero = ok, non-zero = error). When adding that, it turns out that for this example fpLLL itself detects something is wrong.",
    "created_at": "2007-11-19T00:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7345",
    "user": "@wjp"
}
```

Correction to the above comment: fpLLL gets things wrong, not NTL.

Currently Sage doesn't check the return value of the LLL() calls in fplll.pyx (zero = ok, non-zero = error). When adding that, it turns out that for this example fpLLL itself detects something is wrong.



---

archive/issue_comments_007346.json:
```json
{
    "body": "In at least two places, fpLLL was assuming longs and ints were the same size. The patch I'm attaching should fix those. I already e-mailed Damien Stehle about this, too.",
    "created_at": "2007-11-19T02:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7346",
    "user": "@wjp"
}
```

In at least two places, fpLLL was assuming longs and ints were the same size. The patch I'm attaching should fix those. I already e-mailed Damien Stehle about this, too.



---

archive/issue_comments_007347.json:
```json
{
    "body": "fpLLL-2.1.3 64-bit patch",
    "created_at": "2007-11-19T02:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7347",
    "user": "@wjp"
}
```

fpLLL-2.1.3 64-bit patch



---

archive/issue_comments_007348.json:
```json
{
    "body": "Attachment [fplll_64bit.patch](tarball://root/attachments/some-uuid/ticket1188/fplll_64bit.patch) by mabshoff created at 2007-11-19 08:57:57\n\nA new spkg is available at:\n\nhttp://sage.math.washington.edu/home/malb/pkgs/libfplll-2.1.4-20071119.spkg\n\nmalb will add a doctest to verify this issue has really been fixed. Once that is merged we can hopefully close this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-19T08:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7348",
    "user": "mabshoff"
}
```

Attachment [fplll_64bit.patch](tarball://root/attachments/some-uuid/ticket1188/fplll_64bit.patch) by mabshoff created at 2007-11-19 08:57:57

A new spkg is available at:

http://sage.math.washington.edu/home/malb/pkgs/libfplll-2.1.4-20071119.spkg

malb will add a doctest to verify this issue has really been fixed. Once that is merged we can hopefully close this ticket.

Cheers,

Michael



---

archive/issue_comments_007349.json:
```json
{
    "body": "doctests + documentation update",
    "created_at": "2007-11-19T10:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7349",
    "user": "@malb"
}
```

doctests + documentation update



---

archive/issue_comments_007350.json:
```json
{
    "body": "Attachment [fplll.patch](tarball://root/attachments/some-uuid/ticket1188/fplll.patch) by @wjp created at 2007-11-19 11:41:47\n\nmalb: The error codes from LLL() are positive when an error occurs. Attaching an updated (non-hg) patch that replaces the ret < 0 checks by ret != 0.",
    "created_at": "2007-11-19T11:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7350",
    "user": "@wjp"
}
```

Attachment [fplll.patch](tarball://root/attachments/some-uuid/ticket1188/fplll.patch) by @wjp created at 2007-11-19 11:41:47

malb: The error codes from LLL() are positive when an error occurs. Attaching an updated (non-hg) patch that replaces the ret < 0 checks by ret != 0.



---

archive/issue_comments_007351.json:
```json
{
    "body": "Attachment [fplll2.patch](tarball://root/attachments/some-uuid/ticket1188/fplll2.patch) by @wjp created at 2007-11-19 11:42:13\n\nupdated fplll.patch",
    "created_at": "2007-11-19T11:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7351",
    "user": "@wjp"
}
```

Attachment [fplll2.patch](tarball://root/attachments/some-uuid/ticket1188/fplll2.patch) by @wjp created at 2007-11-19 11:42:13

updated fplll.patch



---

archive/issue_comments_007352.json:
```json
{
    "body": "On IRC:\n\n```\n[11:46] <wjp> malb: I slightly updated your fplll patch replacing ret < 0 by ret != 0 since fpLLL returns positive values on error\n[11:46] <malb> I disagree\n[11:46] <malb> are you sure it has to be an error if !=0 ?\n[11:47] <malb> it just returns kappa, doesn't it?\n[11:47] <wjp> only in error case, as far as I can tell\n[11:47] <malb> the example will not work if you test for ret != 0\n[11:47] <malb> i.e. the doctest I just added\n[11:48] <wjp> that's strange; I'll look through the fplll sources again then\n[11:48] <malb> also heuristic may return kappa != 0 because it is not guaranteed to be LLL reduced anyway\n[11:48] <malb> I only superficially scanned the source though\n[11:48] <wjp> hm, so it might not be usable as an error code\n[11:49] <malb> yes, but I am not sure, we could ask Damien?\n```\n",
    "created_at": "2007-11-19T11:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7352",
    "user": "@malb"
}
```

On IRC:

```
[11:46] <wjp> malb: I slightly updated your fplll patch replacing ret < 0 by ret != 0 since fpLLL returns positive values on error
[11:46] <malb> I disagree
[11:46] <malb> are you sure it has to be an error if !=0 ?
[11:47] <malb> it just returns kappa, doesn't it?
[11:47] <wjp> only in error case, as far as I can tell
[11:47] <malb> the example will not work if you test for ret != 0
[11:47] <malb> i.e. the doctest I just added
[11:48] <wjp> that's strange; I'll look through the fplll sources again then
[11:48] <malb> also heuristic may return kappa != 0 because it is not guaranteed to be LLL reduced anyway
[11:48] <malb> I only superficially scanned the source though
[11:48] <wjp> hm, so it might not be usable as an error code
[11:49] <malb> yes, but I am not sure, we could ask Damien?
```




---

archive/issue_comments_007353.json:
```json
{
    "body": "#1188 looks good -- make sure to only apply fplll2.patch instead of fplll.patch.\n\nAnd wow or wow wjp did a great job on that one in multiple ways!",
    "created_at": "2007-11-20T15:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7353",
    "user": "@williamstein"
}
```

#1188 looks good -- make sure to only apply fplll2.patch instead of fplll.patch.

And wow or wow wjp did a great job on that one in multiple ways!



---

archive/issue_comments_007354.json:
```json
{
    "body": "Merged in 2.8.13.rc1. - see #1217 for followup.\n\nI would like to close this ticket. I did apply the doctest.patch and updated to the latest upstream libfplll.spkg that malb provided.",
    "created_at": "2007-11-20T15:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7354",
    "user": "mabshoff"
}
```

Merged in 2.8.13.rc1. - see #1217 for followup.

I would like to close this ticket. I did apply the doctest.patch and updated to the latest upstream libfplll.spkg that malb provided.



---

archive/issue_comments_007355.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-20T15:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1188#issuecomment-7355",
    "user": "mabshoff"
}
```

Resolution: fixed
