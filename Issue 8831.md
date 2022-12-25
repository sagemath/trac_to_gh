# Issue 8831: fail to build PDF version of reference manual in Sage 4.4.1.alpha2

archive/issues_008831.json:
```json
{
    "body": "Assignee: mvngu\n\nAs the subject says. Even after fixing warnings in building the HTML version of the reference manual as per #8819, building the PDF version hangs while processing a reference to graphviz:\n\n```\nUnderfull \\hbox (badness 6380) in paragraph at lines 410101--410105\n[]\\T1/ptm/m/n/10 Aric Hag-berg, Dan Schult and Pieter Swart. Net-workX doc-u-me\nn-ta-tion. [On-line] Avail-able:\n! Missing $ inserted.\n<inserted text> \n                $\nl.410122 \\bibitem[dot_spec]{dot_spec}\n                                     {\\hypertarget{dot_spec}{}\n```\n\nThis is traced to the function `graphviz_string()` in `sage/graphs/generic_graph.py`\n\nIssue created by migration from https://trac.sagemath.org/ticket/8831\n\n",
    "created_at": "2010-04-30T19:28:09Z",
    "labels": [
        "component: documentation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "fail to build PDF version of reference manual in Sage 4.4.1.alpha2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8831",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

As the subject says. Even after fixing warnings in building the HTML version of the reference manual as per #8819, building the PDF version hangs while processing a reference to graphviz:

```
Underfull \hbox (badness 6380) in paragraph at lines 410101--410105
[]\T1/ptm/m/n/10 Aric Hag-berg, Dan Schult and Pieter Swart. Net-workX doc-u-me
n-ta-tion. [On-line] Avail-able:
! Missing $ inserted.
<inserted text> 
                $
l.410122 \bibitem[dot_spec]{dot_spec}
                                     {\hypertarget{dot_spec}{}
```

This is traced to the function `graphviz_string()` in `sage/graphs/generic_graph.py`

Issue created by migration from https://trac.sagemath.org/ticket/8831





---

archive/issue_comments_081081.json:
```json
{
    "body": "Attachment [trac_8831-docbuild-pdf.patch](tarball://root/attachments/some-uuid/ticket8831/trac_8831-docbuild-pdf.patch) by mvngu created at 2010-04-30 19:47:51\n\nbased on Sage 4.4.1.alpha2",
    "created_at": "2010-04-30T19:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8831#issuecomment-81081",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8831-docbuild-pdf.patch](tarball://root/attachments/some-uuid/ticket8831/trac_8831-docbuild-pdf.patch) by mvngu created at 2010-04-30 19:47:51

based on Sage 4.4.1.alpha2



---

archive/issue_comments_081082.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-30T19:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8831#issuecomment-81082",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081083.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-02T16:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8831#issuecomment-81083",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
