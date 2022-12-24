# Issue 2074: PermutationGroupElement constructor bug.

archive/issues_002074.json:
```json
{
    "body": "Assignee: boothby\n\nGetting a permutation with empty, or singleton tuples blows up.\n\n\n```\nsage: G = SymmetricGroup(10)\nsage: G(((1,2,3),(4,),(5,)))\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/boothby/.sage/sage_notebook/worksheets/admin/15/code/148.py\", line 5, in <module>\n    G(((Integer(1),Integer(2),Integer(3)),(Integer(4),),(Integer(4),)))\n  File \"/home/boothby/sage/local/lib/python2.5/site-packages/sympy/plotting/\", line 1, in <module>\n    \n  File \"/home/boothby/sagebuilds/sage-2.9.3/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\", line 298, in __call__\n    return PermutationGroupElement([x], self, check = check)\n  File \"permgroup_element.pyx\", line 239, in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__\n  File \"/home/boothby/sagebuilds/sage-2.9.3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 738, in __call__\n    return cls(self, x)\n  File \"/home/boothby/sagebuilds/sage-2.9.3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 989, in __init__\n    raise TypeError, x\nTypeError: Gap produced error output\nSyntax error: expression expected\n$sage156:=((1,2,3)(4,)(4,));;\n                     ^\n\n   executing $sage156:=((1,2,3)(4,)(4,));;\n```\n\n\nSimilarly, a tuple consisting of a single cycle blows up:\n\n\n```\nsage: G(((1,2,3),))\nException (click to the left for traceback):\n...\n   executing $sage163:=((1,2,3),);;\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2074\n\n",
    "created_at": "2008-02-06T09:41:23Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "PermutationGroupElement constructor bug.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2074",
    "user": "boothby"
}
```
Assignee: boothby

Getting a permutation with empty, or singleton tuples blows up.


```
sage: G = SymmetricGroup(10)
sage: G(((1,2,3),(4,),(5,)))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/boothby/.sage/sage_notebook/worksheets/admin/15/code/148.py", line 5, in <module>
    G(((Integer(1),Integer(2),Integer(3)),(Integer(4),),(Integer(4),)))
  File "/home/boothby/sage/local/lib/python2.5/site-packages/sympy/plotting/", line 1, in <module>
    
  File "/home/boothby/sagebuilds/sage-2.9.3/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py", line 298, in __call__
    return PermutationGroupElement([x], self, check = check)
  File "permgroup_element.pyx", line 239, in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__
  File "/home/boothby/sagebuilds/sage-2.9.3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 738, in __call__
    return cls(self, x)
  File "/home/boothby/sagebuilds/sage-2.9.3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 989, in __init__
    raise TypeError, x
TypeError: Gap produced error output
Syntax error: expression expected
$sage156:=((1,2,3)(4,)(4,));;
                     ^

   executing $sage156:=((1,2,3)(4,)(4,));;
```


Similarly, a tuple consisting of a single cycle blows up:


```
sage: G(((1,2,3),))
Exception (click to the left for traceback):
...
   executing $sage163:=((1,2,3),);;
```


Issue created by migration from https://trac.sagemath.org/ticket/2074





---

archive/issue_comments_013416.json:
```json
{
    "body": "Attachment [2074-permgroup_element_fix.patch](tarball://root/attachments/some-uuid/ticket2074/2074-permgroup_element_fix.patch) by boothby created at 2008-02-06 10:31:26",
    "created_at": "2008-02-06T10:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2074#issuecomment-13416",
    "user": "boothby"
}
```

Attachment [2074-permgroup_element_fix.patch](tarball://root/attachments/some-uuid/ticket2074/2074-permgroup_element_fix.patch) by boothby created at 2008-02-06 10:31:26



---

archive/issue_comments_013417.json:
```json
{
    "body": "Attachment [2074.patch](tarball://root/attachments/some-uuid/ticket2074/2074.patch) by mhansen created at 2008-02-07 08:26:01\n\nApply the second patch -- positive review.",
    "created_at": "2008-02-07T08:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2074#issuecomment-13417",
    "user": "mhansen"
}
```

Attachment [2074.patch](tarball://root/attachments/some-uuid/ticket2074/2074.patch) by mhansen created at 2008-02-07 08:26:01

Apply the second patch -- positive review.



---

archive/issue_comments_013418.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-07T09:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2074#issuecomment-13418",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013419.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-07T09:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2074#issuecomment-13419",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
