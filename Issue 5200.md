# Issue 5200: [with patch, needs review] subsets and subwords bug fix + improvements.

archive/issues_005200.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nKeywords: subsets, subwords\n\nThis patches deals with several issues concerning subwords and subsets:\n1. It implements subsets for finite multisets (sets with repetitions).\n   Before the patch:\n\n```\nsage: Subsets([2,2,3]).list()\n[{}, {2}, {3}, {2, 3}]\n```\n\n     After:\n\n```\nsage: Subsets([2,2,3]).list()\n[[], [2], [3], [2, 2], [2, 3], [2, 2, 3]]\n```\n\n1. It implement `__contains__` which was missing for subsets and subwords:\n   Before:\n\n```\nsage: st = Subsets([1,2,2,3]); Set([1,2]) in st\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n```\n\n     After:\n\n```\nsage: st = Subsets([1,2,2,3]); Set([1,2]) in st\nTrue\n```\n\n1. It fixes a bug in smallest_positions:\n   Before:\n\n```\nsage: sage.combinat.subword.smallest_positions([2,4,3,3,1,2],[1,3,3])\n[4, 4, 4]\n```\n\n     After:\n\n```\nsage.combinat.subword.smallest_positions([2,4,3,3,1,2],[1,3,3])\nFalse\n```\n\n     which means that 113 is not a subword of 243312. \n4. It finally improves the doc and the tests.\n\nSince this is my first trac submission, any comment about this text or the patch is strongly welcome...\n\nIssue created by migration from https://trac.sagemath.org/ticket/5200\n\n",
    "created_at": "2009-02-07T14:02:38Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] subsets and subwords bug fix + improvements.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5200",
    "user": "hivert"
}
```
Assignee: mhansen

CC:  sage-combinat

Keywords: subsets, subwords

This patches deals with several issues concerning subwords and subsets:
1. It implements subsets for finite multisets (sets with repetitions).
   Before the patch:

```
sage: Subsets([2,2,3]).list()
[{}, {2}, {3}, {2, 3}]
```

     After:

```
sage: Subsets([2,2,3]).list()
[[], [2], [3], [2, 2], [2, 3], [2, 2, 3]]
```

1. It implement `__contains__` which was missing for subsets and subwords:
   Before:

```
sage: st = Subsets([1,2,2,3]); Set([1,2]) in st
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
```

     After:

```
sage: st = Subsets([1,2,2,3]); Set([1,2]) in st
True
```

1. It fixes a bug in smallest_positions:
   Before:

```
sage: sage.combinat.subword.smallest_positions([2,4,3,3,1,2],[1,3,3])
[4, 4, 4]
```

     After:

```
sage.combinat.subword.smallest_positions([2,4,3,3,1,2],[1,3,3])
False
```

     which means that 113 is not a subword of 243312. 
4. It finally improves the doc and the tests.

Since this is my first trac submission, any comment about this text or the patch is strongly welcome...

Issue created by migration from https://trac.sagemath.org/ticket/5200





---

archive/issue_comments_039843.json:
```json
{
    "body": "It has been decided (direct talk with Nicolas + irssi with Mike) that the user has to explicitely set that he want multisets. Therefore, on the contrary that is anounced, the following is not working:\n\n```\nsage: Subsets([2,2,3]).list()\n[[], [2], [3], [2, 2], [2, 3], [2, 2, 3]]\n```\n\nInstead one should write\n\n```\nsage: Subsets([2,2,3], multiset=True).list()\n[[], [2], [3], [2, 2], [2, 3], [2, 2, 3]]\n```\n",
    "created_at": "2009-03-01T15:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39843",
    "user": "hivert"
}
```

It has been decided (direct talk with Nicolas + irssi with Mike) that the user has to explicitely set that he want multisets. Therefore, on the contrary that is anounced, the following is not working:

```
sage: Subsets([2,2,3]).list()
[[], [2], [3], [2, 2], [2, 3], [2, 2, 3]]
```

Instead one should write

```
sage: Subsets([2,2,3], multiset=True).list()
[[], [2], [3], [2, 2], [2, 3], [2, 2, 3]]
```




---

archive/issue_comments_039844.json:
```json
{
    "body": "Changing assignee from mhansen to hivert.",
    "created_at": "2009-03-01T15:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39844",
    "user": "hivert"
}
```

Changing assignee from mhansen to hivert.



---

archive/issue_comments_039845.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-01T15:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39845",
    "user": "hivert"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039846.json:
```json
{
    "body": "Sorry for the mess with the description... I just realize because of my mistake that it is possible to change the description. :-)  \n\nI've uploaded a new patch according to remark of Nicolas and Mike. It should be ready for review and hopefully integration. \n\nCheers,\n\nFlorent",
    "created_at": "2009-03-01T15:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39846",
    "user": "hivert"
}
```

Sorry for the mess with the description... I just realize because of my mistake that it is possible to change the description. :-)  

I've uploaded a new patch according to remark of Nicolas and Mike. It should be ready for review and hopefully integration. 

Cheers,

Florent



---

archive/issue_comments_039847.json:
```json
{
    "body": "New patch after Nicolas review.",
    "created_at": "2009-03-17T17:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39847",
    "user": "hivert"
}
```

New patch after Nicolas review.



---

archive/issue_comments_039848.json:
```json
{
    "body": "Attachment\n\nNicolas sent me a review on sage-combinat-devel. The new subsets_subwords-5200-submitted.2.patch patch fixes the various problems pointed out by the review (typos + code improvements). \n\nFlorent",
    "created_at": "2009-03-17T17:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39848",
    "user": "hivert"
}
```

Attachment

Nicolas sent me a review on sage-combinat-devel. The new subsets_subwords-5200-submitted.2.patch patch fixes the various problems pointed out by the review (typos + code improvements). 

Florent



---

archive/issue_comments_039849.json:
```json
{
    "body": "Florent: feel free to switch the title to with review after the following micro updates:\n- iterate -> iterates\n- of all -> \"\"",
    "created_at": "2009-03-19T18:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39849",
    "user": "nthiery"
}
```

Florent: feel free to switch the title to with review after the following micro updates:
- iterate -> iterates
- of all -> ""



---

archive/issue_comments_039850.json:
```json
{
    "body": "Attachment\n\nLast review patch.",
    "created_at": "2009-03-19T20:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39850",
    "user": "hivert"
}
```

Attachment

Last review patch.



---

archive/issue_comments_039851.json:
```json
{
    "body": "The review patch I just submitted address Nicolas last comment.\nSorry for the mess with several version of the patch. The correct patch are:\n\n* attachment:subsets_subwords-5200-submitted.2.patch\n* attachment:subsets_subwords-5200-review.patch\n\nAccording to Nicolas la remarks I allow myself to change the review title. Please tell me if it's not allowed by the review rules. \n\nFlorent",
    "created_at": "2009-03-19T21:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39851",
    "user": "hivert"
}
```

The review patch I just submitted address Nicolas last comment.
Sorry for the mess with several version of the patch. The correct patch are:

* attachment:subsets_subwords-5200-submitted.2.patch
* attachment:subsets_subwords-5200-review.patch

According to Nicolas la remarks I allow myself to change the review title. Please tell me if it's not allowed by the review rules. 

Florent



---

archive/issue_comments_039852.json:
```json
{
    "body": "\"with review\" is meaningless :)\n\nNicolas: Can you give this a formal positive review?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T06:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39852",
    "user": "mabshoff"
}
```

"with review" is meaningless :)

Nicolas: Can you give this a formal positive review?

Cheers,

Michael



---

archive/issue_comments_039853.json:
```json
{
    "body": "After re-reading Nicola's comment I am giving this patch a positive review in his name. The two patches also pass doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T06:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39853",
    "user": "mabshoff"
}
```

After re-reading Nicola's comment I am giving this patch a positive review in his name. The two patches also pass doctests.

Cheers,

Michael



---

archive/issue_comments_039854.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T06:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39854",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039855.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T06:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5200#issuecomment-39855",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.1.alpha0.

Cheers,

Michael
