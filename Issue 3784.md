# Issue 3784: add support for SAGE_PYTHONPATH

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-06 23:48:53

Assignee: cwitty


```
>
> > On Aug 6, 9:33 am, Rupert <rupert.n...`@`gmail.com> wrote:
> >> Hello there,
>
> > Hi Rupert,
>
> >> I installed sage this morning and am doing some testing. I noticed
> >> that sage was ignoring some python modules that live in a directory on
> >> my PYTHONPATH environment variable.
>
> >> Looking in $SAGE_ROOT/local/bin/sage-env, I see that it completely
> >> overrides my $PYTHONPATH, rather than prepending its own directories.
>
> > Yes, we do that on purpose.

Hi,

> I propose offering a workaround, e.g.,
>         SAGE_PYTHONPATH
> which *does* get appended to PYTHONPATH
> on startup.

That sounds reasonable to me.

> Note that this is for picking up *user* code, so
> it makes a huge amount of sense to support this.
> It's not an issue of system-wide python being
> different than Sage's at all.

Well, people will use it to have Sage pick up the extensions of the
system Python, but then I get to tell you "I told you so" :)
```


Add something to sage-env that does what is described above.
Also add something to the README.txt that documents this behavior.


---

Comment by ddrake created at 2008-12-17 04:16:34

This would be very nice for SageTeX, so that the user could put sagetex.py somewhere and use $SAGE_PYTHONPATH to help Sage automatically find the module.


---

Attachment

patch for $SAGE_ROOT/local/bin/sage-env


---

Comment by ddrake created at 2008-12-17 04:56:45

patch for README.txt in $SAGE_ROOT


---

Attachment


---

Comment by mabshoff created at 2008-12-21 12:47:45

I would highly recommend to append PYTHONPATH instead of prepending it. That way if someone has a duplicate python package installed somewhere else, i.e. the system, the Sage packages get preferred treatment. Other people might disagree, so in that case we should take it to sage-devel. So "needs work" for now.

Cheers,

Michael


---

Comment by mhansen created at 2009-10-19 17:28:09

This is already the SAGE_PATH variable that is supposed to be for this purpose.


---

Comment by burcin created at 2010-05-24 17:01:38

Does the `SAGE_PATH` variable provide all the functionality requested here? (IMHO, it does.)

In that case, I suggest we close this ticket. There is already a ticket to document the environment variables used by Sage, #8263. I added a comment mentioning `SAGE_PATH` there.


---

Comment by jhpalmieri created at 2012-03-20 19:21:08

Changing status from needs_work to needs_info.


---

Comment by jhpalmieri created at 2012-03-20 19:21:08

Should this be closed? As Burcin says, `SAGE_PATH` solves the problem.


---

Comment by chapoton created at 2014-10-21 12:35:44

I think this can be closed.


---

Comment by chapoton created at 2014-10-21 12:35:44

Changing status from needs_info to needs_review.


---

Comment by aapitzsch created at 2014-10-21 18:06:59

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-10-27 16:25:49

Resolution: invalid
