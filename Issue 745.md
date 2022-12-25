# Issue 745: update the version of FLINT that is in Sage

archive/issues_000745.json:
```json
{
    "body": "Assignee: somebody\n\n```\nGuys,\n\nI've removed all known bugs from fmpz_poly, including the memory\nmanagement ones I referred to previously. This includes some bugs\nwhich should affect the FLINT polynomial multiplication in SAGE (but\napparently don't). They were in all the set_coeff type functions. To\nbe honest I'm not sure how you got the FLINT wrapper to work. You must\nhave just been lucky in the way you implemented it.\n\nI've also now removed all the bugs I know of in the division\nfunctions. There's also some memory leaks removed from the polynomial\ndivision test code.\n\nIf you find any further bugs please report them. In the mean time\nrevision 1010 is what you want to use in SAGE with the respective\nwrappers that you guys wrote.\n\nTime to start working on Z_poly.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/745\n\n",
    "closed_at": "2007-10-04T03:15:28Z",
    "created_at": "2007-09-24T20:48:19Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "update the version of FLINT that is in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/745",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

```
Guys,

I've removed all known bugs from fmpz_poly, including the memory
management ones I referred to previously. This includes some bugs
which should affect the FLINT polynomial multiplication in SAGE (but
apparently don't). They were in all the set_coeff type functions. To
be honest I'm not sure how you got the FLINT wrapper to work. You must
have just been lucky in the way you implemented it.

I've also now removed all the bugs I know of in the division
functions. There's also some memory leaks removed from the polynomial
division test code.

If you find any further bugs please report them. In the mean time
revision 1010 is what you want to use in SAGE with the respective
wrappers that you guys wrote.

Time to start working on Z_poly.
```

Issue created by migration from https://trac.sagemath.org/ticket/745





---

archive/issue_events_002025.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T03:15:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/745",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/745#event-2025"
}
```



---

archive/issue_comments_004354.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T03:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/745#issuecomment-4354",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
