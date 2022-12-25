# Issue 5794: [with patch, needs review] G2 branching rules

archive/issues_005794.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  sage-combinat\n\nThis patch implements branching rules for the following inclusions\nof Lie groups: \n\n\n```\nA1 in G2 (along short root) \nA2 in G2\nG2 in B3\nG2 in D4\n```\n\n\nIt goes on top of the following patches:\n\n\n```\ntrac_5721-a.patch\ntrac_5721-b.patch\ntrac_5751.patch\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5794\n\n",
    "created_at": "2009-04-16T01:16:30Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "[with patch, needs review] G2 branching rules",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5794",
    "user": "https://github.com/dwbump"
}
```
Assignee: tbd

CC:  sage-combinat

This patch implements branching rules for the following inclusions
of Lie groups: 


```
A1 in G2 (along short root) 
A2 in G2
G2 in B3
G2 in D4
```


It goes on top of the following patches:


```
trac_5721-a.patch
trac_5721-b.patch
trac_5751.patch
```


Issue created by migration from https://trac.sagemath.org/ticket/5794





---

archive/issue_comments_045327.json:
```json
{
    "body": "Changing assignee from tbd to joyner.",
    "created_at": "2009-04-16T04:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45327",
    "user": "https://github.com/dwbump"
}
```

Changing assignee from tbd to joyner.



---

archive/issue_comments_045328.json:
```json
{
    "body": "Changing component from algebra to group_theory.",
    "created_at": "2009-04-16T04:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45328",
    "user": "https://github.com/dwbump"
}
```

Changing component from algebra to group_theory.



---

archive/issue_comments_045329.json:
```json
{
    "body": "Changing keywords from \"\" to \"lie groups\".",
    "created_at": "2009-04-16T04:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45329",
    "user": "https://github.com/dwbump"
}
```

Changing keywords from "" to "lie groups".



---

archive/issue_comments_045330.json:
```json
{
    "body": "The last change indicates that I changed the owner from tbd to joyner. I don't\nremember doing that, and I don't see how I could have done it accidentally.\nMaybe someone else changed the owner, presumably wdj or mabshoff, but then\ntrac shouldn't show that I did. I am puzzled by this.\n\nHere are some comments about the G2=>A1 Levi branching rule. There is a\nbranching rule G2=>A1xA1 (rule = \"extended\"). This is not implemented yet.\nCurrently Weyl character rings are broke for reducible root systems. (I have a\npatch for that but it is not posted on trac yet.) I intend to implement branching\nto reducible root systems but first I want to do a few exceptional branching\nrules first before tackling the *many* cases of branching to reducible root systems.\n\nSo G2=>A1xA1 will come in a later patch but it is relevant here so I will discuss it.\n\nIn the branching rule G2=>A1xA1, the second A1 is almost but not\nquite the A1 in the G2=>A1 Levi branching rule. (The short root A1.) So it might\nseem that one should implement G2=>A1xA1 and then you would get the G2=>A1\n(rule = \"levi\") branching rule. However this is not quite true. The A1 in the G2=>A1\nbranching rule is GL(2) and the A1 in A1xA1 is SL(2).",
    "created_at": "2009-04-18T13:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45330",
    "user": "https://github.com/dwbump"
}
```

The last change indicates that I changed the owner from tbd to joyner. I don't
remember doing that, and I don't see how I could have done it accidentally.
Maybe someone else changed the owner, presumably wdj or mabshoff, but then
trac shouldn't show that I did. I am puzzled by this.

Here are some comments about the G2=>A1 Levi branching rule. There is a
branching rule G2=>A1xA1 (rule = "extended"). This is not implemented yet.
Currently Weyl character rings are broke for reducible root systems. (I have a
patch for that but it is not posted on trac yet.) I intend to implement branching
to reducible root systems but first I want to do a few exceptional branching
rules first before tackling the *many* cases of branching to reducible root systems.

So G2=>A1xA1 will come in a later patch but it is relevant here so I will discuss it.

In the branching rule G2=>A1xA1, the second A1 is almost but not
quite the A1 in the G2=>A1 Levi branching rule. (The short root A1.) So it might
seem that one should implement G2=>A1xA1 and then you would get the G2=>A1
(rule = "levi") branching rule. However this is not quite true. The A1 in the G2=>A1
branching rule is GL(2) and the A1 in A1xA1 is SL(2).



