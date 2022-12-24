# Issue 3693: upgrade moinmoin to 1.7.1

archive/issues_003693.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  was mhansen\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3693\n\n",
    "created_at": "2008-07-21T07:27:31Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "upgrade moinmoin to 1.7.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3693",
    "user": "was"
}
```
Assignee: mabshoff

CC:  was mhansen



Issue created by migration from https://trac.sagemath.org/ticket/3693





---

archive/issue_comments_026160.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-21T07:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26160",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026161.json:
```json
{
    "body": "Changing assignee from mabshoff to was.",
    "created_at": "2008-07-21T07:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26161",
    "user": "was"
}
```

Changing assignee from mabshoff to was.



---

archive/issue_comments_026162.json:
```json
{
    "body": "Current version of spkg here:\n\n    http://sage.math.washington.edu/home/was/patches/moin-1.7.1.spkg\n\nThe current problems:\n\n* moinmoin is totally broken on os x -- weird permission errors; probably related to twisted upgrade.  This was a problem with 1.5.x too, so fixing this isn't needed for this ticket, but should be fixed in another ticket.\n\n* jsmath typesetting doesn't work because url's like this don't work:   http://wiki.sagemath.org/wiki/jsmath/   If anybody can find a URL that works (i.e., lists files), I can make jsmath for sage work fine. \n\n* We have to check that existing moinmoin installs get automatically migrated.\n\n* We need to change things so that (1) the default moinmoin install does *not* allow anonymous edits.  This means editing a file in patches/\n   \n* We need to change things so that the default moinmoin using catchpa's since the whole point of upgrading is to get rid of spammers.",
    "created_at": "2008-07-21T09:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26162",
    "user": "was"
}
```

Current version of spkg here:

    http://sage.math.washington.edu/home/was/patches/moin-1.7.1.spkg

The current problems:

* moinmoin is totally broken on os x -- weird permission errors; probably related to twisted upgrade.  This was a problem with 1.5.x too, so fixing this isn't needed for this ticket, but should be fixed in another ticket.

* jsmath typesetting doesn't work because url's like this don't work:   http://wiki.sagemath.org/wiki/jsmath/   If anybody can find a URL that works (i.e., lists files), I can make jsmath for sage work fine. 

* We have to check that existing moinmoin installs get automatically migrated.

* We need to change things so that (1) the default moinmoin install does *not* allow anonymous edits.  This means editing a file in patches/
   
* We need to change things so that the default moinmoin using catchpa's since the whole point of upgrading is to get rid of spammers.



---

archive/issue_comments_026163.json:
```json
{
    "body": "Attachment [sage-3693-part1.patch](tarball://root/attachments/some-uuid/ticket3693/sage-3693-part1.patch) by mhansen created at 2008-07-22 08:55:39\n\nI have an updated spkg at http://sage.math.washington.edu/home/mhansen/moin-1.7.1.spkg along with a new patch.\n\nIt takes care of all the issues listed above except the weird permissions errors on OS X.  The second patch is just a fairly quick version I did, and it would be good if someone else sat down and looked at it.  I tested the migration bit on a simple wiki and it worked correctly with jsMath, the textchas, etc.",
    "created_at": "2008-07-22T08:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26163",
    "user": "mhansen"
}
```

Attachment [sage-3693-part1.patch](tarball://root/attachments/some-uuid/ticket3693/sage-3693-part1.patch) by mhansen created at 2008-07-22 08:55:39

I have an updated spkg at http://sage.math.washington.edu/home/mhansen/moin-1.7.1.spkg along with a new patch.

It takes care of all the issues listed above except the weird permissions errors on OS X.  The second patch is just a fairly quick version I did, and it would be good if someone else sat down and looked at it.  I tested the migration bit on a simple wiki and it worked correctly with jsMath, the textchas, etc.



---

archive/issue_comments_026164.json:
```json
{
    "body": "Attachment [trac_3693-part2.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3693-part2.patch) by mhansen created at 2008-07-22 08:57:40",
    "created_at": "2008-07-22T08:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26164",
    "user": "mhansen"
}
```

Attachment [trac_3693-part2.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3693-part2.patch) by mhansen created at 2008-07-22 08:57:40



---

archive/issue_comments_026165.json:
```json
{
    "body": "I applied the patches and installed the spkg and everything seemed to work fine.  I did not try to convert any wikis, though, and could not test OS X.  So consider this a positive review if those two issues are looked at by someone.",
    "created_at": "2008-09-30T06:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26165",
    "user": "jason"
}
```

I applied the patches and installed the spkg and everything seemed to work fine.  I did not try to convert any wikis, though, and could not test OS X.  So consider this a positive review if those two issues are looked at by someone.



---

archive/issue_comments_026166.json:
```json
{
    "body": "Mike mentioned that we should go to 1.7.2 directly. We also need someone to test the upgrade of an existing wiki. \n\nMaybe we should do a backup before upgrading the wiki so that in case of a disaster no data are lost.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-30T17:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26166",
    "user": "mabshoff"
}
```

Mike mentioned that we should go to 1.7.2 directly. We also need someone to test the upgrade of an existing wiki. 

Maybe we should do a backup before upgrading the wiki so that in case of a disaster no data are lost.

Cheers,

Michael



---

archive/issue_comments_026167.json:
```json
{
    "body": "I've tested upgrading an existing wiki, but I guess I don't count :-)\n\nAlso, it currently does write a backup before upgrading.",
    "created_at": "2008-09-30T17:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26167",
    "user": "mhansen"
}
```

I've tested upgrading an existing wiki, but I guess I don't count :-)

Also, it currently does write a backup before upgrading.



---

archive/issue_comments_026168.json:
```json
{
    "body": "Attachment [trac_3693-part3.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3693-part3.patch) by mhansen created at 2008-10-02 08:13:57\n\nI posted an spkg for MoinMoin 1.7.2 here:\n\nhttp://sage.math.washington.edu/home/mhansen/moin-1.7.2.spkg",
    "created_at": "2008-10-02T08:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26168",
    "user": "mhansen"
}
```

Attachment [trac_3693-part3.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3693-part3.patch) by mhansen created at 2008-10-02 08:13:57

I posted an spkg for MoinMoin 1.7.2 here:

http://sage.math.washington.edu/home/mhansen/moin-1.7.2.spkg



---

archive/issue_comments_026169.json:
```json
{
    "body": "Hi,\n\nI just tried this on the public sage wiki.  It \"works\", but has the drawback that I guess MoinMoin changed their link format, so essentially every single link (over 3000 pages of them) in the entire wiki is broken.  It would be nice if the Python code actually converted the wiki pages so they work.  As it is now, it doesn't, so anybody who upgrades to this spkg would have their entire wiki broken. \n\nHopefully changing the link format can be done automatically.",
    "created_at": "2008-11-14T13:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26169",
    "user": "was"
}
```

Hi,

I just tried this on the public sage wiki.  It "works", but has the drawback that I guess MoinMoin changed their link format, so essentially every single link (over 3000 pages of them) in the entire wiki is broken.  It would be nice if the Python code actually converted the wiki pages so they work.  As it is now, it doesn't, so anybody who upgrades to this spkg would have their entire wiki broken. 

Hopefully changing the link format can be done automatically.



---

archive/issue_comments_026170.json:
```json
{
    "body": "Mike could you post exactly what you did to very nicely fix the public sage wiki?  You did get it to work.  Thanks!",
    "created_at": "2008-11-15T01:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26170",
    "user": "was"
}
```

Mike could you post exactly what you did to very nicely fix the public sage wiki?  You did get it to work.  Thanks!



---

archive/issue_comments_026171.json:
```json
{
    "body": "\n```\n[01:03am] mabshoff: mhansen: wstein|afk was wondering about how you converted the wiki?\n[01:03am] mabshoff: I.e. the moinmoin 1.6 syntax since he wanted to convert the other wikis hosted at sagemath.org, too.\n[01:04am] mhansen: There's a data migration script that needs to be run.\n[01:05am] mhansen: \"moin migration data --help\"\n[01:17am] mabshoff: mk\n```\n",
    "created_at": "2008-11-20T09:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26171",
    "user": "mabshoff"
}
```


```
[01:03am] mabshoff: mhansen: wstein|afk was wondering about how you converted the wiki?
[01:03am] mabshoff: I.e. the moinmoin 1.6 syntax since he wanted to convert the other wikis hosted at sagemath.org, too.
[01:04am] mhansen: There's a data migration script that needs to be run.
[01:05am] mhansen: "moin migration data --help"
[01:17am] mabshoff: mk
```




---

archive/issue_comments_026172.json:
```json
{
    "body": "Attachment [trac_3693-combined.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3693-combined.patch) by mhansen created at 2008-12-09 03:54:38",
    "created_at": "2008-12-09T03:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26172",
    "user": "mhansen"
}
```

Attachment [trac_3693-combined.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3693-combined.patch) by mhansen created at 2008-12-09 03:54:38



---

archive/issue_comments_026173.json:
```json
{
    "body": "I posted a new spkg at http://sage.math.washington.edu/home/mhansen/moin-1.7.2.spkg and made a new patch.  trac_3693-combined.patch is the only one that should be applied.",
    "created_at": "2008-12-09T03:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26173",
    "user": "mhansen"
}
```

I posted a new spkg at http://sage.math.washington.edu/home/mhansen/moin-1.7.2.spkg and made a new patch.  trac_3693-combined.patch is the only one that should be applied.



---

archive/issue_comments_026174.json:
```json
{
    "body": "Has anyone looked at mhansen's spkg or patch yet? The current state of moinmoin in Sage is pretty sad:\n\n\n```\n$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: pwd\n'/Users/rlmill/sage-3.3.rc2'\nsage: wiki()\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:9000 *\n*                                                *\n**************************************************\nRemoving stale pidfile /Users/rlmill/sage-3.3.rc2/sage_wiki/twistd.pid\n2009-02-20 17:57:31-0800 [-] Log opened.\n2009-02-20 17:57:31-0800 [-] twistd 8.1.0 (/Users/rlmill/sage-3.3.rc2/local/bin/python 2.5.2) starting up\n2009-02-20 17:57:31-0800 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>\n2009-02-20 17:57:31-0800 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9000\n2009-02-20 17:57:31-0800 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x11b5a08>\n2009-02-20 17:57:31-0800 [-] Traceback (most recent call last):\n2009-02-20 17:57:31-0800 [-]   File \"/Users/rlmill/sage-3.3.rc2/local/bin/twistd\", line 21, in <module>\n2009-02-20 17:57:31-0800 [-]     run()\n2009-02-20 17:57:31-0800 [-]   File \"/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/scripts/twistd.py\", line 27, in run\n2009-02-20 17:57:31-0800 [-]     app.run(runApp, ServerOptions)\n2009-02-20 17:57:31-0800 [-]   File \"/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/application/app.py\", line 614, in run\n2009-02-20 17:57:31-0800 [-]     runApp(config)\n2009-02-20 17:57:31-0800 [-]   File \"/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/scripts/twistd.py\", line 23, in runApp\n2009-02-20 17:57:31-0800 [-]     _SomeApplicationRunner(config).run()\n2009-02-20 17:57:31-0800 [-]   File \"/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/application/app.py\", line 337, in run\n2009-02-20 17:57:31-0800 [-]     self.postApplication()\n2009-02-20 17:57:31-0800 [-]   File \"/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/scripts/_twistd_unix.py\", line 207, in postApplication\n2009-02-20 17:57:31-0800 [-]     self.startApplication(self.application)\n2009-02-20 17:57:31-0800 [-]   File \"/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/scripts/_twistd_unix.py\", line 309, in startApplication\n2009-02-20 17:57:31-0800 [-]     self.shedPrivileges(self.config['euid'], uid, gid)\n2009-02-20 17:57:31-0800 [-]   File \"/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/scripts/_twistd_unix.py\", line 281, in shedPrivileges\n2009-02-20 17:57:31-0800 [-]     switchUID(uid, gid, euid)\n2009-02-20 17:57:31-0800 [-]   File \"/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/python/util.py\", line 664, in switchUID\n2009-02-20 17:57:31-0800 [-]     initgroups(uid, gid)\n2009-02-20 17:57:31-0800 [-]   File \"/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/python/util.py\", line 641, in initgroups\n2009-02-20 17:57:31-0800 [-]     _setgroups_until_success(l)\n2009-02-20 17:57:31-0800 [-]   File \"/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/python/util.py\", line 587, in _setgroups_until_success\n2009-02-20 17:57:31-0800 [-]     setgroups(l)\n2009-02-20 17:57:31-0800 [-] OSError: [Errno 1] Operation not permitted\nTrue\nsage: pwd\n'/Users/rlmill/sage-3.3.rc2/sage_wiki'\nsage: exit\nExiting SAGE (CPU time 0m0.08s, Wall time 0m14.13s).\n```\n",
    "created_at": "2009-02-21T01:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26174",
    "user": "rlm"
}
```

Has anyone looked at mhansen's spkg or patch yet? The current state of moinmoin in Sage is pretty sad:


```
$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: pwd
'/Users/rlmill/sage-3.3.rc2'
sage: wiki()
**************************************************
*                                                *
* Open your web browser to http://localhost:9000 *
*                                                *
**************************************************
Removing stale pidfile /Users/rlmill/sage-3.3.rc2/sage_wiki/twistd.pid
2009-02-20 17:57:31-0800 [-] Log opened.
2009-02-20 17:57:31-0800 [-] twistd 8.1.0 (/Users/rlmill/sage-3.3.rc2/local/bin/python 2.5.2) starting up
2009-02-20 17:57:31-0800 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2009-02-20 17:57:31-0800 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9000
2009-02-20 17:57:31-0800 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x11b5a08>
2009-02-20 17:57:31-0800 [-] Traceback (most recent call last):
2009-02-20 17:57:31-0800 [-]   File "/Users/rlmill/sage-3.3.rc2/local/bin/twistd", line 21, in <module>
2009-02-20 17:57:31-0800 [-]     run()
2009-02-20 17:57:31-0800 [-]   File "/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/scripts/twistd.py", line 27, in run
2009-02-20 17:57:31-0800 [-]     app.run(runApp, ServerOptions)
2009-02-20 17:57:31-0800 [-]   File "/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/application/app.py", line 614, in run
2009-02-20 17:57:31-0800 [-]     runApp(config)
2009-02-20 17:57:31-0800 [-]   File "/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/scripts/twistd.py", line 23, in runApp
2009-02-20 17:57:31-0800 [-]     _SomeApplicationRunner(config).run()
2009-02-20 17:57:31-0800 [-]   File "/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/application/app.py", line 337, in run
2009-02-20 17:57:31-0800 [-]     self.postApplication()
2009-02-20 17:57:31-0800 [-]   File "/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/scripts/_twistd_unix.py", line 207, in postApplication
2009-02-20 17:57:31-0800 [-]     self.startApplication(self.application)
2009-02-20 17:57:31-0800 [-]   File "/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/scripts/_twistd_unix.py", line 309, in startApplication
2009-02-20 17:57:31-0800 [-]     self.shedPrivileges(self.config['euid'], uid, gid)
2009-02-20 17:57:31-0800 [-]   File "/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/scripts/_twistd_unix.py", line 281, in shedPrivileges
2009-02-20 17:57:31-0800 [-]     switchUID(uid, gid, euid)
2009-02-20 17:57:31-0800 [-]   File "/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/python/util.py", line 664, in switchUID
2009-02-20 17:57:31-0800 [-]     initgroups(uid, gid)
2009-02-20 17:57:31-0800 [-]   File "/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/python/util.py", line 641, in initgroups
2009-02-20 17:57:31-0800 [-]     _setgroups_until_success(l)
2009-02-20 17:57:31-0800 [-]   File "/Users/rlmill/sage-3.3.rc2/local/lib/python2.5/site-packages/twisted/python/util.py", line 587, in _setgroups_until_success
2009-02-20 17:57:31-0800 [-]     setgroups(l)
2009-02-20 17:57:31-0800 [-] OSError: [Errno 1] Operation not permitted
True
sage: pwd
'/Users/rlmill/sage-3.3.rc2/sage_wiki'
sage: exit
Exiting SAGE (CPU time 0m0.08s, Wall time 0m14.13s).
```




---

archive/issue_comments_026175.json:
```json
{
    "body": "We are actually running this wiki.spkg already at sagemath.org. The failure you saw is a known OSX problem with a ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-21T05:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26175",
    "user": "mabshoff"
}
```

We are actually running this wiki.spkg already at sagemath.org. The failure you saw is a known OSX problem with a ticket.

Cheers,

Michael



---

archive/issue_comments_026176.json:
```json
{
    "body": "The `pwd` behavior is present in Linux as well. If no one else wants to, I can do the review for this ticket.",
    "created_at": "2009-02-21T05:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26176",
    "user": "rlm"
}
```

The `pwd` behavior is present in Linux as well. If no one else wants to, I can do the review for this ticket.



---

archive/issue_comments_026177.json:
```json
{
    "body": "Also, currently I have problems with pointing the directory entry at an old wiki. In sage 2.8.14, it runs fine (as long as I run it in the directory containing `sage_wiki`, that is), but the Sage 3.3 versions don't like it, probably because of it not sitting in $SAGE_ROOT or pwd or something.",
    "created_at": "2009-02-21T05:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26177",
    "user": "rlm"
}
```

Also, currently I have problems with pointing the directory entry at an old wiki. In sage 2.8.14, it runs fine (as long as I run it in the directory containing `sage_wiki`, that is), but the Sage 3.3 versions don't like it, probably because of it not sitting in $SAGE_ROOT or pwd or something.



---

archive/issue_comments_026178.json:
```json
{
    "body": "Looks very good to me.",
    "created_at": "2009-03-06T10:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26178",
    "user": "rlm"
}
```

Looks very good to me.



---

archive/issue_comments_026179.json:
```json
{
    "body": "After upgrading a few wiki's, I'm not sure how I feel about the automatic updates since they only sort of work.  If the user has changed the wikiconfig.py file at all.\n\nI think I'd be more in favor of printing a list of explicit instructions for the user to follow.",
    "created_at": "2009-03-06T11:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26179",
    "user": "mhansen"
}
```

After upgrading a few wiki's, I'm not sure how I feel about the automatic updates since they only sort of work.  If the user has changed the wikiconfig.py file at all.

I think I'd be more in favor of printing a list of explicit instructions for the user to follow.



---

archive/issue_comments_026180.json:
```json
{
    "body": "> I think I'd be more in favor of printing a list of explicit instructions for the user to follow. \n\nI'm very happy with that, as long as the instructions get tested and work.",
    "created_at": "2009-03-06T15:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26180",
    "user": "was"
}
```

> I think I'd be more in favor of printing a list of explicit instructions for the user to follow. 

I'm very happy with that, as long as the instructions get tested and work.



---

archive/issue_comments_026181.json:
```json
{
    "body": "I have an old wiki with a modified `wikiconfig.py`.\n\nMike -- You should write up instructions for changing it over, and I can test it on this wiki.",
    "created_at": "2009-03-06T23:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26181",
    "user": "rlm"
}
```

I have an old wiki with a modified `wikiconfig.py`.

Mike -- You should write up instructions for changing it over, and I can test it on this wiki.



---

archive/issue_comments_026182.json:
```json
{
    "body": "The new spkg here fixes the jsmath issue:\n\nhttp://8tb.us/home/rlmill/moin-1.7.2.p0.spkg",
    "created_at": "2009-03-07T03:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26182",
    "user": "rlm"
}
```

The new spkg here fixes the jsmath issue:

http://8tb.us/home/rlmill/moin-1.7.2.p0.spkg



---

archive/issue_comments_026183.json:
```json
{
    "body": "I just tried using moin-1.7.2.spkg on wiki.wstein.org and the autoupgrade process resulting in the entire wiki being massively corrupted.",
    "created_at": "2009-03-28T16:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26183",
    "user": "was"
}
```

I just tried using moin-1.7.2.spkg on wiki.wstein.org and the autoupgrade process resulting in the entire wiki being massively corrupted.



---

archive/issue_comments_026184.json:
```json
{
    "body": "Replying to [comment:23 was]:\n> I just tried using moin-1.7.2.spkg on wiki.wstein.org and the autoupgrade process resulting in the entire wiki being massively corrupted. \n> \n\nMaking this \"needs work\" again, then.",
    "created_at": "2009-07-16T21:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26184",
    "user": "rlm"
}
```

Replying to [comment:23 was]:
> I just tried using moin-1.7.2.spkg on wiki.wstein.org and the autoupgrade process resulting in the entire wiki being massively corrupted. 
> 

Making this "needs work" again, then.



---

archive/issue_comments_026185.json:
```json
{
    "body": "I change my mind!  It is stupid to not upgrade moinmoin at this point...  auto-upgrading need *not* be automatic.   That is unreasonable.   \n\nMike, if you can put up a new moinmoin spkg that works, even if it doesn't autoupgrade old moinmoins, I'll be happy.",
    "created_at": "2009-09-09T00:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26185",
    "user": "was"
}
```

I change my mind!  It is stupid to not upgrade moinmoin at this point...  auto-upgrading need *not* be automatic.   That is unreasonable.   

Mike, if you can put up a new moinmoin spkg that works, even if it doesn't autoupgrade old moinmoins, I'll be happy.



---

archive/issue_comments_026186.json:
```json
{
    "body": "Since the latest version of MoinMoin is now 1.8.5 (soon to be 1.9), I'm updating the summary.\n\nGah. I meant that as a comment.",
    "created_at": "2009-09-24T12:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26186",
    "user": "timdumol"
}
```

Since the latest version of MoinMoin is now 1.8.5 (soon to be 1.9), I'm updating the summary.

Gah. I meant that as a comment.



---

archive/issue_comments_026187.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-12-15T23:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26187",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_026188.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-20T04:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26188",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_026189.json:
```json
{
    "body": "A new spkg for moin-1.9 is at http://sage.math.washington.edu/home/timdumol/moin-1.9.0.p0.spkg. trac_3683-moinmoin-1.9.patch is the accompanying patch to the sage repo.",
    "created_at": "2009-12-20T04:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26189",
    "user": "timdumol"
}
```

A new spkg for moin-1.9 is at http://sage.math.washington.edu/home/timdumol/moin-1.9.0.p0.spkg. trac_3683-moinmoin-1.9.patch is the accompanying patch to the sage repo.



---

archive/issue_comments_026190.json:
```json
{
    "body": "Patch for moin-1.9.p0.spkg. Apply this patch alone to sage repo.",
    "created_at": "2009-12-20T04:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26190",
    "user": "timdumol"
}
```

Patch for moin-1.9.p0.spkg. Apply this patch alone to sage repo.



---

archive/issue_comments_026191.json:
```json
{
    "body": "Attachment [trac_3683-moinmoin-1.9.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3683-moinmoin-1.9.patch) by timdumol created at 2009-12-20 12:11:58",
    "created_at": "2009-12-20T12:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26191",
    "user": "timdumol"
}
```

Attachment [trac_3683-moinmoin-1.9.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3683-moinmoin-1.9.patch) by timdumol created at 2009-12-20 12:11:58



---

archive/issue_comments_026192.json:
```json
{
    "body": "I forgot to note that this new spkg depends on Twisted 9.0: #7552",
    "created_at": "2009-12-21T02:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26192",
    "user": "timdumol"
}
```

I forgot to note that this new spkg depends on Twisted 9.0: #7552



---

archive/issue_comments_026193.json:
```json
{
    "body": "1.  Notice the ? below; we need to add mointwisted.py to the hg repo in the spkg.\n\n```\nwstein@sage:~/build/referee/sage-4.3.rc0/moin-1.9.0.p0$              hg status\nM patches/wikiconfig.py\nM spkg-install\n? patches/mointwisted.py\n```\n\n\n\nThe actual wiki command is confusing because it now runs as a daemon instead of blocking.  This is highly confusing, mainly because it is exactly the opposite behavior as the notebook command.\n\n```\nsage: wiki(address=\"\")\n...\n2009-12-21 14:37:36,095 WARNING MoinMoin.log:139 using logging configuration read from built-in fallback in MoinMoin.log module!\nsage:\n```\n\nI.e.., I immediately got a prompt back.\nThis is especially bad because once I exit sage the moin wiki is left running:\n\n```\nwstein@sage:~/build/referee/sage-4.3.rc0$ ps ax |grep moin\n 4012 ?        Sl     0:00 python /scratch/wstein/build/referee/sage-4.3.rc0/local/bin/twistd moin -p 9000 -a \n 4021 pts/135  S+     0:00 grep moin\n```\n\nWith the notebook we have two (unfortunately undocumented) options:\n\n```\n             fork = False,\n             quiet = False\n```\n\n\nI think they do basically what you've main moin do by default.   So I would like to request that you keep the current capability, but make it non-default.  Use the fork= option to control what happens.",
    "created_at": "2009-12-21T22:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26193",
    "user": "was"
}
```

1.  Notice the ? below; we need to add mointwisted.py to the hg repo in the spkg.

```
wstein@sage:~/build/referee/sage-4.3.rc0/moin-1.9.0.p0$              hg status
M patches/wikiconfig.py
M spkg-install
? patches/mointwisted.py
```



The actual wiki command is confusing because it now runs as a daemon instead of blocking.  This is highly confusing, mainly because it is exactly the opposite behavior as the notebook command.

```
sage: wiki(address="")
...
2009-12-21 14:37:36,095 WARNING MoinMoin.log:139 using logging configuration read from built-in fallback in MoinMoin.log module!
sage:
```

I.e.., I immediately got a prompt back.
This is especially bad because once I exit sage the moin wiki is left running:

```
wstein@sage:~/build/referee/sage-4.3.rc0$ ps ax |grep moin
 4012 ?        Sl     0:00 python /scratch/wstein/build/referee/sage-4.3.rc0/local/bin/twistd moin -p 9000 -a 
 4021 pts/135  S+     0:00 grep moin
