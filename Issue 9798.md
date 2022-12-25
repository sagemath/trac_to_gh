# Issue 9798: Running "make" in SAGE_ROOT returns the wrong exit code, leading to all kinds of confusion

archive/issues_009798.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @nexttime @jdemeyer drkirkby @kiwifb\n\nThis line in SAGE_ROOT/make\n\n```\ncd spkg && ./install all 2>&1 | tee -a ../install.log\n```\n\nwill *always* return an exit status of 0, even if the build fails miserably.  This leads to much confusion down the line, as explained in this sage-devel post:\n    \n   \nThe fix is probably to do what is described here:\n\n \n      http://www.unix.com/shell-programming-scripting/92163-command-does-not-return-exit-status-due-tee.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/9799\n\n",
    "created_at": "2010-08-25T01:01:15Z",
    "labels": [
        "component: build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Running \"make\" in SAGE_ROOT returns the wrong exit code, leading to all kinds of confusion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9798",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber

CC:  @nexttime @jdemeyer drkirkby @kiwifb

This line in SAGE_ROOT/make

```
cd spkg && ./install all 2>&1 | tee -a ../install.log
```

will *always* return an exit status of 0, even if the build fails miserably.  This leads to much confusion down the line, as explained in this sage-devel post:
    
   
The fix is probably to do what is described here:

 
      http://www.unix.com/shell-programming-scripting/92163-command-does-not-return-exit-status-due-tee.html

Issue created by migration from https://trac.sagemath.org/ticket/9799





---

archive/issue_comments_096094.json:
```json
{
    "body": "I think we already have nearly all we need in\n\n`SAGE_ROOT/spkg/pipestatus`\n\nwhich we use often in \n\n`SAGE_ROOT/spkg/standard/deps`\n\nFor upgrades from Sage versions without `pipestatus`:  What if we create `pipestatus` in the `makefile` instead of in `spkg/install`?\n\nLeif mentioned using `pipestatus` or the equivalent in the `makefile` [comment:ticket:9528:19 here].",
    "created_at": "2010-08-25T02:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96094",
    "user": "https://github.com/qed777"
}
```

I think we already have nearly all we need in

`SAGE_ROOT/spkg/pipestatus`

which we use often in 

`SAGE_ROOT/spkg/standard/deps`

For upgrades from Sage versions without `pipestatus`:  What if we create `pipestatus` in the `makefile` instead of in `spkg/install`?

Leif mentioned using `pipestatus` or the equivalent in the `makefile` [comment:ticket:9528:19 here].



---

archive/issue_comments_096095.json:
```json
{
    "body": "Well, if we could merge #9433, then I think that pipestatus would get installed through the upgrade process.",
    "created_at": "2010-08-25T04:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96095",
    "user": "https://github.com/jhpalmieri"
}
```

Well, if we could merge #9433, then I think that pipestatus would get installed through the upgrade process.



---

archive/issue_comments_096096.json:
```json
{
    "body": "> For upgrades from Sage versions without pipestatus: What if we create pipestatus in the makefile instead of in spkg/install?\n\nI may be wrong about this, but if you run \"sage -upgrade\", then I don't think \"makefile\" gets upgraded.  So if we just modify makefile, we can assume that we have pipestatus available to us: people upgrading won't get the new makefile, and people building from scratch will have spkg/pipestatus.\n\nSo I'm attaching a new makefile and corresponding makefile.diff.  I'm far from an expert at writing makefiles, so there are probably cleaner ways to do this.",
    "created_at": "2010-09-13T05:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96096",
    "user": "https://github.com/jhpalmieri"
}
```

> For upgrades from Sage versions without pipestatus: What if we create pipestatus in the makefile instead of in spkg/install?

I may be wrong about this, but if you run "sage -upgrade", then I don't think "makefile" gets upgraded.  So if we just modify makefile, we can assume that we have pipestatus available to us: people upgrading won't get the new makefile, and people building from scratch will have spkg/pipestatus.

So I'm attaching a new makefile and corresponding makefile.diff.  I'm far from an expert at writing makefiles, so there are probably cleaner ways to do this.



---

archive/issue_comments_096097.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-13T05:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96097",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096098.json:
```json
{
    "body": "Attachment [makefile.diff](tarball://root/attachments/some-uuid/ticket9799/makefile.diff) by @jhpalmieri created at 2010-09-13 05:45:38",
    "created_at": "2010-09-13T05:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96098",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [makefile.diff](tarball://root/attachments/some-uuid/ticket9799/makefile.diff) by @jhpalmieri created at 2010-09-13 05:45:38



---

archive/issue_comments_096099.json:
```json
{
    "body": "Not yet tested, but the changes so far look ok to me.\n\nI'd add dependencies on `spkg/pipestatus`, and perhaps a rule / receipt that makes sure it is (present and) executable. (More of such dependencies could be added as well.)\n\nPerhaps substitute\n\n```sh\n        cd spkg && ./pipestatus \"./install all 2>&1\" \"tee -a ../install.log\"\n```\n\nby\n\n```sh\n        spkg/pipestatus \"cd spkg && ./install all 2>&1\" \"tee -a install.log\"\n```\n\nand, optionally, use a Make variable for `spkg/pipestatus`.\n\nSome changes we should also make:\n* `distclean` should **depend** on `clean`, not **call** `make` (if at all, `$(MAKE)`).\n* The dependency of `all` on `build` is redundant.\n* `s/Deleted/Deleting/g` or move those messages. \n* `makefile` is not a phony target.\n* `./sage -b` is not consistently performed, and btw. **after** the documentation has been built / updated. Another target and dependency on that would be better.\n* Targets `testoptional` (logfile `testall.log`) and `ptestall` (logfile `ptest.log`!) are inconsistent.",
    "created_at": "2010-09-13T09:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96099",
    "user": "https://github.com/nexttime"
}
```

Not yet tested, but the changes so far look ok to me.

I'd add dependencies on `spkg/pipestatus`, and perhaps a rule / receipt that makes sure it is (present and) executable. (More of such dependencies could be added as well.)

Perhaps substitute

```sh
        cd spkg && ./pipestatus "./install all 2>&1" "tee -a ../install.log"
```

by

```sh
        spkg/pipestatus "cd spkg && ./install all 2>&1" "tee -a install.log"
```

and, optionally, use a Make variable for `spkg/pipestatus`.

Some changes we should also make:
* `distclean` should **depend** on `clean`, not **call** `make` (if at all, `$(MAKE)`).
* The dependency of `all` on `build` is redundant.
* `s/Deleted/Deleting/g` or move those messages. 
* `makefile` is not a phony target.
* `./sage -b` is not consistently performed, and btw. **after** the documentation has been built / updated. Another target and dependency on that would be better.
* Targets `testoptional` (logfile `testall.log`) and `ptestall` (logfile `ptest.log`!) are inconsistent.



---

archive/issue_comments_096100.json:
```json
{
    "body": "Attachment [makefile.9799-ll-v2](tarball://root/attachments/some-uuid/ticket9799/makefile.9799-ll-v2) by @nexttime created at 2010-09-13 15:05:32\n\nRevised version of John's Makefile, with many of the other changes I mentioned.",
    "created_at": "2010-09-13T15:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96100",
    "user": "https://github.com/nexttime"
}
```

Attachment [makefile.9799-ll-v2](tarball://root/attachments/some-uuid/ticket9799/makefile.9799-ll-v2) by @nexttime created at 2010-09-13 15:05:32

Revised version of John's Makefile, with many of the other changes I mentioned.



---

archive/issue_comments_096101.json:
```json
{
    "body": "Diff between John's and my Makefile.",
    "created_at": "2010-09-13T15:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96101",
    "user": "https://github.com/nexttime"
}
```

Diff between John's and my Makefile.



---

archive/issue_comments_096102.json:
```json
{
    "body": "Attachment [makefile.jhp-ll-v2.diff](tarball://root/attachments/some-uuid/ticket9799/makefile.jhp-ll-v2.diff) by @nexttime created at 2010-09-13 15:43:50\n\nI've attached a modified version of John's Makefile, and a corresponding diff.\n\nNot yet *very much* tested, but *should* work... ;-)\n\nCeterum censeo makefile esse renominandum[?] (i.e. **M**akefile)",
    "created_at": "2010-09-13T15:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96102",
    "user": "https://github.com/nexttime"
}
```

Attachment [makefile.jhp-ll-v2.diff](tarball://root/attachments/some-uuid/ticket9799/makefile.jhp-ll-v2.diff) by @nexttime created at 2010-09-13 15:43:50

I've attached a modified version of John's Makefile, and a corresponding diff.

Not yet *very much* tested, but *should* work... ;-)

Ceterum censeo makefile esse renominandum[?] (i.e. **M**akefile)



---

archive/issue_comments_096103.json:
```json
{
    "body": "Oh, `testall` and `ptestoptional` should also be added to the phony targets.\n\n(I only added `ptest`, which was missing, and removed `makefile`.)",
    "created_at": "2010-09-13T16:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96103",
    "user": "https://github.com/nexttime"
}
```

Oh, `testall` and `ptestoptional` should also be added to the phony targets.

(I only added `ptest`, which was missing, and removed `makefile`.)



---

archive/issue_comments_096104.json:
```json
{
    "body": "I've tested this a little bit, and it basically seems to work for me.  I also have no objections to renaming it `Makefile`.  (If it does get renamed, then #9433 will need to be changed accordingly.)  I'm attaching version 3; this just adds Leif's requested phony targets, plus changes some tabs to spaces.  With the tabs, I see this at the start of the build:\n\n```\n(sage-4.5.3) [10:58]$ make\n# Note that (currently) \"tee\" will be run in the directory cd'ed to\n# in pipestatus' first argument, i.e. \"spkg/\": \nspkg/pipestatus \"cd spkg && ./install all 2>&1\" \"tee -a ../install.log\"\n```\n\nWith spaces instead, the lines starting with \"#\" do not appear.",
    "created_at": "2010-09-13T18:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96104",
    "user": "https://github.com/jhpalmieri"
}
```

I've tested this a little bit, and it basically seems to work for me.  I also have no objections to renaming it `Makefile`.  (If it does get renamed, then #9433 will need to be changed accordingly.)  I'm attaching version 3; this just adds Leif's requested phony targets, plus changes some tabs to spaces.  With the tabs, I see this at the start of the build:

```
(sage-4.5.3) [10:58]$ make
# Note that (currently) "tee" will be run in the directory cd'ed to
# in pipestatus' first argument, i.e. "spkg/": 
spkg/pipestatus "cd spkg && ./install all 2>&1" "tee -a ../install.log"
```

With spaces instead, the lines starting with "#" do not appear.



---

archive/issue_comments_096105.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> I've tested this a little bit, and it basically seems to work for me.  I also have no objections to renaming it `Makefile`.\n\nFine.\n\n> (If it does get renamed, then #9433 will need to be changed accordingly.)\n\nYes, that's already recorded there.\n\n> I'm attaching version 3; this just adds Leif's requested phony targets,\n\nThanks.\n\n> plus changes some tabs to spaces.  With the tabs, I see this at the start of the build:\n\n```\n(sage-4.5.3) [10:58]$ make\n# Note that (currently) \"tee\" will be run in the directory cd'ed to\n# in pipestatus' first argument, i.e. \"spkg/\": \nspkg/pipestatus \"cd spkg && ./install all 2>&1\" \"tee -a ../install.log\"\n```\n\n\nWell, that's (just) informational and does no harm... ;-)\n\n> With spaces instead, the lines starting with \"#\" do not appear.\n\nI'm currently not that sure that would be very portable; instead, you could also prepend ``@`` (to `#`, and leave the tabs). The comments were actually *shell* comments (i.e., part of the receipt) rather than Makefile comments.",
    "created_at": "2010-09-13T18:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96105",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:8 jhpalmieri]:
