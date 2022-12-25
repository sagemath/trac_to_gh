# Issue 3041: [with spkg, positive review] optimization setting in LinBox.spkg is broken

archive/issues_003041.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrancois reports:\n\n```\nJust reviewing what options linbox is compiled with for sage,\nwell I was really looking at whether optimizations are enabled.\nIn theory they are, except on Sun:\nif [ $UNAME = \"SunOS\" ]; then\n   OPT=\"--enable-optimization=false\"\n   echo \"Building on SunOS\"\nelse\n   OPT=\"--enable-optimization\"\nfi\n\nOf course in practice they aren't because \"$OPS\" and not\n\"$OPT\" is passed to the configuration. I must admit I didn't\ncheck if it was corrected in 3.0.1.alpha0 but if so I missed\nit in michael's log. \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3041\n\n",
    "closed_at": "2008-04-27T05:33:45Z",
    "created_at": "2008-04-27T04:54:06Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with spkg, positive review] optimization setting in LinBox.spkg is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3041",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Francois reports:

```
Just reviewing what options linbox is compiled with for sage,
well I was really looking at whether optimizations are enabled.
In theory they are, except on Sun:
if [ $UNAME = "SunOS" ]; then
   OPT="--enable-optimization=false"
   echo "Building on SunOS"
else
   OPT="--enable-optimization"
fi

Of course in practice they aren't because "$OPS" and not
"$OPT" is passed to the configuration. I must admit I didn't
check if it was corrected in 3.0.1.alpha0 but if so I missed
it in michael's log. 
```

Issue created by migration from https://trac.sagemath.org/ticket/3041





---

archive/issue_comments_020881.json:
```json
{
    "body": "Attachment [trac_3041.patch](tarball://root/attachments/some-uuid/ticket3041/trac_3041.patch) by mabshoff created at 2008-04-27 05:03:17\n\nThe spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/alpha1/linbox-1.1.5.p4.spkg\n\ncontains the fix in form of the above patch. It builds fine for me on sage.math and bsd.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-27T05:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3041#issuecomment-20881",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3041.patch](tarball://root/attachments/some-uuid/ticket3041/trac_3041.patch) by mabshoff created at 2008-04-27 05:03:17

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/alpha1/linbox-1.1.5.p4.spkg

contains the fix in form of the above patch. It builds fine for me on sage.math and bsd.

Cheers,

Michael



---

archive/issue_comments_020882.json:
```json
{
    "body": "Tested on OSX and Linux. Spkg builds, modular forms doctest all pass.",
    "created_at": "2008-04-27T05:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3041#issuecomment-20882",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Tested on OSX and Linux. Spkg builds, modular forms doctest all pass.



---

archive/issue_comments_020883.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-04-27T05:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3041#issuecomment-20883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha1



---

archive/issue_comments_020884.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-27T05:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3041#issuecomment-20884",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006890.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-27T05:33:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3041",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3041#event-6890"
}
```



---

archive/issue_comments_020885.json:
```json
{
    "body": "Partial credit goes to Francois Bissey.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-27T05:36:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3041#issuecomment-20885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Partial credit goes to Francois Bissey.

Cheers,

Michael
