# Issue 9187: Update ECL's spkg-install for building multiple spkgs in parallel

archive/issues_009187.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  drkirkby @jhpalmieri @nexttime @jaapspies\n\nTo build ECL with `SAGE_PARALLEL_SPKG_BUILD=\"yes\"` on Mac OS X, we need to add, e.g.,\n\n```sh\nMAKEFLAGS=\nexport MAKEFLAGS\n```\n\nto the package's `spkg-install`.\n\nPlease see #8306 about building spkgs in parallel.  For `MAKEFLAGS`, see [the GNU Make manual](http://www.gnu.org/software/make/manual/html_node/Options_002fRecursion.html).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9187\n\n",
    "created_at": "2010-06-08T08:42:58Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Update ECL's spkg-install for building multiple spkgs in parallel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9187",
    "user": "https://github.com/qed777"
}
```
Assignee: tbd

CC:  drkirkby @jhpalmieri @nexttime @jaapspies

To build ECL with `SAGE_PARALLEL_SPKG_BUILD="yes"` on Mac OS X, we need to add, e.g.,

```sh
MAKEFLAGS=
export MAKEFLAGS
```

to the package's `spkg-install`.

Please see #8306 about building spkgs in parallel.  For `MAKEFLAGS`, see [the GNU Make manual](http://www.gnu.org/software/make/manual/html_node/Options_002fRecursion.html).

Issue created by migration from https://trac.sagemath.org/ticket/9187





---

archive/issue_comments_085795.json:
```json
{
    "body": "I think we should work from #8951.",
    "created_at": "2010-06-08T09:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85795",
    "user": "https://github.com/qed777"
}
```

I think we should work from #8951.



---

archive/issue_comments_085796.json:
```json
{
    "body": "spkg patch.  Set empty `MAKEFLAGS`.",
    "created_at": "2010-06-09T02:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85796",
    "user": "https://github.com/qed777"
}
```

spkg patch.  Set empty `MAKEFLAGS`.



---

archive/issue_comments_085797.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-09T02:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85797",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085798.json:
```json
{
    "body": "Attachment [trac_9187-ecl_makeflags.patch](tarball://root/attachments/some-uuid/ticket9187/trac_9187-ecl_makeflags.patch) by @qed777 created at 2010-06-09 02:30:02\n\nI've put a new spkg at\n\n* http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.4.1.p0.spkg\n\n(Or should it be p1?)  This is based against the package mentioned in [comment:ticket:8951:10 this comment] at #8951.",
    "created_at": "2010-06-09T02:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85798",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9187-ecl_makeflags.patch](tarball://root/attachments/some-uuid/ticket9187/trac_9187-ecl_makeflags.patch) by @qed777 created at 2010-06-09 02:30:02

I've put a new spkg at

* http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.4.1.p0.spkg

(Or should it be p1?)  This is based against the package mentioned in [comment:ticket:8951:10 this comment] at #8951.



---

archive/issue_comments_085799.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2010-06-18T12:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85799",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_085800.json:
```json
{
    "body": "Unfortunately, there are two spkgs on #8951 and neither have the patches from #8089 and both claim in SPKG.txt to have things they do not. \n\nI intend creating a 10.4.1 package which has this, and all other relevant fixes in the one package. Since no ecl-10.4.1.spkg has been merged, this should be called ecl-10.4.1.spkg. The patch levels start at 0, not 1, but in this case as nothing has been merged, there is no need to increment the patch level. \n\nPlease see #9264, which will have these changes, those which are listed as being in #8591 but are not, and also that at #8089\n\nDave",
    "created_at": "2010-06-18T12:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85800",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Unfortunately, there are two spkgs on #8951 and neither have the patches from #8089 and both claim in SPKG.txt to have things they do not. 

I intend creating a 10.4.1 package which has this, and all other relevant fixes in the one package. Since no ecl-10.4.1.spkg has been merged, this should be called ecl-10.4.1.spkg. The patch levels start at 0, not 1, but in this case as nothing has been merged, there is no need to increment the patch level. 

Please see #9264, which will have these changes, those which are listed as being in #8591 but are not, and also that at #8089

Dave



---

archive/issue_comments_085801.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-18T17:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85801",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085802.json:
```json
{
    "body": "The attached patch is ok and deserves positive review. However, the .spkg attached is not ideal, as it overlooks some other changes which need merging. I think a new .spkg needs to be created, which has all the minor changes together.",
    "created_at": "2010-06-18T17:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85802",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The attached patch is ok and deserves positive review. However, the .spkg attached is not ideal, as it overlooks some other changes which need merging. I think a new .spkg needs to be created, which has all the minor changes together.



---

archive/issue_comments_085803.json:
```json
{
    "body": "There is no need to merge this now. \n\n#9264, which has positive review, includes this patch, along with several others related to ECL. All the relevant problems with ECL are solved by #9264, including this one. \n\nDave",
    "created_at": "2010-06-21T08:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85803",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

There is no need to merge this now. 

#9264, which has positive review, includes this patch, along with several others related to ECL. All the relevant problems with ECL are solved by #9264, including this one. 

Dave



---

archive/issue_comments_085804.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-06-25T11:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85804",
    "user": "https://github.com/rlmill"
}
```

Resolution: duplicate



---

archive/issue_comments_085805.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2010-07-12T01:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85805",
    "user": "https://github.com/qed777"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_085806.json:
```json
{
    "body": "Related tickets: #9264, #9460, #9474.",
    "created_at": "2010-07-12T01:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85806",
    "user": "https://github.com/qed777"
}
```

Related tickets: #9264, #9460, #9474.



---

archive/issue_comments_085807.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-07-12T01:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85807",
    "user": "https://github.com/qed777"
}
```

Changing status from closed to new.



---

archive/issue_comments_085808.json:
```json
{
    "body": "spkg patch rebased vs. #9474.",
    "created_at": "2010-07-12T20:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85808",
    "user": "https://github.com/qed777"
}
```

spkg patch rebased vs. #9474.



---

archive/issue_comments_085809.json:
```json
{
    "body": "Attachment [trac_9187-ecl_makeflags.2.patch](tarball://root/attachments/some-uuid/ticket9187/trac_9187-ecl_makeflags.2.patch) by @qed777 created at 2010-07-12 20:32:07\n\nHere's a new spkg based on #9474:\n\n http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg\n\nIt works for me with 4.5.rc0 + #7379 on sage.math, but I have not yet had a chance to test it on bsd.math.",
    "created_at": "2010-07-12T20:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85809",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9187-ecl_makeflags.2.patch](tarball://root/attachments/some-uuid/ticket9187/trac_9187-ecl_makeflags.2.patch) by @qed777 created at 2010-07-12 20:32:07

Here's a new spkg based on #9474:

 http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg

It works for me with 4.5.rc0 + #7379 on sage.math, but I have not yet had a chance to test it on bsd.math.



---

archive/issue_comments_085810.json:
```json
{
    "body": "This works for me on sage.math and on an OS X box running 10.6, in both cases building spkg's in parallel.  I'm building on t2 now; if there are problems, I'll report them.",
    "created_at": "2010-07-12T21:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85810",
    "user": "https://github.com/jhpalmieri"
}
```

This works for me on sage.math and on an OS X box running 10.6, in both cases building spkg's in parallel.  I'm building on t2 now; if there are problems, I'll report them.



---

archive/issue_comments_085811.json:
```json
{
    "body": "Replying to [comment:9 mpatel]:\n> Here's a new spkg based on #9474:\n> \n>  http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg\n> \n> It works for me with 4.5.rc0 + #7379 on sage.math, but I have not yet had a chance to test it on bsd.math.\n\nIt works for me on bsd.math - at least ecl builds ok. I've not at this time completed the build, but ecl has built ok.",
    "created_at": "2010-07-12T21:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85811",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:9 mpatel]:
> Here's a new spkg based on #9474:
> 
>  http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg
> 
> It works for me with 4.5.rc0 + #7379 on sage.math, but I have not yet had a chance to test it on bsd.math.

It works for me on bsd.math - at least ecl builds ok. I've not at this time completed the build, but ecl has built ok.



---

archive/issue_comments_085812.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n\n> It works for me on bsd.math - at least ecl builds ok. I've not at this time completed the build, but ecl has built ok. \n\nThat's what I meant, too.  The same is also true on t2 now: this version of ecl has built successfully as part of a parallel build, but the full build has several more hours to go...",
    "created_at": "2010-07-12T21:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85812",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:11 drkirkby]:

> It works for me on bsd.math - at least ecl builds ok. I've not at this time completed the build, but ecl has built ok. 

That's what I meant, too.  The same is also true on t2 now: this version of ecl has built successfully as part of a parallel build, but the full build has several more hours to go...



---

archive/issue_comments_085813.json:
```json
{
    "body": "I am testing a new build (on 64-bit ubuntu) of 4.5.rc0 + http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg with SAGE_PARALLEL_SPKG_BUILD=\"yes\" (which I have never tried before) and will report back.  Though these ecl tickets are so confusing that I am not sure this will tell anyone anything useful, I thought it would be fun.  (The other users of the machine may not agree, of course!)",
    "created_at": "2010-07-13T16:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85813",
    "user": "https://github.com/JohnCremona"
}
```

I am testing a new build (on 64-bit ubuntu) of 4.5.rc0 + http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg with SAGE_PARALLEL_SPKG_BUILD="yes" (which I have never tried before) and will report back.  Though these ecl tickets are so confusing that I am not sure this will tell anyone anything useful, I thought it would be fun.  (The other users of the machine may not agree, of course!)



---

archive/issue_comments_085814.json:
```json
{
    "body": "Replying to [comment:13 cremona]:\n> I am testing a new build (on 64-bit ubuntu) of 4.5.rc0 + http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg with SAGE_PARALLEL_SPKG_BUILD=\"yes\" (which I have never tried before) and will report back.  Though these ecl tickets are so confusing that I am not sure this will tell anyone anything useful, I thought it would be fun.  (The other users of the machine may not agree, of course!)\n\nI think you test results will be very useful, as there is a distinct lack of direct evidence for this working on Linux. There is evidence it is working on OS X and Solaris. \n\nYou also need to export MAKE, with something like\n\n$ export MAKE=\"make -j6\"\n\nor however many threads you want. Do not put a space between the 'j' and the '6'. \n\nDave",
    "created_at": "2010-07-13T16:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85814",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:13 cremona]:
> I am testing a new build (on 64-bit ubuntu) of 4.5.rc0 + http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg with SAGE_PARALLEL_SPKG_BUILD="yes" (which I have never tried before) and will report back.  Though these ecl tickets are so confusing that I am not sure this will tell anyone anything useful, I thought it would be fun.  (The other users of the machine may not agree, of course!)

I think you test results will be very useful, as there is a distinct lack of direct evidence for this working on Linux. There is evidence it is working on OS X and Solaris. 

You also need to export MAKE, with something like

$ export MAKE="make -j6"

or however many threads you want. Do not put a space between the 'j' and the '6'. 

Dave



---

archive/issue_comments_085815.json:
```json
{
    "body": "Replying to [comment:14 drkirkby]:\n> Replying to [comment:13 cremona]:\n> > I am testing a new build (on 64-bit ubuntu) of 4.5.rc0 + http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg with SAGE_PARALLEL_SPKG_BUILD=\"yes\" (which I have never tried before) and will report back.  Though these ecl tickets are so confusing that I am not sure this will tell anyone anything useful, I thought it would be fun.  (The other users of the machine may not agree, of course!)\n> \n> I think you test results will be very useful, as there is a distinct lack of direct evidence for this working on Linux. There is evidence it is working on OS X and Solaris. \n> \n> You also need to export MAKE, with something like\n> \n> $ export MAKE=\"make -j6\"\n> \n> or however many threads you want. Do not put a space between the 'j' and the '6'.\n\nThanks -- I use -j 10, and luckily the machine is in an air-conditioned room!\n \n> \n> Dave",
    "created_at": "2010-07-13T16:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85815",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:14 drkirkby]:
> Replying to [comment:13 cremona]:
> > I am testing a new build (on 64-bit ubuntu) of 4.5.rc0 + http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg with SAGE_PARALLEL_SPKG_BUILD="yes" (which I have never tried before) and will report back.  Though these ecl tickets are so confusing that I am not sure this will tell anyone anything useful, I thought it would be fun.  (The other users of the machine may not agree, of course!)
> 
> I think you test results will be very useful, as there is a distinct lack of direct evidence for this working on Linux. There is evidence it is working on OS X and Solaris. 
> 
> You also need to export MAKE, with something like
> 
> $ export MAKE="make -j6"
> 
> or however many threads you want. Do not put a space between the 'j' and the '6'.

Thanks -- I use -j 10, and luckily the machine is in an air-conditioned room!
 
> 
> Dave



---

archive/issue_comments_085816.json:
```json
{
    "body": "John, \n\nI'm not sure if you mis-understood me there. \n\n`$ export MAKE=\"make -j 10\"`\n\nwill not work as well as it could do. The .spkg's will build in parallel, but when it gets to building the Sage library, that will only build serially. You should use \n\n`$ export MAKE=\"make -j10\"`\n\nI assume you are aware you also need a library patch\n\nhttp://trac.sagemath.org/sage_trac/raw-attachment/ticket/7379/trac-7379-decorator-defaults.patch\n\n(only the library patch, not the sagenb patch on that ticket). Only part of #7379 got merged into 4.5.rc0 \n\n\nDave",
    "created_at": "2010-07-13T16:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85816",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

John, 

I'm not sure if you mis-understood me there. 

`$ export MAKE="make -j 10"`

will not work as well as it could do. The .spkg's will build in parallel, but when it gets to building the Sage library, that will only build serially. You should use 

`$ export MAKE="make -j10"`

I assume you are aware you also need a library patch

http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7379/trac-7379-decorator-defaults.patch

(only the library patch, not the sagenb patch on that ticket). Only part of #7379 got merged into 4.5.rc0 


Dave



---

archive/issue_comments_085817.json:
```json
{
    "body": "Replying to [comment:16 drkirkby]:\n> John, \n> \n> I'm not sure if you mis-understood me there. \n> \n> `$ export MAKE=\"make -j 10\"`\n> \n> will not work as well as it could do. The .spkg's will build in parallel, but when it gets to building the Sage library, that will only build serially. You should use \n> \n> `$ export MAKE=\"make -j10\"`\n\nIt's ok, I knew that...\n\n> \n> I assume you are aware you also need a library patch\n> \n> http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7379/trac-7379-decorator-defaults.patch\n> \n\n... and that.  83 spkgs now installed and counting....\n\n> (only the library patch, not the sagenb patch on that ticket). Only part of #7379 got merged into 4.5.rc0 \n> \n> \n> Dave",
    "created_at": "2010-07-13T16:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85817",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:16 drkirkby]:
> John, 
> 
> I'm not sure if you mis-understood me there. 
> 
> `$ export MAKE="make -j 10"`
> 
> will not work as well as it could do. The .spkg's will build in parallel, but when it gets to building the Sage library, that will only build serially. You should use 
> 
> `$ export MAKE="make -j10"`

It's ok, I knew that...

> 
> I assume you are aware you also need a library patch
> 
> http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7379/trac-7379-decorator-defaults.patch
> 

... and that.  83 spkgs now installed and counting....

> (only the library patch, not the sagenb patch on that ticket). Only part of #7379 got merged into 4.5.rc0 
> 
> 
> Dave



---

archive/issue_comments_085818.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-13T17:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85818",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085819.json:
```json
{
    "body": "I built this successfully on sage.math earlier.  I'm willing to give it a positive review right now.  John (Cremona): I'll give you the last word.  If everything works for you, could you give this a positive review?",
    "created_at": "2010-07-13T17:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85819",
    "user": "https://github.com/jhpalmieri"
}
```

I built this successfully on sage.math earlier.  I'm willing to give it a positive review right now.  John (Cremona): I'll give you the last word.  If everything works for you, could you give this a positive review?



---

archive/issue_comments_085820.json:
```json
{
    "body": "I think this ecl-10.2.1.p1.spkg can be merged into rc1, but could you MacOS X testers check which version of Boehm GC is used during install (i.e., the one shipped with Sage or the one included in ECL)?\n\n```sh\n$ grep -i boehm spkg/logs/ecl-10.2.1.p1.log | head -n 2\n```\n\nshould show soemthing like\n\n```\nchecking whether we can use the existing Boehm-Weiser library ... yes\nchecking if we need to copy GC private headers ... checking if we use Boehm-Demers-Weiser precise garbage collector... yes\n```\n\nor\n\n```\nchecking if we use Boehm-Demers-Weiser precise garbage collector... yes\nconfigure: Configuring included Boehm GC library:\n```\n\n(The latter is from Dave's install log on bsd.math/MacOS X 10.4.0.)",
    "created_at": "2010-07-13T17:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85820",
    "user": "https://github.com/nexttime"
}
```

I think this ecl-10.2.1.p1.spkg can be merged into rc1, but could you MacOS X testers check which version of Boehm GC is used during install (i.e., the one shipped with Sage or the one included in ECL)?

```sh
$ grep -i boehm spkg/logs/ecl-10.2.1.p1.log | head -n 2
```

should show soemthing like

```
checking whether we can use the existing Boehm-Weiser library ... yes
checking if we need to copy GC private headers ... checking if we use Boehm-Demers-Weiser precise garbage collector... yes
```

or

```
checking if we use Boehm-Demers-Weiser precise garbage collector... yes
configure: Configuring included Boehm GC library:
```

(The latter is from Dave's install log on bsd.math/MacOS X 10.4.0.)



---

archive/issue_comments_085821.json:
```json
{
    "body": "Replying to [comment:18 jhpalmieri]:\n> I built this successfully on sage.math earlier.  I'm willing to give it a positive review right now.  John (Cremona): I'll give you the last word.  If everything works for you, could you give this a positive review?\n\nIt finished building, now building docs. Then I'll do a ptestlong and report back -- currently I don't know if what was built actually works!",
    "created_at": "2010-07-13T17:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85821",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:18 jhpalmieri]:
> I built this successfully on sage.math earlier.  I'm willing to give it a positive review right now.  John (Cremona): I'll give you the last word.  If everything works for you, could you give this a positive review?

It finished building, now building docs. Then I'll do a ptestlong and report back -- currently I don't know if what was built actually works!



---

archive/issue_comments_085822.json:
```json
{
    "body": "On my OS X box, it says:\n\n```\nchecking if we use Boehm-Demers-Weiser precise garbage collector... yes\n...\nconfigure: Configuring included Boehm GC library:\n```\n\nI'm not an expert in these things, but in src/src/configure, it says:\n\n```\n        darwin*)\n                thehost='darwin'\n                shared='yes'\n                ...\n                # The Boehm-Weiser GC library shipped with Fink does not work\n                # well with our signal handler.\n                enable_boehm=included\n```\n\nwhich leads me to believe that on OS X, it will be a little work to use Sage's installation of boehm_gc.  I think this should go on a follow-up ticket, and it should probably be done in coordination with the ecl people.",
    "created_at": "2010-07-13T17:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85822",
    "user": "https://github.com/jhpalmieri"
}
```

On my OS X box, it says:

```
checking if we use Boehm-Demers-Weiser precise garbage collector... yes
...
configure: Configuring included Boehm GC library:
```

I'm not an expert in these things, but in src/src/configure, it says:

```
        darwin*)
                thehost='darwin'
                shared='yes'
                ...
                # The Boehm-Weiser GC library shipped with Fink does not work
                # well with our signal handler.
                enable_boehm=included
```

which leads me to believe that on OS X, it will be a little work to use Sage's installation of boehm_gc.  I think this should go on a follow-up ticket, and it should probably be done in coordination with the ecl people.



---

archive/issue_comments_085823.json:
```json
{
    "body": "(That is, on OS X, it looks like any setting to the `--enable-boehm` flag gets overridden.)",
    "created_at": "2010-07-13T17:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85823",
    "user": "https://github.com/jhpalmieri"
}
```

(That is, on OS X, it looks like any setting to the `--enable-boehm` flag gets overridden.)



---

archive/issue_comments_085824.json:
```json
{
    "body": "Replying to [comment:22 jhpalmieri]:\n> (That is, on OS X, it looks like any setting to the `--enable-boehm` flag gets overridden.)\n\nThat's odd, since Sage's Boehm GC includes a patch for MacOS X 10.6.\n\nI agree we should open a *new* ticket for that and perhaps include a p2 spkg in 4.5.rc2(?), 4.5.final or 4.5.1.\n\nThe package has to be cleaned up anyway, and perhaps we switch back to ECL 10.**4**.1.",
    "created_at": "2010-07-13T17:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85824",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:22 jhpalmieri]:
> (That is, on OS X, it looks like any setting to the `--enable-boehm` flag gets overridden.)

That's odd, since Sage's Boehm GC includes a patch for MacOS X 10.6.

I agree we should open a *new* ticket for that and perhaps include a p2 spkg in 4.5.rc2(?), 4.5.final or 4.5.1.

The package has to be cleaned up anyway, and perhaps we switch back to ECL 10.**4**.1.



---

archive/issue_comments_085825.json:
```json
{
    "body": "Replying to [comment:23 leif]:\n> Replying to [comment:22 jhpalmieri]:\n> I agree we should open a *new* ticket for that and perhaps include a p2 spkg in 4.5.rc2(?), 4.5.final or 4.5.1.\n\n4.5.1.",
    "created_at": "2010-07-13T17:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85825",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:23 leif]:
> Replying to [comment:22 jhpalmieri]:
> I agree we should open a *new* ticket for that and perhaps include a p2 spkg in 4.5.rc2(?), 4.5.final or 4.5.1.

4.5.1.



---

archive/issue_comments_085826.json:
```json
{
    "body": "Replying to [comment:24 rlm]:\n> 4.5.1.\n\nThat's what I meant by *changing the milestone rather than the priority*. ;-)",
    "created_at": "2010-07-13T18:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85826",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:24 rlm]:
> 4.5.1.

That's what I meant by *changing the milestone rather than the priority*. ;-)



---

archive/issue_comments_085827.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-13T18:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85827",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085828.json:
```json
{
    "body": "Replying to [comment:20 cremona]:\n> Replying to [comment:18 jhpalmieri]:\n> > I built this successfully on sage.math earlier.  I'm willing to give it a positive review right now.  John (Cremona): I'll give you the last word.  If everything works for you, could you give this a positive review?\n> \n> It finished building, now building docs. Then I'll do a ptestlong and report back -- currently I don't know if what was built actually works!\n\nAll tests passed == +++",
    "created_at": "2010-07-13T18:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85828",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:20 cremona]:
> Replying to [comment:18 jhpalmieri]:
> > I built this successfully on sage.math earlier.  I'm willing to give it a positive review right now.  John (Cremona): I'll give you the last word.  If everything works for you, could you give this a positive review?
> 
> It finished building, now building docs. Then I'll do a ptestlong and report back -- currently I don't know if what was built actually works!

All tests passed == +++



---

archive/issue_comments_085829.json:
```json
{
    "body": "Merged\n\nhttp://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg",
    "created_at": "2010-07-13T18:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85829",
    "user": "https://github.com/rlmill"
}
```

Merged

http://sage.math.washington.edu/home/mpatel/trac/9187/ecl-10.2.1.p1.spkg



---

archive/issue_comments_085830.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-13T18:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85830",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_085831.json:
```json
{
    "body": "Replying to [comment:23 leif]:\n> Replying to [comment:22 jhpalmieri]:\n> > (That is, on OS X, it looks like any setting to the `--enable-boehm` flag gets overridden.)\n> \n> That's odd, since Sage's Boehm GC includes a patch for MacOS X 10.6.\n\nJust for the record: The patch just avoids a dumb deprecation *error*(!), and it is already included in ECL's Boehm GC (otherwise ECL wouldn't have built on MacOS X 10.6).",
    "created_at": "2010-07-13T18:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85831",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:23 leif]:
> Replying to [comment:22 jhpalmieri]:
> > (That is, on OS X, it looks like any setting to the `--enable-boehm` flag gets overridden.)
> 
> That's odd, since Sage's Boehm GC includes a patch for MacOS X 10.6.

Just for the record: The patch just avoids a dumb deprecation *error*(!), and it is already included in ECL's Boehm GC (otherwise ECL wouldn't have built on MacOS X 10.6).



---

archive/issue_comments_085832.json:
```json
{
    "body": "For a 4.5 final, we should remove the unnecessary baggage, though (as `SPKG.txt` instructs, btw):\n\n```\nleif@portland:~/Sage/spkgs/ecl-10.2.1.p1$ du -ch src/msvc/ src/contrib/encodings/\n16K\tsrc/msvc/ecl\n8.0K\tsrc/msvc/gc\n8.0K\tsrc/msvc/gmp/mpz\n32K\tsrc/msvc/gmp/mpn/generic\n76K\tsrc/msvc/gmp/mpn/amd64i\n48K\tsrc/msvc/gmp/mpn/x86i/pentium4/sse2\n32K\tsrc/msvc/gmp/mpn/x86i/pentium4/mmx\n92K\tsrc/msvc/gmp/mpn/x86i/pentium4\n48K\tsrc/msvc/gmp/mpn/x86i/p6/mmx\n8.0K\tsrc/msvc/gmp/mpn/x86i/p6/p3mmx\n128K\tsrc/msvc/gmp/mpn/x86i/p6\n300K\tsrc/msvc/gmp/mpn/x86i\n412K\tsrc/msvc/gmp/mpn\n12K\tsrc/msvc/gmp/build.vc8/gen-fib\n16K\tsrc/msvc/gmp/build.vc8/gen-fac_ui\n28K\tsrc/msvc/gmp/build.vc8/lib_gmpxx\n256K\tsrc/msvc/gmp/build.vc8/dll_gmp_amd64\n16K\tsrc/msvc/gmp/build.vc8/gen-bases\n372K\tsrc/msvc/gmp/build.vc8/lib_gmp\n240K\tsrc/msvc/gmp/build.vc8/dll_gmp_p4\n40K\tsrc/msvc/gmp/build.vc8/lib_gmp_p0\n36K\tsrc/msvc/gmp/build.vc8/lib_gmp_p3\n240K\tsrc/msvc/gmp/build.vc8/dll_gmp_p0\n180K\tsrc/msvc/gmp/build.vc8/dll_mpfr\n28K\tsrc/msvc/gmp/build.vc8/gen-psqr\n72K\tsrc/msvc/gmp/build.vc8/lib_gmp_gc\n40K\tsrc/msvc/gmp/build.vc8/lib_gmp_p4\n48K\tsrc/msvc/gmp/build.vc8/lib_gmp_amd64\n436K\tsrc/msvc/gmp/build.vc8/dll_gmp_gc\n240K\tsrc/msvc/gmp/build.vc8/dll_gmp_p3\n208K\tsrc/msvc/gmp/build.vc8/lib_mpfr\n4.8M\tsrc/msvc/gmp/build.vc8\n5.2M\tsrc/msvc/gmp\n8.0K\tsrc/msvc/c\n16K\tsrc/msvc/util\n12K\tsrc/msvc/doc\n5.3M\tsrc/msvc/\n544K\tsrc/contrib/encodings/\n5.8M\ttotal\nleif@portland:~/Sage/spkgs/ecl-10.2.1.p1$ tar cj src/msvc/ src/contrib/encodings/ | wc -c\n859300\n```\n",
    "created_at": "2010-07-13T19:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85832",
    "user": "https://github.com/nexttime"
}
```

For a 4.5 final, we should remove the unnecessary baggage, though (as `SPKG.txt` instructs, btw):

```
leif@portland:~/Sage/spkgs/ecl-10.2.1.p1$ du -ch src/msvc/ src/contrib/encodings/
16K	src/msvc/ecl
8.0K	src/msvc/gc
8.0K	src/msvc/gmp/mpz
32K	src/msvc/gmp/mpn/generic
76K	src/msvc/gmp/mpn/amd64i
48K	src/msvc/gmp/mpn/x86i/pentium4/sse2
32K	src/msvc/gmp/mpn/x86i/pentium4/mmx
92K	src/msvc/gmp/mpn/x86i/pentium4
48K	src/msvc/gmp/mpn/x86i/p6/mmx
8.0K	src/msvc/gmp/mpn/x86i/p6/p3mmx
128K	src/msvc/gmp/mpn/x86i/p6
300K	src/msvc/gmp/mpn/x86i
412K	src/msvc/gmp/mpn
12K	src/msvc/gmp/build.vc8/gen-fib
16K	src/msvc/gmp/build.vc8/gen-fac_ui
28K	src/msvc/gmp/build.vc8/lib_gmpxx
256K	src/msvc/gmp/build.vc8/dll_gmp_amd64
16K	src/msvc/gmp/build.vc8/gen-bases
372K	src/msvc/gmp/build.vc8/lib_gmp
240K	src/msvc/gmp/build.vc8/dll_gmp_p4
40K	src/msvc/gmp/build.vc8/lib_gmp_p0
36K	src/msvc/gmp/build.vc8/lib_gmp_p3
240K	src/msvc/gmp/build.vc8/dll_gmp_p0
180K	src/msvc/gmp/build.vc8/dll_mpfr
28K	src/msvc/gmp/build.vc8/gen-psqr
72K	src/msvc/gmp/build.vc8/lib_gmp_gc
40K	src/msvc/gmp/build.vc8/lib_gmp_p4
48K	src/msvc/gmp/build.vc8/lib_gmp_amd64
436K	src/msvc/gmp/build.vc8/dll_gmp_gc
240K	src/msvc/gmp/build.vc8/dll_gmp_p3
208K	src/msvc/gmp/build.vc8/lib_mpfr
4.8M	src/msvc/gmp/build.vc8
5.2M	src/msvc/gmp
8.0K	src/msvc/c
16K	src/msvc/util
12K	src/msvc/doc
5.3M	src/msvc/
544K	src/contrib/encodings/
5.8M	total
leif@portland:~/Sage/spkgs/ecl-10.2.1.p1$ tar cj src/msvc/ src/contrib/encodings/ | wc -c
859300
```




---

archive/issue_comments_085833.json:
```json
{
    "body": "Replying to [comment:29 leif]:\n> For a 4.5 final, we should remove the unnecessary baggage, though (as `SPKG.txt` instructs, btw):\n\nThat's up to Robert, but I tend to feel saving about 840 KB is of relatively low importance, and can be left for 4.5.1. Especially considering there is a new version of ECL available, and we would expect to resolve the ECL/Maxima issues some time in the near future. So the ecl package will probably be updated for 4.5.1. \n\nDave",
    "created_at": "2010-07-13T20:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85833",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:29 leif]:
> For a 4.5 final, we should remove the unnecessary baggage, though (as `SPKG.txt` instructs, btw):

That's up to Robert, but I tend to feel saving about 840 KB is of relatively low importance, and can be left for 4.5.1. Especially considering there is a new version of ECL available, and we would expect to resolve the ECL/Maxima issues some time in the near future. So the ecl package will probably be updated for 4.5.1. 

Dave



---

archive/issue_comments_085834.json:
```json
{
    "body": "Replying to [comment:29 leif]:\n> For a 4.5 final, we should remove the unnecessary baggage\n\nPlease open a ticket and make a p2 with only these changes. I think it's too late for 4.5.",
    "created_at": "2010-07-13T21:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85834",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:29 leif]:
> For a 4.5 final, we should remove the unnecessary baggage

Please open a ticket and make a p2 with only these changes. I think it's too late for 4.5.



---

archive/issue_comments_085835.json:
```json
{
    "body": "Replying to [comment:31 rlm]:\n> Replying to [comment:29 leif]:\n> > For a 4.5 final, we should remove the unnecessary baggage\n> \n> Please open a ticket and make a p2 with only these changes. I think it's too late for 4.5.\n\nTicket up at #9493.\n\nI unfortunately cannot upload an spkg because I don't have an account on sage.math.\n\n(Perhaps I'll ask again someone to upload it from an e-mail attachment, but it's still fairly large.)",
    "created_at": "2010-07-14T00:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9187#issuecomment-85835",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:31 rlm]:
> Replying to [comment:29 leif]:
> > For a 4.5 final, we should remove the unnecessary baggage
> 
> Please open a ticket and make a p2 with only these changes. I think it's too late for 4.5.

Ticket up at #9493.

I unfortunately cannot upload an spkg because I don't have an account on sage.math.

(Perhaps I'll ask again someone to upload it from an e-mail attachment, but it's still fairly large.)
