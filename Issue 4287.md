# Issue 4287: [with patch, needs review] improve elliptic curve doctest (part 5)

archive/issues_004287.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb\n\nThis is for the file formal_group.py. Note that adding a s == loads(dumps(s)) test revealed a\nfailure:\n\n```\nsage: E = EllipticCurve('11a')\nsage: F = E.formal_group()\nsage: F == loads(dumps(F))\nFalse\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4287\n\n",
    "created_at": "2008-10-14T19:58:56Z",
    "labels": [
        "component: algebraic geometry",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, needs review] improve elliptic curve doctest (part 5)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4287",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @williamstein

CC:  @robertwb

This is for the file formal_group.py. Note that adding a s == loads(dumps(s)) test revealed a
failure:

```
sage: E = EllipticCurve('11a')
sage: F = E.formal_group()
sage: F == loads(dumps(F))
False
```


Issue created by migration from https://trac.sagemath.org/ticket/4287





---

archive/issue_comments_031316.json:
```json
{
    "body": "Attachment [trac_4287.patch](tarball://root/attachments/some-uuid/ticket4287/trac_4287.patch) by @zimmermann6 created at 2008-10-14 20:00:19",
    "created_at": "2008-10-14T20:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4287#issuecomment-31316",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_4287.patch](tarball://root/attachments/some-uuid/ticket4287/trac_4287.patch) by @zimmermann6 created at 2008-10-14 20:00:19



---

archive/issue_comments_031317.json:
```json
{
    "body": "Patch looks good and applies ok.  But as Paul says, we need to see why load(dumps(F))!=F for a formal group F.\n\nI don't know how to fix this.",
    "created_at": "2008-10-19T20:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4287#issuecomment-31317",
    "user": "https://github.com/JohnCremona"
}
```

Patch looks good and applies ok.  But as Paul says, we need to see why load(dumps(F))!=F for a formal group F.

I don't know how to fix this.



---

archive/issue_comments_031318.json:
```json
{
    "body": "Attachment [trac_4287_2.patch](tarball://root/attachments/some-uuid/ticket4287/trac_4287_2.patch) by @JohnCremona created at 2008-10-19 21:02:46",
    "created_at": "2008-10-19T21:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4287#issuecomment-31318",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_4287_2.patch](tarball://root/attachments/some-uuid/ticket4287/trac_4287_2.patch) by @JohnCremona created at 2008-10-19 21:02:46



---

archive/issue_comments_031319.json:
```json
{
    "body": "Replying to [comment:1 cremona]:\n> Patch looks good and applies ok.  But as Paul says, we need to see why load(dumps(F))!=F for a formal group F.\n> \n> I don't know how to fix this.\n\nI didn't know, but now I do.  There was nothing wrong with loads() or dumps() for formal groups, but they were missing a _cmp_ function so the \"==\" comparison was not giving the expected answer.\nThe second patch (modelled on a similar one by robertwb for ell_tate_curve.py) seems to do the trick.  All tests pass in elliptic_curves.",
    "created_at": "2008-10-19T21:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4287#issuecomment-31319",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:1 cremona]:
> Patch looks good and applies ok.  But as Paul says, we need to see why load(dumps(F))!=F for a formal group F.
> 
> I don't know how to fix this.

I didn't know, but now I do.  There was nothing wrong with loads() or dumps() for formal groups, but they were missing a _cmp_ function so the "==" comparison was not giving the expected answer.
The second patch (modelled on a similar one by robertwb for ell_tate_curve.py) seems to do the trick.  All tests pass in elliptic_curves.



---

archive/issue_comments_031320.json:
```json
{
    "body": "Robert (robertwb), I CC'd you on this hoping that you could say that I fixed this appropriately?  I was using a similar patch of yours as a model.  John",
    "created_at": "2008-10-21T20:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4287#issuecomment-31320",
    "user": "https://github.com/JohnCremona"
}
```

Robert (robertwb), I CC'd you on this hoping that you could say that I fixed this appropriately?  I was using a similar patch of yours as a model.  John



---

archive/issue_comments_031321.json:
```json
{
    "body": "Yes, that looks good to me. (As does the other patch--though I only read it at SD 10, I didn't actually try it out yet).",
    "created_at": "2008-10-22T14:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4287#issuecomment-31321",
    "user": "https://github.com/robertwb"
}
```

Yes, that looks good to me. (As does the other patch--though I only read it at SD 10, I didn't actually try it out yet).



---

archive/issue_comments_031322.json:
```json
{
    "body": "The two patches look good and apply cleanly against my 3.2.",
    "created_at": "2008-11-22T07:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4287#issuecomment-31322",
    "user": "https://github.com/aghitza"
}
```

The two patches look good and apply cleanly against my 3.2.



---

archive/issue_comments_031323.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-23T07:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4287#issuecomment-31323",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_comments_031324.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-23T07:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4287#issuecomment-31324",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
