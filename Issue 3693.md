# Issue 3693: upgrade moinmoin to 1.7.1

Issue created by migration from https://trac.sagemath.org/ticket/3693

Original creator: was

Original creation time: 2008-07-21 07:27:31

Assignee: mabshoff

CC:  was mhansen




---

Comment by was created at 2008-07-21 07:42:04

Changing status from new to assigned.


---

Comment by was created at 2008-07-21 07:42:04

Changing assignee from mabshoff to was.


---

Comment by was created at 2008-07-21 09:55:28

Current version of spkg here:

    http://sage.math.washington.edu/home/was/patches/moin-1.7.1.spkg

The current problems:

   * moinmoin is totally broken on os x -- weird permission errors; probably related to twisted upgrade.  This was a problem with 1.5.x too, so fixing this isn't needed for this ticket, but should be fixed in another ticket.

   * jsmath typesetting doesn't work because url's like this don't work:   http://wiki.sagemath.org/wiki/jsmath/   If anybody can find a URL that works (i.e., lists files), I can make jsmath for sage work fine. 

   * We have to check that existing moinmoin installs get automatically migrated.

   * We need to change things so that (1) the default moinmoin install does *not* allow anonymous edits.  This means editing a file in patches/
   
   * We need to change things so that the default moinmoin using catchpa's since the whole point of upgrading is to get rid of spammers.


---

Attachment

I have an updated spkg at http://sage.math.washington.edu/home/mhansen/moin-1.7.1.spkg along with a new patch.

It takes care of all the issues listed above except the weird permissions errors on OS X.  The second patch is just a fairly quick version I did, and it would be good if someone else sat down and looked at it.  I tested the migration bit on a simple wiki and it worked correctly with jsMath, the textchas, etc.


---

Attachment


---

Comment by jason created at 2008-09-30 06:34:38

I applied the patches and installed the spkg and everything seemed to work fine.  I did not try to convert any wikis, though, and could not test OS X.  So consider this a positive review if those two issues are looked at by someone.


---

Comment by mabshoff created at 2008-09-30 17:46:20

Mike mentioned that we should go to 1.7.2 directly. We also need someone to test the upgrade of an existing wiki. 

Maybe we should do a backup before upgrading the wiki so that in case of a disaster no data are lost.

Cheers,

Michael


---

Comment by mhansen created at 2008-09-30 17:47:56

I've tested upgrading an existing wiki, but I guess I don't count :-)

Also, it currently does write a backup before upgrading.


---

Attachment

I posted an spkg for MoinMoin 1.7.2 here:

http://sage.math.washington.edu/home/mhansen/moin-1.7.2.spkg


---

Comment by was created at 2008-11-14 13:15:38

Hi,

I just tried this on the public sage wiki.  It "works", but has the drawback that I guess MoinMoin changed their link format, so essentially every single link (over 3000 pages of them) in the entire wiki is broken.  It would be nice if the Python code actually converted the wiki pages so they work.  As it is now, it doesn't, so anybody who upgrades to this spkg would have their entire wiki broken. 

Hopefully changing the link format can be done automatically.


---

Comment by was created at 2008-11-15 01:07:58

Mike could you post exactly what you did to very nicely fix the public sage wiki?  You did get it to work.  Thanks!


---

Comment by mabshoff created at 2008-11-20 09:20:15


```
[01:03am] mabshoff: mhansen: wstein|afk was wondering about how you converted the wiki?
[01:03am] mabshoff: I.e. the moinmoin 1.6 syntax since he wanted to convert the other wikis hosted at sagemath.org, too.
[01:04am] mhansen: There's a data migration script that needs to be run.
[01:05am] mhansen: "moin migration data --help"
[01:17am] mabshoff: mk
```



---

Attachment


---

Comment by mhansen created at 2008-12-09 03:55:42

I posted a new spkg at http://sage.math.washington.edu/home/mhansen/moin-1.7.2.spkg and made a new patch.  trac_3693-combined.patch is the only one that should be applied.


---

Comment by rlm created at 2009-02-21 01:59:29

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

Comment by mabshoff created at 2009-02-21 05:01:35

We are actually running this wiki.spkg already at sagemath.org. The failure you saw is a known OSX problem with a ticket.

Cheers,

Michael


---

Comment by rlm created at 2009-02-21 05:24:53

The `pwd` behavior is present in Linux as well. If no one else wants to, I can do the review for this ticket.


