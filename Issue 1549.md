# Issue 1549: Sage 2.9: fix optional doctests in tut.tex

archive/issues_001549.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nFile \"tut.py\", line 3390:\n    : G\nExpected:\n    Group([ (1,2,3)(4,5), (3,4) ])\nGot:\n    Group( [ (1,2,3)(4,5), (3,4) ] )\n**********************************************************************\nFile \"tut.py\", line 3392:\n    : G.Center()\nExpected:\n    Group(())\nGot:\n    Group( () ) \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1549\n\n",
    "created_at": "2007-12-17T13:37:02Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "Sage 2.9: fix optional doctests in tut.tex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1549",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
File "tut.py", line 3390:
    : G
Expected:
    Group([ (1,2,3)(4,5), (3,4) ])
Got:
    Group( [ (1,2,3)(4,5), (3,4) ] )
**********************************************************************
File "tut.py", line 3392:
    : G.Center()
Expected:
    Group(())
Got:
    Group( () ) 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1549





---

archive/issue_comments_009876.json:
```json
{
    "body": "doc patch, apply second",
    "created_at": "2008-04-25T00:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1549#issuecomment-9876",
    "user": "@aghitza"
}
```

doc patch, apply second



---

archive/issue_comments_009877.json:
```json
{
    "body": "Attachment [1549-tut_optional.patch](tarball://root/attachments/some-uuid/ticket1549/1549-tut_optional.patch) by @aghitza created at 2008-04-25 00:11:28\n\nI am attaching two patches.  The first changes the _repr_ of Galois groups from the current clunky\n\n\n```\nGalois group PARI group [8, 1, 3, \"E(8)=2[x]2[x]2\"] of degree 8 of the number field Number Field in a with defining polynomial x^2 + 1 over its base field\n```\n\n\nto\n\n\n```\nGalois group PARI group [8, 1, 3, \"E(8)=2[x]2[x]2\"] of degree 8 of the Number Field in a with defining polynomial x^2 + 1 over its base field\n```\n\n\nThe second patch is a documentation patch and fixes the optional doctest failures in tut.tex (and removes the #optional tag from one of them, since now by default GaloisGroup uses PARI instead of optional GAP packages).",
    "created_at": "2008-04-25T00:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1549#issuecomment-9877",
    "user": "@aghitza"
}
```

Attachment [1549-tut_optional.patch](tarball://root/attachments/some-uuid/ticket1549/1549-tut_optional.patch) by @aghitza created at 2008-04-25 00:11:28

I am attaching two patches.  The first changes the _repr_ of Galois groups from the current clunky


```
Galois group PARI group [8, 1, 3, "E(8)=2[x]2[x]2"] of degree 8 of the number field Number Field in a with defining polynomial x^2 + 1 over its base field
```


to


```
Galois group PARI group [8, 1, 3, "E(8)=2[x]2[x]2"] of degree 8 of the Number Field in a with defining polynomial x^2 + 1 over its base field
```


The second patch is a documentation patch and fixes the optional doctest failures in tut.tex (and removes the #optional tag from one of them, since now by default GaloisGroup uses PARI instead of optional GAP packages).



---

archive/issue_comments_009878.json:
```json
{
    "body": "Looks good to me.  There's a tiny typo in the first patch (\"isreducible\" needs a space), otherwise fine.",
    "created_at": "2008-04-27T17:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1549#issuecomment-9878",
    "user": "@JohnCremona"
}
```

Looks good to me.  There's a tiny typo in the first patch ("isreducible" needs a space), otherwise fine.



---

archive/issue_comments_009879.json:
```json
{
    "body": "Attachment [1549-galois_gp.patch](tarball://root/attachments/some-uuid/ticket1549/1549-galois_gp.patch) by @aghitza created at 2008-04-27 17:52:22",
    "created_at": "2008-04-27T17:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1549#issuecomment-9879",
    "user": "@aghitza"
}
```

Attachment [1549-galois_gp.patch](tarball://root/attachments/some-uuid/ticket1549/1549-galois_gp.patch) by @aghitza created at 2008-04-27 17:52:22



---

archive/issue_comments_009880.json:
```json
{
    "body": "I've replaced the first patch with one that fixes the typo pointed out by John.",
    "created_at": "2008-04-27T17:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1549#issuecomment-9880",
    "user": "@aghitza"
}
```

I've replaced the first patch with one that fixes the typo pointed out by John.



---

archive/issue_comments_009881.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-28T00:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1549#issuecomment-9881",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009882.json:
```json
{
    "body": "Merged both patches in Sage 3.0.1.alpha1",
    "created_at": "2008-04-28T00:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1549#issuecomment-9882",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.0.1.alpha1
