# Issue 4666: Make -bdist use canonical binary names

archive/issues_004666.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jhpalmieri @vbraun\n\nWhen we are producing binaries for sagemath.org the naming scheme is often inconsistent and some times even outright misleading. \n\nOn Linux -bdist should produce consistent names for binaries, so use lsb_release when available. I.e. on an x86 Fedora Core 9 system a\n\n```\n ./sage -bdist 3.2.1\n```\n\nwould yield\n\n```\n sage-3.2.1-Fedora-9-x86.tar.gz\n```\n\nThis info can be extracted on Linux via lsb_release\n\n```\n[mabshoff@eno ~]$ lsb_release -i -s\nFedora\n[mabshoff@eno ~]$ lsb_release -r -s\n9\n```\n\nOn OSX use uname to specify OSX release, CPU architecture and 32 vs. 64 bit builds.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4666\n\n",
    "created_at": "2008-12-01T00:01:12Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Make -bdist use canonical binary names",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4666",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @jhpalmieri @vbraun

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

archive/issue_comments_035052.json:
```json
{
    "body": "People get *very* confused by the generic names and end up downloading completely inappropriate releases, so I am making this a 3.3 blocker since I will be fixing this.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-04T21:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35052",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

People get *very* confused by the generic names and end up downloading completely inappropriate releases, so I am making this a 3.3 blocker since I will be fixing this.

Cheers,

Michael



---

archive/issue_comments_035053.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-04T21:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35053",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035054.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-02-04T21:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35054",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_035055.json:
```json
{
    "body": "Reassign it to 3.3 again.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T13:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35055",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Reassign it to 3.3 again.

Cheers,

Michael



---

archive/issue_comments_035056.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35056",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_035057.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35057",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_035058.json:
```json
{
    "body": "If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35058",
    "user": "https://github.com/williamstein"
}
```

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_035059.json:
```json
{
    "body": "Attachment [botdist.py](tarball://root/attachments/some-uuid/ticket4666/botdist.py) by @jdemeyer created at 2012-05-16 20:03:36",
    "created_at": "2012-05-16T20:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35059",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [botdist.py](tarball://root/attachments/some-uuid/ticket4666/botdist.py) by @jdemeyer created at 2012-05-16 20:03:36



---

archive/issue_comments_035060.json:
```json
{
    "body": "A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?",
    "created_at": "2014-11-14T19:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35060",
    "user": "https://github.com/kcrisman"
}
```

A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?



---

archive/issue_comments_035061.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?\n\nThat's more a question for the current release manager. Like I mentioned on the ticket, I was using [attachment:botdist.py William's script] to generate binaries, but if Volker no longer uses this, we might as well close this ticket as \"wontfix\".",
    "created_at": "2014-11-15T08:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35061",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:14 kcrisman]:
> A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?

That's more a question for the current release manager. Like I mentioned on the ticket, I was using [attachment:botdist.py William's script] to generate binaries, but if Volker no longer uses this, we might as well close this ticket as "wontfix".



---

archive/issue_comments_035062.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2015-04-14T07:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35062",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_035063.json:
```json
{
    "body": "Replying to [comment:15 jdemeyer]:\n> Replying to [comment:14 kcrisman]:\n> > A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?\n> \n> That's more a question for the current release manager. Like I mentioned on the ticket, I was using [attachment:botdist.py William's script] to generate binaries, but if Volker no longer uses this, we might as well close this ticket as \"wontfix\".\n\nVolker?",
    "created_at": "2015-04-14T07:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35063",
    "user": "https://github.com/mezzarobba"
}
```

Replying to [comment:15 jdemeyer]:
> Replying to [comment:14 kcrisman]:
> > A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?
> 
> That's more a question for the current release manager. Like I mentioned on the ticket, I was using [attachment:botdist.py William's script] to generate binaries, but if Volker no longer uses this, we might as well close this ticket as "wontfix".

Volker?



---

archive/issue_comments_035064.json:
```json
{
    "body": "I'm not using this script. Labeling binary tarballs by distribution might be worthwile, though. I'm not sure if the current bdist script does that. Note that the buildbots rename the binary tarball as one of the buildsteps.",
    "created_at": "2015-04-14T08:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35064",
    "user": "https://github.com/vbraun"
}
```

I'm not using this script. Labeling binary tarballs by distribution might be worthwile, though. I'm not sure if the current bdist script does that. Note that the buildbots rename the binary tarball as one of the buildsteps.



---

archive/issue_comments_035065.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2015-09-08T12:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35065",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_035066.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2015-09-12T13:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4666#issuecomment-35066",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix
