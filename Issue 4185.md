# Issue 4185: [with spkg, needs review] remove GNUisms from spkg-install of the jmol.spkg

archive/issues_004185.json:
```json
{
    "body": "Assignee: mabshoff\n\nIt boils down to:\n\n```\n # Insert localize.in after first line of startup script.\n-head -n 1 jmol > \"$DIR/jmol\"\n+head -1 jmol > \"$DIR/jmol\"\n cat ../patches/localize.in >> \"$DIR/jmol\"\n-tail -n +2 jmol >> \"$DIR/jmol\"\n+tail +2 jmol >> \"$DIR/jmol\"\n check\n```\n\nThe new spkg can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha1/jmol-11.6.rc8.p0.spkg\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4185\n\n",
    "created_at": "2008-09-24T08:27:24Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with spkg, needs review] remove GNUisms from spkg-install of the jmol.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4185",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

It boils down to:

```
 # Insert localize.in after first line of startup script.
-head -n 1 jmol > "$DIR/jmol"
+head -1 jmol > "$DIR/jmol"
 cat ../patches/localize.in >> "$DIR/jmol"
-tail -n +2 jmol >> "$DIR/jmol"
+tail +2 jmol >> "$DIR/jmol"
 check
```

The new spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha1/jmol-11.6.rc8.p0.spkg

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4185





---

archive/issue_comments_030311.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-24T08:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4185#issuecomment-30311",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030312.json:
```json
{
    "body": "I get this:\n\n\n```\n****************************************************\nCopying Jmol libraries...\nCopying Jmol scripts...\ntail: cannot open `+2' for reading: No such file or directory\nError.\n\nreal\t0m0.377s\nuser\t0m0.020s\nsys\t0m0.056s\nsage: An error occurred while installing jmol-11.6.rc8.p0\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /opt/sage/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/opt/sage/spkg/build/jmol-11.6.rc8.p0 and type 'make'.\nInstead type \"/opt/sage/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/opt/sage/spkg/build/jmol-11.6.rc8.p0\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\n```\n",
    "created_at": "2008-09-24T09:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4185#issuecomment-30312",
    "user": "https://github.com/mwhansen"
}
```

I get this:


```
****************************************************
Copying Jmol libraries...
Copying Jmol scripts...
tail: cannot open `+2' for reading: No such file or directory
Error.

real	0m0.377s
user	0m0.020s
sys	0m0.056s
sage: An error occurred while installing jmol-11.6.rc8.p0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /opt/sage/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/opt/sage/spkg/build/jmol-11.6.rc8.p0 and type 'make'.
Instead type "/opt/sage/sage -sh"
in order to set all environment variables correctly, then cd to
/opt/sage/spkg/build/jmol-11.6.rc8.p0
(When you are done debugging, you can type "exit" to leave the
subshell.)
```




---

archive/issue_comments_030313.json:
```json
{
    "body": "Ok, I need to think about this an fix the problem. It looks like we cannot get something that works equally well on Solaris and on-Solaris.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T09:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4185#issuecomment-30313",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, I need to think about this an fix the problem. It looks like we cannot get something that works equally well on Solaris and on-Solaris.

Cheers,

Michael



---

archive/issue_comments_030314.json:
```json
{
    "body": "Ok, I am taking it back for now and will figure out what to do here.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T10:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4185#issuecomment-30314",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, I am taking it back for now and will figure out what to do here.

Cheers,

Michael



---

archive/issue_comments_030315.json:
```json
{
    "body": "The latest working spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/jmol-11.6.rc8.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T10:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4185#issuecomment-30315",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The latest working spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/jmol-11.6.rc8.p0.spkg

Cheers,

Michael



---

archive/issue_comments_030316.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-01-19T10:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4185#issuecomment-30316",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_030317.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-01-19T10:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4185#issuecomment-30317",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_030318.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T10:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4185#issuecomment-30318",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030319.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T10:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4185#issuecomment-30319",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0
