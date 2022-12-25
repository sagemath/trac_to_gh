# Issue 552: come up with a better way of deciding whether or not the SAGE install has moved

archive/issues_000552.json:
```json
{
    "body": "Assignee: @williamstein\n\nAll too often, because of symlinks, etc., my script for detecting whether or not the SAGE install\ntree has moved gets it wrong.  This is frickin' annoying.  I would like a way to determine this\nthat is much more intelligent. \n\nThe relevant code is SAGE_ROOT/local/bin/sage-location:\n\n```/usr/bin/env sage.bin\n\nimport os\n\nSAGE_ROOT = os.environ['SAGE_ROOT']\n\nlocation_file = '%s/local/lib/sage-current-location.txt'%SAGE_ROOT\n\ndef install_moved():\n    if not os.path.exists(location_file):\n        O = open(location_file,'w')\n        O.write(SAGE_ROOT)\n        O.close()\n        return False, ''   # first time -- so no need to update; this was during the build.\n\n    O = open(location_file)\n    R = O.read().strip()\n    O.close()\n    if os.path.abspath(R) != os.path.abspath(SAGE_ROOT):  # really different\n        return True, R  # it moved\n    return False, ''\n```\n\n\nAny better ideas???\n\nIssue created by migration from https://trac.sagemath.org/ticket/552\n\n",
    "created_at": "2007-09-01T16:55:28Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "come up with a better way of deciding whether or not the SAGE install has moved",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/552",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

All too often, because of symlinks, etc., my script for detecting whether or not the SAGE install
tree has moved gets it wrong.  This is frickin' annoying.  I would like a way to determine this
that is much more intelligent. 

The relevant code is SAGE_ROOT/local/bin/sage-location:

```/usr/bin/env sage.bin

import os

SAGE_ROOT = os.environ['SAGE_ROOT']

location_file = '%s/local/lib/sage-current-location.txt'%SAGE_ROOT

def install_moved():
    if not os.path.exists(location_file):
        O = open(location_file,'w')
        O.write(SAGE_ROOT)
        O.close()
        return False, ''   # first time -- so no need to update; this was during the build.

    O = open(location_file)
    R = O.read().strip()
    O.close()
    if os.path.abspath(R) != os.path.abspath(SAGE_ROOT):  # really different
        return True, R  # it moved
    return False, ''
```


Any better ideas???

Issue created by migration from https://trac.sagemath.org/ticket/552





---

archive/issue_comments_002833.json:
```json
{
    "body": "Changing component from algebraic geometry to packages.",
    "created_at": "2007-09-07T05:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/552#issuecomment-2833",
    "user": "https://github.com/craigcitro"
}
```

Changing component from algebraic geometry to packages.



---

archive/issue_comments_002834.json:
```json
{
    "body": "We can use the shell program \"readlink\" since that follows symbolic links and friends. We already use it in the sage script to determine the actual location of the sage script.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T09:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/552#issuecomment-2834",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We can use the shell program "readlink" since that follows symbolic links and friends. We already use it in the sage script to determine the actual location of the sage script.

Cheers,

Michael



---

archive/issue_comments_002835.json:
```json
{
    "body": "Attachment [trac_552.patch](tarball://root/attachments/some-uuid/ticket552/trac_552.patch) by anakha created at 2008-10-23 23:24:24\n\nos.path.realpath() takes care of symlinks.\n\nIt's that simple folks.",
    "created_at": "2008-10-23T23:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/552#issuecomment-2835",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Attachment [trac_552.patch](tarball://root/attachments/some-uuid/ticket552/trac_552.patch) by anakha created at 2008-10-23 23:24:24

os.path.realpath() takes care of symlinks.

It's that simple folks.



---

archive/issue_events_001465.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T21:27:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/552",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/552#event-1465"
}
```



---

archive/issue_comments_002836.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T21:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/552#issuecomment-2836",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_002837.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T21:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/552#issuecomment-2837",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001466.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T21:30:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/552",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/552#event-1466"
}
```



---

archive/issue_comments_002838.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T21:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/552#issuecomment-2838",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2