---

archive/issue_comments_045331.json:
```json
{
    "body": "I uploaded a second patch trac_5794-f4.patch which goes on top of\nthe first. It implements branching rules F4=>B3 (levi), F4=>C3 (levi)\nand F4=>B4 (extended).\n\nThere is another extended rule F4=>C3xA1 (not implemented yet,\nbut hopefully to be implemented later).\n\nIn contrast with G2, for F4, both Levi branching rules are redundant\nsince the Levi subgroups are not maximal. They factor through branching\nrules F4=>B4=>B3 and F4=>C3xA1=>C3. However I implemented them\nfor convenience. You can check directly that\nF4(x).branch(B3,rule=\"levi\") and\nF4(x).branch(B4,rule=\"extended\").branch(B3,rule=\"levi\") return the\nsame thing for x in F4.fundamental_weights().\n\nI compared the output for these rules against those that I could find in a book, \nPatera and Sankoff, Branching rules for representations of simple Lie algebras.",
    "created_at": "2009-04-18T13:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45331",
    "user": "https://github.com/dwbump"
}
```

I uploaded a second patch trac_5794-f4.patch which goes on top of
the first. It implements branching rules F4=>B3 (levi), F4=>C3 (levi)
and F4=>B4 (extended).

There is another extended rule F4=>C3xA1 (not implemented yet,
but hopefully to be implemented later).

In contrast with G2, for F4, both Levi branching rules are redundant
since the Levi subgroups are not maximal. They factor through branching
rules F4=>B4=>B3 and F4=>C3xA1=>C3. However I implemented them
for convenience. You can check directly that
F4(x).branch(B3,rule="levi") and
F4(x).branch(B4,rule="extended").branch(B3,rule="levi") return the
same thing for x in F4.fundamental_weights().

I compared the output for these rules against those that I could find in a book, 
Patera and Sankoff, Branching rules for representations of simple Lie algebras.



---

archive/issue_comments_045332.json:
```json
{
    "body": "Hi Dan,\n\nthe change in ownership happend because you changed the component to \"group_thoery\". For every ticket you work on and post patches you should accept it (see the bottom left), that way ownership stays with you.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T16:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45332",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Dan,

the change in ownership happend because you changed the component to "group_thoery". For every ticket you work on and post patches you should accept it (see the bottom left), that way ownership stays with you.

Cheers,

Michael



---

archive/issue_comments_045333.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-18T19:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45333",
    "user": "https://github.com/dwbump"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045334.json:
```json
{
    "body": "Changing assignee from joyner to @dwbump.",
    "created_at": "2009-04-18T19:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45334",
    "user": "https://github.com/dwbump"
}
```

Changing assignee from joyner to @dwbump.



---

archive/issue_comments_045335.json:
```json
{
    "body": "Attachment [trac_5794-revised.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-revised.patch) by @dwbump created at 2009-05-06 20:16:33",
    "created_at": "2009-05-06T20:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45335",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_5794-revised.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-revised.patch) by @dwbump created at 2009-05-06 20:16:33



---

archive/issue_comments_045336.json:
```json
{
    "body": "I'm taking the liberty of changing the milestone to 4.0 in case there\nis a chance of getting this merged. It is quite a substantial enhancement.",
    "created_at": "2009-05-06T20:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45336",
    "user": "https://github.com/dwbump"
}
```

I'm taking the liberty of changing the milestone to 4.0 in case there
is a chance of getting this merged. It is quite a substantial enhancement.



---

archive/issue_events_013596.json:
```json
{
    "actor": "https://github.com/dwbump",
    "created_at": "2009-05-06T20:21:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5794#event-13596"
}
```



---

archive/issue_comments_045337.json:
```json
{
    "body": "Here are some tests supplementing those implemented in the doctests:\n\nhttp://sporadic.stanford.edu/bump/branch.sage",
    "created_at": "2009-05-07T04:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45337",
    "user": "https://github.com/dwbump"
}
```

Here are some tests supplementing those implemented in the doctests:

http://sporadic.stanford.edu/bump/branch.sage



---

