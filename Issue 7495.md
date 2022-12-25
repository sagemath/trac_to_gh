# Issue 7495: notebook: get rid of all possible "internal server errors" when doing "Data --> Upload or attach file"

archive/issues_007495.json:
```json
{
    "body": "Assignee: boothby\n\nUploading or attaching an empty file or a file that doesn't exist, etc. can cause internal server errors instead of a proper error message.\n\nMoreover, notice these lines in twist.py:\n\n```\nclass Worksheet_do_upload_data\n...\n        dest = os.path.join(self.worksheet.data_directory(), name)\n        if os.path.exists(dest):\n            os.unlink(dest)\n```\n\n\nWith a properly crafted URL I bet name could contain .. and hence one could make the notebook *server* delete any file it has access to!  This is a critical security vulnerability. \n\nSee also #3849 for similar issues when uploading a worksheet. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7495\n\n",
    "created_at": "2009-11-20T00:34:35Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "notebook: get rid of all possible \"internal server errors\" when doing \"Data --> Upload or attach file\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7495",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

Uploading or attaching an empty file or a file that doesn't exist, etc. can cause internal server errors instead of a proper error message.

Moreover, notice these lines in twist.py:

```
class Worksheet_do_upload_data
...
        dest = os.path.join(self.worksheet.data_directory(), name)
        if os.path.exists(dest):
            os.unlink(dest)
```


With a properly crafted URL I bet name could contain .. and hence one could make the notebook *server* delete any file it has access to!  This is a critical security vulnerability. 

See also #3849 for similar issues when uploading a worksheet. 

Issue created by migration from https://trac.sagemath.org/ticket/7495





---

archive/issue_comments_063228.json:
```json
{
    "body": "Yes, this is fully exploitable and allows one to delete any file on the server:\nE.g., on my laptop I created a file tmp/xyz, then pasted in this url, and that file was deleted. \n\n\n```\nhttp://localhost:8000/home/admin/13/do_upload_data?urlField=%27%27&nameField=../../../../../../../../tmp/xyz\n```\n\n\nWith a little more work, one could not only delete any file, but I think *replace* it by a file of ones choice.  That's a pretty massive exploit.  \n\nSo I'm upping this to a blocker and fixing it now.",
    "created_at": "2009-11-20T01:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63228",
    "user": "https://github.com/williamstein"
}
```

Yes, this is fully exploitable and allows one to delete any file on the server:
E.g., on my laptop I created a file tmp/xyz, then pasted in this url, and that file was deleted. 


```
http://localhost:8000/home/admin/13/do_upload_data?urlField=%27%27&nameField=../../../../../../../../tmp/xyz
```


With a little more work, one could not only delete any file, but I think *replace* it by a file of ones choice.  That's a pretty massive exploit.  

So I'm upping this to a blocker and fixing it now.



---

archive/issue_comments_063229.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2009-11-20T01:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63229",
    "user": "https://github.com/williamstein"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_063230.json:
```json
{
    "body": "Can you do a quick grep through the source to see if any os.* functions are used in a like manner in the notebook?",
    "created_at": "2009-11-20T01:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63230",
    "user": "https://github.com/jasongrout"
}
```

Can you do a quick grep through the source to see if any os.* functions are used in a like manner in the notebook?



---

archive/issue_comments_063231.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-20T02:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63231",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063232.json:
```json
{
    "body": "Attachment [sagenb-7495.patch](tarball://root/attachments/some-uuid/ticket7495/sagenb-7495.patch) by @williamstein created at 2009-11-20 02:18:42",
    "created_at": "2009-11-20T02:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63232",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagenb-7495.patch](tarball://root/attachments/some-uuid/ticket7495/sagenb-7495.patch) by @williamstein created at 2009-11-20 02:18:42



---

archive/issue_comments_063233.json:
```json
{
    "body": "Creating a new file with name `&` raises an OSError.",
    "created_at": "2009-11-20T03:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63233",
    "user": "https://github.com/qed777"
}
```

Creating a new file with name `&` raises an OSError.



---

archive/issue_comments_063234.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Creating a new file with name `&` raises an OSError.\nActually, clicking to delete this file raises the error:\n\n```\n        exceptions.OSError: [Errno 21] Is a directory: '/home/apps/.sage/sage_notebook.sagenb/home/admin/88/data/'\n\n```\n",
    "created_at": "2009-11-20T03:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63234",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:4 mpatel]:
> Creating a new file with name `&` raises an OSError.
Actually, clicking to delete this file raises the error:

```
        exceptions.OSError: [Errno 21] Is a directory: '/home/apps/.sage/sage_notebook.sagenb/home/admin/88/data/'

```




---

archive/issue_comments_063235.json:
```json
{
    "body": "Attachment [sagenb-7495.2.patch](tarball://root/attachments/some-uuid/ticket7495/sagenb-7495.2.patch) by @qed777 created at 2009-11-20 05:56:10\n\nVersion 2.  Minor simplifications.  Apply only this patch to sagenb repo.",
    "created_at": "2009-11-20T05:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63235",
    "user": "https://github.com/qed777"
}
```

Attachment [sagenb-7495.2.patch](tarball://root/attachments/some-uuid/ticket7495/sagenb-7495.2.patch) by @qed777 created at 2009-11-20 05:56:10

Version 2.  Minor simplifications.  Apply only this patch to sagenb repo.



---

archive/issue_comments_063236.json:
```json
{
    "body": "I think the `OSError` above is a separate URI encoding problem.",
    "created_at": "2009-11-20T06:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63236",
    "user": "https://github.com/qed777"
}
```

I think the `OSError` above is a separate URI encoding problem.



---

archive/issue_comments_063237.json:
```json
{
    "body": "Anyway, my digression aside, my review is positive, as far as it goes.",
    "created_at": "2009-11-20T06:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63237",
    "user": "https://github.com/qed777"
}
```

Anyway, my digression aside, my review is positive, as far as it goes.



---

archive/issue_comments_063238.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n> I think the `OSError` above is a separate URI encoding problem.\nThis is now #7500.",
    "created_at": "2009-11-20T07:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63238",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:6 mpatel]:
> I think the `OSError` above is a separate URI encoding problem.
This is now #7500.



---

archive/issue_comments_063239.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-24T15:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63239",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063240.json:
```json
{
    "body": "\"Anyway, my digression aside, my review is positive, as far as it goes. \"  so positive review.",
    "created_at": "2009-11-24T15:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63240",
    "user": "https://github.com/williamstein"
}
```

"Anyway, my digression aside, my review is positive, as far as it goes. "  so positive review.



---

archive/issue_comments_063241.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-07T16:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63241",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_063242.json:
```json
{
    "body": "merged into sage-4.3",
    "created_at": "2009-12-07T16:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7495#issuecomment-63242",
    "user": "https://github.com/williamstein"
}
```

merged into sage-4.3
