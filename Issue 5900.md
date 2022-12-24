# Issue 5900: [with patches, needs review] Add support for system python != Sage python

archive/issues_005900.json:
```json
{
    "body": "Assignee: tabbott\n\nOn Ubuntu jaunty, the system Python is 2.6 but Sage is built with Python 2.5.  This results in problems in a few places where Sage directly invokes a python program rather than running it via python.  For example, running \"trial\" rather than \"python $(which trial)\" would result in \"trial\" being started with Python 2.6.\n\nI've attached the set of patches that I applied in order to deal with this issue in Jaunty.  I believe they should be harmless for Sage, since it puts $SAGE_LOCAL at the start of PATH, ahead of any system copies of trial/twistd/etc. that might exist.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5900\n\n",
    "created_at": "2009-04-26T05:43:42Z",
    "labels": [
        "debian-package",
        "major",
        "enhancement"
    ],
    "title": "[with patches, needs review] Add support for system python != Sage python",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5900",
    "user": "tabbott"
}
```
Assignee: tabbott

On Ubuntu jaunty, the system Python is 2.6 but Sage is built with Python 2.5.  This results in problems in a few places where Sage directly invokes a python program rather than running it via python.  For example, running "trial" rather than "python $(which trial)" would result in "trial" being started with Python 2.6.

I've attached the set of patches that I applied in order to deal with this issue in Jaunty.  I believe they should be harmless for Sage, since it puts $SAGE_LOCAL at the start of PATH, ahead of any system copies of trial/twistd/etc. that might exist.


Issue created by migration from https://trac.sagemath.org/ticket/5900





---

archive/issue_comments_046642.json:
```json
{
    "body": "Attachment [sage_scripts-dsage-trial.patch](tarball://root/attachments/some-uuid/ticket5900/sage_scripts-dsage-trial.patch) by tabbott created at 2009-04-26 05:43:57",
    "created_at": "2009-04-26T05:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5900#issuecomment-46642",
    "user": "tabbott"
}
```

Attachment [sage_scripts-dsage-trial.patch](tarball://root/attachments/some-uuid/ticket5900/sage_scripts-dsage-trial.patch) by tabbott created at 2009-04-26 05:43:57



---

archive/issue_comments_046643.json:
```json
{
    "body": "Attachment [sage_scripts-twistd.patch](tarball://root/attachments/some-uuid/ticket5900/sage_scripts-twistd.patch) by tabbott created at 2009-04-26 05:44:06",
    "created_at": "2009-04-26T05:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5900#issuecomment-46643",
    "user": "tabbott"
}
```

Attachment [sage_scripts-twistd.patch](tarball://root/attachments/some-uuid/ticket5900/sage_scripts-twistd.patch) by tabbott created at 2009-04-26 05:44:06



---

archive/issue_comments_046644.json:
```json
{
    "body": "They look good to me.  I'm not sure if they are still relevant since Sage switched to Python 2.6, but they shouldn't hurt.",
    "created_at": "2009-09-08T05:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5900#issuecomment-46644",
    "user": "mhansen"
}
```

They look good to me.  I'm not sure if they are still relevant since Sage switched to Python 2.6, but they shouldn't hurt.



---

archive/issue_comments_046645.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-08T11:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5900#issuecomment-46645",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_046646.json:
```json
{
    "body": "Applied to the bin repository.",
    "created_at": "2009-09-08T11:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5900#issuecomment-46646",
    "user": "mvngu"
}
```

Applied to the bin repository.
