# Issue 1400: QuadraticFields and ClassGroups

archive/issues_001400.json:
```json
{
    "body": "Assignee: was\n\nSAGE can compute the class group of a quadratic field, but it has issues with computing the order of elements within that class group:\n\nQF.<x>=QuadraticField(-39)\nCF=QF.class_group()\nCF(QF.ideal(1+x)).order()\n\ngives\n\nNotImplementedErrorTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/server2/sage_notebook/worksheets/ljpk/0/code/6.py\", line 6, in <module>\n    CF(QF.ideal(Integer(1)+x)).order()\n  File \"/home/sage10/\", line 1, in <module>\n    \n  File \"element.pyx\", line 1190, in sage.structure.element.MultiplicativeGroupElement.order\n  File \"element.pyx\", line 1130, in sage.structure.element.MonoidElement.multiplicative_order\nNotImplementedError\n\nIssue created by migration from https://trac.sagemath.org/ticket/1400\n\n",
    "created_at": "2007-12-04T23:10:59Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "QuadraticFields and ClassGroups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1400",
    "user": "ljpk"
}
```
Assignee: was

SAGE can compute the class group of a quadratic field, but it has issues with computing the order of elements within that class group:

QF.<x>=QuadraticField(-39)
CF=QF.class_group()
CF(QF.ideal(1+x)).order()

gives

NotImplementedErrorTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/server2/sage_notebook/worksheets/ljpk/0/code/6.py", line 6, in <module>
    CF(QF.ideal(Integer(1)+x)).order()
  File "/home/sage10/", line 1, in <module>
    
  File "element.pyx", line 1190, in sage.structure.element.MultiplicativeGroupElement.order
  File "element.pyx", line 1130, in sage.structure.element.MonoidElement.multiplicative_order
NotImplementedError

Issue created by migration from https://trac.sagemath.org/ticket/1400





---

archive/issue_comments_009028.json:
```json
{
    "body": "Attachment [1400-quadratic_field_order.patch](tarball://root/attachments/some-uuid/ticket1400/1400-quadratic_field_order.patch) by AlexGhitza created at 2008-04-25 02:47:55",
    "created_at": "2008-04-25T02:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9028",
    "user": "AlexGhitza"
}
```

Attachment [1400-quadratic_field_order.patch](tarball://root/attachments/some-uuid/ticket1400/1400-quadratic_field_order.patch) by AlexGhitza created at 2008-04-25 02:47:55



---

archive/issue_comments_009029.json:
```json
{
    "body": "The attached patch adds this functionality for fractional ideals and for their representatives in class groups.",
    "created_at": "2008-04-25T02:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9029",
    "user": "AlexGhitza"
}
```

The attached patch adds this functionality for fractional ideals and for their representatives in class groups.



---

archive/issue_comments_009030.json:
```json
{
    "body": "This uses an O(n) algorithm to compute orders.  Don't we have generic BSGS O(sqrt(n)) that would be better here?",
    "created_at": "2008-04-28T02:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9030",
    "user": "ncalexan"
}
```

This uses an O(n) algorithm to compute orders.  Don't we have generic BSGS O(sqrt(n)) that would be better here?



---

archive/issue_comments_009031.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-20T04:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9031",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_009032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T07:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9032",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009033.json:
```json
{
    "body": "Fixed via #3913.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T07:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9033",
    "user": "mabshoff"
}
```

Fixed via #3913.

Cheers,

Michael
