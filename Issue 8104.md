# Issue 8104: developer's guide for making spkgs should specify that patches need to be version controlled

archive/issues_008104.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  mvngu\n\nWhen working on a spkg and adding or modifying patches, the developers' guide (http://www.sagemath.org/doc/developer/producing_spkgs.html) should remind developers to version-control the patches.\n\n\n```\n19:38 < gsmcwhirter> if some or all of the existing patches no\n  longer apply, should they be left there or deleted? (on networkx, \n  there was an edit to a file to switch from numerix to numpy, but \n  the latest upstream source uses numpy by default)\n19:39 < ddrake> I'd delete obsolete patches, and mention that you \n  did so in SPKG.txt.\n19:48 < ddrake> also note that the patches/ directory is version \n  controlled, so make sure you 'hg add' new patches and 'hg rm' \n  unneeded ones.\n19:51 < mvngu> ddrake: That looks like a sensible thing to do. But \n  it's not documented at http://www.sagemath.org/doc/developer\n  /producing_spkgs.html. \n19:51 < mvngu> ddrake: Could you open a ticket for this and CC me \n  on it?\n19:51 < ddrake> sure. \n19:52 < ddrake> the documentation you just linked to does say \"Make \n  sure that the hg repo contains every file outside the src \n  directory, and that these are all up-to-date and commited into \n  the repo.\"\n19:52 < ddrake> but perhaps patches bear a special mention, just to \n  make it clear. I'll open the ticket.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8104\n\n",
    "created_at": "2010-01-28T03:57:55Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "developer's guide for making spkgs should specify that patches need to be version controlled",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8104",
    "user": "@dandrake"
}
```
Assignee: mvngu

CC:  mvngu

When working on a spkg and adding or modifying patches, the developers' guide (http://www.sagemath.org/doc/developer/producing_spkgs.html) should remind developers to version-control the patches.


```
19:38 < gsmcwhirter> if some or all of the existing patches no
  longer apply, should they be left there or deleted? (on networkx, 
  there was an edit to a file to switch from numerix to numpy, but 
  the latest upstream source uses numpy by default)
19:39 < ddrake> I'd delete obsolete patches, and mention that you 
  did so in SPKG.txt.
19:48 < ddrake> also note that the patches/ directory is version 
  controlled, so make sure you 'hg add' new patches and 'hg rm' 
  unneeded ones.
19:51 < mvngu> ddrake: That looks like a sensible thing to do. But 
  it's not documented at http://www.sagemath.org/doc/developer
  /producing_spkgs.html. 
19:51 < mvngu> ddrake: Could you open a ticket for this and CC me 
  on it?
19:51 < ddrake> sure. 
19:52 < ddrake> the documentation you just linked to does say "Make 
  sure that the hg repo contains every file outside the src 
  directory, and that these are all up-to-date and commited into 
  the repo."
19:52 < ddrake> but perhaps patches bear a special mention, just to 
  make it clear. I'll open the ticket.
```


Issue created by migration from https://trac.sagemath.org/ticket/8104





---

archive/issue_comments_071113.json:
```json
{
    "body": "A patch addressing this issue is up at #8079.",
    "created_at": "2010-02-09T12:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8104#issuecomment-71113",
    "user": "mvngu"
}
```

A patch addressing this issue is up at #8079.



---

archive/issue_comments_071114.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-14T14:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8104#issuecomment-71114",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_071115.json:
```json
{
    "body": "Close as fixed by #8079.",
    "created_at": "2010-02-14T14:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8104#issuecomment-71115",
    "user": "mvngu"
}
```

Close as fixed by #8079.
