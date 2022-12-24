# Issue 9846: Handle a preset R_PROFILE variable

archive/issues_009846.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  ggrafendorfer kcrisman\n\nA preset `R_PROFILE` variable can cause some R packages to fail to build/install and interfere with doctests.\n\nGeorg Grafendorfer [reported this problem on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/b2827cba9319bfed/41eab313614e6d2a#41eab313614e6d2a).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9847\n\n",
    "created_at": "2010-09-01T09:45:22Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Handle a preset R_PROFILE variable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9846",
    "user": "mpatel"
}
```
Assignee: GeorgSWeber

CC:  ggrafendorfer kcrisman

A preset `R_PROFILE` variable can cause some R packages to fail to build/install and interfere with doctests.

Georg Grafendorfer [reported this problem on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/b2827cba9319bfed/41eab313614e6d2a#41eab313614e6d2a).

Issue created by migration from https://trac.sagemath.org/ticket/9847





---

archive/issue_comments_097172.json:
```json
{
    "body": "From around line 180 of `SAGE_LOCAL/bin/sage-env`:\n\n```sh\nif [ -z \"$RHOME\" ]; then\n    RHOME=\"$SAGE_LOCAL/lib/R\" && export RHOME\nfi\n```\n\nShould we add a similar test for `R_PROFILE`?",
    "created_at": "2010-09-01T09:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97172",
    "user": "mpatel"
}
```

From around line 180 of `SAGE_LOCAL/bin/sage-env`:

```sh
if [ -z "$RHOME" ]; then
    RHOME="$SAGE_LOCAL/lib/R" && export RHOME
fi
```

Should we add a similar test for `R_PROFILE`?



---

archive/issue_comments_097173.json:
```json
{
    "body": "I think we should perhaps\n\n```sh\nunset R_PROFILE\n```\n\nin R's `spkg-install`, too.",
    "created_at": "2010-09-01T13:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97173",
    "user": "leif"
}
```

I think we should perhaps

```sh
unset R_PROFILE
```

in R's `spkg-install`, too.



---

archive/issue_comments_097174.json:
```json
{
    "body": "Apparently this might be addressed by a solution to #9906.",
    "created_at": "2010-10-01T14:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97174",
    "user": "kcrisman"
}
```

Apparently this might be addressed by a solution to #9906.



---

archive/issue_comments_097175.json:
```json
{
    "body": "Replying to [comment:2 leif]:\n> I think we should perhaps\n\n```sh\nunset R_PROFILE\n```\n\n> in R's `spkg-install`, too.\n\n#9906 (R 2.10.1.p5) does this now.",
    "created_at": "2011-08-05T10:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97175",
    "user": "leif"
}
```

Replying to [comment:2 leif]:
> I think we should perhaps

```sh
unset R_PROFILE
```

> in R's `spkg-install`, too.

#9906 (R 2.10.1.p5) does this now.



---

archive/issue_comments_097176.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-05T10:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97176",
    "user": "leif"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097177.json:
```json
{
    "body": "Thanks.  Trac isn't sending emails, as you know, so I just saw this.  (Well, six hours isn't bad.)  I'll take a look at #9906 then.",
    "created_at": "2011-08-05T16:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97177",
    "user": "kcrisman"
}
```

Thanks.  Trac isn't sending emails, as you know, so I just saw this.  (Well, six hours isn't bad.)  I'll take a look at #9906 then.



---

archive/issue_comments_097178.json:
```json
{
    "body": "Sorry I didn't come back to this.  It is correct that the spkgs at #9906 do this in the spkg scripts.  \n\nSo I can give this positive review as long as Leif promises that if I or some other reviewer find out that the fix at #9906 doesn't solve the type of problem above, that it will get addressed there and no longer here!  \n\nSound good?  ;-)  But I don't think that will be necessary.",
    "created_at": "2011-08-18T02:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97178",
    "user": "kcrisman"
}
```

Sorry I didn't come back to this.  It is correct that the spkgs at #9906 do this in the spkg scripts.  

So I can give this positive review as long as Leif promises that if I or some other reviewer find out that the fix at #9906 doesn't solve the type of problem above, that it will get addressed there and no longer here!  

Sound good?  ;-)  But I don't think that will be necessary.



---

archive/issue_comments_097179.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> Sorry I didn't come back to this.  It is correct that the spkgs at #9906 do this in the spkg scripts.  \n> \n> So I can give this positive review as long as Leif promises that if I or some other reviewer find out that the fix at #9906 doesn't solve the type of problem above, that it will get addressed there and no longer here!\n\nIn that case, you should also give *this ticket* positive review, such that the release manager will close it, with \"resolution: duplicate\".\n\nIf issues with `R_PROFILE` should (re)arise unrelated to (the installation of) the R spkg, i.e., which would have to be fixed elsewhere, we can still reopen *this* ticket.\n\n(IIRC some of the problems showed up *during doctesting*, but because `R_PROFILE` had been set *during installation*, so are now fixed by the new spkg. If there needs to be done more w.r.t. this -- which I don't think -- this can be addressed at #9906 as Karl-Dieter suggests.)\n\nNote that this ticket already has #9906 as its dependency.",
    "created_at": "2011-08-18T17:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97179",
    "user": "leif"
}
```