archive/issue_comments_045338.json:
```json
{
    "body": "Attachment [trac_5794-continued.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-continued.patch) by @dwbump created at 2009-05-12 15:27:27",
    "created_at": "2009-05-12T15:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45338",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_5794-continued.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-continued.patch) by @dwbump created at 2009-05-12 15:27:27



---

archive/issue_comments_045339.json:
```json
{
    "body": "Is it possible to remove the first two patches:\n\n\n```\ntrac_5794.patch\ntrac_5794-f4.patch\n```\n\n\nThey are superceded by the other patches. I am going to be adding some\nmore patches to this series, and I think it would be less confusing if the\nfirst two patches are removed. I don't think I can do this without help\nfrom admin.\n\nDan",
    "created_at": "2009-05-16T22:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45339",
    "user": "https://github.com/dwbump"
}
```

Is it possible to remove the first two patches:


```
trac_5794.patch
trac_5794-f4.patch
```


They are superceded by the other patches. I am going to be adding some
more patches to this series, and I think it would be less confusing if the
first two patches are removed. I don't think I can do this without help
from admin.

Dan



---

archive/issue_comments_045340.json:
```json
{
    "body": "Attachment [trac_5794-exceptional.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-exceptional.patch) by @dwbump created at 2009-05-16 23:10:50",
    "created_at": "2009-05-16T23:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45340",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_5794-exceptional.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-exceptional.patch) by @dwbump created at 2009-05-16 23:10:50



---

