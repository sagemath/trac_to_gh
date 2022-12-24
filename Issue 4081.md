# Issue 4081: [with patch, needs review] memleaks in nonlinear binary codes

archive/issues_004081.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4081\n\n",
    "created_at": "2008-09-09T01:17:00Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] memleaks in nonlinear binary codes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4081",
    "user": "@rlmill"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/4081





---

archive/issue_comments_029445.json:
```json
{
    "body": "Attachment [trac_4081-nonlinear-memleak.patch](tarball://root/attachments/some-uuid/ticket4081/trac_4081-nonlinear-memleak.patch) by @rlmill created at 2008-09-09 01:19:28\n\nShould fix this:\n\n```\n==5224== 728 bytes in 91 blocks are definitely lost in loss record 6,852 of 13,463\n==5224==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)\n==5224==    by 0x20BC8B55: __pyx_f_4sage_6groups_8perm_gps_9partn_ref_17refinement_binary_bitset_init (refinement_binary.c:1757)\n==5224==    by 0x20BCCF24: __pyx_pf_4sage_6groups_8perm_gps_9partn_ref_17refinement_binary_25NonlinearBinaryCodeStruct___new__ (refinement_binary.c:5642)\n==5224==    by 0x20BD9124: __pyx_tp_new_4sage_6groups_8perm_gps_9partn_ref_17refinement_binary_NonlinearBinaryCodeStruct (refinement_binary.c:11409)\n...\n```\n",
    "created_at": "2008-09-09T01:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4081#issuecomment-29445",
    "user": "@rlmill"
}
```

Attachment [trac_4081-nonlinear-memleak.patch](tarball://root/attachments/some-uuid/ticket4081/trac_4081-nonlinear-memleak.patch) by @rlmill created at 2008-09-09 01:19:28

Should fix this:

```
==5224== 728 bytes in 91 blocks are definitely lost in loss record 6,852 of 13,463
==5224==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==5224==    by 0x20BC8B55: __pyx_f_4sage_6groups_8perm_gps_9partn_ref_17refinement_binary_bitset_init (refinement_binary.c:1757)
==5224==    by 0x20BCCF24: __pyx_pf_4sage_6groups_8perm_gps_9partn_ref_17refinement_binary_25NonlinearBinaryCodeStruct___new__ (refinement_binary.c:5642)
==5224==    by 0x20BD9124: __pyx_tp_new_4sage_6groups_8perm_gps_9partn_ref_17refinement_binary_NonlinearBinaryCodeStruct (refinement_binary.c:11409)
...
```




---

archive/issue_comments_029446.json:
```json
{
    "body": "For valgrind logs after, see\n\nhttp://sage.math.washington.edu/home/rlmill/sage-memcheck.14554",
    "created_at": "2008-09-09T02:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4081#issuecomment-29446",
    "user": "@rlmill"
}
```

For valgrind logs after, see

http://sage.math.washington.edu/home/rlmill/sage-memcheck.14554



---

archive/issue_comments_029447.json:
```json
{
    "body": "Doctests pass and the valgrind log is clean. rlm and I also went over the patch in person. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T02:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4081#issuecomment-29447",
    "user": "mabshoff"
}
```

Doctests pass and the valgrind log is clean. rlm and I also went over the patch in person. Positive review.

Cheers,

Michael



---

archive/issue_comments_029448.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-09T02:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4081#issuecomment-29448",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029449.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-09T02:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4081#issuecomment-29449",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1
