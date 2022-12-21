# Issue 9208: Add PKG_CONFIG_PATH to sage-env so problems like matplotlib link properly.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-06-10 23:14:17

Assignee: GeorgSWeber

CC:  wjp jason

## Hardware & associated software
 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

## Sage version and relevant software in Sage
This issue was discovered with Sage 4.4.3, which includes
 * Freetype 2.5.5, which is also known as version 9.16.3 (see #9202 for more information about this rather strange version numbering used). 
 * matplotlib 0.99.1


## The problem
As discussed here, 

http://groups.google.com/group/sage-devel/browse_thread/thread/1d23bf8990fe06d?hl=en

'matplotlib' will find the system version of 'freetype2', rather than the one in Sage, as it relies on the 'pkg-config' command, to determine the version of freetype2, and what compiler options need to be used to link the required freetype2 library. 

Therefore, matplolib reports it is configured with version 9.7.3, which is an old version of freetype2 installed under /usr/sfw in Solaris 10 03/05. 


```
REQUIRED DEPENDENCIES
                  numpy: 1.3.0
              freetype2: 9.7.3
```

(freetype 9.7.3 is also known as version 2.1.9)

## The solution
The solution to this problem is to ensure pkg-config looks into the directory where Sage stores it's .pc files, which is 

{{{ 
$SAGE_LOCAL/lib/pkgconfig
}}}

rather than the default system directory. 

There we find 11 packages have configuration information

This is easy to resolve, by adding the following 4 lines to sage-env, which ensure pkg-config uses the Sage directory 


```
if [ -z "$PKG_CONFIG_PATH" ]; then
    PKG_CONFIG_PATH="$SAGE_LOCAL/lib/pkgconfig"
    export PKG_CONFIG_PATH 
fi
```


The variable PKG_CONFIG_PATH is used by the pkg-config command.

## The results
Once this is done, matplotlib reports the correction version of 'freetype' 


```
Not building any matplotlib graphical backends.
============================================================================
BUILDING MATPLOTLIB
            matplotlib: 0.99.1
                python: 2.6.4 (r264:75706, Jun  6 2010, 00:37:24)  [GCC
                        4.4.3]
              platform: sunos5

REQUIRED DEPENDENCIES
                 numpy: 1.3.0
             freetype2: 9.16.3

OPTIONAL BACKEND DEPENDENCIES
                libpng: 1.2.35
                  Gtk+: no

```



---

Attachment

Patch for sage-env


---

Comment by drkirkby created at 2010-06-10 23:21:51

Changing status from new to needs_review.


---

Comment by jason created at 2010-06-10 23:55:52

Yep, I came to the same conclusion on the plane today, and even have virtually the same patch on my laptop now.

Unfortunately, this is only part of the problem.  When you move the Sage directory, the SAGE_LOCAL/lib/pkgconfig/ files are not updated, so everything breaks again.  I have another patch which rewrites SAGE_ROOT/local/bin/sage-location to fix this problem and lots of other portability issues with that file.  I'll post that to another ticket.


---

Comment by jason created at 2010-06-10 23:57:47

There is a typo in the patch: "leasat" -> "least".

Snow leopard has pkg-config (at least, mine does, but it might just come from macports...)

Incidentally, this will also probably solve some long-standing issues with macports and Sage, and may also solve the problem that generated the libpng12 kludge that we do.


---

Attachment

Spelling mistake corrected


---

Comment by drkirkby created at 2010-06-11 00:32:59

I meant to overwrite the patch when I corrected the spelling, but forgot, so there is now 9208.2.patch. 

Are you suggesting this gets reviewed and incorporated into Sage and you write another patch which rewrites sage-env if Sage is moved? If so, then this still needs reviewing. 

Dave


---

Comment by drkirkby created at 2010-06-11 00:32:59

Changing assignee from GeorgSWeber to drkirkby.


---

Comment by jason created at 2010-06-11 04:17:27

Replying to [comment:7 drkirkby]:
> I meant to overwrite the patch when I corrected the spelling, but forgot, so there is now 9208.2.patch. 
> 
> Are you suggesting this gets reviewed and incorporated into Sage and you write another patch which rewrites sage-env if Sage is moved? 

Not sage-env.  See #9210 for the patch I talked about.

> If so, then this still needs reviewing. 
> 

Yes.  Since I practically had the same patch, but you beat me to posting it, I think the review will be easy.

I didn't check for the existence of PKG_CONFIG_PATH, though.  In what situation will we not want to overwrite that variable?


---

Comment by drkirkby created at 2010-06-11 10:55:06

Replying to [comment:8 jason]:
> Replying to [comment:7 drkirkby]:
> > I meant to overwrite the patch when I corrected the spelling, but forgot, so there is now 9208.2.patch. 
> > 
> > Are you suggesting this gets reviewed and incorporated into Sage and you write another patch which rewrites sage-env if Sage is moved? 
> 
> Not sage-env.  See #9210 for the patch I talked about.
> 
> > If so, then this still needs reviewing. 
> > 
> 
> Yes.  Since I practically had the same patch, but you beat me to posting it, I think the review will be easy.
> 
> I didn't check for the existence of PKG_CONFIG_PATH, though.  In what situation will we not want to overwrite that variable?
> 
> 
I must admit, I did consider whether it was appropriate to simply overwrite PKG_CONFIG_PATH and ignore whatever the user puts. But I could see some benefits in allowing the user to set this. 

 * If I wanted to use a later version of a library that Sage has, I would be able to do so by putting my libraries in a location of my choosing, and let Sage find them first. 

 * in some cases one might have libraries that Sage lacks, but one wants to use with programs like matplotlib. (GTK could be an exmaple of that). 

Another possibility, is to prepend Sage's path to PKG_CONFIG_PATH, so things in Sage are found first, but others that exist on the system will be found too, since according to the man page of pkg-config on Solaris:


```
User Commands                                       pkg-config(1)

NAME
     pkg-config  -  return  meta  information   about   installed
     libraries
<SNIP>
     PKG_CONFIG_PATH         A   colon-separated   (on   Windows,
                             semicolon-separated)  list of direc-
                             tories to search for .pc files.  The
                             default directory is always searched
                             after searching the  path  specified
                             by   PKG_CONFIG_PATH.   The  default
                             value    of    PKG_CONFIG_PATH    is
                             libdir/pkgconfig,  where  libdir  is
                             the lib directory  where  pkg-config
                             is  installed.  On  Solaris systems,
                             libdir is /usr/lib.

```


PKG_CONFIG_PATH is a colon separated list of paths. Simply overwriting PKG_CONFIG_PATH would make it impossible for someone to get matplotlib to use their version of GTK for example in /usr/local, if they wanted that. 

Doing something about the issue with PKG_CONFIG_PATH is clearly better than doing noting at all, but what is best is a bit subjective. I don't have a strong opinion as to what is best. 

The solution here is the most flexible, as it gives the user complete control, but that flexibility does come at some risk. I suspect the risk is quite small, as I doubt many people set PKG_CONFIG_PATH themselves. If they do, they probably know what they are doing :) 


