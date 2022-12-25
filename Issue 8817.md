# Issue 8817: Rplot001.png left around when doctesting

archive/issues_008817.json:
```json
{
    "body": "Assignee: tbd\n\nI doctested after I think #7665 and this file Rplot001.png appeared in SAGE_ROOT.  That's obnoxious. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8817\n\n",
    "closed_at": "2010-05-02T23:57:20Z",
    "created_at": "2010-04-29T06:06:26Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "Rplot001.png left around when doctesting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8817",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

I doctested after I think #7665 and this file Rplot001.png appeared in SAGE_ROOT.  That's obnoxious. 

Issue created by migration from https://trac.sagemath.org/ticket/8817





---

archive/issue_comments_080793.json:
```json
{
    "body": "eah, this is my fault:\n\n```\n+        This example saves a plot to the standard R output, usually \n+        a filename like ``Rplot001.png`` - from the command line, in \n+        the current directory, and in the cell directory in the notebook::\n+\n+            sage: r.plot(\"1:10\")\n+            null device \n+                      1 \n+\n```\nI actually put this one in to show users how to actually get a file in a directory that they have access to, as opposed to a temp directory, but forgot we can't do that.  Is it legitimate to put #not tested with this doctest as a fix, since it is important to have the example there?",
    "created_at": "2010-04-29T16:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8817#issuecomment-80793",
    "user": "https://github.com/kcrisman"
}
```

eah, this is my fault:

```
+        This example saves a plot to the standard R output, usually 
+        a filename like ``Rplot001.png`` - from the command line, in 
+        the current directory, and in the cell directory in the notebook::
+
+            sage: r.plot("1:10")
+            null device 
+                      1 
+
```
I actually put this one in to show users how to actually get a file in a directory that they have access to, as opposed to a temp directory, but forgot we can't do that.  Is it legitimate to put #not tested with this doctest as a fix, since it is important to have the example there?



---

archive/issue_comments_080794.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-30T00:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8817#issuecomment-80794",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080795.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-30T14:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8817#issuecomment-80795",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080796.json:
```json
{
    "body": "> but forgot we can't do that.  Is it legitimate to put #not tested with\n> this doctest as a fix, since it is important to have the example\n> there?\n\nFrom was:\n\n```\nAnother option:\n\n1. make sufpre the png file you are about to write doesn't exist in the current directory, then write it.\n2. then delete it!\n\n\n# not tested should be avoided at all costs.\n```",
    "created_at": "2010-04-30T14:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8817#issuecomment-80796",
    "user": "https://github.com/kcrisman"
}
```

> but forgot we can't do that.  Is it legitimate to put #not tested with
> this doctest as a fix, since it is important to have the example
> there?

From was:

```
Another option:

1. make sufpre the png file you are about to write doesn't exist in the current directory, then write it.
2. then delete it!


# not tested should be avoided at all costs.
```



---

archive/issue_comments_080797.json:
```json
{
    "body": "Based on Sage 4.4 + R plot patch",
    "created_at": "2010-04-30T15:04:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8817#issuecomment-80797",
    "user": "https://github.com/kcrisman"
}
```

Based on Sage 4.4 + R plot patch



---

archive/issue_comments_080798.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-30T15:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8817#issuecomment-80798",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080799.json:
```json
{
    "body": "Attachment [trac_8817-R-plot-file-remove.patch](tarball://root/attachments/some-uuid/ticket8817/trac_8817-R-plot-file-remove.patch) by @kcrisman created at 2010-04-30 15:05:48\n\nOkay, try this - it is VERY explicit.  I also replaced occurrences of os.unlink with os.remove, which is identical but makes far more sense to those who are not familiar with the unlink command (like me).",
    "created_at": "2010-04-30T15:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8817#issuecomment-80799",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_8817-R-plot-file-remove.patch](tarball://root/attachments/some-uuid/ticket8817/trac_8817-R-plot-file-remove.patch) by @kcrisman created at 2010-04-30 15:05:48

Okay, try this - it is VERY explicit.  I also replaced occurrences of os.unlink with os.remove, which is identical but makes far more sense to those who are not familiar with the unlink command (like me).



---

archive/issue_comments_080800.json:
```json
{
    "body": "I really don't like this very brittle and dangerous patch.  I've posted a new patch.  Please review. I've included this in alpha3 anyways.\n\nWilliam",
    "created_at": "2010-05-01T05:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8817#issuecomment-80800",
    "user": "https://github.com/williamstein"
}
```

I really don't like this very brittle and dangerous patch.  I've posted a new patch.  Please review. I've included this in alpha3 anyways.

William



---

archive/issue_comments_080801.json:
```json
{
    "body": "Attachment [trac_8817-wstein.patch](tarball://root/attachments/some-uuid/ticket8817/trac_8817-wstein.patch) by @williamstein created at 2010-05-01 05:17:04",
    "created_at": "2010-05-01T05:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8817#issuecomment-80801",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8817-wstein.patch](tarball://root/attachments/some-uuid/ticket8817/trac_8817-wstein.patch) by @williamstein created at 2010-05-01 05:17:04



---

archive/issue_events_021503.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-02T23:57:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8817#event-21503"
}
```



---

archive/issue_events_021504.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-02T23:57:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "milestone": "sage-4.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8817#event-21504"
}
```



---

archive/issue_comments_080802.json:
```json
{
    "body": "The directory named by the environment variable `SAGE_TMP` is where junk files can go. Such junk files include temporary files generated during doctesting.",
    "created_at": "2010-05-02T23:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8817#issuecomment-80802",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The directory named by the environment variable `SAGE_TMP` is where junk files can go. Such junk files include temporary files generated during doctesting.



---

archive/issue_comments_080803.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-02T23:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8817#issuecomment-80803",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
