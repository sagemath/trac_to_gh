# Issue 8490: Bad behavior of is_square_free for Words

archive/issues_008490.json:
```json
{
    "body": "Assignee: @videlec\n\nCC:  sage-combinat\n\nKeywords: word\n\nThe method is_square_free of sage.combinat.words.word.Word returns the wrong value in special cases (including squares !)\n\n```\nsage: Word(\"aa\").is_square_free()  # the funniest\nTrue\nsage: Word(\"baa\").is_square_free()\nTrue\nsage: Word(\"cbaa\").is_square_free()\nTrue\nsage: Word(\"dcbaa\").is_square_free()\nTrue\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8490\n\n",
    "closed_at": "2010-06-05T22:30:25Z",
    "created_at": "2010-03-10T16:38:46Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Bad behavior of is_square_free for Words",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8490",
    "user": "https://github.com/videlec"
}
```
Assignee: @videlec

CC:  sage-combinat

Keywords: word

The method is_square_free of sage.combinat.words.word.Word returns the wrong value in special cases (including squares !)

```
sage: Word("aa").is_square_free()  # the funniest
True
sage: Word("baa").is_square_free()
True
sage: Word("cbaa").is_square_free()
True
sage: Word("dcbaa").is_square_free()
True
```

Issue created by migration from https://trac.sagemath.org/ticket/8490





---

archive/issue_comments_076435.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T16:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76435",
    "user": "https://github.com/videlec"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076436.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-10T17:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76436",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076437.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-03-10T17:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76437",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_076438.json:
```json
{
    "body": "Oups, intersection with #8429 which refactors the code of sage.combinat.words.\n\nI post soon a new patch that apply only after #8429 and I think it's better.",
    "created_at": "2010-03-10T17:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76438",
    "user": "https://github.com/videlec"
}
```

Oups, intersection with #8429 which refactors the code of sage.combinat.words.

I post soon a new patch that apply only after #8429 and I think it's better.



---

archive/issue_comments_076439.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-10T17:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76439",
    "user": "https://github.com/videlec"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076440.json:
```json
{
    "body": "another one-line correction that applies after #8429",
    "created_at": "2010-03-10T17:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76440",
    "user": "https://github.com/videlec"
}
```

another one-line correction that applies after #8429



---

archive/issue_comments_076441.json:
```json
{
    "body": "Attachment [trac_8490-square_free-vd.2.patch](tarball://root/attachments/some-uuid/ticket8490/trac_8490-square_free-vd.2.patch) by @videlec created at 2010-03-10 17:40:39\n\nanother one-line correction that applies after #8429",
    "created_at": "2010-03-10T17:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76441",
    "user": "https://github.com/videlec"
}
```

Attachment [trac_8490-square_free-vd.2.patch](tarball://root/attachments/some-uuid/ticket8490/trac_8490-square_free-vd.2.patch) by @videlec created at 2010-03-10 17:40:39

another one-line correction that applies after #8429



---

archive/issue_comments_076442.json:
```json
{
    "body": "Attachment [trac_8490-square_free-vd.3.patch](tarball://root/attachments/some-uuid/ticket8490/trac_8490-square_free-vd.3.patch) by @videlec created at 2010-03-10 22:50:51\n\nApply only this",
    "created_at": "2010-03-10T22:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76442",
    "user": "https://github.com/videlec"
}
```

Attachment [trac_8490-square_free-vd.3.patch](tarball://root/attachments/some-uuid/ticket8490/trac_8490-square_free-vd.3.patch) by @videlec created at 2010-03-10 22:50:51

Apply only this



---

archive/issue_comments_076443.json:
```json
{
    "body": "Attachment [trac_8490-square_free-vd.patch](tarball://root/attachments/some-uuid/ticket8490/trac_8490-square_free-vd.patch) by @seblabbe created at 2010-04-28 10:12:41\n\nThe same bug was occuring with `is_cube_free` :\n\n```\nsage: Word('111').is_cube_free()\nTrue\nsage: Word('2111').is_cube_free()\nTrue\nsage: Word('32111').is_cube_free()\nTrue\n```\n\nI just applied a patch which fixes this problem. I changed some doctests of both `is_square_free` and `is_cube_free`. I also removed a useless slice in the code of both functions and this gives good improvements in timings :\n\nBEFORE:\n\n```\nsage: t = words.ThueMorseWord()\nsage: %timeit t[:100].is_cube_free()\n5 loops, best of 3: 3.13 s per loop\n```\n\nAFTER:\n\n```\nsage: t = words.ThueMorseWord()\nsage: %timeit t[:100].is_cube_free()\n5 loops, best of 3: 1.18 s per loop\n```",
    "created_at": "2010-04-28T10:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76443",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8490-square_free-vd.patch](tarball://root/attachments/some-uuid/ticket8490/trac_8490-square_free-vd.patch) by @seblabbe created at 2010-04-28 10:12:41

The same bug was occuring with `is_cube_free` :

```
sage: Word('111').is_cube_free()
True
sage: Word('2111').is_cube_free()
True
sage: Word('32111').is_cube_free()
True
```

I just applied a patch which fixes this problem. I changed some doctests of both `is_square_free` and `is_cube_free`. I also removed a useless slice in the code of both functions and this gives good improvements in timings :

BEFORE:

```
sage: t = words.ThueMorseWord()
sage: %timeit t[:100].is_cube_free()
5 loops, best of 3: 3.13 s per loop
```

AFTER:

```
sage: t = words.ThueMorseWord()
sage: %timeit t[:100].is_cube_free()
5 loops, best of 3: 1.18 s per loop
```



---

archive/issue_comments_076444.json:
```json
{
    "body": "Applies over the precedent patch",
    "created_at": "2010-04-28T10:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76444",
    "user": "https://github.com/seblabbe"
}
```

Applies over the precedent patch



---

archive/issue_comments_076445.json:
```json
{
    "body": "Attachment [trac_8490_review-sl.patch](tarball://root/attachments/some-uuid/ticket8490/trac_8490_review-sl.patch) by @seblabbe created at 2010-04-28 10:21:34",
    "created_at": "2010-04-28T10:21:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76445",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8490_review-sl.patch](tarball://root/attachments/some-uuid/ticket8490/trac_8490_review-sl.patch) by @seblabbe created at 2010-04-28 10:21:34



---

archive/issue_comments_076446.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-28T10:21:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76446",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076447.json:
```json
{
    "body": "Hello !! This patch is finem except for a small unimportant thing which bothered me :\n\n```\nfor end in xrange(start+3, L+1, 3): \n```\n\nWhy go up to L+1 when the last letter is L-1 ? The algorithm is still correct as \n\n```\nWord(\"abc\")[:50000]\n```\n\nraises no exception, but as there is no reason to.... So I give a positive review to the patches above, and trac_8490_review-ncohen.patch is left to be reviewed by anyone other than me (quoting Minh) :-)\n\nThank you for this patch !!\n\nNathann",
    "created_at": "2010-05-09T17:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76447",
    "user": "https://github.com/nathanncohen"
}
```

Hello !! This patch is finem except for a small unimportant thing which bothered me :

```
for end in xrange(start+3, L+1, 3): 
```

Why go up to L+1 when the last letter is L-1 ? The algorithm is still correct as 

```
Word("abc")[:50000]
```

raises no exception, but as there is no reason to.... So I give a positive review to the patches above, and trac_8490_review-ncohen.patch is left to be reviewed by anyone other than me (quoting Minh) :-)

Thank you for this patch !!

Nathann



---

archive/issue_comments_076448.json:
```json
{
    "body": "The patches are to be applied in this order :\n\n* trac_8490-square_free-vd.patch\n* trac_8490_review-sl.patch\n* trac_8490_review-ncohen.patch\n\nNathann",
    "created_at": "2010-05-09T17:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76448",
    "user": "https://github.com/nathanncohen"
}
```

The patches are to be applied in this order :

* trac_8490-square_free-vd.patch
* trac_8490_review-sl.patch
* trac_8490_review-ncohen.patch

Nathann



---

archive/issue_comments_076449.json:
```json
{
    "body": "Replying to [comment:7 ncohen]:\n> Hello !! This patch is finem except for a small unimportant thing which bothered me :\n> \n> \n> ```\n> for end in xrange(start+3, L+1, 3): \n> ```\n> \n> Why go up to L+1 when the last letter is L-1 ?\n\n\nFirst, xrange returns a left-closed and right-open interval. Hence, one needs to write something like `xrange(0,L+1)` if one wants to go up to `L` :\n\n```\nsage: list(xrange(0,5))\n[0, 1, 2, 3, 4]\n```\n\nSecond, the variable `end` is not used to get a specific item in self but for slicing self. Hence, if one wants to consider all the slicing possibilities, the variable `end` must take the last possible value `L`:\n\n```\nsage: list(xrange(0,5)) [2:5]   #is good\n[2, 3, 4]\nsage: list(xrange(0,5)) [2:4]   #forgets the last letter\n[2, 3]\n```\n\nHence, your patch is strange in the sense that doctests should not pass!\n\n> The algorithm is still correct as \n> \n> \n> ```\n> Word(\"abc\")[:50000]\n> ```\n> \n> raises no exception, but as there is no reason to.... \n\n\nWe made the choice of following the Python behavior for slices that goes too far:\n\n```\nsage: L = range(10)\nsage: L\n[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\nsage: L[:100]\n[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n```\n\nS\u00e9bastien",
    "created_at": "2010-05-13T14:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76449",
    "user": "https://github.com/seblabbe"
}
```

Replying to [comment:7 ncohen]:
> Hello !! This patch is finem except for a small unimportant thing which bothered me :
> 
> 
> ```
> for end in xrange(start+3, L+1, 3): 
> ```
> 
> Why go up to L+1 when the last letter is L-1 ?


First, xrange returns a left-closed and right-open interval. Hence, one needs to write something like `xrange(0,L+1)` if one wants to go up to `L` :

```
sage: list(xrange(0,5))
[0, 1, 2, 3, 4]
```

Second, the variable `end` is not used to get a specific item in self but for slicing self. Hence, if one wants to consider all the slicing possibilities, the variable `end` must take the last possible value `L`:

```
sage: list(xrange(0,5)) [2:5]   #is good
[2, 3, 4]
sage: list(xrange(0,5)) [2:4]   #forgets the last letter
[2, 3]
```

Hence, your patch is strange in the sense that doctests should not pass!

> The algorithm is still correct as 
> 
> 
> ```
> Word("abc")[:50000]
> ```
> 
> raises no exception, but as there is no reason to.... 


We made the choice of following the Python behavior for slices that goes too far:

```
sage: L = range(10)
sage: L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sage: L[:100]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Sébastien



---

archive/issue_comments_076450.json:
```json
{
    "body": "Replying to [comment:8 ncohen]:\n> The patches are to be applied in this order :\n> \n> * trac_8490-square_free-vd.patch\n> * trac_8490_review-sl.patch\n> * trac_8490_review-ncohen.patch\n> \n> Nathann\n\n\nThe patch `trac_8490_review-ncohen.patch` reintroduce the same bug as the current ticket is trying to solve. Hence, I think the patches are to be reviewed in this order again :\n\n* trac_8490-square_free-vd.patch\n* trac_8490_review-sl.patch\n\nS\u00e9bastien",
    "created_at": "2010-05-13T14:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76450",
    "user": "https://github.com/seblabbe"
}
```

Replying to [comment:8 ncohen]:
> The patches are to be applied in this order :
> 
> * trac_8490-square_free-vd.patch
> * trac_8490_review-sl.patch
> * trac_8490_review-ncohen.patch
> 
> Nathann


The patch `trac_8490_review-ncohen.patch` reintroduce the same bug as the current ticket is trying to solve. Hence, I think the patches are to be reviewed in this order again :

* trac_8490-square_free-vd.patch
* trac_8490_review-sl.patch

Sébastien



---

archive/issue_comments_076451.json:
```json
{
    "body": "Perfectly right !! sorryyyyyyyyyyy !!! :-)\n\nNathann",
    "created_at": "2010-05-13T14:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76451",
    "user": "https://github.com/nathanncohen"
}
```

Perfectly right !! sorryyyyyyyyyyy !!! :-)

Nathann



---

archive/issue_comments_076452.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-16T17:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76452",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076453.json:
```json
{
    "body": "Well, then short of this, which was my mistake, I noticed nothing wrong with these two patches ! :-)\n\nNathann",
    "created_at": "2010-05-16T17:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76453",
    "user": "https://github.com/nathanncohen"
}
```

Well, then short of this, which was my mistake, I noticed nothing wrong with these two patches ! :-)

Nathann



---

archive/issue_events_020393.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T22:30:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8490#event-20393"
}
```



---

archive/issue_comments_076454.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76454",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
