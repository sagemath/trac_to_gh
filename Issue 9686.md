# Issue 9686: Polish documentation for canonical label

archive/issues_009686.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9686\n\n",
    "created_at": "2010-08-04T13:38:38Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Polish documentation for canonical label",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9686",
    "user": "https://github.com/rlmill"
}
```
Assignee: jason, ncohen, rlm



Issue created by migration from https://trac.sagemath.org/ticket/9686





---

archive/issue_comments_094003.json:
```json
{
    "body": "Attachment [trac_9686.patch](tarball://root/attachments/some-uuid/ticket9686/trac_9686.patch) by @rlmill created at 2010-08-04 13:39:49",
    "created_at": "2010-08-04T13:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9686#issuecomment-94003",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9686.patch](tarball://root/attachments/some-uuid/ticket9686/trac_9686.patch) by @rlmill created at 2010-08-04 13:39:49



---

archive/issue_comments_094004.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-04T13:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9686#issuecomment-94004",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094005.json:
```json
{
    "body": "Attachment [trac_9686-reviewer.patch](tarball://root/attachments/some-uuid/ticket9686/trac_9686-reviewer.patch) by mvngu created at 2010-08-04 19:54:42",
    "created_at": "2010-08-04T19:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9686#issuecomment-94005",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_9686-reviewer.patch](tarball://root/attachments/some-uuid/ticket9686/trac_9686-reviewer.patch) by mvngu created at 2010-08-04 19:54:42



---

archive/issue_comments_094006.json:
```json
{
    "body": "With Sage 4.5.2.rc1 and the patch [attachment:trac_9686.patch], building the reference manual produces the following warning:\n\n```sh\n[mvngu@sage sage-4.5.2.rc1]$ ./sage -docbuild reference html\nsphinx-build -b html -d /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/output/doctrees/en/reference    /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/en/reference /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/output/html/en/reference\nRunning Sphinx v0.6.3\nloading pickled environment... done\nbuilding [html]: targets for 1 source files that are out of date\nupdating environment: 0 added, 1 changed, 0 removed\nreading sources... [100%] sage/graphs/generic_graph\n:0: (ERROR/3) Unexpected indentation.\nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... [100%] sage/graphs/generic_graph\nwriting additional files... genindex modindex search\ncopying static files... done\ndumping search index... done\ndumping object inventory... done\nbuild succeeded, 1 warning.\nBuild finished.  The built documents can be found in /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/output/html/en/reference\n```\n\nThis is due to how the added list are indented. The indentation of lists in the enclosing method, i.e. `canonical_label`, is inconsistent. Look at how the list of input is indented as compared with the list immediately following the first docstring line and the new list proposed by the patch [attachment:trac_9686.patch]. The reviewer patch [attachment:trac_9686-reviewer.patch] should restore some consistency in how lists in `canonical_label` are indented. The reviewer patch also resolves the above warning. \n\n\n\nI'm happy with the content of [attachment:trac_9686.patch]. We need someone other than me to look over [attachment:trac_9686-reviewer.patch].",
    "created_at": "2010-08-04T19:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9686#issuecomment-94006",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

With Sage 4.5.2.rc1 and the patch [attachment:trac_9686.patch], building the reference manual produces the following warning:

```sh
[mvngu@sage sage-4.5.2.rc1]$ ./sage -docbuild reference html
sphinx-build -b html -d /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/output/doctrees/en/reference    /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/en/reference /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/output/html/en/reference
Running Sphinx v0.6.3
loading pickled environment... done
building [html]: targets for 1 source files that are out of date
updating environment: 0 added, 1 changed, 0 removed
reading sources... [100%] sage/graphs/generic_graph
:0: (ERROR/3) Unexpected indentation.
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] sage/graphs/generic_graph
writing additional files... genindex modindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 1 warning.
Build finished.  The built documents can be found in /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/output/html/en/reference
```

This is due to how the added list are indented. The indentation of lists in the enclosing method, i.e. `canonical_label`, is inconsistent. Look at how the list of input is indented as compared with the list immediately following the first docstring line and the new list proposed by the patch [attachment:trac_9686.patch]. The reviewer patch [attachment:trac_9686-reviewer.patch] should restore some consistency in how lists in `canonical_label` are indented. The reviewer patch also resolves the above warning. 



I'm happy with the content of [attachment:trac_9686.patch]. We need someone other than me to look over [attachment:trac_9686-reviewer.patch].



---

archive/issue_comments_094007.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-08-04T22:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9686#issuecomment-94007",
    "user": "https://github.com/rlmill"
}
```

Looks good.



---

archive/issue_comments_094008.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-04T22:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9686#issuecomment-94008",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009818.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:47:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9686",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9686#event-9818"
}
```



---

archive/issue_comments_094009.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9686#issuecomment-94009",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
