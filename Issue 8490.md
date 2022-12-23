# Issue 8490: Bad behavior of is_square_free for Words

archive/issues_008490.json:
```json
{
    "body": "Assignee: vdelecroix\n\nCC:  sage-combinat\n\nKeywords: word\n\nThe method is_square_free of sage.combinat.words.word.Word returns the wrong value in special case (including squares !)\n\n\n```\nsage: Word(\"aa\").is_square_free()  # the most funny\nTrue\nsage: Word(\"baa\").is_square_free()\nTrue\nsage: Word(\"cbaa\").is_square_free()\nTrue\nsage: Word(\"dcbaa\").is_square_free()\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8490\n\n",
    "created_at": "2010-03-10T16:38:46Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Bad behavior of is_square_free for Words",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8490",
    "user": "vdelecroix"
}
```
Assignee: vdelecroix

CC:  sage-combinat

Keywords: word

The method is_square_free of sage.combinat.words.word.Word returns the wrong value in special case (including squares !)


```
sage: Word("aa").is_square_free()  # the most funny
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

archive/issue_comments_076562.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T16:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76562",
    "user": "vdelecroix"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076563.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-10T17:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76563",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076564.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-03-10T17:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76564",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_076565.json:
```json
{
    "body": "Oups, intersection with #8429 which refactors the code of sage.combinat.words.\n\nI post soon a new patch that apply only after #8429 and I think it's better.",
    "created_at": "2010-03-10T17:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76565",
    "user": "vdelecroix"
}
```

Oups, intersection with #8429 which refactors the code of sage.combinat.words.

I post soon a new patch that apply only after #8429 and I think it's better.



---

archive/issue_comments_076566.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-10T17:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76566",
    "user": "vdelecroix"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076567.json:
```json
{
    "body": "another one-line correction that applies after #8429",
    "created_at": "2010-03-10T17:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76567",
    "user": "vdelecroix"
}
```

another one-line correction that applies after #8429



---

archive/issue_comments_076568.json:
```json
{
    "body": "Attachment\n\nanother one-line correction that applies after #8429",
    "created_at": "2010-03-10T17:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76568",
    "user": "vdelecroix"
}
```

Attachment

another one-line correction that applies after #8429



---

archive/issue_comments_076569.json:
```json
{
    "body": "Attachment\n\nApply only this",
    "created_at": "2010-03-10T22:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76569",
    "user": "vdelecroix"
}
```

Attachment

Apply only this



---

archive/issue_comments_076570.json:
```json
{
    "body": "Attachment\n\nThe same bug was occuring with `is_cube_free` :\n\n\n```\nsage: Word('111').is_cube_free()\nTrue\nsage: Word('2111').is_cube_free()\nTrue\nsage: Word('32111').is_cube_free()\nTrue\n```\n\n\nI just applied a patch which fixes this problem. I changed some doctests of both `is_square_free` and `is_cube_free`. I also removed a useless slice in the code of both functions and this gives good improvements in timings :\n\nBEFORE:\n\n\n```\nsage: t = words.ThueMorseWord()\nsage: %timeit t[:100].is_cube_free()\n5 loops, best of 3: 3.13 s per loop\n```\n\n\nAFTER:\n\n\n```\nsage: t = words.ThueMorseWord()\nsage: %timeit t[:100].is_cube_free()\n5 loops, best of 3: 1.18 s per loop\n```\n",
    "created_at": "2010-04-28T10:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76570",
    "user": "slabbe"
}
```

Attachment

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

archive/issue_comments_076571.json:
```json
{
    "body": "Applies over the precedent patch",
    "created_at": "2010-04-28T10:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76571",
    "user": "slabbe"
}
```

Applies over the precedent patch



---

