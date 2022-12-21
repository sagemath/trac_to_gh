# Issue 3306: [with patch; needs review] shared library for symmetrica

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-05-26 03:46:45

Assignee: mabshoff

CC:  fbissey

I've attached a patch that completely replaces the minimal symmetrica makefile with a much more standard version.  It includes a shared library with a soname (the symmetrica version number must be maintained in the package; currently its a variable in the makefile) and adds normal targets like clean, install, etc.

This probably needs to be fixed to do shared libraries correctly for non-linux; I'm not sure exactly how that is supposed to work.


---

Attachment

The only problem I see here is that "install" is generally not guaranteed to be available, i.e. on Solaris it is commonly called ginstall. I will fix this, but other than that positive review. I am also not quite sure if the Solaris ld can handle this as is, but as I am porting Sage to use the Sun Forte compiler suite I will fix those issues anyway.

Cheers,

Michael


---

Comment by fbissey created at 2008-05-26 04:29:43

Actually on linux (and probably other unix variants) it seems we
should use the "-Dunix" flag as well. Mind you after a quick grep
through the source only the file de.c make use of that directive.
It also has a MSDOS option there may have been a windows variant
at some point but I cannot find traces of it on the symmetrica
web site.


---

Comment by mabshoff created at 2008-05-29 14:54:17

I am still sitting here pondering whether to apply this patch or not. One issue is that on non-Linux I would need also need to add support for dynamic libraries. But that could be done later, so I will give this another spin and see if it works at least on OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-29 15:05:36

Ok, after looking at this some more I decided that this needs fixing for OSX, Solaris and Cygwin, so I am not applying it as is.

Sorry Tim, but I do not have time right now to fix this properly. Hopefully in the next couple days.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-29 15:11:37

Sorry for the noise: It would obviously be good for the Debianization project of Sage if this patch were applied. So I would propose that you post a patch that does not touch spkg-install and also does not change the makefile in patches/makefile, i.e. leaves the Sage build as is and moves those changes to the Debian makefile patch. Later on when things are sorted out on other platforms we can then unify the two approaches.

Any such patch would be applied more or less immediately. 

Cheers,

Michael


---

Comment by craigcitro created at 2008-06-20 04:57:35

Changing keywords from "" to "editor_mabshoff".


---

Comment by drkirkby created at 2009-12-16 22:22:43

Note HP-UX uses .sl for shared libaries, not .so, so I would not hard-code .so anywhere. 

Dave


---

Comment by fbissey created at 2011-05-01 23:58:43

I think we should close bugs that are related to debianization of sage. The content of
this bug as been obsoloted by later work in any case. I suspect it may have been merged too without being closed.


---

Comment by fbissey created at 2012-03-10 19:13:14

As mentioned in a previous this is obsolete. Let's close it.


---

Comment by fbissey created at 2012-03-10 19:13:14

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-03-11 15:39:17

Changing keywords from "editor_mabshoff" to "".


---

Comment by jdemeyer created at 2012-03-16 10:53:32

Resolution: invalid
