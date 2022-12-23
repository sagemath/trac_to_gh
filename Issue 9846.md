# Issue 9846: Handle a preset R_PROFILE variable

Issue created by migration from https://trac.sagemath.org/ticket/9847

Original creator: mpatel

Original creation time: 2010-09-01 09:45:22

Assignee: GeorgSWeber

CC:  ggrafendorfer kcrisman

A preset `R_PROFILE` variable can cause some R packages to fail to build/install and interfere with doctests.

Georg Grafendorfer [reported this problem on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/b2827cba9319bfed/41eab313614e6d2a#41eab313614e6d2a).


---

Comment by mpatel created at 2010-09-01 09:47:40

From around line 180 of `SAGE_LOCAL/bin/sage-env`:

```sh
if [ -z "$RHOME" ]; then
    RHOME="$SAGE_LOCAL/lib/R" && export RHOME
fi
```

Should we add a similar test for `R_PROFILE`?


---

Comment by leif created at 2010-09-01 13:59:34

I think we should perhaps

```sh
unset R_PROFILE
```

in R's `spkg-install`, too.


---

Comment by kcrisman created at 2010-10-01 14:08:35

Apparently this might be addressed by a solution to #9906.


---

Comment by leif created at 2011-08-05 10:13:18

Replying to [comment:2 leif]:
> I think we should perhaps

```sh
unset R_PROFILE
```

> in R's `spkg-install`, too.

#9906 (R 2.10.1.p5) does this now.


---

Comment by leif created at 2011-08-05 10:13:18

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-08-05 16:30:35

Thanks.  Trac isn't sending emails, as you know, so I just saw this.  (Well, six hours isn't bad.)  I'll take a look at #9906 then.


---

Comment by kcrisman created at 2011-08-18 02:10:11

Sorry I didn't come back to this.  It is correct that the spkgs at #9906 do this in the spkg scripts.  

So I can give this positive review as long as Leif promises that if I or some other reviewer find out that the fix at #9906 doesn't solve the type of problem above, that it will get addressed there and no longer here!  

Sound good?  ;-)  But I don't think that will be necessary.


---

Comment by leif created at 2011-08-18 17:15:22

Replying to [comment:6 kcrisman]:
> Sorry I didn't come back to this.  It is correct that the spkgs at #9906 do this in the spkg scripts.  
> 
> So I can give this positive review as long as Leif promises that if I or some other reviewer find out that the fix at #9906 doesn't solve the type of problem above, that it will get addressed there and no longer here!

In that case, you should also give _this ticket_ positive review, such that the release manager will close it, with "resolution: duplicate".

If issues with `R_PROFILE` should (re)arise unrelated to (the installation of) the R spkg, i.e., which would have to be fixed elsewhere, we can still reopen _this_ ticket.

(IIRC some of the problems showed up _during doctesting_, but because `R_PROFILE` had been set _during installation_, so are now fixed by the new spkg. If there needs to be done more w.r.t. this -- which I don't think -- this can be addressed at #9906 as Karl-Dieter suggests.)

Note that this ticket already has #9906 as its dependency.


---

Comment by kcrisman created at 2011-08-18 17:46:36

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-08-18 17:46:36

> > So I can give this positive review as long as Leif promises that if I or some other reviewer find out that the fix at #9906 doesn't solve the type of problem above, that it will get addressed there and no longer here!
> 
> In that case, you should also give _this ticket_ positive review, such that the release manager will close it, with "resolution: duplicate".

Correct.  I just wanted to make sure :)  Great.

> (IIRC some of the problems showed up _during doctesting_, but because `R_PROFILE` had been set _during installation_, so are now fixed by the new spkg. If there needs to be done more w.r.t. this -- which I don't think -- this can be addressed at #9906 as Karl-Dieter suggests.)
Yeah, I'm pretty sure that was the issue, or more precisely that `R_PROFILE` was _not_ (re)set.
> Note that this ticket already has #9906 as its dependency.
Well, that wouldn't be necessary with a duplicate/wontfix one.

See you at #9906, eventually (when I get time to do all the many tests on that).


---

Comment by jdemeyer created at 2011-11-15 09:21:56

Resolution: duplicate


---

Comment by jdemeyer created at 2012-09-04 13:37:44

Resolution changed from duplicate to 


---

Comment by jdemeyer created at 2012-09-04 13:37:44

Changing status from closed to new.


---

Comment by jdemeyer created at 2012-09-04 13:38:20

I order to finally finish #9906, I decided not to add this change anymore.


---

Comment by kcrisman created at 2012-09-19 01:21:19

Ok.  What was the solution there - simply `unset R_PROFILE` in its spkg-install as suggested in comment:2, or something more involved like in comment:1 (sage-env), or both, or... after reading Leif's comments and Georg's diagnosis in the thread in the description, maybe the simplest solution will be best.


---

Comment by jdemeyer created at 2013-03-27 00:53:10

Changing priority from major to blocker.


---

Attachment


---

Comment by kcrisman created at 2013-03-27 01:19:56

Looks good, based on the various discussions in question.

And the `R_HOME` and `R_PROFILE` will be "reset" after one exits the Sage shell, correct?  I do know that some people use their own custom R packages (or try to) but I guess that isn't supported behavior, given the structure of Sage.

In that case, applies and presumably works (I certainly can't test this, but based on all the above) so we should get this in, at long last.


---

Comment by jdemeyer created at 2013-03-27 01:36:07

Replying to [comment:16 kcrisman]:
> And the `R_HOME` and `R_PROFILE` will be "reset" after one exits the Sage shell, correct?
Sure, although nothing is really "reset", you just get your old shell back which never saw `sage-env`.


---

Comment by kcrisman created at 2013-03-27 01:40:34

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-03-27 01:40:34

Fair enough.  I think this is a realistic solution to this; I don't think we have to support combinations of these environments.  If someone really wanted to, they could set these things in `init.sage`, right?


---

Comment by kcrisman created at 2013-03-27 01:40:46

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-28 17:55:25

Resolution: fixed
