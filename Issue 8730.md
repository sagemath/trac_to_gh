# Issue 8730: cddlib makefile looks for gmp in /usr/local, should be $SAGE_LOCAL

archive/issues_008730.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  dimpase drkirkby\n\nThe current problem with this spkg is that gmp must be in SAGE_LOCAL, and not in /usr/local This stops the thing building on Solaris, see http://groups.google.com/group/sage-release/msg/35b0c600a5ef250f and other messages in this thread. And gmpdir=/usr/local is hardwired in Makefile.am.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8730\n\n",
    "created_at": "2010-04-20T17:30:50Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "cddlib makefile looks for gmp in /usr/local, should be $SAGE_LOCAL",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8730",
    "user": "vbraun"
}
```
Assignee: AlexGhitza

CC:  dimpase drkirkby

The current problem with this spkg is that gmp must be in SAGE_LOCAL, and not in /usr/local This stops the thing building on Solaris, see http://groups.google.com/group/sage-release/msg/35b0c600a5ef250f and other messages in this thread. And gmpdir=/usr/local is hardwired in Makefile.am.



Issue created by migration from https://trac.sagemath.org/ticket/8730





---

archive/issue_comments_079741.json:
```json
{
    "body": "Updated spkg is at \n\nhttp://www.stp.dias.ie/~vbraun/Sage/spkg/cddlib-094f.p6.spkg\n\nI changed gmplib in Makefile.am, re-ran autotools, and added the updated files to patches/. It should work now, but I have no Solaris machine to test on. Please let us know if this fixes the build problem.",
    "created_at": "2010-04-20T17:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79741",
    "user": "vbraun"
}
```

Updated spkg is at 

http://www.stp.dias.ie/~vbraun/Sage/spkg/cddlib-094f.p6.spkg

I changed gmplib in Makefile.am, re-ran autotools, and added the updated files to patches/. It should work now, but I have no Solaris machine to test on. Please let us know if this fixes the build problem.



---

archive/issue_comments_079742.json:
```json
{
    "body": "It builds on t2.math.washington.edu now.",
    "created_at": "2010-04-20T21:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79742",
    "user": "jhpalmieri"
}
```

It builds on t2.math.washington.edu now.



---

archive/issue_comments_079743.json:
```json
{
    "body": "The hg repository in the spkg has unchecked-in changes.  Other than this, is this ready for review?",
    "created_at": "2010-04-21T17:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79743",
    "user": "jhpalmieri"
}
```

The hg repository in the spkg has unchecked-in changes.  Other than this, is this ready for review?



---

archive/issue_comments_079744.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> The hg repository in the spkg has unchecked-in changes.  Other than this, is this ready for review?\n \nIMHO there should be a short explanation (in SPKG.txt?) on how to make modifications to patches. The whole autoconf/automake machinery is not so trivial...\n\nThanks,\nDima",
    "created_at": "2010-04-21T17:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79744",
    "user": "dimpase"
}
```

Replying to [comment:3 jhpalmieri]:
> The hg repository in the spkg has unchecked-in changes.  Other than this, is this ready for review?
 
IMHO there should be a short explanation (in SPKG.txt?) on how to make modifications to patches. The whole autoconf/automake machinery is not so trivial...

Thanks,
Dima



---

archive/issue_comments_079745.json:
```json
{
    "body": "This fixes my build problem under 64-bit Fedora 10, where /usr/local/lib was providing 32-bit libraries and causing linking errors.",
    "created_at": "2010-04-21T18:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79745",
    "user": "kedlaya"
}
```

This fixes my build problem under 64-bit Fedora 10, where /usr/local/lib was providing 32-bit libraries and causing linking errors.



---

archive/issue_comments_079746.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-21T20:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79746",
    "user": "vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079747.json:
```json
{
    "body": "Dima: \"autoreconf -f\" regenerates all auto-generated files. If you want to make changes to the autotools sources you need to read the autoconf manual or ask the friendly package maintainer. Once you understand what autoconf does the organization of the patches/ directory should be self-explanatory (but then, I'm biased :-)\n\nI checked in the changes and the package is ready for review.",
    "created_at": "2010-04-21T20:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79747",
    "user": "vbraun"
}
```

