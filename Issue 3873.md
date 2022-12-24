# Issue 3873: Doctest should test for warnings

archive/issues_003873.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis patch makes it so that warnings are output to stdout and are compared in the doctest framework.  To doctest a warning, do something like:\n\n\n```\ndef mytest():\n    r\"\"\"\n    EXAMPLES:\n        sage: warnings.warn(\"hi\")\n        /...:1: UserWarning: hi\n        #...\n        \"\"\"\n    pass\n```\n\n\nThis patch will probably break a few doctests (that gave warnings before, but the warnings were ignored).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3873\n\n",
    "created_at": "2008-08-15T11:05:50Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Doctest should test for warnings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3873",
    "user": "jason"
}
```
Assignee: mabshoff

This patch makes it so that warnings are output to stdout and are compared in the doctest framework.  To doctest a warning, do something like:


```
def mytest():
    r"""
    EXAMPLES:
        sage: warnings.warn("hi")
        /...:1: UserWarning: hi
        #...
        """
    pass
```


This patch will probably break a few doctests (that gave warnings before, but the warnings were ignored).

Issue created by migration from https://trac.sagemath.org/ticket/3873





---

archive/issue_comments_027618.json:
```json
{
    "body": "Attachment [doctest-warnings.patch](tarball://root/attachments/some-uuid/ticket3873/doctest-warnings.patch) by mhansen created at 2008-08-15 21:53:49",
    "created_at": "2008-08-15T21:53:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3873#issuecomment-27618",
    "user": "mhansen"
}
```

Attachment [doctest-warnings.patch](tarball://root/attachments/some-uuid/ticket3873/doctest-warnings.patch) by mhansen created at 2008-08-15 21:53:49



---

archive/issue_comments_027619.json:
```json
{
    "body": "This patch should be applied to whatever repository includes $SAGE_LOCAL/bin/",
    "created_at": "2008-08-16T16:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3873#issuecomment-27619",
    "user": "jason"
}
```

This patch should be applied to whatever repository includes $SAGE_LOCAL/bin/



---

archive/issue_comments_027620.json:
```json
{
    "body": "This depends on #3940 (which imports the warnings module on sage startup).",
    "created_at": "2008-08-24T00:14:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3873#issuecomment-27620",
    "user": "jason"
}
```

This depends on #3940 (which imports the warnings module on sage startup).



---

archive/issue_comments_027621.json:
```json
{
    "body": "Attachment [trac3873-sage_scripts.patch](tarball://root/attachments/some-uuid/ticket3873/trac3873-sage_scripts.patch) by cwitty created at 2008-08-24 00:50:41",
    "created_at": "2008-08-24T00:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3873#issuecomment-27621",
    "user": "cwitty"
}
```

Attachment [trac3873-sage_scripts.patch](tarball://root/attachments/some-uuid/ticket3873/trac3873-sage_scripts.patch) by cwitty created at 2008-08-24 00:50:41



---

archive/issue_comments_027622.json:
```json
{
    "body": "Attachment [trac3873-doctest-warnings.patch](tarball://root/attachments/some-uuid/ticket3873/trac3873-doctest-warnings.patch) by cwitty created at 2008-08-24 00:50:59",
    "created_at": "2008-08-24T00:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3873#issuecomment-27622",
    "user": "cwitty"
}
```

Attachment [trac3873-doctest-warnings.patch](tarball://root/attachments/some-uuid/ticket3873/trac3873-doctest-warnings.patch) by cwitty created at 2008-08-24 00:50:59



---

archive/issue_comments_027623.json:
```json
{
    "body": "Positive review for Jason's patch; my two patches need to be reviewed.  The first patch (to be applied to sage_scripts after Jason's patch) fixes Jason's patch to not depend on #3940 any more, and to get rid of useless filenames (that would have to be elided from every doctest).\n\nThe second patch fixes the two places in the Sage library that generate warnings in doctests.",
    "created_at": "2008-08-24T00:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3873#issuecomment-27623",
    "user": "cwitty"
}
```

Positive review for Jason's patch; my two patches need to be reviewed.  The first patch (to be applied to sage_scripts after Jason's patch) fixes Jason's patch to not depend on #3940 any more, and to get rid of useless filenames (that would have to be elided from every doctest).

The second patch fixes the two places in the Sage library that generate warnings in doctests.



---

archive/issue_comments_027624.json:
```json
{
    "body": "Nice patches, but how does #3940 relate here?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T00:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3873#issuecomment-27624",
    "user": "mabshoff"
}
```

Nice patches, but how does #3940 relate here?

Cheers,

Michael



---

archive/issue_comments_027625.json:
```json
{
    "body": "Positive review for Carl's patches.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T00:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3873#issuecomment-27625",
    "user": "mabshoff"
}
```

Positive review for Carl's patches.

Cheers,

Michael



---

archive/issue_comments_027626.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.2.alpha1",
    "created_at": "2008-08-25T01:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3873#issuecomment-27626",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.1.2.alpha1



---

archive/issue_comments_027627.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T01:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3873#issuecomment-27627",
    "user": "mabshoff"
}
```

Resolution: fixed
