# Issue 9208: Add PKG_CONFIG_PATH to sage-env so problems like matplotlib link properly.

archive/issues_009208.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  wjp jason\n\n## Hardware & associated software\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n## Sage version and relevant software in Sage\nThis issue was discovered with Sage 4.4.3, which includes\n* Freetype 2.5.5, which is also known as version 9.16.3 (see #9202 for more information about this rather strange version numbering used). \n* matplotlib 0.99.1\n\n\n## The problem\nAs discussed here, \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/1d23bf8990fe06d?hl=en\n\n'matplotlib' will find the system version of 'freetype2', rather than the one in Sage, as it relies on the 'pkg-config' command, to determine the version of freetype2, and what compiler options need to be used to link the required freetype2 library. \n\nTherefore, matplolib reports it is configured with version 9.7.3, which is an old version of freetype2 installed under /usr/sfw in Solaris 10 03/05. \n\n\n```\nREQUIRED DEPENDENCIES\n                  numpy: 1.3.0\n              freetype2: 9.7.3\n```\n\n(freetype 9.7.3 is also known as version 2.1.9)\n\n## The solution\nThe solution to this problem is to ensure pkg-config looks into the directory where Sage stores it's .pc files, which is \n\n\n``` \n$SAGE_LOCAL/lib/pkgconfig\n```\n\n\nrather than the default system directory. \n\nThere we find 11 packages have configuration information\n\nThis is easy to resolve, by adding the following 4 lines to sage-env, which ensure pkg-config uses the Sage directory \n\n\n```\nif [ -z \"$PKG_CONFIG_PATH\" ]; then\n    PKG_CONFIG_PATH=\"$SAGE_LOCAL/lib/pkgconfig\"\n    export PKG_CONFIG_PATH \nfi\n```\n\n\nThe variable PKG_CONFIG_PATH is used by the pkg-config command.\n\n## The results\nOnce this is done, matplotlib reports the correction version of 'freetype' \n\n\n```\nNot building any matplotlib graphical backends.\n============================================================================\nBUILDING MATPLOTLIB\n            matplotlib: 0.99.1\n                python: 2.6.4 (r264:75706, Jun  6 2010, 00:37:24)  [GCC\n                        4.4.3]\n              platform: sunos5\n\nREQUIRED DEPENDENCIES\n                 numpy: 1.3.0\n             freetype2: 9.16.3\n\nOPTIONAL BACKEND DEPENDENCIES\n                libpng: 1.2.35\n                  Gtk+: no\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9208\n\n",
    "created_at": "2010-06-10T23:14:17Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Add PKG_CONFIG_PATH to sage-env so problems like matplotlib link properly.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9208",
    "user": "drkirkby"
}
```
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


``` 
$SAGE_LOCAL/lib/pkgconfig
```


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


Issue created by migration from https://trac.sagemath.org/ticket/9208





---

archive/issue_comments_086177.json:
```json
{
    "body": "Attachment\n\nPatch for sage-env",
    "created_at": "2010-06-10T23:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86177",
    "user": "drkirkby"
}
```

Attachment

Patch for sage-env



---

archive/issue_comments_086178.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-10T23:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86178",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086179.json:
```json
{
    "body": "Yep, I came to the same conclusion on the plane today, and even have virtually the same patch on my laptop now.\n\nUnfortunately, this is only part of the problem.  When you move the Sage directory, the SAGE_LOCAL/lib/pkgconfig/ files are not updated, so everything breaks again.  I have another patch which rewrites SAGE_ROOT/local/bin/sage-location to fix this problem and lots of other portability issues with that file.  I'll post that to another ticket.",
    "created_at": "2010-06-10T23:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86179",
    "user": "jason"
}
```

Yep, I came to the same conclusion on the plane today, and even have virtually the same patch on my laptop now.

Unfortunately, this is only part of the problem.  When you move the Sage directory, the SAGE_LOCAL/lib/pkgconfig/ files are not updated, so everything breaks again.  I have another patch which rewrites SAGE_ROOT/local/bin/sage-location to fix this problem and lots of other portability issues with that file.  I'll post that to another ticket.



---

archive/issue_comments_086180.json:
```json
{
    "body": "There is a typo in the patch: \"leasat\" -> \"least\".\n\nSnow leopard has pkg-config (at least, mine does, but it might just come from macports...)\n\nIncidentally, this will also probably solve some long-standing issues with macports and Sage, and may also solve the problem that generated the libpng12 kludge that we do.",
    "created_at": "2010-06-10T23:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86180",
    "user": "jason"
}
```

There is a typo in the patch: "leasat" -> "least".

Snow leopard has pkg-config (at least, mine does, but it might just come from macports...)

Incidentally, this will also probably solve some long-standing issues with macports and Sage, and may also solve the problem that generated the libpng12 kludge that we do.



---

archive/issue_comments_086181.json:
```json
{
    "body": "Attachment\n\nSpelling mistake corrected",
    "created_at": "2010-06-11T00:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86181",
    "user": "drkirkby"
}
```

Attachment

Spelling mistake corrected



---

archive/issue_comments_086182.json:
```json
{
    "body": "I meant to overwrite the patch when I corrected the spelling, but forgot, so there is now 9208.2.patch. \n\nAre you suggesting this gets reviewed and incorporated into Sage and you write another patch which rewrites sage-env if Sage is moved? If so, then this still needs reviewing. \n\nDave",
    "created_at": "2010-06-11T00:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86182",
    "user": "drkirkby"
}
```

I meant to overwrite the patch when I corrected the spelling, but forgot, so there is now 9208.2.patch. 

Are you suggesting this gets reviewed and incorporated into Sage and you write another patch which rewrites sage-env if Sage is moved? If so, then this still needs reviewing. 

Dave



---

archive/issue_comments_086183.json:
```json
{
    "body": "Changing assignee from GeorgSWeber to drkirkby.",
    "created_at": "2010-06-11T00:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86183",
    "user": "drkirkby"
}
```

Changing assignee from GeorgSWeber to drkirkby.



---

archive/issue_comments_086184.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> I meant to overwrite the patch when I corrected the spelling, but forgot, so there is now 9208.2.patch. \n> \n> Are you suggesting this gets reviewed and incorporated into Sage and you write another patch which rewrites sage-env if Sage is moved? \n\nNot sage-env.  See #9210 for the patch I talked about.\n\n> If so, then this still needs reviewing. \n> \n\nYes.  Since I practically had the same patch, but you beat me to posting it, I think the review will be easy.\n\nI didn't check for the existence of PKG_CONFIG_PATH, though.  In what situation will we not want to overwrite that variable?",
    "created_at": "2010-06-11T04:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86184",
    "user": "jason"
}
```

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

