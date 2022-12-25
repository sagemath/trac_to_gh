# Issue 3019: Integrate Frobby into Sage

archive/issues_003019.json:
```json
{
    "body": "Assignee: broune\n\nKeywords: monomial ideal, decomposition, frobby, spkg\n\nThis ticket is about improving the Frobby spkg (attached) enough that it is suitable for inclusion as a standard component of Sage. Frobby is a software system for performing computations on monomial ideals, such as computing minimal generators, colons, intersections, irreducible decomposition, maximal standard monomials, irreducible decomposition and Alexander dual.\n\nThe point of such a program is that these operations can be performed incomparably faster on monomial ideals than on general multivariate ideals, and performing these operations on monomial ideals is a useful computation. Frobby is the fastest program today on these kinds of problems. This is especially true for it current main feature, which is to compute irreducible decomposition of monomial ideals, which is documented in the Slice paper preprint at www.broune.com/papers\n\nFrobby is written in C++ and is licensed as GPL v. 2.0 or later. It depends only on GMP, and is available at www.broune.com/frobby/ . It builds using a makefile with no user interaction, and there is a makefile target for creating a statically linked library. It is developed on Cygwin and Mac OS 10.5. It includes a large automated test suite available as a makefile target. The functionality is exposed as a command-line program, and as a C++ header file that references no internal data structures.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3019\n\n",
    "created_at": "2008-04-24T18:06:43Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Integrate Frobby into Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3019",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```
Assignee: broune

Keywords: monomial ideal, decomposition, frobby, spkg

This ticket is about improving the Frobby spkg (attached) enough that it is suitable for inclusion as a standard component of Sage. Frobby is a software system for performing computations on monomial ideals, such as computing minimal generators, colons, intersections, irreducible decomposition, maximal standard monomials, irreducible decomposition and Alexander dual.

The point of such a program is that these operations can be performed incomparably faster on monomial ideals than on general multivariate ideals, and performing these operations on monomial ideals is a useful computation. Frobby is the fastest program today on these kinds of problems. This is especially true for it current main feature, which is to compute irreducible decomposition of monomial ideals, which is documented in the Slice paper preprint at www.broune.com/papers

Frobby is written in C++ and is licensed as GPL v. 2.0 or later. It depends only on GMP, and is available at www.broune.com/frobby/ . It builds using a makefile with no user interaction, and there is a makefile target for creating a statically linked library. It is developed on Cygwin and Mac OS 10.5. It includes a large automated test suite available as a makefile target. The functionality is exposed as a command-line program, and as a C++ header file that references no internal data structures.

Issue created by migration from https://trac.sagemath.org/ticket/3019





---

archive/issue_comments_020701.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-04-24T21:13:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3019#issuecomment-20701",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_020702.json:
```json
{
    "body": "This is a dupe of #3018.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-24T21:13:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3019#issuecomment-20702",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a dupe of #3018.

Cheers,

Michael



---

archive/issue_events_003224.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-24T21:13:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3019",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3019#event-3224"
}
```