Dima: "autoreconf -f" regenerates all auto-generated files. If you want to make changes to the autotools sources you need to read the autoconf manual or ask the friendly package maintainer. Once you understand what autoconf does the organization of the patches/ directory should be self-explanatory (but then, I'm biased :-)

I checked in the changes and the package is ready for review.



---

archive/issue_comments_079748.json:
```json
{
    "body": "Replying to [comment:6 vbraun]:\n> Dima: \"autoreconf -f\" regenerates all auto-generated files. If you want to make changes to the autotools sources you need to read the autoconf manual or ask the friendly package maintainer. Once you understand what autoconf does the organization of the patches/ directory should be self-explanatory (but then, I'm biased :-)\n\nIMHO it is unusual to have sources and configuration files reside in a directory tree like this one.\nE.g. it's unclear in which directory autoreconf must be run...\nAlthough I must admit last time I messed around with autotools config files 11 years ago. :-)\n\n\n> \n> I checked in the changes and the package is ready for review.",
    "created_at": "2010-04-22T04:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79748",
    "user": "dimpase"
}
```

Replying to [comment:6 vbraun]:
> Dima: "autoreconf -f" regenerates all auto-generated files. If you want to make changes to the autotools sources you need to read the autoconf manual or ask the friendly package maintainer. Once you understand what autoconf does the organization of the patches/ directory should be self-explanatory (but then, I'm biased :-)

IMHO it is unusual to have sources and configuration files reside in a directory tree like this one.
E.g. it's unclear in which directory autoreconf must be run...
Although I must admit last time I messed around with autotools config files 11 years ago. :-)


> 
> I checked in the changes and the package is ready for review.



---

archive/issue_comments_079749.json:
```json
{
    "body": "For the record, autoreconf needs to be run in the build directory. The auto(re)generated files then need to be copied into patches/autogenerated/\n\nIf anybody with a good grasp of autotools has a better idea of how to organize things, I'd be happy to hear your opinion. Ideally we'd fix the automake sources upstream, and take upstream's autogenerated files. I'll try to communicate our patches upstream once we make sure our changes build on all Sage-supported platforms.",
    "created_at": "2010-04-22T09:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79749",
    "user": "vbraun"
}
```

For the record, autoreconf needs to be run in the build directory. The auto(re)generated files then need to be copied into patches/autogenerated/

If anybody with a good grasp of autotools has a better idea of how to organize things, I'd be happy to hear your opinion. Ideally we'd fix the automake sources upstream, and take upstream's autogenerated files. I'll try to communicate our patches upstream once we make sure our changes build on all Sage-supported platforms.



---

archive/issue_comments_079750.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-22T09:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79750",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079751.json:
```json
{
    "body": "I agree with Dima in that the fact patches/autogenerated has files autogenerated by running autoreconf should be stated in SPKG.txt - not just the tickets. It is not obvious to someone that does not know autoconf/automake well.\n\nAlso, I believe the directory autom4te.cache should be copied too. When 'autoreconf' is run, it creates that directory. The only file in there which says it can be safely removed is autom4te.cache/requests. There is nothing to indicate to me that is is safe to remove the other files from autom4te.cache. One might get away with it, but I think it is wrong to not include them. Note this directory is created by autoreconf - not when one runs the configure script.\n\nWhoever wrote the cddlib package in the first place clearly did not understand autoconf/automake. The whole point of using autoconf/automake is to create a configure script where things like the locations of the libraries can be specified as options - they should not be hard-coded in Makefile.am like they are. The file Makefile.am starts with \"Site customizations:\" which should not be necessary.\n\nAlso, there is a file \"ChangeLog?\" and another \"ChangeLog? (Autosaved)\" in the src directory. Couple that with facts there is no LICENSE file, History/News/ChangeLog are all the same, and you get the feeling the developers did not understand autoconf/automake.\n\nWhat I find strange is that libgmp has been in /usr/local/lib for almost 10 months on 't2'\n\nkirkby`@`t2:[/usr/local/lib] $ ls -l /usr/local/lib/libgmp*\n-rw-r--r--   1 nobody   nobody    659804 Jun 27  2009 /usr/local/lib/libgmp.a\n-rwxr-xr-x   1 nobody   nobody       785 Jun 27  2009 /usr/local/lib/libgmp.la\nlrwxrwxrwx   1 nobody   nobody        15 Jun 27  2009 /usr/local/lib/libgmp.so -> libgmp.so.3.5.0\nlrwxrwxrwx   1 nobody   nobody        15 Jun 27  2009 /usr/local/lib/libgmp.so.3 -> libgmp.so.3.5.0\n-rwxr-xr-x   1 nobody   nobody    355108 Jun 27  2009 /usr/local/lib/libgmp.so.3.5.0\nkirkby`@`t2:[/usr/local/lib] $\n\nWhy this should suddenly be a problem is a bit puzzling to me, given cddlib-094f.p5.spkg was merged into sage 4.3.4 and 4.3.4 built on 't2' OK.\n\nDoes anyone know why this suddenly stops working?\n\nBut in principle, I think changing Kakefile.am and regenerating the files with autoreconf is the way to go. I'm just a bit concerned that the autom4te.cache directory is not included. \n\nI think it is important to point out to the upstream developers that having a site customisation file Makefile.am goes totally against the principle of using autoconf/automake. \n\n\nDave",
    "created_at": "2010-04-22T09:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79751",
    "user": "drkirkby"
}
```

I agree with Dima in that the fact patches/autogenerated has files autogenerated by running autoreconf should be stated in SPKG.txt - not just the tickets. It is not obvious to someone that does not know autoconf/automake well.

Also, I believe the directory autom4te.cache should be copied too. When 'autoreconf' is run, it creates that directory. The only file in there which says it can be safely removed is autom4te.cache/requests. There is nothing to indicate to me that is is safe to remove the other files from autom4te.cache. One might get away with it, but I think it is wrong to not include them. Note this directory is created by autoreconf - not when one runs the configure script.

Whoever wrote the cddlib package in the first place clearly did not understand autoconf/automake. The whole point of using autoconf/automake is to create a configure script where things like the locations of the libraries can be specified as options - they should not be hard-coded in Makefile.am like they are. The file Makefile.am starts with "Site customizations:" which should not be necessary.

Also, there is a file "ChangeLog?" and another "ChangeLog? (Autosaved)" in the src directory. Couple that with facts there is no LICENSE file, History/News/ChangeLog are all the same, and you get the feeling the developers did not understand autoconf/automake.

What I find strange is that libgmp has been in /usr/local/lib for almost 10 months on 't2'

kirkby`@`t2:[/usr/local/lib] $ ls -l /usr/local/lib/libgmp*
-rw-r--r--   1 nobody   nobody    659804 Jun 27  2009 /usr/local/lib/libgmp.a
-rwxr-xr-x   1 nobody   nobody       785 Jun 27  2009 /usr/local/lib/libgmp.la
lrwxrwxrwx   1 nobody   nobody        15 Jun 27  2009 /usr/local/lib/libgmp.so -> libgmp.so.3.5.0
lrwxrwxrwx   1 nobody   nobody        15 Jun 27  2009 /usr/local/lib/libgmp.so.3 -> libgmp.so.3.5.0
-rwxr-xr-x   1 nobody   nobody    355108 Jun 27  2009 /usr/local/lib/libgmp.so.3.5.0
kirkby`@`t2:[/usr/local/lib] $

Why this should suddenly be a problem is a bit puzzling to me, given cddlib-094f.p5.spkg was merged into sage 4.3.4 and 4.3.4 built on 't2' OK.

Does anyone know why this suddenly stops working?

But in principle, I think changing Kakefile.am and regenerating the files with autoreconf is the way to go. I'm just a bit concerned that the autom4te.cache directory is not included. 

I think it is important to point out to the upstream developers that having a site customisation file Makefile.am goes totally against the principle of using autoconf/automake. 


Dave



---

archive/issue_comments_079752.json:
```json
{
    "body": "Have any of these issues with cddlib been reported upstream?  The configure script should allow \"--with-gmp=...\" -- we shouldn't have to hack it in ourselves.  Can someone please contact the cddlib people about this, and then change the \"Report Upstream\" field accordingly?\n\n> Why this should suddenly be a problem is a bit puzzling to me, given cddlib-094f.p5.spkg was merged into sage 4.3.4 and 4.3.4 built on 't2' OK.\n\nWell, maybe it's something in my setup on t2 in particular; I haven't heard that Minh (for example) has had this trouble building on t2.  (It also seems to fix Kiran's problem on his linux box.)",
    "created_at": "2010-04-22T15:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79752",
    "user": "jhpalmieri"
}
```

Have any of these issues with cddlib been reported upstream?  The configure script should allow "--with-gmp=..." -- we shouldn't have to hack it in ourselves.  Can someone please contact the cddlib people about this, and then change the "Report Upstream" field accordingly?

> Why this should suddenly be a problem is a bit puzzling to me, given cddlib-094f.p5.spkg was merged into sage 4.3.4 and 4.3.4 built on 't2' OK.

Well, maybe it's something in my setup on t2 in particular; I haven't heard that Minh (for example) has had this trouble building on t2.  (It also seems to fix Kiran's problem on his linux box.)



---

archive/issue_comments_079753.json:
```json
{
    "body": "Replying to [comment:10 jhpalmieri]:\n> Have any of these issues with cddlib been reported upstream?  The configure script should allow \"--with-gmp=...\" -- we shouldn't have to hack it in ourselves.  Can someone please contact the cddlib people about this, and then change the \"Report Upstream\" field accordingly?\n\nI happen to know Komei Fukuda, the cdd(lib) author, (even had a joint paper with him quite a while ago).\nI'll write to him, once the spkg is ready.\n\nDima\n\n\n> \n> > Why this should suddenly be a problem is a bit puzzling to me, given cddlib-094f.p5.spkg was merged into sage 4.3.4 and 4.3.4 built on 't2' OK.\n> \n> Well, maybe it's something in my setup on t2 in particular; I haven't heard that Minh (for example) has had this trouble building on t2.  (It also seems to fix Kiran's problem on his linux box.)",
    "created_at": "2010-04-22T16:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79753",
    "user": "dimpase"
}
```

Replying to [comment:10 jhpalmieri]:
> Have any of these issues with cddlib been reported upstream?  The configure script should allow "--with-gmp=..." -- we shouldn't have to hack it in ourselves.  Can someone please contact the cddlib people about this, and then change the "Report Upstream" field accordingly?

I happen to know Komei Fukuda, the cdd(lib) author, (even had a joint paper with him quite a while ago).
I'll write to him, once the spkg is ready.

Dima


> 
> > Why this should suddenly be a problem is a bit puzzling to me, given cddlib-094f.p5.spkg was merged into sage 4.3.4 and 4.3.4 built on 't2' OK.
> 
> Well, maybe it's something in my setup on t2 in particular; I haven't heard that Minh (for example) has had this trouble building on t2.  (It also seems to fix Kiran's problem on his linux box.)



---

archive/issue_comments_079754.json:
```json
{
    "body": "Replying to [comment:10 jhpalmieri]:\n> Have any of these issues with cddlib been reported upstream?  The configure script should allow \"--with-gmp=...\" -- we shouldn't have to hack it in ourselves.  Can someone please contact the cddlib people about this, and then change the \"Report Upstream\" field accordingly?\n> \n> > Why this should suddenly be a problem is a bit puzzling to me, given cddlib-094f.p5.spkg was merged into sage 4.3.4 and 4.3.4 built on 't2' OK.\n> \n> Well, maybe it's something in my setup on t2 in particular; I haven't heard that Minh (for example) has had this trouble building on t2.  (It also seems to fix Kiran's problem on his linux box.)\n\nFor the record, I started having those problems on my Fedora box already at 4.3.4 (probably when the cddlib spkg was merged).",
    "created_at": "2010-04-22T16:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79754",
    "user": "kedlaya"
}
```

Replying to [comment:10 jhpalmieri]:
> Have any of these issues with cddlib been reported upstream?  The configure script should allow "--with-gmp=..." -- we shouldn't have to hack it in ourselves.  Can someone please contact the cddlib people about this, and then change the "Report Upstream" field accordingly?
> 
> > Why this should suddenly be a problem is a bit puzzling to me, given cddlib-094f.p5.spkg was merged into sage 4.3.4 and 4.3.4 built on 't2' OK.
> 
> Well, maybe it's something in my setup on t2 in particular; I haven't heard that Minh (for example) has had this trouble building on t2.  (It also seems to fix Kiran's problem on his linux box.)

For the record, I started having those problems on my Fedora box already at 4.3.4 (probably when the cddlib spkg was merged).



---

archive/issue_comments_079755.json:
```json
{
    "body": "Replying to [comment:11 dimpase]:\n> I happen to know Komei Fukuda, the cdd(lib) author, (even had a joint paper with him quite a while ago).\n> I'll write to him, once the spkg is ready.\n> \n> Dima\n\nI think he needs to add an AC_ARG_WITH into configure.ac. There must be many packages in Sage which allow the location of gmp to be specified, so there must be plenty of examples of how to do it. I suspect mpfr is probably the best place to look, as the mpfr developers seem to know what they are doing with autoconf/automake. \n\nBut I agree with Dima, that there should be an explanation of what files are in the patches/autogenerated directory. \n\nThere also needs to be a Mercurial patch added on the ticket once the wording is sorted out. \n\nDave",
    "created_at": "2010-04-22T21:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79755",
    "user": "drkirkby"
}
```

Replying to [comment:11 dimpase]:
> I happen to know Komei Fukuda, the cdd(lib) author, (even had a joint paper with him quite a while ago).
> I'll write to him, once the spkg is ready.
> 
> Dima

I think he needs to add an AC_ARG_WITH into configure.ac. There must be many packages in Sage which allow the location of gmp to be specified, so there must be plenty of examples of how to do it. I suspect mpfr is probably the best place to look, as the mpfr developers seem to know what they are doing with autoconf/automake. 

But I agree with Dima, that there should be an explanation of what files are in the patches/autogenerated directory. 

There also needs to be a Mercurial patch added on the ticket once the wording is sorted out. 

Dave



---

archive/issue_comments_079756.json:
```json
{
    "body": "Changing component from algebra to packages.",
    "created_at": "2010-04-22T23:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79756",
    "user": "jhpalmieri"
}
```

Changing component from algebra to packages.



---

archive/issue_comments_079757.json:
```json
{
    "body": "By the way, this is my main blocker ticket for Sage 4.4: without it, Sage doesn't build (for me) on Solaris, nor on certain Fedora setups.  With it, it does.  So if the issues (whether the \"autom4te.cache\" directory is included, and the contents of SPKG.txt) can be settled quickly, that would be great.  Otherwise, we can merge it more or less as is and then deal with follow-up issues on another ticket.",
    "created_at": "2010-04-22T23:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79757",
    "user": "jhpalmieri"
}
```

By the way, this is my main blocker ticket for Sage 4.4: without it, Sage doesn't build (for me) on Solaris, nor on certain Fedora setups.  With it, it does.  So if the issues (whether the "autom4te.cache" directory is included, and the contents of SPKG.txt) can be settled quickly, that would be great.  Otherwise, we can merge it more or less as is and then deal with follow-up issues on another ticket.



---

archive/issue_comments_079758.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-04-22T23:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79758",
    "user": "jhpalmieri"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_079759.json:
```json
{
    "body": "After talking with John about this, let's move followup to a new ticket.    This is just what we have to do because of limited time by the release manager, etc.    Please somebody make a new ticket and summarize what needs to be done next to make this stuff perfect.\n\nAnd David K. -- many thanks for your careful comments above.",
    "created_at": "2010-04-23T23:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79759",
    "user": "was"
}
```

After talking with John about this, let's move followup to a new ticket.    This is just what we have to do because of limited time by the release manager, etc.    Please somebody make a new ticket and summarize what needs to be done next to make this stuff perfect.

And David K. -- many thanks for your careful comments above.



---

archive/issue_comments_079760.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-23T23:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79760",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079761.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-23T23:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79761",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079762.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-24T00:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79762",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_079763.json:
```json
{
    "body": "Followup for the remaining issues raised in this ticket is at #9177",
    "created_at": "2010-06-07T11:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79763",
    "user": "vbraun"
}
```

Followup for the remaining issues raised in this ticket is at #9177



---

archive/issue_comments_079764.json:
```json
{
    "body": "full author name",
    "created_at": "2017-07-19T09:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8730#issuecomment-79764",
    "user": "chapoton"
}
```

full author name