archive/issue_comments_045341.json:
```json
{
    "body": "Attachment [trac_5794-more-exceptional.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-more-exceptional.patch) by @dwbump created at 2009-05-20 20:23:44",
    "created_at": "2009-05-20T20:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45341",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_5794-more-exceptional.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-more-exceptional.patch) by @dwbump created at 2009-05-20 20:23:44



---

archive/issue_comments_045342.json:
```json
{
    "body": "Since I don't know the order in which patches should be applied, let alone which one to apply, I skimmed through all 4 patches. Most docstrings adhere to the ReST format, but some don't. I'm merely enforcing proper ReST formatting, not reviewing the patches.",
    "created_at": "2009-06-08T03:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45342",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Since I don't know the order in which patches should be applied, let alone which one to apply, I skimmed through all 4 patches. Most docstrings adhere to the ReST format, but some don't. I'm merely enforcing proper ReST formatting, not reviewing the patches.



---

archive/issue_comments_045343.json:
```json
{
    "body": "Apply all four patches in order.\n\n\n```\ntrac_5794-revised.patch\ntrac_5794-continued.patch\ntrac_5794-exceptional.patch\ntrac_5794-more-exceptional.patch\n```\n\n\n> Most docstrings adhere to the ReST format, but some don't.\n\nIf you find nonconforming docstrings, please cite them by line number.\nThere is a lot of doc in these patches.",
    "created_at": "2009-06-11T05:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45343",
    "user": "https://github.com/dwbump"
}
```

Apply all four patches in order.


```
trac_5794-revised.patch
trac_5794-continued.patch
trac_5794-exceptional.patch
trac_5794-more-exceptional.patch
```


> Most docstrings adhere to the ReST format, but some don't.

If you find nonconforming docstrings, please cite them by line number.
There is a lot of doc in these patches.



---

archive/issue_comments_045344.json:
```json
{
    "body": "Replying to [comment:19 bump]:\n> Apply all four patches in order.\n> \n> {{{\n> trac_5794-revised.patch\n> trac_5794-continued.patch\n> trac_5794-exceptional.patch\n> trac_5794-more-exceptional.patch\n> }}}\n>\n> > Most docstrings adhere to the ReST format, but some don't.\n> \n> If you find nonconforming docstrings, please cite them by line number.\n> There is a lot of doc in these patches.\nNote that I'm not qualified to review the mathematical content of the patch. However, I would like to point out that the following patches and line numbers don't conform to ReST formatting:\n\n\n\nIn `trac_5794-revised.patch`:\n* Patching against the file `sage/combinat/root_system/type_A.py`, the examples section starting from line 117.\n* Patching against the file `sage/combinat/root_system/type_reducible.py`, the examples section starting from line 249.\n* Patching against the file `sage/combinat/root_system/weyl_characters.py`, the examples section starting from line 458, the example starting from line 1202, the examples section starting from line 1211, the example starting from line 1227, the examples section starting from line 1235, the example starting from line 1280, the example section starting from line 1299.\nIn `trac_5794-continued.patch`:\n* Patching against the file `sage/combinat/root_system/weyl_characters.py`, the example starting from line 1431, the example starting from line 1443, the example starting from line 1452, the example starting from line 1831, the example starting from line 1842.\nThe following files are not in the reference manual. You might want to consider exposing their features by adding them to the reference manual:\n1. `sage/combinat/root_system/type_A.py`\n2. `sage/combinat/root_system/type_reducible.py`",
    "created_at": "2009-06-19T21:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45344",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:19 bump]:
> Apply all four patches in order.
> 
> {{{
> trac_5794-revised.patch
> trac_5794-continued.patch
> trac_5794-exceptional.patch
> trac_5794-more-exceptional.patch
> }}}
>
> > Most docstrings adhere to the ReST format, but some don't.
> 
> If you find nonconforming docstrings, please cite them by line number.
> There is a lot of doc in these patches.
Note that I'm not qualified to review the mathematical content of the patch. However, I would like to point out that the following patches and line numbers don't conform to ReST formatting:



In `trac_5794-revised.patch`:
* Patching against the file `sage/combinat/root_system/type_A.py`, the examples section starting from line 117.
* Patching against the file `sage/combinat/root_system/type_reducible.py`, the examples section starting from line 249.
* Patching against the file `sage/combinat/root_system/weyl_characters.py`, the examples section starting from line 458, the example starting from line 1202, the examples section starting from line 1211, the example starting from line 1227, the examples section starting from line 1235, the example starting from line 1280, the example section starting from line 1299.
In `trac_5794-continued.patch`:
* Patching against the file `sage/combinat/root_system/weyl_characters.py`, the example starting from line 1431, the example starting from line 1443, the example starting from line 1452, the example starting from line 1831, the example starting from line 1842.
The following files are not in the reference manual. You might want to consider exposing their features by adding them to the reference manual:
1. `sage/combinat/root_system/type_A.py`
2. `sage/combinat/root_system/type_reducible.py`



---

archive/issue_comments_045345.json:
```json
{
    "body": "Attachment [trac_5794-reviewer-nt.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-reviewer-nt.patch) by @dwbump created at 2009-07-21 17:08:40\n\nNicolas Thiery wrote the patch `trac_5794-reviewer-nt.patch`.\nIt is in the combinat patch queue. I took the liberty of uploading\nit.\n\nIt addresses at least some of the ReST complaints.\n\nI am changing the title back to [with patch, needs review] since\napart from the issue of the ReST formatting, the patches still\nneeds a technical review. The following remark is addressed\nto whoever does the technical review. (Brant Jones was suggested.)\n\nThe patches as posted differ slightly from the versions in the combinat queue.\nThe reason for the difference is that the meaning of the is_reducible\nCartan type attribute is changed by #4326. After #4326 (which preceed\nthese patches in the queue) the root system D2 is not reducible. See\n\nhttp://groups.google.com/group/sage-combinat-devel/msg/8b3569b4e2f2b7e1?hl=en\n\nand thread for discussion. (Note: the `patch cartan_type_temporary-1.patch` \nmentioned in that message was qfolded shortly afterwards.)",
    "created_at": "2009-07-21T17:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45345",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_5794-reviewer-nt.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-reviewer-nt.patch) by @dwbump created at 2009-07-21 17:08:40

Nicolas Thiery wrote the patch `trac_5794-reviewer-nt.patch`.
It is in the combinat patch queue. I took the liberty of uploading
it.

It addresses at least some of the ReST complaints.

I am changing the title back to [with patch, needs review] since
apart from the issue of the ReST formatting, the patches still
needs a technical review. The following remark is addressed
to whoever does the technical review. (Brant Jones was suggested.)

The patches as posted differ slightly from the versions in the combinat queue.
The reason for the difference is that the meaning of the is_reducible
Cartan type attribute is changed by #4326. After #4326 (which preceed
these patches in the queue) the root system D2 is not reducible. See

http://groups.google.com/group/sage-combinat-devel/msg/8b3569b4e2f2b7e1?hl=en

and thread for discussion. (Note: the `patch cartan_type_temporary-1.patch` 
mentioned in that message was qfolded shortly afterwards.)



---

