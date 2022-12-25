# Issue 2886: change an error message

archive/issues_002886.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen you crash Sage you get this error message:\n\n```\n**********************************************************************\n\nOops, SAGE crashed. We do our best to make it stable, but...\n\nA crash report was automatically generated with the following information:\n  - A verbatim copy of the crash traceback.\n  - A copy of your input history during this session.\n  - Data on your current SAGE configuration.\n\nIt was left in the file named:\n\t'/Users/was/.sage/ipython/SAGE_crash_report.txt'\nIf you can email this file to the developers, the information in it will help\nthem in understanding and correcting the problem.\n\nYou can mail it to: William Stein at wstein@gmail.com\nwith the subject 'SAGE Crash Report'.\n\nIf you want to do it now, the following command will work (under Unix):\nmail -s 'SAGE Crash Report' wstein@gmail.com < /Users/was/.sage/ipython/SAGE_crash_report.txt\n\nTo ensure accurate tracking of this issue, please file a report about it at:\nhttp://www.sagemath.org:9002/sage_trac\n\n```\n\nIssues: \n  (1) People need accounts to file a report.  It might be much better to tell people to report to sage-support.\n\n  (2) the url for trac is now trac.sagemath.org/sage_trac\n\n--\n\nI think doing (2) would be fine to fix this ticket.\n\nWilliam\n\nIssue created by migration from https://trac.sagemath.org/ticket/2886\n\n",
    "created_at": "2008-04-12T00:09:35Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "change an error message",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2886",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

When you crash Sage you get this error message:

```
**********************************************************************

Oops, SAGE crashed. We do our best to make it stable, but...

A crash report was automatically generated with the following information:
  - A verbatim copy of the crash traceback.
  - A copy of your input history during this session.
  - Data on your current SAGE configuration.

It was left in the file named:
	'/Users/was/.sage/ipython/SAGE_crash_report.txt'
If you can email this file to the developers, the information in it will help
them in understanding and correcting the problem.

You can mail it to: William Stein at wstein@gmail.com
with the subject 'SAGE Crash Report'.

If you want to do it now, the following command will work (under Unix):
mail -s 'SAGE Crash Report' wstein@gmail.com < /Users/was/.sage/ipython/SAGE_crash_report.txt

To ensure accurate tracking of this issue, please file a report about it at:
http://www.sagemath.org:9002/sage_trac

```

Issues: 
  (1) People need accounts to file a report.  It might be much better to tell people to report to sage-support.

  (2) the url for trac is now trac.sagemath.org/sage_trac

--

I think doing (2) would be fine to fix this ticket.

William

Issue created by migration from https://trac.sagemath.org/ticket/2886





---

archive/issue_comments_019806.json:
```json
{
    "body": "Attachment [2886.patch](tarball://root/attachments/some-uuid/ticket2886/2886.patch) by @mwhansen created at 2008-04-12 07:45:13",
    "created_at": "2008-04-12T07:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2886#issuecomment-19806",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2886.patch](tarball://root/attachments/some-uuid/ticket2886/2886.patch) by @mwhansen created at 2008-04-12 07:45:13



---

archive/issue_comments_019807.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-12T07:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2886#issuecomment-19807",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019808.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-04-12T07:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2886#issuecomment-19808",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_019809.json:
```json
{
    "body": "The patch applies to hg_scripts.",
    "created_at": "2008-04-12T07:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2886#issuecomment-19809",
    "user": "https://github.com/mwhansen"
}
```

The patch applies to hg_scripts.



---

archive/issue_comments_019810.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2008-04-15T16:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2886#issuecomment-19810",
    "user": "https://github.com/ncalexan"
}
```

Fine by me.



---

archive/issue_comments_019811.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-15T20:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2886#issuecomment-19811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha6



---

archive/issue_events_006607.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-15T20:01:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2886",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2886#event-6607"
}
```



---

archive/issue_comments_019812.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T20:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2886#issuecomment-19812",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
