# Issue 4956: html accents in the notebook aren't saved properly on second load

archive/issues_004956.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @mwhansen\n\nReported in http://groups.google.com/group/sage-support/browse_thread/thread/60a863def66c05a1\n\n```\nThis works \nhtml(r'Donde $\\Sigma$ es la sumatoria de los n&uacute;meros... etc.' ) \nbut only works the first time. If you save & quit your work, after \ntrying again it fails. This is because when saving it converts \n\"n&uacute;meros\" to \"n\u00fameros\". \n```\n\n\nNote that this issue might be closely related to some other notebook tickets.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4956\n\n",
    "created_at": "2009-01-08T20:32:42Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "html accents in the notebook aren't saved properly on second load",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4956",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: boothby

CC:  @williamstein @mwhansen

Reported in http://groups.google.com/group/sage-support/browse_thread/thread/60a863def66c05a1

```
This works 
html(r'Donde $\Sigma$ es la sumatoria de los n&uacute;meros... etc.' ) 
but only works the first time. If you save & quit your work, after 
trying again it fails. This is because when saving it converts 
"n&uacute;meros" to "números". 
```


Note that this issue might be closely related to some other notebook tickets.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4956





---

archive/issue_comments_037601.json:
```json
{
    "body": "mhansen says this is fixed at #5564.",
    "created_at": "2009-05-30T07:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4956#issuecomment-37601",
    "user": "https://github.com/jasongrout"
}
```

mhansen says this is fixed at #5564.



---

archive/issue_comments_037602.json:
```json
{
    "body": "Ticket #5564 has been closed because it addresses many issues. The issues it addresses are also considered by other tickets. If anyone is working on this ticket, please refer to #5564 for code and inspiration.",
    "created_at": "2009-08-26T19:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4956#issuecomment-37602",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ticket #5564 has been closed because it addresses many issues. The issues it addresses are also considered by other tickets. If anyone is working on this ticket, please refer to #5564 for code and inspiration.



---

archive/issue_comments_037603.json:
```json
{
    "body": "This works for me now, since the output files now have the magic utf-8 comment. Please close this.",
    "created_at": "2009-11-15T12:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4956#issuecomment-37603",
    "user": "https://github.com/TimDumol"
}
```

This works for me now, since the output files now have the magic utf-8 comment. Please close this.



---

archive/issue_comments_037604.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-11-15T13:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4956#issuecomment-37604",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_005197.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-11-15T13:47:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4956",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4956#event-5197"
}
```