archive/issue_comments_086185.json:
```json
{
    "body": "Replying to [comment:8 jason]:\n> Replying to [comment:7 drkirkby]:\n> > I meant to overwrite the patch when I corrected the spelling, but forgot, so there is now 9208.2.patch. \n> > \n> > Are you suggesting this gets reviewed and incorporated into Sage and you write another patch which rewrites sage-env if Sage is moved? \n> \n> Not sage-env.  See #9210 for the patch I talked about.\n> \n> > If so, then this still needs reviewing. \n> > \n> \n> Yes.  Since I practically had the same patch, but you beat me to posting it, I think the review will be easy.\n> \n> I didn't check for the existence of PKG_CONFIG_PATH, though.  In what situation will we not want to overwrite that variable?\n> \n> \nI must admit, I did consider whether it was appropriate to simply overwrite PKG_CONFIG_PATH and ignore whatever the user puts. But I could see some benefits in allowing the user to set this. \n\n* If I wanted to use a later version of a library that Sage has, I would be able to do so by putting my libraries in a location of my choosing, and let Sage find them first. \n\n* in some cases one might have libraries that Sage lacks, but one wants to use with programs like matplotlib. (GTK could be an exmaple of that). \n\nAnother possibility, is to prepend Sage's path to PKG_CONFIG_PATH, so things in Sage are found first, but others that exist on the system will be found too, since according to the man page of pkg-config on Solaris:\n\n\n```\nUser Commands                                       pkg-config(1)\n\nNAME\n     pkg-config  -  return  meta  information   about   installed\n     libraries\n<SNIP>\n     PKG_CONFIG_PATH         A   colon-separated   (on   Windows,\n                             semicolon-separated)  list of direc-\n                             tories to search for .pc files.  The\n                             default directory is always searched\n                             after searching the  path  specified\n                             by   PKG_CONFIG_PATH.   The  default\n                             value    of    PKG_CONFIG_PATH    is\n                             libdir/pkgconfig,  where  libdir  is\n                             the lib directory  where  pkg-config\n                             is  installed.  On  Solaris systems,\n                             libdir is /usr/lib.\n\n```\n\n\nPKG_CONFIG_PATH is a colon separated list of paths. Simply overwriting PKG_CONFIG_PATH would make it impossible for someone to get matplotlib to use their version of GTK for example in /usr/local, if they wanted that. \n\nDoing something about the issue with PKG_CONFIG_PATH is clearly better than doing noting at all, but what is best is a bit subjective. I don't have a strong opinion as to what is best. \n\nThe solution here is the most flexible, as it gives the user complete control, but that flexibility does come at some risk. I suspect the risk is quite small, as I doubt many people set PKG_CONFIG_PATH themselves. If they do, they probably know what they are doing :) \n\n\nDave",
    "created_at": "2010-06-11T10:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86185",
    "user": "drkirkby"
}
```

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

archive/issue_comments_086186.json:
```json
{
    "body": "> Snow leopard has pkg-config (at least, mine does, but it might just come from macports...)\n> \n\nAs far as I can tell, vanilla Snow Leopard doesn't have it unless you get it via Fink or something like that, correct.  (That's the only one I can find.)",
    "created_at": "2010-06-11T17:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86186",
    "user": "kcrisman"
}
```

> Snow leopard has pkg-config (at least, mine does, but it might just come from macports...)
> 

As far as I can tell, vanilla Snow Leopard doesn't have it unless you get it via Fink or something like that, correct.  (That's the only one I can find.)



---

