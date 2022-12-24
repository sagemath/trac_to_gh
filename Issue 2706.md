# Issue 2706: [with patch] Fast bitset implimentation

archive/issues_002706.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @rlmill\n\nSet of functions for manipulating individual bits in lists of longs. This will be especially helpful for the graph isomorphism code as it provides a level of abstraction that should help eliminate bugs. \n\nIt is a pxi file so that the functions can be declared and used inline. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2706\n\n",
    "created_at": "2008-03-28T20:00:01Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch] Fast bitset implimentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2706",
    "user": "@robertwb"
}
```
Assignee: @rlmill

CC:  @rlmill

Set of functions for manipulating individual bits in lists of longs. This will be especially helpful for the graph isomorphism code as it provides a level of abstraction that should help eliminate bugs. 

It is a pxi file so that the functions can be declared and used inline. 

Issue created by migration from https://trac.sagemath.org/ticket/2706





---

archive/issue_comments_018663.json:
```json
{
    "body": "Attachment [bitsets.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets.patch) by @robertwb created at 2008-03-28 20:00:10",
    "created_at": "2008-03-28T20:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18663",
    "user": "@robertwb"
}
```

Attachment [bitsets.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets.patch) by @robertwb created at 2008-03-28 20:00:10



---

archive/issue_comments_018664.json:
```json
{
    "body": "Attachment [bitsets2.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets2.patch) by @robertwb created at 2008-03-28 20:52:49",
    "created_at": "2008-03-28T20:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18664",
    "user": "@robertwb"
}
```

Attachment [bitsets2.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets2.patch) by @robertwb created at 2008-03-28 20:52:49



---

archive/issue_comments_018665.json:
```json
{
    "body": "Looks good, passes tests. Applies cleanly to 2.11.alpha1.",
    "created_at": "2008-03-28T22:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18665",
    "user": "@rlmill"
}
```

Looks good, passes tests. Applies cleanly to 2.11.alpha1.



---

archive/issue_comments_018666.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T00:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18666",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018667.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-29T00:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18667",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_018668.json:
```json
{
    "body": "Attachment [bitsets3.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets3.patch) by @robertwb created at 2008-03-29 01:45:46\n\nFixed minor bug, added more doctests. \n\nAll tests pass on 32-bit intel OS X and on sage.math (modulo limbs count)",
    "created_at": "2008-03-29T01:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18668",
    "user": "@robertwb"
}
```

Attachment [bitsets3.patch](tarball://root/attachments/some-uuid/ticket2706/bitsets3.patch) by @robertwb created at 2008-03-29 01:45:46

Fixed minor bug, added more doctests. 

All tests pass on 32-bit intel OS X and on sage.math (modulo limbs count)



---

archive/issue_comments_018669.json:
```json
{
    "body": "this patch should fix the limb size doctest issue on 32 vs. 64 bit",
    "created_at": "2008-03-29T02:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18669",
    "user": "mabshoff"
}
```

this patch should fix the limb size doctest issue on 32 vs. 64 bit



---

archive/issue_comments_018670.json:
```json
{
    "body": "Attachment [trac_2706_bitsets4.patch](tarball://root/attachments/some-uuid/ticket2706/trac_2706_bitsets4.patch) by mabshoff created at 2008-03-29 02:02:13\n\nMerged all four patches in Sage 2.11.alpha2",
    "created_at": "2008-03-29T02:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2706#issuecomment-18670",
    "user": "mabshoff"
}
```

Attachment [trac_2706_bitsets4.patch](tarball://root/attachments/some-uuid/ticket2706/trac_2706_bitsets4.patch) by mabshoff created at 2008-03-29 02:02:13

Merged all four patches in Sage 2.11.alpha2
