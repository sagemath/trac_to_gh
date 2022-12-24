# Issue 9057: Supporting elliptic curves over function fields and their L-functions

archive/issues_009057.json:
```json
{
    "body": "Assignee: cremona\n\nKeywords: elliptic curves, L-functions, function fields\n\nSage currently cannot compute L-functions of elliptic curves over function fields. Chris Hall and I have developed Cython code so that Sage can make use of our ELLFF (elliptic curve L-functions over function fields) library (written in C++ with NTL). The next step is to patch this into Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9057\n\n",
    "created_at": "2010-05-26T21:10:31Z",
    "labels": [
        "elliptic curves",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Supporting elliptic curves over function fields and their L-functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9057",
    "user": "salmanhb"
}
```
Assignee: cremona

Keywords: elliptic curves, L-functions, function fields

Sage currently cannot compute L-functions of elliptic curves over function fields. Chris Hall and I have developed Cython code so that Sage can make use of our ELLFF (elliptic curve L-functions over function fields) library (written in C++ with NTL). The next step is to patch this into Sage.

Issue created by migration from https://trac.sagemath.org/ticket/9057





---

archive/issue_comments_084037.json:
```json
{
    "body": "Installed ellff.pyx. This will allow you to compute L-functions of elliptic curves over F_q(t).\n\nWARNING: the interface is surely to change, especially in light of the following ticket:\n\n     [http://trac.sagemath.org/sage_trac/ticket/9054](http://trac.sagemath.org/sage_trac/ticket/9054)",
    "created_at": "2010-05-26T22:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9057#issuecomment-84037",
    "user": "salmanhb"
}
```

Installed ellff.pyx. This will allow you to compute L-functions of elliptic curves over F_q(t).

WARNING: the interface is surely to change, especially in light of the following ticket:

     [http://trac.sagemath.org/sage_trac/ticket/9054](http://trac.sagemath.org/sage_trac/ticket/9054)



---

archive/issue_comments_084038.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-26T22:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9057#issuecomment-84038",
    "user": "salmanhb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_084039.json:
```json
{
    "body": "Attachment [trac_9057_ellff.patch](tarball://root/attachments/some-uuid/ticket9057/trac_9057_ellff.patch) by salmanhb created at 2010-05-26 22:55:22\n\nInitial patch",
    "created_at": "2010-05-26T22:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9057#issuecomment-84039",
    "user": "salmanhb"
}
```

Attachment [trac_9057_ellff.patch](tarball://root/attachments/some-uuid/ticket9057/trac_9057_ellff.patch) by salmanhb created at 2010-05-26 22:55:22

Initial patch



---

archive/issue_comments_084040.json:
```json
{
    "body": "Attachment [trac_9057_ellff_ff.patch](tarball://root/attachments/some-uuid/ticket9057/trac_9057_ellff_ff.patch) by salmanhb created at 2010-05-28 04:22:14\n\nELLFF now uses FunctionField in #9054",
    "created_at": "2010-05-28T04:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9057#issuecomment-84040",
    "user": "salmanhb"
}
```

Attachment [trac_9057_ellff_ff.patch](tarball://root/attachments/some-uuid/ticket9057/trac_9057_ellff_ff.patch) by salmanhb created at 2010-05-28 04:22:14

ELLFF now uses FunctionField in #9054



---

archive/issue_comments_084041.json:
```json
{
    "body": "merges initial file with FunctionField functionality",
    "created_at": "2010-05-28T04:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9057#issuecomment-84041",
    "user": "salmanhb"
}
```

merges initial file with FunctionField functionality



---

archive/issue_comments_084042.json:
```json
{
    "body": "Attachment [trac_9057_ellff-part2.patch](tarball://root/attachments/some-uuid/ticket9057/trac_9057_ellff-part2.patch) by salmanhb created at 2010-05-28 20:48:02",
    "created_at": "2010-05-28T20:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9057#issuecomment-84042",
    "user": "salmanhb"
}
```

Attachment [trac_9057_ellff-part2.patch](tarball://root/attachments/some-uuid/ticket9057/trac_9057_ellff-part2.patch) by salmanhb created at 2010-05-28 20:48:02



---

archive/issue_comments_084043.json:
```json
{
    "body": "trac_9057_ellff-part2.patch adds doctests and resolves some bugs with the previous patches.",
    "created_at": "2010-05-28T20:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9057#issuecomment-84043",
    "user": "salmanhb"
}
```

trac_9057_ellff-part2.patch adds doctests and resolves some bugs with the previous patches.



---

archive/issue_comments_084044.json:
```json
{
    "body": "The requisite SPKG can be found here:\n\nhttp://sage.math.washington.edu/home/sbutt/ellff/ellff-0.1.spkg",
    "created_at": "2010-06-03T18:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9057#issuecomment-84044",
    "user": "salmanhb"
}
```

The requisite SPKG can be found here:

http://sage.math.washington.edu/home/sbutt/ellff/ellff-0.1.spkg



---

archive/issue_comments_084045.json:
```json
{
    "body": "This is now in PSAGE: http://code.google.com/p/purplesage/source/checkout",
    "created_at": "2010-10-26T22:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9057#issuecomment-84045",
    "user": "was"
}
```

This is now in PSAGE: http://code.google.com/p/purplesage/source/checkout
