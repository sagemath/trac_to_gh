# Issue 6300: doctest fix related to singular upgrad; needed on 32-bit OS X intel, at least (maybe all 32-bit)

archive/issues_006300.json:
```json
{
    "body": "Assignee: tbd\n\n> >> File\n> >> \"/Users/was/build/sage-4.0.2.rc0/devel/sage/sage/libs/singular/singular.\n\n> >>pyx \", line 501:\n> >>     sage: P(2^32-1)\n\n> >> Expected:\n> >>     -1\n\n> >> Got:\n> >>     4294967295\n\n> >\n> > Is that with my the fix at\n\n> >\n> >  http://trac.sagemath.org/sage_trac/attachment/ticket/6051/singular_exp_o\n\n> >verflow.patch\n> >\n> > or without? It seems (since you are using a 32-bit system) all that needs\n> > to be done is to fix the doctest.\n\n>\n> No, I had not applied your patch.  However, I just did, and the above\n> issue remains.\n\n\nYes, the issue remains. One should change the doctest, i.e. the behaviour we\nexpect now is the wrong behaviour.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6300\n\n",
    "created_at": "2009-06-15T15:45:30Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "doctest fix related to singular upgrad; needed on 32-bit OS X intel, at least (maybe all 32-bit)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6300",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

> >> File
> >> "/Users/was/build/sage-4.0.2.rc0/devel/sage/sage/libs/singular/singular.

> >>pyx ", line 501:
> >>     sage: P(2^32-1)

> >> Expected:
> >>     -1

> >> Got:
> >>     4294967295

> >
> > Is that with my the fix at

> >
> >  http://trac.sagemath.org/sage_trac/attachment/ticket/6051/singular_exp_o

> >verflow.patch
> >
> > or without? It seems (since you are using a 32-bit system) all that needs
> > to be done is to fix the doctest.

>
> No, I had not applied your patch.  However, I just did, and the above
> issue remains.


Yes, the issue remains. One should change the doctest, i.e. the behaviour we
expect now is the wrong behaviour.

Issue created by migration from https://trac.sagemath.org/ticket/6300





---

archive/issue_comments_050165.json:
```json
{
    "body": "Attachment [trac_6300.patch](tarball://root/attachments/some-uuid/ticket6300/trac_6300.patch) by @malb created at 2009-06-15 15:58:25\n\nPatch depends on hotfix at #6051.",
    "created_at": "2009-06-15T15:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6300#issuecomment-50165",
    "user": "https://github.com/malb"
}
```

Attachment [trac_6300.patch](tarball://root/attachments/some-uuid/ticket6300/trac_6300.patch) by @malb created at 2009-06-15 15:58:25

Patch depends on hotfix at #6051.



---

archive/issue_comments_050166.json:
```json
{
    "body": "With this patch and the hotfix from #6051 all doctests pass on sage.math FWIW.",
    "created_at": "2009-06-15T16:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6300#issuecomment-50166",
    "user": "https://github.com/malb"
}
```

With this patch and the hotfix from #6051 all doctests pass on sage.math FWIW.



---

archive/issue_comments_050167.json:
```json
{
    "body": "merged into 4.0.2.rc1",
    "created_at": "2009-06-15T23:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6300#issuecomment-50167",
    "user": "https://github.com/williamstein"
}
```

merged into 4.0.2.rc1



---

archive/issue_comments_050168.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-15T23:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6300#issuecomment-50168",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_014731.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-06-15T23:57:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6300",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6300#event-14731"
}
```
