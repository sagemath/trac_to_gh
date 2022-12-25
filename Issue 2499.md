# Issue 2499: cython -- issues with cython-ing on the fly (fix one instance of lame code; also fix a bug)

archive/issues_002499.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe attached patch (1) cleans up some ugly code, and (2) Fixes a bug that occurs on some NFS mounted filesystems.  \n\nThe (2) uses except: since I don't know the exact exception that occurs.  This could be fixed later.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2499\n\n",
    "created_at": "2008-03-12T16:25:55Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "cython -- issues with cython-ing on the fly (fix one instance of lame code; also fix a bug)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2499",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

The attached patch (1) cleans up some ugly code, and (2) Fixes a bug that occurs on some NFS mounted filesystems.  

The (2) uses except: since I don't know the exact exception that occurs.  This could be fixed later.

Issue created by migration from https://trac.sagemath.org/ticket/2499





---

archive/issue_comments_016904.json:
```json
{
    "body": "Attachment [sage-2499_cython.patch](tarball://root/attachments/some-uuid/ticket2499/sage-2499_cython.patch) by @williamstein created at 2008-03-12 16:26:40",
    "created_at": "2008-03-12T16:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16904",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2499_cython.patch](tarball://root/attachments/some-uuid/ticket2499/sage-2499_cython.patch) by @williamstein created at 2008-03-12 16:26:40



---

archive/issue_comments_016905.json:
```json
{
    "body": "The exception that occurs when trying to unlink .nfsXXX files is an OSError. I'm attaching a second (incremental) patch to change `except:` into `except OSError:` (and made sure it still fixes the problem).\n\nPositive review, in any case.",
    "created_at": "2008-03-14T16:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16905",
    "user": "https://github.com/wjp"
}
```

The exception that occurs when trying to unlink .nfsXXX files is an OSError. I'm attaching a second (incremental) patch to change `except:` into `except OSError:` (and made sure it still fixes the problem).

Positive review, in any case.



---

archive/issue_comments_016906.json:
```json
{
    "body": "Attachment [sage-2499_OSError.patch](tarball://root/attachments/some-uuid/ticket2499/sage-2499_OSError.patch) by @wjp created at 2008-03-14 16:57:43",
    "created_at": "2008-03-14T16:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16906",
    "user": "https://github.com/wjp"
}
```

Attachment [sage-2499_OSError.patch](tarball://root/attachments/some-uuid/ticket2499/sage-2499_OSError.patch) by @wjp created at 2008-03-14 16:57:43



---

archive/issue_comments_016907.json:
```json
{
    "body": "wjp's incremental patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-14T17:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16907",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

wjp's incremental patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_016908.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T17:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16908",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005881.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-14T17:13:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2499#event-5881"
}
```



---

archive/issue_comments_016909.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T17:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2499#issuecomment-16909",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
