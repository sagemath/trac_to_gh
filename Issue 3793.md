# Issue 3793: Some elliptic curve doctests fail when the optional database is installed

archive/issues_003793.json:
```json
{
    "body": "Assignee: was\n\nA few of the doctests in `ell_rational_field.py` fail when the optional package database_cremona_ellcurve-20071019 is installed, mainly because for curves in the database the gens() as supplied by the database may differ from those computed on the fly.  (In almost all cases the generators are not uniquely determined, being the generators of a finitely-generated abelian group.  We have put some thought into how to make the generators canonical but have not yet succeeded.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3793\n\n",
    "created_at": "2008-08-09T12:51:34Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "bug"
    ],
    "title": "Some elliptic curve doctests fail when the optional database is installed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3793",
    "user": "cremona"
}
```
Assignee: was

A few of the doctests in `ell_rational_field.py` fail when the optional package database_cremona_ellcurve-20071019 is installed, mainly because for curves in the database the gens() as supplied by the database may differ from those computed on the fly.  (In almost all cases the generators are not uniquely determined, being the generators of a finitely-generated abelian group.  We have put some thought into how to make the generators canonical but have not yet succeeded.)


Issue created by migration from https://trac.sagemath.org/ticket/3793





---

archive/issue_comments_026969.json:
```json
{
    "body": "Attachment [10109.patch](tarball://root/attachments/some-uuid/ticket3793/10109.patch) by cremona created at 2008-08-09 12:54:54\n\nTo test this you should really test the doctests in ell_rational_field.py both before and after installing the database.",
    "created_at": "2008-08-09T12:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3793#issuecomment-26969",
    "user": "cremona"
}
```

Attachment [10109.patch](tarball://root/attachments/some-uuid/ticket3793/10109.patch) by cremona created at 2008-08-09 12:54:54

To test this you should really test the doctests in ell_rational_field.py both before and after installing the database.



---

archive/issue_comments_026970.json:
```json
{
    "body": "I ran the tests on 3.0.6 before and after installing the database, *without* applying the patch, and both tests passed everything.  So... is this really necessary?\n\nBut I still think this looks good and should be applied, since it addresses some ambiguity that could be annoying.",
    "created_at": "2008-08-10T20:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3793#issuecomment-26970",
    "user": "ncalexan"
}
```

I ran the tests on 3.0.6 before and after installing the database, *without* applying the patch, and both tests passed everything.  So... is this really necessary?

But I still think this looks good and should be applied, since it addresses some ambiguity that could be annoying.



---

archive/issue_comments_026971.json:
```json
{
    "body": "The point is that there was randomness in the old doctests:  whenever they use E.gens() where E is an elliptic curve we cannot guarantee that the same gens are computed (on different systems, etc).  As a special case of this ambiguity, the gens obtained from the database (which don't change! -- or at least ont very rarely, e.g. if they are found to be wrong)  may not agree with computed gens.\n\nI dealt with this by either inserting \"# random\", or by using explicit points instead of gens().\n\nI hope that with this explanation you can give this (admittedly rather trivial) patch a positive review.",
    "created_at": "2008-08-10T21:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3793#issuecomment-26971",
    "user": "cremona"
}
```

The point is that there was randomness in the old doctests:  whenever they use E.gens() where E is an elliptic curve we cannot guarantee that the same gens are computed (on different systems, etc).  As a special case of this ambiguity, the gens obtained from the database (which don't change! -- or at least ont very rarely, e.g. if they are found to be wrong)  may not agree with computed gens.

I dealt with this by either inserting "# random", or by using explicit points instead of gens().

I hope that with this explanation you can give this (admittedly rather trivial) patch a positive review.



---

archive/issue_comments_026972.json:
```json
{
    "body": "ok, so it already has a positive review!  Thanks!",
    "created_at": "2008-08-10T21:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3793#issuecomment-26972",
    "user": "cremona"
}
```

ok, so it already has a positive review!  Thanks!



---

archive/issue_comments_026973.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T04:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3793#issuecomment-26973",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026974.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-11T04:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3793#issuecomment-26974",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1
