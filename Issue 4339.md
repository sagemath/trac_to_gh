# Issue 4339: modular forms -- incorporate Nils Skoruppa's code for computing generators for the ring of modular forms of given level

archive/issues_004339.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  nilsskoruppa\n\nCraig has an email from Nils with this code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4339\n\n",
    "created_at": "2008-10-22T17:49:42Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "modular forms -- incorporate Nils Skoruppa's code for computing generators for the ring of modular forms of given level",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4339",
    "user": "was"
}
```
Assignee: craigcitro

CC:  nilsskoruppa

Craig has an email from Nils with this code.

Issue created by migration from https://trac.sagemath.org/ticket/4339





---

archive/issue_comments_031824.json:
```json
{
    "body": "I am adding Nils to the CC here so he is aware of the ticket. IIRC it was also a team effort to write that code, but I could be wrong. Some copy of Nil's code seems to be at\n\nhttp://modular.math.washington.edu/home/ljpk/sage-add-ons/nils/\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T21:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31824",
    "user": "mabshoff"
}
```

I am adding Nils to the CC here so he is aware of the ticket. IIRC it was also a team effort to write that code, but I could be wrong. Some copy of Nil's code seems to be at

http://modular.math.washington.edu/home/ljpk/sage-add-ons/nils/

Cheers,

Michael



---

archive/issue_comments_031825.json:
```json
{
    "body": "Craig, \n\nany news on this front? Maybe somebody else would be willing to start the review process if the code was posted?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T06:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31825",
    "user": "mabshoff"
}
```

Craig, 

any news on this front? Maybe somebody else would be willing to start the review process if the code was posted?

Cheers,

Michael



---

archive/issue_comments_031826.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T00:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31826",
    "user": "craigcitro"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_031827.json:
```json
{
    "body": "Can I suggest closing this ticket? I independently fixed the code for the ring of modular forms last year, and it got committed as part of #5727 (changeset 11961). I've since looked at Nils' code and it seems that he and I independently fixed the same bug in more or less the same way. Certainly find_generators.py now works, and has extensive doctests and passes them all.\n\nI'm setting this to \"needs review\" (if you like, I'm asking for a review for the empty patch).\n\nDavid",
    "created_at": "2010-01-21T09:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31827",
    "user": "davidloeffler"
}
```

Can I suggest closing this ticket? I independently fixed the code for the ring of modular forms last year, and it got committed as part of #5727 (changeset 11961). I've since looked at Nils' code and it seems that he and I independently fixed the same bug in more or less the same way. Certainly find_generators.py now works, and has extensive doctests and passes them all.

I'm setting this to "needs review" (if you like, I'm asking for a review for the empty patch).

David



---

archive/issue_comments_031828.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-21T09:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31828",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_031829.json:
```json
{
    "body": "Looks good to me.  I can't see any bugs, and you didn't lower the coverage score.",
    "created_at": "2010-01-21T17:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31829",
    "user": "was"
}
```

Looks good to me.  I can't see any bugs, and you didn't lower the coverage score.



---

archive/issue_comments_031830.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-21T17:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31830",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_031831.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-21T18:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31831",
    "user": "craigcitro"
}
```

Resolution: fixed



---

archive/issue_comments_031832.json:
```json
{
    "body": "I agree. I intended to close this ticket once you (David) fixed up that code, but apparently forgot.",
    "created_at": "2010-01-21T18:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31832",
    "user": "craigcitro"
}
```

I agree. I intended to close this ticket once you (David) fixed up that code, but apparently forgot.