```

With the notebook we have two (unfortunately undocumented) options:

```
             fork = False,
             quiet = False
```


I think they do basically what you've main moin do by default.   So I would like to request that you keep the current capability, but make it non-default.  Use the fork= option to control what happens.



---

archive/issue_comments_026194.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-21T22:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26194",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_026195.json:
```json
{
    "body": "Attachment [trac_3683-moinmoin-1.9.2.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3683-moinmoin-1.9.2.patch) by timdumol created at 2009-12-22 04:50:18\n\nAdds a `fork` argument.",
    "created_at": "2009-12-22T04:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26195",
    "user": "timdumol"
}
```

Attachment [trac_3683-moinmoin-1.9.2.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3683-moinmoin-1.9.2.patch) by timdumol created at 2009-12-22 04:50:18

Adds a `fork` argument.



---

archive/issue_comments_026196.json:
```json
{
    "body": "New patch with the requested `fork` argument is now up. New package at http://sage.math.washington.edu/home/timdumol/moin-1.9.0.p0.spkg.",
    "created_at": "2009-12-22T04:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26196",
    "user": "timdumol"
}
```

New patch with the requested `fork` argument is now up. New package at http://sage.math.washington.edu/home/timdumol/moin-1.9.0.p0.spkg.



---

archive/issue_comments_026197.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-22T04:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26197",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_026198.json:
```json
{
    "body": "Possibly related: #1870?",
    "created_at": "2010-01-16T20:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26198",
    "user": "mpatel"
}
```

Possibly related: #1870?



---

archive/issue_comments_026199.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T06:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26199",
    "user": "timdumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_026200.json:
```json
{
    "body": "1.9.1 has been released, so this should be updated to 1.9.1.",
    "created_at": "2010-01-20T06:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26200",
    "user": "timdumol"
}
```

1.9.1 has been released, so this should be updated to 1.9.1.



---

archive/issue_comments_026201.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T13:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26201",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_026202.json:
```json
{
    "body": "The package for 1.9.1 is at http://boxen.math.washignton.edu/home/timdumol/moin-1.9.1.spkg.",
    "created_at": "2010-01-20T13:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26202",
    "user": "timdumol"
}
```

The package for 1.9.1 is at http://boxen.math.washignton.edu/home/timdumol/moin-1.9.1.spkg.



---

archive/issue_comments_026203.json:
```json
{
    "body": "Minor formatting, docstring changes.  Replaces previous.  sage repo.",
    "created_at": "2010-01-21T09:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26203",
    "user": "mpatel"
}
```

Minor formatting, docstring changes.  Replaces previous.  sage repo.



---

archive/issue_comments_026204.json:
```json
{
    "body": "Attachment [trac_3683-upgrade_moinmoin.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3683-upgrade_moinmoin.patch) by mpatel created at 2010-01-21 10:03:23",
    "created_at": "2010-01-21T10:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26204",
    "user": "mpatel"
}
```

Attachment [trac_3683-upgrade_moinmoin.patch](tarball://root/attachments/some-uuid/ticket3693/trac_3683-upgrade_moinmoin.patch) by mpatel created at 2010-01-21 10:03:23



---

archive/issue_comments_026205.json:
```json
{
    "body": "The [attachment:trac_3683-upgrade_moinmoin.patch updated patch]\n\n* Untabifies `moin.py`.\n* Adds a missing `INPUT` block.\n* Adds the note about upgrading existing MoinMoin wikis.\n\nThe [updated spkg](http://boxen.math.washington.edu/home/mpatel/trac/3693/moin-1.9.1.p1.spkg)\n\n* Includes jsMath.\n* Commits an uncommitted file.\n* Fixes the [GUI editor](http://ckeditor.com/).  The jsMath parser was the problem.\n  * Maybe we can use the same fix for the [Sage wiki](http://wiki.sagemath.org/)?\n  * For another ticket:  Keep MoinMoin from stripping `$`s from GUI mode.\n* Uses Sage's `easy/load.js` to load/configure jsMath.  This adds `\\QQ`, `\\Bold{}`, etc.\n\nPositive review, but someone should review my changes.",
    "created_at": "2010-01-21T10:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26205",
    "user": "mpatel"
}
```

The [attachment:trac_3683-upgrade_moinmoin.patch updated patch]

* Untabifies `moin.py`.
* Adds a missing `INPUT` block.
* Adds the note about upgrading existing MoinMoin wikis.

The [updated spkg](http://boxen.math.washington.edu/home/mpatel/trac/3693/moin-1.9.1.p1.spkg)

* Includes jsMath.
* Commits an uncommitted file.
* Fixes the [GUI editor](http://ckeditor.com/).  The jsMath parser was the problem.
  * Maybe we can use the same fix for the [Sage wiki](http://wiki.sagemath.org/)?
  * For another ticket:  Keep MoinMoin from stripping `$`s from GUI mode.
* Uses Sage's `easy/load.js` to load/configure jsMath.  This adds `\QQ`, `\Bold{}`, etc.

Positive review, but someone should review my changes.



---

archive/issue_comments_026206.json:
```json
{
    "body": "mpatel's changes look fine to me.",
    "created_at": "2010-02-07T06:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26206",
    "user": "mhansen"
}
```

mpatel's changes look fine to me.



---

archive/issue_comments_026207.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-07T06:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26207",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_026208.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3693#issuecomment-26208",
    "user": "mpatel"
}
```

Resolution: fixed
