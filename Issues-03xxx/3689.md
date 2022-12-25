# Issue 3689: [with patch, positive review] trivial problems in the examples spkg

archive/issues_003689.json:
```json
{
    "body": "Assignee: mabshoff\n\n# Scripts missing #!/bin/sh lines in examples-3.0.5.spkg:\n\n```\nprogramming/standalone_scripts/python/test\n```\n\n# Empty directories in examples-3.0.5.spkg\n\n```\nexamples/misc/\n```\n\n# Scripts that use #!sage or #!sage.bin as their interpreter in examples-3.0.5.spkg\n# You want to use #!/usr/bin/env sage\n\n```\nprogramming/standalone_scripts/python/binom \nprogramming/standalone_scripts/python/factor \nprogramming/standalone_scripts/sage/factor.sage \nprogramming/standalone_scripts/sage/simple.sage\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3689\n\n",
    "closed_at": "2009-07-23T09:48:39Z",
    "created_at": "2008-07-21T05:48:56Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, positive review] trivial problems in the examples spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3689",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

# Scripts missing #!/bin/sh lines in examples-3.0.5.spkg:

```
programming/standalone_scripts/python/test
```

# Empty directories in examples-3.0.5.spkg

```
examples/misc/
```

# Scripts that use #!sage or #!sage.bin as their interpreter in examples-3.0.5.spkg
# You want to use #!/usr/bin/env sage

```
programming/standalone_scripts/python/binom 
programming/standalone_scripts/python/factor 
programming/standalone_scripts/sage/factor.sage 
programming/standalone_scripts/sage/simple.sage
```

Issue created by migration from https://trac.sagemath.org/ticket/3689





---

archive/issue_comments_026095.json:
```json
{
    "body": "Attachment [sage_scripts-shebang.patch](tarball://root/attachments/some-uuid/ticket3689/sage_scripts-shebang.patch) by @timabbott created at 2009-04-26 05:20:33",
    "created_at": "2009-04-26T05:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3689#issuecomment-26095",
    "user": "https://github.com/timabbott"
}
```

Attachment [sage_scripts-shebang.patch](tarball://root/attachments/some-uuid/ticket3689/sage_scripts-shebang.patch) by @timabbott created at 2009-04-26 05:20:33



---

archive/issue_comments_026096.json:
```json
{
    "body": "Oops, tried to update the wrong patch.  You just want the examples-shebang.patch.\nAlong with applying that patch, one should run\n\n```\nrmdir misc\n```\nfrom the root of the examples spkg.  The /usr/bin/env/sage issues have already been fixed.",
    "created_at": "2009-04-26T05:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3689#issuecomment-26096",
    "user": "https://github.com/timabbott"
}
```

Oops, tried to update the wrong patch.  You just want the examples-shebang.patch.
Along with applying that patch, one should run

```
rmdir misc
```
from the root of the examples spkg.  The /usr/bin/env/sage issues have already been fixed.



---

archive/issue_comments_026097.json:
```json
{
    "body": "I applied the patch and ran the rmdir command as suggested above.\n\nNote: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1.",
    "created_at": "2009-07-22T06:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3689#issuecomment-26097",
    "user": "https://github.com/maxthemouse"
}
```

I applied the patch and ran the rmdir command as suggested above.

Note: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1.



---

archive/issue_events_008460.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-23T09:48:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3689",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3689#event-8460"
}
```



---

archive/issue_comments_026098.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T09:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3689#issuecomment-26098",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
