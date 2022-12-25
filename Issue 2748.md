# Issue 2748: Permutation constructor does not accept lists of tuples

archive/issues_002748.json:
```json
{
    "body": "Assignee: @dandrake\n\nCC:  sage-combinat\n\nKeywords: combinat, permutations\n\nThe following works:\n\n```\nsage: p = ((1, 2, 4, 5, 3, 6))\nsage: q = Permutation(p)\nsage: q.to_cycles()\n[(1, 2, 4, 5, 3, 6)]\nsage: q.cycle_type()\n[6]\n```\n\n...but if `p` is a list of tuples, it doesn't, and Permutation doesn't tell you that it's not happy with the input:\n\n```\nsage: p = [(1, 2, 4, 5, 3, 6)]\nsage: q = Permutation(p)\nsage: q.to_cycles()\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/home/drake/code/sage/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/combinat/permutation.py in to_cycles(self, singletons)\n    415             else:\n    416                 cycle.append( next )    \n--> 417                 l.remove( next )\n    418                 toConsider = next\n    419 \n\n<type 'exceptions.ValueError'>: list.remove(x): x not in list\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2748\n\n",
    "created_at": "2008-04-01T01:42:23Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Permutation constructor does not accept lists of tuples",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2748",
    "user": "https://github.com/dandrake"
}
```
Assignee: @dandrake

CC:  sage-combinat

Keywords: combinat, permutations

The following works:

```
sage: p = ((1, 2, 4, 5, 3, 6))
sage: q = Permutation(p)
sage: q.to_cycles()
[(1, 2, 4, 5, 3, 6)]
sage: q.cycle_type()
[6]
```

...but if `p` is a list of tuples, it doesn't, and Permutation doesn't tell you that it's not happy with the input:

```
sage: p = [(1, 2, 4, 5, 3, 6)]
sage: q = Permutation(p)
sage: q.to_cycles()
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/drake/code/sage/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/combinat/permutation.py in to_cycles(self, singletons)
    415             else:
    416                 cycle.append( next )    
--> 417                 l.remove( next )
    418                 toConsider = next
    419 

<type 'exceptions.ValueError'>: list.remove(x): x not in list
```

Issue created by migration from https://trac.sagemath.org/ticket/2748





---

archive/issue_comments_018841.json:
```json
{
    "body": "Attachment [permutation-list-of-tuples.patch](tarball://root/attachments/some-uuid/ticket2748/permutation-list-of-tuples.patch) by @dandrake created at 2008-04-07 07:39:35",
    "created_at": "2008-04-07T07:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2748#issuecomment-18841",
    "user": "https://github.com/dandrake"
}
```

Attachment [permutation-list-of-tuples.patch](tarball://root/attachments/some-uuid/ticket2748/permutation-list-of-tuples.patch) by @dandrake created at 2008-04-07 07:39:35



---

archive/issue_comments_018842.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-07T08:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2748#issuecomment-18842",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_018843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T14:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2748#issuecomment-18843",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006380.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-07T14:44:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2748",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2748#event-6380"
}
```



---

archive/issue_comments_018844.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-07T14:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2748#issuecomment-18844",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha3
