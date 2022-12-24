# Issue 3018: Integrate Frobby into Sage

archive/issues_003018.json:
```json
{
    "body": "Assignee: broune\n\nKeywords: monomial ideal, decomposition, frobby, spkg\n\nThis ticket is about improving the Frobby spkg (attached) enough that it is suitable for inclusion as a standard component of Sage. Frobby is a software system for performing computations on monomial ideals, such as computing minimal generators, colons, intersections, irreducible decomposition, maximal standard monomials, irreducible decomposition and Alexander dual.\n\nThe point of such a program is that these operations can be performed incomparably faster on monomial ideals than on general multivariate ideals, and performing these operations on monomial ideals is a useful computation. Frobby is the fastest program today on these kinds of problems. This is especially true for it current main feature, which is to compute irreducible decomposition of monomial ideals, which is documented in the Slice paper preprint at www.broune.com/papers\n\nFrobby is written in C++ and is licensed as GPL v. 2.0 or later. It depends only on GMP, and is available at www.broune.com/frobby/ . It builds using a makefile with no user interaction, and there is a makefile target for creating a statically linked library. It is developed on Cygwin and Mac OS 10.5. It includes a large automated test suite available as a makefile target. The functionality is exposed as a command-line program, and as a C++ header file that references no internal data structures.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3018\n\n",
    "created_at": "2008-04-24T18:06:24Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Integrate Frobby into Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3018",
    "user": "broune"
}
```
Assignee: broune

Keywords: monomial ideal, decomposition, frobby, spkg

This ticket is about improving the Frobby spkg (attached) enough that it is suitable for inclusion as a standard component of Sage. Frobby is a software system for performing computations on monomial ideals, such as computing minimal generators, colons, intersections, irreducible decomposition, maximal standard monomials, irreducible decomposition and Alexander dual.

The point of such a program is that these operations can be performed incomparably faster on monomial ideals than on general multivariate ideals, and performing these operations on monomial ideals is a useful computation. Frobby is the fastest program today on these kinds of problems. This is especially true for it current main feature, which is to compute irreducible decomposition of monomial ideals, which is documented in the Slice paper preprint at www.broune.com/papers

Frobby is written in C++ and is licensed as GPL v. 2.0 or later. It depends only on GMP, and is available at www.broune.com/frobby/ . It builds using a makefile with no user interaction, and there is a makefile target for creating a statically linked library. It is developed on Cygwin and Mac OS 10.5. It includes a large automated test suite available as a makefile target. The functionality is exposed as a command-line program, and as a C++ header file that references no internal data structures.

Issue created by migration from https://trac.sagemath.org/ticket/3018





---

archive/issue_comments_020735.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-01T01:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3018#issuecomment-20735",
    "user": "broune"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020736.json:
```json
{
    "body": "This is an interface to and spkg for Frobby that uses popen for communication in the same way that the gfan interface does. It currently implements irreducible decomposition for monomial ideals, which was the computation that initially motivated the development of Frobby.",
    "created_at": "2008-05-01T01:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3018#issuecomment-20736",
    "user": "broune"
}
```

This is an interface to and spkg for Frobby that uses popen for communication in the same way that the gfan interface does. It currently implements irreducible decomposition for monomial ideals, which was the computation that initially motivated the development of Frobby.



---

archive/issue_comments_020737.json:
```json
{
    "body": "For the record: We usually do not attach spkgs to track ticket, but put them up on an external website and then link them from a ticket via the comment section.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-01T03:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3018#issuecomment-20737",
    "user": "mabshoff"
}
```

For the record: We usually do not attach spkgs to track ticket, but put them up on an external website and then link them from a ticket via the comment section.

Cheers,

Michael



---

archive/issue_comments_020738.json:
```json
{
    "body": "New spkg available at\n\nhttp://www.broune.com/frobby/frobby-0.7.6.spkg\n\nThis version has several improvements, most of which have been done by Michael Mabshoff.",
    "created_at": "2008-05-20T00:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3018#issuecomment-20738",
    "user": "broune"
}
```

New spkg available at

http://www.broune.com/frobby/frobby-0.7.6.spkg

This version has several improvements, most of which have been done by Michael Mabshoff.



---

archive/issue_comments_020739.json:
```json
{
    "body": "This is the only patch needed.",
    "created_at": "2008-05-20T00:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3018#issuecomment-20739",
    "user": "broune"
}
```

This is the only patch needed.



---

archive/issue_comments_020740.json:
```json
{
    "body": "Attachment [frobby-0.7.6.patch](tarball://root/attachments/some-uuid/ticket3018/frobby-0.7.6.patch) by mhansen created at 2008-05-22 10:36:59\n\nLooks good to me.",
    "created_at": "2008-05-22T10:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3018#issuecomment-20740",
    "user": "mhansen"
}
```

Attachment [frobby-0.7.6.patch](tarball://root/attachments/some-uuid/ticket3018/frobby-0.7.6.patch) by mhansen created at 2008-05-22 10:36:59

Looks good to me.



---

archive/issue_comments_020741.json:
```json
{
    "body": "Mhansen gave the patch a positive review and the spkg is good according to me :)\n\nCheers,\n\nMichael",
    "created_at": "2008-05-22T23:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3018#issuecomment-20741",
    "user": "mabshoff"
}
```

Mhansen gave the patch a positive review and the spkg is good according to me :)

Cheers,

Michael



---

archive/issue_comments_020742.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc0",
    "created_at": "2008-05-22T23:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3018#issuecomment-20742",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.rc0



---

archive/issue_comments_020743.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-22T23:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3018#issuecomment-20743",
    "user": "mabshoff"
}
```

Resolution: fixed
