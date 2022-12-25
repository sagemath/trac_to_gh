# Issue 2853: A correction to the weight of crystal elements for type A and a speedup for all types

archive/issues_002853.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nFor Cartan Types 'A' a problem with the weight function of crystals was described here:\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/7cdfe075257ba963?hl=en\n\nThe method of correcting this problem was to hard-code the weight in the crystals of letters, \nand to have the crystals of tensors get the weight of a tensor element by summing the weights \nof its constituents. This alters the weight for Type A (correcting the defect) and returns the\nsame weight as the old algorithm for other Cartan types.\n\nWhen the patch was implemented it was found to be 2-3 times faster than the old algorithm.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2853\n\n",
    "created_at": "2008-04-08T05:55:37Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "A correction to the weight of crystal elements for type A and a speedup for all types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2853",
    "user": "https://github.com/dwbump"
}
```
Assignee: @mwhansen

CC:  sage-combinat

For Cartan Types 'A' a problem with the weight function of crystals was described here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/7cdfe075257ba963?hl=en

The method of correcting this problem was to hard-code the weight in the crystals of letters, 
and to have the crystals of tensors get the weight of a tensor element by summing the weights 
of its constituents. This alters the weight for Type A (correcting the defect) and returns the
same weight as the old algorithm for other Cartan types.

When the patch was implemented it was found to be 2-3 times faster than the old algorithm.

Issue created by migration from https://trac.sagemath.org/ticket/2853





---

archive/issue_comments_019537.json:
```json
{
    "body": "patch correcting problem with weights for crystal graphs of type A and speeding up all Cartan types.",
    "created_at": "2008-04-08T05:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2853#issuecomment-19537",
    "user": "https://github.com/dwbump"
}
```

patch correcting problem with weights for crystal graphs of type A and speeding up all Cartan types.



---

archive/issue_comments_019538.json:
```json
{
    "body": "Attachment [crystal_weights.patch](tarball://root/attachments/some-uuid/ticket2853/crystal_weights.patch) by mabshoff created at 2008-04-08 08:57:44",
    "created_at": "2008-04-08T08:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2853#issuecomment-19538",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [crystal_weights.patch](tarball://root/attachments/some-uuid/ticket2853/crystal_weights.patch) by mabshoff created at 2008-04-08 08:57:44



---

archive/issue_comments_019539.json:
```json
{
    "body": "Attachment [2853.patch](tarball://root/attachments/some-uuid/ticket2853/2853.patch) by @mwhansen created at 2008-04-08 09:28:25",
    "created_at": "2008-04-08T09:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2853#issuecomment-19539",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2853.patch](tarball://root/attachments/some-uuid/ticket2853/2853.patch) by @mwhansen created at 2008-04-08 09:28:25



---

archive/issue_comments_019540.json:
```json
{
    "body": "Hi Dan,\n\nI've updated a patch to move the tests for .weight() to the docstring for the definition of weight.  There is an issue with ['G',2] though:\n\n\nBefore the patch:\n\n```\nsage: C = CrystalOfLetters(['G',2])\nsage: hwvs = C.highest_weight_vectors()\nsage: wlr = C.weight_lattice_realization()\nsage: v = hwvs[0]; v\n1\nsage: v.weight()\n(1, 0, -1)\nsage: wlr.weyl_dimension(v.weight())\n7\n```\n\n\nAfter the patch:\n\n```\nsage: C = CrystalOfLetters(['G',2])\nsage: wlr = C.weight_lattice_realization()\nsage: hwvs = C.highest_weight_vectors()\nsage: hwvs\n[1]\nsage: v = hwvs[0]; v\n1\nsage: v.weight()\n(-1, 0, 1)\nsage: wlr.weyl_dimension(v.weight())\n0\n```\n",
    "created_at": "2008-04-08T09:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2853#issuecomment-19540",
    "user": "https://github.com/mwhansen"
}
```

Hi Dan,

I've updated a patch to move the tests for .weight() to the docstring for the definition of weight.  There is an issue with ['G',2] though:


Before the patch:

```
sage: C = CrystalOfLetters(['G',2])
sage: hwvs = C.highest_weight_vectors()
sage: wlr = C.weight_lattice_realization()
sage: v = hwvs[0]; v
1
sage: v.weight()
(1, 0, -1)
sage: wlr.weyl_dimension(v.weight())
7
```


After the patch:

```
sage: C = CrystalOfLetters(['G',2])
sage: wlr = C.weight_lattice_realization()
sage: hwvs = C.highest_weight_vectors()
sage: hwvs
[1]
sage: v = hwvs[0]; v
1
sage: v.weight()
(-1, 0, 1)
sage: wlr.weyl_dimension(v.weight())
0
```




---

archive/issue_comments_019541.json:
```json
{
    "body": "I was unable to confirm the problem with G2. I applied the patch in the modified form\nthat you posted, and sage: wlr.weyl_dimension(v.weight()) returns 7 for me.\n\nDan",
    "created_at": "2008-04-08T16:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2853#issuecomment-19541",
    "user": "https://github.com/dwbump"
}
```

I was unable to confirm the problem with G2. I applied the patch in the modified form
that you posted, and sage: wlr.weyl_dimension(v.weight()) returns 7 for me.

Dan



---

archive/issue_comments_019542.json:
```json
{
    "body": "Replying to [comment:3 bump]:\n> I was unable to confirm the problem with G2. I applied the patch in the modified form\n> that you posted, and sage: wlr.weyl_dimension(v.weight()) returns 7 for me.\n> \n> Dan\n\nHi Dan,\n\nI can confirm that with 3.0.alpha2 and your patch applied wlr.weyl_dimension(v.weight()) returns 0. With what build did you try? Are there any other patches you have in your tree?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-08T17:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2853#issuecomment-19542",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 bump]:
> I was unable to confirm the problem with G2. I applied the patch in the modified form
> that you posted, and sage: wlr.weyl_dimension(v.weight()) returns 7 for me.
> 
> Dan

Hi Dan,

I can confirm that with 3.0.alpha2 and your patch applied wlr.weyl_dimension(v.weight()) returns 0. With what build did you try? Are there any other patches you have in your tree?

Cheers,

Michael



---

archive/issue_comments_019543.json:
```json
{
    "body": "> Hi Dan,\n> \n> I can confirm that with 3.0.alpha2 and your patch applied wlr.weyl_dimension(v.weight()) returns 0. With what build did you try? Are there any other patches you have in your tree?\n> \n> Cheers,\n> \n> Michael\n\nI did this with 3.0-alph0 and no other patches. I can install 3.0.alpha2 and debug the patch.\n\nDan",
    "created_at": "2008-04-08T19:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2853#issuecomment-19543",
    "user": "https://github.com/dwbump"
}
```

> Hi Dan,
> 
> I can confirm that with 3.0.alpha2 and your patch applied wlr.weyl_dimension(v.weight()) returns 0. With what build did you try? Are there any other patches you have in your tree?
> 
> Cheers,
> 
> Michael

I did this with 3.0-alph0 and no other patches. I can install 3.0.alpha2 and debug the patch.

Dan



---

archive/issue_comments_019544.json:
```json
{
    "body": "Attachment [2853.1.patch](tarball://root/attachments/some-uuid/ticket2853/2853.1.patch) by @dwbump created at 2008-04-08 23:17:29\n\nIt turns out that I had forgotten the G2 patch that went in on Saturday.\n\nI corrected the patch and added it as 2853.1.patch. I believe it is now\ncorrect.\n\nDan",
    "created_at": "2008-04-08T23:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2853#issuecomment-19544",
    "user": "https://github.com/dwbump"
}
```

Attachment [2853.1.patch](tarball://root/attachments/some-uuid/ticket2853/2853.1.patch) by @dwbump created at 2008-04-08 23:17:29

It turns out that I had forgotten the G2 patch that went in on Saturday.

I corrected the patch and added it as 2853.1.patch. I believe it is now
correct.

Dan



---

archive/issue_comments_019545.json:
```json
{
    "body": "Looks good to me.  Apply just 2853.1.patch.",
    "created_at": "2008-04-08T23:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2853#issuecomment-19545",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  Apply just 2853.1.patch.



---

archive/issue_events_006535.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-09T00:11:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2853#event-6535"
}
```



---

archive/issue_comments_019546.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-09T00:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2853#issuecomment-19546",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019547.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3.",
    "created_at": "2008-04-09T00:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2853#issuecomment-19547",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha3.
