# Issue 1323: [with patch, positive review] generate all subspaces of a vector space/projective space

archive/issues_001323.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @mwhansen\n\nFrom Chris Godsil's wishlist:\n\n```\n>>> Sometimes I want to construct graphs whose vertices are subspaces of a\n>>> vector space over a finite field. It could be useful to have a\n>>> generator for\n>>> the lines of the associated projective space, or even subspaces of a given\n>>> dimension.\n>> Is there an easy way to generate all of the subspaces of a vector space\n>> already in Sage, maybe restricted to a particular dimension, from the\n>> original vector space?\n> Maybe make a ticket for this?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1323\n\n",
    "closed_at": "2008-10-18T20:30:33Z",
    "created_at": "2007-11-28T20:18:47Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, positive review] generate all subspaces of a vector space/projective space",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1323",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

CC:  @mwhansen

From Chris Godsil's wishlist:

```
>>> Sometimes I want to construct graphs whose vertices are subspaces of a
>>> vector space over a finite field. It could be useful to have a
>>> generator for
>>> the lines of the associated projective space, or even subspaces of a given
>>> dimension.
>> Is there an easy way to generate all of the subspaces of a vector space
>> already in Sage, maybe restricted to a particular dimension, from the
>> original vector space?
> Maybe make a ticket for this?
```


Issue created by migration from https://trac.sagemath.org/ticket/1323





---

archive/issue_comments_008452.json:
```json
{
    "body": "Here is a method for iterating over dimension `k` subspaces of a space of dimension `n`:\n\nFirst, suppose that `F` is a finite field, and our ambient vector space is just `F^n`.\n\nAny subspace of dimension `k` is uniquely described as the rowspace of a `k x n` matrix in reduced row echelon form. This is determined by which columns are pivots, and what the entries of the remaining positions are. Thus it suffices to iterate over `k`-subsets of `[0..n-1]`, declaring those to be the pivots. Certain entries must be zero, according to row-reduced form, and the rest can be arbitrary elements of `F`.\n\nThus, for each `k`-subset of `[0..n-1]`, call it `[j_1, ..., j_k]`, construct a matrix with pivots as described by the `j_i`. For the `m` entries that are nonzero, construct a vector space of dimension `m`, and iterate over it, using the resulting tuples to fill in the matrix.\n\nVoila!\n\nI don't know about projective space, though.",
    "created_at": "2008-09-25T23:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1323#issuecomment-8452",
    "user": "https://github.com/rlmill"
}
```

Here is a method for iterating over dimension `k` subspaces of a space of dimension `n`:

First, suppose that `F` is a finite field, and our ambient vector space is just `F^n`.

Any subspace of dimension `k` is uniquely described as the rowspace of a `k x n` matrix in reduced row echelon form. This is determined by which columns are pivots, and what the entries of the remaining positions are. Thus it suffices to iterate over `k`-subsets of `[0..n-1]`, declaring those to be the pivots. Certain entries must be zero, according to row-reduced form, and the rest can be arbitrary elements of `F`.

Thus, for each `k`-subset of `[0..n-1]`, call it `[j_1, ..., j_k]`, construct a matrix with pivots as described by the `j_i`. For the `m` entries that are nonzero, construct a vector space of dimension `m`, and iterate over it, using the resulting tuples to fill in the matrix.

Voila!

I don't know about projective space, though.



---

archive/issue_comments_008453.json:
```json
{
    "body": "Oh wait, to get projective space, just shift the dimension by one, duh...",
    "created_at": "2008-09-25T23:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1323#issuecomment-8453",
    "user": "https://github.com/rlmill"
}
```

Oh wait, to get projective space, just shift the dimension by one, duh...



---

archive/issue_comments_008454.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-16T13:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1323#issuecomment-8454",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008455.json:
```json
{
    "body": "Changing assignee from @williamstein to @rlmill.",
    "created_at": "2008-10-16T13:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1323#issuecomment-8455",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from @williamstein to @rlmill.



---

archive/issue_comments_008456.json:
```json
{
    "body": "Attachment [trac_1323-subspaces.patch](tarball://root/attachments/some-uuid/ticket1323/trac_1323-subspaces.patch) by @rlmill created at 2008-10-17 13:40:21",
    "created_at": "2008-10-17T13:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1323#issuecomment-8456",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_1323-subspaces.patch](tarball://root/attachments/some-uuid/ticket1323/trac_1323-subspaces.patch) by @rlmill created at 2008-10-17 13:40:21



---

archive/issue_comments_008457.json:
```json
{
    "body": "Applies cleanly and passes sage -testall. Looks good. \nGAP has this very useful function and now Sage does. \nThanks Robert!",
    "created_at": "2008-10-17T17:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1323#issuecomment-8457",
    "user": "https://github.com/wdjoyner"
}
```

Applies cleanly and passes sage -testall. Looks good. 
GAP has this very useful function and now Sage does. 
Thanks Robert!



---

archive/issue_comments_008458.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T20:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1323#issuecomment-8458",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008459.json:
```json
{
    "body": "Merged in Sage 3.2.alpha0",
    "created_at": "2008-10-18T20:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1323#issuecomment-8459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha0



---

archive/issue_events_003456.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-18T20:30:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1323",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1323#event-3456"
}
```



---

archive/issue_events_003457.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-18T20:30:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1323",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1323#event-3457"
}
```
