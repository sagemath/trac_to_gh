# Issue 1679: [with patch, with positive review] two documentation typos

archive/issues_001679.json:
```json
{
    "body": "Assignee: tba\n\n```\nFabio Tonti to sage-devel\n\t\nshow details 12:56 AM (20 minutes ago)\n\t\n\t\n\t\nReply\n\t\n\t\nThe page numbers are numbers in the pdf version (in parentheses the printed page numbers)\nI'm actually not sure about how to reference the page numbers...\n\npage 175 (162): ** instead of ^;\nthe pyx example says: \"sage: y(x) = x*sin(x**2)\"\nusing the \"**\" is nice for python, but isn't Sage emphasizing to use \"^\" instead?\n\npage 1843 (1830): ncols()... return number of \"rows\" instead of \"coloumns\";\nthe description for ncols() reads \"number of rows\" instead of \"number of coloumns\"\n\n\n\nBest wishes, Fabio\n```\n\nNOTES:\n   The first sin(x**2) above this from plot.py, and I agree with changing it to sin(x^2)\n\n   The second listed problem seems like a clear mistake. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1679\n\n",
    "closed_at": "2008-01-13T14:58:26Z",
    "created_at": "2008-01-04T09:20:27Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch, with positive review] two documentation typos",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1679",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba

```
Fabio Tonti to sage-devel
	
show details 12:56 AM (20 minutes ago)
	
	
	
Reply
	
	
The page numbers are numbers in the pdf version (in parentheses the printed page numbers)
I'm actually not sure about how to reference the page numbers...

page 175 (162): ** instead of ^;
the pyx example says: "sage: y(x) = x*sin(x**2)"
using the "**" is nice for python, but isn't Sage emphasizing to use "^" instead?

page 1843 (1830): ncols()... return number of "rows" instead of "coloumns";
the description for ncols() reads "number of rows" instead of "number of coloumns"



Best wishes, Fabio
```

NOTES:
   The first sin(x**2) above this from plot.py, and I agree with changing it to sin(x^2)

   The second listed problem seems like a clear mistake. 



Issue created by migration from https://trac.sagemath.org/ticket/1679





---

archive/issue_comments_010623.json:
```json
{
    "body": "Attachment [1679.patch](tarball://root/attachments/some-uuid/ticket1679/1679.patch) by @mwhansen created at 2008-01-13 13:53:33",
    "created_at": "2008-01-13T13:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1679#issuecomment-10623",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1679.patch](tarball://root/attachments/some-uuid/ticket1679/1679.patch) by @mwhansen created at 2008-01-13 13:53:33



---

archive/issue_comments_010624.json:
```json
{
    "body": "Looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-13T14:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1679#issuecomment-10624",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me.

Cheers,

Michael



---

archive/issue_comments_010625.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-13T14:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1679#issuecomment-10625",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010626.json:
```json
{
    "body": "Merged in Sage 2.10.alpha3.",
    "created_at": "2008-01-13T14:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1679#issuecomment-10626",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha3.



---

archive/issue_events_004127.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-13T14:58:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1679",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1679#event-4127"
}
```
