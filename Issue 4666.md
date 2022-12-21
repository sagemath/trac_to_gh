# Issue 4666: Make -bdist use canonical binary names

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-01 00:01:12

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
[mabshoff`@`eno ~]$ lsb_release -i -s
Fedora
[mabshoff`@`eno ~]$ lsb_release -r -s
9
```

On OSX use uname to specify OSX release, CPU architecture and 32 vs. 64 bit builds.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-04 21:32:17

People get *very* confused by the generic names and end up downloading completely inappropriate releases, so I am making this a 3.3 blocker since I will be fixing this.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-04 21:32:17

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-04 21:32:17

Changing priority from major to blocker.


---

Comment by mabshoff created at 2009-02-09 13:07:25

Reassign it to 3.3 again.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 02:25:03

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by was created at 2009-06-15 23:23:05

Changing priority from blocker to critical.


---

Comment by was created at 2009-06-15 23:23:05

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.


---

Comment by jdemeyer created at 2012-05-16 20:01:36

Changing priority from critical to major.


---

Attachment


---

Comment by kcrisman created at 2014-11-14 19:29:51

A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?


---

Comment by jdemeyer created at 2014-11-15 08:46:00

Replying to [comment:14 kcrisman]:
> A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?

That's more a question for the current release manager. Like I mentioned on the ticket, I was using [attachment:botdist.py William's script] to generate binaries, but if Volker no longer uses this, we might as well close this ticket as "wontfix".


---

Comment by mmezzarobba created at 2015-04-14 07:37:10

Changing status from new to needs_info.


---

Comment by mmezzarobba created at 2015-04-14 07:37:10

Replying to [comment:15 jdemeyer]:
> Replying to [comment:14 kcrisman]:
> > A lot of this is now in `sage-bdist`.  Is there still a need for some of the stuff in this?
> 
> That's more a question for the current release manager. Like I mentioned on the ticket, I was using [attachment:botdist.py William's script] to generate binaries, but if Volker no longer uses this, we might as well close this ticket as "wontfix".

Volker?


---

Comment by vbraun created at 2015-04-14 08:21:49

I'm not using this script. Labeling binary tarballs by distribution might be worthwile, though. I'm not sure if the current bdist script does that. Note that the buildbots rename the binary tarball as one of the buildsteps.


---

Comment by jdemeyer created at 2015-09-08 12:46:59

Changing status from needs_info to positive_review.


---

Comment by vbraun created at 2015-09-12 13:57:33

Resolution: wontfix
