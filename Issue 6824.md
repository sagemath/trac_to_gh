# Issue 6824: cdef in timeseries.pyx follows use of variable

archive/issues_006824.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein\n\n> During sage -upgrade (from a mirror)\n> \n> <snip>\n> python `which cython` --embed-positions --incref-local-binop -I/usr/local/src/sage-4.1/devel/sage-main -o sage/finance/time_series.c sage/finance/time_series.pyx\n> warning: /usr/local/src/sage-4.1/devel/sage-main/sage/finance/time_series.pyx:1722:24: cdef variable 'j' declared after it is used\n\n\n\nInteresting.  We have in that function:\n\n        `v = [(mn + j*step, mn + (j+1)*step) for j in range(bins)]`\n\nand then a few lines later:\n\n        `cdef Py_ssize_t j`\n\n\nThat's probably a bad idea.  The cdef line should be above that first line.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6824\n\n",
    "created_at": "2009-08-25T15:36:37Z",
    "labels": [
        "finance",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "cdef in timeseries.pyx follows use of variable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6824",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

CC:  @williamstein

> During sage -upgrade (from a mirror)
> 
> <snip>
> python `which cython` --embed-positions --incref-local-binop -I/usr/local/src/sage-4.1/devel/sage-main -o sage/finance/time_series.c sage/finance/time_series.pyx
> warning: /usr/local/src/sage-4.1/devel/sage-main/sage/finance/time_series.pyx:1722:24: cdef variable 'j' declared after it is used



Interesting.  We have in that function:

        `v = [(mn + j*step, mn + (j+1)*step) for j in range(bins)]`

and then a few lines later:

        `cdef Py_ssize_t j`


That's probably a bad idea.  The cdef line should be above that first line.


Issue created by migration from https://trac.sagemath.org/ticket/6824





---

archive/issue_comments_056280.json:
```json
{
    "body": "Attachment [trac_6824-cdef-in-timeseries.pyx](tarball://root/attachments/some-uuid/ticket6824/trac_6824-cdef-in-timeseries.pyx) by @jasongrout created at 2009-08-25 15:38:21",
    "created_at": "2009-08-25T15:38:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6824#issuecomment-56280",
    "user": "@jasongrout"
}
```

Attachment [trac_6824-cdef-in-timeseries.pyx](tarball://root/attachments/some-uuid/ticket6824/trac_6824-cdef-in-timeseries.pyx) by @jasongrout created at 2009-08-25 15:38:21



---

archive/issue_comments_056281.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-08-25T15:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6824#issuecomment-56281",
    "user": "@jasongrout"
}
```

Changing priority from major to minor.



---

archive/issue_comments_056282.json:
```json
{
    "body": "Jason: You should change the file extension to \".patch\" so the patch would display nicely within the browser.",
    "created_at": "2009-08-25T16:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6824#issuecomment-56282",
    "user": "mvngu"
}
```

Jason: You should change the file extension to ".patch" so the patch would display nicely within the browser.



---

archive/issue_comments_056283.json:
```json
{
    "body": "Attachment [trac_6824-cdef-in-timeseries.patch](tarball://root/attachments/some-uuid/ticket6824/trac_6824-cdef-in-timeseries.patch) by @jasongrout created at 2009-08-25 18:37:00\n\nsame as above, but with a \".patch\" extension",
    "created_at": "2009-08-25T18:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6824#issuecomment-56283",
    "user": "@jasongrout"
}
```

Attachment [trac_6824-cdef-in-timeseries.patch](tarball://root/attachments/some-uuid/ticket6824/trac_6824-cdef-in-timeseries.patch) by @jasongrout created at 2009-08-25 18:37:00

same as above, but with a ".patch" extension



---

archive/issue_comments_056284.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-09-26T04:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6824#issuecomment-56284",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_056285.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-26T05:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6824#issuecomment-56285",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056286.json:
```json
{
    "body": "Merged `trac_6824-cdef-in-timeseries.patch`.",
    "created_at": "2009-09-26T05:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6824#issuecomment-56286",
    "user": "mvngu"
}
```

Merged `trac_6824-cdef-in-timeseries.patch`.



---

archive/issue_comments_056287.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6824#issuecomment-56287",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
