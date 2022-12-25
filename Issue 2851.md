# Issue 2851: clean binary install of sage followed by "sage -br" is broken

archive/issues_002851.json:
```json
{
    "body": "Assignee: mabshoff\n\nGet any binary of sage, type \"sage -br\", and it is broken.\nThe workaround is to touch any pyx file.  This should have been fixed but hasn't, and is a _major_ problem.  This *must* be fixed for 3.0. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2851\n\n",
    "created_at": "2008-04-07T22:36:34Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "clean binary install of sage followed by \"sage -br\" is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2851",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

Get any binary of sage, type "sage -br", and it is broken.
The workaround is to touch any pyx file.  This should have been fixed but hasn't, and is a _major_ problem.  This *must* be fixed for 3.0. 

Issue created by migration from https://trac.sagemath.org/ticket/2851





---

archive/issue_comments_019521.json:
```json
{
    "body": "This is caused by the sage directory is symlink fix from a while back. We need to invalidate the cache when files are moved.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T22:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19521",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is caused by the sage directory is symlink fix from a while back. We need to invalidate the cache when files are moved.

Cheers,

Michael



---

archive/issue_comments_019522.json:
```json
{
    "body": "Attachment [sage-2851.patch](tarball://root/attachments/some-uuid/ticket2851/sage-2851.patch) by @williamstein created at 2008-04-15 00:44:16",
    "created_at": "2008-04-15T00:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19522",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2851.patch](tarball://root/attachments/some-uuid/ticket2851/sage-2851.patch) by @williamstein created at 2008-04-15 00:44:16



---

archive/issue_comments_019523.json:
```json
{
    "body": "Patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T01:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19523",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_019524.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-15T01:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19524",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha5



---

archive/issue_events_003041.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-15T01:00:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2851#event-3041"
}
```



---

archive/issue_comments_019525.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T01:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19525",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019526.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-04-15T16:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19526",
    "user": "https://github.com/yqiang"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_019527.json:
```json
{
    "body": "This still doesn't seem to be fixed. I just untared the sage-3.0.alpha5 binary from mabshoff's home directory and did a ./sage -br and got the following:\n\n...\ncopying sage/dsage/dist_functions/tests/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/dist_functions/tests\ncreating build/lib.linux-x86_64-2.5/sage/dsage/misc\ncopying sage/dsage/misc/countrefs.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc\ncopying sage/dsage/misc/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc\ncopying sage/dsage/misc/misc.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc\ncopying sage/dsage/misc/constants.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc\ncopying sage/dsage/misc/hostinfo.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc\ncopying sage/dsage/misc/config.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc\ncopying sage/dsage/misc/nodoctest.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc\ncreating build/lib.linux-x86_64-2.5/sage/dsage/misc/tests\ncopying sage/dsage/misc/tests/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc/tests\ncreating build/lib.linux-x86_64-2.5/sage/dsage/web\ncopying sage/dsage/web/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/web\ncopying sage/dsage/web/web_server.py -> build/lib.linux-x86_64-2.5/sage/dsage/web\ncreating build/lib.linux-x86_64-2.5/sage/dsage/scripts\ncopying sage/dsage/scripts/dsage_worker.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts\ncopying sage/dsage/scripts/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts\ncopying sage/dsage/scripts/dsage_setup.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts\ncopying sage/dsage/scripts/nodoctest.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts\nrunning build_ext\nbuilding 'sage.modules.free_module_element' extension\nerror: unknown file type '.pyx' (from 'sage/modules/free_module_element.pyx')\nsage: There was an error installing modified sage library code.",
    "created_at": "2008-04-15T16:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19527",
    "user": "https://github.com/yqiang"
}
```

This still doesn't seem to be fixed. I just untared the sage-3.0.alpha5 binary from mabshoff's home directory and did a ./sage -br and got the following:

...
copying sage/dsage/dist_functions/tests/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/dist_functions/tests
creating build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/countrefs.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/misc.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/constants.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/hostinfo.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/config.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
copying sage/dsage/misc/nodoctest.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc
creating build/lib.linux-x86_64-2.5/sage/dsage/misc/tests
copying sage/dsage/misc/tests/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/misc/tests
creating build/lib.linux-x86_64-2.5/sage/dsage/web
copying sage/dsage/web/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/web
copying sage/dsage/web/web_server.py -> build/lib.linux-x86_64-2.5/sage/dsage/web
creating build/lib.linux-x86_64-2.5/sage/dsage/scripts
copying sage/dsage/scripts/dsage_worker.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts
copying sage/dsage/scripts/__init__.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts
copying sage/dsage/scripts/dsage_setup.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts
copying sage/dsage/scripts/nodoctest.py -> build/lib.linux-x86_64-2.5/sage/dsage/scripts
running build_ext
building 'sage.modules.free_module_element' extension
error: unknown file type '.pyx' (from 'sage/modules/free_module_element.pyx')
sage: There was an error installing modified sage library code.



---

archive/issue_comments_019528.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-04-15T16:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19528",
    "user": "https://github.com/yqiang"
}
```

Changing status from closed to reopened.



---

archive/issue_events_003042.json:
```json
{
    "actor": "https://github.com/yqiang",
    "created_at": "2008-04-15T16:53:24Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2851#event-3042"
}
```



---

archive/issue_comments_019529.json:
```json
{
    "body": "Attachment [scripts-2851.patch](tarball://root/attachments/some-uuid/ticket2851/scripts-2851.patch) by @williamstein created at 2008-04-15 17:19:41\n\nnew patch (we want both) -- this to the SCRIPTS repo.",
    "created_at": "2008-04-15T17:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19529",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-2851.patch](tarball://root/attachments/some-uuid/ticket2851/scripts-2851.patch) by @williamstein created at 2008-04-15 17:19:41

new patch (we want both) -- this to the SCRIPTS repo.



---

archive/issue_comments_019530.json:
```json
{
    "body": "scripts-2851.patch fixes the problem and this time I actually did test it :). Shame on me of rubber stamping this the first time around :|\n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T18:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19530",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

scripts-2851.patch fixes the problem and this time I actually did test it :). Shame on me of rubber stamping this the first time around :|

Cheers,

Michael



---

archive/issue_comments_019531.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T18:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19531",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003043.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-15T18:21:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2851#event-3043"
}
```



---

archive/issue_comments_019532.json:
```json
{
    "body": "Merged scripts-2851.patch in Sage 3.0.alpha6",
    "created_at": "2008-04-15T18:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2851#issuecomment-19532",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged scripts-2851.patch in Sage 3.0.alpha6
