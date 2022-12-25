# Issue 4125: Build breaks entirely or pulls in non-standard libraries with fink and macports

archive/issues_004125.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  dphilp\n\nThe Sage build process pulls in non-standard libraries if they are easily found.  Fink and MacPorts have a habit of making their libraries easily found, because they fiddle with $PATH, etc.  This sometimes means that the build fails, or works, but the resulting product is broken.  \n\nThe fix is simple: move /sw and /opt/local during the build process.  However, this is not at all obvious the first time.  This script runs a simple test to check whether fink or ports are likely to interfere, and gives a useful error message.\n\n\n```/bin/bash\n\n# Try to find ports automatically.\nPORTS_PATH=`which port`\n\n# Try to find fink automatically.\nFINK_PATH=`which fink`\n\nif [ \"$PORTS_PATH\" -o \"$FINK_PATH\" ] ; then\n  echo \"Found either MacPorts or Fink in your path, which often prevents Sage from compiling.\"\n  if [ \"$SAGE_COMPILE_DESPITE_PORTS_AND_FINK\" ] ; then\n    echo \"Continuing because SAGE_COMPILE_DESPITE_PORTS_AND_FINK is set.\"\n  else\n    echo \"If you want to want to compile, you should rename /opt/local and /sw\"\n    echo \"during the build process.  (Once Sage is built, you can move them to\"\n    echo \"their original location.)\"\n    exit 1\n  fi\nfi\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4125\n\n",
    "created_at": "2008-09-15T01:53:19Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Build breaks entirely or pulls in non-standard libraries with fink and macports",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4125",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```
Assignee: mabshoff

CC:  dphilp

The Sage build process pulls in non-standard libraries if they are easily found.  Fink and MacPorts have a habit of making their libraries easily found, because they fiddle with $PATH, etc.  This sometimes means that the build fails, or works, but the resulting product is broken.  

The fix is simple: move /sw and /opt/local during the build process.  However, this is not at all obvious the first time.  This script runs a simple test to check whether fink or ports are likely to interfere, and gives a useful error message.


```/bin/bash

# Try to find ports automatically.
PORTS_PATH=`which port`

# Try to find fink automatically.
FINK_PATH=`which fink`

if [ "$PORTS_PATH" -o "$FINK_PATH" ] ; then
  echo "Found either MacPorts or Fink in your path, which often prevents Sage from compiling."
  if [ "$SAGE_COMPILE_DESPITE_PORTS_AND_FINK" ] ; then
    echo "Continuing because SAGE_COMPILE_DESPITE_PORTS_AND_FINK is set."
  else
    echo "If you want to want to compile, you should rename /opt/local and /sw"
    echo "during the build process.  (Once Sage is built, you can move them to"
    echo "their original location.)"
    exit 1
  fi
fi
```


Issue created by migration from https://trac.sagemath.org/ticket/4125





---

archive/issue_comments_029846.json:
```json
{
    "body": "Attachment [trac_4125.patch](tarball://root/attachments/some-uuid/ticket4125/trac_4125.patch) by mabshoff created at 2008-09-15 02:25:45",
    "created_at": "2008-09-15T02:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4125#issuecomment-29846",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4125.patch](tarball://root/attachments/some-uuid/ticket4125/trac_4125.patch) by mabshoff created at 2008-09-15 02:25:45



---

archive/issue_comments_029847.json:
```json
{
    "body": "Looks good to me!",
    "created_at": "2008-09-15T02:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4125#issuecomment-29847",
    "user": "https://github.com/rlmill"
}
```

Looks good to me!



---

archive/issue_events_004362.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-15T02:49:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4125#event-4362"
}
```



---

archive/issue_comments_029848.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-15T02:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4125#issuecomment-29848",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029849.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc4",
    "created_at": "2008-09-15T02:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4125#issuecomment-29849",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc4



---

archive/issue_comments_029850.json:
```json
{
    "body": "This doesn't work for me: I don't have macports or fink and it kills my build.",
    "created_at": "2008-09-15T14:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4125#issuecomment-29850",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This doesn't work for me: I don't have macports or fink and it kills my build.



---

archive/issue_comments_029851.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-10-06T19:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4125#issuecomment-29851",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_029852.json:
```json
{
    "body": "Negative review, please revert the patch.\n\nIt breaks age builds that otherwise went fine, thus is a \"false negative\", e.g. for mhampton as reported above, or for David Harvey, as reported in the sage-devel discussion \"macports\" on Oct. 5th., see there for more (negative) opinions.\n\nOn the other hand, the patch might has become superfluous by patch 4127, but that should be confirmed by others.\n\nIf not, probably it is best to enhance 4127 until that one works as desired.\n\nSo please revert the patch of this ticket and then close the ticket as \"wont\", or better, as a \"doublette\" to 4127.",
    "created_at": "2008-10-06T19:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4125#issuecomment-29852",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Negative review, please revert the patch.

It breaks age builds that otherwise went fine, thus is a "false negative", e.g. for mhampton as reported above, or for David Harvey, as reported in the sage-devel discussion "macports" on Oct. 5th., see there for more (negative) opinions.

On the other hand, the patch might has become superfluous by patch 4127, but that should be confirmed by others.

If not, probably it is best to enhance 4127 until that one works as desired.

So please revert the patch of this ticket and then close the ticket as "wont", or better, as a "doublette" to 4127.



---

archive/issue_comments_029853.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-10-06T19:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4125#issuecomment-29853",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing status from closed to reopened.



---

archive/issue_events_004363.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2008-10-06T19:23:12Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4125#event-4363"
}
```



---

archive/issue_comments_029854.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-07T11:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4125#issuecomment-29854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029855.json:
```json
{
    "body": "Replying to [comment:5 GeorgSWeber]:\n> Negative review, please revert the patch.\n> \n> It breaks age builds that otherwise went fine, thus is a \"false negative\", e.g. for mhampton as reported above, or for David Harvey, as reported in the sage-devel discussion \"macports\" on Oct. 5th., see there for more (negative) opinions.\n\nI do not care. This ticket resolves numerous problems where in the end after *much* debugging it turned out that either MacPorts or Fink was at fault. \n\n> On the other hand, the patch might has become superfluous by patch 4127, but that should be confirmed by others.\n\n\n> If not, probably it is best to enhance 4127 until that one works as desired.\n> \n> So please revert the patch of this ticket and then close the ticket as \"wont\", or better, as a \"doublette\" to 4127.\n\nThis patch will not be reverted.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-07T11:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4125#issuecomment-29855",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 GeorgSWeber]:
> Negative review, please revert the patch.
> 
> It breaks age builds that otherwise went fine, thus is a "false negative", e.g. for mhampton as reported above, or for David Harvey, as reported in the sage-devel discussion "macports" on Oct. 5th., see there for more (negative) opinions.

I do not care. This ticket resolves numerous problems where in the end after *much* debugging it turned out that either MacPorts or Fink was at fault. 

> On the other hand, the patch might has become superfluous by patch 4127, but that should be confirmed by others.


> If not, probably it is best to enhance 4127 until that one works as desired.
> 
> So please revert the patch of this ticket and then close the ticket as "wont", or better, as a "doublette" to 4127.

This patch will not be reverted.

Cheers,

Michael



---

archive/issue_events_004364.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-07T11:56:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4125",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4125#event-4364"
}
```
