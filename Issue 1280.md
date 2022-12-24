# Issue 1280: make Permutation(range(10)).random() fast instead of dog slow.

archive/issues_001280.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n\n```\n[01:06am] williamstein: mhansen -- I wonder if you could make this faster?\n[01:06am] williamstein: p = Permutations(range(9)); p\n[01:06am] williamstein: time p.random()\n[01:06am] williamstein: 5 seconds.\n[01:06am] williamstein: Maybe I'm being naive.\n[01:06am] williamstein: for 10 it takes forever.\n[01:06am] mhansen: Heh, yeah -- I definitely could \n[01:07am] williamstein: Since p = Permutations(10); time p.random() is instant.\n[01:07am] williamstein: I was trying to permute the rows of a matrix and thought your combinatorics stuff would be really nice to use\n[01:07am] mhansen: Yep, I just need to override the default random.  There\n[01:07am] williamstein: and it was trivial to figure out how to use it for that, but since I wanted 0-based I used range(10), which made it insanely slow.\n[01:08am] mhansen: 's all sorts of these things that'd be super-easy for an undergrad to do.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1280\n\n",
    "created_at": "2007-11-26T09:09:42Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "make Permutation(range(10)).random() fast instead of dog slow.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1280",
    "user": "@williamstein"
}
```
Assignee: @mwhansen

CC:  sage-combinat


```
[01:06am] williamstein: mhansen -- I wonder if you could make this faster?
[01:06am] williamstein: p = Permutations(range(9)); p
[01:06am] williamstein: time p.random()
[01:06am] williamstein: 5 seconds.
[01:06am] williamstein: Maybe I'm being naive.
[01:06am] williamstein: for 10 it takes forever.
[01:06am] mhansen: Heh, yeah -- I definitely could 
[01:07am] williamstein: Since p = Permutations(10); time p.random() is instant.
[01:07am] williamstein: I was trying to permute the rows of a matrix and thought your combinatorics stuff would be really nice to use
[01:07am] mhansen: Yep, I just need to override the default random.  There
[01:07am] williamstein: and it was trivial to figure out how to use it for that, but since I wanted 0-based I used range(10), which made it insanely slow.
[01:08am] mhansen: 's all sorts of these things that'd be super-easy for an undergrad to do.
```


Issue created by migration from https://trac.sagemath.org/ticket/1280





---

archive/issue_comments_008027.json:
```json
{
    "body": "Attachment [1280.patch](tarball://root/attachments/some-uuid/ticket1280/1280.patch) by @mwhansen created at 2007-11-26 10:16:17",
    "created_at": "2007-11-26T10:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1280#issuecomment-8027",
    "user": "@mwhansen"
}
```

Attachment [1280.patch](tarball://root/attachments/some-uuid/ticket1280/1280.patch) by @mwhansen created at 2007-11-26 10:16:17



---

archive/issue_comments_008028.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-26T10:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1280#issuecomment-8028",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008029.json:
```json
{
    "body": "I skimmed the patch, and nothing jumped out as being wrong.  Also, I applied the patch and doctested the changed file, and tests passed.  (I did not do testall.)\n\nIn short, looks good to me.",
    "created_at": "2007-11-27T05:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1280#issuecomment-8029",
    "user": "cwitty"
}
```

I skimmed the patch, and nothing jumped out as being wrong.  Also, I applied the patch and doctested the changed file, and tests passed.  (I did not do testall.)

In short, looks good to me.



---

archive/issue_comments_008030.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T16:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1280#issuecomment-8030",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008031.json:
```json
{
    "body": "Merged in 2.8.15.alpha1.",
    "created_at": "2007-12-01T16:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1280#issuecomment-8031",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha1.