> I've tested this a little bit, and it basically seems to work for me.  I also have no objections to renaming it `Makefile`.

Fine.

> (If it does get renamed, then #9433 will need to be changed accordingly.)

Yes, that's already recorded there.

> I'm attaching version 3; this just adds Leif's requested phony targets,

Thanks.

> plus changes some tabs to spaces.  With the tabs, I see this at the start of the build:

```
(sage-4.5.3) [10:58]$ make
# Note that (currently) "tee" will be run in the directory cd'ed to
# in pipestatus' first argument, i.e. "spkg/": 
spkg/pipestatus "cd spkg && ./install all 2>&1" "tee -a ../install.log"
```


Well, that's (just) informational and does no harm... ;-)

> With spaces instead, the lines starting with "#" do not appear.

I'm currently not that sure that would be very portable; instead, you could also prepend ``@`` (to `#`, and leave the tabs). The comments were actually *shell* comments (i.e., part of the receipt) rather than Makefile comments.



---

archive/issue_comments_096106.json:
```json
{
    "body": "> Well, that's (just) informational and does no harm... ;-\n\nI think it could be a little confusing: it looks like it should be informational, but it won't mean much to some users, and so they might be concerned or worried or puzzled.  If we skip it, then the first printed line looks like something technical which therefore be safely ignored by uninterested people...\n\nI'm attaching new versions with \"`@`#\".",
    "created_at": "2010-09-13T18:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96106",
    "user": "https://github.com/jhpalmieri"
}
```

> Well, that's (just) informational and does no harm... ;-

I think it could be a little confusing: it looks like it should be informational, but it won't mean much to some users, and so they might be concerned or worried or puzzled.  If we skip it, then the first printed line looks like something technical which therefore be safely ignored by uninterested people...

I'm attaching new versions with "`@`#".



---

archive/issue_comments_096107.json:
```json
{
    "body": "(I'm assuming that \"interested\" people will start browsing through the Makefile, so will see the comment...)",
    "created_at": "2010-09-13T18:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96107",
    "user": "https://github.com/jhpalmieri"
}
```

(I'm assuming that "interested" people will start browsing through the Makefile, so will see the comment...)



---

archive/issue_comments_096108.json:
```json
{
    "body": "Replying to [comment:10 jhpalmieri]:\n> > Well, that's (just) informational and does no harm... ;-\n> \n> I think it could be a little confusing [...]\n\nAgreed.",
    "created_at": "2010-09-13T19:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96108",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:10 jhpalmieri]:
> > Well, that's (just) informational and does no harm... ;-
> 
> I think it could be a little confusing [...]

Agreed.



---

archive/issue_comments_096109.json:
```json
{
    "body": "version 3 of the makefile (or Makefile)",
    "created_at": "2010-09-13T19:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96109",
    "user": "https://github.com/jhpalmieri"
}
```

version 3 of the makefile (or Makefile)



---

archive/issue_comments_096110.json:
```json
{
    "body": "Attachment [makefile.v3.diff](tarball://root/attachments/some-uuid/ticket9799/makefile.v3.diff) by @jhpalmieri created at 2010-09-13 19:41:37\n\nDiff between v2 and v3",
    "created_at": "2010-09-13T19:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96110",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [makefile.v3.diff](tarball://root/attachments/some-uuid/ticket9799/makefile.v3.diff) by @jhpalmieri created at 2010-09-13 19:41:37

Diff between v2 and v3



---

archive/issue_comments_096111.json:
```json
{
    "body": "I changed one more \"#\" to \"`@`#\": without the \"`@`\", `make test` print this possibly confusing message:\n\n```\n# . local/bin/sage-env && sage-starts && (also) puts sage-maketest into the path\n```\n\nIt reads better as a comment, with no evaluation of the variable:\n\n```\n     @# $(TESTPRELIMS) (also) puts sage-maketest into the path\n```\n",
    "created_at": "2010-09-13T19:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96111",
    "user": "https://github.com/jhpalmieri"
}
```

I changed one more "#" to "`@`#": without the "`@`", `make test` print this possibly confusing message:

```
# . local/bin/sage-env && sage-starts && (also) puts sage-maketest into the path
```

It reads better as a comment, with no evaluation of the variable:

```
     @# $(TESTPRELIMS) (also) puts sage-maketest into the path
```




---

archive/issue_comments_096112.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> > For upgrades from Sage versions without pipestatus: What if we create pipestatus in the makefile instead of in spkg/install?\n> \n> I may be wrong about this, but if you run \"sage -upgrade\", then I don't think \"makefile\" gets upgraded.  So if we just modify makefile, we can assume that we have pipestatus available to us: people upgrading won't get the new makefile, and people building from scratch will have spkg/pipestatus.\n\nYou're right.  Your idea is simpler and better.\n\nI can't test V3 right now, but here or elsewhere, should we rewrite the `test` target so it works like the other testing targets?\n\nOn renaming `makefile`:  Does any platform (Windows?) require the current name?",
    "created_at": "2010-09-13T22:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96112",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:4 jhpalmieri]:
> > For upgrades from Sage versions without pipestatus: What if we create pipestatus in the makefile instead of in spkg/install?
> 
> I may be wrong about this, but if you run "sage -upgrade", then I don't think "makefile" gets upgraded.  So if we just modify makefile, we can assume that we have pipestatus available to us: people upgrading won't get the new makefile, and people building from scratch will have spkg/pipestatus.

You're right.  Your idea is simpler and better.

I can't test V3 right now, but here or elsewhere, should we rewrite the `test` target so it works like the other testing targets?

On renaming `makefile`:  Does any platform (Windows?) require the current name?



---

archive/issue_comments_096113.json:
```json
{
    "body": "What is the status of this ticket?  It looks like there are some good ideas here, let's not waste this effort...  Is this related to #9896 or is it independent of that?",
    "created_at": "2010-10-19T08:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96113",
    "user": "https://github.com/jdemeyer"
}
```

What is the status of this ticket?  It looks like there are some good ideas here, let's not waste this effort...  Is this related to #9896 or is it independent of that?



---

archive/issue_comments_096114.json:
```json
{
    "body": "Replying to [comment:16 jdemeyer]:\n> What is the status of this ticket?  It looks like there are some good ideas here, let's not waste this effort...  Is this related to #9896 or is it independent of that?\n\nThis one is rather unrelated (or even better, afaik *independent* of #9896).\n\nFeel free to improve the Makefile further, or review what we have so far... ;-) (See some comments above.)\n\nThe (or a) \"concurrent\" ticket to this (and #9896) is *\"Put more files under revision control\"*, #9433, which I'd like to see merged in 4.6.1.\n\n(Also related: #9811, which is I guess caused by `tee`ing without `pipestatus` as well.)",
    "created_at": "2010-10-19T11:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96114",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:16 jdemeyer]:
> What is the status of this ticket?  It looks like there are some good ideas here, let's not waste this effort...  Is this related to #9896 or is it independent of that?

This one is rather unrelated (or even better, afaik *independent* of #9896).

Feel free to improve the Makefile further, or review what we have so far... ;-) (See some comments above.)

The (or a) "concurrent" ticket to this (and #9896) is *"Put more files under revision control"*, #9433, which I'd like to see merged in 4.6.1.

(Also related: #9811, which is I guess caused by `tee`ing without `pipestatus` as well.)



---

archive/issue_comments_096115.json:
```json
{
    "body": "Something to review... ;-)",
    "created_at": "2010-10-19T12:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96115",
    "user": "https://github.com/nexttime"
}
```

Something to review... ;-)



---

archive/issue_comments_096116.json:
```json
{
    "body": "Complete patch from the makefile in sage-4.6.alpha3",
    "created_at": "2010-10-19T21:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96116",
    "user": "https://github.com/jdemeyer"
}
```

Complete patch from the makefile in sage-4.6.alpha3



---

archive/issue_comments_096117.json:
```json
{
    "body": "Changing keywords from \"\" to \"makefile\".",
    "created_at": "2010-10-19T21:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96117",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "" to "makefile".



---

archive/issue_comments_096118.json:
```json
{
    "body": "Attachment [9799_makefile.patch](tarball://root/attachments/some-uuid/ticket9799/9799_makefile.patch) by @jdemeyer created at 2010-10-19 21:11:02\n\nI have read the patch and it looks okay to me, but perhaps somebody who is more familiar with the Sage build process should have a second look.  I am currently doing a full build from scratch with the new `Makefile` (with capital).  I have a few comments (which you're free to ignore...).\n\nWhy not leave\n\n```\nall: build doc \n```\n\nas it is?  I agree that \"build\" is superfluous, but I think it adds clarity.  It is also more robust in case other parts of the makefile are changed.\n\nthe same for\n\n```\ndoc-html: build # (already) indirectly depends on $(PIPE)\n```\n\n\nAbout the comments: I think it more common to put them outside the make rules, so instead of\n\n```\nbuild:  $(PIPE)\n    @# Note that (currently) \"tee\" will be run in the directory cd'ed to \n    @# in pipestatus' first argument, i.e. \"spkg/\":  \n    $(PIPE) \"cd spkg && ./install all 2>&1\" \"tee -a ../install.log\" \n```\n\nwhy not write\n\n```\n# Note that (currently) \"tee\" will be run in the directory cd'ed to\n# in pipestatus' first argument, i.e. \"spkg/\":\nbuild:  $(PIPE)\n    $(PIPE) \"cd spkg && ./install all 2>&1\" \"tee -a ../install.log\" \n```\n",
    "created_at": "2010-10-19T21:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96118",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9799_makefile.patch](tarball://root/attachments/some-uuid/ticket9799/9799_makefile.patch) by @jdemeyer created at 2010-10-19 21:11:02

I have read the patch and it looks okay to me, but perhaps somebody who is more familiar with the Sage build process should have a second look.  I am currently doing a full build from scratch with the new `Makefile` (with capital).  I have a few comments (which you're free to ignore...).

Why not leave

```
all: build doc 
```

as it is?  I agree that "build" is superfluous, but I think it adds clarity.  It is also more robust in case other parts of the makefile are changed.

the same for

```
doc-html: build # (already) indirectly depends on $(PIPE)
```


About the comments: I think it more common to put them outside the make rules, so instead of

```
build:  $(PIPE)
    @# Note that (currently) "tee" will be run in the directory cd'ed to 
    @# in pipestatus' first argument, i.e. "spkg/":  
    $(PIPE) "cd spkg && ./install all 2>&1" "tee -a ../install.log" 
```

why not write

```
# Note that (currently) "tee" will be run in the directory cd'ed to
# in pipestatus' first argument, i.e. "spkg/":
build:  $(PIPE)
    $(PIPE) "cd spkg && ./install all 2>&1" "tee -a ../install.log" 
```




---

archive/issue_comments_096119.json:
```json
{
    "body": "Replying to [comment:19 jdemeyer]:\n> Why not leave\n\n```\nall: build doc \n```\n\n> as it is?  I agree that \"build\" is superfluous, but I think it adds clarity.\n\nA matter of taste, though I think making just `doc` an explicit prerequisite of `all` is more clear here, since it is rather uncommon that the documentation depends on compiling all of the code. (For `spkg/standard/deps`, I prefer at least *some* redundancy because it's partially obscure what depends on what. Especially omitting true direct dependencies because they're already accomplished through deep indirect dependencies is quite error-prone, since in fact *there* dependencies are more likely to change than here. Analogous to the new Fedora library dependency scheme.)\n\n> It is also more robust in case other parts of the makefile are changed.\n\nSee above; I don't think that's the case here, since the dependencies are rather trivial and clear from the context. ;-) \n\n> the same for\n\n```\ndoc-html: build # (already) indirectly depends on $(PIPE)\n```\n\n\nI agree on adding `$(PIPE)`, saves some characters (the comment) anyway. ;-)\n\n> About the comments: I think it more common to put them outside the make rules, so instead of\n\n```\nbuild:  $(PIPE)\n    @# Note that (currently) \"tee\" will be run in the directory cd'ed to \n    @# in pipestatus' first argument, i.e. \"spkg/\":  \n    $(PIPE) \"cd spkg && ./install all 2>&1\" \"tee -a ../install.log\" \n```\n\n> why not write\n\n```\n# Note that (currently) \"tee\" will be run in the directory cd'ed to\n# in pipestatus' first argument, i.e. \"spkg/\":\nbuild:  $(PIPE)\n    $(PIPE) \"cd spkg && ./install all 2>&1\" \"tee -a ../install.log\" \n```\n\n\nWell, the comment actually refers solely to the single shell command line, not the rule. Just imagine there were more of them...",
    "created_at": "2010-10-19T21:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96119",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:19 jdemeyer]:
> Why not leave

```
all: build doc 
```

> as it is?  I agree that "build" is superfluous, but I think it adds clarity.

A matter of taste, though I think making just `doc` an explicit prerequisite of `all` is more clear here, since it is rather uncommon that the documentation depends on compiling all of the code. (For `spkg/standard/deps`, I prefer at least *some* redundancy because it's partially obscure what depends on what. Especially omitting true direct dependencies because they're already accomplished through deep indirect dependencies is quite error-prone, since in fact *there* dependencies are more likely to change than here. Analogous to the new Fedora library dependency scheme.)

> It is also more robust in case other parts of the makefile are changed.

See above; I don't think that's the case here, since the dependencies are rather trivial and clear from the context. ;-) 

> the same for

```
doc-html: build # (already) indirectly depends on $(PIPE)
```


I agree on adding `$(PIPE)`, saves some characters (the comment) anyway. ;-)

> About the comments: I think it more common to put them outside the make rules, so instead of

```
build:  $(PIPE)
    @# Note that (currently) "tee" will be run in the directory cd'ed to 
    @# in pipestatus' first argument, i.e. "spkg/":  
    $(PIPE) "cd spkg && ./install all 2>&1" "tee -a ../install.log" 
```

> why not write

```
# Note that (currently) "tee" will be run in the directory cd'ed to
# in pipestatus' first argument, i.e. "spkg/":
build:  $(PIPE)
    $(PIPE) "cd spkg && ./install all 2>&1" "tee -a ../install.log" 
```


Well, the comment actually refers solely to the single shell command line, not the rule. Just imagine there were more of them...



---

archive/issue_comments_096120.json:
```json
{
    "body": "Installing with the patched Makefile worked fine, also tried to see what happens if `make`, `make doc` or `make ptest` fails.  This does return an error code as it should.  So positive_review.",
    "created_at": "2010-10-20T15:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96120",
    "user": "https://github.com/jdemeyer"
}
```

Installing with the patched Makefile worked fine, also tried to see what happens if `make`, `make doc` or `make ptest` fails.  This does return an error code as it should.  So positive_review.



---

archive/issue_comments_096121.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-20T15:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96121",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096122.json:
```json
{
    "body": "Replying to [comment:23 jdemeyer]:\n\nAnd the reason for this is that files like **M**akefile and README etc. (should) appear first in directory listings, therefore uppercase.\n\nBtw, I wonder if we should at all let the mixed-up output appear on the screen (i.e., `stdout`) when doing *parallel* builds. This isn't *that* easy to handle, because the \"decision\" to actually perform a parallel build is currently (IMHO unnecessarily) made in `spkg/install`. If we want to change that (I'd prefer having just *\"Building package xy...\"*, *\"Successfully installed package xy\"* / *\"Error installing package xy\"* on the screen and in the main log, `$SAGE_ROOT/install.log`), this should of course be addressed on another ticket.\n\nIt's currently hard to see which package actually failed to install after getting *\"Error building Sage.\"*; grepping for \"Error\" gives a lot of harmless lines.",
    "created_at": "2010-10-20T15:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96122",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:23 jdemeyer]:

And the reason for this is that files like **M**akefile and README etc. (should) appear first in directory listings, therefore uppercase.

Btw, I wonder if we should at all let the mixed-up output appear on the screen (i.e., `stdout`) when doing *parallel* builds. This isn't *that* easy to handle, because the "decision" to actually perform a parallel build is currently (IMHO unnecessarily) made in `spkg/install`. If we want to change that (I'd prefer having just *"Building package xy..."*, *"Successfully installed package xy"* / *"Error installing package xy"* on the screen and in the main log, `$SAGE_ROOT/install.log`), this should of course be addressed on another ticket.

It's currently hard to see which package actually failed to install after getting *"Error building Sage."*; grepping for "Error" gives a lot of harmless lines.



---

archive/issue_comments_096123.json:
```json
{
    "body": "Replying to [comment:24 leif]:\n> It's currently hard to see which package actually failed to install after getting *\"Error building Sage.\"*; grepping for \"Error\" gives a lot of harmless lines.\n\nWe could at least (on errors) print a summary at the end, analogous to doctesting (*\"The following packages failed to build/install: ...\"*). This would currently be a bit easier to implement (by keeping track of which packages are to be built, and at the end checking if they were successfully built).",
    "created_at": "2010-10-20T15:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96123",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:24 leif]:
> It's currently hard to see which package actually failed to install after getting *"Error building Sage."*; grepping for "Error" gives a lot of harmless lines.

We could at least (on errors) print a summary at the end, analogous to doctesting (*"The following packages failed to build/install: ..."*). This would currently be a bit easier to implement (by keeping track of which packages are to be built, and at the end checking if they were successfully built).



---

archive/issue_comments_096124.json:
```json
{
    "body": "Replying to [comment:24 leif]:\n> Btw, I wonder if we should at all let the mixed-up output appear on the screen (i.e., `stdout`) when doing *parallel* builds. This isn't *that* easy to handle, because the \"decision\" to actually perform a parallel build is currently (IMHO unnecessarily) made in `spkg/install`. If we want to change that (I'd prefer having just *\"Building package xy...\"*, *\"Successfully installed package xy\"* / *\"Error installing package xy\"* on the screen and in the main log, `$SAGE_ROOT/install.log`), this should of course be addressed on another ticket.\n\nWould using, e.g.,\n\n```\n        @echo '  ACTION  ' $@; command that does the action\n```\n\nin `Makefile` and `deps` and replacing \"pipestatus/tee\" with \">>\" in `deps` help?  Is there any way to keep recording a big, multiplexed log in the background, if we still want it?",
    "created_at": "2010-10-20T23:12:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96124",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:24 leif]:
> Btw, I wonder if we should at all let the mixed-up output appear on the screen (i.e., `stdout`) when doing *parallel* builds. This isn't *that* easy to handle, because the "decision" to actually perform a parallel build is currently (IMHO unnecessarily) made in `spkg/install`. If we want to change that (I'd prefer having just *"Building package xy..."*, *"Successfully installed package xy"* / *"Error installing package xy"* on the screen and in the main log, `$SAGE_ROOT/install.log`), this should of course be addressed on another ticket.

Would using, e.g.,

```
        @echo '  ACTION  ' $@; command that does the action
```

in `Makefile` and `deps` and replacing "pipestatus/tee" with ">>" in `deps` help?  Is there any way to keep recording a big, multiplexed log in the background, if we still want it?



---

archive/issue_comments_096125.json:
```json
{
    "body": "Replying to [comment:26 mpatel]:\n> Replying to [comment:24 leif]:\n> > Btw, I wonder if we should at all let the mixed-up output appear on the screen (i.e., `stdout`) when doing *parallel* builds. This isn't *that* easy to handle, because the \"decision\" to actually perform a parallel build is currently (IMHO unnecessarily) made in `spkg/install`. If we want to change that (I'd prefer having just *\"Building package xy...\"*, *\"Successfully installed package xy\"* / *\"Error installing package xy\"* on the screen and in the main log, `$SAGE_ROOT/install.log`), this should of course be addressed on another ticket.\n> \n> Would using, e.g.,\n\n```\n        @echo '  ACTION  ' $@; command that does the action\n```\n\n> in `Makefile` and `deps` and replacing \"pipestatus/tee\" with \">>\" in `deps` help?  Is there any way to keep recording a big, multiplexed log in the background, if we still want it?\n\nI was thinking of *conditionally* `tee`ing (at least) in the top-level Makefile (just *redirecting* stdout on parallel builds) and checking the exit status inside the receipts to print appropriate messages to some other file descriptor than stdout in `deps`.\n\nVerbosity levels for `sage-spkg` wouldn't be bad either, especially suppressing the verbose `tar` output is IMHO worth doing, since a lot of spkgs contain hundreds or thousands of files (while the actual build log is often only a few lines).\n\nBut I must admit I've already forgotten what exactly I'd planned yesterday... ;-)",
    "created_at": "2010-10-21T00:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96125",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:26 mpatel]:
> Replying to [comment:24 leif]:
> > Btw, I wonder if we should at all let the mixed-up output appear on the screen (i.e., `stdout`) when doing *parallel* builds. This isn't *that* easy to handle, because the "decision" to actually perform a parallel build is currently (IMHO unnecessarily) made in `spkg/install`. If we want to change that (I'd prefer having just *"Building package xy..."*, *"Successfully installed package xy"* / *"Error installing package xy"* on the screen and in the main log, `$SAGE_ROOT/install.log`), this should of course be addressed on another ticket.
> 
> Would using, e.g.,

```
        @echo '  ACTION  ' $@; command that does the action
```

> in `Makefile` and `deps` and replacing "pipestatus/tee" with ">>" in `deps` help?  Is there any way to keep recording a big, multiplexed log in the background, if we still want it?

I was thinking of *conditionally* `tee`ing (at least) in the top-level Makefile (just *redirecting* stdout on parallel builds) and checking the exit status inside the receipts to print appropriate messages to some other file descriptor than stdout in `deps`.

Verbosity levels for `sage-spkg` wouldn't be bad either, especially suppressing the verbose `tar` output is IMHO worth doing, since a lot of spkgs contain hundreds or thousands of files (while the actual build log is often only a few lines).

But I must admit I've already forgotten what exactly I'd planned yesterday... ;-)



---

archive/issue_comments_096126.json:
```json
{
    "body": "Replying to [comment:27 leif]:\n \n> Verbosity levels for `sage-spkg` wouldn't be bad either, especially suppressing the verbose `tar` output is IMHO worth doing, since a lot of spkgs contain hundreds or thousands of files (while the actual build log is often only a few lines).\n\nI think removing the 'v' option from tar output would be sensible. It would make the log files smaller & reduce disk I/O. It would also make finding things like \"warnings\" easier, as you could grep the log looking for warnings, and not find every file which has the name \"warning\" in it. \n\nIn the absence of anyone writing a patch to control verbosity, just removing the 'v' would be a useful addition I think. The default action should not be to produce tons of unnecessary output. \n\nDave",
    "created_at": "2010-10-21T15:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96126",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:27 leif]:
 
> Verbosity levels for `sage-spkg` wouldn't be bad either, especially suppressing the verbose `tar` output is IMHO worth doing, since a lot of spkgs contain hundreds or thousands of files (while the actual build log is often only a few lines).

I think removing the 'v' option from tar output would be sensible. It would make the log files smaller & reduce disk I/O. It would also make finding things like "warnings" easier, as you could grep the log looking for warnings, and not find every file which has the name "warning" in it. 

In the absence of anyone writing a patch to control verbosity, just removing the 'v' would be a useful addition I think. The default action should not be to produce tons of unnecessary output. 

Dave



---

archive/issue_comments_096127.json:
```json
{
    "body": "Replying to [comment:28 drkirkby]:\n> In the absence of anyone writing a patch to control verbosity, just removing the 'v' would be a useful addition I think. The default action should not be to produce tons of unnecessary output. \n\nI can provide a patch for that. :) (Though there are currently a couple? of other tickets modifying `sage-spkg`.)\n\nWe can still fall back to the old behavoir if yet another undocumented environment variable (e.g. `SAGE_SPKG_VERBOSE` or `SAGE_SPKG_LIST_FILES`) is set, to not annoy people who heat their home with harddisks, or need more network traffic etc.\n\nThe advantage of verbose extraction is that you by chance see a lot of useless files that could or should be removed from an spkg. Take e.g. a look at the files in SageNB's Mercurial repository, currently also listed in `spkg/logs/sagenb-*` (it's about 22500 lines)... ;-)",
    "created_at": "2010-10-21T16:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96127",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:28 drkirkby]:
> In the absence of anyone writing a patch to control verbosity, just removing the 'v' would be a useful addition I think. The default action should not be to produce tons of unnecessary output. 

I can provide a patch for that. :) (Though there are currently a couple? of other tickets modifying `sage-spkg`.)

