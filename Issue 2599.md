# Issue 2599: Permutation -> PermutationGroupElement fails for the identity

archive/issues_002599.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\n\n```\nsage: Permutation([1,2,3]).to_permutation_group_element()\n---------------------------------------------------------------------------\n<type 'exceptions.IndexError'>            Traceback (most recent call last)\n\n/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/devel/sage-review/<ipython console> in <module>()\n\n/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/combinat/permutation.py in to_permutation_group_element(self)\n    438         \"\"\"\n    439 \n--> 440         return PermutationGroupElement(self.to_cycles(singletons=False))\n    441 \n    442     def signature(p):\n\n/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/devel/sage-review/permgroup_element.pyx in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__()\n\n/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/devel/sage-review/permgroup_element.pyx in sage.groups.perm_gps.permgroup_element.gap_format()\n\n<type 'exceptions.IndexError'>: list index out of range\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2599\n\n",
    "created_at": "2008-03-19T18:46:00Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "title": "Permutation -> PermutationGroupElement fails for the identity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2599",
    "user": "mhansen"
}
```
Assignee: mhansen

CC:  sage-combinat


```
sage: Permutation([1,2,3]).to_permutation_group_element()
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/devel/sage-review/<ipython console> in <module>()

/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/combinat/permutation.py in to_permutation_group_element(self)
    438         """
    439 
--> 440         return PermutationGroupElement(self.to_cycles(singletons=False))
    441 
    442     def signature(p):

/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/devel/sage-review/permgroup_element.pyx in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__()

/home/mhansen/sage-2.10.4.alpha0-sage.math-only-x86_64-Linux/devel/sage-review/permgroup_element.pyx in sage.groups.perm_gps.permgroup_element.gap_format()

<type 'exceptions.IndexError'>: list index out of range
```


Issue created by migration from https://trac.sagemath.org/ticket/2599





---

archive/issue_comments_017789.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-19T19:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2599#issuecomment-17789",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_017790.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-19T19:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2599#issuecomment-17790",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017791.json:
```json
{
    "body": "The patch does what it advertises and doctests that behavior. All good, I say apply. One could replace the '()' by () though to gain a little speed.",
    "created_at": "2008-03-21T02:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2599#issuecomment-17791",
    "user": "malb"
}
```

The patch does what it advertises and doctests that behavior. All good, I say apply. One could replace the '()' by () though to gain a little speed.



---

archive/issue_comments_017792.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-21T02:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2599#issuecomment-17792",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_comments_017793.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T02:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2599#issuecomment-17793",
    "user": "mabshoff"
}
```

Resolution: fixed
