# Issue 4688: wrap pari functions idealstar and ideallog

archive/issues_004688.json:
```json
{
    "body": "Assignee: was\n\nCC:  m.t.aranes@warwick.ac.uk\n\nIf I is an ideal in the ring of integers R of a number field K, then the pari functions idealstar(K,I) returns the group `(R/I)^*` in the form of an abstract abelian group (order, invariants, and a list of generators).  And ideallog() computes the discrete log with respect to I, i.e. given a in K with valuation 0 at all primes dividing I, returns a vector representing a mod I as an element of that abstract abelian group.\n\nIt would be very useful to have these wrapped in Sage.  They appear in libs/pari/decl.pxi already so that should not be hard.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4688\n\n",
    "created_at": "2008-12-03T20:54:42Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "wrap pari functions idealstar and ideallog",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4688",
    "user": "cremona"
}
```
Assignee: was

CC:  m.t.aranes@warwick.ac.uk

If I is an ideal in the ring of integers R of a number field K, then the pari functions idealstar(K,I) returns the group `(R/I)^*` in the form of an abstract abelian group (order, invariants, and a list of generators).  And ideallog() computes the discrete log with respect to I, i.e. given a in K with valuation 0 at all primes dividing I, returns a vector representing a mod I as an element of that abstract abelian group.

It would be very useful to have these wrapped in Sage.  They appear in libs/pari/decl.pxi already so that should not be hard.


Issue created by migration from https://trac.sagemath.org/ticket/4688





---

archive/issue_comments_035336.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-17T12:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35336",
    "user": "AlexGhitza"
}
```

Attachment



---

archive/issue_comments_035337.json:
```json
{
    "body": "Maite Aranes wrote the code for wrapping the pari functions into Sage, and I reviewed it and added docstrings/doctests.\n\nWe need someone to review the docstrings, then this is ready to go.",
    "created_at": "2009-02-17T12:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35337",
    "user": "AlexGhitza"
}
```

Maite Aranes wrote the code for wrapping the pari functions into Sage, and I reviewed it and added docstrings/doctests.

We need someone to review the docstrings, then this is ready to go.



---

archive/issue_comments_035338.json:
```json
{
    "body": "Postive review (and thanks to Alex for doing a good job on this).  the patch applies fine to 3.3.rc0 and the tests in sage/libs/pari pass.\n\nIt will be easy to test this properly until we have Sage-level functions to access them, but that is being worked on and will be in a separate ticket, so this patch should PASS.",
    "created_at": "2009-02-17T17:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35338",
    "user": "cremona"
}
```

Postive review (and thanks to Alex for doing a good job on this).  the patch applies fine to 3.3.rc0 and the tests in sage/libs/pari pass.

It will be easy to test this properly until we have Sage-level functions to access them, but that is being worked on and will be in a separate ticket, so this patch should PASS.



---

archive/issue_comments_035339.json:
```json
{
    "body": "Ticket #5306 will handle the user interface to these from with Sage's own classes for number fields and ideals.",
    "created_at": "2009-02-18T17:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35339",
    "user": "cremona"
}
```

Ticket #5306 will handle the user interface to these from with Sage's own classes for number fields and ideals.



---

archive/issue_comments_035340.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T06:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35340",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_comments_035341.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T06:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4688#issuecomment-35341",
    "user": "mabshoff"
}
```

Resolution: fixed