Replying to [comment:6 kcrisman]:
> Sorry I didn't come back to this.  It is correct that the spkgs at #9906 do this in the spkg scripts.  
> 
> So I can give this positive review as long as Leif promises that if I or some other reviewer find out that the fix at #9906 doesn't solve the type of problem above, that it will get addressed there and no longer here!

In that case, you should also give *this ticket* positive review, such that the release manager will close it, with "resolution: duplicate".

If issues with `R_PROFILE` should (re)arise unrelated to (the installation of) the R spkg, i.e., which would have to be fixed elsewhere, we can still reopen *this* ticket.

(IIRC some of the problems showed up *during doctesting*, but because `R_PROFILE` had been set *during installation*, so are now fixed by the new spkg. If there needs to be done more w.r.t. this -- which I don't think -- this can be addressed at #9906 as Karl-Dieter suggests.)

Note that this ticket already has #9906 as its dependency.



---

archive/issue_comments_097180.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-18T17:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97180",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097181.json:
```json
{
    "body": "> > So I can give this positive review as long as Leif promises that if I or some other reviewer find out that the fix at #9906 doesn't solve the type of problem above, that it will get addressed there and no longer here!\n> \n> In that case, you should also give *this ticket* positive review, such that the release manager will close it, with \"resolution: duplicate\".\n\nCorrect.  I just wanted to make sure :)  Great.\n\n> (IIRC some of the problems showed up *during doctesting*, but because `R_PROFILE` had been set *during installation*, so are now fixed by the new spkg. If there needs to be done more w.r.t. this -- which I don't think -- this can be addressed at #9906 as Karl-Dieter suggests.)\nYeah, I'm pretty sure that was the issue, or more precisely that `R_PROFILE` was *not* (re)set.\n> Note that this ticket already has #9906 as its dependency.\nWell, that wouldn't be necessary with a duplicate/wontfix one.\n\nSee you at #9906, eventually (when I get time to do all the many tests on that).",
    "created_at": "2011-08-18T17:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97181",
    "user": "kcrisman"
}
```

> > So I can give this positive review as long as Leif promises that if I or some other reviewer find out that the fix at #9906 doesn't solve the type of problem above, that it will get addressed there and no longer here!
> 
> In that case, you should also give *this ticket* positive review, such that the release manager will close it, with "resolution: duplicate".

Correct.  I just wanted to make sure :)  Great.

