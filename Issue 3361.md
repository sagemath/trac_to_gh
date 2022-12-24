# Issue 3361: fricas install problem.

archive/issues_003361.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis was reported first by John Cremona and discussed in the thread\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/85bb061c36c57527\nEven though William Stein mentioned someone should create a trac ticket for this issue,\nI could not find one, so made this one.\n\nFrom John C's email:\n\n\n```\nI tried to install fricas (prompted by an earlier thread -- I wonder\nwhich?) but this happened (with 3.0.2 on linux):\n\n axiom_build_bindir =\n/home/jec/sage-3.0.1/spkg/build/fricas-1.0.2/build-dir/build/x86_64-suse-linux/bin\nchecking for gcl... no\nconfigure: error: GCL and GCL sources missing, see README.wh\n***********************************************************\nFailed to configure Axiom.\n***********************************************************\n\nreal    0m0.546s\nuser    0m0.280s\nsys     0m0.268s\nsage: An error occurred while installing fricas-1.0.2\n...\n```\n\nThe file 'fricas-1.0.2.spkg' from\nhttp://www.sagemath.org/packages/optional\ncame from Burcin Erocal on April 1, 2008. \n\nI can duplicate this problem on amd64 hardy heron (ubuntu 8.04,\non a phenom processor machine), with gcl and binutils-dev installed. \nA similar problem occurs for the older version made by Bill Page at \nhttp://sage.math.washington.edu/home/page/packages/axiom4sage-0.3.1.spkg\n\n- David Joyner\n\nIssue created by migration from https://trac.sagemath.org/ticket/3361\n\n",
    "created_at": "2008-06-04T16:04:10Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "fricas install problem.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3361",
    "user": "@wdjoyner"
}
```
Assignee: mabshoff

This was reported first by John Cremona and discussed in the thread
http://groups.google.com/group/sage-devel/browse_thread/thread/85bb061c36c57527
Even though William Stein mentioned someone should create a trac ticket for this issue,
I could not find one, so made this one.

From John C's email:


```
I tried to install fricas (prompted by an earlier thread -- I wonder
which?) but this happened (with 3.0.2 on linux):

 axiom_build_bindir =
/home/jec/sage-3.0.1/spkg/build/fricas-1.0.2/build-dir/build/x86_64-suse-linux/bin
checking for gcl... no
configure: error: GCL and GCL sources missing, see README.wh
***********************************************************
Failed to configure Axiom.
***********************************************************

real    0m0.546s
user    0m0.280s
sys     0m0.268s
sage: An error occurred while installing fricas-1.0.2
...
```

The file 'fricas-1.0.2.spkg' from
http://www.sagemath.org/packages/optional
came from Burcin Erocal on April 1, 2008. 

I can duplicate this problem on amd64 hardy heron (ubuntu 8.04,
on a phenom processor machine), with gcl and binutils-dev installed. 
A similar problem occurs for the older version made by Bill Page at 
http://sage.math.washington.edu/home/page/packages/axiom4sage-0.3.1.spkg

- David Joyner

Issue created by migration from https://trac.sagemath.org/ticket/3361





---

archive/issue_comments_023522.json:
```json
{
    "body": "Waldek Hebish and Bill Page updated the FriCAS.spkg. The new one can be found at\n\nhttp://sage.math.washington.edu/home/page/packages/fricas-1.0.3.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T01:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3361#issuecomment-23522",
    "user": "mabshoff"
}
```

Waldek Hebish and Bill Page updated the FriCAS.spkg. The new one can be found at

http://sage.math.washington.edu/home/page/packages/fricas-1.0.3.spkg

Cheers,

Michael



---

archive/issue_comments_023523.json:
```json
{
    "body": "An updated spkg with minimal fixes, i.e. I checked in the files into a repo, can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1/alpha0/fricas-1.0.3.p0.spkg\n\nPositive review from my end. \n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T02:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3361#issuecomment-23523",
    "user": "mabshoff"
}
```

An updated spkg with minimal fixes, i.e. I checked in the files into a repo, can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1/alpha0/fricas-1.0.3.p0.spkg

Positive review from my end. 

Cheers,

Michael



---

archive/issue_comments_023524.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-31T02:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3361#issuecomment-23524",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023525.json:
```json
{
    "body": "Merged in Sage 3.1.alpha0",
    "created_at": "2008-07-31T02:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3361#issuecomment-23525",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha0