archive/issue_comments_086187.json:
```json
{
    "body": "I don't know if this is helpful, but when installing a new mpl spkg (which jason knows about):\n\n```\nBUILDING MATPLOTLIB\n            matplotlib: 1.0.svn\n                python: 2.6.4 (r264:75706, May 19 2010, 16:32:34)  [GCC\n                        4.2.1 (Apple Inc. build 5659)]\n              platform: darwin\n\nREQUIRED DEPENDENCIES\n                 numpy: 1.3.0\n             freetype2: found, but unknown version (no pkg-config)\n\nOPTIONAL BACKEND DEPENDENCIES\n                libpng: found, but unknown version (no pkg-config)\n                  Gtk+: no\n                        * Building for Gtk+ requires pygtk; you must be able\n                        * to \"import gtk\" in your build/install environment\n                    Qt: no\n                   Qt4: no\n                 Cairo: no\n\nOPTIONAL DATE/TIMEZONE DEPENDENCIES\n              datetime: present, version unknown\n              dateutil: matplotlib will provide\n                  pytz: 2010h\n\nOPTIONAL USETEX DEPENDENCIES\n                dvipng: no\n           ghostscript: 8.63\n                 latex: no\n\n```\n\nand then, while doing the last extension (matplotlib._png)\n\n```\nld: library not found for -lpng\ncollect2: ld returned 1 exit status\nerror: command 'g++' failed with exit status 1\nError building matplotlib package.\n```\n\nThis is after installing this patch and #9210 patch.  After moving Sage and trying again, the same thing happened.  After rolling back #9210 and reverting it, same thing.  After then moving Sage back to its original location (which one of the last error message suggested might be causing a problem, it was looking in a nonexistent local/lib at that point) the same thing happened.  After then reverting this patch as well... the same thing happened.  Just FYI.\n\nAnd sage -f the standard mpl package went just fine, even though the same info about pkg-config appeared.  Not sure if this is relevant to this ticket, but I hope it is!",
    "created_at": "2010-06-11T17:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86187",
    "user": "kcrisman"
}
```

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

archive/issue_comments_086188.json:
```json
{
    "body": "Okay, the libpng issue is not related to this issue.  It just means the backup when pkg-config is not found is not sufficient in the matplotlib code.",
    "created_at": "2010-06-11T18:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86188",
    "user": "jason"
}
```

Okay, the libpng issue is not related to this issue.  It just means the backup when pkg-config is not found is not sufficient in the matplotlib code.



---

archive/issue_comments_086189.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-06-11T20:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86189",
    "user": "jason"
}
```

Changing priority from major to critical.



---

archive/issue_comments_086190.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-11T20:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86190",
    "user": "jason"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086191.json:
```json
{
    "body": "Looks good to me.  Positive Review.  I'm going to set this as critical (and maybe it should be a blocker), as it is very bad that we link to the system versions of these libraries.",
    "created_at": "2010-06-11T20:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86191",
    "user": "jason"
}
```

Looks good to me.  Positive Review.  I'm going to set this as critical (and maybe it should be a blocker), as it is very bad that we link to the system versions of these libraries.



---

archive/issue_comments_086192.json:
```json
{
    "body": "David, can you review #9210, which goes hand-in-hand with this ticket?",
    "created_at": "2010-06-11T20:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86192",
    "user": "jason"
}
```

David, can you review #9210, which goes hand-in-hand with this ticket?



---

archive/issue_comments_086193.json:
```json
{
    "body": "Replying to [comment:13 jason]:\n> Looks good to me.  Positive Review.  I'm going to set this as critical (and maybe it should be a blocker), as it is very bad that we link to the system versions of these libraries.\n\nI agree it is bad, but I don't think it quite warrants a blocker, as it does not stop Sage building. (I've marked tickets as blockers before, which actually break a build, but they have had to wait). \n\nBut in general, given the arguments given for including a huge amount in the tarball so we can control exactly what library versions get linked, it is a bit dumb if we don't control it! \n\nI'll look at #9210 now. Unfortunately, it takes a long time to make the binary distribution on my old SPARC, so don't expect a review in the next few hours. \n\nDave",
    "created_at": "2010-06-11T21:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86193",
    "user": "drkirkby"
}
```

Replying to [comment:13 jason]:
> Looks good to me.  Positive Review.  I'm going to set this as critical (and maybe it should be a blocker), as it is very bad that we link to the system versions of these libraries.

I agree it is bad, but I don't think it quite warrants a blocker, as it does not stop Sage building. (I've marked tickets as blockers before, which actually break a build, but they have had to wait). 

But in general, given the arguments given for including a huge amount in the tarball so we can control exactly what library versions get linked, it is a bit dumb if we don't control it! 

I'll look at #9210 now. Unfortunately, it takes a long time to make the binary distribution on my old SPARC, so don't expect a review in the next few hours. 

Dave



---

archive/issue_comments_086194.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86194",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_086195.json:
```json
{
    "body": "Applied 9208.2.patch.",
    "created_at": "2010-06-25T15:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9208#issuecomment-86195",
    "user": "rlm"
}
```

Applied 9208.2.patch.
