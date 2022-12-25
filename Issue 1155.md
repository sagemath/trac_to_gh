# Issue 1155: PermutationGroup coercion bug

archive/issues_001155.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nCC:  sage-combinat\n\nKeywords: GAP, permutation group\n\nThe patch \nhttp://sage.math.washington.edu/home/wdj/patches/permgp-2007-11-12.hg\nfixes a bug reported by Carlo H. Part of his email is pasted below:\n\n+++++++++++++++++++++++++++++++++++++++++++++++\n\nHi,\n\nI'm doing some work with groups. Using gap.Image() I can get a\npermutation like this:\n\n```\nsage: x\n(1,2)(3,7)(4,6)(5,8)\n```\n\nBut to make a permutation group out of this element I have to enclose\nthe x in two sets of brackets:\n\n```\nsage: PermutationGroup([[x]])\nPermutation Group with generators [(1,2)(3,7)(4,6)(5,8)]\n```\n\nOn the other hand, the following command fails (see below for code and output):\n\n```\nsage: PermutationGroup([x])\n```\n\nIn my mind the second version is clearer - x is a permutation so [x]\nis a list of permutations and I should be able to use that to get a\ngroup.\n\nShould SAGE do a coercion here, or am I doing something in a strange way?\n\nCode and output:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.11, Release Date: 2007-11-02                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: p = 2\nsage: assert is_prime(p)\nsage:\nsage: F = gap.new(\"FreeGroup(3)\")\nsage:\nsage: a = F.gen(1)\nsage: b = F.gen(2)\nsage: c = F.gen(3)\nsage:\nsage: rels = []\nsage: rels.append( a**Integer(p) )\nsage: rels.append( b**Integer(p) )\nsage: rels.append( c**Integer(p) )\nsage: rels.append( a*b*((b*a*c)**Integer(-1)) )\nsage: rels.append( c*a*((a*c)**Integer(-1)) )\nsage: rels.append( c*b*((b*c)**Integer(-1)) )\nsage:\nsage: N = gap.NormalClosure(F, gap.Subgroup(F, rels))\nsage: niso = gap.NaturalHomomorphismByNormalSubgroupNC(F, N)\nsage:\nsage: x = gap.Image(niso, a)\nsage: x\n(1,2)(3,7)(4,6)(5,8)\nsage: PermutationGroup([[x]])\nPermutation Group with generators [(1,2)(3,7)(4,6)(5,8)]\nsage:\nsage: PermutationGroup([x])\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n```\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1155\n\n",
    "created_at": "2007-11-12T15:24:03Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "PermutationGroup coercion bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1155",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @wdjoyner

CC:  sage-combinat

Keywords: GAP, permutation group

The patch 
http://sage.math.washington.edu/home/wdj/patches/permgp-2007-11-12.hg
fixes a bug reported by Carlo H. Part of his email is pasted below:

+++++++++++++++++++++++++++++++++++++++++++++++

Hi,

I'm doing some work with groups. Using gap.Image() I can get a
permutation like this:

```
sage: x
(1,2)(3,7)(4,6)(5,8)
```

But to make a permutation group out of this element I have to enclose
the x in two sets of brackets:

```
sage: PermutationGroup([[x]])
Permutation Group with generators [(1,2)(3,7)(4,6)(5,8)]
```

On the other hand, the following command fails (see below for code and output):

```
sage: PermutationGroup([x])
```

In my mind the second version is clearer - x is a permutation so [x]
is a list of permutations and I should be able to use that to get a
group.

Should SAGE do a coercion here, or am I doing something in a strange way?

Code and output:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.11, Release Date: 2007-11-02                      |
| Type notebook() for the GUI, and license() for information.        |
sage: p = 2
sage: assert is_prime(p)
sage:
sage: F = gap.new("FreeGroup(3)")
sage:
sage: a = F.gen(1)
sage: b = F.gen(2)
sage: c = F.gen(3)
sage:
sage: rels = []
sage: rels.append( a**Integer(p) )
sage: rels.append( b**Integer(p) )
sage: rels.append( c**Integer(p) )
sage: rels.append( a*b*((b*a*c)**Integer(-1)) )
sage: rels.append( c*a*((a*c)**Integer(-1)) )
sage: rels.append( c*b*((b*c)**Integer(-1)) )
sage:
sage: N = gap.NormalClosure(F, gap.Subgroup(F, rels))
sage: niso = gap.NaturalHomomorphismByNormalSubgroupNC(F, N)
sage:
sage: x = gap.Image(niso, a)
sage: x
(1,2)(3,7)(4,6)(5,8)
sage: PermutationGroup([[x]])
Permutation Group with generators [(1,2)(3,7)(4,6)(5,8)]
sage:
sage: PermutationGroup([x])
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

```





Issue created by migration from https://trac.sagemath.org/ticket/1155





---

archive/issue_comments_007026.json:
```json
{
    "body": "This patch doesn't feel right to me; it seems like it's fixing the problem at the wrong level.  (For instance, it sometimes breaks if you try to create a permutation group from a list of generators where some of the generators are Python lists and some are Gap permutation group elements.  Maybe that's too strange a case to worry about?)\n\nI haven't tried it, but it looks like adding a special case to gap_format() for Gap permutation group elements would also fix the problem, perhaps in a better way?",
    "created_at": "2007-11-27T05:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1155#issuecomment-7026",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

This patch doesn't feel right to me; it seems like it's fixing the problem at the wrong level.  (For instance, it sometimes breaks if you try to create a permutation group from a list of generators where some of the generators are Python lists and some are Gap permutation group elements.  Maybe that's too strange a case to worry about?)

I haven't tried it, but it looks like adding a special case to gap_format() for Gap permutation group elements would also fix the problem, perhaps in a better way?



---

archive/issue_comments_007027.json:
```json
{
    "body": "Also, there are no doctests in the patch.",
    "created_at": "2007-11-27T05:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1155#issuecomment-7027",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Also, there are no doctests in the patch.



---

archive/issue_comments_007028.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T03:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1155#issuecomment-7028",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007029.json:
```json
{
    "body": "Changing assignee from @wdjoyner to @mwhansen.",
    "created_at": "2007-12-06T03:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1155#issuecomment-7029",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @wdjoyner to @mwhansen.



---

archive/issue_comments_007030.json:
```json
{
    "body": "I've put a new patch up.",
    "created_at": "2007-12-06T03:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1155#issuecomment-7030",
    "user": "https://github.com/mwhansen"
}
```

I've put a new patch up.



---

archive/issue_comments_007031.json:
```json
{
    "body": "Attachment [1155.patch](tarball://root/attachments/some-uuid/ticket1155/1155.patch) by @mwhansen created at 2007-12-06 03:47:11",
    "created_at": "2007-12-06T03:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1155#issuecomment-7031",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1155.patch](tarball://root/attachments/some-uuid/ticket1155/1155.patch) by @mwhansen created at 2007-12-06 03:47:11



---

archive/issue_comments_007032.json:
```json
{
    "body": "Code looks good; doctest passes.",
    "created_at": "2008-01-27T02:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1155#issuecomment-7032",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Code looks good; doctest passes.



---

archive/issue_events_001285.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-27T02:34:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1155",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1155#event-1285"
}
```



---

archive/issue_comments_007033.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T02:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1155#issuecomment-7033",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007034.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc1",
    "created_at": "2008-01-27T02:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1155#issuecomment-7034",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc1
