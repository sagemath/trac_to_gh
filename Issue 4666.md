# Issue 4666: Make -bdist use canonical binary names

archive/issues_004666.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  jhpalmieri vbraun\n\nWhen we are producing binaries for sagemath.org the naming scheme is often inconsistent and some times even outright misleading. \n\nOn Linux -bdist should produce consistent names for binaries, so use lsb_release when available. I.e. on an x86 Fedora Core 9 system a\n\n```\n ./sage -bdist 3.2.1\n```\n\nwould yield\n\n```\n sage-3.2.1-Fedora-9-x86.tar.gz\n```\n\nThis info can be extracted on Linux via lsb_release\n\n```\n[mabshoff@eno ~]$ lsb_release -i -s\nFedora\n[mabshoff@eno ~]$ lsb_release -r -s\n9\n```\n\nOn OSX use uname to specify OSX release, CPU architecture and 32 vs. 64 bit builds.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4666\n\n",
    "created_at": "2008-12-01T00:01:12Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Make -bdist use canonical binary names",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4666",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  jhpalmieri vbraun

When we are producing binaries for sagemath.org the naming scheme is often inconsistent and some times even outright misleading. 

On Linux -bdist should produce consistent names for binaries, so use lsb_release when available. I.e. on an x86 Fedora Core 9 system a

```
 ./sage -bdist 3.2.1
```

would yield

```
 sage-3.2.1-Fedora-9-x86.tar.gz
```

This info can be extracted on Linux via lsb_release

```
[mabshoff@eno ~]$ lsb_release -i -s
Fedora
[mabshoff@eno ~]$ lsb_release -r -s
9
```

On OSX use uname to specify OSX release, CPU architecture and 32 vs. 64 bit builds.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4666





---

archive/issue_comments_035120.json:
```json
{
    "body": "People get *very* confused by the generic names and end up downloading completely inappropriate releases, so I am making this a 3.3 blocker since I will be fixing this.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-04T21:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35120",
    "user": "mabshoff"
}
```

People get *very* confused by the generic names and end up downloading completely inappropriate releases, so I am making this a 3.3 blocker since I will be fixing this.

Cheers,

Michael



---

archive/issue_comments_035121.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-04T21:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35121",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035122.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-02-04T21:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35122",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_035123.json:
```json
{
    "body": "Reassign it to 3.3 again.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T13:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35123",
    "user": "mabshoff"
}
```

Reassign it to 3.3 again.

Cheers,

Michael



---

archive/issue_comments_035124.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35124",
    "user": "mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_035125.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35125",
    "user": "was"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_035126.json:
```json
{
    "body": "If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35126",
    "user": "was"
}
```

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_035127.json:
```json
{
    "body": "Changing priority from critical to major.",
    "created_at": "2012-05-16T20:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35127",
    "user": "jdemeyer"
}
```

Changing priority from critical to major.



---

archive/issue_comments_035128.json:
```json
{
    "body": "Attachment [botdist.py](tarball://root/attachments/some-uuid/ticket4666/botdist.py) by jdemeyer created at 2012-05-16 20:03:36",
    "created_at": "2012-05-16T20:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35128",
    "user": "jdemeyer"
}
```

Attachment [botdist.py](tarball://root/attachments/some-uuid/ticket4666/botdist.py) by jdemeyer created at 2012-05-16 20:03:36



---

archive/issue_comments_035129.json:
```json
{
    "body": "A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?",
    "created_at": "2014-11-14T19:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35129",
    "user": "kcrisman"
}
```

A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?



---

archive/issue_comments_035130.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?\n\nThat's more a question for the current release manager. Like I mentioned on the ticket, I was using [attachment:botdist.py William's script] to generate binaries, but if Volker no longer uses this, we might as well close this ticket as \"wontfix\".",
    "created_at": "2014-11-15T08:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35130",
    "user": "jdemeyer"
}
```

Replying to [comment:14 kcrisman]:
> A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?

That's more a question for the current release manager. Like I mentioned on the ticket, I was using [attachment:botdist.py William's script] to generate binaries, but if Volker no longer uses this, we might as well close this ticket as "wontfix".



---

archive/issue_comments_035131.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2015-04-14T07:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35131",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_035132.json:
```json
{
    "body": "Replying to [comment:15 jdemeyer]:\n> Replying to [comment:14 kcrisman]:\n> > A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?\n> \n> That's more a question for the current release manager. Like I mentioned on the ticket, I was using [attachment:botdist.py William's script] to generate binaries, but if Volker no longer uses this, we might as well close this ticket as \"wontfix\".\n\nVolker?",
    "created_at": "2015-04-14T07:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35132",
    "user": "mmezzarobba"
}
```

Replying to [comment:15 jdemeyer]:
> Replying to [comment:14 kcrisman]:
> > A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?
> 
> That's more a question for the current release manager. Like I mentioned on the ticket, I was using [attachment:botdist.py William's script] to generate binaries, but if Volker no longer uses this, we might as well close this ticket as "wontfix".

Volker?



---

archive/issue_comments_035133.json:
```json
{
    "body": "I'm not using this script. Labeling binary tarballs by distribution might be worthwile, though. I'm not sure if the current bdist script does that. Note that the buildbots rename the binary tarball as one of the buildsteps.",
    "created_at": "2015-04-14T08:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35133",
    "user": "vbraun"
}
```

I'm not using this script. Labeling binary tarballs by distribution might be worthwile, though. I'm not sure if the current bdist script does that. Note that the buildbots rename the binary tarball as one of the buildsteps.



---

archive/issue_comments_035134.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2015-09-08T12:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35134",
    "user": "jdemeyer"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_035135.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2015-09-12T13:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35135",
    "user": "vbraun"
}
```

Resolution: wontfix
