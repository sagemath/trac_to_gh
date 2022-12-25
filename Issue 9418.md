# Issue 9418: Add GNU patch as a standard package.

archive/issues_009418.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @nexttime\n\nAs discussed here:\n\nhttp://groups.google.co.uk/group/sage-devel/browse_thread/thread/c566520374106df3\n\nGNU patch\n\nhttp://www.gnu.org/software/patch/\n\nis to be added as a standard package to Sage, to allow the use of 'patch' to be used to make patches, rather than to us 'cp' as now. \n\nA new package may be found here \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/patch-2.6.1.spkg\n\nbut the file `spkg/standard/deps will need to be updated` too. There are several tickets currently open (#9274, #9351 and #9412) for making updates to 'deps' so these need to be coordinated. \n\nOnce this is done, the [Sage Developers Guide](http://www.sagemath.org/doc/developer/) will need to be updated to reflect a new method to create patches. A separate ticket will be opened for that. \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9418\n\n",
    "created_at": "2010-07-03T08:29:24Z",
    "labels": [
        "component: build"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Add GNU patch as a standard package.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9418",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @nexttime

As discussed here:

http://groups.google.co.uk/group/sage-devel/browse_thread/thread/c566520374106df3

GNU patch

http://www.gnu.org/software/patch/

is to be added as a standard package to Sage, to allow the use of 'patch' to be used to make patches, rather than to us 'cp' as now. 

A new package may be found here 

http://boxen.math.washington.edu/home/kirkby/patches/patch-2.6.1.spkg

but the file `spkg/standard/deps will need to be updated` too. There are several tickets currently open (#9274, #9351 and #9412) for making updates to 'deps' so these need to be coordinated. 

Once this is done, the [Sage Developers Guide](http://www.sagemath.org/doc/developer/) will need to be updated to reflect a new method to create patches. A separate ticket will be opened for that. 

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9418





---

archive/issue_comments_089611.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-13T18:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89611",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089612.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-13T23:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89612",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089613.json:
```json
{
    "body": "Would you care to provide a `spkg/deps` patch so we can test that too?",
    "created_at": "2010-11-13T23:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89613",
    "user": "https://github.com/jdemeyer"
}
```

Would you care to provide a `spkg/deps` patch so we can test that too?



---

archive/issue_comments_089614.json:
```json
{
    "body": "Changing keywords from \"\" to \"patch spkg\".",
    "created_at": "2010-11-13T23:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89614",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "" to "patch spkg".



---

archive/issue_comments_089615.json:
```json
{
    "body": "Attachment [install.patch](tarball://root/attachments/some-uuid/ticket9418/install.patch) by drkirkby created at 2010-11-13 23:48:57\n\nPatch for the install file in the sage_scripts-4.6.1.alpha1 package.",
    "created_at": "2010-11-13T23:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89615",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [install.patch](tarball://root/attachments/some-uuid/ticket9418/install.patch) by drkirkby created at 2010-11-13 23:48:57

Patch for the install file in the sage_scripts-4.6.1.alpha1 package.



---

archive/issue_comments_089616.json:
```json
{
    "body": "Attachment [install](tarball://root/attachments/some-uuid/ticket9418/install) by drkirkby created at 2010-11-13 23:51:31\n\nReplacement 'install' file",
    "created_at": "2010-11-13T23:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89616",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [install](tarball://root/attachments/some-uuid/ticket9418/install) by drkirkby created at 2010-11-13 23:51:31

Replacement 'install' file



---

archive/issue_comments_089617.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-13T23:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89617",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089618.json:
```json
{
    "body": "I'm somewhat puzzled. There seems to be two copies of the install file - one in `$SAGE_ROOT/spkg/install`, and another in the sage-scripts package. \n\nI think its only necessary to update the one in spkg, which makes me wonder whats the point of the one in the sage_scripts package. That has a repository, but there are uncommitted changes. \n\nDave",
    "created_at": "2010-11-13T23:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89618",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm somewhat puzzled. There seems to be two copies of the install file - one in `$SAGE_ROOT/spkg/install`, and another in the sage-scripts package. 

I think its only necessary to update the one in spkg, which makes me wonder whats the point of the one in the sage_scripts package. That has a repository, but there are uncommitted changes. 

Dave



---

archive/issue_comments_089619.json:
```json
{
    "body": "I just realised, I ommitted to add PATCH as a dependancy of GAP. It's implied anyway, due to the fact readline, sage and termcap all depend on patch, and gap depends on all them. But I will correct it to make it clearer. \n\nIMHO, it would be a lot nice if this file was sorted alphabetically a bit better, but I wont do that now.",
    "created_at": "2010-11-14T00:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89619",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I just realised, I ommitted to add PATCH as a dependancy of GAP. It's implied anyway, due to the fact readline, sage and termcap all depend on patch, and gap depends on all them. But I will correct it to make it clearer. 

IMHO, it would be a lot nice if this file was sorted alphabetically a bit better, but I wont do that now.



---

archive/issue_comments_089620.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-14T00:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89620",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089621.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-14T00:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89621",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_023254.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-11-14T00:16:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "milestone": "sage-4.6.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9418#event-23254"
}
```



---

archive/issue_comments_089622.json:
```json
{
    "body": "Changing keywords from \"patch spkg\" to \"patch spkg\".",
    "created_at": "2010-11-14T00:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89622",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing keywords from "patch spkg" to "patch spkg".



---

archive/issue_comments_089623.json:
```json
{
    "body": "SPKG.txt",
    "created_at": "2010-11-14T00:36:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89623",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

SPKG.txt



---

archive/issue_comments_089624.json:
```json
{
    "body": "Attachment [SPKG.txt](tarball://root/attachments/some-uuid/ticket9418/SPKG.txt) by drkirkby created at 2010-11-14 00:36:28\n\nspkg-check",
    "created_at": "2010-11-14T00:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89624",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [SPKG.txt](tarball://root/attachments/some-uuid/ticket9418/SPKG.txt) by drkirkby created at 2010-11-14 00:36:28

spkg-check



---

archive/issue_comments_089625.json:
```json
{
    "body": "Attachment [spkg-install](tarball://root/attachments/some-uuid/ticket9418/spkg-install) by drkirkby created at 2010-11-14 00:36:43\n\nspkg-install",
    "created_at": "2010-11-14T00:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89625",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [spkg-install](tarball://root/attachments/some-uuid/ticket9418/spkg-install) by drkirkby created at 2010-11-14 00:36:43

spkg-install



---

archive/issue_comments_089626.json:
```json
{
    "body": "I realised I had not stuck a Mercurial repository in the package - I guess I was expecting people to want to make changes. But I've added one now. I don't know if its normal to add the SPKG.txt, spkg-install and spkg-check files to a new package, but I've them here anyway. No doubt Leif will find something wrong!\n\nDave",
    "created_at": "2010-11-14T00:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89626",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I realised I had not stuck a Mercurial repository in the package - I guess I was expecting people to want to make changes. But I've added one now. I don't know if its normal to add the SPKG.txt, spkg-install and spkg-check files to a new package, but I've them here anyway. No doubt Leif will find something wrong!

Dave



---

archive/issue_comments_089627.json:
```json
{
    "body": "What I meant to say was, I don't know if its normal to attach those 3 files to the ticket. But it can't do any harm I guess.",
    "created_at": "2010-11-14T00:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89627",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

What I meant to say was, I don't know if its normal to attach those 3 files to the ticket. But it can't do any harm I guess.



---

archive/issue_comments_089628.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n> I think its only necessary to update the one in spkg, which makes me wonder whats the point of the one in the sage_scripts package.\n\nAt some point during the installation (or during sdist maybe?), the `install` from the `sage_scripts` package gets copied to `spkg/install`.  Also, `sage-spkg`, `sage-env`, `sage-make_relative` are copied to `spkg/base`.  Don't ask me why, but that's the way it is.",
    "created_at": "2010-11-14T09:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89628",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:5 drkirkby]:
> I think its only necessary to update the one in spkg, which makes me wonder whats the point of the one in the sage_scripts package.

At some point during the installation (or during sdist maybe?), the `install` from the `sage_scripts` package gets copied to `spkg/install`.  Also, `sage-spkg`, `sage-env`, `sage-make_relative` are copied to `spkg/base`.  Don't ask me why, but that's the way it is.



---

archive/issue_comments_089629.json:
```json
{
    "body": "David: instead of adding $(INST)/$(PATCH) as a dependency for every package, would it not be better to do it on a \"as-needed\" basis?  I mean that, whenever a spkg gets upgraded to use `patch`, we add `PATCH` as a dependency?",
    "created_at": "2010-11-14T09:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89629",
    "user": "https://github.com/jdemeyer"
}
```

David: instead of adding $(INST)/$(PATCH) as a dependency for every package, would it not be better to do it on a "as-needed" basis?  I mean that, whenever a spkg gets upgraded to use `patch`, we add `PATCH` as a dependency?



---

archive/issue_comments_089630.json:
```json
{
    "body": "Proof-of-concept spkg using patch: [http://sage.math.washington.edu/home/jdemeyer/spkg/sphinx-1.0.4.p2.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/sphinx-1.0.4.p2.spkg)",
    "created_at": "2010-11-14T10:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89630",
    "user": "https://github.com/jdemeyer"
}
```

Proof-of-concept spkg using patch: [http://sage.math.washington.edu/home/jdemeyer/spkg/sphinx-1.0.4.p2.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/sphinx-1.0.4.p2.spkg)



---

archive/issue_comments_089631.json:
```json
{
    "body": "Replying to [comment:12 jdemeyer]:\n> David: instead of adding $(INST)/$(PATCH) as a dependency for every package, would it not be better to do it on a \"as-needed\" basis?  I mean that, whenever a spkg gets upgraded to use `patch`, we add `PATCH` as a dependency?\nI do not think that would be a good idea. Every time someone wants to add a patch, they would need to create one for 'deps' too. A lot of people don't know how to use that file. Note even my initial comments I noted there were several tickets touching 'deps' and these would need to be coordinated. To make matters even more complicated, the 'deps' file is not under revision control, which make s updating that file more problematic. \n\nIf the `patch` package took a long time to build, then I could see it would slow the build of Sage, as it introduces a sometimes unnecessary dependency. But for a package which takes less than 4 seconds to build **and** run all the self tests, I think it is better to add it to 'deps' now, so every package could use it now. \n\nIt also avoids the very real risk someone will create a patch, which will work on their system since either\n* patch has already benn built.\n* There's a suitable version of patch on their system.\n\nThe patch would fail to install on another computer, because patch is not built at that point in time. Since the order of building packages is not fixed. \n\nIMHO, `patch` should be built early, so it can be used with the minimum amount of effort.\n\n\nDave",
    "created_at": "2010-11-14T10:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89631",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:12 jdemeyer]:
> David: instead of adding $(INST)/$(PATCH) as a dependency for every package, would it not be better to do it on a "as-needed" basis?  I mean that, whenever a spkg gets upgraded to use `patch`, we add `PATCH` as a dependency?
I do not think that would be a good idea. Every time someone wants to add a patch, they would need to create one for 'deps' too. A lot of people don't know how to use that file. Note even my initial comments I noted there were several tickets touching 'deps' and these would need to be coordinated. To make matters even more complicated, the 'deps' file is not under revision control, which make s updating that file more problematic. 

If the `patch` package took a long time to build, then I could see it would slow the build of Sage, as it introduces a sometimes unnecessary dependency. But for a package which takes less than 4 seconds to build **and** run all the self tests, I think it is better to add it to 'deps' now, so every package could use it now. 

It also avoids the very real risk someone will create a patch, which will work on their system since either
* patch has already benn built.
* There's a suitable version of patch on their system.

The patch would fail to install on another computer, because patch is not built at that point in time. Since the order of building packages is not fixed. 

IMHO, `patch` should be built early, so it can be used with the minimum amount of effort.


Dave



---

archive/issue_comments_089632.json:
```json
{
    "body": "Attachment [9418_install.patch](tarball://root/attachments/some-uuid/ticket9418/9418_install.patch) by @jdemeyer created at 2010-11-14 11:07:09\n\nAdded ticket number to file name",
    "created_at": "2010-11-14T11:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89632",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9418_install.patch](tarball://root/attachments/some-uuid/ticket9418/9418_install.patch) by @jdemeyer created at 2010-11-14 11:07:09

Added ticket number to file name



---

archive/issue_comments_089633.json:
```json
{
    "body": "I suggest a small \"sanity check\" at the end of `spkg-install` to check that the `patch` in the PATH is the right one.  Something like\n\n```\nif ! patch --version | grep >/dev/null 'patch 2.6.1'; then\n    echo \"Cannot to find the patch program we just installed\"\n    exit 1\nfi\n```\n\n\nI know you like `grep >/dev/null`  ;-)",
    "created_at": "2010-11-14T23:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89633",
    "user": "https://github.com/jdemeyer"
}
```

I suggest a small "sanity check" at the end of `spkg-install` to check that the `patch` in the PATH is the right one.  Something like

```
if ! patch --version | grep >/dev/null 'patch 2.6.1'; then
    echo "Cannot to find the patch program we just installed"
    exit 1
fi
```


I know you like `grep >/dev/null`  ;-)



---

archive/issue_comments_089634.json:
```json
{
    "body": "Also: do we really *need* all the 64-bit checking stuff?",
    "created_at": "2010-11-14T23:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89634",
    "user": "https://github.com/jdemeyer"
}
```

Also: do we really *need* all the 64-bit checking stuff?



---

archive/issue_comments_089635.json:
```json
{
    "body": "Regarding `deps`: is there a reason that SQLALCHEMY doesn't have PATCH as dependency?\n\nAlso, some packages are their own \"upstream\", so should never include patches.  These are genus2reduction, extcode, examples, sagenb (and possibly more).",
    "created_at": "2010-11-15T00:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89635",
    "user": "https://github.com/jdemeyer"
}
```

Regarding `deps`: is there a reason that SQLALCHEMY doesn't have PATCH as dependency?

Also, some packages are their own "upstream", so should never include patches.  These are genus2reduction, extcode, examples, sagenb (and possibly more).



---

archive/issue_comments_089636.json:
```json
{
    "body": "Yes, I feel we do need the 64-bit things. Sure, a 32-bit version of patch would probably do all we want, but the same is true of some other commands like 'rubiks'. But building them all 64-bit makes it much easier to detect if there are any 32-bit code by mistake. Knowing that every single library and ever single binary should be 64-bit makes finding any 32-bit objects very easy. \n\nHaving the option to specify another another 64-bit flag could be useful in a port. Having spent ages sorting out the mess someone created by assuming only 64-bit OS X would be supported, and the option would be `-m64`, I'm reluctant to inflict such a stupid thing on someone else. \n\nSQLALCHEMY is an oversight. That does need correcting. \n\nI don't think it's safe to assume that just because a package is it's own upstream, that it will not necessarily ever be patched by someone other than the developer. Consider genus2reduction. That is currently at patch level 8, There are no patches, but many times people have changed spkg-install. What gives you confidence that someone might not need to change a file in this package? 64-bit support as added to genus2reduction, but on the Pari package, adding 64-bit supported needed updating of makefiles. How can you be so confident that a change in genus2reduction would not need a patch? \n\nTo me, removing dependencies will not speed up the build of Sage, but could potentially lead to problems. Being able to say \"you can use patch for **any** package not in the BASE group (`prereq`, `bzip2 etc`, `dir` and `sage_scripts`), is much easier than documenting you can use patch on most package, not not A, B, C, D, E ...etc. \n\nI fail to see what is gained by removing what may be a technically unnecessary dependency, but in practice will have no harmful effect, and can stop difficult problems occurring. \n\nWith few exceptions, where we know there has been issues (like readline), we normally trust the result of `make install` and don't actually check the packages work. But I see nothing wrong with your suggestion. So I'm find on adding that. \n\nBut it's 0037 AM here, and I'm not going to be making any changes for 8 hours at least. \n\nDave",
    "created_at": "2010-11-15T00:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89636",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Yes, I feel we do need the 64-bit things. Sure, a 32-bit version of patch would probably do all we want, but the same is true of some other commands like 'rubiks'. But building them all 64-bit makes it much easier to detect if there are any 32-bit code by mistake. Knowing that every single library and ever single binary should be 64-bit makes finding any 32-bit objects very easy. 

Having the option to specify another another 64-bit flag could be useful in a port. Having spent ages sorting out the mess someone created by assuming only 64-bit OS X would be supported, and the option would be `-m64`, I'm reluctant to inflict such a stupid thing on someone else. 

SQLALCHEMY is an oversight. That does need correcting. 

I don't think it's safe to assume that just because a package is it's own upstream, that it will not necessarily ever be patched by someone other than the developer. Consider genus2reduction. That is currently at patch level 8, There are no patches, but many times people have changed spkg-install. What gives you confidence that someone might not need to change a file in this package? 64-bit support as added to genus2reduction, but on the Pari package, adding 64-bit supported needed updating of makefiles. How can you be so confident that a change in genus2reduction would not need a patch? 

To me, removing dependencies will not speed up the build of Sage, but could potentially lead to problems. Being able to say "you can use patch for **any** package not in the BASE group (`prereq`, `bzip2 etc`, `dir` and `sage_scripts`), is much easier than documenting you can use patch on most package, not not A, B, C, D, E ...etc. 

I fail to see what is gained by removing what may be a technically unnecessary dependency, but in practice will have no harmful effect, and can stop difficult problems occurring. 

With few exceptions, where we know there has been issues (like readline), we normally trust the result of `make install` and don't actually check the packages work. But I see nothing wrong with your suggestion. So I'm find on adding that. 

But it's 0037 AM here, and I'm not going to be making any changes for 8 hours at least. 

Dave



---

archive/issue_comments_089637.json:
```json
{
    "body": "Dave, I agree with all of your post above.",
    "created_at": "2010-11-15T09:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89637",
    "user": "https://github.com/jdemeyer"
}
```

Dave, I agree with all of your post above.



---

archive/issue_comments_089638.json:
```json
{
    "body": "Replying to [comment:20 drkirkby]:\n> With few exceptions, where we know there has been issues (like readline), we normally trust the result of `make install` and don't actually check the packages work. But I see nothing wrong with your suggestion. So I'm find on adding that. \n\nYou can also consider it to be a sanity check that SAGE_LOCAL and PATH have sensible values.",
    "created_at": "2010-11-15T09:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89638",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:20 drkirkby]:
> With few exceptions, where we know there has been issues (like readline), we normally trust the result of `make install` and don't actually check the packages work. But I see nothing wrong with your suggestion. So I'm find on adding that. 

You can also consider it to be a sanity check that SAGE_LOCAL and PATH have sensible values.



---

archive/issue_comments_089639.json:
```json
{
    "body": "\n```\nSAGE_CHECK='yes' sage -f http://boxen.math.washington.edu/home/kirkby/patches/patch-2.6.1.spkg\n```\n\nworked fine on 64-bit ubuntu and 32-bit Suse, with 4.6.1.alpha1 and 4.6.1.alpha0 respectively.\n\nFor a positive review is it enough that this spkg builds fine on all supported systems, or do we also need to have at least one other spkg converted to use it and build ok?",
    "created_at": "2010-11-15T11:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89639",
    "user": "https://github.com/JohnCremona"
}
```


```
SAGE_CHECK='yes' sage -f http://boxen.math.washington.edu/home/kirkby/patches/patch-2.6.1.spkg
```

worked fine on 64-bit ubuntu and 32-bit Suse, with 4.6.1.alpha1 and 4.6.1.alpha0 respectively.

For a positive review is it enough that this spkg builds fine on all supported systems, or do we also need to have at least one other spkg converted to use it and build ok?



---

archive/issue_comments_089640.json:
```json
{
    "body": "There are a couple of issues to be fixed\n* SQLALCHEMY is not listed as depending on patch, when it should be. \n* Jeroen felt testin that patch actually reported the right version would be sensible. \n* I think it would be sensible the self-tests of the package are run on every system, not just with SAGE_CHECK=yes. Since\n  * They take less than half a second on my machine (3.33 GHz Xeon). \n  * A bad version of patch could create all sorts of problems. \n\nI will address these today, but I have to do some other things. I'll put it to needs work for now, until I get chance to do this. \n\nDave",
    "created_at": "2010-11-15T11:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89640",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

There are a couple of issues to be fixed
* SQLALCHEMY is not listed as depending on patch, when it should be. 
* Jeroen felt testin that patch actually reported the right version would be sensible. 
* I think it would be sensible the self-tests of the package are run on every system, not just with SAGE_CHECK=yes. Since
  * They take less than half a second on my machine (3.33 GHz Xeon). 
  * A bad version of patch could create all sorts of problems. 

I will address these today, but I have to do some other things. I'll put it to needs work for now, until I get chance to do this. 

Dave



---

archive/issue_comments_089641.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-15T11:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89641",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089642.json:
```json
{
    "body": "On the 64-bit ubuntu system, I installed the new version of the Sphinx package (with -f) and did a full test.  All OK except this:\n\n```\nsage -t -long ./sage/misc/sagedoc.py\n**********************************************************************\nFile \"/home/jec/sage-4.6.1.alpha1/devel/sage-main/sage/misc/sagedoc.py\", line 891:\n    sage: len(search_doc('tree', interact=False).splitlines()) > 2000\nExpected:\n    True\nGot:\n    Warning, the following Sage documentation hasn't been built,\n    so documentation search results may be incomplete:\n    <BLANKLINE>\n    /home/jec/sage-current/devel/sage/doc/output/html/en/website\n    /home/jec/sage-current/devel/sage/doc/output/html/en/developer\n    /home/jec/sage-current/devel/sage/doc/output/html/en/installation\n    /home/jec/sage-current/devel/sage/doc/output/html/en/constructions\n    /home/jec/sage-current/devel/sage/doc/output/html/en/a_tour_of_sage\n    /home/jec/sage-current/devel/sage/doc/output/html/en/numerical_sage\n    /home/jec/sage-current/devel/sage/doc/output/html/en/faq\n    /home/jec/sage-current/devel/sage/doc/output/html/en/thematic_tutorials\n    /home/jec/sage-current/devel/sage/doc/output/html/en/reference\n    /home/jec/sage-current/devel/sage/doc/output/html/en/bordeaux_2008\n    /home/jec/sage-current/devel/sage/doc/output/html/fr/a_tour_of_sage\n    /home/jec/sage-current/devel/sage/doc/output/html/fr/tutorial\n    <BLANKLINE>\n    You can build these with 'sage -docbuild DOCUMENT html',\n    where DOCUMENT is one of 'website', 'developer', 'installation', 'constructions', 'a_tour_of_sage', 'numerical_sage', 'faq', 'thematic_tutorials', 'reference', 'bordeaux_2008', 'a_tour_of_sage', 'tutorial', \n    or you can use 'sage -docbuild all html' to build all of the missing documentation.\n    False\n**********************************************************************\nFile \"/home/jec/sage-4.6.1.alpha1/devel/sage-main/sage/misc/sagedoc.py\", line 893:\n    sage: len(search_doc('tree', whole_word=True, interact=False).splitlines()) < 200\nExpected:\n    True\nGot:\n    Warning, the following Sage documentation hasn't been built,\n    so documentation search results may be incomplete:\n    <BLANKLINE>\n    /home/jec/sage-current/devel/sage/doc/output/html/en/website\n    /home/jec/sage-current/devel/sage/doc/output/html/en/developer\n    /home/jec/sage-current/devel/sage/doc/output/html/en/installation\n    /home/jec/sage-current/devel/sage/doc/output/html/en/constructions\n    /home/jec/sage-current/devel/sage/doc/output/html/en/a_tour_of_sage\n    /home/jec/sage-current/devel/sage/doc/output/html/en/numerical_sage\n    /home/jec/sage-current/devel/sage/doc/output/html/en/faq\n    /home/jec/sage-current/devel/sage/doc/output/html/en/thematic_tutorials\n    /home/jec/sage-current/devel/sage/doc/output/html/en/reference\n    /home/jec/sage-current/devel/sage/doc/output/html/en/bordeaux_2008\n    /home/jec/sage-current/devel/sage/doc/output/html/fr/a_tour_of_sage\n    /home/jec/sage-current/devel/sage/doc/output/html/fr/tutorial\n    <BLANKLINE>\n    You can build these with 'sage -docbuild DOCUMENT html',\n    where DOCUMENT is one of 'website', 'developer', 'installation', 'constructions', 'a_tour_of_sage', 'numerical_sage', 'faq', 'thematic_tutorials', 'reference', 'bordeaux_2008', 'a_tour_of_sage', 'tutorial', \n    or you can use 'sage -docbuild all html' to build all of the missing documentation.\n    True\n**********************************************************************\nFile \"/home/jec/sage-4.6.1.alpha1/devel/sage-main/sage/misc/sagedoc.py\", line 496:\n    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)\nExpected:\n    True\nGot:\n    Warning, the following Sage documentation hasn't been built,\n    so documentation search results may be incomplete:\n    <BLANKLINE>\n    /home/jec/sage-current/devel/sage/doc/output/html/en/website\n    /home/jec/sage-current/devel/sage/doc/output/html/en/developer\n    /home/jec/sage-current/devel/sage/doc/output/html/en/installation\n    /home/jec/sage-current/devel/sage/doc/output/html/en/constructions\n    /home/jec/sage-current/devel/sage/doc/output/html/en/a_tour_of_sage\n    /home/jec/sage-current/devel/sage/doc/output/html/en/numerical_sage\n    /home/jec/sage-current/devel/sage/doc/output/html/en/faq\n    /home/jec/sage-current/devel/sage/doc/output/html/en/thematic_tutorials\n    /home/jec/sage-current/devel/sage/doc/output/html/en/reference\n    /home/jec/sage-current/devel/sage/doc/output/html/en/bordeaux_2008\n    /home/jec/sage-current/devel/sage/doc/output/html/fr/a_tour_of_sage\n    /home/jec/sage-current/devel/sage/doc/output/html/fr/tutorial\n    <BLANKLINE>\n    You can build these with 'sage -docbuild DOCUMENT html',\n    where DOCUMENT is one of 'website', 'developer', 'installation', 'constructions', 'a_tour_of_sage', 'numerical_sage', 'faq', 'thematic_tutorials', 'reference', 'bordeaux_2008', 'a_tour_of_sage', 'tutorial', \n    or you can use 'sage -docbuild all html' to build all of the missing documentation.\n    False\n**********************************************************************\n```\n\nBefore installing the patch spkg and sphinx I had built the docs, but I had not rebuilt them, so perhaps this is harmless?",
    "created_at": "2010-11-15T12:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89642",
    "user": "https://github.com/JohnCremona"
}
```

On the 64-bit ubuntu system, I installed the new version of the Sphinx package (with -f) and did a full test.  All OK except this:

```
sage -t -long ./sage/misc/sagedoc.py
**********************************************************************
File "/home/jec/sage-4.6.1.alpha1/devel/sage-main/sage/misc/sagedoc.py", line 891:
    sage: len(search_doc('tree', interact=False).splitlines()) > 2000
Expected:
    True
Got:
    Warning, the following Sage documentation hasn't been built,
    so documentation search results may be incomplete:
    <BLANKLINE>
    /home/jec/sage-current/devel/sage/doc/output/html/en/website
    /home/jec/sage-current/devel/sage/doc/output/html/en/developer
    /home/jec/sage-current/devel/sage/doc/output/html/en/installation
    /home/jec/sage-current/devel/sage/doc/output/html/en/constructions
    /home/jec/sage-current/devel/sage/doc/output/html/en/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/numerical_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/faq
    /home/jec/sage-current/devel/sage/doc/output/html/en/thematic_tutorials
    /home/jec/sage-current/devel/sage/doc/output/html/en/reference
    /home/jec/sage-current/devel/sage/doc/output/html/en/bordeaux_2008
    /home/jec/sage-current/devel/sage/doc/output/html/fr/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/fr/tutorial
    <BLANKLINE>
    You can build these with 'sage -docbuild DOCUMENT html',
    where DOCUMENT is one of 'website', 'developer', 'installation', 'constructions', 'a_tour_of_sage', 'numerical_sage', 'faq', 'thematic_tutorials', 'reference', 'bordeaux_2008', 'a_tour_of_sage', 'tutorial', 
    or you can use 'sage -docbuild all html' to build all of the missing documentation.
    False
**********************************************************************
File "/home/jec/sage-4.6.1.alpha1/devel/sage-main/sage/misc/sagedoc.py", line 893:
    sage: len(search_doc('tree', whole_word=True, interact=False).splitlines()) < 200
Expected:
    True
Got:
    Warning, the following Sage documentation hasn't been built,
    so documentation search results may be incomplete:
    <BLANKLINE>
    /home/jec/sage-current/devel/sage/doc/output/html/en/website
    /home/jec/sage-current/devel/sage/doc/output/html/en/developer
    /home/jec/sage-current/devel/sage/doc/output/html/en/installation
    /home/jec/sage-current/devel/sage/doc/output/html/en/constructions
    /home/jec/sage-current/devel/sage/doc/output/html/en/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/numerical_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/faq
    /home/jec/sage-current/devel/sage/doc/output/html/en/thematic_tutorials
    /home/jec/sage-current/devel/sage/doc/output/html/en/reference
    /home/jec/sage-current/devel/sage/doc/output/html/en/bordeaux_2008
    /home/jec/sage-current/devel/sage/doc/output/html/fr/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/fr/tutorial
    <BLANKLINE>
    You can build these with 'sage -docbuild DOCUMENT html',
    where DOCUMENT is one of 'website', 'developer', 'installation', 'constructions', 'a_tour_of_sage', 'numerical_sage', 'faq', 'thematic_tutorials', 'reference', 'bordeaux_2008', 'a_tour_of_sage', 'tutorial', 
    or you can use 'sage -docbuild all html' to build all of the missing documentation.
    True
**********************************************************************
File "/home/jec/sage-4.6.1.alpha1/devel/sage-main/sage/misc/sagedoc.py", line 496:
    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)
Expected:
    True
Got:
    Warning, the following Sage documentation hasn't been built,
    so documentation search results may be incomplete:
    <BLANKLINE>
    /home/jec/sage-current/devel/sage/doc/output/html/en/website
    /home/jec/sage-current/devel/sage/doc/output/html/en/developer
    /home/jec/sage-current/devel/sage/doc/output/html/en/installation
    /home/jec/sage-current/devel/sage/doc/output/html/en/constructions
    /home/jec/sage-current/devel/sage/doc/output/html/en/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/numerical_sage
    /home/jec/sage-current/devel/sage/doc/output/html/en/faq
    /home/jec/sage-current/devel/sage/doc/output/html/en/thematic_tutorials
    /home/jec/sage-current/devel/sage/doc/output/html/en/reference
    /home/jec/sage-current/devel/sage/doc/output/html/en/bordeaux_2008
    /home/jec/sage-current/devel/sage/doc/output/html/fr/a_tour_of_sage
    /home/jec/sage-current/devel/sage/doc/output/html/fr/tutorial
    <BLANKLINE>
    You can build these with 'sage -docbuild DOCUMENT html',
    where DOCUMENT is one of 'website', 'developer', 'installation', 'constructions', 'a_tour_of_sage', 'numerical_sage', 'faq', 'thematic_tutorials', 'reference', 'bordeaux_2008', 'a_tour_of_sage', 'tutorial', 
    or you can use 'sage -docbuild all html' to build all of the missing documentation.
    False
**********************************************************************
```

Before installing the patch spkg and sphinx I had built the docs, but I had not rebuilt them, so perhaps this is harmless?



---

archive/issue_comments_089643.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket9418/deps) by drkirkby created at 2010-11-15 12:34:32\n\nCorectted 'deps' file, with SQLALCHEMY taken care of",
    "created_at": "2010-11-15T12:34:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89643",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket9418/deps) by drkirkby created at 2010-11-15 12:34:32

Corectted 'deps' file, with SQLALCHEMY taken care of



---

archive/issue_comments_089644.json:
```json
{
    "body": "Updated deps patch, with ticket name and with the SQLALCHEMY resolved",
    "created_at": "2010-11-15T12:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89644",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Updated deps patch, with ticket name and with the SQLALCHEMY resolved



---

archive/issue_comments_089645.json:
```json
{
    "body": "Attachment [9418_deps.patch](tarball://root/attachments/some-uuid/ticket9418/9418_deps.patch) by drkirkby created at 2010-11-15 13:11:15\n\nI've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. \n\nIt would be useful to get this tested in its current state, as changes will be minimal\n\ndave",
    "created_at": "2010-11-15T13:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89645",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9418_deps.patch](tarball://root/attachments/some-uuid/ticket9418/9418_deps.patch) by drkirkby created at 2010-11-15 13:11:15

I've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. 

It would be useful to get this tested in its current state, as changes will be minimal

dave



---

archive/issue_comments_089646.json:
```json
{
    "body": "Replying to [comment:26 cremona]:\n> Before installing the patch spkg and sphinx I had built the docs, but I had not rebuilt them, so perhaps this is harmless?\n\nIn any case, I doubt this is an issue regarding *patch*.  The main point was to test whether the spkg installed.",
    "created_at": "2010-11-15T13:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89646",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:26 cremona]:
> Before installing the patch spkg and sphinx I had built the docs, but I had not rebuilt them, so perhaps this is harmless?

In any case, I doubt this is an issue regarding *patch*.  The main point was to test whether the spkg installed.



---

archive/issue_comments_089647.json:
```json
{
    "body": "Replying to [comment:27 drkirkby]:\n> I've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. \n\nThat would be a colour patch, I presume?",
    "created_at": "2010-11-15T14:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89647",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:27 drkirkby]:
> I've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. 

That would be a colour patch, I presume?



---

archive/issue_comments_089648.json:
```json
{
    "body": "Replying to [comment:29 cremona]:\n> Replying to [comment:27 drkirkby]:\n> > I've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. \n> \n> That would be a colour patch, I presume?\n> \nI think it will be showed as red and green in the browser, though the paint was white!\n\ndave",
    "created_at": "2010-11-15T15:01:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89648",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:29 cremona]:
> Replying to [comment:27 drkirkby]:
> > I've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. 
> 
> That would be a colour patch, I presume?
> 
I think it will be showed as red and green in the browser, though the paint was white!

dave



---

archive/issue_comments_089649.json:
```json
{
    "body": "Patch >= 2.6 seems to be broken on OS X 10.4 (and supposedly also Solaris).  I have tested upstream patch 2.5.9 and that works fine.\n\nSo I propose to use [http://ftp.gnu.org/gnu/patch/patch-2.5.9.tar.gz](http://ftp.gnu.org/gnu/patch/patch-2.5.9.tar.gz)",
    "created_at": "2010-11-16T15:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89649",
    "user": "https://github.com/jdemeyer"
}
```

Patch >= 2.6 seems to be broken on OS X 10.4 (and supposedly also Solaris).  I have tested upstream patch 2.5.9 and that works fine.

So I propose to use [http://ftp.gnu.org/gnu/patch/patch-2.5.9.tar.gz](http://ftp.gnu.org/gnu/patch/patch-2.5.9.tar.gz)



---

archive/issue_comments_089650.json:
```json
{
    "body": "I created a spkg with patch 2.5.9 which works on OS X 10.4: [http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg)\n\nI also added the sanity check that I mentioned, not yet the `make check`.",
    "created_at": "2010-11-16T16:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89650",
    "user": "https://github.com/jdemeyer"
}
```

I created a spkg with patch 2.5.9 which works on OS X 10.4: [http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg)

I also added the sanity check that I mentioned, not yet the `make check`.



---

archive/issue_comments_089651.json:
```json
{
    "body": "Replying to [comment:33 jdemeyer]:\n> I created a spkg with patch 2.5.9 which works on OS X 10.4: [http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg)\n> \n> I also added the sanity check that I mentioned, not yet the `make check`.\n\nI built it on OpenSolaris OK. There's a `make check` which I had created. \n\nHowever, the version you have now used has no test facility, so `make-check` should simply be removed. The developers must have added the facility to test on more recent versions only. \n\nI've created a version at \n\nhttp://boxen.math.washington.edu/home/kirkby/older/patch-2.5.9.spkg\n\nwhich has the spkg-check file removed, and so notes to say not to update to 2.6 or 2.6.1. I will add a Mecurial patch in a minute. \n\n\nDave",
    "created_at": "2010-11-16T16:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89651",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:33 jdemeyer]:
> I created a spkg with patch 2.5.9 which works on OS X 10.4: [http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg)
> 
> I also added the sanity check that I mentioned, not yet the `make check`.

I built it on OpenSolaris OK. There's a `make check` which I had created. 

However, the version you have now used has no test facility, so `make-check` should simply be removed. The developers must have added the facility to test on more recent versions only. 

I've created a version at 

http://boxen.math.washington.edu/home/kirkby/older/patch-2.5.9.spkg

which has the spkg-check file removed, and so notes to say not to update to 2.6 or 2.6.1. I will add a Mecurial patch in a minute. 


Dave



---

archive/issue_comments_089652.json:
```json
{
    "body": "Remove the spkg-check file, as this version of patch has no self-tests that can be run.",
    "created_at": "2010-11-16T16:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89652",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Remove the spkg-check file, as this version of patch has no self-tests that can be run.



---

archive/issue_comments_089653.json:
```json
{
    "body": "Attachment [9418-remove-spkg-check-file.patch](tarball://root/attachments/some-uuid/ticket9418/9418-remove-spkg-check-file.patch) by drkirkby created at 2010-11-16 17:13:52\n\nI've checked the version at \n\nhttp://boxen.math.washington.edu/home/kirkby/older/patch-2.5.9.spkg\n\ninstalls OK on \n\n* OpenSolaris 06/2009 (my machine hawk).\n* Solaris 10 SPARC (t2.math)\n* Solaris 10 x86 (fulvia on skynet)\n* Linux (sage.math)  \n* OS X 10.6 (bsd.math)\n \nI can confirm that 2.6.1 did fail to install on Solaris 10 on SPARC (t2.math)\n\nDave",
    "created_at": "2010-11-16T17:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89653",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9418-remove-spkg-check-file.patch](tarball://root/attachments/some-uuid/ticket9418/9418-remove-spkg-check-file.patch) by drkirkby created at 2010-11-16 17:13:52

I've checked the version at 

http://boxen.math.washington.edu/home/kirkby/older/patch-2.5.9.spkg

installs OK on 

* OpenSolaris 06/2009 (my machine hawk).
* Solaris 10 SPARC (t2.math)
* Solaris 10 x86 (fulvia on skynet)
* Linux (sage.math)  
* OS X 10.6 (bsd.math)
 
I can confirm that 2.6.1 did fail to install on Solaris 10 on SPARC (t2.math)

Dave



---

archive/issue_comments_089654.json:
```json
{
    "body": "We need info about if this builds OK on other operating systems. \n\nI've changed from Needs Work -> Needs Info, as I think this **should** need no further changes. \n\nCan someone confirm it works on OS X 10.4? If so, I think this will be ready for review. \n\nDave",
    "created_at": "2010-11-16T17:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89654",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

We need info about if this builds OK on other operating systems. 

I've changed from Needs Work -> Needs Info, as I think this **should** need no further changes. 

Can someone confirm it works on OS X 10.4? If so, I think this will be ready for review. 

Dave



---

archive/issue_comments_089655.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-11-16T17:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89655",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_089656.json:
```json
{
    "body": "David's spkg works on OS X 10.4 (as expected)",
    "created_at": "2010-11-16T18:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89656",
    "user": "https://github.com/jdemeyer"
}
```

David's spkg works on OS X 10.4 (as expected)



---

archive/issue_comments_089657.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-11-16T18:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89657",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_089658.json:
```json
{
    "body": "With this now checked on \n\n* Linux (sage.math)\n* OpenSolaris 06/2009 (my machine hawk).\n* Solaris 10 SPARC (t2.math)\n* Solaris 10 x86 (fulvia on skynet)   \n* OS X 10.6 (bsd.math) \n* OS X 10.4 \n\nI think this is enough for a positive review. I've set to needs review. If someone else feels likewise, we might as well set this to positive. \n\nIf there are any issues on fully supported platforms, the buildbot should find them.\n\nWill the sphinx package that has been used as a test be in the next alpha? If so, that will test not only the build, but also the functionality. \n\nDave",
    "created_at": "2010-11-16T18:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89658",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

With this now checked on 

* Linux (sage.math)
* OpenSolaris 06/2009 (my machine hawk).
* Solaris 10 SPARC (t2.math)
* Solaris 10 x86 (fulvia on skynet)   
* OS X 10.6 (bsd.math) 
* OS X 10.4 

I think this is enough for a positive review. I've set to needs review. If someone else feels likewise, we might as well set this to positive. 

If there are any issues on fully supported platforms, the buildbot should find them.

Will the sphinx package that has been used as a test be in the next alpha? If so, that will test not only the build, but also the functionality. 

Dave



---

archive/issue_comments_089659.json:
```json
{
    "body": "Replying to [comment:39 drkirkby]:\n> Will the sphinx package that has been used as a test be in the next alpha? If so, that will test not only the build, but also the functionality. \n\nYes, it will be in the next alpha (unless there is major breakage on my own testing systems), but it still needs_review (#10118).",
    "created_at": "2010-11-16T19:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89659",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:39 drkirkby]:
> Will the sphinx package that has been used as a test be in the next alpha? If so, that will test not only the build, but also the functionality. 

Yes, it will be in the next alpha (unless there is major breakage on my own testing systems), but it still needs_review (#10118).



---

archive/issue_comments_089660.json:
```json
{
    "body": "PS, it would be useful to attach a build log of the failure to build on OS X 10.4 with patch 2.6.1, along with the config.log for OS X. Just log building the upstream source, outside of Sage. I'll do likewise for Solaris 10 on SPARC.\n\nThen I can report the bug with patch 2.6.1 upstream, and provide links to the failed logs. Having provided links to failed builds on two platforms, the developers should be in a good position to fix the bug. \n\nDave",
    "created_at": "2010-11-16T19:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89660",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

PS, it would be useful to attach a build log of the failure to build on OS X 10.4 with patch 2.6.1, along with the config.log for OS X. Just log building the upstream source, outside of Sage. I'll do likewise for Solaris 10 on SPARC.

Then I can report the bug with patch 2.6.1 upstream, and provide links to the failed logs. Having provided links to failed builds on two platforms, the developers should be in a good position to fix the bug. 

Dave



---

archive/issue_comments_089661.json:
```json
{
    "body": "Fixed a trivial typo (`cannot to find...` -> `cannot find`) in `spkg-install`.\n\nNew spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg)",
    "created_at": "2010-11-18T09:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89661",
    "user": "https://github.com/jdemeyer"
}
```

Fixed a trivial typo (`cannot to find...` -> `cannot find`) in `spkg-install`.

New spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/patch-2.5.9.spkg)



---

archive/issue_comments_089662.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-18T09:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89662",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089663.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-19T07:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89663",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_023255.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-19T07:54:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9418#event-23255"
}
```



---

archive/issue_comments_089664.json:
```json
{
    "body": "See #10299 for a follow-up.",
    "created_at": "2010-11-20T19:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89664",
    "user": "https://github.com/jhpalmieri"
}
```

See #10299 for a follow-up.



---

archive/issue_comments_089665.json:
```json
{
    "body": "Replying to [comment:30 drkirkby]:\n> Replying to [comment:29 cremona]:\n> > Replying to [comment:27 drkirkby]:\n> > > I've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. \n> > \n> > That would be a colour patch, I presume?\n> > \n> I think it will be showed as red and green in the browser, though the paint was white!\n\nShould we ask Microsoft if we can make `paint` a standard spkg as well?\n\n----\n\nStop environmental pollution...\n\nWe already have nice environment variables like \"`R`\" and \"`PYTHON`\"; can we rename it to e.g. `GNU_PATCH` in `spkg/install` and `spkg/standard/deps`?\n\n----\n\nP.S.: Why not add the `patch` spkg to `$(BASE)` (and make it depend on the previous three `$(BASE)` packages)?\n\nAs is, **all** standard spkgs will get rebuilt on an upgrade (to a version of Sage with `patch` \"newly\" included) anyway. (Therefore I would actually prefer adding `patch` as a dependency selectively. `spkg/standard/deps` will be under revision control soon...)",
    "created_at": "2010-11-21T22:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89665",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:30 drkirkby]:
> Replying to [comment:29 cremona]:
> > Replying to [comment:27 drkirkby]:
> > > I've updated deps and the patch for it. The package will have to wait though, as I need to do some painting. 
> > 
> > That would be a colour patch, I presume?
> > 
> I think it will be showed as red and green in the browser, though the paint was white!

Should we ask Microsoft if we can make `paint` a standard spkg as well?

----

Stop environmental pollution...

We already have nice environment variables like "`R`" and "`PYTHON`"; can we rename it to e.g. `GNU_PATCH` in `spkg/install` and `spkg/standard/deps`?

----

P.S.: Why not add the `patch` spkg to `$(BASE)` (and make it depend on the previous three `$(BASE)` packages)?

As is, **all** standard spkgs will get rebuilt on an upgrade (to a version of Sage with `patch` "newly" included) anyway. (Therefore I would actually prefer adding `patch` as a dependency selectively. `spkg/standard/deps` will be under revision control soon...)



---

archive/issue_comments_089666.json:
```json
{
    "body": "Leif: I don't have any particular feelings either in favour of or against your suggestions.  Feel free to open a new ticket for these issues.\n\nAbout `$(BASE)`: I never quite understood the difference between `spkg/base` and `spkg/standard`.  What is the difference?",
    "created_at": "2010-11-22T08:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9418#issuecomment-89666",
    "user": "https://github.com/jdemeyer"
}
```

Leif: I don't have any particular feelings either in favour of or against your suggestions.  Feel free to open a new ticket for these issues.

About `$(BASE)`: I never quite understood the difference between `spkg/base` and `spkg/standard`.  What is the difference?
