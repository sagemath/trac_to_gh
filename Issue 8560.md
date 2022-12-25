# Issue 8560: magma interface should be changed to use sage-native-execute

archive/issues_008560.json:
```json
{
    "body": "Assignee: @williamstein\n\nLatest Magma v2.16-6 fails to load under Sage 4.3.3, with \n  the following error message: \n\n\nsage: magma_console() \n  dyld: Library not loaded: `@`executable_path/libgmp.3.dylib \n \u00a0  Referenced from: /Applications/Magma/bin/magma.exe \n \u00a0 Reason:  Incompatible library version: magma.exe requires version \n 9.0.0 or  later, but libgmp.3.dylib provides version 8.0.0 \n /usr/bin/magma:  line 72: 16880 Trace/BPT trap \u00a0 \u00a0 \u00a0 \u00a0 \u00a0\"${ROOT}/bin/ \n magma.exe\" $* \n\n\nThe reason of the failure is  that Sage defines the variable DYLD_LIBRARY_PATH when it executes  Magma. If you undefine it or define it to point to the right place,  then there is no problem\n\nThe solution is to use sage-native-execute in Magma interface.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8560\n\n",
    "closed_at": "2010-04-16T18:47:14Z",
    "created_at": "2010-03-19T09:14:06Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "magma interface should be changed to use sage-native-execute",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8560",
    "user": "https://github.com/kwankyu"
}
```
Assignee: @williamstein

Latest Magma v2.16-6 fails to load under Sage 4.3.3, with 
  the following error message: 


sage: magma_console() 
  dyld: Library not loaded: `@`executable_path/libgmp.3.dylib 
    Referenced from: /Applications/Magma/bin/magma.exe 
   Reason:  Incompatible library version: magma.exe requires version 
 9.0.0 or  later, but libgmp.3.dylib provides version 8.0.0 
 /usr/bin/magma:  line 72: 16880 Trace/BPT trap          "${ROOT}/bin/ 
 magma.exe" $* 


The reason of the failure is  that Sage defines the variable DYLD_LIBRARY_PATH when it executes  Magma. If you undefine it or define it to point to the right place,  then there is no problem

The solution is to use sage-native-execute in Magma interface.

Issue created by migration from https://trac.sagemath.org/ticket/8560





---

archive/issue_comments_077379.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-20T03:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8560#issuecomment-77379",
    "user": "https://github.com/kwankyu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077380.json:
```json
{
    "body": "Attachment [trac_8560.patch](tarball://root/attachments/some-uuid/ticket8560/trac_8560.patch) by @kwankyu created at 2010-03-20 03:38:05\n\nI implemented the simple solution.",
    "created_at": "2010-03-20T03:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8560#issuecomment-77380",
    "user": "https://github.com/kwankyu"
}
```

Attachment [trac_8560.patch](tarball://root/attachments/some-uuid/ticket8560/trac_8560.patch) by @kwankyu created at 2010-03-20 03:38:05

I implemented the simple solution.



---

archive/issue_comments_077381.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-01T00:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8560#issuecomment-77381",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8560#issuecomment-77382",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_020657.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T18:47:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8560",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8560#event-20657"
}
```



---

archive/issue_comments_077383.json:
```json
{
    "body": "Merged \"trac_8560.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8560#issuecomment-77383",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8560.patch" in 4.4.alpha0.
