# Issue 8951: Clear /tmp/ECL* after building ECL

archive/issues_008951.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @williamstein mvngu juanjose.garciaripoll@googlemail.com @kcrisman @nbruin\n\nAs reported here\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/54544d8649bd027a\n\nthere is a problem when temp files created during the build of ECL. A correct fix requires changes made to ECL source code, but as a temporary fix, it may be sufficient to remove /tmp/ECL* after building ecl. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8951\n\n",
    "created_at": "2010-05-11T20:38:47Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Clear /tmp/ECL* after building ECL",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8951",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @williamstein mvngu juanjose.garciaripoll@googlemail.com @kcrisman @nbruin

As reported here

http://groups.google.com/group/sage-devel/browse_thread/thread/54544d8649bd027a

there is a problem when temp files created during the build of ECL. A correct fix requires changes made to ECL source code, but as a temporary fix, it may be sufficient to remove /tmp/ECL* after building ecl. 



Issue created by migration from https://trac.sagemath.org/ticket/8951





---

archive/issue_comments_082305.json:
```json
{
    "body": "I've attached a patch. It removes the files only on Solaris. It also has a couple of minor corrections \n\n* It no longer reports a 32-bit build. Previously it reported a 32-bit build unless a 64-bit build was requested, but on some systems the default is 64-bit, so the message was incorrect. \n* Checks for SAGE64 being 'yes' and not 'yes' and '1' as before, as there is other code in Sage which prevents '1' being used. \n\nThese two are just very minor changes - the main change is to delete /tmp/ECL*\n\nWhat I find a bit odd, is that I don't see these tmp files on my own Sun Blade 2000 SPARC, which runs Solaris 10 update 8 (05/2009). I can only assume they are created them removed by ecl, so why this should not happen on 't2' is a mystery. \n\nhttp://boxen.math.washington.edu/home/kirkby/Solaris-fixes/ecl-10.2.1.p0.spkg\n\n\nDave",
    "created_at": "2010-05-12T23:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82305",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've attached a patch. It removes the files only on Solaris. It also has a couple of minor corrections 

* It no longer reports a 32-bit build. Previously it reported a 32-bit build unless a 64-bit build was requested, but on some systems the default is 64-bit, so the message was incorrect. 
* Checks for SAGE64 being 'yes' and not 'yes' and '1' as before, as there is other code in Sage which prevents '1' being used. 

These two are just very minor changes - the main change is to delete /tmp/ECL*

What I find a bit odd, is that I don't see these tmp files on my own Sun Blade 2000 SPARC, which runs Solaris 10 update 8 (05/2009). I can only assume they are created them removed by ecl, so why this should not happen on 't2' is a mystery. 

http://boxen.math.washington.edu/home/kirkby/Solaris-fixes/ecl-10.2.1.p0.spkg


Dave



---

archive/issue_comments_082306.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-12T23:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82306",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082307.json:
```json
{
    "body": "Note #8808 as another ECL spkg update.  \n\nAlso, the patch about the 'yes' and '1' still says\n\n```\n# Compile for 64-bit if SAGE64 is set to 'yes' or '1' \n```\n\nalthough of course the code behaves as Dave describes... but maybe that's ok?",
    "created_at": "2010-05-13T13:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82307",
    "user": "https://github.com/kcrisman"
}
```

Note #8808 as another ECL spkg update.  

Also, the patch about the 'yes' and '1' still says

```
# Compile for 64-bit if SAGE64 is set to 'yes' or '1' 
```

although of course the code behaves as Dave describes... but maybe that's ok?



---

archive/issue_comments_082308.json:
```json
{
    "body": "I'll create a new package based on Williams at #8808, which address all issues about ECL",
    "created_at": "2010-05-14T09:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82308",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'll create a new package based on Williams at #8808, which address all issues about ECL



---

archive/issue_comments_082309.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-14T09:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82309",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082310.json:
```json
{
    "body": "Attachment [clear-ECL-from-tmp.patch](tarball://root/attachments/some-uuid/ticket8951/clear-ECL-from-tmp.patch) by drkirkby created at 2010-05-14 11:39:19\n\nMercurial patch - removes tmp files, based on latest verison of ecl",
    "created_at": "2010-05-14T11:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82310",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [clear-ECL-from-tmp.patch](tarball://root/attachments/some-uuid/ticket8951/clear-ECL-from-tmp.patch) by drkirkby created at 2010-05-14 11:39:19

Mercurial patch - removes tmp files, based on latest verison of ecl



---

archive/issue_comments_082311.json:
```json
{
    "body": "Here's a revised ecl-10.4.1. \n\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/ecl-10.4.1/ecl-10.4.1.spkg\n\nIt includes \n\n* The latest release of ecl - taken from the package posted at #8808\n* Removes /tmp/ECL* on Solaris. \n* Corrected minor issue with SAGE64, which would have in theory worked if SAGE64 was set to '1', but earlier bits of sage force SAGE64 to be only 'yes' or 'no', so there was no point checking for this. \n* Comment in the code about this SAGE64 change is now more accurate. \n\nI've tested this on sage.math and it works fine. \n\n```\nreal\t2m20.869s\nuser\t1m47.690s\nsys\t0m23.480s\nSuccessfully installed ecl-10.4.1\nkirkby@sage:~/sage-4.4.2.alpha0$ uname -a\nLinux sage.math.washington.edu 2.6.24-26-server #1 SMP Tue Dec 1 18:26:43 UTC 2009 x86_64 GNU/Linux\n```\n\n\n\n**Note, this code to remove /tmp/ECL* is not a perfect solution. Once ECL is fixed, this should be removed.**\nDave",
    "created_at": "2010-05-14T12:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82311",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Here's a revised ecl-10.4.1. 


http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.4.1/ecl-10.4.1.spkg

It includes 

* The latest release of ecl - taken from the package posted at #8808
* Removes /tmp/ECL* on Solaris. 
* Corrected minor issue with SAGE64, which would have in theory worked if SAGE64 was set to '1', but earlier bits of sage force SAGE64 to be only 'yes' or 'no', so there was no point checking for this. 
* Comment in the code about this SAGE64 change is now more accurate. 

I've tested this on sage.math and it works fine. 

```
real	2m20.869s
user	1m47.690s
sys	0m23.480s
Successfully installed ecl-10.4.1
kirkby@sage:~/sage-4.4.2.alpha0$ uname -a
Linux sage.math.washington.edu 2.6.24-26-server #1 SMP Tue Dec 1 18:26:43 UTC 2009 x86_64 GNU/Linux
```



**Note, this code to remove /tmp/ECL* is not a perfect solution. Once ECL is fixed, this should be removed.**
Dave



---

archive/issue_comments_082312.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-14T12:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82312",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082313.json:
```json
{
    "body": "## Note to release manager\n\n* Apply the patch at #8808\n* Apply the patch attacked here. \n* Copy the file http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.4.1/ecl-10.4.1.spkg to the new source. \n* Do **NOT** use the .spkg at http://wstein.org/home/wstein/patches/ecl-10.4.1.spkg as that lacks the patches here, whereas this ticket includes the updated ECL at http://wstein.org/home/wstein/patches/ecl-10.4.1.spkg. \n\nDave",
    "created_at": "2010-05-14T12:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82313",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

## Note to release manager

* Apply the patch at #8808
* Apply the patch attacked here. 
* Copy the file http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.4.1/ecl-10.4.1.spkg to the new source. 
* Do **NOT** use the .spkg at http://wstein.org/home/wstein/patches/ecl-10.4.1.spkg as that lacks the patches here, whereas this ticket includes the updated ECL at http://wstein.org/home/wstein/patches/ecl-10.4.1.spkg. 

Dave



---

archive/issue_comments_082314.json:
```json
{
    "body": "Replying to [comment:6 drkirkby]:\n> == Note to release manager ==\n> \n>  * Apply the patch at #8808\n>  * Apply the patch attacked here. \n\nBoth of these patches are included in your spkg, right?  In that case, the release manager would just use your spkg, and wouldn't apply any patches anywhere.",
    "created_at": "2010-05-14T15:02:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82314",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:6 drkirkby]:
> == Note to release manager ==
> 
>  * Apply the patch at #8808
>  * Apply the patch attacked here. 

Both of these patches are included in your spkg, right?  In that case, the release manager would just use your spkg, and wouldn't apply any patches anywhere.



---

archive/issue_comments_082315.json:
```json
{
    "body": "As a reminder here, this should *only* be merged simultaneously with the new maxima at #8731.",
    "created_at": "2010-05-14T15:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82315",
    "user": "https://github.com/jasongrout"
}
```

As a reminder here, this should *only* be merged simultaneously with the new maxima at #8731.



---

archive/issue_comments_082316.json:
```json
{
    "body": "As pointed out in #8808, #8645 actually built the new spkg correctly, so we should have started with the spkg from #8645 instead of the spkg from #8808.  I've posted a new spkg which removes the directories that #8645 removed, as per the spkg instructions.",
    "created_at": "2010-05-14T17:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82316",
    "user": "https://github.com/jasongrout"
}
```

As pointed out in #8808, #8645 actually built the new spkg correctly, so we should have started with the spkg from #8645 instead of the spkg from #8808.  I've posted a new spkg which removes the directories that #8645 removed, as per the spkg instructions.



---

archive/issue_comments_082317.json:
```json
{
    "body": "New spkg up at http://sage.math.washington.edu/home/jason/ecl-10.4.1.spkg\n\nI'm not sure who can review it, since I fixed it, to follow Nils' spkg, but David also fixed something on it.\n\nMaybe kcrisman can review it, in conjunction with the new maxima update?",
    "created_at": "2010-05-14T17:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82317",
    "user": "https://github.com/jasongrout"
}
```

New spkg up at http://sage.math.washington.edu/home/jason/ecl-10.4.1.spkg

I'm not sure who can review it, since I fixed it, to follow Nils' spkg, but David also fixed something on it.

Maybe kcrisman can review it, in conjunction with the new maxima update?



---

archive/issue_comments_082318.json:
```json
{
    "body": "Replying to [comment:7 jason]:\n> Replying to [comment:6 drkirkby]:\n> > == Note to release manager ==\n> > \n> >  * Apply the patch at #8808\n> >  * Apply the patch attacked here. \n> \n> Both of these patches are included in your spkg, right?  In that case, the release manager would just use your spkg, and wouldn't apply any patches anywhere.\n> \n> \n\nMy package should work fine.\n\nMy reason for saying to add #8808 first is because my patch was based on the patch applied in #8088, so assumed the wording of SPKG.txt in #8088 as a starting point and used the Mercurial repository in #8088 as a starting point. Also, since William updated the package, he should get credit for that ticket. It has already got positive review. \n\nFrom the point of view of actual code, it would have made no difference whatsoever.\n\nAnyway, you have now posted another version, based on #8645. Someone needs to review it. I looked over spkg-install and SPKG.txt and they look OK to me, but I can hardly review it.",
    "created_at": "2010-05-14T21:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82318",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:7 jason]:
> Replying to [comment:6 drkirkby]:
> > == Note to release manager ==
> > 
> >  * Apply the patch at #8808
> >  * Apply the patch attacked here. 
> 
> Both of these patches are included in your spkg, right?  In that case, the release manager would just use your spkg, and wouldn't apply any patches anywhere.
> 
> 

My package should work fine.

My reason for saying to add #8808 first is because my patch was based on the patch applied in #8088, so assumed the wording of SPKG.txt in #8088 as a starting point and used the Mercurial repository in #8088 as a starting point. Also, since William updated the package, he should get credit for that ticket. It has already got positive review. 

From the point of view of actual code, it would have made no difference whatsoever.

Anyway, you have now posted another version, based on #8645. Someone needs to review it. I looked over spkg-install and SPKG.txt and they look OK to me, but I can hardly review it.



---

archive/issue_comments_082319.json:
```json
{
    "body": "I positive reviewed #8808, which was a mistake.  That's why I posted a new spkg, giving credit to Nils, William, and you, but using #8645 as a base for your patch.  Well, actually I just took your spkg and removed the appropriate directories, since that should end up with the same final result.\n\nIf Nils agrees that the changes are good (i.e., the right directories were removed, I think we can mark this as positive review, because then at least 3 pairs of eyes will have looked at the spkg.",
    "created_at": "2010-05-14T21:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82319",
    "user": "https://github.com/jasongrout"
}
```

I positive reviewed #8808, which was a mistake.  That's why I posted a new spkg, giving credit to Nils, William, and you, but using #8645 as a base for your patch.  Well, actually I just took your spkg and removed the appropriate directories, since that should end up with the same final result.

If Nils agrees that the changes are good (i.e., the right directories were removed, I think we can mark this as positive review, because then at least 3 pairs of eyes will have looked at the spkg.



---

archive/issue_comments_082320.json:
```json
{
    "body": "I confirm that the src directories in\n`/home/nbruin/ecl-10.4.1.spkg`\nand\n`/home/jason/ecl-10.4.1.spkg`\nagree according to `diff -r`. Differences are only in\n`spkg-install` and `SPKG.txt`, as expected (and in .hg).",
    "created_at": "2010-05-18T07:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82320",
    "user": "https://github.com/nbruin"
}
```

I confirm that the src directories in
`/home/nbruin/ecl-10.4.1.spkg`
and
`/home/jason/ecl-10.4.1.spkg`
agree according to `diff -r`. Differences are only in
`spkg-install` and `SPKG.txt`, as expected (and in .hg).



---

archive/issue_comments_082321.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-18T07:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82321",
    "user": "https://github.com/nbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082322.json:
```json
{
    "body": "Replying to [comment:8 jason]:\n> As a reminder here, this should *only* be merged simultaneously with the new maxima at #8731. \n\nJason, \n\nwhat is there about this ticket that means it can only be merged simultaneously with the new Maxima at #8731? That Maxima ticket has not been updated for 3 weeks. If ECL & Maxima need to be updated together, that leaves a whole load of issues unresolved about ECL. Some I can think of are\n\n* The original aim of the ticket, which was to clear the tmp files - a trivial change, that does not need ECL updated, but allows Sage to build more relieably on 't2'\n* The minor SAGE64 issue - again, a trivial (cosmetic) change that does not need ECL updated.\n* It stops the building of spkg's in parallel, as the ECL makefile needs a trivial edit for that - see #9187. Again, that does not need a new version of ECL for this. \n* It stops a build of ECL on 64-bit OpenSolaris - see #8089. Again, the option to permit this does not need a new upstream version of ECL. \n\nIt seems to me we have three choices here:\n\n* Update ECL, without updating Maxima, which I think you are saying is not possible.  \n* Update both Maxima and ECL to the latest versions **quickly**. \n* Apply all the other very small changes to the ECL 10.2.1 that is in Sage now. So leaving updating ECL to 10.4.1 until a later date. \n\nI've created #9264 to update ECL to 10.4.1 and apply all changes. \n\nIt might however be wiser to create another ticket to just apply all the small changes to ECL 10.2.1. \n\nDave",
    "created_at": "2010-06-18T14:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82322",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:8 jason]:
> As a reminder here, this should *only* be merged simultaneously with the new maxima at #8731. 

Jason, 

what is there about this ticket that means it can only be merged simultaneously with the new Maxima at #8731? That Maxima ticket has not been updated for 3 weeks. If ECL & Maxima need to be updated together, that leaves a whole load of issues unresolved about ECL. Some I can think of are

* The original aim of the ticket, which was to clear the tmp files - a trivial change, that does not need ECL updated, but allows Sage to build more relieably on 't2'
* The minor SAGE64 issue - again, a trivial (cosmetic) change that does not need ECL updated.
* It stops the building of spkg's in parallel, as the ECL makefile needs a trivial edit for that - see #9187. Again, that does not need a new version of ECL for this. 
* It stops a build of ECL on 64-bit OpenSolaris - see #8089. Again, the option to permit this does not need a new upstream version of ECL. 

It seems to me we have three choices here:

* Update ECL, without updating Maxima, which I think you are saying is not possible.  
* Update both Maxima and ECL to the latest versions **quickly**. 
* Apply all the other very small changes to the ECL 10.2.1 that is in Sage now. So leaving updating ECL to 10.4.1 until a later date. 

I've created #9264 to update ECL to 10.4.1 and apply all changes. 

It might however be wiser to create another ticket to just apply all the small changes to ECL 10.2.1. 

Dave



---

archive/issue_comments_082323.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-18T14:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82323",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_082324.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-06-18T14:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82324",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_082325.json:
```json
{
    "body": "#9264 solves this issue, and several others related to ECL. Hence #9264, which has positive review, can be merged whilst solving not just this issue, but others related to building packages in parallel and building on OpenSolaris.",
    "created_at": "2010-06-21T09:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82325",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

#9264 solves this issue, and several others related to ECL. Hence #9264, which has positive review, can be merged whilst solving not just this issue, but others related to building packages in parallel and building on OpenSolaris.



---

archive/issue_comments_082326.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-06-25T11:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82326",
    "user": "https://github.com/rlmill"
}
```

Resolution: duplicate



---

archive/issue_comments_082327.json:
```json
{
    "body": "For what it's worth, jjgarcia reports the original issue with `/tmp/ECLINIT.c` being used instead of a unique tempfile has been fixed in ECL. It appears to be in the latest ECL release already, but I haven't checked personally if it now works on Solaris.",
    "created_at": "2011-01-17T16:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8951#issuecomment-82327",
    "user": "https://github.com/wjp"
}
```

For what it's worth, jjgarcia reports the original issue with `/tmp/ECLINIT.c` being used instead of a unique tempfile has been fixed in ECL. It appears to be in the latest ECL release already, but I haven't checked personally if it now works on Solaris.
