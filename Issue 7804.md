# Issue 7804: Move mipCoin and mipGlpk to Sage

archive/issues_007804.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  mvngu\n\nHello !!\n\nThis patches moves the files mipCoin and mipGlpk to Sage. They are currently included in the packages CBC and GLPK and are a lot harder to work on because of this.\n\nThis patch copies them in sage/numerical/ and adds several lines to modules_list so that they will only be compiled if the corresponding packages are installed.\n\nFor the moment, the copies of these files included in the packages will not be removed, in order to preserve backward-compatibility : the users of earlier versions of Sage will then be able to keep using the same packages. \n\n*Only the changes to file modules_list need to be reviewed -- mipCoin and mipGLPK are copies of what is included in the spkg and have already been checked ! This should be a short review :-) *\n\nIssue created by migration from https://trac.sagemath.org/ticket/7804\n\n",
    "created_at": "2010-01-01T13:36:52Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Move mipCoin and mipGlpk to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7804",
    "user": "ncohen"
}
```
Assignee: AlexGhitza

CC:  mvngu

Hello !!

This patches moves the files mipCoin and mipGlpk to Sage. They are currently included in the packages CBC and GLPK and are a lot harder to work on because of this.

This patch copies them in sage/numerical/ and adds several lines to modules_list so that they will only be compiled if the corresponding packages are installed.

For the moment, the copies of these files included in the packages will not be removed, in order to preserve backward-compatibility : the users of earlier versions of Sage will then be able to keep using the same packages. 

*Only the changes to file modules_list need to be reviewed -- mipCoin and mipGLPK are copies of what is included in the spkg and have already been checked ! This should be a short review :-) *

Issue created by migration from https://trac.sagemath.org/ticket/7804





---

archive/issue_comments_067518.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-01T13:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7804#issuecomment-67518",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067519.json:
```json
{
    "body": "Changing component from algebra to numerical.",
    "created_at": "2010-01-01T13:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7804#issuecomment-67519",
    "user": "ncohen"
}
```

Changing component from algebra to numerical.



---

archive/issue_comments_067520.json:
```json
{
    "body": "I was curious and skimmed this patch for ~ 3 minutes and it \"looks good\" (not a positive review -- I didn't test it yet).",
    "created_at": "2010-01-04T17:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7804#issuecomment-67520",
    "user": "was"
}
```

I was curious and skimmed this patch for ~ 3 minutes and it "looks good" (not a positive review -- I didn't test it yet).



---

archive/issue_comments_067521.json:
```json
{
    "body": "Attachment\n\nI just modified it so that it is now independent from the huge changes going on in graph.py. Would it be possible to have this merged to the next release ? It would let me write another speed-up patch now that solve_glpk and solve_cbc are available ;-)\n\nNathann",
    "created_at": "2010-01-11T17:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7804#issuecomment-67521",
    "user": "ncohen"
}
```

Attachment

I just modified it so that it is now independent from the huge changes going on in graph.py. Would it be possible to have this merged to the next release ? It would let me write another speed-up patch now that solve_glpk and solve_cbc are available ;-)

Nathann



---

archive/issue_comments_067522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T11:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7804#issuecomment-67522",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_067523.json:
```json
{
    "body": "positive review",
    "created_at": "2010-01-13T11:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7804#issuecomment-67523",
    "user": "rlm"
}
```

positive review



---

archive/issue_comments_067524.json:
```json
{
    "body": "Yessssssssssss !! :-) Thanks !!!!\n\nNathann",
    "created_at": "2010-01-13T11:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7804#issuecomment-67524",
    "user": "ncohen"
}
```

Yessssssssssss !! :-) Thanks !!!!

Nathann



---

archive/issue_comments_067525.json:
```json
{
    "body": "How did this get a positive review when the new pyx files have no doctests?",
    "created_at": "2010-01-13T22:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7804#issuecomment-67525",
    "user": "jhpalmieri"
}
```

How did this get a positive review when the new pyx files have no doctests?



---

archive/issue_comments_067526.json:
```json
{
    "body": "That's a good point-- I suppose my review was a bit rushed.\n\nNathann,\n\nDo you want to make a separate ticket for making some doctests here, or would you prefer it if I just pull the patch back out?",
    "created_at": "2010-01-13T23:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7804#issuecomment-67526",
    "user": "rlm"
}
```

That's a good point-- I suppose my review was a bit rushed.

Nathann,

Do you want to make a separate ticket for making some doctests here, or would you prefer it if I just pull the patch back out?



---

archive/issue_comments_067527.json:
```json
{
    "body": "see #7925 :-)\n\nBut they will be way harder to write with the spkg GLPK and cbc broken :-/\n\nNathann",
    "created_at": "2010-01-14T06:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7804#issuecomment-67527",
    "user": "ncohen"
}
```

see #7925 :-)

But they will be way harder to write with the spkg GLPK and cbc broken :-/

Nathann
