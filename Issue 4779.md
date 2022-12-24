# Issue 4779: [with patch; not ready for review] make function for creating random rings and running automated testing on them

archive/issues_004779.json:
```json
{
    "body": "Assignee: cwitty\n\nThis will uncover numerous bugs.  It already has. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4779\n\n",
    "created_at": "2008-12-13T02:57:56Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch; not ready for review] make function for creating random rings and running automated testing on them",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4779",
    "user": "was"
}
```
Assignee: cwitty

This will uncover numerous bugs.  It already has. 

Issue created by migration from https://trac.sagemath.org/ticket/4779





---

archive/issue_comments_036220.json:
```json
{
    "body": "There are some bits missing here since the first hunk from the first patch does not apply. It shouldn't be too hard to rebase, but I am busy with other things today.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-15T10:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36220",
    "user": "mabshoff"
}
```

There are some bits missing here since the first hunk from the first patch does not apply. It shouldn't be too hard to rebase, but I am busy with other things today.

Cheers,

Michael



---

archive/issue_comments_036221.json:
```json
{
    "body": "I've posted a 100% doctest patch that creates lots of random rings, elements, and does arithmetic with them. \n\nOf course, there are numerous more rings that can be added.  But I think this is a good and very useful first step.\n\n\nThis patch has zero overlap with anything else, so is fairly safe to apply.   The only problem could be that the new random doctests in this patch could potentially expose some bugs, which of course would be good.",
    "created_at": "2008-12-31T02:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36221",
    "user": "was"
}
```

I've posted a 100% doctest patch that creates lots of random rings, elements, and does arithmetic with them. 

Of course, there are numerous more rings that can be added.  But I think this is a good and very useful first step.


This patch has zero overlap with anything else, so is fairly safe to apply.   The only problem could be that the new random doctests in this patch could potentially expose some bugs, which of course would be good.



---

archive/issue_comments_036222.json:
```json
{
    "body": "Attachment [trac_4779.patch](tarball://root/attachments/some-uuid/ticket4779/trac_4779.patch) by was created at 2008-12-31 02:37:09",
    "created_at": "2008-12-31T02:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36222",
    "user": "was"
}
```

Attachment [trac_4779.patch](tarball://root/attachments/some-uuid/ticket4779/trac_4779.patch) by was created at 2008-12-31 02:37:09



---

archive/issue_comments_036223.json:
```json
{
    "body": "Looks good to me. One tiny issue probably worth fixing: The docstring says:\n\n```\nCreate a random prime finite field with cardinality at most 10^20. \n```\n\nBut you create\n\n```\nGF(ZZ.random_element(x=2, y=10**20).next_prime())\n```\n\nSo it is likely, but extremely unlikely that this will happen:\n\n```\nsage: ZZ.random_element(x=10**20-1, y=10**20).next_prime()\n100000000000000000039\n```\n\nThere is an analog issue further down in another docstring IIRC.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-31T03:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36223",
    "user": "mabshoff"
}
```

Looks good to me. One tiny issue probably worth fixing: The docstring says:

```
Create a random prime finite field with cardinality at most 10^20. 
```

But you create

```
GF(ZZ.random_element(x=2, y=10**20).next_prime())
```

So it is likely, but extremely unlikely that this will happen:

```
sage: ZZ.random_element(x=10**20-1, y=10**20).next_prime()
100000000000000000039
```

There is an analog issue further down in another docstring IIRC.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_036224.json:
```json
{
    "body": "**Read-Only Review**\n* I agree with mabshoff's comment on `next_prime` \n* there is a copy'n'paste error in the docstring of rings0\n* shouldn't \"RINGS\" in `rings0` mention number fields and GF(p<sup>n</sup>)?\n* the docstring fro `random_rings` seems wrong (\"level 0 rings\")",
    "created_at": "2008-12-31T18:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36224",
    "user": "malb"
}
```

**Read-Only Review**
* I agree with mabshoff's comment on `next_prime` 
* there is a copy'n'paste error in the docstring of rings0
* shouldn't "RINGS" in `rings0` mention number fields and GF(p<sup>n</sup>)?
* the docstring fro `random_rings` seems wrong ("level 0 rings")



---

archive/issue_comments_036225.json:
```json
{
    "body": "malb's comments should be addressed, but this could be applied as is.\n\nI used this to test lots of polynomials and it was good.  Relative number fields should be added after we upgrade pari.",
    "created_at": "2009-01-24T21:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36225",
    "user": "ncalexan"
}
```

malb's comments should be addressed, but this could be applied as is.

I used this to test lots of polynomials and it was good.  Relative number fields should be added after we upgrade pari.



---

archive/issue_comments_036226.json:
```json
{
    "body": "Attachment [trac_4779-part2.patch](tarball://root/attachments/some-uuid/ticket4779/trac_4779-part2.patch) by was created at 2009-02-20 05:06:49",
    "created_at": "2009-02-20T05:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36226",
    "user": "was"
}
```

Attachment [trac_4779-part2.patch](tarball://root/attachments/some-uuid/ticket4779/trac_4779-part2.patch) by was created at 2009-02-20 05:06:49



---

archive/issue_comments_036227.json:
```json
{
    "body": "+1 - all issues raised have been addressed. The patch applies to my merge tree and passes doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T05:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36227",
    "user": "mabshoff"
}
```

+1 - all issues raised have been addressed. The patch applies to my merge tree and passes doctests.

Cheers,

Michael



---

archive/issue_comments_036228.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T05:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36228",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036229.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T05:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36229",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_comments_036230.json:
```json
{
    "body": "Attachment [trac_4779-reviewer.patch](tarball://root/attachments/some-uuid/ticket4779/trac_4779-reviewer.patch) by mabshoff created at 2009-02-20 08:27:02",
    "created_at": "2009-02-20T08:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36230",
    "user": "mabshoff"
}
```

Attachment [trac_4779-reviewer.patch](tarball://root/attachments/some-uuid/ticket4779/trac_4779-reviewer.patch) by mabshoff created at 2009-02-20 08:27:02



---

archive/issue_comments_036231.json:
```json
{
    "body": "The relative numeber fields still cause trouble, so disabled them for now until the pari-2.4.3svn fix should take care of it.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T08:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4779#issuecomment-36231",
    "user": "mabshoff"
}
```

The relative numeber fields still cause trouble, so disabled them for now until the pari-2.4.3svn fix should take care of it.

Cheers,

Michael
