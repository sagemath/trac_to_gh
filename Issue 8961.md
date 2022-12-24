# Issue 8961: zope.testbrowser is included in sagenb but is no longer required

archive/issues_008961.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  mpatel leif\n\n`zope.testbrowser` is no longer needed by sagenb but is still listed as a requirement.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8961\n\n",
    "created_at": "2010-05-14T11:27:14Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "zope.testbrowser is included in sagenb but is no longer required",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8961",
    "user": "timdumol"
}
```
Assignee: jason, was

CC:  mpatel leif

`zope.testbrowser` is no longer needed by sagenb but is still listed as a requirement.

Issue created by migration from https://trac.sagemath.org/ticket/8961





---

archive/issue_comments_082598.json:
```json
{
    "body": "Removes zope.testbrowser as a dependency.",
    "created_at": "2010-07-06T13:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8961#issuecomment-82598",
    "user": "timdumol"
}
```

Removes zope.testbrowser as a dependency.



---

archive/issue_comments_082599.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2010-07-06T13:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8961#issuecomment-82599",
    "user": "timdumol"
}
```

Changing priority from minor to major.



---

archive/issue_comments_082600.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-06T13:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8961#issuecomment-82600",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082601.json:
```json
{
    "body": "Attachment [trac_8961-remove-zope.testbrowser.patch](tarball://root/attachments/some-uuid/ticket8961/trac_8961-remove-zope.testbrowser.patch) by timdumol created at 2010-07-06 13:23:04\n\nNow only Twisted (and its zope.interface, which is included in the Twisted spkg) is required by SageNB.",
    "created_at": "2010-07-06T13:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8961#issuecomment-82601",
    "user": "timdumol"
}
```

Attachment [trac_8961-remove-zope.testbrowser.patch](tarball://root/attachments/some-uuid/ticket8961/trac_8961-remove-zope.testbrowser.patch) by timdumol created at 2010-07-06 13:23:04

Now only Twisted (and its zope.interface, which is included in the Twisted spkg) is required by SageNB.



---

archive/issue_comments_082602.json:
```json
{
    "body": "Removes an extra line.",
    "created_at": "2010-07-06T16:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8961#issuecomment-82602",
    "user": "timdumol"
}
```

Removes an extra line.



---

archive/issue_comments_082603.json:
```json
{
    "body": "Attachment [trac_8961-remove-zope.testbrowser.2.patch](tarball://root/attachments/some-uuid/ticket8961/trac_8961-remove-zope.testbrowser.2.patch) by timdumol created at 2010-07-06 17:09:19\n\nThe package is at http://sage.math.washington.edu/home/timdumol/sagenb-0.8.1.spkg, and is the tentative package for #9430.",
    "created_at": "2010-07-06T17:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8961#issuecomment-82603",
    "user": "timdumol"
}
```

Attachment [trac_8961-remove-zope.testbrowser.2.patch](tarball://root/attachments/some-uuid/ticket8961/trac_8961-remove-zope.testbrowser.2.patch) by timdumol created at 2010-07-06 17:09:19

The package is at http://sage.math.washington.edu/home/timdumol/sagenb-0.8.1.spkg, and is the tentative package for #9430.



---

archive/issue_comments_082604.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-11T06:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8961#issuecomment-82604",
    "user": "timdumol"
}
```

Resolution: fixed
