# Issue 8789: Improve doctest coverage of modules/free_module_element.pyx

archive/issues_008789.json:
```json
{
    "body": "Assignee: tbd\n\nStarting score in sage-4.4:\n\n```\nfree_module_element.pyx: 47% (50 of 105)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8789\n\n",
    "created_at": "2010-04-28T04:16:47Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Improve doctest coverage of modules/free_module_element.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8789",
    "user": "was"
}
```
Assignee: tbd

Starting score in sage-4.4:

```
free_module_element.pyx: 47% (50 of 105)
```



Issue created by migration from https://trac.sagemath.org/ticket/8789





---

archive/issue_comments_080476.json:
```json
{
    "body": "Attachment [trac_8789.patch](tarball://root/attachments/some-uuid/ticket8789/trac_8789.patch) by was created at 2010-04-29 05:17:43",
    "created_at": "2010-04-29T05:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8789#issuecomment-80476",
    "user": "was"
}
```

Attachment [trac_8789.patch](tarball://root/attachments/some-uuid/ticket8789/trac_8789.patch) by was created at 2010-04-29 05:17:43



---

archive/issue_comments_080477.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-29T05:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8789#issuecomment-80477",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080478.json:
```json
{
    "body": "Attachment [trac_8789_part2.patch](tarball://root/attachments/some-uuid/ticket8789/trac_8789_part2.patch) by mhansen created at 2010-05-01 17:41:20\n\nLooks good to me.",
    "created_at": "2010-05-01T17:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8789#issuecomment-80478",
    "user": "mhansen"
}
```

Attachment [trac_8789_part2.patch](tarball://root/attachments/some-uuid/ticket8789/trac_8789_part2.patch) by mhansen created at 2010-05-01 17:41:20

Looks good to me.



---

archive/issue_comments_080479.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-01T17:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8789#issuecomment-80479",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080480.json:
```json
{
    "body": "Attachment [trac_8789_part2-rebased.patch](tarball://root/attachments/some-uuid/ticket8789/trac_8789_part2-rebased.patch) by mvngu created at 2010-05-08 03:44:58\n\nThe second patch doesn't apply when applied on top of the first one:\n\n\n```sh\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8789/trac_8789.patch && hg qpush \nadding trac_8789.patch to series file\napplying trac_8789.patch\nnow at: trac_8789.patch\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8789/trac_8789_part2.patch && hg qpush \nadding trac_8789_part2.patch to series file\napplying trac_8789_part2.patch\npatching file sage/modules/free_module_element.pyx\nHunk #1 FAILED at 439\nHunk #2 FAILED at 576\nHunk #3 FAILED at 2137\n3 out of 3 hunks FAILED -- saving rejects to file sage/modules/free_module_element.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8789_part2.patch\n```\n\n\nI have attached a rebase of the second patch.",
    "created_at": "2010-05-08T03:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8789#issuecomment-80480",
    "user": "mvngu"
}
```

Attachment [trac_8789_part2-rebased.patch](tarball://root/attachments/some-uuid/ticket8789/trac_8789_part2-rebased.patch) by mvngu created at 2010-05-08 03:44:58

The second patch doesn't apply when applied on top of the first one:


```sh
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8789/trac_8789.patch && hg qpush 
adding trac_8789.patch to series file
applying trac_8789.patch
now at: trac_8789.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8789/trac_8789_part2.patch && hg qpush 
adding trac_8789_part2.patch to series file
applying trac_8789_part2.patch
patching file sage/modules/free_module_element.pyx
Hunk #1 FAILED at 439
Hunk #2 FAILED at 576
Hunk #3 FAILED at 2137
3 out of 3 hunks FAILED -- saving rejects to file sage/modules/free_module_element.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8789_part2.patch
```


I have attached a rebase of the second patch.



---

archive/issue_comments_080481.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8789.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8789/trac_8789.patch)\n2. [trac_8789_part2-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8789/trac_8789_part2-rebased.patch)",
    "created_at": "2010-05-08T21:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8789#issuecomment-80481",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_8789.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8789/trac_8789.patch)
2. [trac_8789_part2-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8789/trac_8789_part2-rebased.patch)



---

archive/issue_comments_080482.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8789#issuecomment-80482",
    "user": "mvngu"
}
```

Resolution: fixed
