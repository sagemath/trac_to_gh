# Issue 9437: special linear group over finite rings

archive/issues_009437.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @videlec\n\nKeywords: group, matrix, special linear\n\nSage is not able to work with special linear group over finite rings (for example iterate over its element). As in the following example, the constructor accept the argument Zmod(4). But the object is not able to do anything due to call to finite field in gap. Curiously, list(G) and G.list() does not raise the same error (but both of them do).\n\n\n```\nsage: G = SL(2, Zmod(4))\nsage: print G\nsage: list(G)\nTypeError                                 Traceback (most recent call last)\n...\nTypeError: variable names have not yet been set using self._assign_names(...)\nerror coercing to finite field\nsage: G.list()\nNameError                                 Traceback (most recent call last)\nNameError: name 'ZmodnZObj' is not defined\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9437\n\n",
    "created_at": "2010-07-06T15:24:59Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "special linear group over finite rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9437",
    "user": "https://github.com/videlec"
}
```
Assignee: @aghitza

CC:  @videlec

Keywords: group, matrix, special linear

Sage is not able to work with special linear group over finite rings (for example iterate over its element). As in the following example, the constructor accept the argument Zmod(4). But the object is not able to do anything due to call to finite field in gap. Curiously, list(G) and G.list() does not raise the same error (but both of them do).


```
sage: G = SL(2, Zmod(4))
sage: print G
sage: list(G)
TypeError                                 Traceback (most recent call last)
...
TypeError: variable names have not yet been set using self._assign_names(...)
error coercing to finite field
sage: G.list()
NameError                                 Traceback (most recent call last)
NameError: name 'ZmodnZObj' is not defined
```


Issue created by migration from https://trac.sagemath.org/ticket/9437





---

archive/issue_comments_090192.json:
```json
{
    "body": "Attachment [trac_9437_matrix_group_finite_ring.patch](tarball://root/attachments/some-uuid/ticket9437/trac_9437_matrix_group_finite_ring.patch) by @loefflerd created at 2010-09-23 13:28:21\n\npatch against 4.6.alpha1",
    "created_at": "2010-09-23T13:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90192",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_9437_matrix_group_finite_ring.patch](tarball://root/attachments/some-uuid/ticket9437/trac_9437_matrix_group_finite_ring.patch) by @loefflerd created at 2010-09-23 13:28:21

patch against 4.6.alpha1



---

archive/issue_comments_090193.json:
```json
{
    "body": "For a matrix group G, the two commands `list(G)` and `G.list()` are totally different implementations; the former uses Gap to calculate the generators of G, and does the rest in Sage, while the latter just asks Gap for the list. The former works since #8970. The patch above fixes the latter, and adds doctests to prove that they both work.\n\nIt is, of course, really dumb that we have two independent implementations, but that's a job for another ticket.",
    "created_at": "2010-09-23T13:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90193",
    "user": "https://github.com/loefflerd"
}
```

For a matrix group G, the two commands `list(G)` and `G.list()` are totally different implementations; the former uses Gap to calculate the generators of G, and does the rest in Sage, while the latter just asks Gap for the list. The former works since #8970. The patch above fixes the latter, and adds doctests to prove that they both work.

It is, of course, really dumb that we have two independent implementations, but that's a job for another ticket.



---

archive/issue_comments_090194.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-23T13:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90194",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090195.json:
```json
{
    "body": "With 4.6.rc0 the patch applies and works fine.  But look at these timings:\n\n```\nsage: G = SL(2, Zmod(4))\nsage: time a = list(G)  \nCPU times: user 0.05 s, sys: 0.01 s, total: 0.06 s\nWall time: 1.69 s\nsage: time b = G.list() \nCPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s\nWall time: 20.60 s\n```\n\n\nI'm not letting that stop me giving the patch a positive review, but it suggest that the list() method should be calling whatever the other one uses!\n\nTesting the directory matrix_gps, the file which this patch changes now takes a very long time:\n\n```\nsage -t  \"sage/groups/matrix_gps/matrix_group.py\"           \n\t [263.9 s]\n```\n\nwhereas without the patch:\n\n```\n[240.1s]\n```\n\nIs the extra time just the time of the new doctest (if so, mark it #long time), or are some other doctests now slower?",
    "created_at": "2010-10-28T19:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90195",
    "user": "https://github.com/JohnCremona"
}
```

With 4.6.rc0 the patch applies and works fine.  But look at these timings:

```
sage: G = SL(2, Zmod(4))
sage: time a = list(G)  
CPU times: user 0.05 s, sys: 0.01 s, total: 0.06 s
Wall time: 1.69 s
sage: time b = G.list() 
CPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s
Wall time: 20.60 s
```


I'm not letting that stop me giving the patch a positive review, but it suggest that the list() method should be calling whatever the other one uses!

Testing the directory matrix_gps, the file which this patch changes now takes a very long time:

```
sage -t  "sage/groups/matrix_gps/matrix_group.py"           
	 [263.9 s]