We can still fall back to the old behavoir if yet another undocumented environment variable (e.g. `SAGE_SPKG_VERBOSE` or `SAGE_SPKG_LIST_FILES`) is set, to not annoy people who heat their home with harddisks, or need more network traffic etc.

The advantage of verbose extraction is that you by chance see a lot of useless files that could or should be removed from an spkg. Take e.g. a look at the files in SageNB's Mercurial repository, currently also listed in `spkg/logs/sagenb-*` (it's about 22500 lines)... ;-)



---

archive/issue_comments_096128.json:
```json
{
    "body": "I recently opened #10040 for not using `tar`'s `v` option (by default) when extracting packages.",
    "created_at": "2010-10-21T20:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96128",
    "user": "https://github.com/qed777"
}
```

I recently opened #10040 for not using `tar`'s `v` option (by default) when extracting packages.



---

archive/issue_events_024595.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-01T10:04:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9798#event-24595"
}
```



---

archive/issue_comments_096129.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96129",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_024596.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-11-01T10:23:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "milestone": "sage-4.6.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9798#event-24596"
}
```



---

archive/issue_comments_096130.json:
```json
{
    "body": "One more argument: ;-)\n\n```sh\nSuccessfully installed gnutls-2.2.1.p5\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\npython: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)\nMaking script relocatable\nFinished installing gnutls-2.2.1.p5.spkg\nmake[1]: Leaving directory `/home/leif/Sage/sage-4.6/spkg'\n\nreal\t3m36.199s\nuser\t10m5.250s\nsys\t2m8.140s\nError building Sage.\n./sage -docbuild all html  2>&1 | tee -a dochtml.log\npython: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)\npython: can't open file '/home/leif/Sage/sage-4.6/devel/sage/doc/common/builder.py': [Errno 2] No such file or directory\n. local/bin/sage-env && sage-starts && ./sage -tp 8 -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log\npython: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)\nTesting that Sage starts...\npython: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)\npython: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)\npython: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)\nTraceback (most recent call last):\n  File \"/home/leif/Sage/sage-4.6/local/bin/sage-eval\", line 4, in <module>\n    from sage.all import *\nImportError: No module named sage.all\nSage failed to startup.\nmake: *** [ptestlong] Error 1\n```\n",
    "created_at": "2010-11-01T13:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9798#issuecomment-96130",
    "user": "https://github.com/nexttime"
}
```

One more argument: ;-)

```sh
Successfully installed gnutls-2.2.1.p5
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
Making script relocatable
Finished installing gnutls-2.2.1.p5.spkg
make[1]: Leaving directory `/home/leif/Sage/sage-4.6/spkg'

real	3m36.199s
user	10m5.250s
sys	2m8.140s
Error building Sage.
./sage -docbuild all html  2>&1 | tee -a dochtml.log
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
python: can't open file '/home/leif/Sage/sage-4.6/devel/sage/doc/common/builder.py': [Errno 2] No such file or directory
. local/bin/sage-env && sage-starts && ./sage -tp 8 -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
Testing that Sage starts...
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
Traceback (most recent call last):
  File "/home/leif/Sage/sage-4.6/local/bin/sage-eval", line 4, in <module>
    from sage.all import *
ImportError: No module named sage.all
Sage failed to startup.
make: *** [ptestlong] Error 1
```

