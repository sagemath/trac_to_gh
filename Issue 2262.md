# Issue 2262: Move the debian directory from the sage to the ext repo

Issue created by migration from https://trac.sagemath.org/ticket/2262

Original creator: mabshoff

Original creation time: 2008-02-22 18:35:55

Assignee: tabbott

In retro perspective it was a bad choice to put the dist specific Debian stuff into the Sage repo. It would be much better to create a dist directory in the ext repo and move it all over there. Too late for 2.10.2, but doable in 2.10.3.

Cheers,

Michael


---

Comment by tabbott created at 2008-02-22 19:04:53

How does the ext repo work?  I'm not familiar with this piece of the
SAGE setup (where it unpacks, etc.).

What are the problems with the current setup?  I can imagine various
possible problems, but am curious which we're actually running into.

I find the proximity of directory trees that the current setup has to
be useful for modifying the debian/rules file if the spkg-install
script is nearby, but this is obviously not particularly important.


---

Comment by cwitty created at 2008-02-23 04:03:37

tabbott, the extcode repo unpacks into $SAGE_ROOT/data/extcode.


---

Comment by tabbott created at 2008-02-24 19:32:18

Okay.  Thinking about this more, my main concern is that this would interfere with my plan of building Debian packages for SAGE and all its dependencies by simply running

DEBIAN_RELEASE=lenny-i386 DEBIAN_REPO=<some path> make

from a freshly unpacked SAGE copy, which will build SAGE and upload it to a new Debian apt repository at that path (this would not be our production repository, obviously), since the extcode repository isn't unpacked until late in the SAGE build process.


---

Comment by was created at 2008-02-24 20:37:39

> since the extcode repository isn't unpacked until late in the SAGE build process.

That is by accident.  It could be unpacked at any time.   It's all pure source code with no dependencies for unpacking.  If you would like it to be unpacked much earlier, you should feel free to make that change, in my opinion.  I hope mabshoff can also chime in on this.


---

Comment by mabshoff created at 2008-02-24 20:55:51

Replying to [comment:4 was]:
> > since the extcode repository isn't unpacked until late in the SAGE build process.
> 
> That is by accident.  It could be unpacked at any time.   It's all pure source code with no dependencies for unpacking.  If you would like it to be unpacked much earlier, you should feel free to make that change, in my opinion.  I hope mabshoff can also chime in on this. 

Changing the dependencies would be easy, so I think that it will lead to a workable compromise. sage-lib (or whatever we call the deb) would depend on sage-ext, so we would have the needed files present at build time. The current solution (by adding it to setup.py certainly isn't elegant) and as we pick up other distributions it certainly will become very, very ugly. The dist directory in ext with debian as a subdirectory sounds like the perfect solution to me.

Cheers,

Michael


---

Comment by tabbott created at 2008-02-24 21:15:57

Oh, is this only for the SAGE spkg?


---

Comment by mabshoff created at 2008-02-24 21:30:51

Replying to [comment:6 tabbott]:
> Oh, is this only for the SAGE spkg?

Yes. All the Debian bits needed for all the other spkgs will stay where they are. Since I am doing work on the spkg audit I plan to merge the patches from #2199 as I do the audit.

Cheers,

Michael


---

Comment by tabbott created at 2008-02-24 21:47:03

OK.  This makes much more sense now.

The main thing I guess that needs to be decided then is what to replace the Debian-specific changes to setup.py with.  They include:

1) adding things to library_dirs and include_dirs.  This should be made into a generic environment variable that can be used for any distribution build system.

2) adding /usr/lib/python2.5 to the hardcoded python libraries search path.  I guess we also want to have an environment variable that can extend the set of places that looks for python libraries?


---

Comment by mabshoff created at 2008-02-24 21:53:15

Replying to [comment:8 tabbott]:
> OK.  This makes much more sense now.
> 
> The main thing I guess that needs to be decided then is what to replace the Debian-specific changes to setup.py with.  They include:
> 
> 1) adding things to library_dirs and include_dirs.  This should be made into a generic environment variable that can be used for any distribution build system.

Yes, I agree.

> 
> 2) adding /usr/lib/python2.5 to the hardcoded python libraries search path.  I guess we also want to have an environment variable that can extend the set of places that looks for python libraries?

Sure, but I plan to merge the slightly fixed version of #2173 tonight. Once we have additional distributions on board (or earlier at your convenience, i.e. you want to do the work) we should generalize the infrastructure. Right now there isn't really anybody but Debian (and indirectly Ubuntu) working on packaging within the Sage project, so I am willing to cross that bridge once we get to it.

Cheers,

Michael

Cheers,

Michael


---

Attachment

apply to the extcode repo


---

Comment by mabshoff created at 2008-03-19 09:13:48

apply to the sage repo - removes debian files


---

Attachment

apply to the sage repo - removes debian files from setup.py


---

Attachment


---

Comment by mabshoff created at 2008-03-19 09:14:46

Changing assignee from tabbott to mabshoff.


---

Comment by mabshoff created at 2008-03-19 09:14:46

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-19 09:21:09

This looks good to me.


---

Comment by mabshoff created at 2008-03-19 09:27:35

Ok, this is good.

Tim: let me know if you have any trouble getting this to work or finding things let me know.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-19 09:27:50

Resolution: fixed


---

Comment by mabshoff created at 2008-03-19 09:27:50

Merged in Sage 2.11.alpha0
