# Issue 2499: cython -- issues with cython-ing on the fly (fix one instance of lame code; also fix a bug)

archive/issues_002499.json:
```json
{
    "body": "Assignee: was\n\nThe attached patch (1) cleans up some ugly code, and (2) Fixes a bug that occurs on some NFS mounted filesystems.  \n\nThe (2) uses except: since I don't know the exact exception that occurs.  This could be fixed later.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2499\n\n",
    "created_at": "2008-03-12T16:25:55Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "cython -- issues with cython-ing on the fly (fix one instance of lame code; also fix a bug)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2499",
    "user": "was"
}
```
Assignee: was

The attached patch (1) cleans up some ugly code, and (2) Fixes a bug that occurs on some NFS mounted filesystems.  

The (2) uses except: since I don't know the exact exception that occurs.  This could be fixed later.

Issue created by migration from https://trac.sagemath.org/ticket/2499





---

archive/issue_comments_016940.json:
```json
{
    "body": "Attachment [sage-2499_cython.patch](tarball://root/attachments/some-uuid/ticket2499/sage-2499_cython.patch) by was created at 2008-03-12 16:26:40",
    "created_at": "2008-03-12T16:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16940",
    "user": "was"
}
```

Attachment [sage-2499_cython.patch](tarball://root/attachments/some-uuid/ticket2499/sage-2499_cython.patch) by was created at 2008-03-12 16:26:40



---

archive/issue_comments_016941.json:
```json
{
    "body": "The exception that occurs when trying to unlink .nfsXXX files is an OSError. I'm attaching a second (incremental) patch to change `except:` into `except OSError:` (and made sure it still fixes the problem).\n\nPositive review, in any case.",
    "created_at": "2008-03-14T16:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16941",
    "user": "wjp"
}
```

The exception that occurs when trying to unlink .nfsXXX files is an OSError. I'm attaching a second (incremental) patch to change `except:` into `except OSError:` (and made sure it still fixes the problem).

Positive review, in any case.



---

archive/issue_comments_016942.json:
```json
{
    "body": "Attachment [sage-2499_OSError.patch](tarball://root/attachments/some-uuid/ticket2499/sage-2499_OSError.patch) by wjp created at 2008-03-14 16:57:43",
    "created_at": "2008-03-14T16:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16942",
    "user": "wjp"
}
```

Attachment [sage-2499_OSError.patch](tarball://root/attachments/some-uuid/ticket2499/sage-2499_OSError.patch) by wjp created at 2008-03-14 16:57:43



---

archive/issue_comments_016943.json:
```json
{
    "body": "wjp's incremental patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-14T17:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16943",
    "user": "mabshoff"
}
```

wjp's incremental patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_016944.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T17:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16944",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016945.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T17:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16945",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
