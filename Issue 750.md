# Issue 750: permutation group element (dict method, acting on lists)

archive/issues_000750.json:
```json
{
    "body": "Assignee: was\n\nCC:  sage-combinat\n\nIt would be nice to get permutation elements as dictionaries as well as lists.  If g is a permutation group element, then something like\n\n\n```\n  sage: g.dict()\n{1:2, 2:1}\n```\n\n\nIt would also be nice if we could have permutation elements act on lists to switch the order according to the permutation.\n\n\n```\n  sage: g.action(range(3))\n[0,2,1]\n```\n\n\nAre these things possible already?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/750\n\n",
    "created_at": "2007-09-24T23:13:58Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "title": "permutation group element (dict method, acting on lists)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/750",
    "user": "jason"
}
```
Assignee: was

CC:  sage-combinat

It would be nice to get permutation elements as dictionaries as well as lists.  If g is a permutation group element, then something like


```
  sage: g.dict()
{1:2, 2:1}
```


It would also be nice if we could have permutation elements act on lists to switch the order according to the permutation.


```
  sage: g.action(range(3))
[0,2,1]
```


Are these things possible already?


Issue created by migration from https://trac.sagemath.org/ticket/750





---

archive/issue_comments_004435.json:
```json
{
    "body": "Attachment [750.hg](tarball://root/attachments/some-uuid/ticket750/750.hg) by boothby created at 2007-10-27 22:01:10\n\nAdded a patch to implement something similar to the second.  With this patch, one may do the following:\n\n\n```\nsage: G = SymmetricGroup(4)\nsage: g = G((1,2,3,4))\nsage: sage: g('abcd')\n'bcda'\nsage: sage: g([0,1,2,3])\n[1, 2, 3, 0]\nsage: sage: g(('foo','bar','baz','what'))\n('bar', 'baz', 'what', 'foo')\n```\n\n\nHowever, I can see absolutely no reason for one to want a dict rather than a list.  Do you have an example of where this might be useful?",
    "created_at": "2007-10-27T22:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/750#issuecomment-4435",
    "user": "boothby"
}
```

Attachment [750.hg](tarball://root/attachments/some-uuid/ticket750/750.hg) by boothby created at 2007-10-27 22:01:10

Added a patch to implement something similar to the second.  With this patch, one may do the following:


```
sage: G = SymmetricGroup(4)
sage: g = G((1,2,3,4))
sage: sage: g('abcd')
'bcda'
sage: sage: g([0,1,2,3])
[1, 2, 3, 0]
sage: sage: g(('foo','bar','baz','what'))
('bar', 'baz', 'what', 'foo')
```


However, I can see absolutely no reason for one to want a dict rather than a list.  Do you have an example of where this might be useful?



---

archive/issue_comments_004436.json:
```json
{
    "body": "Robert Miller convinced me that there are good reasons to want a dict, so I implemented this, too.",
    "created_at": "2007-10-31T18:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/750#issuecomment-4436",
    "user": "boothby"
}
```

Robert Miller convinced me that there are good reasons to want a dict, so I implemented this, too.



---

archive/issue_comments_004437.json:
```json
{
    "body": "Changing assignee from was to boothby.",
    "created_at": "2007-10-31T18:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/750#issuecomment-4437",
    "user": "boothby"
}
```

Changing assignee from was to boothby.



---

archive/issue_comments_004438.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-31T18:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/750#issuecomment-4438",
    "user": "boothby"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004439.json:
```json
{
    "body": "Attachment [750.1.hg](tarball://root/attachments/some-uuid/ticket750/750.1.hg) by boothby created at 2007-10-31 18:03:05\n\nIncludes .dict() code.",
    "created_at": "2007-10-31T18:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/750#issuecomment-4439",
    "user": "boothby"
}
```

Attachment [750.1.hg](tarball://root/attachments/some-uuid/ticket750/750.1.hg) by boothby created at 2007-10-31 18:03:05

Includes .dict() code.



---

archive/issue_comments_004440.json:
```json
{
    "body": "fixes bugs from previous edition / ready for 2.8.11",
    "created_at": "2007-11-01T18:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/750#issuecomment-4440",
    "user": "boothby"
}
```

fixes bugs from previous edition / ready for 2.8.11



---

archive/issue_comments_004441.json:
```json
{
    "body": "Attachment [750.1.2.hg](tarball://root/attachments/some-uuid/ticket750/750.1.2.hg) by mabshoff created at 2007-11-01 20:12:35",
    "created_at": "2007-11-01T20:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/750#issuecomment-4441",
    "user": "mabshoff"
}
```

Attachment [750.1.2.hg](tarball://root/attachments/some-uuid/ticket750/750.1.2.hg) by mabshoff created at 2007-11-01 20:12:35



---

archive/issue_comments_004442.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-02T03:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/750#issuecomment-4442",
    "user": "mabshoff"
}
```

Resolution: fixed
