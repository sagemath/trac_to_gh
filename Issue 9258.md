# Issue 9258: problem with converting FriCAS domains to Sage objects

archive/issues_009258.json:
```json
{
    "body": "Assignee: tbd\n\nFricas seems to have an api change which breaks a few tests in fricas.py.\n\n\n```\n\n\"\"\"\n        A helper function for converting FriCAS domains to the corresponding\n        Sage object.\n        \n        EXAMPLES::\n        \n            sage: fricas('Integer').sage() #optional - fricas\n            Integer Ring\n            sage: fricas('Fraction Integer').sage() #optional - fricas\n            Rational Field\n            sage: fricas('DoubleFloat').sage() #optional - fricas\n            Real Double Field\n\n        \"\"\"\n```\n\n\nThese now give either a different return value or simply results in raising a NotImplementedError.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9258\n\n",
    "created_at": "2010-06-18T07:11:40Z",
    "labels": [
        "packages: optional",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "problem with converting FriCAS domains to Sage objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9258",
    "user": "awebb"
}
```
Assignee: tbd

Fricas seems to have an api change which breaks a few tests in fricas.py.


```

"""
        A helper function for converting FriCAS domains to the corresponding
        Sage object.
        
        EXAMPLES::
        
            sage: fricas('Integer').sage() #optional - fricas
            Integer Ring
            sage: fricas('Fraction Integer').sage() #optional - fricas
            Rational Field
            sage: fricas('DoubleFloat').sage() #optional - fricas
            Real Double Field

        """
```


These now give either a different return value or simply results in raising a NotImplementedError.

Issue created by migration from https://trac.sagemath.org/ticket/9258





---

archive/issue_comments_087119.json:
```json
{
    "body": "Attachment [trac_9258.patch](tarball://root/attachments/some-uuid/ticket9258/trac_9258.patch) by mhansen created at 2010-06-27 20:13:41",
    "created_at": "2010-06-27T20:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9258#issuecomment-87119",
    "user": "mhansen"
}
```

Attachment [trac_9258.patch](tarball://root/attachments/some-uuid/ticket9258/trac_9258.patch) by mhansen created at 2010-06-27 20:13:41



---

archive/issue_comments_087120.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-27T20:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9258#issuecomment-87120",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087121.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-02T12:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9258#issuecomment-87121",
    "user": "awebb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087122.json:
```json
{
    "body": "That was easier than I thought it would be. :-)\n\nAdam",
    "created_at": "2010-07-02T12:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9258#issuecomment-87122",
    "user": "awebb"
}
```

That was easier than I thought it would be. :-)

Adam



---

archive/issue_comments_087123.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T10:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9258#issuecomment-87123",
    "user": "mpatel"
}
```

Resolution: fixed
