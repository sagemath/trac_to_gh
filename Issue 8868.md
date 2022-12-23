# Issue 8868: Make R graphics work regardless of X and other things

Issue created by migration from https://trac.sagemath.org/ticket/8868

Original creator: kcrisman

Original creation time: 2010-05-04 15:21:08

Assignee: jason, was

CC:  drkirkby

See #8834, where doctests for R graphics had to be made optional.  However, it should be possible for R to always return graphics, if only we understand better how the device selection works.


---

Comment by kcrisman created at 2010-05-04 15:34:06

Some comments from #8834:
R install guide says:

```
Unless you do not want to view graphs on-screen you need ‘X11’ installed, including its headers and client libraries. For recent Fedora distributions it means (at least) ‘libX11’, ‘libX11-devel’, ‘libXt’ and ‘libXt-devel’. On Debian we recommend the meta-package ‘xorg-dev’. If you really do not want these you will need to explicitly configure R without X11, using --with-x=no.
```

But see [this](http://stat.ethz.ch/R-manual/R-patched/library/grDevices/html/Devices.html), which talks about the devices more generally, as well as the R_DEFAULT_DEVICE variable.  In particular, the [pdf](http://stat.ethz.ch/R-manual/R-patched/library/grDevices/html/pdf.html) output, or png via the [bitmap](http://stat.ethz.ch/R-manual/R-patched/library/grDevices/html/dev2bitmap.html) function, could be platform-independent enough to reinstate doctests for R graphics.  Though the bitmap function apparently needs ghostscript, though, which we also can't always count on being present, I don't think.


---

Comment by kcrisman created at 2010-05-04 15:35:45

Of course, if X or Aqua *are* available, we would totally want to have the ability to use them, via interactive output.  But for things like the notebook, we really only want to generate one image at a time, for which anything that makes pdf or png should be appropriate, at least to my way of thinking about this.


---

Comment by jbandlow created at 2010-11-09 16:10:03

I'm recording here what I learned while exploring this [ask.sagemath question](http://ask.sagemath.org/question/192/compiling-r-with-png-support).  Namely, on Ubuntu, the packages xorg-dev and libpng are prerequisites for R graphics to work.


---

Comment by kcrisman created at 2010-11-09 18:01:05

Hmm, that's bad.  We include libpng as part of Sage, as far as I know (libpng-1.2.35.p2.spkg).  So somehow R wasn't picking up the Sage copy of libpng.   That is very interesting.  And bad.

cc:ing drkirkby only because he knows about Sage components picking up (or not) non-Sage libraries.


---

Comment by drkirkby created at 2010-11-09 18:26:27

Replying to [comment:4 kcrisman]:
> Hmm, that's bad.  We include libpng as part of Sage, as far as I know (libpng-1.2.35.p2.spkg).  So somehow R wasn't picking up the Sage copy of libpng.   That is very interesting.  And bad.
> 
> cc:ing drkirkby only because he knows about Sage components picking up (or not) non-Sage libraries.

Using Sage 4.6.1.alpha0 on my OpenSolaris 06/2009 machine, I just run those two commands given on ask.sagemath.question:


```
sage:  r.eval('capabilities("png")')
'  png \nFALSE '
sage: r.eval('capabilities("X11")')
'  X11 \nFALSE '
sage: 
```


looks like I have neither PNG or X support built in. This is odd. When I check `spkg/logs/r-2.10.1.p4.log` I see:


```
checking if libpng version >= 1.0.5... yes
```


then later 


```
R is now configured for i386-pc-solaris2.11

  Source directory:          .
  Installation directory:    /export/home/drkirkby/sage-4.6.1.alpha0/local

  C compiler:                gcc -std=gnu99  -I/export/home/drkirkby/sage-4.6.1.alpha0/local/include -L/export/home/drkirkby/sage-4.6.1.alpha0/local/lib/
  Fortran 77 compiler:       sage_fortran  -g -O2

  C++ compiler:              g++  -g -O2
  Fortran 90/95 compiler:    sage_fortran -g -O2
  Obj-C compiler:

  Interfaces supported:
  External libraries:        readline
  Additional capabilities:   PNG, JPEG, TIFF, NLS
  Options enabled:           shared R library, shared BLAS, R profiling, Java

  Recommended packages:      yes
```


So despite PNG support apparently built in, `r.eval('capabilities("png")')` indicates otherwise. 

It's difficult to know what to trust. 

Dave


---

Comment by kcrisman created at 2011-01-12 16:43:32

Just putting this info here - from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/7d911e59a649eaf6/9ab984487050b968):

```
This binary package works for me without having xorg-dev packages/ 
headers installed, i.e. 
sage -sh 
R 
demo(graphics) 
produces the demo-plots. During creation of the binaries the headers 
are needed, but not for execution
```



---

Comment by kcrisman created at 2011-04-20 12:38:38

See also [this R-devel thread](https://stat.ethz.ch/pipermail/r-devel/2011-April/060600.html) for more information which may lead us to a resolution.


---

Comment by kcrisman created at 2011-04-21 13:55:50

Replying to [comment:7 kcrisman]:
> See also [this R-devel thread](https://stat.ethz.ch/pipermail/r-devel/2011-April/060600.html) for more information which may lead us to a resolution.

In particular, it looks like one has to compile on a machine (if Linux) that has a working display in order for png to pick up the X11.  That sounds weird to me, but it's how it's written.  Or we have to use Cairo, which I don't know that we want to add to the tarball.


---

Comment by jason created at 2011-04-21 15:43:47

I solved this on Ubuntu by installing the `libpango1.0-dev` and `libcairo-dev` packages.  I had also earlier installed the `xorg-dev` package, but I don't know if it is actually needed here.


---

Comment by kcrisman created at 2011-04-21 15:49:35

Thanks, Jason.

To other readers - see also the [whole R-devel thread](https://stat.ethz.ch/pipermail/r-devel/2011-April/thread.html#60600), where a slew of possible configure and download options are mentioned.  Yikes! 

A resolution of this ticket may end up consisting of adding precise instructions for how to make this work on a given Linux, assuming it works all the time on Mac (perhaps a dangerous assumption, but one I haven't seen go wrong yet on this issue; maybe I need to test it more widely).


---

Comment by kcrisman created at 2011-04-25 12:28:36

See also #11249 for a related ticket.


---

Comment by vbraun created at 2011-11-19 22:20:44

I made a new R (r-project) spkg at #12057, this gives me working PNG output without any X11 headers installed. If #12057 fixes any issues you might have, we can close this ticket imho.


---

Comment by kcrisman created at 2011-11-20 01:12:34

Changing keywords from "" to "r-project".
