# Issue 6110: [with patch, needs review] implement a "decorator" to allow pickling nested classes

archive/issues_006110.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  craigcitro\n\nThe nested_pickle decorator modifies nested classes to be picklable.  (In Python 2.6 it should be usable as a decorator, although that hasn't been tested; Python 2.5 doesn't support class decorators, so you can't use that syntax in Sage until it upgrades.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6110\n\n",
    "created_at": "2009-05-21T09:10:24Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] implement a \"decorator\" to allow pickling nested classes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6110",
    "user": "cwitty"
}
```
Assignee: cwitty

CC:  craigcitro

The nested_pickle decorator modifies nested classes to be picklable.  (In Python 2.6 it should be usable as a decorator, although that hasn't been tested; Python 2.5 doesn't support class decorators, so you can't use that syntax in Sage until it upgrades.)

Issue created by migration from https://trac.sagemath.org/ticket/6110





---

archive/issue_comments_048813.json:
```json
{
    "body": "Attachment [nested-pickles.patch](tarball://root/attachments/some-uuid/ticket6110/nested-pickles.patch) by nthiery created at 2009-05-23 00:09:10\n\nReviewer patch, with demo of metaclass",
    "created_at": "2009-05-23T00:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6110#issuecomment-48813",
    "user": "nthiery"
}
```

Attachment [nested-pickles.patch](tarball://root/attachments/some-uuid/ticket6110/nested-pickles.patch) by nthiery created at 2009-05-23 00:09:10

Reviewer patch, with demo of metaclass



---

archive/issue_comments_048814.json:
```json
{
    "body": "Attachment [nested-pickles-reviewer.patch](tarball://root/attachments/some-uuid/ticket6110/nested-pickles-reviewer.patch) by nthiery created at 2009-05-23 00:15:38\n\nI just uploaded a super patch (for sage 3.4.2) which:\n- Demonstrates the use a metaclass call nested_pickle automatically on a class, *and all derived subclasse*. Potential application: put this on Category, and all categories would be handled properly. Same thing on Parent? Hmm.\n- Fix nested_pickle to handle old-style classes",
    "created_at": "2009-05-23T00:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6110#issuecomment-48814",
    "user": "nthiery"
}
```

Attachment [nested-pickles-reviewer.patch](tarball://root/attachments/some-uuid/ticket6110/nested-pickles-reviewer.patch) by nthiery created at 2009-05-23 00:15:38

I just uploaded a super patch (for sage 3.4.2) which:
- Demonstrates the use a metaclass call nested_pickle automatically on a class, *and all derived subclasse*. Potential application: put this on Category, and all categories would be handled properly. Same thing on Parent? Hmm.
- Fix nested_pickle to handle old-style classes



---

archive/issue_comments_048815.json:
```json
{
    "body": "Perfect for 4.0.1.",
    "created_at": "2009-05-28T07:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6110#issuecomment-48815",
    "user": "was"
}
```

Perfect for 4.0.1.



---

archive/issue_comments_048816.json:
```json
{
    "body": "Looks and works well for me. Lets get this pickle stuff in.",
    "created_at": "2009-06-10T08:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6110#issuecomment-48816",
    "user": "robertwb"
}
```

Looks and works well for me. Lets get this pickle stuff in.



---

archive/issue_comments_048817.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:53:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6110#issuecomment-48817",
    "user": "ncalexan"
}
```

Resolution: fixed
