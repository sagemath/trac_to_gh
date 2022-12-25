# Issue 8100: running the notebook should not change the working directory

archive/issues_008100.json:
```json
{
    "body": "Assignee: @williamstein\n\nIn sage-4.3.2.alpha0 (and all earlier versions I can remember), running the notebook changes my working directory:\n\n```\nsage: pwd\n'/Users/palmieri'\nsage: notebook()\nThe notebook files are stored in: sage_notebook.sagenb\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:8000 *\n*                                                *\n**************************************************\n...\n^C\n...\nsage: pwd\n'/Users/palmieri/.sage'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8100\n\n",
    "created_at": "2010-01-27T23:45:50Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "running the notebook should not change the working directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8100",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @williamstein

In sage-4.3.2.alpha0 (and all earlier versions I can remember), running the notebook changes my working directory:

```
sage: pwd
'/Users/palmieri'
sage: notebook()
The notebook files are stored in: sage_notebook.sagenb
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
...
^C
...
sage: pwd
'/Users/palmieri/.sage'
```



Issue created by migration from https://trac.sagemath.org/ticket/8100





---

archive/issue_comments_070954.json:
```json
{
    "body": "Restore working directory when `notebook` returns.  sagenb repo.",
    "created_at": "2010-02-05T13:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8100#issuecomment-70954",
    "user": "https://github.com/qed777"
}
```

Restore working directory when `notebook` returns.  sagenb repo.



---

archive/issue_comments_070955.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-05T13:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8100#issuecomment-70955",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070956.json:
```json
{
    "body": "Attachment [trac_8100-run_notebook_cwd.patch](tarball://root/attachments/some-uuid/ticket8100/trac_8100-run_notebook_cwd.patch) by @qed777 created at 2010-02-05 13:17:25\n\nPatch attached.",
    "created_at": "2010-02-05T13:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8100#issuecomment-70956",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8100-run_notebook_cwd.patch](tarball://root/attachments/some-uuid/ticket8100/trac_8100-run_notebook_cwd.patch) by @qed777 created at 2010-02-05 13:17:25

Patch attached.



---

archive/issue_comments_070957.json:
```json
{
    "body": "Looks good to me; restores my working directory to whatever it was before running `notebook()`.",
    "created_at": "2010-02-05T15:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8100#issuecomment-70957",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me; restores my working directory to whatever it was before running `notebook()`.



---

archive/issue_comments_070958.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-05T15:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8100#issuecomment-70958",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070959.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-10T18:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8100#issuecomment-70959",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
