# Issue 4047: [with patch, needs review] automorphism groups/canonical labels for hypergraphs

archive/issues_004047.json:
```json
{
    "body": "Assignee: @rlmill\n\nAlso known as nonlinear binary codes. This patch sets up the framework needed for matrix automorphism groups, and automorphism groups of nonbinary linear codes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4047\n\n",
    "created_at": "2008-09-03T17:40:41Z",
    "labels": [
        "component: coding theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] automorphism groups/canonical labels for hypergraphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4047",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

Also known as nonlinear binary codes. This patch sets up the framework needed for matrix automorphism groups, and automorphism groups of nonbinary linear codes.

Issue created by migration from https://trac.sagemath.org/ticket/4047





---

archive/issue_comments_029126.json:
```json
{
    "body": "This seems like an awesome patch. It applies to 3.1.2.alpha4 fine and passes sage -testall.\nI don't understand the cython code, though it appears to be well-documented. However, I have a few general questions anyway:-)\n\n1. Where is there written a \"big picture\" explanation of what the general idea is and where it is going. I know rlm-blog has some details but it seems a lot of details (even in vague global terms) are missing from that, so it would be great to see how this fits into the grand scheme. \n\n2. It seems (based on my vague understanding) that the automorphism group function could be replaced by a more general equivalence function, which returns the group of equivalences if two \"non-linear codes\" are equivalent (and \"False\" otherwise, or something). Is this true?\n\n3. What exactly is a hypergraph and how does it correspond to a non-linear code? (And by non-linear I assume you mean a subset of GF(2)^n which is not necessarily closed under the usual coordinate-wise addition.)\n\nHope these comments help. If not feel free to ignore them!",
    "created_at": "2008-09-03T21:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4047#issuecomment-29126",
    "user": "https://github.com/wdjoyner"
}
```

This seems like an awesome patch. It applies to 3.1.2.alpha4 fine and passes sage -testall.
I don't understand the cython code, though it appears to be well-documented. However, I have a few general questions anyway:-)

1. Where is there written a "big picture" explanation of what the general idea is and where it is going. I know rlm-blog has some details but it seems a lot of details (even in vague global terms) are missing from that, so it would be great to see how this fits into the grand scheme. 

2. It seems (based on my vague understanding) that the automorphism group function could be replaced by a more general equivalence function, which returns the group of equivalences if two "non-linear codes" are equivalent (and "False" otherwise, or something). Is this true?

3. What exactly is a hypergraph and how does it correspond to a non-linear code? (And by non-linear I assume you mean a subset of GF(2)^n which is not necessarily closed under the usual coordinate-wise addition.)

Hope these comments help. If not feel free to ignore them!



---

archive/issue_comments_029127.json:
```json
{
    "body": "> 1. Where is there written a \"big picture\" explanation of what the general idea is and where it is going. I know rlm-blog has some details but it seems a lot of details (even in vague global terms) are missing from that, so it would be great to see how this fits into the grand scheme. \n\nCheck the top of the file sage/groups/perm_gps/partn_ref/automorphism_group_canonical_label.pyx\n\n> 2. It seems (based on my vague understanding) that the automorphism group function could be replaced by a more general equivalence function, which returns the group of equivalences if two \"non-linear codes\" are equivalent (and \"False\" otherwise, or something). Is this true?\n\nThis isn't quite true, the set of isomorphisms does not form a subgroup, but a double coset. If you know the automorphism groups `A1 = Aut(G1)` and `A2 = Aut(G2)`, and you have an isomorphism `g : G1 --> G2`, then any other isomorphism is going to be something in the double coset `A2 g A1.` There's no point computing all the isomorphisms...\n\n> 3. What exactly is a hypergraph and how does it correspond to a non-linear code? (And by non-linear I assume you mean a subset of GF(2)^n which is not necessarily closed under the usual coordinate-wise addition.)\n\nExactly. A hypergraph is a \"graph\" whose \"edges\" need only be subsets of the vertex set, not necessarily of size 2.",
    "created_at": "2008-09-03T23:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4047#issuecomment-29127",
    "user": "https://github.com/rlmill"
}
```

> 1. Where is there written a "big picture" explanation of what the general idea is and where it is going. I know rlm-blog has some details but it seems a lot of details (even in vague global terms) are missing from that, so it would be great to see how this fits into the grand scheme. 

Check the top of the file sage/groups/perm_gps/partn_ref/automorphism_group_canonical_label.pyx

> 2. It seems (based on my vague understanding) that the automorphism group function could be replaced by a more general equivalence function, which returns the group of equivalences if two "non-linear codes" are equivalent (and "False" otherwise, or something). Is this true?

This isn't quite true, the set of isomorphisms does not form a subgroup, but a double coset. If you know the automorphism groups `A1 = Aut(G1)` and `A2 = Aut(G2)`, and you have an isomorphism `g : G1 --> G2`, then any other isomorphism is going to be something in the double coset `A2 g A1.` There's no point computing all the isomorphisms...

> 3. What exactly is a hypergraph and how does it correspond to a non-linear code? (And by non-linear I assume you mean a subset of GF(2)^n which is not necessarily closed under the usual coordinate-wise addition.)

Exactly. A hypergraph is a "graph" whose "edges" need only be subsets of the vertex set, not necessarily of size 2.



---

archive/issue_comments_029128.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-05T19:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4047#issuecomment-29128",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_029129.json:
```json
{
    "body": "Attachment [trac_4047-hypergraphs.patch](tarball://root/attachments/some-uuid/ticket4047/trac_4047-hypergraphs.patch) by @mwhansen created at 2008-09-05 19:37:04\n\nThe updated patch is good too :-)",
    "created_at": "2008-09-05T19:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4047#issuecomment-29129",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4047-hypergraphs.patch](tarball://root/attachments/some-uuid/ticket4047/trac_4047-hypergraphs.patch) by @mwhansen created at 2008-09-05 19:37:04

The updated patch is good too :-)



---

archive/issue_events_009246.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-06T00:52:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4047",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4047#event-9246"
}
```



---

archive/issue_comments_029130.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-06T00:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4047#issuecomment-29130",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc0



---

archive/issue_comments_029131.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-06T00:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4047#issuecomment-29131",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
