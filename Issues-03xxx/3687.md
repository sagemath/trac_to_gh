# Issue 3687: [with patch, positive review] trivial problems in the sage_scripts spkg

archive/issues_003687.json:
```json
{
    "body": "Assignee: mabshoff\n\nBelow is a list trivial problems in the sage_scripts spkg that were found by Debian's automatic package quality checking tools:\n\n# Scripts missing #!/bin/sh lines in sage_scripts-3.0.5.spkg:\nsage-pull\nsage-push\nsage-mirror\nsage-mirror-darcs-scripts\nsage-osx-open\n\n# Scripts missing #!/usr/bin/python lines in sage_scripts-3.0.5.dpkg:\nsage-startuptime.py\nsage-gdb-pythonstartup\ndsage_setup.py\n\n# Files unnecessarily marked as executable in sage_scripts-3.0.5.spkg\nsage-banner\nsage-gdb-commands\nsage-maxima.lisp\n\n# Scripts that use #!sage or #!sage.bin as their interpreter in sage_scripts-3.0.5.spkg\n# You want to use #!/usr/bin/env sage\nsage-ipython \nsage-location\nsage-preparse\nsage-run \nsage-run2\n\n# Weird files in sage_scripts-3.0.5.spkg marked executable\nsage-README-osx.txt (duplicate of file of the same name in the root of the sage distribution)\nsage-verify-pyc (this one is just weird)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3687\n\n",
    "closed_at": "2009-07-23T09:42:35Z",
    "created_at": "2008-07-21T05:46:02Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, positive review] trivial problems in the sage_scripts spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3687",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

Below is a list trivial problems in the sage_scripts spkg that were found by Debian's automatic package quality checking tools:

# Scripts missing #!/bin/sh lines in sage_scripts-3.0.5.spkg:
sage-pull
sage-push
sage-mirror
sage-mirror-darcs-scripts
sage-osx-open

# Scripts missing #!/usr/bin/python lines in sage_scripts-3.0.5.dpkg:
sage-startuptime.py
sage-gdb-pythonstartup
dsage_setup.py

# Files unnecessarily marked as executable in sage_scripts-3.0.5.spkg
sage-banner
sage-gdb-commands
sage-maxima.lisp

# Scripts that use #!sage or #!sage.bin as their interpreter in sage_scripts-3.0.5.spkg
# You want to use #!/usr/bin/env sage
sage-ipython 
sage-location
sage-preparse
sage-run 
sage-run2

# Weird files in sage_scripts-3.0.5.spkg marked executable
sage-README-osx.txt (duplicate of file of the same name in the root of the sage distribution)
sage-verify-pyc (this one is just weird)


Issue created by migration from https://trac.sagemath.org/ticket/3687





---

archive/issue_comments_026082.json:
```json
{
    "body": "Let's try that again with proper formatting:\n\n# Scripts missing #!/bin/sh lines in sage_scripts-3.0.5.spkg:\n\n```\nsage-pull\nsage-push\nsage-mirror\nsage-mirror-darcs-scripts\nsage-osx-open\n```\n\n# Scripts missing #!/usr/bin/python lines in sage_scripts-3.0.5.dpkg:\n\n```\nsage-startuptime.py\nsage-gdb-pythonstartup\ndsage_setup.py\n```\n\n# Files unnecessarily marked as executable in sage_scripts-3.0.5.spkg\n\n```\nsage-banner\nsage-gdb-commands\nsage-maxima.lisp\n```\n\n# Scripts that use #!sage or #!sage.bin as their interpreter in sage_scripts-3.0.5.spkg\n# You want to use #!/usr/bin/env sage\n\n```\nsage-ipython \nsage-location\nsage-preparse\nsage-run \nsage-run2\n```\n\n# Weird files in sage_scripts-3.0.5.spkg marked executable\n\n```\nsage-README-osx.txt (duplicate of file of the same name in the root of the sage distribution)\nsage-verify-pyc (this one is just weird)\n```",
    "created_at": "2008-07-21T05:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3687#issuecomment-26082",
    "user": "https://github.com/timabbott"
}
```

Let's try that again with proper formatting:

# Scripts missing #!/bin/sh lines in sage_scripts-3.0.5.spkg:

```
sage-pull
sage-push
sage-mirror
sage-mirror-darcs-scripts
sage-osx-open
```

# Scripts missing #!/usr/bin/python lines in sage_scripts-3.0.5.dpkg:

```
sage-startuptime.py
sage-gdb-pythonstartup
dsage_setup.py
```

# Files unnecessarily marked as executable in sage_scripts-3.0.5.spkg

```
sage-banner
sage-gdb-commands
sage-maxima.lisp
```

# Scripts that use #!sage or #!sage.bin as their interpreter in sage_scripts-3.0.5.spkg
# You want to use #!/usr/bin/env sage

```
sage-ipython 
sage-location
sage-preparse
sage-run 
sage-run2
```

# Weird files in sage_scripts-3.0.5.spkg marked executable

```
sage-README-osx.txt (duplicate of file of the same name in the root of the sage distribution)
sage-verify-pyc (this one is just weird)
```



---

archive/issue_comments_026083.json:
```json
{
    "body": "Attachment [sage_scripts-shebang.patch](tarball://root/attachments/some-uuid/ticket3687/sage_scripts-shebang.patch) by @timabbott created at 2009-04-26 05:26:09",
    "created_at": "2009-04-26T05:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3687#issuecomment-26083",
    "user": "https://github.com/timabbott"
}
```

Attachment [sage_scripts-shebang.patch](tarball://root/attachments/some-uuid/ticket3687/sage_scripts-shebang.patch) by @timabbott created at 2009-04-26 05:26:09



---

archive/issue_comments_026084.json:
```json
{
    "body": "Along with applying the attached patch, one should run\n\n```\nchmod -x sage-banner sage-gdb-commands sage-maxima.lisp sage-README-osx.txt sage-verify-pyc\n```",
    "created_at": "2009-04-26T05:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3687#issuecomment-26084",
    "user": "https://github.com/timabbott"
}
```

Along with applying the attached patch, one should run

```
chmod -x sage-banner sage-gdb-commands sage-maxima.lisp sage-README-osx.txt sage-verify-pyc
```



---

archive/issue_comments_026085.json:
```json
{
    "body": "I applied the patch and ran the chmod command as suggested above.\n\nNote: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1.",
    "created_at": "2009-07-22T06:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3687#issuecomment-26085",
    "user": "https://github.com/maxthemouse"
}
```

I applied the patch and ran the chmod command as suggested above.

Note: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1.



---

archive/issue_comments_026086.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T09:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3687#issuecomment-26086",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_008458.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-23T09:42:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3687",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3687#event-8458"
}
```



---

archive/issue_comments_026087.json:
```json
{
    "body": "See #6625 for a follow up to this ticket.",
    "created_at": "2009-07-26T06:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3687#issuecomment-26087",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #6625 for a follow up to this ticket.