> (IIRC some of the problems showed up *during doctesting*, but because `R_PROFILE` had been set *during installation*, so are now fixed by the new spkg. If there needs to be done more w.r.t. this -- which I don't think -- this can be addressed at #9906 as Karl-Dieter suggests.)
Yeah, I'm pretty sure that was the issue, or more precisely that `R_PROFILE` was *not* (re)set.
> Note that this ticket already has #9906 as its dependency.
Well, that wouldn't be necessary with a duplicate/wontfix one.

See you at #9906, eventually (when I get time to do all the many tests on that).



---

archive/issue_comments_097182.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-11-15T09:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97182",
    "user": "jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_097183.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2012-09-04T13:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97183",
    "user": "jdemeyer"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_097184.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2012-09-04T13:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97184",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_097185.json:
```json
{
    "body": "I order to finally finish #9906, I decided not to add this change anymore.",
    "created_at": "2012-09-04T13:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97185",
    "user": "jdemeyer"
}
```

I order to finally finish #9906, I decided not to add this change anymore.



---

archive/issue_comments_097186.json:
```json
{
    "body": "Ok.  What was the solution there - simply `unset R_PROFILE` in its spkg-install as suggested in comment:2, or something more involved like in comment:1 (sage-env), or both, or... after reading Leif's comments and Georg's diagnosis in the thread in the description, maybe the simplest solution will be best.",
    "created_at": "2012-09-19T01:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97186",
    "user": "kcrisman"
}
```

Ok.  What was the solution there - simply `unset R_PROFILE` in its spkg-install as suggested in comment:2, or something more involved like in comment:1 (sage-env), or both, or... after reading Leif's comments and Georg's diagnosis in the thread in the description, maybe the simplest solution will be best.



---

archive/issue_comments_097187.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2013-03-27T00:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97187",
    "user": "jdemeyer"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_097188.json:
```json
{
    "body": "Attachment [9847_unset_R.patch](tarball://root/attachments/some-uuid/ticket9847/9847_unset_R.patch) by jdemeyer created at 2013-03-27 01:12:07",
    "created_at": "2013-03-27T01:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97188",
    "user": "jdemeyer"
}
```

Attachment [9847_unset_R.patch](tarball://root/attachments/some-uuid/ticket9847/9847_unset_R.patch) by jdemeyer created at 2013-03-27 01:12:07



---

archive/issue_comments_097189.json:
```json
{
    "body": "Looks good, based on the various discussions in question.\n\nAnd the `R_HOME` and `R_PROFILE` will be \"reset\" after one exits the Sage shell, correct?  I do know that some people use their own custom R packages (or try to) but I guess that isn't supported behavior, given the structure of Sage.\n\nIn that case, applies and presumably works (I certainly can't test this, but based on all the above) so we should get this in, at long last.",
    "created_at": "2013-03-27T01:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97189",
    "user": "kcrisman"
}
```

Looks good, based on the various discussions in question.

And the `R_HOME` and `R_PROFILE` will be "reset" after one exits the Sage shell, correct?  I do know that some people use their own custom R packages (or try to) but I guess that isn't supported behavior, given the structure of Sage.

In that case, applies and presumably works (I certainly can't test this, but based on all the above) so we should get this in, at long last.



---

archive/issue_comments_097190.json:
```json
{
    "body": "Replying to [comment:16 kcrisman]:\n> And the `R_HOME` and `R_PROFILE` will be \"reset\" after one exits the Sage shell, correct?\nSure, although nothing is really \"reset\", you just get your old shell back which never saw `sage-env`.",
    "created_at": "2013-03-27T01:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97190",
    "user": "jdemeyer"
}
```

Replying to [comment:16 kcrisman]:
> And the `R_HOME` and `R_PROFILE` will be "reset" after one exits the Sage shell, correct?
Sure, although nothing is really "reset", you just get your old shell back which never saw `sage-env`.



---

archive/issue_comments_097191.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-27T01:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97191",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097192.json:
```json
{
    "body": "Fair enough.  I think this is a realistic solution to this; I don't think we have to support combinations of these environments.  If someone really wanted to, they could set these things in `init.sage`, right?",
    "created_at": "2013-03-27T01:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97192",
    "user": "kcrisman"
}
```

Fair enough.  I think this is a realistic solution to this; I don't think we have to support combinations of these environments.  If someone really wanted to, they could set these things in `init.sage`, right?



---

archive/issue_comments_097193.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-27T01:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97193",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097194.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-03-28T17:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9846#issuecomment-97194",
    "user": "jdemeyer"
}
```

Resolution: fixed
