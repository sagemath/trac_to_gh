# Issue 7457: improvements to quotient_ring.py

archive/issues_007457.json:
```json
{
    "body": "Assignee: @aghitza\n\nThe attached patch makes a few improvements in `rings/quotient_ring.py`: implement `is_noetherian`, fix a todo in `cover_ring`, and minor docstring fixes.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7457\n\n",
    "created_at": "2009-11-14T12:29:00Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "improvements to quotient_ring.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7457",
    "user": "https://github.com/aghitza"
}
```
Assignee: @aghitza

The attached patch makes a few improvements in `rings/quotient_ring.py`: implement `is_noetherian`, fix a todo in `cover_ring`, and minor docstring fixes.


Issue created by migration from https://trac.sagemath.org/ticket/7457





---

archive/issue_comments_062689.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-14T12:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62689",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062690.json:
```json
{
    "body": "Can `self.cover_ring()` ever be non-Noetherian (with our current code)?\n\nOf course if you take an infinitely generated polynomial ring over a field and mod out by all of the polynomial generators, the quotient is Noetherian but the cover ring is not.  I don't know if that can come up in Sage now, and I also don't know how else we would easily tell whether the quotient ring is Noetherian...\n\nOtherwise, the patch looks good.",
    "created_at": "2009-11-19T22:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62690",
    "user": "https://github.com/jhpalmieri"
}
```

Can `self.cover_ring()` ever be non-Noetherian (with our current code)?

Of course if you take an infinitely generated polynomial ring over a field and mod out by all of the polynomial generators, the quotient is Noetherian but the cover ring is not.  I don't know if that can come up in Sage now, and I also don't know how else we would easily tell whether the quotient ring is Noetherian...

Otherwise, the patch looks good.



---

archive/issue_comments_062691.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-11-19T22:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62691",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_062692.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2009-11-22T10:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62692",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_062693.json:
```json
{
    "body": "That's a very good point, I should definitely fix this.  I'll have `is_noetherian` return True if `cover_ring` is Noetherian, and raise a `NotImplementedError` otherwise.\n\nI'm marking this as needs_work, and I'll try to get to it soon.",
    "created_at": "2009-11-22T10:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62693",
    "user": "https://github.com/aghitza"
}
```

That's a very good point, I should definitely fix this.  I'll have `is_noetherian` return True if `cover_ring` is Noetherian, and raise a `NotImplementedError` otherwise.

I'm marking this as needs_work, and I'll try to get to it soon.



---

archive/issue_comments_062694.json:
```json
{
    "body": "Alright, in the process of fixing this I added a few trivial methods to `InfinitePolynomialRing` and fixed a `NotImplementedError` being returned rather than raised in `ring.pyx`.",
    "created_at": "2009-11-22T11:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62694",
    "user": "https://github.com/aghitza"
}
```

Alright, in the process of fixing this I added a few trivial methods to `InfinitePolynomialRing` and fixed a `NotImplementedError` being returned rather than raised in `ring.pyx`.



---

archive/issue_comments_062695.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-22T11:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62695",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062696.json:
```json
{
    "body": "Attachment [trac_7457.patch](tarball://root/attachments/some-uuid/ticket7457/trac_7457.patch) by @aghitza created at 2009-11-22 11:26:15",
    "created_at": "2009-11-22T11:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62696",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_7457.patch](tarball://root/attachments/some-uuid/ticket7457/trac_7457.patch) by @aghitza created at 2009-11-22 11:26:15



---

archive/issue_comments_062697.json:
```json
{
    "body": "Two comments: this is not your fault, but can you fix lines 39-40 of quotient_ring.py?  Right now it says\n\n```\n    Creates a quotient ring of the ring `R` by the ideal `I`. Variables are \n    labeled by ``names``. (If the quotient ring is a quotient of a \n    polynomial ring.). If ``names`` isn't given, 'bar' will be appended to \n    the variable names in `R`. \n```\nand the parentheses and surrounding punctuation really bother me.  Should this say\n\n```\n    Creates a quotient ring of the ring `R` by the ideal `I`. Variables are \n    labeled by ``names`` (if the quotient ring is a quotient of a \n    polynomial ring). If ``names`` isn't given, 'bar' will be appended to \n    the variable names in `R`. \n```\n?  Or even remove the parentheses altogether?\n\nSecond and more importantly, I'm getting doctest failures in schemes/elliptic_curves:\n\n```\nThe following tests failed:\n\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 8 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 46 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/formal_group.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py # 3 doctests failed\n```\nThe problem seems to be the change to rings.pyx.  I don't know why you would ever want to `return` a `NotImplementedError` instead of raising it, but that change seems to be causing the problems.  So my suggestion is to get rid of that change, make sure doctests pass, and then perhaps open up a new ticket in which that issue is addressed.",
    "created_at": "2009-11-23T05:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62697",
    "user": "https://github.com/jhpalmieri"
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

archive/issue_comments_062698.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-23T05:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62698",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062699.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-26T15:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62699",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062700.json:
```json
{
    "body": "Here's a referee's patch to fix these two issues.  See #7532 for a follow-up.",
    "created_at": "2009-11-26T15:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62700",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a referee's patch to fix these two issues.  See #7532 for a follow-up.



---

archive/issue_comments_062701.json:
```json
{
    "body": "Attachment [trac_7457-ref.patch](tarball://root/attachments/some-uuid/ticket7457/trac_7457-ref.patch) by @jhpalmieri created at 2009-11-26 15:36:03\n\napply on top of the other patch",
    "created_at": "2009-11-26T15:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62701",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_7457-ref.patch](tarball://root/attachments/some-uuid/ticket7457/trac_7457-ref.patch) by @jhpalmieri created at 2009-11-26 15:36:03

apply on top of the other patch



---

archive/issue_comments_062702.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-26T15:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62702",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062703.json:
```json
{
    "body": "Wow, I look away for a couple of days and this is all done and fixed.  Thanks, John!",
    "created_at": "2009-11-26T22:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62703",
    "user": "https://github.com/aghitza"
}
```

Wow, I look away for a couple of days and this is all done and fixed.  Thanks, John!



---

archive/issue_comments_062704.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:33:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7457#issuecomment-62704",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017685.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-29T05:33:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7457",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7457#event-17685"
}
```