archive/issue_comments_076572.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-28T10:21:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76572",
    "user": "slabbe"
}
```

Attachment



---

archive/issue_comments_076573.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-28T10:21:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76573",
    "user": "slabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076574.json:
```json
{
    "body": "Hello !! This patch is finem except for a small unimportant thing which bothered me :\n\n\n```\nfor end in xrange(start+3, L+1, 3): \n```\n\n\nWhy go up to L+1 when the last letter is L-1 ? The algorithm is still correct as \n\n\n```\nWord(\"abc\")[:50000]\n```\n\n\nraises no exception, but as there is no reason to.... So I give a positive review to the patches above, and trac_8490_review-ncohen.patch is left to be reviewed by anyone other than me (quoting Minh) :-)\n\nThank you for this patch !!\n\nNathann",
    "created_at": "2010-05-09T17:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76574",
    "user": "ncohen"
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

archive/issue_comments_076575.json:
```json
{
    "body": "The patches are to be applied in this order :\n\n* trac_8490-square_free-vd.patch\n* trac_8490_review-sl.patch\n* trac_8490_review-ncohen.patch\n\nNathann",
    "created_at": "2010-05-09T17:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76575",
    "user": "ncohen"
}
```

The patches are to be applied in this order :

* trac_8490-square_free-vd.patch
* trac_8490_review-sl.patch
* trac_8490_review-ncohen.patch

Nathann



---

archive/issue_comments_076576.json:
```json
{
    "body": "Replying to [comment:7 ncohen]:\n> Hello !! This patch is finem except for a small unimportant thing which bothered me :\n> \n> {{{\n> for end in xrange(start+3, L+1, 3): \n> }}}\n> \n> Why go up to L+1 when the last letter is L-1 ?\n\nFirst, xrange returns a left-closed and right-open interval. Hence, one needs to write something like `xrange(0,L+1)` if one wants to go up to `L` :\n\n\n```\nsage: list(xrange(0,5))\n[0, 1, 2, 3, 4]\n```\n\n\nSecond, the variable `end` is not used to get a specific item in self but for slicing self. Hence, if one wants to consider all the slicing possibilities, the variable `end` must take the last possible value `L`:\n\n\n```\nsage: list(xrange(0,5)) [2:5]   #is good\n[2, 3, 4]\nsage: list(xrange(0,5)) [2:4]   #forgets the last letter\n[2, 3]\n```\n\n\nHence, your patch is strange in the sense that doctests should not pass!\n\n> The algorithm is still correct as \n> \n> {{{\n> Word(\"abc\")[:50000]\n> }}}\n> \n> raises no exception, but as there is no reason to.... \n\nWe made the choice of following the Python behavior for slices that goes too far:\n\n\n```\nsage: L = range(10)\nsage: L\n[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\nsage: L[:100]\n[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n```\n\n\nS\u00e9bastien",
    "created_at": "2010-05-13T14:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76576",
    "user": "slabbe"
}
```

Replying to [comment:7 ncohen]:
> Hello !! This patch is finem except for a small unimportant thing which bothered me :
> 
> {{{
> for end in xrange(start+3, L+1, 3): 
> }}}
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
> {{{
> Word("abc")[:50000]
> }}}
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

archive/issue_comments_076577.json:
```json
{
    "body": "Replying to [comment:8 ncohen]:\n> The patches are to be applied in this order :\n> \n>   * trac_8490-square_free-vd.patch\n>   * trac_8490_review-sl.patch\n>   * trac_8490_review-ncohen.patch\n> \n> Nathann\n\nThe patch `trac_8490_review-ncohen.patch` reintroduce the same bug as the current ticket is trying to solve. Hence, I think the patches are to be reviewed in this order again :\n\n* trac_8490-square_free-vd.patch\n* trac_8490_review-sl.patch\n\nS\u00e9bastien",
    "created_at": "2010-05-13T14:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76577",
    "user": "slabbe"
}
```

Replying to [comment:8 ncohen]:
> The patches are to be applied in this order :
> 
>   * trac_8490-square_free-vd.patch
>   * trac_8490_review-sl.patch
>   * trac_8490_review-ncohen.patch
> 
> Nathann

The patch `trac_8490_review-ncohen.patch` reintroduce the same bug as the current ticket is trying to solve. Hence, I think the patches are to be reviewed in this order again :

* trac_8490-square_free-vd.patch
* trac_8490_review-sl.patch

Sébastien



---

archive/issue_comments_076578.json:
```json
{
    "body": "Perfectly right !! sorryyyyyyyyyyy !!! :-)\n\nNathann",
    "created_at": "2010-05-13T14:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76578",
    "user": "ncohen"
}
```

Perfectly right !! sorryyyyyyyyyyy !!! :-)

Nathann



---

archive/issue_comments_076579.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-16T17:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76579",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076580.json:
```json
{
    "body": "Well, then short of this, which was my mistake, I noticed nothing wrong with these two patches ! :-)\n\nNathann",
    "created_at": "2010-05-16T17:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76580",
    "user": "ncohen"
}
```

Well, then short of this, which was my mistake, I noticed nothing wrong with these two patches ! :-)

Nathann



---

archive/issue_comments_076581.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8490#issuecomment-76581",
    "user": "mhansen"
}
```

Resolution: fixed
