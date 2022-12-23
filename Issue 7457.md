# Issue 7457: improvements to quotient_ring.py

archive/issues_007457.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThe attached patch makes a few improvements in `rings/quotient_ring.py`: implement `is_noetherian`, fix a todo in `cover_ring`, and minor docstring fixes.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7457\n\n",
    "created_at": "2009-11-14T12:29:00Z",
    "labels": [
        "algebra",
        "minor",
        "enhancement"
    ],
    "title": "improvements to quotient_ring.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7457",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

The attached patch makes a few improvements in `rings/quotient_ring.py`: implement `is_noetherian`, fix a todo in `cover_ring`, and minor docstring fixes.


Issue created by migration from https://trac.sagemath.org/ticket/7457





---

archive/issue_comments_062804.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-14T12:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62804",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062805.json:
```json
{
    "body": "Can `self.cover_ring()` ever be non-Noetherian (with our current code)?\n\nOf course if you take an infinitely generated polynomial ring over a field and mod out by all of the polynomial generators, the quotient is Noetherian but the cover ring is not.  I don't know if that can come up in Sage now, and I also don't know how else we would easily tell whether the quotient ring is Noetherian...\n\nOtherwise, the patch looks good.",
    "created_at": "2009-11-19T22:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62805",
    "user": "jhpalmieri"
}
```

Can `self.cover_ring()` ever be non-Noetherian (with our current code)?

Of course if you take an infinitely generated polynomial ring over a field and mod out by all of the polynomial generators, the quotient is Noetherian but the cover ring is not.  I don't know if that can come up in Sage now, and I also don't know how else we would easily tell whether the quotient ring is Noetherian...

Otherwise, the patch looks good.



---

archive/issue_comments_062806.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-11-19T22:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62806",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_062807.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2009-11-22T10:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62807",
    "user": "AlexGhitza"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_062808.json:
```json
{
    "body": "That's a very good point, I should definitely fix this.  I'll have `is_noetherian` return True if `cover_ring` is Noetherian, and raise a `NotImplementedError` otherwise.\n\nI'm marking this as needs_work, and I'll try to get to it soon.",
    "created_at": "2009-11-22T10:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62808",
    "user": "AlexGhitza"
}
```

That's a very good point, I should definitely fix this.  I'll have `is_noetherian` return True if `cover_ring` is Noetherian, and raise a `NotImplementedError` otherwise.

I'm marking this as needs_work, and I'll try to get to it soon.



---

archive/issue_comments_062809.json:
```json
{
    "body": "Alright, in the process of fixing this I added a few trivial methods to `InfinitePolynomialRing` and fixed a `NotImplementedError` being returned rather than raised in `ring.pyx`.",
    "created_at": "2009-11-22T11:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62809",
    "user": "AlexGhitza"
}
```

Alright, in the process of fixing this I added a few trivial methods to `InfinitePolynomialRing` and fixed a `NotImplementedError` being returned rather than raised in `ring.pyx`.



---

archive/issue_comments_062810.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-22T11:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62810",
    "user": "AlexGhitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062811.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-22T11:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62811",
    "user": "AlexGhitza"
}
```

Attachment



---

archive/issue_comments_062812.json:
```json
{
    "body": "Two comments: this is not your fault, but can you fix lines 39-40 of quotient_ring.py?  Right now it says\n\n```\n    Creates a quotient ring of the ring `R` by the ideal `I`. Variables are \n    labeled by ``names``. (If the quotient ring is a quotient of a \n    polynomial ring.). If ``names`` isn't given, 'bar' will be appended to \n    the variable names in `R`. \n```\n\nand the parentheses and surrounding punctuation really bother me.  Should this say\n\n```\n    Creates a quotient ring of the ring `R` by the ideal `I`. Variables are \n    labeled by ``names`` (if the quotient ring is a quotient of a \n    polynomial ring). If ``names`` isn't given, 'bar' will be appended to \n    the variable names in `R`. \n```\n\n?  Or even remove the parentheses altogether?\n\nSecond and more importantly, I'm getting doctest failures in schemes/elliptic_curves:\n\n```\nThe following tests failed:\n\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 8 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 46 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/formal_group.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py # 3 doctests failed\n```\n\nThe problem seems to be the change to rings.pyx.  I don't know why you would ever want to `return` a `NotImplementedError` instead of raising it, but that change seems to be causing the problems.  So my suggestion is to get rid of that change, make sure doctests pass, and then perhaps open up a new ticket in which that issue is addressed.",
    "created_at": "2009-11-23T05:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62812",
    "user": "jhpalmieri"
}
```

Two comments: this is not your fault, but can you fix lines 39-40 of quotient_ring.py?  Right now it says

```
    Creates a quotient ring of the ring `R` by the ideal `I`. Variables are 
    labeled by ``names``. (If the quotient ring is a quotient of a 
    polynomial ring.). If ``names`` isn't given, 'bar' will be appended to 
    the variable names in `R`. 
```

and the parentheses and surrounding punctuation really bother me.  Should this say

```
    Creates a quotient ring of the ring `R` by the ideal `I`. Variables are 
    labeled by ``names`` (if the quotient ring is a quotient of a 
    polynomial ring). If ``names`` isn't given, 'bar' will be appended to 
    the variable names in `R`. 
```

?  Or even remove the parentheses altogether?

Second and more importantly, I'm getting doctest failures in schemes/elliptic_curves:

```
The following tests failed:

	sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 8 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 46 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/formal_group.py # 1 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py # 3 doctests failed
```

The problem seems to be the change to rings.pyx.  I don't know why you would ever want to `return` a `NotImplementedError` instead of raising it, but that change seems to be causing the problems.  So my suggestion is to get rid of that change, make sure doctests pass, and then perhaps open up a new ticket in which that issue is addressed.



---

archive/issue_comments_062813.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-23T05:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62813",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062814.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-26T15:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62814",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062815.json:
```json
{
    "body": "Here's a referee's patch to fix these two issues.  See #7532 for a follow-up.",
    "created_at": "2009-11-26T15:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62815",
    "user": "jhpalmieri"
}
```

Here's a referee's patch to fix these two issues.  See #7532 for a follow-up.



---

archive/issue_comments_062816.json:
```json
{
    "body": "Attachment\n\napply on top of the other patch",
    "created_at": "2009-11-26T15:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62816",
    "user": "jhpalmieri"
}
```

Attachment

apply on top of the other patch



---

archive/issue_comments_062817.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-26T15:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62817",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062818.json:
```json
{
    "body": "Wow, I look away for a couple of days and this is all done and fixed.  Thanks, John!",
    "created_at": "2009-11-26T22:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62818",
    "user": "AlexGhitza"
}
```

Wow, I look away for a couple of days and this is all done and fixed.  Thanks, John!



---

archive/issue_comments_062819.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:33:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62819",
    "user": "mhansen"
}
```

Resolution: fixed
