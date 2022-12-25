# Issue 4531: Sage 3.2.rc1: automorphism_group() doctest failure on 32 bit in sage/combinat/species/library.py

archive/issues_004531.json:
```json
{
    "body": "Assignee: @mwhansen\n\n\n```\nsage -t  devel/sage/sage/combinat/species/library.py \n********************************************************************** \nFile \"/home/john/sage-3.2.rc1/devel/sage/sage/combinat/species/library.py\", \nline 86: \n    sage: a.automorphism_group() \nExpected: \n    Permutation Group with generators [(), ()] \nGot: \n    Permutation Group with generators [()] \n********************************************************************** \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4531\n\n",
    "created_at": "2008-11-15T20:13:32Z",
    "labels": [
        "component: combinatorics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 3.2.rc1: automorphism_group() doctest failure on 32 bit in sage/combinat/species/library.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4531",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @mwhansen


```
sage -t  devel/sage/sage/combinat/species/library.py 
********************************************************************** 
File "/home/john/sage-3.2.rc1/devel/sage/sage/combinat/species/library.py", 
line 86: 
    sage: a.automorphism_group() 
Expected: 
    Permutation Group with generators [(), ()] 
Got: 
    Permutation Group with generators [()] 
********************************************************************** 
```


Issue created by migration from https://trac.sagemath.org/ticket/4531





---

archive/issue_comments_033682.json:
```json
{
    "body": "That seems to be a problem of how Sage displays/prints permutation groups. Internally, everything seems fine. I just produced such a group and I get:\n\n```\nsage: B = species.BinaryTreeSpecies()\nsage: a = B.structures([1,2,3,4,5]).random_element(); a\n(1*5)*((2*3)*4)\nsage: grp = a.automorphism_group()\nsage: grp\nPermutation Group with generators [(), ()]\nsage: grp.list()\n[()]\n```\n\nThe latter two lines are pretty inconsistent.",
    "created_at": "2008-11-16T10:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4531#issuecomment-33682",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

That seems to be a problem of how Sage displays/prints permutation groups. Internally, everything seems fine. I just produced such a group and I get:

```
sage: B = species.BinaryTreeSpecies()
sage: a = B.structures([1,2,3,4,5]).random_element(); a
(1*5)*((2*3)*4)
sage: grp = a.automorphism_group()
sage: grp
Permutation Group with generators [(), ()]
sage: grp.list()
[()]
```

The latter two lines are pretty inconsistent.



---

archive/issue_comments_033683.json:
```json
{
    "body": "Mike Hansen mentioned in IRC that this is the expected output and will post a patch to fix this in the morning.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-16T10:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4531#issuecomment-33683",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mike Hansen mentioned in IRC that this is the expected output and will post a patch to fix this in the morning.

Cheers,

Michael



---

archive/issue_comments_033684.json:
```json
{
    "body": "OK. Thanks for this info!",
    "created_at": "2008-11-16T10:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4531#issuecomment-33684",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

OK. Thanks for this info!



---

archive/issue_comments_033685.json:
```json
{
    "body": "I am fixing this by changing permutation groups to make their gens be canonicalized by default (meaning they are sorted and duplicates are removed).  This is *much* more in the spirit of Sage.  There is still the option to have the generators be exactly what is input (duplicates and all).",
    "created_at": "2008-11-18T07:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4531#issuecomment-33685",
    "user": "https://github.com/williamstein"
}
```

I am fixing this by changing permutation groups to make their gens be canonicalized by default (meaning they are sorted and duplicates are removed).  This is *much* more in the spirit of Sage.  There is still the option to have the generators be exactly what is input (duplicates and all).



---

archive/issue_comments_033686.json:
```json
{
    "body": "Changing assignee from @mwhansen to @williamstein.",
    "created_at": "2008-11-18T07:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4531#issuecomment-33686",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from @mwhansen to @williamstein.



---

archive/issue_comments_033687.json:
```json
{
    "body": "Attachment [sage-4531.patch](tarball://root/attachments/some-uuid/ticket4531/sage-4531.patch) by @williamstein created at 2008-11-18 16:56:50",
    "created_at": "2008-11-18T16:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4531#issuecomment-33687",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4531.patch](tarball://root/attachments/some-uuid/ticket4531/sage-4531.patch) by @williamstein created at 2008-11-18 16:56:50



---

archive/issue_comments_033688.json:
```json
{
    "body": "Attachment [doc-4531.patch](tarball://root/attachments/some-uuid/ticket4531/doc-4531.patch) by @williamstein created at 2008-11-18 16:56:58",
    "created_at": "2008-11-18T16:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4531#issuecomment-33688",
    "user": "https://github.com/williamstein"
}
```

Attachment [doc-4531.patch](tarball://root/attachments/some-uuid/ticket4531/doc-4531.patch) by @williamstein created at 2008-11-18 16:56:58



---

archive/issue_comments_033689.json:
```json
{
    "body": "Attachment [sage-4531-part2.patch](tarball://root/attachments/some-uuid/ticket4531/sage-4531-part2.patch) by @williamstein created at 2008-11-18 17:01:06\n\ntrivial followup",
    "created_at": "2008-11-18T17:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4531#issuecomment-33689",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4531-part2.patch](tarball://root/attachments/some-uuid/ticket4531/sage-4531-part2.patch) by @williamstein created at 2008-11-18 17:01:06

trivial followup



---

archive/issue_comments_033690.json:
```json
{
    "body": "mhansen gave this patch a positive review assuming the doctests pass. Since they do I am changing the subject.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-18T19:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4531#issuecomment-33690",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

mhansen gave this patch a positive review assuming the doctests pass. Since they do I am changing the subject.

Cheers,

Michael



---

archive/issue_comments_033691.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-18T19:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4531#issuecomment-33691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_033692.json:
```json
{
    "body": "Merged all three patches in Sage 3.2.rc2",
    "created_at": "2008-11-18T19:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4531#issuecomment-33692",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.2.rc2