Dave


---

Comment by kcrisman created at 2010-06-11 17:26:25

> Snow leopard has pkg-config (at least, mine does, but it might just come from macports...)
> 

As far as I can tell, vanilla Snow Leopard doesn't have it unless you get it via Fink or something like that, correct.  (That's the only one I can find.)


---

Comment by kcrisman created at 2010-06-11 17:48:43

I don't know if this is helpful, but when installing a new mpl spkg (which jason knows about):

```
BUILDING MATPLOTLIB
            matplotlib: 1.0.svn
                python: 2.6.4 (r264:75706, May 19 2010, 16:32:34)  [GCC
                        4.2.1 (Apple Inc. build 5659)]
              platform: darwin

REQUIRED DEPENDENCIES
                 numpy: 1.3.0
             freetype2: found, but unknown version (no pkg-config)

OPTIONAL BACKEND DEPENDENCIES
                libpng: found, but unknown version (no pkg-config)
                  Gtk+: no
                        * Building for Gtk+ requires pygtk; you must be able
                        * to "import gtk" in your build/install environment
                    Qt: no
                   Qt4: no
                 Cairo: no

OPTIONAL DATE/TIMEZONE DEPENDENCIES
              datetime: present, version unknown
              dateutil: matplotlib will provide
                  pytz: 2010h

OPTIONAL USETEX DEPENDENCIES
                dvipng: no
           ghostscript: 8.63
                 latex: no

```

and then, while doing the last extension (matplotlib._png)

```
ld: library not found for -lpng
collect2: ld returned 1 exit status
error: command 'g++' failed with exit status 1
Error building matplotlib package.
```

This is after installing this patch and #9210 patch.  After moving Sage and trying again, the same thing happened.  After rolling back #9210 and reverting it, same thing.  After then moving Sage back to its original location (which one of the last error message suggested might be causing a problem, it was looking in a nonexistent local/lib at that point) the same thing happened.  After then reverting this patch as well... the same thing happened.  Just FYI.

And sage -f the standard mpl package went just fine, even though the same info about pkg-config appeared.  Not sure if this is relevant to this ticket, but I hope it is!


---

Comment by jason created at 2010-06-11 18:00:59

Okay, the libpng issue is not related to this issue.  It just means the backup when pkg-config is not found is not sufficient in the matplotlib code.


---

Comment by jason created at 2010-06-11 20:44:24

Changing priority from major to critical.


---

Comment by jason created at 2010-06-11 20:44:24

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-06-11 20:44:24

Looks good to me.  Positive Review.  I'm going to set this as critical (and maybe it should be a blocker), as it is very bad that we link to the system versions of these libraries.


---

Comment by jason created at 2010-06-11 20:44:58

David, can you review #9210, which goes hand-in-hand with this ticket?


---

Comment by drkirkby created at 2010-06-11 21:06:01

Replying to [comment:13 jason]:
> Looks good to me.  Positive Review.  I'm going to set this as critical (and maybe it should be a blocker), as it is very bad that we link to the system versions of these libraries.

I agree it is bad, but I don't think it quite warrants a blocker, as it does not stop Sage building. (I've marked tickets as blockers before, which actually break a build, but they have had to wait). 

But in general, given the arguments given for including a huge amount in the tarball so we can control exactly what library versions get linked, it is a bit dumb if we don't control it! 

I'll look at #9210 now. Unfortunately, it takes a long time to make the binary distribution on my old SPARC, so don't expect a review in the next few hours. 

Dave


---

Comment by rlm created at 2010-06-25 15:40:15

Resolution: fixed


---

Comment by rlm created at 2010-06-25 15:40:15

Applied 9208.2.patch.
