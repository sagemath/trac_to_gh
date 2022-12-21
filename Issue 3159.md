# Issue 3159: [with patch; needs review] Patch adding soname to ntl shared library

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-05-11 16:56:36

Assignee: mabshoff

CC:  f.r.bissey@massey.ac.nz

François Bissey and I merged our patches for adding library versioning and a soname to ntl's shared library and for building the static library without -fPIC and the shared library with -fPIC, and tested that they work for Debian and Gentoo builds.  I believe that if this patch were applied upstream, SAGE would be able to stop patch the ntl makefile as well.  I'm submitting it here so that it can be tested for a standard SAGE build, so we can be sure the patch works before submitting it to Victor Shoup.



---

Attachment


---

Comment by mabshoff created at 2008-05-11 20:16:56

Hi Tim, Francois, 

the patch looks good, but as is it needs some changes to our spkg-install. I also noticed some other issues with some scripts in to the src directory, i.e. all shell scripts are missing a shebang, so that causes trouble with csh in some instances. Once I got those sorted out I will respin our spkg and merge this patch while I am at it.

Cheers,

Michael


---

Comment by fbissey created at 2008-05-11 20:46:45

Mea culpa! One of us should at least have thought about the spkg-install,
we were more concerned that it would work correctly with our distros and that
it was "minimal". Good thing is now libntl.a is correctly compiled without
-fpic and libntl.so is now completely compiled with -fpic.
I attach a tentative patch for spkg-install.

Cheers,
Francois


---

Attachment

I have fixed a small couple issues with the patch in

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha0/ntl-5.4.2.p3.spkg

I did not patch src/src/mfile, but the one in patches, so the new Debian package as well as the ebuild needs to take that into consideration. The spkg builds fine on OSX and Linux, so positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-11 21:56:40

One more thing: When creating symbolic links in spkg-install do not make those links absolute since they will break Sage once it is moved or install to another location. I fixed that and a couple other things, so I am taking partial credit on this ticket :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-11 22:00:10

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-11 22:00:10

Resolution: fixed


---

Comment by fbissey created at 2008-05-11 22:32:03

I'll remember that. It was a _tentative_ patch :)


---

Comment by tabbott created at 2008-05-20 17:26:23

I noticed the spkg-install script now has the current NTL version number in it; I'm attaching a patch that copies libntl*.so that should avoid having to update the patch every time there's a new NTL release.


---

Attachment
