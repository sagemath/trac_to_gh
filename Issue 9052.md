# Issue 9052: Hasse invariant for elliptic curves

archive/issues_009052.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nKeywords: Hasse invariant\n\nCreates a method to compute the Hasse invariant of an elliptic curve over a function field of positive characteristic. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9052\n\n",
    "created_at": "2010-05-26T01:41:30Z",
    "labels": [
        "component: elliptic curves",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "Hasse invariant for elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9052",
    "user": "https://trac.sagemath.org/admin/accounts/users/voloch"
}
```
Assignee: @JohnCremona

Keywords: Hasse invariant

Creates a method to compute the Hasse invariant of an elliptic curve over a function field of positive characteristic. 

Issue created by migration from https://trac.sagemath.org/ticket/9052





---

archive/issue_comments_083696.json:
```json
{
    "body": "Attachment [trac_9052.patch](tarball://root/attachments/some-uuid/ticket9052/trac_9052.patch) by voloch created at 2010-05-26 01:54:21",
    "created_at": "2010-05-26T01:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9052#issuecomment-83696",
    "user": "https://trac.sagemath.org/admin/accounts/users/voloch"
}
```

Attachment [trac_9052.patch](tarball://root/attachments/some-uuid/ticket9052/trac_9052.patch) by voloch created at 2010-05-26 01:54:21



---

archive/issue_comments_083697.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-26T01:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9052#issuecomment-83697",
    "user": "https://trac.sagemath.org/admin/accounts/users/voloch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083698.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-26T02:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9052#issuecomment-83698",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083699.json:
```json
{
    "body": "Attachment [trac_9052_part2.patch](tarball://root/attachments/some-uuid/ticket9052/trac_9052_part2.patch) by @williamstein created at 2010-05-26 02:14:17\n\nLooks good to me.",
    "created_at": "2010-05-26T02:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9052#issuecomment-83699",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9052_part2.patch](tarball://root/attachments/some-uuid/ticket9052/trac_9052_part2.patch) by @williamstein created at 2010-05-26 02:14:17

Looks good to me.



---

archive/issue_comments_083700.json:
```json
{
    "body": "This is a coincidence, since just yesterday I was considering implementing functions is_supersingular() and is_ordinary().  Now this can be done very simply (since s.s. curves have invariant 0 and ordinary ones have nonzero invariant).\n\nHowever, I'm a little worried about the efficiency of the current implementation for even modest p, since it involves raising a degree 3 polynomial to the power (p-1)/2 and then picking out one coefficient.   There are easier ways to test supersingularity for small p, since one can precompute the s.s. j-invariants and check that.  This would be a quicker way of computing H when it is 0.  One could check that the j-invariant has degree at most 2 (else ordinary).  And over the prime field GF(p), s.s. curves have cardinality p+1, and another way to check ordinary-ness is to take random points and multiply then by p+1.  As a last resort one can compute the cardinality.\n\nI guess this is enough for a second ticket!",
    "created_at": "2010-05-26T08:35:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9052#issuecomment-83700",
    "user": "https://github.com/JohnCremona"
}
```

This is a coincidence, since just yesterday I was considering implementing functions is_supersingular() and is_ordinary().  Now this can be done very simply (since s.s. curves have invariant 0 and ordinary ones have nonzero invariant).

However, I'm a little worried about the efficiency of the current implementation for even modest p, since it involves raising a degree 3 polynomial to the power (p-1)/2 and then picking out one coefficient.   There are easier ways to test supersingularity for small p, since one can precompute the s.s. j-invariants and check that.  This would be a quicker way of computing H when it is 0.  One could check that the j-invariant has degree at most 2 (else ordinary).  And over the prime field GF(p), s.s. curves have cardinality p+1, and another way to check ordinary-ness is to take random points and multiply then by p+1.  As a last resort one can compute the cardinality.

I guess this is enough for a second ticket!



---

archive/issue_comments_083701.json:
```json
{
    "body": "Apply after both previous patches",
    "created_at": "2010-05-27T12:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9052#issuecomment-83701",
    "user": "https://github.com/JohnCremona"
}
```

Apply after both previous patches



---

archive/issue_comments_083702.json:
```json
{
    "body": "Attachment [trac_9053-reviewer.patch](tarball://root/attachments/some-uuid/ticket9052/trac_9053-reviewer.patch) by @JohnCremona created at 2010-05-27 12:37:59\n\nThe first two patches apply fine and tests pass.  I added a review patch which beefs up the docstring a little, adds some more examples (including one over a non-prime field), and also added one-liners for characteristics 5 and 7.\n\nStrictly this should be looked at again (William?), but I don't seem to have the option of marking it as \"needs review\" again.  In case you are wondering about the char. 5,7 cases, as well as doing the math I also systematically checked that this gives the same as the general method for *all* curves over GF(5) and GF(7)!",
    "created_at": "2010-05-27T12:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9052#issuecomment-83702",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_9053-reviewer.patch](tarball://root/attachments/some-uuid/ticket9052/trac_9053-reviewer.patch) by @JohnCremona created at 2010-05-27 12:37:59

The first two patches apply fine and tests pass.  I added a review patch which beefs up the docstring a little, adds some more examples (including one over a non-prime field), and also added one-liners for characteristics 5 and 7.

Strictly this should be looked at again (William?), but I don't seem to have the option of marking it as "needs review" again.  In case you are wondering about the char. 5,7 cases, as well as doing the math I also systematically checked that this gives the same as the general method for *all* curves over GF(5) and GF(7)!



---

archive/issue_comments_083703.json:
```json
{
    "body": "Looks even better to me now, by far!  Thanks John.",
    "created_at": "2010-05-28T19:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9052#issuecomment-83703",
    "user": "https://github.com/williamstein"
}
```

Looks even better to me now, by far!  Thanks John.



---

archive/issue_comments_083704.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-28T19:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9052#issuecomment-83704",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_009203.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-05-28T19:28:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9052#event-9203"
}
```



---

archive/issue_comments_083705.json:
```json
{
    "body": "Excellent.  I have nearly finished a patch which implements is_supersingular and is_ordinary (independently of computing the Hasse inv.)",
    "created_at": "2010-05-28T19:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9052#issuecomment-83705",
    "user": "https://github.com/JohnCremona"
}
```

Excellent.  I have nearly finished a patch which implements is_supersingular and is_ordinary (independently of computing the Hasse inv.)



---

archive/issue_comments_083706.json:
```json
{
    "body": "Replying to [comment:7 cremona]:\n> Excellent.  I have nearly finished a patch which implements is_supersingular and is_ordinary (independently of computing the Hasse inv.)\n\nSee #9087",
    "created_at": "2010-05-30T11:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9052#issuecomment-83706",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:7 cremona]:
> Excellent.  I have nearly finished a patch which implements is_supersingular and is_ordinary (independently of computing the Hasse inv.)

See #9087
