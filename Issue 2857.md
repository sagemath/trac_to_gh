# Issue 2857: numerical_approx for matrices

archive/issues_002857.json:
```json
{
    "body": "Assignee: was\n\nI'm running into problems with coercing to complexes or reals in\nmatrices:\n\n sage: d = matrix([[3, 0],[0,sqrt(2)]])\n sage: b = matrix([[1, -1], [2, 2]])\n sage: e = b * d * b.inverse(); e\n\n [    1/sqrt(2) + 3/2 3/4 - 1/(2*sqrt(2))]\n [        3 - sqrt(2)     1/sqrt(2) + 3/2]\n\nand when I try to run n() on the matrix e, I get:\n\n sage: e.n()  # or n(e)\n [snip]\n <type 'exceptions.TypeError'>: unable to coerce to a [ComplexNumber](ComplexNumber)\n\n\n\nIf you take a look at the source code for n(), you'll see that the first thing that it does is to try calling numerical_approx(prec) on the object, and then tries coercing to real or complex fields.  So the solution is to write a method numerical_approx(prec) in the matrix base class that tries to numerically approximate the entries and make a new matrix out of them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2857\n\n",
    "created_at": "2008-04-08T17:54:48Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "numerical_approx for matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2857",
    "user": "roed"
}
```
Assignee: was

I'm running into problems with coercing to complexes or reals in
matrices:

 sage: d = matrix([[3, 0],[0,sqrt(2)]])
 sage: b = matrix([[1, -1], [2, 2]])
 sage: e = b * d * b.inverse(); e

 [    1/sqrt(2) + 3/2 3/4 - 1/(2*sqrt(2))]
 [        3 - sqrt(2)     1/sqrt(2) + 3/2]

and when I try to run n() on the matrix e, I get:

 sage: e.n()  # or n(e)
 [snip]
 <type 'exceptions.TypeError'>: unable to coerce to a [ComplexNumber](ComplexNumber)



If you take a look at the source code for n(), you'll see that the first thing that it does is to try calling numerical_approx(prec) on the object, and then tries coercing to real or complex fields.  So the solution is to write a method numerical_approx(prec) in the matrix base class that tries to numerically approximate the entries and make a new matrix out of them.

Issue created by migration from https://trac.sagemath.org/ticket/2857





---

archive/issue_comments_019597.json:
```json
{
    "body": "Attachment [2857.patch](tarball://root/attachments/some-uuid/ticket2857/2857.patch) by dfdeshom created at 2008-04-13 19:11:48",
    "created_at": "2008-04-13T19:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2857#issuecomment-19597",
    "user": "dfdeshom"
}
```

Attachment [2857.patch](tarball://root/attachments/some-uuid/ticket2857/2857.patch) by dfdeshom created at 2008-04-13 19:11:48



---

archive/issue_comments_019598.json:
```json
{
    "body": "Patch attached. The functionality was already there (in `change_ring()` and this wrapper around it works fairly well.",
    "created_at": "2008-04-13T19:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2857#issuecomment-19598",
    "user": "dfdeshom"
}
```

Patch attached. The functionality was already there (in `change_ring()` and this wrapper around it works fairly well.



---

archive/issue_comments_019599.json:
```json
{
    "body": "Attachment [2857.2.patch](tarball://root/attachments/some-uuid/ticket2857/2857.2.patch) by mhansen created at 2008-04-14 23:01:35\n\nLooks good to me.\n\nApply 2857.2.patch after #1763",
    "created_at": "2008-04-14T23:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2857#issuecomment-19599",
    "user": "mhansen"
}
```

Attachment [2857.2.patch](tarball://root/attachments/some-uuid/ticket2857/2857.2.patch) by mhansen created at 2008-04-14 23:01:35

Looks good to me.

Apply 2857.2.patch after #1763



---

archive/issue_comments_019600.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T00:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2857#issuecomment-19600",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019601.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-15T00:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2857#issuecomment-19601",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha5