```

whereas without the patch:

```
[240.1s]
```

Is the extra time just the time of the new doctest (if so, mark it #long time), or are some other doctests now slower?



---

archive/issue_comments_090196.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-10-28T19:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90196",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_090197.json:
```json
{
    "body": "I just remembered this ticket, which I'd forgotten about completely...\n\nCan I propose that we have another ticket for dealing with the discrepancy between the two \"list\" methods? It's somewhat independent of the problem with non-finite-field base rings -- even if `G = SL(3, 17)` then `G.list()` and `list(G)` are using completely independent implementations -- so it's a preexisting problem. Hence I'm putting this back to \"needs review\".",
    "created_at": "2011-01-23T10:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90197",
    "user": "https://github.com/loefflerd"
}
```

I just remembered this ticket, which I'd forgotten about completely...

Can I propose that we have another ticket for dealing with the discrepancy between the two "list" methods? It's somewhat independent of the problem with non-finite-field base rings -- even if `G = SL(3, 17)` then `G.list()` and `list(G)` are using completely independent implementations -- so it's a preexisting problem. Hence I'm putting this back to "needs review".



---

archive/issue_comments_090198.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-01-23T10:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90198",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_090199.json:
```json
{
    "body": "In fact there is already a ticket for the discrepancy of the \"list\" methods: #8588.",
    "created_at": "2011-01-24T09:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90199",
    "user": "https://github.com/loefflerd"
}
```

In fact there is already a ticket for the discrepancy of the "list" methods: #8588.



---

archive/issue_comments_090200.json:
```json
{
    "body": "I've done a test and the before/after timings for testing `matrix_group.py` (on selmer.warwick.ac.uk using 4.6.2.alpha1) are 25.9 s and 27.0 s. I think that's acceptable without flagging anything as #long.",
    "created_at": "2011-01-24T09:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90200",
    "user": "https://github.com/loefflerd"
}
```

I've done a test and the before/after timings for testing `matrix_group.py` (on selmer.warwick.ac.uk using 4.6.2.alpha1) are 25.9 s and 27.0 s. I think that's acceptable without flagging anything as #long.



---

archive/issue_comments_090201.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-24T14:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90201",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090202.json:
```json
{
    "body": "OK, and I checked that it still works fine with 4.6.2.alpha1.",
    "created_at": "2011-01-24T14:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90202",
    "user": "https://github.com/JohnCremona"
}
```

OK, and I checked that it still works fine with 4.6.2.alpha1.



---

archive/issue_comments_090203.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-27T14:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90203",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_090204.json:
```json
{
    "body": "This patch conflicts with #10515.  So could you please rebase this patch so that it applies on top of #10515?",
    "created_at": "2011-01-27T14:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90204",
    "user": "https://github.com/jdemeyer"
}
```

This patch conflicts with #10515.  So could you please rebase this patch so that it applies on top of #10515?



---

archive/issue_comments_090205.json:
```json
{
    "body": "rebased version",
    "created_at": "2011-01-27T15:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90205",
    "user": "https://github.com/loefflerd"
}
```

rebased version



---

archive/issue_comments_090206.json:
```json
{
    "body": "Attachment [trac_9437_matrix_group_finite_ring-rebase.patch](tarball://root/attachments/some-uuid/ticket9437/trac_9437_matrix_group_finite_ring-rebase.patch) by @loefflerd created at 2011-01-27 15:24:04\n\nDone. There's no change in the actual code of the patch, just variable names and diff context, so I'm reinstating the positive review.",
    "created_at": "2011-01-27T15:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90206",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_9437_matrix_group_finite_ring-rebase.patch](tarball://root/attachments/some-uuid/ticket9437/trac_9437_matrix_group_finite_ring-rebase.patch) by @loefflerd created at 2011-01-27 15:24:04

Done. There's no change in the actual code of the patch, just variable names and diff context, so I'm reinstating the positive review.



---

archive/issue_comments_090207.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-27T15:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90207",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_090208.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-28T08:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9437#issuecomment-90208",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
