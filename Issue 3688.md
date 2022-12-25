# Issue 3688: trivial problems in the sage spkg

archive/issues_003688.json:
```json
{
    "body": "Assignee: mabshoff\n\n# Scripts missing #!/bin/sh lines in sage-3.0.5.spkg:\n\n```\npull\ninstall\n```\n\n\n# Scripts missing #!/usr/bin/python lines in sage-3.0.5.dpkg:\n\n```\nsage/dsage/misc/hostinfo.py\nsage/dsage/scripts/dsage_setup.py\n```\n\n\n# Files unnecessarily marked as executable in sage-3.0.5.spkg\n\n```\nsage/graphs/planarity/graphEmbed.c\nsage/graphs/planarity/graphIO.c\nsage/graphs/planarity/graphIsolator.c\nsage/graphs/planarity/graphNonplanar.c\nsage/graphs/planarity/graphPreprocess.c\nsage/graphs/planarity/graphStructure.c\nsage/graphs/planarity/graphTests.c\nsage/graphs/planarity/listcoll.c\nsage/graphs/planarity/planarity.c\nsage/graphs/planarity/stack.c\n```\n\n\n# Other files unnecessarily marked as executable\n\n```\nsage-README-osx.txt (in the root of the sage distribution)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3688\n\n",
    "created_at": "2008-07-21T05:48:09Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "trivial problems in the sage spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3688",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

# Scripts missing #!/bin/sh lines in sage-3.0.5.spkg:

```
pull
install
```


# Scripts missing #!/usr/bin/python lines in sage-3.0.5.dpkg:

```
sage/dsage/misc/hostinfo.py
sage/dsage/scripts/dsage_setup.py
```


# Files unnecessarily marked as executable in sage-3.0.5.spkg

```
sage/graphs/planarity/graphEmbed.c
sage/graphs/planarity/graphIO.c
sage/graphs/planarity/graphIsolator.c
sage/graphs/planarity/graphNonplanar.c
sage/graphs/planarity/graphPreprocess.c
sage/graphs/planarity/graphStructure.c
sage/graphs/planarity/graphTests.c
sage/graphs/planarity/listcoll.c
sage/graphs/planarity/planarity.c
sage/graphs/planarity/stack.c
```


# Other files unnecessarily marked as executable

```
sage-README-osx.txt (in the root of the sage distribution)
```



Issue created by migration from https://trac.sagemath.org/ticket/3688





---

archive/issue_comments_026088.json:
```json
{
    "body": "Attachment [sage-shebang-fixes.patch](tarball://root/attachments/some-uuid/ticket3688/sage-shebang-fixes.patch) by @timabbott created at 2008-08-03 05:43:28",
    "created_at": "2008-08-03T05:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3688#issuecomment-26088",
    "user": "https://github.com/timabbott"
}
```

Attachment [sage-shebang-fixes.patch](tarball://root/attachments/some-uuid/ticket3688/sage-shebang-fixes.patch) by @timabbott created at 2008-08-03 05:43:28



---

archive/issue_comments_026089.json:
```json
{
    "body": "I realized this should probably be marked as having a patch, since it does.  You'll want to apply the patch that is attached and run\n\n```\n   chmod -x sage/graphs/planarity/*.c\n```\n\nfrom the root of the Sage spkg.",
    "created_at": "2009-04-26T05:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3688#issuecomment-26089",
    "user": "https://github.com/timabbott"
}
```

I realized this should probably be marked as having a patch, since it does.  You'll want to apply the patch that is attached and run

```
   chmod -x sage/graphs/planarity/*.c
```

from the root of the Sage spkg.



---

archive/issue_comments_026090.json:
```json
{
    "body": "I don't see a sage/dsage directory in sage-4.1.spkg. Has this been moved/removed?",
    "created_at": "2009-07-21T16:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3688#issuecomment-26090",
    "user": "https://github.com/maxthemouse"
}
```

I don't see a sage/dsage directory in sage-4.1.spkg. Has this been moved/removed?



---

archive/issue_comments_026091.json:
```json
{
    "body": "I applied the patch and ran the chmod command as suggested above. The patch failed due to missing files but I continued anyway.\n\nNote: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1. \n\nAssuming that the change in dsage is fine then I would give this a positive review.",
    "created_at": "2009-07-22T06:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3688#issuecomment-26091",
    "user": "https://github.com/maxthemouse"
}
```

I applied the patch and ran the chmod command as suggested above. The patch failed due to missing files but I continued anyway.

Note: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1. 

Assuming that the change in dsage is fine then I would give this a positive review.



---

archive/issue_comments_026092.json:
```json
{
    "body": "skip dsage files",
    "created_at": "2009-07-22T06:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3688#issuecomment-26092",
    "user": "https://github.com/maxthemouse"
}
```

skip dsage files



---

archive/issue_events_008459.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-24T09:11:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3688",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3688#event-8459"
}
```



---

archive/issue_comments_026093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-24T09:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3688#issuecomment-26093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_026094.json:
```json
{
    "body": "Attachment [sage-shebang-fixes.2.patch](tarball://root/attachments/some-uuid/ticket3688/sage-shebang-fixes.2.patch) by mvngu created at 2009-07-24 09:11:34\n\ndsage has been moved into its own package. You can find it under `SAGE_ROOT/spkg/standard/`.",
    "created_at": "2009-07-24T09:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3688#issuecomment-26094",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [sage-shebang-fixes.2.patch](tarball://root/attachments/some-uuid/ticket3688/sage-shebang-fixes.2.patch) by mvngu created at 2009-07-24 09:11:34

dsage has been moved into its own package. You can find it under `SAGE_ROOT/spkg/standard/`.
