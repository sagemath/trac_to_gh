# Issue 1400: [with patch, with negative review] QuadraticFields and ClassGroups

archive/issues_001400.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: editor_craigcitro\n\nSAGE can compute the class group of a quadratic field, but it has issues with computing the order of elements within that class group:\n\n```\nQF.<x>=QuadraticField(-39)\nCF=QF.class_group()\nCF(QF.ideal(1+x)).order()\n```\ngives\n\n```\nNotImplementedErrorTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/server2/sage_notebook/worksheets/ljpk/0/code/6.py\", line 6, in <module>\n    CF(QF.ideal(Integer(1)+x)).order()\n  File \"/home/sage10/\", line 1, in <module>\n    \n  File \"element.pyx\", line 1190, in sage.structure.element.MultiplicativeGroupElement.order\n  File \"element.pyx\", line 1130, in sage.structure.element.MonoidElement.multiplicative_order\nNotImplementedError\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1400\n\n",
    "closed_at": "2008-08-27T07:37:49Z",
    "created_at": "2007-12-04T23:10:59Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, with negative review] QuadraticFields and ClassGroups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1400",
    "user": "https://trac.sagemath.org/admin/accounts/users/ljpk"
}
```
Assignee: @williamstein

Keywords: editor_craigcitro

SAGE can compute the class group of a quadratic field, but it has issues with computing the order of elements within that class group:

```
QF.<x>=QuadraticField(-39)
CF=QF.class_group()
CF(QF.ideal(1+x)).order()
```
gives

```
NotImplementedErrorTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/server2/sage_notebook/worksheets/ljpk/0/code/6.py", line 6, in <module>
    CF(QF.ideal(Integer(1)+x)).order()
  File "/home/sage10/", line 1, in <module>
    
  File "element.pyx", line 1190, in sage.structure.element.MultiplicativeGroupElement.order
  File "element.pyx", line 1130, in sage.structure.element.MonoidElement.multiplicative_order
NotImplementedError
```

Issue created by migration from https://trac.sagemath.org/ticket/1400





---

archive/issue_events_003615.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-04T23:23:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1400#event-3615"
}
```



---

archive/issue_comments_009004.json:
```json
{
    "body": "Attachment [1400-quadratic_field_order.patch](tarball://root/attachments/some-uuid/ticket1400/1400-quadratic_field_order.patch) by @aghitza created at 2008-04-25 02:47:55",
    "created_at": "2008-04-25T02:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9004",
    "user": "https://github.com/aghitza"
}
```

Attachment [1400-quadratic_field_order.patch](tarball://root/attachments/some-uuid/ticket1400/1400-quadratic_field_order.patch) by @aghitza created at 2008-04-25 02:47:55



---

archive/issue_comments_009005.json:
```json
{
    "body": "The attached patch adds this functionality for fractional ideals and for their representatives in class groups.",
    "created_at": "2008-04-25T02:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9005",
    "user": "https://github.com/aghitza"
}
```

The attached patch adds this functionality for fractional ideals and for their representatives in class groups.



---

archive/issue_comments_009006.json:
```json
{
    "body": "This uses an O(n) algorithm to compute orders.  Don't we have generic BSGS O(sqrt(n)) that would be better here?",
    "created_at": "2008-04-28T02:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9006",
    "user": "https://github.com/ncalexan"
}
```

This uses an O(n) algorithm to compute orders.  Don't we have generic BSGS O(sqrt(n)) that would be better here?



---

archive/issue_comments_009007.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-20T04:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9007",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_009008.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T07:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9008",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009009.json:
```json
{
    "body": "Fixed via #3913.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T07:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1400#issuecomment-9009",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed via #3913.

Cheers,

Michael



---

archive/issue_events_003616.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-27T07:37:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1400",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1400#event-3616"
}
```
