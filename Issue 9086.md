# Issue 9086: LaTeX representation of negative symbolic fractions broken

archive/issues_009086.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: symbolic fraction, sign, minus, latex\n\nWhen the numerator of a (negative) symbolic expression happens to be `1` (and only then), the sign is dropped in its LaTeX representation (but not its string representation):\n\n\n```\nsage: latex(-1/x)\n\\frac{1}{x}\nsage: latex(1/-x) \n\\frac{1}{x}\n```\n\n\nOrigin of the new doctest failure in `sage/graphs/generic_graphy.py`, introduced with Sage 4.4.3.alpha0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9086\n\n",
    "created_at": "2010-05-29T18:44:54Z",
    "labels": [
        "symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "LaTeX representation of negative symbolic fractions broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9086",
    "user": "@nexttime"
}
```
Assignee: @burcin

Keywords: symbolic fraction, sign, minus, latex

When the numerator of a (negative) symbolic expression happens to be `1` (and only then), the sign is dropped in its LaTeX representation (but not its string representation):


```
sage: latex(-1/x)
\frac{1}{x}
sage: latex(1/-x) 
\frac{1}{x}
```


Origin of the new doctest failure in `sage/graphs/generic_graphy.py`, introduced with Sage 4.4.3.alpha0.

Issue created by migration from https://trac.sagemath.org/ticket/9086





---

archive/issue_comments_084367.json:
```json
{
    "body": "Changing keywords from \"symbolic fraction, sign, minus, latex\" to \"symbolic fraction, sign, minus, latex, pynac\".",
    "created_at": "2010-05-29T18:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84367",
    "user": "@burcin"
}
```

Changing keywords from "symbolic fraction, sign, minus, latex" to "symbolic fraction, sign, minus, latex, pynac".



---

archive/issue_comments_084368.json:
```json
{
    "body": "Thanks for tracking this down. This patch is the culprit:\n\nhttp://pynac.sagemath.org/hg/rev/cbd65a7dcf6a\n\n\nI will only be able to look at this after next weekend.",
    "created_at": "2010-05-29T18:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84368",
    "user": "@burcin"
}
```

Thanks for tracking this down. This patch is the culprit:

http://pynac.sagemath.org/hg/rev/cbd65a7dcf6a


I will only be able to look at this after next weekend.



---

archive/issue_comments_084369.json:
```json
{
    "body": "Attachment [trac_9086.patch](tarball://root/attachments/some-uuid/ticket9086/trac_9086.patch) by @williamstein created at 2010-06-03 01:25:17\n\napply to sage library",
    "created_at": "2010-06-03T01:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84369",
    "user": "@williamstein"
}
```

Attachment [trac_9086.patch](tarball://root/attachments/some-uuid/ticket9086/trac_9086.patch) by @williamstein created at 2010-06-03 01:25:17

apply to sage library



---

archive/issue_comments_084370.json:
```json
{
    "body": "Attachment [trac_9086-apply_to_pynac.patch](tarball://root/attachments/some-uuid/ticket9086/trac_9086-apply_to_pynac.patch) by @williamstein created at 2010-06-03 01:25:34\n\napply to src/ repo in pynac spkg",
    "created_at": "2010-06-03T01:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84370",
    "user": "@williamstein"
}
```

Attachment [trac_9086-apply_to_pynac.patch](tarball://root/attachments/some-uuid/ticket9086/trac_9086-apply_to_pynac.patch) by @williamstein created at 2010-06-03 01:25:34

apply to src/ repo in pynac spkg



---

archive/issue_comments_084371.json:
```json
{
    "body": "The patch to the pynac spkg is long, but is logically nearly trivial.  I just copied some code for printing a sign, which Burcin forgot.\n\nThe patch to the sage library is merely to test that this is fixed. \n\nWilliam",
    "created_at": "2010-06-03T01:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84371",
    "user": "@williamstein"
}
```

The patch to the pynac spkg is long, but is logically nearly trivial.  I just copied some code for printing a sign, which Burcin forgot.

The patch to the sage library is merely to test that this is fixed. 

William



---

archive/issue_comments_084372.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-03T01:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84372",
    "user": "@williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084373.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-06-03T01:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84373",
    "user": "@williamstein"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_084374.json:
```json
{
    "body": "New spkg here:\n\n   http://sage.math.washington.edu/home/wstein/patches/pynac-0.2.0.p1.spkg",
    "created_at": "2010-06-03T01:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84374",
    "user": "@williamstein"
}
```

New spkg here:

   http://sage.math.washington.edu/home/wstein/patches/pynac-0.2.0.p1.spkg



---

archive/issue_comments_084375.json:
```json
{
    "body": "This looks good to me and fixes the issue.  There was a change for #9037 that didn't get included in the spkg merged so far in 4.4.3 so I've included it at \n\nhttp://sage.math.washington.edu/home/mhansen/pynac-0.2.0.p1.spkg\n\nwhich should be used instead of the above link.",
    "created_at": "2010-06-03T01:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84375",
    "user": "@mwhansen"
}
```

This looks good to me and fixes the issue.  There was a change for #9037 that didn't get included in the spkg merged so far in 4.4.3 so I've included it at 

http://sage.math.washington.edu/home/mhansen/pynac-0.2.0.p1.spkg

which should be used instead of the above link.



---

archive/issue_comments_084376.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-03T01:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84376",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084377.json:
```json
{
    "body": "Mike, Can you give #9037 a positive review?",
    "created_at": "2010-06-03T04:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84377",
    "user": "@williamstein"
}
```

Mike, Can you give #9037 a positive review?



---

archive/issue_comments_084378.json:
```json
{
    "body": "Positive review up at #9037.",
    "created_at": "2010-06-03T04:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84378",
    "user": "@mwhansen"
}
```

Positive review up at #9037.



---

archive/issue_comments_084379.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-03T16:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84379",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_084380.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-06-21T20:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84380",
    "user": "damm"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_084381.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-06-21T20:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84381",
    "user": "damm"
}
```

Changing status from closed to new.



---

archive/issue_comments_084382.json:
```json
{
    "body": "Replying to [comment:10 damm]:\nSorry, i've changed the description and couldn't revert the change.\n\nI think the fix didn't solve all problems:\n\n\n```\nsage: var('x y')\nsage: latex(-x/y) \n\\frac{x}{y}\n```\n",
    "created_at": "2010-06-21T20:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84382",
    "user": "damm"
}
```

Replying to [comment:10 damm]:
Sorry, i've changed the description and couldn't revert the change.

I think the fix didn't solve all problems:


```
sage: var('x y')
sage: latex(-x/y) 
\frac{x}{y}
```




---

archive/issue_comments_084383.json:
```json
{
    "body": "Replying to [comment:12 damm]:\n> I think the fix didn't solve all problems\n\nIndeed. Despite the ticket's name, I think this second case should be addressed on another ticket, since this one had already been merged.",
    "created_at": "2010-06-22T16:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84383",
    "user": "@nexttime"
}
```

Replying to [comment:12 damm]:
> I think the fix didn't solve all problems

Indeed. Despite the ticket's name, I think this second case should be addressed on another ticket, since this one had already been merged.



---

archive/issue_comments_084384.json:
```json
{
    "body": "Done. http://trac.sagemath.org/sage_trac/ticket/9314",
    "created_at": "2010-06-22T18:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84384",
    "user": "damm"
}
```

Done. http://trac.sagemath.org/sage_trac/ticket/9314



---

archive/issue_comments_084385.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-22T18:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84385",
    "user": "@nexttime"
}
```

Resolution: fixed
