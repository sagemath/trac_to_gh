# Issue 6626: can't upgrade to cliquer-1.2.p0 since package name is missing from file deps

archive/issues_006626.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @nathanncohen @rlmill\n\nKeywords: cliquer\n\nAs the subject says. This is a follow up to #6355.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6626\n\n",
    "created_at": "2009-07-26T08:26:02Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "can't upgrade to cliquer-1.2.p0 since package name is missing from file deps",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6626",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mabshoff

CC:  @nathanncohen @rlmill

Keywords: cliquer

As the subject says. This is a follow up to #6355.

Issue created by migration from https://trac.sagemath.org/ticket/6626





---

archive/issue_comments_054184.json:
```json
{
    "body": "The SPKG installs OK if doing so from source. But there is a problem when it comes to upgrading from 4.1.1.alpha0 to 4.1.1.alpha1. Here's a relevant snippet:\n\n```\nMachine:\nLinux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux\nsage: dsage-1.0.1.p0 is already installed\ncd /home/mvngu/usr/bin/sage && . local/bin/sage-env && cd local/bin/ && ./sage-make_relative\nMaking script relocatable\n\nreal\t58m23.858s\nuser\t52m19.696s\nsys\t4m53.842s\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py\", line 673, in <module>\n    getattr(get_builder(name), type)()\n  File \"/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py\", line 259, in _wrapper\n    getattr(get_builder(document), name)(*args, **kwds)\n  File \"/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py\", line 616, in get_builder\n    elif name in get_documents() or name in AllBuilder().get_all_documents():\nNameError: global name 'get_documents' is not defined\nDouble checking that all packages have been installed.\nDownloading packages from http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg\nhttp://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard\nReading package lists...\nDone\nThe following packages will be upgraded:\n  cliquer-1.2.p0\n* WARNING: This is a source-based upgrade, which could take hours, fail and render your Sage install useless!!\nDo you want to continue [y/N]? y\nhttp://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard/cliquer-1.2.p0.spkg --> cliquer-1.2.p0.spkg\n[..........]\nDeleting old spkg cliquer-1.2.p0.spkg\nhttp://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/install --> install\n[.]\nhttp://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard/deps --> deps\n[..]\nhttp://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard/newest_version --> newest_version\n[.]\nsage-spkg sage-4.1.1.alpha1 \nYou must set the SAGE_ROOT environment variable or\nrun this script from the SAGE_ROOT or \nSAGE_ROOT/local/bin/ directory.\nsage-4.1.1.alpha1\nMachine:\nLinux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux\nsage: sage-4.1.1.alpha1 is already installed\ncd /home/mvngu/usr/bin/sage && . local/bin/sage-env && cd local/bin/ && ./sage-make_relative\nMaking script relocatable\nsage-spkg gap-4.4.10.p12 2>&1\nYou must set the SAGE_ROOT environment variable or\nrun this script from the SAGE_ROOT or \nSAGE_ROOT/local/bin/ directory.\ngap-4.4.10.p12\nMachine:\nLinux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux\nsage: gap-4.4.10.p12 is already installed\nsage-spkg dsage-1.0.1.p0 2>&1\nYou must set the SAGE_ROOT environment variable or\nrun this script from the SAGE_ROOT or \nSAGE_ROOT/local/bin/ directory.\ndsage-1.0.1.p0\nMachine:\nLinux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux\nsage: dsage-1.0.1.p0 is already installed\ncd /home/mvngu/usr/bin/sage && . local/bin/sage-env && cd local/bin/ && ./sage-make_relative\nMaking script relocatable\n\nreal\t0m0.414s\nuser\t0m0.156s\nsys\t0m0.184s\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py\", line 673, in <module>\n    getattr(get_builder(name), type)()\n  File \"/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py\", line 259, in _wrapper\n    getattr(get_builder(document), name)(*args, **kwds)\n  File \"/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py\", line 616, in get_builder\n    elif name in get_documents() or name in AllBuilder().get_all_documents():\nNameError: global name 'get_documents' is not defined\n```\n\nApparently, the package name should have been added to the file\n\n```\nSAGE_ROOT/spkg/standard/deps\n```\n",
    "created_at": "2009-07-26T08:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6626#issuecomment-54184",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The SPKG installs OK if doing so from source. But there is a problem when it comes to upgrading from 4.1.1.alpha0 to 4.1.1.alpha1. Here's a relevant snippet:

