# Issue 2182: undefined symbol: gzopen64 when starting the notebook()

archive/issues_002182.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe issue was reported in https://groups.google.com/group/sage-support/t/8f03a6f2f3d0aea8 by Matthias Hillenbrand:\n\n```\nHello,\n\nSince I have upgraded to SAGE 2.10.x I get the following error message\nwhen starting the notebook:\n\ngnome-www-browser: symbol lookup error: /usr/lib/libxml2.so.2:\nundefined symbol: gzopen64\n\nI get this error message on two different computers (one running\nUbuntu 7.10 the other Debian Testing, which I installed today) and\nwith any browser (e.g. Firefox as standard browser). If I open a\nsession of the browser before starting SAGE, the error won't occur.\n```\n\n\nJason Grout figured out that `SAGE_ORIG_LD_LIBRARY_PATH` is being overwritten improperly when the second Sage session starts (due to the launch of the notebook). He has proposed a fix and is working on a patch which will hopefully make it into 2.10.2.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2182\n\n",
    "created_at": "2008-02-16T22:13:06Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "undefined symbol: gzopen64 when starting the notebook()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2182",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The issue was reported in https://groups.google.com/group/sage-support/t/8f03a6f2f3d0aea8 by Matthias Hillenbrand:

```
Hello,

Since I have upgraded to SAGE 2.10.x I get the following error message
when starting the notebook:

gnome-www-browser: symbol lookup error: /usr/lib/libxml2.so.2:
undefined symbol: gzopen64

I get this error message on two different computers (one running
Ubuntu 7.10 the other Debian Testing, which I installed today) and
with any browser (e.g. Firefox as standard browser). If I open a
session of the browser before starting SAGE, the error won't occur.
```


Jason Grout figured out that `SAGE_ORIG_LD_LIBRARY_PATH` is being overwritten improperly when the second Sage session starts (due to the launch of the notebook). He has proposed a fix and is working on a patch which will hopefully make it into 2.10.2.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2182





---

archive/issue_comments_014302.json:
```json
{
    "body": "To be applied to the sage repository.",
    "created_at": "2008-02-17T03:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14302",
    "user": "https://github.com/jasongrout"
}
```

To be applied to the sage repository.



---

archive/issue_comments_014303.json:
```json
{
    "body": "Attachment [LD-LIBRARY-clobbered-SAGE-SCRIPTS.patch](tarball://root/attachments/some-uuid/ticket2182/LD-LIBRARY-clobbered-SAGE-SCRIPTS.patch) by @jasongrout created at 2008-02-17 03:11:15\n\nTo be applied to the sage-scripts repository (changes sage-env)",
    "created_at": "2008-02-17T03:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14303",
    "user": "https://github.com/jasongrout"
}
```

Attachment [LD-LIBRARY-clobbered-SAGE-SCRIPTS.patch](tarball://root/attachments/some-uuid/ticket2182/LD-LIBRARY-clobbered-SAGE-SCRIPTS.patch) by @jasongrout created at 2008-02-17 03:11:15

To be applied to the sage-scripts repository (changes sage-env)



---

archive/issue_comments_014304.json:
```json
{
    "body": "The sage patch above fixes the open_page function (which opens the notebook in the browser) to use the standard sage mechanism for opening an external app instead of the previously hard-coded way.  The sage-scripts patch changes sage-env so that recursively run sage sessions do not clobber the saved original LD_LIBRARY environment variable.",
    "created_at": "2008-02-17T03:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14304",
    "user": "https://github.com/jasongrout"
}
```

The sage patch above fixes the open_page function (which opens the notebook in the browser) to use the standard sage mechanism for opening an external app instead of the previously hard-coded way.  The sage-scripts patch changes sage-env so that recursively run sage sessions do not clobber the saved original LD_LIBRARY environment variable.



---

archive/issue_comments_014305.json:
```json
{
    "body": "Both patches look good to me. Positive review. Thanks for the excellent work.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T04:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14305",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Both patches look good to me. Positive review. Thanks for the excellent work.

Cheers,

Michael



---

archive/issue_comments_014306.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T04:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14306",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014307.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T04:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14307",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