---

Comment by rlm created at 2009-02-21 05:27:33

Also, currently I have problems with pointing the directory entry at an old wiki. In sage 2.8.14, it runs fine (as long as I run it in the directory containing `sage_wiki`, that is), but the Sage 3.3 versions don't like it, probably because of it not sitting in $SAGE_ROOT or pwd or something.


---

Comment by rlm created at 2009-03-06 10:33:58

Looks very good to me.


---

Comment by mhansen created at 2009-03-06 11:09:00

After upgrading a few wiki's, I'm not sure how I feel about the automatic updates since they only sort of work.  If the user has changed the wikiconfig.py file at all.

I think I'd be more in favor of printing a list of explicit instructions for the user to follow.


---

Comment by was created at 2009-03-06 15:19:37

> I think I'd be more in favor of printing a list of explicit instructions for the user to follow. 

I'm very happy with that, as long as the instructions get tested and work.


---

Comment by rlm created at 2009-03-06 23:59:13

I have an old wiki with a modified `wikiconfig.py`.

Mike -- You should write up instructions for changing it over, and I can test it on this wiki.


---

Comment by rlm created at 2009-03-07 03:05:57

The new spkg here fixes the jsmath issue:

http://8tb.us/home/rlmill/moin-1.7.2.p0.spkg


---

Comment by was created at 2009-03-28 16:38:23

I just tried using moin-1.7.2.spkg on wiki.wstein.org and the autoupgrade process resulting in the entire wiki being massively corrupted.


---

Comment by rlm created at 2009-07-16 21:29:12

Replying to [comment:23 was]:
> I just tried using moin-1.7.2.spkg on wiki.wstein.org and the autoupgrade process resulting in the entire wiki being massively corrupted. 
> 

Making this "needs work" again, then.


---

Comment by was created at 2009-09-09 00:03:36

I change my mind!  It is stupid to not upgrade moinmoin at this point...  auto-upgrading need *not* be automatic.   That is unreasonable.   

Mike, if you can put up a new moinmoin spkg that works, even if it doesn't autoupgrade old moinmoins, I'll be happy.


---

Comment by timdumol created at 2009-09-24 12:53:58

Since the latest version of MoinMoin is now 1.8.5 (soon to be 1.9), I'm updating the summary.

Gah. I meant that as a comment.


---

Comment by was created at 2009-12-15 23:14:50

Changing priority from major to blocker.


---

Comment by timdumol created at 2009-12-20 04:55:35

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2009-12-20 04:55:35

A new spkg for moin-1.9 is at http://sage.math.washington.edu/home/timdumol/moin-1.9.0.p0.spkg. trac_3683-moinmoin-1.9.patch is the accompanying patch to the sage repo.


---

Comment by timdumol created at 2009-12-20 04:56:25

Patch for moin-1.9.p0.spkg. Apply this patch alone to sage repo.


---

Attachment


---

Comment by timdumol created at 2009-12-21 02:31:34

I forgot to note that this new spkg depends on Twisted 9.0: #7552


---

Comment by was created at 2009-12-21 22:44:06

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

Comment by was created at 2009-12-21 22:44:06

Changing status from needs_review to needs_work.


---

Attachment

Adds a `fork` argument.


---

Comment by timdumol created at 2009-12-22 04:51:02

New patch with the requested `fork` argument is now up. New package at http://sage.math.washington.edu/home/timdumol/moin-1.9.0.p0.spkg.


---

Comment by timdumol created at 2009-12-22 04:51:02

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-01-16 20:12:09

Possibly related: #1870?


---

Comment by timdumol created at 2010-01-20 06:48:14

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2010-01-20 06:48:14

1.9.1 has been released, so this should be updated to 1.9.1.


---

Comment by timdumol created at 2010-01-20 13:05:59

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-01-20 13:05:59

The package for 1.9.1 is at http://boxen.math.washignton.edu/home/timdumol/moin-1.9.1.spkg.


---

Comment by mpatel created at 2010-01-21 09:57:35

Minor formatting, docstring changes.  Replaces previous.  sage repo.


---

Attachment


---

Comment by mpatel created at 2010-01-21 10:19:38

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

Comment by mhansen created at 2010-02-07 06:22:38

mpatel's changes look fine to me.


---

Comment by mhansen created at 2010-02-07 06:22:38

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 14:24:20

Resolution: fixed
