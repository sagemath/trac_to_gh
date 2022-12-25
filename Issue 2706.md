# Issue 2706: [with patch] Fast bitset implimentation

archive/issues_002706.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @rlmill\n\nSet of functions for manipulating individual bits in lists of longs. This will be especially helpful for the graph isomorphism code as it provides a level of abstraction that should help eliminate bugs. \n\nIt is a pxi file so that the functions can be declared and used inline. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2706\n\n",
    "created_at": "2008-03-28T20:00:01Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch] Fast bitset implimentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2706",
    "user": "https://github.com/robertwb"
}
```
Assignee: @rlmill

CC:  @rlmill

Set of functions for manipulating individual bits in lists of longs. This will be especially helpful for the graph isomorphism code as it provides a level of abstraction that should help eliminate bugs. 

It is a pxi file so that the functions can be declared and used inline. 

Issue created by migration from https://trac.sagemath.org/ticket/2706





---

archive/issue_comments_018624.json:
```json
{
    "body": "Attachment [bitsets.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets.patch) by @robertwb created at 2008-03-28 20:00:10",
    "created_at": "2008-03-28T20:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18624",
    "user": "https://github.com/robertwb"
}
```

Attachment [bitsets.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets.patch) by @robertwb created at 2008-03-28 20:00:10



---

archive/issue_comments_018625.json:
```json
{
    "body": "Attachment [bitsets2.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets2.patch) by @robertwb created at 2008-03-28 20:52:49",
    "created_at": "2008-03-28T20:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18625",
    "user": "https://github.com/robertwb"
}
```

Attachment [bitsets2.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets2.patch) by @robertwb created at 2008-03-28 20:52:49



---

archive/issue_comments_018626.json:
```json
{
    "body": "Looks good, passes tests. Applies cleanly to 2.11.alpha1.",
    "created_at": "2008-03-28T22:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18626",
    "user": "https://github.com/rlmill"
}
```

Looks good, passes tests. Applies cleanly to 2.11.alpha1.



---

archive/issue_comments_018627.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T00:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18627",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018628.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-29T00:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_018629.json:
```json
{
    "body": "Attachment [bitsets3.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets3.patch) by @robertwb created at 2008-03-29 01:45:46\n\nFixed minor bug, added more doctests. \n\nAll tests pass on 32-bit intel OS X and on sage.math (modulo limbs count)",
    "created_at": "2008-03-29T01:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18629",
    "user": "https://github.com/robertwb"
}
```

Attachment [bitsets3.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets3.patch) by @robertwb created at 2008-03-29 01:45:46

Fixed minor bug, added more doctests. 

All tests pass on 32-bit intel OS X and on sage.math (modulo limbs count)



---

archive/issue_comments_018630.json:
```json
{
    "body": "this patch should fix the limb size doctest issue on 32 vs. 64 bit",
    "created_at": "2008-03-29T02:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18630",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

this patch should fix the limb size doctest issue on 32 vs. 64 bit



---

archive/issue_comments_018631.json:
```json
{
    "body": "Attachment [trac_2706_bitsets4.patch](tarball://root/attachments/some-uuid/ticket2706/trac_2706_bitsets4.patch) by mabshoff created at 2008-03-29 02:02:13\n\nMerged all four patches in Sage 2.11.alpha2",
    "created_at": "2008-03-29T02:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18631",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2706_bitsets4.patch](tarball://root/attachments/some-uuid/ticket2706/trac_2706_bitsets4.patch) by mabshoff created at 2008-03-29 02:02:13

Merged all four patches in Sage 2.11.alpha2
