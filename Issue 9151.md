# Issue 9151: build multithreaded version of ATLAS

archive/issues_009151.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jdemeyer\n\nKeywords: ATLAS BLAS LAPACK multi-threading pthreads\n\nHi,\n\nI noted that multi-threading in ATLAS is switched off by default (switch -t 0). I was wondering if it wouldn't be better to make a multi-threaded build the default, since it results in big performance increases on most modern computers.\n\nI attached a patch that enables threading. It works fine for me on a multi-core Linux machine. I tried to make it work for single-core machines (for which atlas might turn of threading automatically) by testing for the presence of the threaded version of the BLAS library before running the make command that builds the shared atlas library. However I haven't tested it on a single-core machine.\n\nKilian\n\nIssue created by migration from https://trac.sagemath.org/ticket/9151\n\n",
    "created_at": "2010-06-05T17:23:31Z",
    "labels": [
        "component: build"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "build multithreaded version of ATLAS",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9151",
    "user": "https://trac.sagemath.org/admin/accounts/users/kilian"
}
```
Assignee: GeorgSWeber

CC:  @jdemeyer

Keywords: ATLAS BLAS LAPACK multi-threading pthreads

Hi,

I noted that multi-threading in ATLAS is switched off by default (switch -t 0). I was wondering if it wouldn't be better to make a multi-threaded build the default, since it results in big performance increases on most modern computers.

I attached a patch that enables threading. It works fine for me on a multi-core Linux machine. I tried to make it work for single-core machines (for which atlas might turn of threading automatically) by testing for the presence of the threaded version of the BLAS library before running the make command that builds the shared atlas library. However I haven't tested it on a single-core machine.

Kilian

Issue created by migration from https://trac.sagemath.org/ticket/9151





---

archive/issue_comments_085297.json:
```json
{
    "body": "Attachment [atlas_pthread.patch](tarball://root/attachments/some-uuid/ticket9151/atlas_pthread.patch) by kilian created at 2010-06-05 17:25:08\n\nenables multi-threaded build in atlas-3.8.3.p12.spkg",
    "created_at": "2010-06-05T17:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9151#issuecomment-85297",
    "user": "https://trac.sagemath.org/admin/accounts/users/kilian"
}
```

Attachment [atlas_pthread.patch](tarball://root/attachments/some-uuid/ticket9151/atlas_pthread.patch) by kilian created at 2010-06-05 17:25:08

enables multi-threaded build in atlas-3.8.3.p12.spkg



---

archive/issue_comments_085298.json:
```json
{
    "body": "Hi,\n\nIt would be great if this patch would make it into the next release. I tested it on Linux 32bit and 64bit, single and multi core, Intel and AMD. On the 8 core machine, it increased the speed of e.g. a matrix dot product about 4-fold, and it didn't break the single-threaded build on the one-core machine. \n\nKilian",
    "created_at": "2010-06-08T16:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9151#issuecomment-85298",
    "user": "https://trac.sagemath.org/admin/accounts/users/kilian"
}
```

Hi,

It would be great if this patch would make it into the next release. I tested it on Linux 32bit and 64bit, single and multi core, Intel and AMD. On the 8 core machine, it increased the speed of e.g. a matrix dot product about 4-fold, and it didn't break the single-threaded build on the one-core machine. 

Kilian



---

archive/issue_comments_085299.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-04-05T15:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9151#issuecomment-85299",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085300.json:
```json
{
    "body": "Superseded by #10508.",
    "created_at": "2013-04-05T15:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9151#issuecomment-85300",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Superseded by #10508.



---

archive/issue_comments_085301.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-07T17:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9151#issuecomment-85301",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085302.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-04-10T08:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9151",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9151#issuecomment-85302",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
