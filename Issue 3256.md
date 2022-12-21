# Issue 3256: [with patch; needs review] soname and correct -fPIC handling for zn_poly

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-05-19 18:43:23

Assignee: mabshoff

CC:  f.r.bissey@massey.ac.nz dmharvey

I've attached a patch (developed with Francois Bissey) that should make zn_poly have shared library versioning and build the shared library with -fPIC but the static library without -fPIC.

My patch includes the relevant changes to the Debian packaging to make it fully Debian policy-compliant.

It also includes the relevant changes to spkg-install and SAGE-style copy patches that should make SAGE use the new version, though I haven't tested that part.


---

Attachment

I added David Harvey to the CC field since he is upstream. I did also do some work to get zn_poly to build in 64 bit mode on OSX [But I think I can limit this to spkg-install], so I will likely merge this in together with that patch into 3.0.2.rc0.

Cheers,

Michael


---

Comment by tabbott created at 2008-05-19 22:23:16

I bet you'll need to change the cp -a I used when patching to just cp for it to work on solaris.


---

Comment by tabbott created at 2008-05-26 03:06:40

By the way, the dist/debian/rules file in the current zn_poly spkg is incorrectly not marked as executable.

Also, I've attached a patch on top of the last patch that does some trivial improvements to the zn_poly Debian packaging.


---

Attachment

This patch as is breaks when using either the Solaris or *BSD linker. I would suggest that for the Debian package we patch in the soname and other options only when building the Debian package.

Cheers,

Michael


---

Comment by tabbott created at 2008-06-14 20:47:37

What goes wrong?

In the long term, I'd like to see the patch fixed to work on all platforms and merged upstream.  It's of course fine to have them just on Debian in the short term, but it's bad for sonames to be different between different distributions.  So, I think our goal should be to fix the bugs.


---

Comment by dmharvey created at 2008-06-14 20:54:11

Hi guys,

I am quite happy to merge the patch upstream as soon as y'all have figured it out. I have been distracted by another project for a couple of weeks. I will get back to zn_poly soon.


---

Comment by mabshoff created at 2008-06-14 21:00:32

Hi,

the problem is that on Solaris the ld available does not understand the GNUism of -Wlsoname as is. Check out the soname linker options for Solaris at

http://www.fortran-2000.com/ArnaudRecipes/sharedlib.html

I did not find anything comprehensive on linker options anywhere else on the quick, but it ought to do. The patch will work on all currently working platforms, but will break on Solaris and *BSD when using the default linker. The GNU linker is usually available, but normally not installed or not in the default $PATH. And on Solaris we want to be able to build Sage without relying on GNU tools in the future. In addition gcc can be compiled on Solaris to use the Sun ld and many people on Solaris do that, so even if GNU ld is available things go horribly wrong.

Cheers,

Michael


---

Comment by craigcitro created at 2008-06-20 04:56:27

Changing keywords from "" to "editor_mabshoff".


---

Comment by drkirkby created at 2009-12-16 22:20:48

I would second the comments about no using GNU specific options. Also note that .so is not the only extension used for libraries - on HP-UX it is .sl

Dave


---

Comment by fbissey created at 2009-12-17 02:44:06

I was almost going to blame Tim for that one, but I contributed quite a bit to that one
(unlike ticket 3306 which is mostly his if I remember correctly). 
I agree that the patches are fine for debian and linux in general but that for sage we should 
try to be less gld/gcc specific.
We need a strategy for dealing alternative extension though.
Shell variables including the correct suffixes?
Fix in spkg-install?
The problem with putting everything in spkg-install is become big and bloated.


---

Comment by drkirkby created at 2009-12-24 03:14:31

I believe what we need to do is to make better use of sage-env. 

Virtually every package has something like

```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
  CFLAGS = "$CFLAGS -m64"
fi
```


Lets consider what are 3 major things wrong with this. 

 * 64-bit builds are possible on other platforms like Solaris, which is a supported operating system. So SAGE64 should not be restricted to Darwin.
 * -m64 works for the GNU compiler and Sun compilers, but other options are used to generate 64-bit code on other platforms. 
 * The same code is written in loads of packages, adding clutter. 

It would be far more sensible to set the CFLAGS once, taking into account the compiler, platform, setting of SAGE64 and other variables. 

I'd suggest that we replace all this different library names (.dll on Cygwin, .so on most platforms, .dlyn on some, .sl on HP-UX), with a simple $SHARED_LIBRARY_EXTENSION. Then set that once and for all, and people don't have to worry about it, just refer to it as a variable. 

#6595 shows two examples of what William considers serious bugs, which were only found when the Sun compiler was used. In one case, a function computed an answer, but never returned it to what called it. g++ accepted that. The Sun compiler will not. There's a lot more to be gained by writing portable code than simply getting code to run on other systems. 

#7505 will allow the compiler to be determined easily, whether that be gcc, Sun Studio, HP's on HP-UX, IBM's on AIX, and several others. Once we know what compiler we have, we have a reasonable chance of knowing the right options. 


Anyway, there is a lot we can do to improve things, but I do agree that doing a lot of things in spkg-install is not sensible. It would seem sensible that only has things specific to that package, rather than code which needs to be in every package.


---

Comment by fbissey created at 2011-05-01 23:56:52

I think that we should close this bug. Possibly as "won't fix" or "invalid". If it has been merged I suspect it has been obsoleted by some later work.
