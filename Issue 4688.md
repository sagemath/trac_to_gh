# Issue 4688: wrap pari functions idealstar and ideallog

archive/issues_004688.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  m.t.aranes@warwick.ac.uk\n\nIf I is an ideal in the ring of integers R of a number field K, then the pari functions idealstar(K,I) returns the group `(R/I)^*` in the form of an abstract abelian group (order, invariants, and a list of generators).  And ideallog() computes the discrete log with respect to I, i.e. given a in K with valuation 0 at all primes dividing I, returns a vector representing a mod I as an element of that abstract abelian group.\n\nIt would be very useful to have these wrapped in Sage.  They appear in libs/pari/decl.pxi already so that should not be hard.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4688\n\n",
    "created_at": "2008-12-03T20:54:42Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "wrap pari functions idealstar and ideallog",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4688",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

CC:  m.t.aranes@warwick.ac.uk

If I is an ideal in the ring of integers R of a number field K, then the pari functions idealstar(K,I) returns the group `(R/I)^*` in the form of an abstract abelian group (order, invariants, and a list of generators).  And ideallog() computes the discrete log with respect to I, i.e. given a in K with valuation 0 at all primes dividing I, returns a vector representing a mod I as an element of that abstract abelian group.

It would be very useful to have these wrapped in Sage.  They appear in libs/pari/decl.pxi already so that should not be hard.


Issue created by migration from https://trac.sagemath.org/ticket/4688





---

archive/issue_comments_035267.json:
```json
{
    "body": "Attachment [trac_4688.patch](tarball://root/attachments/some-uuid/ticket4688/trac_4688.patch) by @aghitza created at 2009-02-17 12:13:00",
    "created_at": "2009-02-17T12:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35267",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_4688.patch](tarball://root/attachments/some-uuid/ticket4688/trac_4688.patch) by @aghitza created at 2009-02-17 12:13:00



---

archive/issue_comments_035268.json:
```json
{
    "body": "Maite Aranes wrote the code for wrapping the pari functions into Sage, and I reviewed it and added docstrings/doctests.\n\nWe need someone to review the docstrings, then this is ready to go.",
    "created_at": "2009-02-17T12:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35268",
    "user": "https://github.com/aghitza"
}
```

Maite Aranes wrote the code for wrapping the pari functions into Sage, and I reviewed it and added docstrings/doctests.

We need someone to review the docstrings, then this is ready to go.



---

archive/issue_comments_035269.json:
```json
{
    "body": "Postive review (and thanks to Alex for doing a good job on this).  the patch applies fine to 3.3.rc0 and the tests in sage/libs/pari pass.\n\nIt will be easy to test this properly until we have Sage-level functions to access them, but that is being worked on and will be in a separate ticket, so this patch should PASS.",
    "created_at": "2009-02-17T17:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35269",
    "user": "https://github.com/JohnCremona"
}
```

Postive review (and thanks to Alex for doing a good job on this).  the patch applies fine to 3.3.rc0 and the tests in sage/libs/pari pass.

It will be easy to test this properly until we have Sage-level functions to access them, but that is being worked on and will be in a separate ticket, so this patch should PASS.



---

archive/issue_comments_035270.json:
```json
{
    "body": "Ticket #5306 will handle the user interface to these from with Sage's own classes for number fields and ideals.",
    "created_at": "2009-02-18T17:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35270",
    "user": "https://github.com/JohnCremona"
}
```

Ticket #5306 will handle the user interface to these from with Sage's own classes for number fields and ideals.



---

archive/issue_comments_035271.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T06:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35271",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_comments_035272.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T06:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35272",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004934.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-20T06:06:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4688#event-4934"
}
```
