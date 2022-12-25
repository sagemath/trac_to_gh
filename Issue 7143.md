# Issue 7143: We must check if the version of 'make' found is gnu 'make'

archive/issues_007143.json:
```json
{
    "body": "Assignee: tbd\n\nSage needs GNU make (at least I know neither Sun's 'make' in Solaris or HP's make in HP-UX are not suitable), so we need to check that 'make' is in fact gnu 'make', and not some other version of make. \n\nOn HP-UX there does not appear to be a version of GNU make on the system. With Solaris, there  is a version called 'gmake' at /usr/sfw/bin/gmake. \n\nOne way or another, we need to make sure that the 'make' that Sage finds is the GNU version. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7143\n\n",
    "created_at": "2009-10-06T17:08:29Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "We must check if the version of 'make' found is gnu 'make'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7143",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Sage needs GNU make (at least I know neither Sun's 'make' in Solaris or HP's make in HP-UX are not suitable), so we need to check that 'make' is in fact gnu 'make', and not some other version of make. 

On HP-UX there does not appear to be a version of GNU make on the system. With Solaris, there  is a version called 'gmake' at /usr/sfw/bin/gmake. 

One way or another, we need to make sure that the 'make' that Sage finds is the GNU version. 

Issue created by migration from https://trac.sagemath.org/ticket/7143





---

archive/issue_comments_059074.json:
```json
{
    "body": "Fixed by #7352",
    "created_at": "2009-11-20T06:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7143#issuecomment-59074",
    "user": "https://github.com/mwhansen"
}
```

Fixed by #7352



---

archive/issue_comments_059075.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-20T06:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7143#issuecomment-59075",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
