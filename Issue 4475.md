# Issue 4475: create a native Sage implementation of Dokchitser's L-functions algorithm

archive/issues_004475.json:
```json
{
    "body": "Assignee: was\n\nSee http://wiki.sagemath.org/days11/projects for now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4475\n\n",
    "created_at": "2008-11-09T04:26:47Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "create a native Sage implementation of Dokchitser's L-functions algorithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4475",
    "user": "was"
}
```
Assignee: was

See http://wiki.sagemath.org/days11/projects for now.

Issue created by migration from https://trac.sagemath.org/ticket/4475





---

archive/issue_comments_033049.json:
```json
{
    "body": "Attachment\n\nfirst very preliminary version",
    "created_at": "2008-11-09T04:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-33049",
    "user": "was"
}
```

Attachment

first very preliminary version



---

archive/issue_comments_033050.json:
```json
{
    "body": "Jen's original code which this work is based on was at #2568. Obviously Jen should get partial credit once the code from this ticket has been merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-09T06:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-33050",
    "user": "mabshoff"
}
```

Jen's original code which this work is based on was at #2568. Obviously Jen should get partial credit once the code from this ticket has been merged.

Cheers,

Michael



---

archive/issue_comments_033051.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-09T10:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-33051",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_033052.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-18T00:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-33052",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_033053.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-18T09:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-33053",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_033054.json:
```json
{
    "body": "Attachment\n\nI attached a wrapping of the G_s(t) terms, and got it working (at least it computes the Riemann zeta function correctly). There is an off-by-one typo in formula (10) of the paper (the computation of the poles should be `rj k!/(pj - s)^(k+1)`). However, this fix still didn't give the right answer so I examined Dokchister's code and he has an extra summation over the poles (very last function of computel.gp) and I couldn't figure out where that was coming from. \n\nThe weight and the exponential factor are used for calculating the intermediate precision/number of terms needed in the various series related to computing G_s(t), which turns out to be the bulk of the work of `initLdata`, so it made things a lot cleaner to simply call that function for now. \n\nIt should be noted that to compute the value at s it may be necessary to compute the power series at s and then evaluate to let the poles and zeros of the gamma factor cancel out poles/zeros of L* appropriately.",
    "created_at": "2008-11-18T10:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-33054",
    "user": "robertwb"
}
```

Attachment

I attached a wrapping of the G_s(t) terms, and got it working (at least it computes the Riemann zeta function correctly). There is an off-by-one typo in formula (10) of the paper (the computation of the poles should be `rj k!/(pj - s)^(k+1)`). However, this fix still didn't give the right answer so I examined Dokchister's code and he has an extra summation over the poles (very last function of computel.gp) and I couldn't figure out where that was coming from. 

The weight and the exponential factor are used for calculating the intermediate precision/number of terms needed in the various series related to computing G_s(t), which turns out to be the bulk of the work of `initLdata`, so it made things a lot cleaner to simply call that function for now. 

It should be noted that to compute the value at s it may be necessary to compute the power series at s and then evaluate to let the poles and zeros of the gamma factor cancel out poles/zeros of L* appropriately.



---

archive/issue_comments_033055.json:
```json
{
    "body": "Attachment\n\n(Partial) native implementation of the G function.",
    "created_at": "2008-12-20T05:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-33055",
    "user": "robertwb"
}
```

Attachment

(Partial) native implementation of the G function.