archive/issue_comments_045346.json:
```json
{
    "body": "Patch review: trac_5794\n\nThe patch author is a widely acknowledged expert in the area, having written a textbook which includes a discussion of the root systems and branching rules implemented here.  Although we did not check all of the details of the algorithms, the root system code has been used by the reviewer to implement the alcove path model for crystals of Lenart and Postnikov, and the branching code has computed some verified data in type E_6.  This patch implements useful mathematics and the extensive documentation includes references to relevant mathematical literature.\n\nThere are currently two warnings for the reference manual (sage -docbuild reference html); these require help from Sage developers to be fixed.  The Sage library test passes, and all methods have doctests which pass.\n\n-- Brant Jones",
    "created_at": "2009-07-23T14:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45346",
    "user": "https://trac.sagemath.org/admin/accounts/users/sage-combinat"
}
```

Patch review: trac_5794

The patch author is a widely acknowledged expert in the area, having written a textbook which includes a discussion of the root systems and branching rules implemented here.  Although we did not check all of the details of the algorithms, the root system code has been used by the reviewer to implement the alcove path model for crystals of Lenart and Postnikov, and the branching code has computed some verified data in type E_6.  This patch implements useful mathematics and the extensive documentation includes references to relevant mathematical literature.

There are currently two warnings for the reference manual (sage -docbuild reference html); these require help from Sage developers to be fixed.  The Sage library test passes, and all methods have doctests which pass.

-- Brant Jones



---

archive/issue_comments_045347.json:
```json
{
    "body": "This depends on #4326.",
    "created_at": "2009-07-23T14:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45347",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This depends on #4326.



---

archive/issue_comments_045348.json:
```json
{
    "body": "Attachment [trac_5794-long-time-nt.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-long-time-nt.patch) by @nthiery created at 2009-11-19 11:25:22\n\nAnnotates the long tests with their time, and disables one which took 160s.",
    "created_at": "2009-11-19T11:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45348",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_5794-long-time-nt.patch](tarball://root/attachments/some-uuid/ticket5794/trac_5794-long-time-nt.patch) by @nthiery created at 2009-11-19 11:25:22

Annotates the long tests with their time, and disables one which took 160s.



---

archive/issue_comments_045349.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-11-19T11:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45349",
    "user": "https://github.com/nthiery"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_045350.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-19T11:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45350",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_045351.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-19T15:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45351",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_045352.json:
```json
{
    "body": "Positive review from Dan on sage-combinat-devel",
    "created_at": "2009-11-19T15:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45352",
    "user": "https://github.com/nthiery"
}
```

Positive review from Dan on sage-combinat-devel



---

archive/issue_comments_045353.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T17:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45353",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_013597.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-19T17:02:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5794#event-13597"
}
```



---

archive/issue_comments_045354.json:
```json
{
    "body": "Did `trac_5794-long-time-nt.patch` actually get merged?  I don't see these changes in sage-4.3.rc0, and therefore running long doctests on weyl_characters.py still takes forever:\n\n\n```\n[ghitza@sage root_system]$ sd -t -long weyl_characters.py \nsage -t -long \"devel/sage-main/sage/combinat/root_system/weyl_characters.py\"\n         [242.2 s]\n```\n",
    "created_at": "2009-12-14T02:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45354",
    "user": "https://github.com/aghitza"
}
```

Did `trac_5794-long-time-nt.patch` actually get merged?  I don't see these changes in sage-4.3.rc0, and therefore running long doctests on weyl_characters.py still takes forever:


```
[ghitza@sage root_system]$ sd -t -long weyl_characters.py 
sage -t -long "devel/sage-main/sage/combinat/root_system/weyl_characters.py"
         [242.2 s]
```




---

archive/issue_comments_045355.json:
```json
{
    "body": "Thanks for picking that up.  I've merged that one patch in 4.3.rc1.",
    "created_at": "2009-12-14T16:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45355",
    "user": "https://github.com/mwhansen"
}
```

Thanks for picking that up.  I've merged that one patch in 4.3.rc1.



---

archive/issue_comments_045356.json:
```json
{
    "body": "I seems the patches here on Trac are not the ones which were actually merged 4 years ago, which was discovered in #15279.",
    "created_at": "2013-10-17T07:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5794#issuecomment-45356",
    "user": "https://github.com/jdemeyer"
}
```

I seems the patches here on Trac are not the ones which were actually merged 4 years ago, which was discovered in #15279.
