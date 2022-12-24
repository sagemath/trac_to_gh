# Issue 8868: Make R graphics work regardless of X and other things

archive/issues_008868.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  drkirkby\n\nSee #8834, where doctests for R graphics had to be made optional.  However, it should be possible for R to always return graphics, if only we understand better how the device selection works.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8868\n\n",
    "created_at": "2010-05-04T15:21:08Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Make R graphics work regardless of X and other things",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8868",
    "user": "kcrisman"
}
```
Assignee: jason, was

CC:  drkirkby

See #8834, where doctests for R graphics had to be made optional.  However, it should be possible for R to always return graphics, if only we understand better how the device selection works.

Issue created by migration from https://trac.sagemath.org/ticket/8868





---

archive/issue_comments_081512.json:
```json
{
    "body": "Some comments from #8834:\nR install guide says:\n\n```\nUnless you do not want to view graphs on-screen you need \u2018X11\u2019 installed, including its headers and client libraries. For recent Fedora distributions it means (at least) \u2018libX11\u2019, \u2018libX11-devel\u2019, \u2018libXt\u2019 and \u2018libXt-devel\u2019. On Debian we recommend the meta-package \u2018xorg-dev\u2019. If you really do not want these you will need to explicitly configure R without X11, using --with-x=no.\n```\n\nBut see [this](http://stat.ethz.ch/R-manual/R-patched/library/grDevices/html/Devices.html), which talks about the devices more generally, as well as the R_DEFAULT_DEVICE variable.  In particular, the [pdf](http://stat.ethz.ch/R-manual/R-patched/library/grDevices/html/pdf.html) output, or png via the [bitmap](http://stat.ethz.ch/R-manual/R-patched/library/grDevices/html/dev2bitmap.html) function, could be platform-independent enough to reinstate doctests for R graphics.  Though the bitmap function apparently needs ghostscript, though, which we also can't always count on being present, I don't think.",
    "created_at": "2010-05-04T15:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81512",
    "user": "kcrisman"
}
```

Some comments from #8834:
R install guide says:

```
Unless you do not want to view graphs on-screen you need ‘X11’ installed, including its headers and client libraries. For recent Fedora distributions it means (at least) ‘libX11’, ‘libX11-devel’, ‘libXt’ and ‘libXt-devel’. On Debian we recommend the meta-package ‘xorg-dev’. If you really do not want these you will need to explicitly configure R without X11, using --with-x=no.
```

But see [this](http://stat.ethz.ch/R-manual/R-patched/library/grDevices/html/Devices.html), which talks about the devices more generally, as well as the R_DEFAULT_DEVICE variable.  In particular, the [pdf](http://stat.ethz.ch/R-manual/R-patched/library/grDevices/html/pdf.html) output, or png via the [bitmap](http://stat.ethz.ch/R-manual/R-patched/library/grDevices/html/dev2bitmap.html) function, could be platform-independent enough to reinstate doctests for R graphics.  Though the bitmap function apparently needs ghostscript, though, which we also can't always count on being present, I don't think.



---

archive/issue_comments_081513.json:
```json
{
    "body": "Of course, if X or Aqua *are* available, we would totally want to have the ability to use them, via interactive output.  But for things like the notebook, we really only want to generate one image at a time, for which anything that makes pdf or png should be appropriate, at least to my way of thinking about this.",
    "created_at": "2010-05-04T15:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81513",
    "user": "kcrisman"
}
```

Of course, if X or Aqua *are* available, we would totally want to have the ability to use them, via interactive output.  But for things like the notebook, we really only want to generate one image at a time, for which anything that makes pdf or png should be appropriate, at least to my way of thinking about this.



---

archive/issue_comments_081514.json:
```json
{
    "body": "I'm recording here what I learned while exploring this [ask.sagemath question](http://ask.sagemath.org/question/192/compiling-r-with-png-support).  Namely, on Ubuntu, the packages xorg-dev and libpng are prerequisites for R graphics to work.",
    "created_at": "2010-11-09T16:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81514",
    "user": "jbandlow"
}
```

I'm recording here what I learned while exploring this [ask.sagemath question](http://ask.sagemath.org/question/192/compiling-r-with-png-support).  Namely, on Ubuntu, the packages xorg-dev and libpng are prerequisites for R graphics to work.



---

archive/issue_comments_081515.json:
```json
{
    "body": "Hmm, that's bad.  We include libpng as part of Sage, as far as I know (libpng-1.2.35.p2.spkg).  So somehow R wasn't picking up the Sage copy of libpng.   That is very interesting.  And bad.\n\ncc:ing drkirkby only because he knows about Sage components picking up (or not) non-Sage libraries.",
    "created_at": "2010-11-09T18:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81515",
    "user": "kcrisman"
}
```

Hmm, that's bad.  We include libpng as part of Sage, as far as I know (libpng-1.2.35.p2.spkg).  So somehow R wasn't picking up the Sage copy of libpng.   That is very interesting.  And bad.

cc:ing drkirkby only because he knows about Sage components picking up (or not) non-Sage libraries.



---

archive/issue_comments_081516.json:
```json
{
    "body": "Replying to [comment:4 kcrisman]:\n> Hmm, that's bad.  We include libpng as part of Sage, as far as I know (libpng-1.2.35.p2.spkg).  So somehow R wasn't picking up the Sage copy of libpng.   That is very interesting.  And bad.\n> \n> cc:ing drkirkby only because he knows about Sage components picking up (or not) non-Sage libraries.\n\nUsing Sage 4.6.1.alpha0 on my OpenSolaris 06/2009 machine, I just run those two commands given on ask.sagemath.question:\n\n\n```\nsage:  r.eval('capabilities(\"png\")')\n'  png \\nFALSE '\nsage: r.eval('capabilities(\"X11\")')\n'  X11 \\nFALSE '\nsage: \n```\n\n\nlooks like I have neither PNG or X support built in. This is odd. When I check `spkg/logs/r-2.10.1.p4.log` I see:\n\n\n```\nchecking if libpng version >= 1.0.5... yes\n```\n\n\nthen later \n\n\n```\nR is now configured for i386-pc-solaris2.11\n\n  Source directory:          .\n  Installation directory:    /export/home/drkirkby/sage-4.6.1.alpha0/local\n\n  C compiler:                gcc -std=gnu99  -I/export/home/drkirkby/sage-4.6.1.alpha0/local/include -L/export/home/drkirkby/sage-4.6.1.alpha0/local/lib/\n  Fortran 77 compiler:       sage_fortran  -g -O2\n\n  C++ compiler:              g++  -g -O2\n  Fortran 90/95 compiler:    sage_fortran -g -O2\n  Obj-C compiler:\n\n  Interfaces supported:\n  External libraries:        readline\n  Additional capabilities:   PNG, JPEG, TIFF, NLS\n  Options enabled:           shared R library, shared BLAS, R profiling, Java\n\n  Recommended packages:      yes\n```\n\n\nSo despite PNG support apparently built in, `r.eval('capabilities(\"png\")')` indicates otherwise. \n\nIt's difficult to know what to trust. \n\nDave",
    "created_at": "2010-11-09T18:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81516",
    "user": "drkirkby"
}
```

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

archive/issue_comments_081517.json:
```json
{
    "body": "Just putting this info here - from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/7d911e59a649eaf6/9ab984487050b968):\n\n```\nThis binary package works for me without having xorg-dev packages/ \nheaders installed, i.e. \nsage -sh \nR \ndemo(graphics) \nproduces the demo-plots. During creation of the binaries the headers \nare needed, but not for execution\n```\n",
    "created_at": "2011-01-12T16:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81517",
    "user": "kcrisman"
}
```

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

archive/issue_comments_081518.json:
```json
{
    "body": "See also [this R-devel thread](https://stat.ethz.ch/pipermail/r-devel/2011-April/060600.html) for more information which may lead us to a resolution.",
    "created_at": "2011-04-20T12:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81518",
    "user": "kcrisman"
}
```

See also [this R-devel thread](https://stat.ethz.ch/pipermail/r-devel/2011-April/060600.html) for more information which may lead us to a resolution.



---

archive/issue_comments_081519.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> See also [this R-devel thread](https://stat.ethz.ch/pipermail/r-devel/2011-April/060600.html) for more information which may lead us to a resolution.\n\nIn particular, it looks like one has to compile on a machine (if Linux) that has a working display in order for png to pick up the X11.  That sounds weird to me, but it's how it's written.  Or we have to use Cairo, which I don't know that we want to add to the tarball.",
    "created_at": "2011-04-21T13:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81519",
    "user": "kcrisman"
}
```

