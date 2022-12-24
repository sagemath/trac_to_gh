# Issue 2748: Permutation constructor does not accept lists of tuples

archive/issues_002748.json:
```json
{
    "body": "Assignee: ddrake\n\nCC:  sage-combinat\n\nKeywords: combinat, permutations\n\nThe following works:\n\n\n```\nsage: p = ((1, 2, 4, 5, 3, 6))\nsage: q = Permutation(p)\nsage: q.to_cycles()\n[(1, 2, 4, 5, 3, 6)]\nsage: q.cycle_type()\n[6]\n```\n\n\n...but if `p` is a list of tuples, it doesn't, and Permutation doesn't tell you that it's not happy with the input:\n\n\n```\nsage: p = [(1, 2, 4, 5, 3, 6)]\nsage: q = Permutation(p)\nsage: q.to_cycles()\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/home/drake/code/sage/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/combinat/permutation.py in to_cycles(self, singletons)\n    415             else:\n    416                 cycle.append( next )    \n--> 417                 l.remove( next )\n    418                 toConsider = next\n    419 \n\n<type 'exceptions.ValueError'>: list.remove(x): x not in list\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2748\n\n",
    "created_at": "2008-04-01T01:42:23Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Permutation constructor does not accept lists of tuples",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2748",
    "user": "ddrake"
}
```
Assignee: ddrake

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

archive/issue_comments_018880.json:
```json
{
    "body": "Attachment [permutation-list-of-tuples.patch](tarball://root/attachments/some-uuid/ticket2748/permutation-list-of-tuples.patch) by ddrake created at 2008-04-07 07:39:35",
    "created_at": "2008-04-07T07:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2748#issuecomment-18880",
    "user": "ddrake"
}
```

Attachment [permutation-list-of-tuples.patch](tarball://root/attachments/some-uuid/ticket2748/permutation-list-of-tuples.patch) by ddrake created at 2008-04-07 07:39:35



---

archive/issue_comments_018881.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-07T08:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2748#issuecomment-18881",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_018882.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T14:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2748#issuecomment-18882",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018883.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-07T14:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2748#issuecomment-18883",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha3