```
Machine:
Linux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux
sage: dsage-1.0.1.p0 is already installed
cd /home/mvngu/usr/bin/sage && . local/bin/sage-env && cd local/bin/ && ./sage-make_relative
Making script relocatable

real	58m23.858s
user	52m19.696s
sys	4m53.842s
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 673, in <module>
    getattr(get_builder(name), type)()
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 259, in _wrapper
    getattr(get_builder(document), name)(*args, **kwds)
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 616, in get_builder
    elif name in get_documents() or name in AllBuilder().get_all_documents():
NameError: global name 'get_documents' is not defined
Double checking that all packages have been installed.
Downloading packages from http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg
http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard
Reading package lists...
Done
The following packages will be upgraded:
  cliquer-1.2.p0
* WARNING: This is a source-based upgrade, which could take hours, fail and render your Sage install useless!!
Do you want to continue [y/N]? y
http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard/cliquer-1.2.p0.spkg --> cliquer-1.2.p0.spkg
[..........]
Deleting old spkg cliquer-1.2.p0.spkg
http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/install --> install
[.]
http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard/deps --> deps
[..]
http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard/newest_version --> newest_version
[.]
sage-spkg sage-4.1.1.alpha1 
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or 
SAGE_ROOT/local/bin/ directory.
sage-4.1.1.alpha1
Machine:
Linux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux
sage: sage-4.1.1.alpha1 is already installed
cd /home/mvngu/usr/bin/sage && . local/bin/sage-env && cd local/bin/ && ./sage-make_relative
Making script relocatable
sage-spkg gap-4.4.10.p12 2>&1
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or 
SAGE_ROOT/local/bin/ directory.
gap-4.4.10.p12
Machine:
Linux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux
sage: gap-4.4.10.p12 is already installed
sage-spkg dsage-1.0.1.p0 2>&1
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or 
SAGE_ROOT/local/bin/ directory.
dsage-1.0.1.p0
Machine:
Linux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux
sage: dsage-1.0.1.p0 is already installed
cd /home/mvngu/usr/bin/sage && . local/bin/sage-env && cd local/bin/ && ./sage-make_relative
Making script relocatable

real	0m0.414s
user	0m0.156s
sys	0m0.184s
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 673, in <module>
    getattr(get_builder(name), type)()
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 259, in _wrapper
    getattr(get_builder(document), name)(*args, **kwds)
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 616, in get_builder
    elif name in get_documents() or name in AllBuilder().get_all_documents():
NameError: global name 'get_documents' is not defined
```

Apparently, the package name should have been added to the file

```
SAGE_ROOT/spkg/standard/deps
```




---

archive/issue_comments_054185.json:
```json
{
    "body": "Replying to [comment:1 mvngu]:\n> Apparently, the package name should have been added to the file\n> {{{\n> SAGE_ROOT/spkg/standard/deps\n> }}}\n\nThis has always been the release manager's job. For example, when I added ratpoints to sage-4.1, I just put the relevant lines into `deps` myself, since I was managing the release.",
    "created_at": "2009-07-27T15:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6626#issuecomment-54185",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:1 mvngu]:
> Apparently, the package name should have been added to the file
> {{{
> SAGE_ROOT/spkg/standard/deps
> }}}

This has always been the release manager's job. For example, when I added ratpoints to sage-4.1, I just put the relevant lines into `deps` myself, since I was managing the release.



---

archive/issue_comments_054186.json:
```json
{
    "body": "Replying to [comment:2 rlm]:\n> Replying to [comment:1 mvngu]:\n> > Apparently, the package name should have been added to the file\n> > {{{\n> > SAGE_ROOT/spkg/standard/deps\n> > }}}\n> \n> This has always been the release manager's job. For example, when I added ratpoints to sage-4.1, I just put the relevant lines into `deps` myself, since I was managing the release.\nAh... I didn't know about this. The release management wiki page should have some information about updating the `deps` file, if it's not there already. Looks like this ticket is now invalid, right?",
    "created_at": "2009-07-28T03:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6626#issuecomment-54186",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 rlm]:
> Replying to [comment:1 mvngu]:
> > Apparently, the package name should have been added to the file
> > {{{
> > SAGE_ROOT/spkg/standard/deps
> > }}}
> 
> This has always been the release manager's job. For example, when I added ratpoints to sage-4.1, I just put the relevant lines into `deps` myself, since I was managing the release.
Ah... I didn't know about this. The release management wiki page should have some information about updating the `deps` file, if it's not there already. Looks like this ticket is now invalid, right?



---

archive/issue_events_006866.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-30T15:15:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6626",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6626#event-6866"
}
```



---

archive/issue_comments_054187.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-07-30T15:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6626#issuecomment-54187",
    "user": "https://github.com/rlmill"
}
```

Resolution: invalid
