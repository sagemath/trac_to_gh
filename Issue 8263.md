# Issue 8263: Document ALL environment variables used by Sage

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-02-14 14:00:37

Assignee: mvngu

CC:  leif

Few if any environment variables are documented fully. #8262 is supposed to do this for MAKE_CHECK, but I'm aware of some others which need documenting. 
 
 * SAGE_PORT (Allows one to build on any rare (unsupported) platform, like AIX, FreeBSD, HP-UX, Solaris on x86 hardware etc. 
 * SAGE_USE_OLD_GCC (Allows use of gcc 3.4.x) 
 * CFLAG64 (Flag to build 64-bit binary, defaults to -m64) 
 * SAGE_ATLAS_LIB (I've not much idea, but found it when looking)
 * INCLUDE_MPFR_PATCH - (Adds a patch to MPFR to bypass a bug in the Solaris memset on sun4v machines.  Note, if Sun patch 142542-01 is installed on sun4v machines, this is not needed, as that fixes the bug. Values are: 
   * INCLUDE_MPFR_PATCH=0 will never include the patch - useful if you know any sun4v machines MPFR will be used on, are patched. 
   * INCLUDE_MPFR_PATCH=1 will include, so binary will work on a sun4v machine, even if created on an older sun4u machine.
   * If unset, will include patch on sun4v machines only.
 

There are probably others too. Some like CC, are fairly obvious, but in many cases do not work, so in some ways, they might be best either undocumented, or documented with a warning that not all packages accept them.


---

Comment by jhpalmieri created at 2010-02-14 15:44:47

I just added a few to the list.  Where do you think are the best places to document these?  They also fall into several categories: ones related to building, ones related to doctesting, and perhaps others?


---

Comment by jhpalmieri created at 2010-04-13 05:11:13

Note that "SAGE_DOCTEST_ALLOW_TABS" is not an environment variable: it's searched for as a string inside a file to allow tabs to be present in that file (via the patch at #8680).  So I don't think it belongs here.


---

Comment by jhpalmieri created at 2010-04-21 21:20:38

Should "DOT_SAGE" be included?


---

Comment by burcin created at 2010-05-24 16:57:25

There is also a `SAGE_PATH` variable, see #3784.


---

Comment by drkirkby created at 2010-06-04 08:50:38

Replying to [comment:5 jhpalmieri]:
> Should "DOT_SAGE" be included?
Yes, I think so.


---

Comment by drkirkby created at 2010-06-04 08:52:05

I stumbled across this 'SAGE_MATPLOTLIB_GUI' in one of the patches for matplotlib.


```
#####################################################################
# Sage code -- all this code just sets the graphical_backend variable.
# If True, that means we try to build GUI's; otherwise, we definitely
# will not even try, even if we could.  See trac #5301.
#####################################################################
if os.environ.has_key('SAGE_MATPLOTLIB_GUI'):
    if os.environ['SAGE_MATPLOTLIB_GUI'].lower() == 'no':
        graphical_backend = False
    else:
        graphical_backend = True
else:
    graphical_backend = False

print "NOTE: Set SAGE_MATPLOTLIB_GUI to anything but 'no' to try to build the Matplotlib GUI."
if graphical_backend:
    print "Building graphical backends.  WARNING: This may causing some annoying and confusing behavior"
    print "when using Sage + pylab, at least on OS X."
else:
    print "Not building any matplotlib graphical backends."
 #####################################################################

```



---

Comment by mpatel created at 2010-06-14 06:18:43

Ticket #8306 introduces `SAGE_PARALLEL_SPKG_BUILD`.  Setting this to `"yes"` (and `MAKE="make -jX"` with `X > 1`) enables building multiple spkgs in parallel.


---

Comment by drkirkby created at 2010-06-14 07:17:15

Thank you for adding this. I'm not sure of the best place to document these environment variables, but I created the ticket with a view that the Sage documentation should document the variables. Adding them to a ticket was not really my long term aim of the ticket!

Perhaps README.txt is a good place to document these. 

With the exception of SAGE_USE_OLD_GCC and SAGE_USE_OLD_GCC which are "self-documenting", in that a message will soon appear after typing "make" if you need them, the others shold be documented. 

At the moment, peple are more likely to erroneously set CC (which does not work 100%) than they are most of these.


---

Comment by mpatel created at 2010-06-14 09:18:51

Or maybe the [Installation Guide](http://www.sagemath.org/doc/installation/index.html) or [Developer's Guide](http://www.sagemath.org/doc/developer/index.html)?

I _think_ `SAGE_ATLAS_LIB` allows one to use pre-existing ATLAS libraries (system-wide or part of a different Sage installation), instead of compiling them from scratch.


---

Comment by jhpalmieri created at 2010-06-25 20:39:00

Changing status from new to needs_work.


---

Comment by jhpalmieri created at 2010-06-25 20:39:00

Here's a patch to the installation guide.  I'm marking this as "needs work" because I don't know what SAGE_FAT_BINARY and SAGE_VALGRIND do.

Also, is this the right place to put this information?  I also tried it in just before the Fortran section in the same document.  Other suggestions?


---

Comment by drkirkby created at 2010-06-25 23:26:24

I don't know the format of the .rst file, so there is not a lot of point me trying to edit it, but I can make some comments based on the the text of it. 

 * I would say that "SAGE_PARALLEL_SPKG_BUILD" is experimental and has not been fully tested, so if the Sage build fails, one should unset it. (Robert raised an interesting question about how this may work with programs which do tuning.) 
 * I think to say setting CC and CXX *may* be unreliable is an understatement. I can guarantee 100% it will fail to work. I'd be more clear about that, saying it is only for experimental purposes. 
 * CFLAGS/CXXFLAGS - I'd make the point that these do not work for all packages, so are of limited use and setting them may cause build problems. 
 * The meaning of the SAGE64 variable is not correctly described. SAGE64 does not work on only on Solaris. The original aim of SAGE64 was to force a 64-bit build on *OS X* systems where the default was to build 32-bit. So that is why most of the packages had the following rather stupid bit of code. 


```
if [ $SAGE64 = yes -a `uname` = Darwin ] ; 
  CFLAGS=$CFLAGS=m64
  etc etc
fi
```


I've basically changed all those to 


```
if [ "x$SAGE64" = xyes ] ; 
  CFLAGS=$CFLAGS=m64
  etc etc
fi
```


In other words, the variable is now platform independent. So I think something like this would be better:

"SAGE64 - Set this variable to "yes" on any system where you wish to build a 64-bit version of Sage, but the default for the platform it to build 32-bit binaries. This will add the compiler flag -m64 when building binaries. The SAGE64 variable is mainly of use is on OS X, Solaris and OpenSolaris, though it will add the -m64 on any operating system. Some versions of OS X default to 64-bit binaries, in which case this does not need setting. (It would be nice to find out exactly what versions of OS X support both 32 and 64-bit binaries and so remove references to "some versions". But I don't know the facts on this. William will I expect)

 * SAGE_USE_OLD_GCC. I would add the fact Sage will not build with versions of gcc older than 4.0.1, so this is only of use if you intend changing the Sage source code to allow it to build with older versions of GCC. I think we need to stop people wasting their time thinking it might work, because it most certainly will not. 
 
 * CFLAG64. I would add that it is unnecessary to set this on any mainstream operating system, and the only use would be if attempting to port Sage to a platform like AIX or HP-UX using a non-GNU compiler. 

 * INCLUDE_MPFR_PATCH. There is a space missing between at this point "sun4v machines.If" 
 * SAGE_MATPLOTLIB_GUI. There is a 't' missing from the word 'attempt'. 
 * SAGE_PORT. I would add that any attempt to build Sage with a compiler other than GCC will need this set, and furthermore than Sage has never been successfully built with any compiler other than GCC. (This variable is sort of self-documenting, as it explains exactly what to do, so perhaps we don't need to spell it out too much.) 
 * SAGE_TIMEOUT & SAGE_TIMEOUT_LONG are not described. 
 * SAGE_CHECK. I would add that only a small subset of Sage packages support this, but this is being expanded. A reasonably upto date list of packages supporting this may be found at http://trac.sagemath.org/sage_trac/ticket/9281 
 * Should these variables be listed alphabetically? In categories? At the moment, the order seems a bit random. I would think put them in categories, but then sort them alphabetically in there. 

Dave


---

Comment by drkirkby created at 2010-06-25 23:26:24

Changing assignee from mvngu to drkirkby.


---

Comment by jhpalmieri created at 2010-06-26 05:16:52

Here's a new patch which deals with some of these comments.  This is still "needs work"; for example, I don't suggest we keep the text surrounding "SAGE_FAT_BINARY".

Replying to [comment:13 drkirkby]:

>  * I would say that "SAGE_PARALLEL_SPKG_BUILD" is experimental 

Okay.

>  * I think to say setting CC and CXX *may* be unreliable is an understatement.

Okay.

>  * CFLAGS/CXXFLAGS - I'd make the point that these do not work for all packages, so are of limited use and setting them may cause build problems. 

Okay.

>  * The meaning of the SAGE64 variable is not correctly described. 

Sorry, I got this straight out of the sage-env script.
SAGE64 does not work on only on Solaris. The original aim of SAGE64 was to force a 64-bit build on *OS X* systems where 

> Some versions of OS X default to 64-bit binaries

This is either OS X 10.6, or maybe just 64-bit machines on OS X 10.6.  Must be the latter.  But we should check with William or sage-devel.

>  * SAGE_USE_OLD_GCC. I would add the fact Sage will not build with versions of gcc older than 4.0.1, so this is only of use if you intend changing the Sage source code to allow it to build with older versions of GCC. I think we need to stop people wasting their time thinking it might work, because it most certainly will not. 

I've changed this part a bit, but maybe it should be more strongly worded.

>  * CFLAG64. I would add that it is unnecessary to set this on any mainstream operating system, and the only use would be if attempting to port Sage to a platform like AIX or HP-UX using a non-GNU compiler. 

Okay.

>  * INCLUDE_MPFR_PATCH. There is a space missing between at this point "sun4v machines.If" 

Okay

>  * SAGE_MATPLOTLIB_GUI. There is a 't' missing from the word 'attempt'. 

Okay

>  * SAGE_PORT. I would add that any attempt to build Sage with a compiler other than GCC will need this set, and furthermore than Sage has never been successfully built with any compiler other than GCC. (This variable is sort of self-documenting, as it explains exactly what to do, so perhaps we don't need to spell it out too much.) 

Okay.

>  * SAGE_TIMEOUT & SAGE_TIMEOUT_LONG are not described. 

They deal with doctesting, not the build process, so I'm not sure they belong here.  I've added them now.

>  * SAGE_CHECK. I would add that only a small subset of Sage packages support this, but this is being expanded. A reasonably upto date list of packages supporting this may be found at http://trac.sagemath.org/sage_trac/ticket/9281 

I don't know if we should mention this or just work hard at #9281.  This particular piece of documentation doesn't seem to get updated very much -- see the statements at the top of the page I'm editing about Sage not working on Solaris, for example -- so I don't want to post information which is too time-sensitive.

>  * Should these variables be listed alphabetically? In categories? At the moment, the order seems a bit random. I would think put them in categories, but then sort them alphabetically in there. 

I've put them in categories, and then within each category I've started the ones that seem most useful.


---

Comment by jhpalmieri created at 2010-06-27 01:50:55

By reading the source in the atlas spkg, I've figured out more precisely what ``SAGE_ATLAS_LIB`` does, and documented it.  (This is perhaps not what it should do: I've had success building Sage including some library files ending in .so and others ending in .a, so perhaps SAGE_ATLAS_LIB should check for either liblapack.so or liblapack.a, etc.?  Anyway, that belongs on another ticket.)


---

Comment by jhpalmieri created at 2010-06-27 18:42:03

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-06-27 18:42:03

I'm marking this as "needs revew" now.  It doesn't include SAGE_VALGRIND because I don't know what that does.  When we find out, we can add it, but we should probably get a version of this done.  Meanwhile, I've found several other variables by browing through spkg-install files and searching the Sage library:

 - SAGE_DEBUG
 - SAGE_BINARY_BUILD
 - SAGE_PIL_NOTK
 - SAGE_CBLAS
 - SAGE_BROWSER
 - SAGE_PICKLE_JAR


---

Comment by drkirkby created at 2010-06-27 19:51:59

That looks quite an improvement. 

But how can I generate a file which has these changes? I simply do not know what to do with a .rst file. Can you provide a link to a pdf, web-page or something else where I can read it properly? I've never really looked at any Sage documentation apart from on the web site! 

I think once this gets in, we should create another ticket to document the remaining ones. I think you have covered all the common ones. I suspect the others are rarely if ever used. 

Dave


---

Comment by jhpalmieri created at 2010-06-27 20:18:52

From your shell prompt, type "sage -docbuild installation html" or "sage -docbuild installation pdf".  Meanwhile, I've put it up here: [http://sage.math.washington.edu/home/palmieri/misc/installation/source.html](http://sage.math.washington.edu/home/palmieri/misc/installation/source.html).


---

Comment by drkirkby created at 2010-06-27 22:40:53

Thanks John. A couple of minor changes I would suggest. I don't have an install of Sage handy, so are not going to apply a review patch. 

 * Line 202. The comment "you need to check this" can be removed. What you have is correct. 
 * Line 495 - commmonly -> commonly 
 * Line 500 - invididual -> individual 
 * Line 576 says "SAGE_ATLAS_LIB - if you have an installation of ATLAS on your system and you want Sage to use it instead of buliding and installing its own version of Sage, set this variable to be the parent directory of your ATLAS installation:"
   * 'buliding' needs changing to 'building'
   * I believe you mean for Sage to install its own version of ATLAS rather than its own version of Sage. 
 * Line 591. This bug fix was integrated into Solaris 10 update 8 (10/09), so only affects Solaris 10 update 7 (5/09) or earlier. So I think it might be better to change it to. 


```
`INCLUDE_MPFR_PATCH` - This is used to add a patch to MPFR to bypass a bug in the  memset function affecting sun4v machines with versions of Solaris earlier than than Solaris 10 update 8 (10/09). Earlier versions of Solaris 10 can be patched by applying Sun patch 142542-01.

Recognized values are:

INCLUDE_MPFR_PATCH=0 - never include the patch - useful if you know all sun4v machines Sage will be used on are running Solaris 10 update 8 or later, or have been patched with Sun patch 142542-01.
```

 * Line 644. It would be useful to state what directory packages are expected to be in. The default server is http://www.sagemath.org/ but the packages do not sit in the top level. They seem to be in sub-directories below http://www.sagemath.org/packages/ So I suspect if someone sets up their own server they will need to create a directory 'packages'. What happens beyond that I'm not 100% sure - it looks like http://www.sagemath.org/packages/optional/ http://www.sagemath.org/packages/experimental/ and http://www.sagemath.org/packages/spkg/standard/ are all searched for. One would need to check the source code to find out exactly what happens here. (Unless you know the details, it might be easier to put a comment like "please ask for advice on sage-devel if wishing to set up your own server"). 

Apart from those very minor things, that looks a huge improvement. 

Dave


---

Comment by jhpalmieri created at 2010-06-27 23:39:46

Here's a new patch, and I've also updated the web page.

Replying to [comment:19 drkirkby]:
>  * Line 202. The comment "you need to check this" can be removed. What you have is correct. 

(It was there before, it wasn't me.  But I changed it anyway.)

>  * Line 495 - commmonly -> commonly 
>  * Line 500 - invididual -> individual 

Sorry for all of the typos.  My editor is really sluggish when editing rst files -- several seconds delay between when I type things and when they appear, I don't know why.  So I don't get the usual instant feedback, and so I miss things I shouldn't.

I've fixed all of the other comments, and done a bit more rewording.

>  * Line 644. It would be useful to state what directory packages are expected to be in. 

I looked this up and documented it.


---

Comment by drkirkby created at 2010-06-28 00:51:49

Positive review. 

There is one embarrassing (for me) mistake on line 592, as the word "than" appears twice. Perhaps you can fix that, but positive review.


---

Comment by drkirkby created at 2010-06-28 00:51:49

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-06-28 01:18:56

Fixed.


---

Comment by mpatel created at 2010-06-28 01:40:58

Is there a dash missing from ```export MAKE='make jNUM'```?

By the way, another potentially useful GNU Make option is `-l`.  For example, `make -j16 -l24` tells make to use up to 16 jobs but to spawn a new one only if the one-minute load average is less than 24 (and at least one job is already running).  It should be possible, maybe by subclassing [multiprocessing.Pool](http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool), to create a similar option for doctesting.


---

Attachment


---

Comment by jhpalmieri created at 2010-06-28 02:33:35

Fixed.  I didn't put in "-l", though.


---

Comment by rlm created at 2010-07-05 22:47:13

Resolution: fixed


---

Comment by jhpalmieri created at 2010-07-06 18:11:04

See #9440 for a followup.
