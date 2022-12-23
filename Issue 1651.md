# Issue 1651: bug in decode

archive/issues_001651.json:
```json
{
    "body": "Assignee: wdj\n\nReported by Harald Schilly:\n\nHere what I've tried (documentation does it a bit more \"difficult\",\nbut should be the same -- at least I hope so)\nhttp://www.sagemath.org/doc/html/const/node37.html\n\nC = HammingCode(2,GF(5))\nv = matrix(GF(5),[This is the Trac macro *1,0,0,2,1,0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,0,0,2,1,0-macro))\nC.decode(v)\n\nworks (at least no errors), but\n\nv = vector(GF(5),[1,0,0,2,1,0])\nC.decode(v)\n\nsays:\n\nTypeError: Gap produced error output\nPermutation: <expr> must be a positive integer (not a integer)\nexecuting $sage333:=(1, 0, 0, 2, 1, 0);;\n\nI can see the different braces in the output, but internally a 1xn/nx1\nmatrix should handled in some way the same as a vector.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1651\n\n",
    "created_at": "2008-01-01T14:46:56Z",
    "labels": [
        "coding theory",
        "minor",
        "bug"
    ],
    "title": "bug in decode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1651",
    "user": "wdj"
}
```
Assignee: wdj

Reported by Harald Schilly:

Here what I've tried (documentation does it a bit more "difficult",
but should be the same -- at least I hope so)
http://www.sagemath.org/doc/html/const/node37.html

C = HammingCode(2,GF(5))
v = matrix(GF(5),[This is the Trac macro *1,0,0,2,1,0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,0,0,2,1,0-macro))
C.decode(v)

works (at least no errors), but

v = vector(GF(5),[1,0,0,2,1,0])
C.decode(v)

says:

TypeError: Gap produced error output
Permutation: <expr> must be a positive integer (not a integer)
executing $sage333:=(1, 0, 0, 2, 1, 0);;

I can see the different braces in the output, but internally a 1xn/nx1
matrix should handled in some way the same as a vector.


Issue created by migration from https://trac.sagemath.org/ticket/1651





---

archive/issue_comments_010504.json:
```json
{
    "body": "I fixed this bug. The patch is at\nhttp://sage.math.washington.edu/home/wdj/patches/linear-codes20071210.hg\nIt passes sage -t.",
    "created_at": "2008-01-02T17:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10504",
    "user": "wdj"
}
```

I fixed this bug. The patch is at
http://sage.math.washington.edu/home/wdj/patches/linear-codes20071210.hg
It passes sage -t.



---

archive/issue_comments_010505.json:
```json
{
    "body": "patch for bug fix of decode in linear_code.py",
    "created_at": "2008-01-02T17:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10505",
    "user": "wdj"
}
```

patch for bug fix of decode in linear_code.py



---

archive/issue_comments_010506.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-13T13:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10506",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_010507.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-15T06:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10507",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_010508.json:
```json
{
    "body": "Seems reasonable, I say apply.  The formatting on the 1651-doctest patch is not the best, and I don't think the docstring to decode() is clear about what the acceptable inputs are.",
    "created_at": "2008-01-22T18:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10508",
    "user": "ncalexan"
}
```

Seems reasonable, I say apply.  The formatting on the 1651-doctest patch is not the best, and I don't think the docstring to decode() is clear about what the acceptable inputs are.



---

archive/issue_comments_010509.json:
```json
{
    "body": "Attachment\n\nI added an attachment which includes (1) my fix of the H Schilly bug, (2) M Hansen's docstring addition (reformatted, as the referee suggested), (3) an additional doctest (as suggested by the referee).",
    "created_at": "2008-01-27T17:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10509",
    "user": "wdj"
}
```

Attachment

I added an attachment which includes (1) my fix of the H Schilly bug, (2) M Hansen's docstring addition (reformatted, as the referee suggested), (3) an additional doctest (as suggested by the referee).



---

archive/issue_comments_010510.json:
```json
{
    "body": "Could we get somebody to review this updated patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-02T03:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10510",
    "user": "mabshoff"
}
```

Could we get somebody to review this updated patch?

Cheers,

Michael



---

archive/issue_comments_010511.json:
```json
{
    "body": "Thumbs up from me!",
    "created_at": "2008-02-16T17:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10511",
    "user": "ncalexan"
}
```

Thumbs up from me!



---

archive/issue_comments_010512.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-16T17:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10512",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010513.json:
```json
{
    "body": "Merged linear_code20080127.hg in Sage 2.10.2.alpha0",
    "created_at": "2008-02-16T17:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10513",
    "user": "mabshoff"
}
```

Merged linear_code20080127.hg in Sage 2.10.2.alpha0



---

archive/issue_comments_010514.json:
```json
{
    "body": "Arrg, it was actually merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-16T18:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1651#issuecomment-10514",
    "user": "mabshoff"
}
```

Arrg, it was actually merged in Sage 2.10.2.alpha1
