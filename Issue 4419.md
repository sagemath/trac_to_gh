# Issue 4419: [with patch, needs review] conversion of Permutations to GAP not implemented

archive/issues_004419.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nThe following fails \n\n```\nsage: p = gap(Permutation('(1,2,3)'))\nsage: q = gap(Permutation([()]))\nsage: gap.Group([p, q])\n```\n\nbecause \n\n```\nsage: gap(Permutation((1,2,3)))\n[ 2 3 1 ]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4419\n\n",
    "created_at": "2008-11-02T00:17:11Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] conversion of Permutations to GAP not implemented",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4419",
    "user": "mhansen"
}
```
Assignee: mhansen

CC:  sage-combinat

The following fails 

```
sage: p = gap(Permutation('(1,2,3)'))
sage: q = gap(Permutation([()]))
sage: gap.Group([p, q])
```

because 

```
sage: gap(Permutation((1,2,3)))
[ 2 3 1 ]
```


Issue created by migration from https://trac.sagemath.org/ticket/4419





---

archive/issue_comments_032496.json:
```json
{
    "body": "Attachment\n\nI don't see how this fixes the original problem. I get this:\n\n\n```\nsage: p = gap(Permutation('(1,2,3)'))                                                                                              \nsage: q = gap(Permutation('()'))                                                                                       \n---------------------------------------------------------------------------                                            \nValueError                                Traceback (most recent call last)\n<snip>\n\n\nValueError: invalid literal for int() with base 10: ''\n```\n\n\nand this:\n\n\n```\nsage: q = gap(Permutation(()))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n<snip>\n\nTypeError: not enough arguments for format string\n```\n\n\nIt seems to me you want Permutation to work like\nPermutationGroupElement does here:\n\n```\nsage: p = gap(PermutationGroupElement('(1,2,3)'))\nsage: q = gap(PermutationGroupElement('()'))\nsage: gap.Group([p, q])\nGroup( [ (1,2,3), () ] )\nsage: gap.Group([p]) == gap.Group([p, q])\nTrue\n```\n\nIs that correct?",
    "created_at": "2008-11-02T01:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4419#issuecomment-32496",
    "user": "wdj"
}
```

Attachment

I don't see how this fixes the original problem. I get this:


```
sage: p = gap(Permutation('(1,2,3)'))                                                                                              
sage: q = gap(Permutation('()'))                                                                                       
---------------------------------------------------------------------------                                            
ValueError                                Traceback (most recent call last)
<snip>


ValueError: invalid literal for int() with base 10: ''
```


and this:


```
sage: q = gap(Permutation(()))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<snip>

TypeError: not enough arguments for format string
```


It seems to me you want Permutation to work like
PermutationGroupElement does here:

```
sage: p = gap(PermutationGroupElement('(1,2,3)'))
sage: q = gap(PermutationGroupElement('()'))
sage: gap.Group([p, q])
Group( [ (1,2,3), () ] )
sage: gap.Group([p]) == gap.Group([p, q])
True
```

Is that correct?



---

archive/issue_comments_032497.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-02T03:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4419#issuecomment-32497",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032498.json:
```json
{
    "body": "Actually, the original issue was this:\n\n\n```\nsage: p = gap(Permutation('(1,2,3)'))\nsage: q = gap(Permutation([()]))\nsage: gap.Group([p, q])\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n```\n\n\nThose things that you encountered are \"bugs\" in the constructor of Permutation.  I always construct Permutations from their list notation.",
    "created_at": "2008-11-02T03:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4419#issuecomment-32498",
    "user": "mhansen"
}
```

Actually, the original issue was this:


```
sage: p = gap(Permutation('(1,2,3)'))
sage: q = gap(Permutation([()]))
sage: gap.Group([p, q])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
```


Those things that you encountered are "bugs" in the constructor of Permutation.  I always construct Permutations from their list notation.



---

archive/issue_comments_032499.json:
```json
{
    "body": "This patch should get a positive review because it fixes the conversion to gap problem:\n\n\n```\nsage: p = Permutation('(1,2,3)')\nsage: q = Permutation([()])\nsage: gap.Group([p,q])\nGroup( [ (1,2,3), () ] )\n```\n\n\nThe other issues noticed by wdj are problems with the Permutations constructor function, and I will open a new ticket for them.",
    "created_at": "2008-11-20T20:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4419#issuecomment-32499",
    "user": "saliola"
}
```

This patch should get a positive review because it fixes the conversion to gap problem:


```
sage: p = Permutation('(1,2,3)')
sage: q = Permutation([()])
sage: gap.Group([p,q])
Group( [ (1,2,3), () ] )
```


The other issues noticed by wdj are problems with the Permutations constructor function, and I will open a new ticket for them.



---

archive/issue_comments_032500.json:
```json
{
    "body": "The new ticket is here: #4569",
    "created_at": "2008-11-20T20:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4419#issuecomment-32500",
    "user": "saliola"
}
```

The new ticket is here: #4569



---

archive/issue_comments_032501.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T10:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4419#issuecomment-32501",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032502.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T10:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4419#issuecomment-32502",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha0
