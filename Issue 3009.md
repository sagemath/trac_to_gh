# Issue 3009: remove spaces after continuation characters "\"

archive/issues_003009.json:
```json
{
    "body": "Assignee: tba\n\n  \tJohn H Palmieri reports:\n\nIn the section of the tutorial on 3d plotting,\n\n  <http://sagemath.org/doc/html/tut/node22.html>\n\nthe continuation characters \"\\\" all have spaces after them, which\nmesses up cutting and pasting.  Also in the section on Maxima,\n\n  <http://sagemath.org/doc/html/tut/node54.html>\n\ntwo of the backslashes have spaces after them (in the Mobius strip and\nthe Klein bottle examples).\n\nThe same thing happens half a dozen times in \"SAGE Constructions\".\n\nI've only searched the tutorial and the constructions documentation\nfor this issue (by searching the files \"tut.tex\" and \"const.tex\"); I\nhaven't looked at the rest of the documentation. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3009\n\n",
    "created_at": "2008-04-23T20:45:37Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "remove spaces after continuation characters \"\\\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3009",
    "user": "mabshoff"
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

archive/issue_comments_020688.json:
```json
{
    "body": "Attachment [3009_tex.patch](tarball://root/attachments/some-uuid/ticket3009/3009_tex.patch) by jwmerrill created at 2008-09-14 05:59:12",
    "created_at": "2008-09-14T05:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20688",
    "user": "jwmerrill"
}
```

Attachment [3009_tex.patch](tarball://root/attachments/some-uuid/ticket3009/3009_tex.patch) by jwmerrill created at 2008-09-14 05:59:12



---

archive/issue_comments_020689.json:
```json
{
    "body": "I did a regex search on all the tex documentation and all the docstrings for the pattern \"\\\\[\\ ]+$\" and replaced all the appropriate matches (filtered by eye).  The changes are separated into patches for the docstrings and patches for the tex documentation.  If this is accepted, both patches should be applied.",
    "created_at": "2008-09-14T06:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20689",
    "user": "jwmerrill"
}
```

I did a regex search on all the tex documentation and all the docstrings for the pattern "\\[\ ]+$" and replaced all the appropriate matches (filtered by eye).  The changes are separated into patches for the docstrings and patches for the tex documentation.  If this is accepted, both patches should be applied.



---

archive/issue_comments_020690.json:
```json
{
    "body": "Changing assignee from tba to jwmerrill.",
    "created_at": "2008-09-14T06:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20690",
    "user": "jwmerrill"
}
```

Changing assignee from tba to jwmerrill.



---

archive/issue_comments_020691.json:
```json
{
    "body": "Patches look good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T11:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20691",
    "user": "mabshoff"
}
```

Patches look good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_020692.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc3",
    "created_at": "2008-09-14T11:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20692",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc3



---

archive/issue_comments_020693.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-14T11:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3009#issuecomment-20693",
    "user": "mabshoff"
}
```

Resolution: fixed
