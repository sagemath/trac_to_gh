# Issue 8274: R's spkg-install needs a good overhall.

Issue created by migration from https://trac.sagemath.org/ticket/8274

Original creator: drkirkby

Original creation time: 2010-02-15 18:34:02

Assignee: amhou

CC:  jason was kcrisman leif

The spkg-install file for R would appear to need a bit of an overhaul, and some thought given to what is actually needed. This is hardly surprising, given the version r-2.6.1 of R reached patch level p22 in Sage! 

R was updated by Karl-Dieter Crisman recently, but obviously not checked on Solaris, as R fails to build on Solaris due to a lack of iconv support. But there appear to be several issues, which perhaps need addressing. 

 * The R installation manual http://cran.r-project.org/doc/manuals/R-admin.pdf documents that fact that there are problems on Linux with early versions of gcc4, but R has been extensively tested with gcc 4.1
 * The configure option --with-iconv=no is used on OS X and Solaris, yet that option is no longer documented. In contrast, the manual says iconv is needed. On Solaris, one gets the message: 


```
configure: error: a suitable iconv is essential
```

 This specific issue is #8272, though an iconv package has been built, and at the time of writing needs testing (#8191)
 * There is a comment the option '--with-libiconv-prefix' is not working on FreeBSD. In fact, this option is not documented at all in the latest R manual, so perhaps that is why it does not work. 
 * The check for X support relies on the file /usr/include/X11/Xwindows.h That file does not exist on Solaris, yet it supports X. Perhaps a better test is needed. 
 * There is this patch patches/R.sh.in, which does not appear to me do very much at, as the only significant difference between the version in the patches directory and the version in Sage is commented out. 
 {{{
# HACK for Sage to avoid hardcoding.  NOthing
# else has been changed in this file.
#R_HOME_DIR="${SAGE_LOCAL}/lib/R/"
#SAGEHACK#
 }}} 
 The only other change this patch appears to make is probably undesirable, as it overwrites a line of code related to documentation. However, I might be wrong on this, as another patch appears to be related to this. 
 * #7865 documents an error on OpenSolaris - I've not verified if this is an issue with the latest R. 
 * SAGE64 is not used on any platform other than OX X, so prevents a 64-bit build on OpenSolaris, Solaris, or any other platform which supports the building of 64-bit code by addition of the -m64 option. 
 * From a quick read of the R manual, it would appear better performance is possible if certainly libraries exist. It would seem sensible that notices are issues that better performance can be obtained, and how one might go about that. 

Overall, with a previous version having reached patch level 22, I suspect this package needs a bit of a cleanup followed by proper testing on multiple platforms.


---

Comment by drkirkby created at 2010-02-17 00:59:22

#8285 addresses
 * SAGE64 problem. Now works on any platform, not just OS X. 
 * Removes --with-iconv=no option to configure. 
 * Improved testing for X, which allows X to be used on Solaris. 

The other issues with R's spkg-install file still remain.


---

Comment by drkirkby created at 2010-08-20 15:33:38

Adding Leif as I know he like these sort of things! 

Dave


---

Comment by leif created at 2010-08-20 15:59:36

And *please* move the Rpy spkg out of R's...


---

Comment by kcrisman created at 2010-08-20 16:01:23

#9201 and #9668 may also be related. 

Updated the description as well to reflect drkirkby's comment.  However, it is still mystifying to me exactly when R will really compile with png support.

I'm not touching rpy, but you can feel free if you can figure it out.


---

Comment by mpatel created at 2010-09-13 23:09:18

Replying to [comment:4 leif]:
> And *please* move the Rpy spkg out of R's...

This is #9906.


---

Comment by drkirkby created at 2010-10-01 13:41:28

Just to note, R has for a very long time built on Solaris now, so the particular issue with it not building on Solaris has been resolved. But the package is still a mess. 

Dave


---

Comment by kcrisman created at 2011-04-19 23:58:31

