# Issue 3009: remove spaces after continuation characters "\"

archive/issues_003009.json:
```json
{
    "body": "Assignee: tba\n\n  \tJohn H Palmieri reports:\n\nIn the section of the tutorial on 3d plotting,\n\n  <http://sagemath.org/doc/html/tut/node22.html>\n\nthe continuation characters \"\\\" all have spaces after them, which\nmesses up cutting and pasting.  Also in the section on Maxima,\n\n  <http://sagemath.org/doc/html/tut/node54.html>\n\ntwo of the backslashes have spaces after them (in the Mobius strip and\nthe Klein bottle examples).\n\nThe same thing happens half a dozen times in \"SAGE Constructions\".\n\nI've only searched the tutorial and the constructions documentation\nfor this issue (by searching the files \"tut.tex\" and \"const.tex\"); I\nhaven't looked at the rest of the documentation. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3009\n\n",
    "created_at": "2008-04-23T20:45:37Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "remove spaces after continuation characters \"\\\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3009",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: tba

  	John H Palmieri reports:

In the section of the tutorial on 3d plotting,

  <http://sagemath.org/doc/html/tut/node22.html>

the continuation characters "\" all have spaces after them, which
messes up cutting and pasting.  Also in the section on Maxima,

  <http://sagemath.org/doc/html/tut/node54.html>

two of the backslashes have spaces after them (in the Mobius strip and
the Klein bottle examples).

The same thing happens half a dozen times in "SAGE Constructions".

I've only searched the tutorial and the constructions documentation
for this issue (by searching the files "tut.tex" and "const.tex"); I
haven't looked at the rest of the documentation. 

Issue created by migration from https://trac.sagemath.org/ticket/3009





---

archive/issue_comments_020645.json:
```json
{
    "body": "Attachment [3009_tex.patch](tarball://root/attachments/some-uuid/ticket3009/3009_tex.patch) by @jicama created at 2008-09-14 05:59:12",
    "created_at": "2008-09-14T05:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20645",
    "user": "https://github.com/jicama"
}
```

Attachment [3009_tex.patch](tarball://root/attachments/some-uuid/ticket3009/3009_tex.patch) by @jicama created at 2008-09-14 05:59:12



---

archive/issue_comments_020646.json:
```json
{
    "body": "I did a regex search on all the tex documentation and all the docstrings for the pattern \"\\\\[\\ ]+$\" and replaced all the appropriate matches (filtered by eye).  The changes are separated into patches for the docstrings and patches for the tex documentation.  If this is accepted, both patches should be applied.",
    "created_at": "2008-09-14T06:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20646",
    "user": "https://github.com/jicama"
}
```

I did a regex search on all the tex documentation and all the docstrings for the pattern "\\[\ ]+$" and replaced all the appropriate matches (filtered by eye).  The changes are separated into patches for the docstrings and patches for the tex documentation.  If this is accepted, both patches should be applied.



---

archive/issue_comments_020647.json:
```json
{
    "body": "Changing assignee from tba to @jicama.",
    "created_at": "2008-09-14T06:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20647",
    "user": "https://github.com/jicama"
}
```

Changing assignee from tba to @jicama.



---

archive/issue_comments_020648.json:
```json
{
    "body": "Patches look good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T11:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20648",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patches look good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_020649.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc3",
    "created_at": "2008-09-14T11:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20649",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc3



---

archive/issue_events_006838.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-14T11:53:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3009#event-6838"
}
```



---

archive/issue_comments_020650.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-14T11:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20650",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006839.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-15T03:29:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3009#event-6839"
}
```
