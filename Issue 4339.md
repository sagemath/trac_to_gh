# Issue 4339: modular forms -- incorporate Nils Skoruppa's code for computing generators for the ring of modular forms of given level

archive/issues_004339.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  nilsskoruppa\n\nCraig has an email from Nils with this code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4339\n\n",
    "created_at": "2008-10-22T17:49:42Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "modular forms -- incorporate Nils Skoruppa's code for computing generators for the ring of modular forms of given level",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4339",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

CC:  nilsskoruppa

Craig has an email from Nils with this code.

Issue created by migration from https://trac.sagemath.org/ticket/4339





---

archive/issue_comments_031762.json:
```json
{
    "body": "I am adding Nils to the CC here so he is aware of the ticket. IIRC it was also a team effort to write that code, but I could be wrong. Some copy of Nil's code seems to be at\n\nhttp://modular.math.washington.edu/home/ljpk/sage-add-ons/nils/\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T21:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31762",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am adding Nils to the CC here so he is aware of the ticket. IIRC it was also a team effort to write that code, but I could be wrong. Some copy of Nil's code seems to be at

http://modular.math.washington.edu/home/ljpk/sage-add-ons/nils/

Cheers,

Michael



---

archive/issue_comments_031763.json:
```json
{
    "body": "Craig, \n\nany news on this front? Maybe somebody else would be willing to start the review process if the code was posted?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T06:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31763",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Craig, 

any news on this front? Maybe somebody else would be willing to start the review process if the code was posted?

Cheers,

Michael



---

archive/issue_comments_031764.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T00:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31764",
    "user": "https://github.com/craigcitro"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_031765.json:
```json
{
    "body": "Can I suggest closing this ticket? I independently fixed the code for the ring of modular forms last year, and it got committed as part of #5727 (changeset 11961). I've since looked at Nils' code and it seems that he and I independently fixed the same bug in more or less the same way. Certainly find_generators.py now works, and has extensive doctests and passes them all.\n\nI'm setting this to \"needs review\" (if you like, I'm asking for a review for the empty patch).\n\nDavid",
    "created_at": "2010-01-21T09:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31765",
    "user": "https://github.com/loefflerd"
}
```

Can I suggest closing this ticket? I independently fixed the code for the ring of modular forms last year, and it got committed as part of #5727 (changeset 11961). I've since looked at Nils' code and it seems that he and I independently fixed the same bug in more or less the same way. Certainly find_generators.py now works, and has extensive doctests and passes them all.

I'm setting this to "needs review" (if you like, I'm asking for a review for the empty patch).

David



---

archive/issue_comments_031766.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-21T09:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31766",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_031767.json:
```json
{
    "body": "Looks good to me.  I can't see any bugs, and you didn't lower the coverage score.",
    "created_at": "2010-01-21T17:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31767",
    "user": "https://github.com/williamstein"
}
```

Looks good to me.  I can't see any bugs, and you didn't lower the coverage score.



---

archive/issue_comments_031768.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-21T17:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31768",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_031769.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-21T18:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31769",
    "user": "https://github.com/craigcitro"
}
```

Resolution: fixed



---

archive/issue_comments_031770.json:
```json
{
    "body": "I agree. I intended to close this ticket once you (David) fixed up that code, but apparently forgot.",
    "created_at": "2010-01-21T18:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4339#issuecomment-31770",
    "user": "https://github.com/craigcitro"
}
```

I agree. I intended to close this ticket once you (David) fixed up that code, but apparently forgot.



---

archive/issue_events_004586.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2010-01-21T18:20:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4339",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4339#event-4586"
}
```
