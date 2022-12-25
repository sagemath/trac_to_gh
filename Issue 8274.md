# Issue 8274: R's spkg-install needs a good overhall.

archive/issues_008274.json:
```json
{
    "body": "Assignee: amhou\n\nCC:  @jasongrout @williamstein @kcrisman @nexttime\n\nThe spkg-install file for R would appear to need a bit of an overhaul, and some thought given to what is actually needed. This is hardly surprising, given the version r-2.6.1 of R reached patch level p22 in Sage! \n\nR was updated by Karl-Dieter Crisman recently, but obviously not checked on Solaris, as R fails to build on Solaris due to a lack of iconv support. But there appear to be several issues, which perhaps need addressing. \n\n* The R installation manual http://cran.r-project.org/doc/manuals/R-admin.pdf documents that fact that there are problems on Linux with early versions of gcc4, but R has been extensively tested with gcc 4.1\n* The configure option --with-iconv=no is used on OS X and Solaris, yet that option is no longer documented. In contrast, the manual says iconv is needed. On Solaris, one gets the message: \n\n\n```\nconfigure: error: a suitable iconv is essential\n```\n\n This specific issue is #8272, though an iconv package has been built, and at the time of writing needs testing (#8191)\n* There is a comment the option '--with-libiconv-prefix' is not working on FreeBSD. In fact, this option is not documented at all in the latest R manual, so perhaps that is why it does not work. \n* The check for X support relies on the file /usr/include/X11/Xwindows.h That file does not exist on Solaris, yet it supports X. Perhaps a better test is needed. \n* There is this patch patches/R.sh.in, which does not appear to me do very much at, as the only significant difference between the version in the patches directory and the version in Sage is commented out. \n {{{\n# HACK for Sage to avoid hardcoding.  NOthing\n# else has been changed in this file.\n#R_HOME_DIR=\"${SAGE_LOCAL}/lib/R/\"\n#SAGEHACK#\n }}} \n The only other change this patch appears to make is probably undesirable, as it overwrites a line of code related to documentation. However, I might be wrong on this, as another patch appears to be related to this. \n* #7865 documents an error on OpenSolaris - I've not verified if this is an issue with the latest R. \n* SAGE64 is not used on any platform other than OX X, so prevents a 64-bit build on OpenSolaris, Solaris, or any other platform which supports the building of 64-bit code by addition of the -m64 option. \n* From a quick read of the R manual, it would appear better performance is possible if certainly libraries exist. It would seem sensible that notices are issues that better performance can be obtained, and how one might go about that. \n\nOverall, with a previous version having reached patch level 22, I suspect this package needs a bit of a cleanup followed by proper testing on multiple platforms.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8274\n\n",
    "created_at": "2010-02-15T18:34:02Z",
    "labels": [
        "component: statistics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "R's spkg-install needs a good overhall.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8274",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: amhou

CC:  @jasongrout @williamstein @kcrisman @nexttime

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

Issue created by migration from https://trac.sagemath.org/ticket/8274





---

archive/issue_comments_073122.json:
```json
{
    "body": "#8285 addresses\n* SAGE64 problem. Now works on any platform, not just OS X. \n* Removes --with-iconv=no option to configure. \n* Improved testing for X, which allows X to be used on Solaris. \n\nThe other issues with R's spkg-install file still remain.",
    "created_at": "2010-02-17T00:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73122",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

#8285 addresses
* SAGE64 problem. Now works on any platform, not just OS X. 
* Removes --with-iconv=no option to configure. 
* Improved testing for X, which allows X to be used on Solaris. 

The other issues with R's spkg-install file still remain.



---

archive/issue_comments_073123.json:
```json
{
    "body": "Adding Leif as I know he like these sort of things! \n\nDave",
    "created_at": "2010-08-20T15:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73123",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Adding Leif as I know he like these sort of things! 

Dave



---

archive/issue_comments_073124.json:
```json
{
    "body": "And **please** move the Rpy spkg out of R's...",
    "created_at": "2010-08-20T15:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73124",
    "user": "https://github.com/nexttime"
}
```

And **please** move the Rpy spkg out of R's...



---

archive/issue_comments_073125.json:
```json
{
    "body": "#9201 and #9668 may also be related. \n\nUpdated the description as well to reflect drkirkby's comment.  However, it is still mystifying to me exactly when R will really compile with png support.\n\nI'm not touching rpy, but you can feel free if you can figure it out.",
    "created_at": "2010-08-20T16:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73125",
    "user": "https://github.com/kcrisman"
}
```

#9201 and #9668 may also be related. 

Updated the description as well to reflect drkirkby's comment.  However, it is still mystifying to me exactly when R will really compile with png support.

I'm not touching rpy, but you can feel free if you can figure it out.



---

archive/issue_comments_073126.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> And **please** move the Rpy spkg out of R's...\n\nThis is #9906.",
    "created_at": "2010-09-13T23:09:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73126",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:4 leif]:
> And **please** move the Rpy spkg out of R's...

This is #9906.



---

archive/issue_comments_073127.json:
```json
{
    "body": "Just to note, R has for a very long time built on Solaris now, so the particular issue with it not building on Solaris has been resolved. But the package is still a mess. \n\nDave",
    "created_at": "2010-10-01T13:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73127",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Just to note, R has for a very long time built on Solaris now, so the particular issue with it not building on Solaris has been resolved. But the package is still a mess. 

Dave



---

archive/issue_comments_073128.json:
```json
{
    "body": "Changing assignee from amhou to tbd.",
    "created_at": "2011-04-19T23:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73128",
    "user": "https://github.com/kcrisman"
}
```

Changing assignee from amhou to tbd.



---

archive/issue_comments_073129.json:
```json
{
    "body": "Since this really isn't about the statistics, I'm moving this to packages issues.",
    "created_at": "2011-04-19T23:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73129",
    "user": "https://github.com/kcrisman"
}
```

Since this really isn't about the statistics, I'm moving this to packages issues.



---

archive/issue_comments_073130.json:
```json
{
    "body": "Changing component from statistics to packages.",
    "created_at": "2011-04-19T23:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73130",
    "user": "https://github.com/kcrisman"
}
```

Changing component from statistics to packages.



---

archive/issue_comments_073131.json:
```json
{
    "body": "There seem to still be hardcoding issues as well.  See [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/1d21e08c3eae8d33).\n\n```\nWarning: R include directory is empty -- perhaps need to install R- \ndevel.rpm or similar \nmake: /Users/buildbot/build/sage/bsd-1/bsd_64_binary/build/sage-4.7/ \nlocal/lib/R/share/make/shlib.mk: No such file or directory \nmake: *** No rule to make target `/Users/buildbot/build/sage/bsd-1/ \nbsd_64_binary/build/sage-4.7/local/lib/R/share/make/shlib.mk'.  Stop. \nERROR: compilation failed for package \u2018actuar\u2019 \n* removing \u2018/Applications/Sage-4.7-OSX-64bit-10.6.app/Contents/ \nResources/sage/local/lib/R/library/actuar\u2019 \nThe downloaded packages are in \n        \u2018/private/var/folders/D8/D8+XDdMDEJ4XIybIIPvnt++++TQ/-Tmp-/RtmpZeAJMz/ \ndownloaded_packages\u2019 \nUpdating HTML index of packages in '.Library' \nWarning messages: \n1: In install.packages(\"actuar\") : \n  installation of package 'actuar' had non-zero exit status \n2: In file.create(f.tg) : \n  cannot create file '/Users/buildbot/build/sage/bsd-1/bsd_64_binary/ \nbuild/sage-4.7/local/lib/R/doc/html/packages.html', reason 'No such \nfile or directory' \n3: In tools:::unix.packages.html(.Library) : \n  cannot create HTML package index \n```\n",
    "created_at": "2011-06-16T15:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73131",
    "user": "https://github.com/kcrisman"
}
```

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

archive/issue_comments_073132.json:
```json
{
    "body": "Conceivably related, from a sage-support thread where someone had trouble moving the Mac version.  Just for reference.\n\n```\nThe problem was with hard-coded paths, not the \npermissions.  Anyway, the fix was easy.  I opened all the files listed \nabove by George: \nsage/local/lib/R/bin/R \nsage/local/lib/R/bin/libtool \nsage/local/lib/R/etc/Makeconf \nsage/local/lib/R/etc/ldpath \nsage/local/lib/R/etc/Renviron \nsage/local/bin/R \nand edited obvious lines containing hardcoded paths (using find- \nreplace-all at once). \n```\n",
    "created_at": "2011-06-21T14:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73132",
    "user": "https://github.com/kcrisman"
}
```

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

archive/issue_comments_073133.json:
```json
{
    "body": "It would be helpful to know what exactly needs to be cleaned up. \n* The hardcoding issues are at #9668.\n* The R.sh.in thing is currently used, though it's not clear; #9906 clarifies this\n\n```\n+=== Patches ===\n+ * src/src/scripts/R.sh.in:\n+   Only adds a comment (\"#SAGEHACK#\") to later, after installation, be\n+   replaced with R_HOME_DIR=\"${SAGE_LOCAL}/lib/R/\", by the Python script\n+   patches/fix_hardcode.\n```\n\n* In fact, #9906 does a LOT of cleanup of the spkg-install.  It looks a lot more readable now.\n* #7865 has its own ticket.\n* The !FreeBSD issue is something that should have its own ticket, if it's still an issue.\n* The gcc4 and \"performance\" issues aren't really about the spkg-install.\n\nSo I propose that this be closed, possibly after opening a ticket for the !FreeBSD issue.  Ideas?",
    "created_at": "2011-08-05T17:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73133",
    "user": "https://github.com/kcrisman"
}
```

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

archive/issue_comments_073134.json:
```json
{
    "body": "Changing keywords from \"\" to \"r-project\".",
    "created_at": "2011-11-20T01:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73134",
    "user": "https://github.com/kcrisman"
}
```

Changing keywords from "" to "r-project".



---

archive/issue_comments_073135.json:
```json
{
    "body": ">  * The !FreeBSD issue is something that should have its own ticket, if it's still an issue.\n\nThis is now #12059.  I am suggesting this is ready for closing.",
    "created_at": "2011-11-20T01:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73135",
    "user": "https://github.com/kcrisman"
}
```

>  * The !FreeBSD issue is something that should have its own ticket, if it's still an issue.

This is now #12059.  I am suggesting this is ready for closing.



---

archive/issue_comments_073136.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-11-20T01:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73136",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073137.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-11-20T01:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73137",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073138.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-11-26T13:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8274#issuecomment-73138",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
