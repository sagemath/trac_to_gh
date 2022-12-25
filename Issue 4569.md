# Issue 4569: problems with the Permutation constructor function

archive/issues_004569.json:
```json
{
    "body": "Assignee: @saliola\n\nCC:  sage-combinat\n\nwdj pointed out in the comments to #4419:\n\n\n```\n{{{\nsage: p = gap(Permutation('(1,2,3)'))\nsage: q = gap(Permutation('()'))\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n<snip>\n\nValueError: invalid literal for int() with base 10: ''\n}}}\n\nand this:\n\n{{{\nsage: q = gap(Permutation(()))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n<snip>\n\nTypeError: not enough arguments for format string\n}}}\n\nIt seems to me you want Permutation to work like\nPermutationGroupElement does here:\n{{{\nsage: p = gap(PermutationGroupElement('(1,2,3)'))\nsage: q = gap(PermutationGroupElement('()'))\nsage: gap.Group([p, q])\nGroup( [ (1,2,3), () ] )\nsage: gap.Group([p]) == gap.Group([p, q])\nTrue\n}}}\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4569\n\n",
    "created_at": "2008-11-20T20:47:04Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "problems with the Permutation constructor function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4569",
    "user": "https://github.com/saliola"
}
```
Assignee: @saliola

CC:  sage-combinat

wdj pointed out in the comments to #4419:


```
{{{
sage: p = gap(Permutation('(1,2,3)'))
sage: q = gap(Permutation('()'))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<snip>

ValueError: invalid literal for int() with base 10: ''
}}}

and this:

{{{
sage: q = gap(Permutation(()))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<snip>

TypeError: not enough arguments for format string
}}}

It seems to me you want Permutation to work like
PermutationGroupElement does here:
{{{
sage: p = gap(PermutationGroupElement('(1,2,3)'))
sage: q = gap(PermutationGroupElement('()'))
sage: gap.Group([p, q])
Group( [ (1,2,3), () ] )
sage: gap.Group([p]) == gap.Group([p, q])
True
}}}
```



Issue created by migration from https://trac.sagemath.org/ticket/4569





---

archive/issue_comments_034162.json:
```json
{
    "body": "Attachment [trac_4569.patch](tarball://root/attachments/some-uuid/ticket4569/trac_4569.patch) by @saliola created at 2008-11-20 21:50:28\n\npatched against 3.2.rc2",
    "created_at": "2008-11-20T21:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4569#issuecomment-34162",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_4569.patch](tarball://root/attachments/some-uuid/ticket4569/trac_4569.patch) by @saliola created at 2008-11-20 21:50:28

patched against 3.2.rc2



---

archive/issue_comments_034163.json:
```json
{
    "body": "After this patch:\n\n```\nsage: Permutation([()])\n[1]\nsage: Permutation('()')\n[1]\n```\n\nwhich agree with PermutationGroupElement:\n\n```\nsage: PermutationGroupElement([()]).list()\n[1]\nsage: PermutationGroupElement('()').list()\n[1]\n```\n\nand:\n\n```\nsage: p = Permutation('(1,2,3)')\nsage: q = Permutation('()')\nsage: gap.Group([p,q])\nGroup( [ (1,2,3), () ] )\nsage: gap.Group([p]) == gap.Group([p, q])\nTrue\n```\n",
    "created_at": "2008-11-20T21:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4569#issuecomment-34163",
    "user": "https://github.com/saliola"
}
```

After this patch:

```
sage: Permutation([()])
[1]
sage: Permutation('()')
[1]
```

which agree with PermutationGroupElement:

```
sage: PermutationGroupElement([()]).list()
[1]
sage: PermutationGroupElement('()').list()
[1]
```

and:

```
sage: p = Permutation('(1,2,3)')
sage: q = Permutation('()')
sage: gap.Group([p,q])
Group( [ (1,2,3), () ] )
sage: gap.Group([p]) == gap.Group([p, q])
True
```




---

archive/issue_comments_034164.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-11-21T14:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4569#issuecomment-34164",
    "user": "https://github.com/mwhansen"
}
```

Looks good.



---

archive/issue_comments_034165.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-21T14:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4569#issuecomment-34165",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034166.json:
```json
{
    "body": "Changing assignee from @saliola to @mwhansen.",
    "created_at": "2008-11-21T14:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4569#issuecomment-34166",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @saliola to @mwhansen.



---

archive/issue_comments_034167.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T23:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4569#issuecomment-34167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004814.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-21T23:43:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4569",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4569#event-4814"
}
```



---

archive/issue_comments_034168.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T23:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4569#issuecomment-34168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0
