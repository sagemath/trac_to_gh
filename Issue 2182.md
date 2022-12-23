# Issue 2182: undefined symbol: gzopen64 when starting the notebook()

archive/issues_002182.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe issue was reported in https://groups.google.com/group/sage-support/t/8f03a6f2f3d0aea8 by Matthias Hillenbrand:\n\n```\nHello,\n\nSince I have upgraded to SAGE 2.10.x I get the following error message\nwhen starting the notebook:\n\ngnome-www-browser: symbol lookup error: /usr/lib/libxml2.so.2:\nundefined symbol: gzopen64\n\nI get this error message on two different computers (one running\nUbuntu 7.10 the other Debian Testing, which I installed today) and\nwith any browser (e.g. Firefox as standard browser). If I open a\nsession of the browser before starting SAGE, the error won't occur.\n```\n\n\nJason Grout figured out that `SAGE_ORIG_LD_LIBRARY_PATH` is being overwritten improperly when the second Sage session starts (due to the launch of the notebook). He has proposed a fix and is working on a patch which will hopefully make it into 2.10.2.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2182\n\n",
    "created_at": "2008-02-16T22:13:06Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "undefined symbol: gzopen64 when starting the notebook()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2182",
    "user": "mabshoff"
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

archive/issue_comments_014333.json:
```json
{
    "body": "To be applied to the sage repository.",
    "created_at": "2008-02-17T03:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14333",
    "user": "jason"
}
```

To be applied to the sage repository.



---

archive/issue_comments_014334.json:
```json
{
    "body": "Attachment\n\nTo be applied to the sage-scripts repository (changes sage-env)",
    "created_at": "2008-02-17T03:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14334",
    "user": "jason"
}
```

Attachment

To be applied to the sage-scripts repository (changes sage-env)



---

archive/issue_comments_014335.json:
```json
{
    "body": "The sage patch above fixes the open_page function (which opens the notebook in the browser) to use the standard sage mechanism for opening an external app instead of the previously hard-coded way.  The sage-scripts patch changes sage-env so that recursively run sage sessions do not clobber the saved original LD_LIBRARY environment variable.",
    "created_at": "2008-02-17T03:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14335",
    "user": "jason"
}
```

The sage patch above fixes the open_page function (which opens the notebook in the browser) to use the standard sage mechanism for opening an external app instead of the previously hard-coded way.  The sage-scripts patch changes sage-env so that recursively run sage sessions do not clobber the saved original LD_LIBRARY environment variable.



---

archive/issue_comments_014336.json:
```json
{
    "body": "Both patches look good to me. Positive review. Thanks for the excellent work.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T04:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14336",
    "user": "mabshoff"
}
```

Both patches look good to me. Positive review. Thanks for the excellent work.

Cheers,

Michael



---

archive/issue_comments_014337.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T04:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14337",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014338.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T04:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2182#issuecomment-14338",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
