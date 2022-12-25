# Issue 4610: [with patch, positive review] "sage -tp X": Move certain long doctests to the start of the list of files to test

archive/issues_004610.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nThere are various doctests in Sage that take a while, chief among those is\n\n```\nsage -t -long devel/sage/sage/crypto/mq/sr.py\n [630.4 s]\n```\nWhen running -tp with a high number of parallel threads those tests end up running at the end and making the user wait a while until that test finishes:\n\n```\nTotal time for all tests: 1287.6 seconds\n```\nMoving this and a couple other files to the beginning of the list to doctest in local/bin/sage-ptest would likely result in a more even utilization of the cores. This also annoys me personally since I run -tp 8 -long after each patch merged in sage.math and it would shave probably 4 minutes off the total time of each run.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4610\n\n",
    "closed_at": "2008-12-05T06:36:21Z",
    "created_at": "2008-11-25T01:06:11Z",
    "labels": [
        "component: doctest coverage",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch, positive review] \"sage -tp X\": Move certain long doctests to the start of the list of files to test",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4610",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @garyfurnish

There are various doctests in Sage that take a while, chief among those is

```
sage -t -long devel/sage/sage/crypto/mq/sr.py
 [630.4 s]
```
When running -tp with a high number of parallel threads those tests end up running at the end and making the user wait a while until that test finishes:

```
Total time for all tests: 1287.6 seconds
```
Moving this and a couple other files to the beginning of the list to doctest in local/bin/sage-ptest would likely result in a more even utilization of the cores. This also annoys me personally since I run -tp 8 -long after each patch merged in sage.math and it would shave probably 4 minutes off the total time of each run.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4610





---

archive/issue_comments_034531.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-25T01:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4610#issuecomment-34531",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034532.json:
```json
{
    "body": "The following doctest take more than 100 seconds on sage.math with the current 3.2.1.a2:\n\n```\ndevel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\ndevel/sage/sage/rings/qqbar.py\ndevel/sage/sage/schemes/elliptic_curves/sha_tate.py\ndevel/sage/sage/functions/piecewise.py\ndevel/sage/sage/graphs/graph_generators.py\ndevel/sage/sage/groups/perm_gps/partn_ref/refinement_binary.pyx\ndevel/sage/sage/groups/matrix_gps/matrix_group.py\ndevel/sage/sage/graphs/graph.py\ndevel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx\ndevel/sage/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx\ndevel/sage/sage/combinat/root_system/weyl_characters.py\ndevel/sage/sage/combinat/root_system/weyl_characters.py\ndevel/sage/sage/calculus/calculus.py\ndevel/sage/sage/crypto/mq/sr.py\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T02:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4610#issuecomment-34532",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The following doctest take more than 100 seconds on sage.math with the current 3.2.1.a2:

```
devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
devel/sage/sage/rings/qqbar.py
devel/sage/sage/schemes/elliptic_curves/sha_tate.py
devel/sage/sage/functions/piecewise.py
devel/sage/sage/graphs/graph_generators.py
devel/sage/sage/groups/perm_gps/partn_ref/refinement_binary.pyx
devel/sage/sage/groups/matrix_gps/matrix_group.py
devel/sage/sage/graphs/graph.py
devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx
devel/sage/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx
devel/sage/sage/combinat/root_system/weyl_characters.py
devel/sage/sage/combinat/root_system/weyl_characters.py
devel/sage/sage/calculus/calculus.py
devel/sage/sage/crypto/mq/sr.py
```

Cheers,

Michael



---

archive/issue_comments_034533.json:
```json
{
    "body": "Attachment [trac_4610_bin.patch](tarball://root/attachments/some-uuid/ticket4610/trac_4610_bin.patch) by @garyfurnish created at 2008-12-05 04:06:42",
    "created_at": "2008-12-05T04:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4610#issuecomment-34533",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_4610_bin.patch](tarball://root/attachments/some-uuid/ticket4610/trac_4610_bin.patch) by @garyfurnish created at 2008-12-05 04:06:42



---

archive/issue_comments_034534.json:
```json
{
    "body": "Changing assignee from mabshoff to @garyfurnish.",
    "created_at": "2008-12-05T04:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4610#issuecomment-34534",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from mabshoff to @garyfurnish.



---

archive/issue_comments_034535.json:
```json
{
    "body": "This patch autotracks timing of files so that they test in the right order.",
    "created_at": "2008-12-05T04:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4610#issuecomment-34535",
    "user": "https://github.com/garyfurnish"
}
```

This patch autotracks timing of files so that they test in the right order.



---

archive/issue_comments_034536.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-12-05T04:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4610#issuecomment-34536",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from assigned to new.



---

archive/issue_comments_034537.json:
```json
{
    "body": "Nice work, positive review. I am adding some tiny additional print statements to keep the user informed.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T05:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4610#issuecomment-34537",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice work, positive review. I am adding some tiny additional print statements to keep the user informed.

Cheers,

Michael



---

archive/issue_events_010478.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-05T06:36:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4610",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4610#event-10478"
}
```



---

archive/issue_comments_034538.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-05T06:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4610#issuecomment-34538",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha0



---

archive/issue_comments_034539.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-05T06:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4610#issuecomment-34539",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
