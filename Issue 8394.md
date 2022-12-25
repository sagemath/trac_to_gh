# Issue 8394: plot/plot3d/tri_plot.py is at 0% coverage: get it to 100%

archive/issues_008394.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  wcauchois boothby\n\nKeywords: doctests, coverage, plotting\n\nThe adaptive refinement code in tri_plot.py has almost no docstrings or tests.  However, there are a lot of helpful comments in the code, and the file is not very long, so it should be pretty easy to bring this up to 100% coverage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8394\n\n",
    "created_at": "2010-02-28T14:48:33Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "plot/plot3d/tri_plot.py is at 0% coverage: get it to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8394",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: @williamstein

CC:  wcauchois boothby

Keywords: doctests, coverage, plotting

The adaptive refinement code in tri_plot.py has almost no docstrings or tests.  However, there are a lot of helpful comments in the code, and the file is not very long, so it should be pretty easy to bring this up to 100% coverage.

Issue created by migration from https://trac.sagemath.org/ticket/8394





---

archive/issue_comments_075085.json:
```json
{
    "body": "adds basic doctests to tri_plot.py",
    "created_at": "2010-04-25T21:35:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8394#issuecomment-75085",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

adds basic doctests to tri_plot.py



---

archive/issue_comments_075086.json:
```json
{
    "body": "Attachment [trac_8394_v1.patch](tarball://root/attachments/some-uuid/ticket8394/trac_8394_v1.patch) by mhampton created at 2010-04-25 21:38:05",
    "created_at": "2010-04-25T21:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8394#issuecomment-75086",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_8394_v1.patch](tarball://root/attachments/some-uuid/ticket8394/trac_8394_v1.patch) by mhampton created at 2010-04-25 21:38:05



---

archive/issue_comments_075087.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-25T21:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8394#issuecomment-75087",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075088.json:
```json
{
    "body": "The patch formally gets coverage of tri_plot.py from 0 to 100%.  Since I still don't completely understand this module, the tests and descriptions could be better but this is an improvement.",
    "created_at": "2010-04-25T21:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8394#issuecomment-75088",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

The patch formally gets coverage of tri_plot.py from 0 to 100%.  Since I still don't completely understand this module, the tests and descriptions could be better but this is an improvement.



---

archive/issue_comments_075089.json:
```json
{
    "body": "Attachment [trac_8394-reviewer.patch](tarball://root/attachments/some-uuid/ticket8394/trac_8394-reviewer.patch) by mvngu created at 2010-04-28 13:36:24\n\nThe documentation is OK by me. I have just one trivial patch to add, which requires another pair of eyes other than mine. So if that reviewer patch gets a positive review, the whole ticket is good to go.\n\n\n\nWhen the module `plot/plot3d/tri_plot.py` is added to the reference manual, building the reference manual with that newly added module would result in some warnings. But fixing that is another ticket.",
    "created_at": "2010-04-28T13:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8394#issuecomment-75089",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8394-reviewer.patch](tarball://root/attachments/some-uuid/ticket8394/trac_8394-reviewer.patch) by mvngu created at 2010-04-28 13:36:24

The documentation is OK by me. I have just one trivial patch to add, which requires another pair of eyes other than mine. So if that reviewer patch gets a positive review, the whole ticket is good to go.



When the module `plot/plot3d/tri_plot.py` is added to the reference manual, building the reference manual with that newly added module would result in some warnings. But fixing that is another ticket.



---

archive/issue_comments_075090.json:
```json
{
    "body": "Looks great!  Thank you!",
    "created_at": "2010-04-28T16:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8394#issuecomment-75090",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Looks great!  Thank you!



---

archive/issue_comments_075091.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-28T16:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8394#issuecomment-75091",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075092.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8394#issuecomment-75092",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
