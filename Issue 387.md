# Issue 387: Inconsistencies with IntegerMod subtypes

archive/issues_000387.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  dmharvey@math.harvard.edu\n\nThe following bug was found by Thea Gegenberg. There seems to be in inconsistency in how elements in a ring Integers(D) for a bigger D are represented and there don't seem to be automatic coercions between the different representatives.\n\nThe culprits are IntegerMod_int, IntegerMod_int64 and IntegerMod_gmp (not illustrated here, but with bigger D similar errors arise wrt. gmp.)\n\nThis code illustrates the problem:\n\n\n```\nA=matrix([(70, 49, -20, -34, 57), (-49, -14, 95, 43, 85), (-95, -63, 68, 52, 12), (11,\n-16, -50, 43, 76), (-55, 83, 55, 40, -14)])\nD=A.determinant()\nR=Integers(D)\nMD=MatrixSpace(R,A.nrows(),A.ncols())\nAD=MD(A)\n# You would expect elements of R and entries of AD to be of exactly the same type.\n# this is not the case, however:\nprint parent(AD.row(1)[1])\nprint parent(R(3))\n# Indeed, the types of these are not the same:\nprint type(AD.row(1)[1])\nprint type(R(3))\n# and this has consequences: You'd expect the following to work, but it gives an error:\nR(3)*AD.row(1)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/387\n\n",
    "created_at": "2007-06-12T20:56:32Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "Inconsistencies with IntegerMod subtypes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/387",
    "user": "@nbruin"
}
```
Assignee: somebody

CC:  dmharvey@math.harvard.edu

The following bug was found by Thea Gegenberg. There seems to be in inconsistency in how elements in a ring Integers(D) for a bigger D are represented and there don't seem to be automatic coercions between the different representatives.

The culprits are IntegerMod_int, IntegerMod_int64 and IntegerMod_gmp (not illustrated here, but with bigger D similar errors arise wrt. gmp.)

This code illustrates the problem:


```
A=matrix([(70, 49, -20, -34, 57), (-49, -14, 95, 43, 85), (-95, -63, 68, 52, 12), (11,
-16, -50, 43, 76), (-55, 83, 55, 40, -14)])
D=A.determinant()
R=Integers(D)
MD=MatrixSpace(R,A.nrows(),A.ncols())
AD=MD(A)
# You would expect elements of R and entries of AD to be of exactly the same type.
# this is not the case, however:
print parent(AD.row(1)[1])
print parent(R(3))
# Indeed, the types of these are not the same:
print type(AD.row(1)[1])
print type(R(3))
# and this has consequences: You'd expect the following to work, but it gives an error:
R(3)*AD.row(1)
```


Issue created by migration from https://trac.sagemath.org/ticket/387





---

archive/issue_comments_001899.json:
```json
{
    "body": "Changing assignee from somebody to dmharvey.",
    "created_at": "2007-08-28T18:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/387#issuecomment-1899",
    "user": "dmharvey"
}
```

Changing assignee from somebody to dmharvey.



---

archive/issue_comments_001900.json:
```json
{
    "body": "I think this issue can be closed:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.3.alpha2, Release Date: 2007-08-29                |\n| Type notebook() for the GUI, and license() for information.        |\nsage: A=matrix([(70, 49, -20, -34, 57), (-49, -14, 95, 43, 85), (-95, -63, 68, 52, 12), (11,\n....: -16, -50, 43, 76), (-55, 83, 55, 40, -14)])\nsage: D=A.determinant()\nsage: R=Integers(D)\nsage: MD=MatrixSpace(R,A.nrows(),A.ncols())\nsage: AD=MD(A)\nsage: # You would expect elements of R and entries of AD to be of exactly the same type.\nsage: # this is not the case, however:\nsage: print parent(AD.row(1)[1])\nRing of integers modulo 1240031145\nsage: print parent(R(3))\nRing of integers modulo 1240031145\nsage: # Indeed, the types of these are not the same:\nsage: print type(AD.row(1)[1])\n<type 'sage.rings.integer_mod.IntegerMod_int64'>\nsage: print type(R(3))\n<type 'sage.rings.integer_mod.IntegerMod_int64'>\nsage: # and this has consequences: You'd expect the following to work, but it gives an error:\nsage: R(3)*AD.row(1)\n(1240030998, 1240031103, 285, 129, 255)\n```\n\nCheers,\n\nReassigned to 2.8.3.\n\nMichael",
    "created_at": "2007-08-30T12:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/387#issuecomment-1900",
    "user": "mabshoff"
}
```

I think this issue can be closed:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.3.alpha2, Release Date: 2007-08-29                |
| Type notebook() for the GUI, and license() for information.        |
sage: A=matrix([(70, 49, -20, -34, 57), (-49, -14, 95, 43, 85), (-95, -63, 68, 52, 12), (11,
....: -16, -50, 43, 76), (-55, 83, 55, 40, -14)])
sage: D=A.determinant()
sage: R=Integers(D)
sage: MD=MatrixSpace(R,A.nrows(),A.ncols())
sage: AD=MD(A)
sage: # You would expect elements of R and entries of AD to be of exactly the same type.
sage: # this is not the case, however:
sage: print parent(AD.row(1)[1])
Ring of integers modulo 1240031145
sage: print parent(R(3))
Ring of integers modulo 1240031145
sage: # Indeed, the types of these are not the same:
sage: print type(AD.row(1)[1])
<type 'sage.rings.integer_mod.IntegerMod_int64'>
sage: print type(R(3))
<type 'sage.rings.integer_mod.IntegerMod_int64'>
sage: # and this has consequences: You'd expect the following to work, but it gives an error:
sage: R(3)*AD.row(1)
(1240030998, 1240031103, 285, 129, 255)
```

Cheers,

Reassigned to 2.8.3.

Michael



---

archive/issue_comments_001901.json:
```json
{
    "body": "Is there a reason this is still open, looks good to me...",
    "created_at": "2007-09-06T23:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/387#issuecomment-1901",
    "user": "@robertwb"
}
```

Is there a reason this is still open, looks good to me...



---

archive/issue_comments_001902.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T04:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/387#issuecomment-1902",
    "user": "@williamstein"
}
```

Resolution: fixed