Changing assignee from amhou to tbd.


---

Comment by kcrisman created at 2011-04-19 23:58:31

Since this really isn't about the statistics, I'm moving this to packages issues.


---

Comment by kcrisman created at 2011-04-19 23:58:31

Changing component from statistics to packages.


---

Comment by kcrisman created at 2011-06-16 15:13:12

There seem to still be hardcoding issues as well.  See [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/1d21e08c3eae8d33).

```
Warning: R include directory is empty -- perhaps need to install R- 
devel.rpm or similar 
make: /Users/buildbot/build/sage/bsd-1/bsd_64_binary/build/sage-4.7/ 
local/lib/R/share/make/shlib.mk: No such file or directory 
make: *** No rule to make target `/Users/buildbot/build/sage/bsd-1/ 
bsd_64_binary/build/sage-4.7/local/lib/R/share/make/shlib.mk'.  Stop. 
ERROR: compilation failed for package ‘actuar’ 
* removing ‘/Applications/Sage-4.7-OSX-64bit-10.6.app/Contents/ 
Resources/sage/local/lib/R/library/actuar’ 
The downloaded packages are in 
        ‘/private/var/folders/D8/D8+XDdMDEJ4XIybIIPvnt++++TQ/-Tmp-/RtmpZeAJMz/ 
downloaded_packages’ 
Updating HTML index of packages in '.Library' 
Warning messages: 
1: In install.packages("actuar") : 
  installation of package 'actuar' had non-zero exit status 
2: In file.create(f.tg) : 
  cannot create file '/Users/buildbot/build/sage/bsd-1/bsd_64_binary/ 
build/sage-4.7/local/lib/R/doc/html/packages.html', reason 'No such 
file or directory' 
3: In tools:::unix.packages.html(.Library) : 
  cannot create HTML package index 
```



---

Comment by kcrisman created at 2011-06-21 14:55:24

Conceivably related, from a sage-support thread where someone had trouble moving the Mac version.  Just for reference.

```
The problem was with hard-coded paths, not the 
permissions.  Anyway, the fix was easy.  I opened all the files listed 
above by George: 
sage/local/lib/R/bin/R 
sage/local/lib/R/bin/libtool 
sage/local/lib/R/etc/Makeconf 
sage/local/lib/R/etc/ldpath 
sage/local/lib/R/etc/Renviron 
sage/local/bin/R 
and edited obvious lines containing hardcoded paths (using find- 
replace-all at once). 
```



---

Comment by kcrisman created at 2011-08-05 17:58:19

It would be helpful to know what exactly needs to be cleaned up. 
 * The hardcoding issues are at #9668.
 * The R.sh.in thing is currently used, though it's not clear; #9906 clarifies this

```
+=== Patches ===
+ * src/src/scripts/R.sh.in:
+   Only adds a comment ("#SAGEHACK#") to later, after installation, be
+   replaced with R_HOME_DIR="${SAGE_LOCAL}/lib/R/", by the Python script
+   patches/fix_hardcode.
```

 * In fact, #9906 does a LOT of cleanup of the spkg-install.  It looks a lot more readable now.
 * #7865 has its own ticket.
 * The !FreeBSD issue is something that should have its own ticket, if it's still an issue.
 * The gcc4 and "performance" issues aren't really about the spkg-install.

So I propose that this be closed, possibly after opening a ticket for the !FreeBSD issue.  Ideas?


---

Comment by kcrisman created at 2011-11-20 01:15:28

Changing keywords from "" to "r-project".


---

Comment by kcrisman created at 2011-11-20 01:15:28

>  * The !FreeBSD issue is something that should have its own ticket, if it's still an issue.

This is now #12059.  I am suggesting this is ready for closing.


---

Comment by kcrisman created at 2011-11-20 01:15:28

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-11-20 01:15:34

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-11-26 13:02:46

Resolution: duplicate
