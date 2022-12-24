# Issue 3847: can't make vector of ints

archive/issues_003847.json:
```json
{
    "body": "Assignee: tbd\n\nsage: vector([int(0)])\nTraceback (most recent call last):\n...\nTypeError: unable to find a common ring for all elements\n\nShouldn't ints be coerced to Integers?\n\nIssue created by migration from https://trac.sagemath.org/ticket/3847\n\n",
    "created_at": "2008-08-14T04:24:35Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "can't make vector of ints",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3847",
    "user": "@saliola"
}
```
Assignee: tbd

sage: vector([int(0)])
Traceback (most recent call last):
...
TypeError: unable to find a common ring for all elements

Shouldn't ints be coerced to Integers?

Issue created by migration from https://trac.sagemath.org/ticket/3847





---

archive/issue_comments_027365.json:
```json
{
    "body": "Attachment [3847-vector.patch](tarball://root/attachments/some-uuid/ticket3847/3847-vector.patch) by @aghitza created at 2008-09-08 10:47:40\n\nThis issue has also come up in other guises on sage-devel or sage-support (can't seem to be able to find the threads right now, though).\n\nIt all boils down to Sequence(), which takes a list of things and returns a sequence of things that lie in the same \"universe\", if canonical coercions are possible.  So if you give it a list containing an RDF, an Integer, and a Rational, it will give you back a sequence of three RDF's.  The problem is with the builtin Python types (int, long, float, complex), for which we of course have no coercions.  So given a bunch of ints, Sequence tries to see where in the Sage hierarchy they fit, finds nothing, and sends them back without a common \"universe\".  This makes vector() throw an exception, because a vector should be over a ring.\n\nThe patch fixes this by giving Sequence() an optional parameter use_sage_types, defaulting to False.  If the parameter is True, Sequence() catches the builtin Python types and makes them into the appropriate Sage objects, then carries on.  I am making vector() always pass use_sage_types=True to Sequence().  This fixes the unpleasant behavior reported in this ticket, and gives vector() a bit more flexibility -- see the new doctests for more examples.\n\nSequence() is a fairly fundamental class and I didn't want to change its default behavior for fear of speed degradation in places other than vector().",
    "created_at": "2008-09-08T10:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3847#issuecomment-27365",
    "user": "@aghitza"
}
```

Attachment [3847-vector.patch](tarball://root/attachments/some-uuid/ticket3847/3847-vector.patch) by @aghitza created at 2008-09-08 10:47:40

This issue has also come up in other guises on sage-devel or sage-support (can't seem to be able to find the threads right now, though).

It all boils down to Sequence(), which takes a list of things and returns a sequence of things that lie in the same "universe", if canonical coercions are possible.  So if you give it a list containing an RDF, an Integer, and a Rational, it will give you back a sequence of three RDF's.  The problem is with the builtin Python types (int, long, float, complex), for which we of course have no coercions.  So given a bunch of ints, Sequence tries to see where in the Sage hierarchy they fit, finds nothing, and sends them back without a common "universe".  This makes vector() throw an exception, because a vector should be over a ring.

The patch fixes this by giving Sequence() an optional parameter use_sage_types, defaulting to False.  If the parameter is True, Sequence() catches the builtin Python types and makes them into the appropriate Sage objects, then carries on.  I am making vector() always pass use_sage_types=True to Sequence().  This fixes the unpleasant behavior reported in this ticket, and gives vector() a bit more flexibility -- see the new doctests for more examples.

Sequence() is a fairly fundamental class and I didn't want to change its default behavior for fear of speed degradation in places other than vector().



---

archive/issue_comments_027366.json:
```json
{
    "body": "Review: I think this has been done very well.   The default behaviour for Sequence() has not changed, so there should be no effect anywhere other than for the Vector constructor, which does what it should.\n\nThe patch applies cleanly to 3.1.2.rc0 and all doctests in sage.structure and sage.modules pass.\n\nThere may be other places where Sequence() is used where this functionality would be useful.",
    "created_at": "2008-09-08T13:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3847#issuecomment-27366",
    "user": "@JohnCremona"
}
```

Review: I think this has been done very well.   The default behaviour for Sequence() has not changed, so there should be no effect anywhere other than for the Vector constructor, which does what it should.

The patch applies cleanly to 3.1.2.rc0 and all doctests in sage.structure and sage.modules pass.

There may be other places where Sequence() is used where this functionality would be useful.



---

archive/issue_comments_027367.json:
```json
{
    "body": "Oops, this patch nearly escaped. Note that the two spaces between positive and review let this review escape from the report.\n\nCheers,\n\nMichal",
    "created_at": "2008-09-14T13:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3847#issuecomment-27367",
    "user": "mabshoff"
}
```

Oops, this patch nearly escaped. Note that the two spaces between positive and review let this review escape from the report.

Cheers,

Michal



---

archive/issue_comments_027368.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-15T03:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3847#issuecomment-27368",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027369.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc4",
    "created_at": "2008-09-15T03:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3847#issuecomment-27369",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc4