Replying to [comment:7 kcrisman]:
> See also [this R-devel thread](https://stat.ethz.ch/pipermail/r-devel/2011-April/060600.html) for more information which may lead us to a resolution.

In particular, it looks like one has to compile on a machine (if Linux) that has a working display in order for png to pick up the X11.  That sounds weird to me, but it's how it's written.  Or we have to use Cairo, which I don't know that we want to add to the tarball.



---

archive/issue_comments_081520.json:
```json
{
    "body": "I solved this on Ubuntu by installing the `libpango1.0-dev` and `libcairo-dev` packages.  I had also earlier installed the `xorg-dev` package, but I don't know if it is actually needed here.",
    "created_at": "2011-04-21T15:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81520",
    "user": "jason"
}
```

I solved this on Ubuntu by installing the `libpango1.0-dev` and `libcairo-dev` packages.  I had also earlier installed the `xorg-dev` package, but I don't know if it is actually needed here.



---

archive/issue_comments_081521.json:
```json
{
    "body": "Thanks, Jason.\n\nTo other readers - see also the [whole R-devel thread](https://stat.ethz.ch/pipermail/r-devel/2011-April/thread.html#60600), where a slew of possible configure and download options are mentioned.  Yikes! \n\nA resolution of this ticket may end up consisting of adding precise instructions for how to make this work on a given Linux, assuming it works all the time on Mac (perhaps a dangerous assumption, but one I haven't seen go wrong yet on this issue; maybe I need to test it more widely).",
    "created_at": "2011-04-21T15:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81521",
    "user": "kcrisman"
}
```

Thanks, Jason.

To other readers - see also the [whole R-devel thread](https://stat.ethz.ch/pipermail/r-devel/2011-April/thread.html#60600), where a slew of possible configure and download options are mentioned.  Yikes! 

A resolution of this ticket may end up consisting of adding precise instructions for how to make this work on a given Linux, assuming it works all the time on Mac (perhaps a dangerous assumption, but one I haven't seen go wrong yet on this issue; maybe I need to test it more widely).



---

archive/issue_comments_081522.json:
```json
{
    "body": "See also #11249 for a related ticket.",
    "created_at": "2011-04-25T12:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81522",
    "user": "kcrisman"
}
```

See also #11249 for a related ticket.



---

archive/issue_comments_081523.json:
```json
{
    "body": "I made a new R (r-project) spkg at #12057, this gives me working PNG output without any X11 headers installed. If #12057 fixes any issues you might have, we can close this ticket imho.",
    "created_at": "2011-11-19T22:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81523",
    "user": "vbraun"
}
```

I made a new R (r-project) spkg at #12057, this gives me working PNG output without any X11 headers installed. If #12057 fixes any issues you might have, we can close this ticket imho.



---

archive/issue_comments_081524.json:
```json
{
    "body": "Changing keywords from \"\" to \"r-project\".",
    "created_at": "2011-11-20T01:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8868#issuecomment-81524",
    "user": "kcrisman"
}
```

Changing keywords from "" to "r-project".
