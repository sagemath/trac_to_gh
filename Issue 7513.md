# Issue 7513: Update Mercurial to 1.4

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-11-22 06:23:45

Assignee: tbd

CC:  leif jdemeyer




---

Comment by leif created at 2010-09-01 17:05:21

Changing keywords from "" to "hg spkg".


---

Comment by jdemeyer created at 2010-11-01 23:44:38

Changing status from new to needs_review.


---

Attachment

SPKG reviewer patch, based on Jeroen's changes.


---

Comment by leif created at 2010-11-02 06:52:08

I originally wanted to give it immediately a positive review, though `patches/posix.py.patch` (which is redundant and for reference only) had not been updated, but just the line numbers changed. (I haven't updated it either.)

Jeroen's changes look fine, except `spkg-install` still tried to copy an obsolete, now removed patch (to `setup.py`).

Then I took a closer look at the rest (including `SPKG.txt`), which ended up in my reviewer patch.

Jeroen, if you agree with my changes, please merge them into the spkg, and I can give it positive review. ;-)


---

Comment by jdemeyer created at 2010-11-02 10:18:56

Replying to [comment:6 leif]:
> I originally wanted to give it immediately a positive review, though `patches/posix.py.patch` (which is redundant and for reference only) had not been updated, but just the line numbers changed. (I haven't updated it either.)
Since the patch still applies perfectly fine, I don't think it is a problem that the line numbers don't match (note that I created `patches/posix.py` from `patches/posix.py.patch`, not the other way around).

> Jeroen's changes look fine, except `spkg-install` still tried to copy an obsolete, now removed patch (to `setup.py`).
Thanks for spotting this.

> Then I took a closer look at the rest (including `SPKG.txt`), which ended up in my reviewer patch.
> 
> Jeroen, if you agree with my changes, please merge them into the spkg, and I can give it positive review. ;-)
Thanks for looking more carefully at this, I just wanted a new spkg quickly :-)


---

Comment by jdemeyer created at 2010-11-02 10:36:16

Leif, I added some minor changes (`7513_review_review.patch`) and posted the resulting spkg at [http://sage.math.washington.edu/home/jdemeyer/spkg/mercurial-1.6.4.p0.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/mercurial-1.6.4.p0.spkg).  Please review.


---

Comment by jdemeyer created at 2010-11-02 10:36:31

Apply on top of leif's patch


---

Attachment

Replying to [comment:7 jdemeyer]:
> Since the patch still applies perfectly fine, I don't think it is a problem that the line numbers don't match (note that I created `patches/posix.py` from `patches/posix.py.patch`, not the other way around).

Obviously. Florent recently complained about a patch of mine that wasn't based on vanilla and so (just) the line numbers changed s.t. Mercurial operated more verbosely than usual. ;-)

In general it's better to also touch the diffs, or keep them in full sync with the patched files; I've come across spkgs where apparently obsolete files were copied over; and it's confusing when there are dead old patches that do not reflect the current differences.
 
> Thanks for looking more carefully at this, I just wanted a new spkg quickly :-)

Well, the ticket's first (opening) anniversary is close...


---

Comment by leif created at 2010-11-02 10:57:47

Yes, I forgot to suggest you removing the code commented out.

Reviewed reviewer's patch looks ok.

I wasn't sure if quoting the '`$`' was intended or not, but assumed the latter. Giving the effective filename would IMHO be ok, too.

Going to check the new spkg...


---

Comment by leif created at 2010-11-02 11:08:56

Ooops, did you patch/upload the wrong package?

I have a completely different upstream src now... (and the size decreased significantly)


---

Comment by leif created at 2010-11-02 11:08:56

Changing assignee from tbd to leif.


---

Comment by leif created at 2010-11-02 11:12:44

Yep, it's the old one again:

```sh
Finished installing mercurial-1.6.4.p0.spkg

real	0m2.384s
user	0m1.960s
sys	0m0.430s
leif`@`quadriga:~/Sage/sage-4.6$ ./sage -hg --version
Mercurial Distributed SCM (version 1.3.1)

Copyright (C) 2005-2009 Matt Mackall <mpm`@`selenic.com> and others
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```



---

Comment by jdemeyer created at 2010-11-02 11:15:15

Replying to [comment:11 leif]:
> Ooops, did you patch/upload the wrong package?
> 
> I have a completely different upstream src now... (and the size decreased significantly)

You are totally right, I forgot to update the `src/` directory when making the new spkg.  I automated this for the PARI spkg and forgot that not every spkg does this automatically :-)


---

Comment by jdemeyer created at 2010-11-02 11:15:34

Should be fixed now, sorry for this...


---

Comment by leif created at 2010-11-02 11:26:37


```
! patches/setup.py
! patches/setup.py.patch
```

;-)


---

Comment by jdemeyer created at 2010-11-02 11:32:39

Next attempt...


---

Comment by leif created at 2010-11-02 11:42:25

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-10 22:19:28

Resolution: fixed
