# Issue 3544: PermutationGroup.is_transitive is broken

archive/issues_003544.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  alexghitza\n\n\n```\nsage: G = Graph({0:[1],1:[2]}); G.num_verts()\n3\nsage: A = G.automorphism_group(); A\nPermutation Group with generators [(2,3)]\nsage: A.is_transitive()\nTrue\nsage: A.gens()[0].list()\n[1,3,2]\n```\n\n\nHuh?  The cyclic group of order 2 acting on 3 letters is transitive?\n\nIssue created by migration from https://trac.sagemath.org/ticket/3544\n\n",
    "created_at": "2008-07-03T17:57:05Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "PermutationGroup.is_transitive is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3544",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: tbd

CC:  alexghitza


```
sage: G = Graph({0:[1],1:[2]}); G.num_verts()
3
sage: A = G.automorphism_group(); A
Permutation Group with generators [(2,3)]
sage: A.is_transitive()
True
sage: A.gens()[0].list()
[1,3,2]
```


Huh?  The cyclic group of order 2 acting on 3 letters is transitive?

Issue created by migration from https://trac.sagemath.org/ticket/3544





---

archive/issue_comments_025019.json:
```json
{
    "body": "This is closely related to #3404. See #3545.",
    "created_at": "2008-07-03T18:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3544#issuecomment-25019",
    "user": "https://github.com/rlmill"
}
```

This is closely related to #3404. See #3545.



---

archive/issue_comments_025020.json:
```json
{
    "body": "This wraps IsTransitive, which is assuming that the degree is 2:\n\n\n```\nsage: G = Graph({0:[1],1:[2]})\nsage: A = G.automorphism_group(); A\nAPermutation Group with generators [(2,3)]\nsage: GA = gap(A)\nsage: GA.Transitivity()\n2\nsage: GA.IsTransitive()\ntrue\n```\n\n\nHowever, the docstring for is_transitive is wrong. There is no method A.set() implemented.",
    "created_at": "2008-07-03T18:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3544#issuecomment-25020",
    "user": "https://github.com/wdjoyner"
}
```

This wraps IsTransitive, which is assuming that the degree is 2:


```
sage: G = Graph({0:[1],1:[2]})
sage: A = G.automorphism_group(); A
APermutation Group with generators [(2,3)]
sage: GA = gap(A)
sage: GA.Transitivity()
2
sage: GA.IsTransitive()
true
```


However, the docstring for is_transitive is wrong. There is no method A.set() implemented.



---

archive/issue_comments_025021.json:
```json
{
    "body": "Please always assign a milestone.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T17:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3544#issuecomment-25021",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Please always assign a milestone.

Cheers,

Michael



---

archive/issue_comments_025022.json:
```json
{
    "body": "I would suggest the following: \n\n(a) There is no bug in is_transitive but the docstring is wrong. \n\n(b) a \"set\" method should be implemented for the class PermutationGroup.\n\n(c) Possibly a verbose option could be added which prints (if the group\nis transitive) the set on which the group acts transitively?\n\nIf this seems reasonable, I could try working on this.",
    "created_at": "2008-07-06T20:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3544#issuecomment-25022",
    "user": "https://github.com/wdjoyner"
}
```

I would suggest the following: 

(a) There is no bug in is_transitive but the docstring is wrong. 

(b) a "set" method should be implemented for the class PermutationGroup.

(c) Possibly a verbose option could be added which prints (if the group
is transitive) the set on which the group acts transitively?

If this seems reasonable, I could try working on this.



---

archive/issue_comments_025023.json:
```json
{
    "body": "I don't like this approach. Instead, you should be able to tell the permutation group what it is acting on, and all the functions should be consistent. This is part of my goal for my summer work with permutation groups.",
    "created_at": "2008-07-06T20:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3544#issuecomment-25023",
    "user": "https://github.com/rlmill"
}
```

I don't like this approach. Instead, you should be able to tell the permutation group what it is acting on, and all the functions should be consistent. This is part of my goal for my summer work with permutation groups.



---

archive/issue_comments_025024.json:
```json
{
    "body": "Some remarks:\n\n* In GAP it is clearly documented that IsTransitive(G) returns whether or not G is transitive on the set of points moved by G.  That's why this \"bug\" happens (this ticket).  \n  \n* In Magma, all permutation groups G are embedded in a specific S_n and IsTransitive returns whether or not G is transitive on [1..n]. \n\n* Sage has a degree method for permutation groups, which gives back an n.\n\nI think we view permutation groups as contained in S_n, which naturally acts on [1..n], so that should be the default.   I think permutations groups should also at some point in the future be equipable with an action on any set.  But the resulting object will be \"a permutation group equipped with an action\", and is_transitive will be defined relative to that.  So for this ticket, we just need to decide on the default set acted on by a permutation group generated by a list of permutations.  I think the most natural choice is the set {1,2, ..., n} given the embedding in S_n. \n\nAnyway, I've attached a patch that fixes the bug, and makes is_transitive() return whether or not the group is transitive on `[1..G.degree()]`.    I also fixed a few surrounding docstrings and added one to load_hap, so that doctest coverage for the file permgroup.py is now 100%.",
    "created_at": "2009-01-22T12:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3544#issuecomment-25024",
    "user": "https://github.com/williamstein"
}
```

Some remarks:

* In GAP it is clearly documented that IsTransitive(G) returns whether or not G is transitive on the set of points moved by G.  That's why this "bug" happens (this ticket).  
  
* In Magma, all permutation groups G are embedded in a specific S_n and IsTransitive returns whether or not G is transitive on [1..n]. 

* Sage has a degree method for permutation groups, which gives back an n.

I think we view permutation groups as contained in S_n, which naturally acts on [1..n], so that should be the default.   I think permutations groups should also at some point in the future be equipable with an action on any set.  But the resulting object will be "a permutation group equipped with an action", and is_transitive will be defined relative to that.  So for this ticket, we just need to decide on the default set acted on by a permutation group generated by a list of permutations.  I think the most natural choice is the set {1,2, ..., n} given the embedding in S_n. 

Anyway, I've attached a patch that fixes the bug, and makes is_transitive() return whether or not the group is transitive on `[1..G.degree()]`.    I also fixed a few surrounding docstrings and added one to load_hap, so that doctest coverage for the file permgroup.py is now 100%.



---

archive/issue_comments_025025.json:
```json
{
    "body": "Attachment [trac_3544.patch](tarball://root/attachments/some-uuid/ticket3544/trac_3544.patch) by @williamstein created at 2009-01-22 12:52:36",
    "created_at": "2009-01-22T12:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3544#issuecomment-25025",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_3544.patch](tarball://root/attachments/some-uuid/ticket3544/trac_3544.patch) by @williamstein created at 2009-01-22 12:52:36



---

archive/issue_comments_025026.json:
```json
{
    "body": "Looks good to me!",
    "created_at": "2009-01-22T16:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3544#issuecomment-25026",
    "user": "https://github.com/rlmill"
}
```

Looks good to me!



---

archive/issue_comments_025027.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T07:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3544#issuecomment-25027",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025028.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T07:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3544#issuecomment-25028",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1
