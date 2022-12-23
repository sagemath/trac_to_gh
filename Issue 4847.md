# Issue 4847: [with patch, needs review] Remove deadwood: sage/functions/elementary.py and sage/rings/interval.py

archive/issues_004847.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  wdj\n\nThe two files in question are ancient (2006 or earlier), not imported and deprecated. So let's get rid of them.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4847\n\n",
    "created_at": "2008-12-21T15:49:08Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Remove deadwood: sage/functions/elementary.py and sage/rings/interval.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4847",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  wdj

The two files in question are ancient (2006 or earlier), not imported and deprecated. So let's get rid of them.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4847





---

archive/issue_comments_036752.json:
```json
{
    "body": "Attachment\n\nAfter applying the patch, deleting the build directory followed by a \"sage -ba\" all doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T15:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4847#issuecomment-36752",
    "user": "mabshoff"
}
```

Attachment

After applying the patch, deleting the build directory followed by a "sage -ba" all doctests pass.

Cheers,

Michael



---

archive/issue_comments_036753.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-21T15:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4847#issuecomment-36753",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036754.json:
```json
{
    "body": "These files are clearly old and untested.  Interval.py is deprecated by its own author and it seems fine to remove it.  It is less clear to me that elementary.py is totally redundant, it would be good if David Joyner could explicitly comment on its usefulness.  Otherwise it looks reasonable to get rid of these.",
    "created_at": "2008-12-21T16:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4847#issuecomment-36754",
    "user": "mhampton"
}
```

These files are clearly old and untested.  Interval.py is deprecated by its own author and it seems fine to remove it.  It is less clear to me that elementary.py is totally redundant, it would be good if David Joyner could explicitly comment on its usefulness.  Otherwise it looks reasonable to get rid of these.



---

archive/issue_comments_036755.json:
```json
{
    "body": "David, can you comment on elementary.py?\nThanks,\nMarshall",
    "created_at": "2008-12-21T16:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4847#issuecomment-36755",
    "user": "mhampton"
}
```

David, can you comment on elementary.py?
Thanks,
Marshall



---

archive/issue_comments_036756.json:
```json
{
    "body": "\n```\n14:03 < wstein> The interval.py file I wrote, and can be safely deleted.\n14:03 < wstein> It was deprecated and it has been > 6 mnths.\n14:04 < mabs> Well, I had never seen that file, which should tell you something :)\n14:05 < wstein> The elementary functions thing is totally of a different nature.\n14:05 < wstein> I very much doubt it has been replaced by something newer.\n14:05 < wstein> And it's very useful for differential equations teaching.\n14:05 < wstein> At least that was the intention.\n14:05 < wstein> But I personally don't have interest in that.\n14:06 < wstein> Best thing would be to delete it and have David -- if he cares -- submit a new\n14:06 < wstein> patch that adds back a version that fully works.\n```\n",
    "created_at": "2008-12-22T22:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4847#issuecomment-36756",
    "user": "was"
}
```


```
14:03 < wstein> The interval.py file I wrote, and can be safely deleted.
14:03 < wstein> It was deprecated and it has been > 6 mnths.
14:04 < mabs> Well, I had never seen that file, which should tell you something :)
14:05 < wstein> The elementary functions thing is totally of a different nature.
14:05 < wstein> I very much doubt it has been replaced by something newer.
14:05 < wstein> And it's very useful for differential equations teaching.
14:05 < wstein> At least that was the intention.
14:05 < wstein> But I personally don't have interest in that.
14:06 < wstein> Best thing would be to delete it and have David -- if he cares -- submit a new
14:06 < wstein> patch that adds back a version that fully works.
```




---

archive/issue_comments_036757.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-22T22:19:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4847#issuecomment-36757",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3.alpha0



---

archive/issue_comments_036758.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-22T22:19:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4847#issuecomment-36758",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036759.json:
```json
{
    "body": "Sorry, for the late reply. I read some of these comments but missed the request to comment on this. \n\nComments: I am unconvinced by the usefulness of the code in elementary.py (which I wrote, so I can be as critical as I want:-). It was written way before the excellent code implementing the symbolic expression rings. As William said, it was motivated by solving constant coefficient ODEs using the method of undetermined coefficients/annihilators. It was also motivated by a desire to experiment with ways to implement differential operator rings, but it does this unconvincingly as well. (I don't want to say \"it does this badly\" because it might be that rings of differential operators should be implemented as a method for the SR class - I don't know.)\n\nBottom line - I agree elementary should be dumped. However, I'm very interested in alternative approaches anyone comes up with, especially ones that implement differential operator rings properly.",
    "created_at": "2008-12-23T00:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4847#issuecomment-36759",
    "user": "wdj"
}
```

Sorry, for the late reply. I read some of these comments but missed the request to comment on this. 

Comments: I am unconvinced by the usefulness of the code in elementary.py (which I wrote, so I can be as critical as I want:-). It was written way before the excellent code implementing the symbolic expression rings. As William said, it was motivated by solving constant coefficient ODEs using the method of undetermined coefficients/annihilators. It was also motivated by a desire to experiment with ways to implement differential operator rings, but it does this unconvincingly as well. (I don't want to say "it does this badly" because it might be that rings of differential operators should be implemented as a method for the SR class - I don't know.)

Bottom line - I agree elementary should be dumped. However, I'm very interested in alternative approaches anyone comes up with, especially ones that implement differential operator rings properly.
