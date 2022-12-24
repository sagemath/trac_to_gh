# Issue 5931: [with patch, needs review] Greatly speed up sage.combinat.symmetric_group_algebra.e

archive/issues_005931.json:
```json
{
    "body": "Assignee: mhansen\n\nThe old code essentially reimplemented the multiplication in the group algebra.  The new code accumulates the symmetrizers and antisymmetrizers separately, and then does one multiply at the end.  This probably results in the same number of operations, but it avoids creating many intermediate objects, so it is about 10x faster.\n\nAlso update docs for e and e_hat.\n\nTiming on 2.2 GHz Core2Duo running 32-bit Ubuntu 8.04 of\n\nfrom sage.combinat.symmetric_group_algebra import e\n\n\ntime dummy=e([[1,2,3,4],[5,6,7]])\n\nBefore patch:\n\nTime: CPU 3.38 s, Wall: 3.73 s\n\nAfter patch:\n\nTime: CPU 0.26 s, Wall: 0.40 s\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5931\n\n",
    "created_at": "2009-04-29T02:01:49Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, needs review] Greatly speed up sage.combinat.symmetric_group_algebra.e",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5931",
    "user": "jdc"
}
```
Assignee: mhansen

The old code essentially reimplemented the multiplication in the group algebra.  The new code accumulates the symmetrizers and antisymmetrizers separately, and then does one multiply at the end.  This probably results in the same number of operations, but it avoids creating many intermediate objects, so it is about 10x faster.

Also update docs for e and e_hat.

Timing on 2.2 GHz Core2Duo running 32-bit Ubuntu 8.04 of

from sage.combinat.symmetric_group_algebra import e


time dummy=e([[1,2,3,4],[5,6,7]])

Before patch:

Time: CPU 3.38 s, Wall: 3.73 s

After patch:

Time: CPU 0.26 s, Wall: 0.40 s


Issue created by migration from https://trac.sagemath.org/ticket/5931





---

archive/issue_comments_046907.json:
```json
{
    "body": "Attachment [e.patch](tarball://root/attachments/some-uuid/ticket5931/e.patch) by jdc created at 2009-04-29 02:02:13",
    "created_at": "2009-04-29T02:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5931#issuecomment-46907",
    "user": "jdc"
}
```

Attachment [e.patch](tarball://root/attachments/some-uuid/ticket5931/e.patch) by jdc created at 2009-04-29 02:02:13



---

archive/issue_comments_046908.json:
```json
{
    "body": "Attachment [doc.patch](tarball://root/attachments/some-uuid/ticket5931/doc.patch) by jdc created at 2009-04-29 16:08:46\n\nI think the main reason the old code was slow was that it multiplied GAP group elements in the inner loop, while the new code in e.patch uses the combinatorial algebra multiplication, which internally multiplies sage Permutations.  Another reason the old code was slower is that it looped over the GAP column_stabilizer group multiple times (probably requiring interaction with GAP) and re-computed v.sign() each time.  However, I did some tests where I avoid just these problems, and still the new code in e.patch is better, almost certainly because it avoids creating lots of intermediate elements of QSn.\n\nWe can avoid even more of the intermediate elements of QSn with dict.patch which I will attach below.  But it only speeds things up by about 2% in the test I ran, since the runtime is dominated by the antisym*sym multiplication.\n\nIf we are willing to assume that the entries in the tableau are distinct, I have another method which is 25% faster, but I don't think we want to make that assumption.  Just for the record, the point is that if the entries are distinct, then each of the products v*h is distinct, so we can easily construct a dictionary for the final result whose values are plus or minus 1.\n\nSummary: I recommend the new dict.patch (which includes the documentation change), but it would also be ok to use e.patch and doc.patch if that method is preferred.\n\nPS: Note that these patches seem to reverse the order of multiplication from h*v to v*h.  That's because of differing conventions between GAP group elements and permutations.\n\nPPS: My latest test case has been e([[1,2,3,4,5],[6,7,8],[9,10],[11]]), which takes forever with sage 3.4, but takes 20-30 seconds with the above patches.",
    "created_at": "2009-04-29T16:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5931#issuecomment-46908",
    "user": "jdc"
}
```

Attachment [doc.patch](tarball://root/attachments/some-uuid/ticket5931/doc.patch) by jdc created at 2009-04-29 16:08:46

I think the main reason the old code was slow was that it multiplied GAP group elements in the inner loop, while the new code in e.patch uses the combinatorial algebra multiplication, which internally multiplies sage Permutations.  Another reason the old code was slower is that it looped over the GAP column_stabilizer group multiple times (probably requiring interaction with GAP) and re-computed v.sign() each time.  However, I did some tests where I avoid just these problems, and still the new code in e.patch is better, almost certainly because it avoids creating lots of intermediate elements of QSn.

We can avoid even more of the intermediate elements of QSn with dict.patch which I will attach below.  But it only speeds things up by about 2% in the test I ran, since the runtime is dominated by the antisym*sym multiplication.

If we are willing to assume that the entries in the tableau are distinct, I have another method which is 25% faster, but I don't think we want to make that assumption.  Just for the record, the point is that if the entries are distinct, then each of the products v*h is distinct, so we can easily construct a dictionary for the final result whose values are plus or minus 1.

Summary: I recommend the new dict.patch (which includes the documentation change), but it would also be ok to use e.patch and doc.patch if that method is preferred.

PS: Note that these patches seem to reverse the order of multiplication from h*v to v*h.  That's because of differing conventions between GAP group elements and permutations.

PPS: My latest test case has been e([[1,2,3,4,5],[6,7,8],[9,10],[11]]), which takes forever with sage 3.4, but takes 20-30 seconds with the above patches.



---

archive/issue_comments_046909.json:
```json
{
    "body": "Replaces both e.patch and doc.patch; relative to 3.4",
    "created_at": "2009-04-29T16:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5931#issuecomment-46909",
    "user": "jdc"
}
```

Replaces both e.patch and doc.patch; relative to 3.4



---

archive/issue_comments_046910.json:
```json
{
    "body": "Attachment [dict.patch](tarball://root/attachments/some-uuid/ticket5931/dict.patch) by mabshoff created at 2009-04-30 07:12:06",
    "created_at": "2009-04-30T07:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5931#issuecomment-46910",
    "user": "mabshoff"
}
```

Attachment [dict.patch](tarball://root/attachments/some-uuid/ticket5931/dict.patch) by mabshoff created at 2009-04-30 07:12:06



---

archive/issue_comments_046911.json:
```json
{
    "body": "Looks good to me.  Thanks for this!\n\nMerged in 4.0.1.rc1.",
    "created_at": "2009-06-04T19:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5931#issuecomment-46911",
    "user": "mhansen"
}
```

Looks good to me.  Thanks for this!

Merged in 4.0.1.rc1.



---

archive/issue_comments_046912.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T19:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5931#issuecomment-46912",
    "user": "mhansen"
}
```

Resolution: fixed
