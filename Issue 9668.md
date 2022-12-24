# Issue 9668: Fix hardcoding of paths in R binary

archive/issues_009668.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  leif jhpalmieri\n\nSee [this](http://groups.google.com/group/sage-devel/browse_thread/thread/b35848f099c763a9) thread on sage-support.\n\n\n```\nHere is how I got the optional package automap to install into a \nbinary sage R. \nGo into the sage directory and edit the following files: \nlocal/bin/R and local/lib/R/bin/R \nand change all the hard-set user variables \"/scratch/....\" to the true \nlocations of R_HOME_DIR, R_HOME, R_INCLUDE_DIR, R_SHARE_DIR and for \ngood measure, R_DOC_DIR. Replace the default string EVERYWHERE in the \nfile. \nI then exported SAGE_HOME as well (Not sure that this is needed.), and \nrun local/bin/R \nInside R, install.packages(\"automap\") \nNo more build errors, and when I restart R, automap loads using \nlibrary. Just have to try it out from sage now. \nAny chance there's a script to find all of these hard-set strings and \nchange them to correct values? \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9668\n\n",
    "created_at": "2010-08-02T14:33:47Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.9",
    "title": "Fix hardcoding of paths in R binary",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9668",
    "user": "kcrisman"
}
```
Assignee: tbd

CC:  leif jhpalmieri

See [this](http://groups.google.com/group/sage-devel/browse_thread/thread/b35848f099c763a9) thread on sage-support.


```
Here is how I got the optional package automap to install into a 
binary sage R. 
Go into the sage directory and edit the following files: 
local/bin/R and local/lib/R/bin/R 
and change all the hard-set user variables "/scratch/...." to the true 
locations of R_HOME_DIR, R_HOME, R_INCLUDE_DIR, R_SHARE_DIR and for 
good measure, R_DOC_DIR. Replace the default string EVERYWHERE in the 
file. 
I then exported SAGE_HOME as well (Not sure that this is needed.), and 
run local/bin/R 
Inside R, install.packages("automap") 
No more build errors, and when I restart R, automap loads using 
library. Just have to try it out from sage now. 
Any chance there's a script to find all of these hard-set strings and 
change them to correct values? 
```


Issue created by migration from https://trac.sagemath.org/ticket/9668





---

archive/issue_comments_093863.json:
```json
{
    "body": "IIRC I have some \"almost\" ready R spkg for #9906, which also does a lot of clean-up in `spkg-install`...",
    "created_at": "2011-08-03T14:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93863",
    "user": "leif"
}
```

IIRC I have some "almost" ready R spkg for #9906, which also does a lot of clean-up in `spkg-install`...



---

archive/issue_comments_093864.json:
```json
{
    "body": "Well, I would certainly welcome and help review this.  Anything which cleans up parts of #8274 could be commented there, and perhaps even a new ticket opened if there isn't much left.  \n\nBut what about #9668 (this ticket) itself?  Does the stuff that is \"almost\" ready at #9906 address that?",
    "created_at": "2011-08-03T15:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93864",
    "user": "kcrisman"
}
```

Well, I would certainly welcome and help review this.  Anything which cleans up parts of #8274 could be commented there, and perhaps even a new ticket opened if there isn't much left.  

But what about #9668 (this ticket) itself?  Does the stuff that is "almost" ready at #9906 address that?



---

archive/issue_comments_093865.json:
```json
{
    "body": "Replying to [comment:3 kcrisman]:\n> But what about #9668 (this ticket) itself?  Does the stuff that is \"almost\" ready at #9906 address that?\n\nNot yet, i.e. not all of it. See [comment:ticket:9906:14 this comment there].",
    "created_at": "2011-08-05T11:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93865",
    "user": "leif"
}
```

Replying to [comment:3 kcrisman]:
> But what about #9668 (this ticket) itself?  Does the stuff that is "almost" ready at #9906 address that?

Not yet, i.e. not all of it. See [comment:ticket:9906:14 this comment there].



---

archive/issue_comments_093866.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> Replying to [comment:3 kcrisman]:\n> > But what about #9668 (this ticket) itself?  Does the stuff that is \"almost\" ready at #9906 address that?\n> \n> Not yet, i.e. not all of it. See [comment:ticket:9906:14 this comment there].\n\nOk, a bit more subtle than I expected (R is quite weird, failed to build inbetween), but I now have a p6 that fixes both the `R` scripts and the `pkg-config` file (`libR.pc`).\n\n----\n\nThere was another issue with R [someone reported on sage-devel](http://groups.google.com/group/sage-devel/msg/ebb50bd73aba7d53?dmode=source) which was caused by a \"complicated\" setting of an environment variable, in this case `PAGER`, but that's certainly an upstream problem and rather exotic.",
    "created_at": "2011-08-05T16:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93866",
    "user": "leif"
}
```

Replying to [comment:4 leif]:
> Replying to [comment:3 kcrisman]:
> > But what about #9668 (this ticket) itself?  Does the stuff that is "almost" ready at #9906 address that?
> 
> Not yet, i.e. not all of it. See [comment:ticket:9906:14 this comment there].

Ok, a bit more subtle than I expected (R is quite weird, failed to build inbetween), but I now have a p6 that fixes both the `R` scripts and the `pkg-config` file (`libR.pc`).

----

There was another issue with R [someone reported on sage-devel](http://groups.google.com/group/sage-devel/msg/ebb50bd73aba7d53?dmode=source) which was caused by a "complicated" setting of an environment variable, in this case `PAGER`, but that's certainly an upstream problem and rather exotic.



---

archive/issue_comments_093867.json:
```json
{
    "body": "Replying to [comment:5 leif]:\n> Replying to [comment:4 leif]:\n> > Replying to [comment:3 kcrisman]:\n> > > But what about #9668 (this ticket) itself?  Does the stuff that is \"almost\" ready at #9906 address that?\n> > \n> > Not yet, i.e. not all of it. See [comment:ticket:9906:14 this comment there].\n> Ok, a bit more subtle than I expected (R is quite weird, failed to build inbetween), but I now have a p6 that fixes both the `R` scripts and the `pkg-config` file (`libR.pc`).\nOkay, I'll watch this space.\n> There was another issue with R [someone reported on sage-devel](http://groups.google.com/group/sage-devel/msg/ebb50bd73aba7d53?dmode=source) which was caused by a \"complicated\" setting of an environment variable, in this case `PAGER`, but that's certainly an upstream problem and rather exotic.\nAgreed.",
    "created_at": "2011-08-05T16:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93867",
    "user": "kcrisman"
}
```

Replying to [comment:5 leif]:
> Replying to [comment:4 leif]:
> > Replying to [comment:3 kcrisman]:
> > > But what about #9668 (this ticket) itself?  Does the stuff that is "almost" ready at #9906 address that?
> > 
> > Not yet, i.e. not all of it. See [comment:ticket:9906:14 this comment there].
> Ok, a bit more subtle than I expected (R is quite weird, failed to build inbetween), but I now have a p6 that fixes both the `R` scripts and the `pkg-config` file (`libR.pc`).
Okay, I'll watch this space.
> There was another issue with R [someone reported on sage-devel](http://groups.google.com/group/sage-devel/msg/ebb50bd73aba7d53?dmode=source) which was caused by a "complicated" setting of an environment variable, in this case `PAGER`, but that's certainly an upstream problem and rather exotic.
Agreed.



---

archive/issue_comments_093868.json:
```json
{
    "body": "See also #10967.  We should probably either incorporate that here, or make a followup spkg there.",
    "created_at": "2011-08-19T13:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93868",
    "user": "kcrisman"
}
```

See also #10967.  We should probably either incorporate that here, or make a followup spkg there.



---

archive/issue_comments_093869.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> See also #10967.  We should probably either incorporate that here, or make a followup spkg there.  \n\nAlmost certainly the former.\n\n[Note to myself:]\n\nThe problem is that removing any reference to `SAGE_ROOT` and `SAGE_LOCAL` disables the script being \"automatically\" relocated in the first place.\n\nI'll then have to guess `SAGE_ROOT` if none of Sage's variables are defined. We also have two copies of the R script, one in `local/bin/`, and one in `local/lib/R/bin/`.",
    "created_at": "2011-08-19T14:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93869",
    "user": "leif"
}
```

Replying to [comment:7 kcrisman]:
> See also #10967.  We should probably either incorporate that here, or make a followup spkg there.  

Almost certainly the former.

[Note to myself:]

The problem is that removing any reference to `SAGE_ROOT` and `SAGE_LOCAL` disables the script being "automatically" relocated in the first place.

I'll then have to guess `SAGE_ROOT` if none of Sage's variables are defined. We also have two copies of the R script, one in `local/bin/`, and one in `local/lib/R/bin/`.



---

archive/issue_comments_093870.json:
```json
{
    "body": "Changing keywords from \"\" to \"R spkg R.sh.in libR.pc pkg-config hard-coded package installation R_HOME_DIR\".",
    "created_at": "2011-08-21T00:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93870",
    "user": "leif"
}
```

Changing keywords from "" to "R spkg R.sh.in libR.pc pkg-config hard-coded package installation R_HOME_DIR".



---

archive/issue_comments_093871.json:
```json
{
    "body": "Changing assignee from tbd to leif.",
    "created_at": "2011-08-21T00:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93871",
    "user": "leif"
}
```

Changing assignee from tbd to leif.



---

archive/issue_comments_093872.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> [Note to myself:] \n\n> \n> The problem is that removing any reference to `SAGE_ROOT` and `SAGE_LOCAL` disables the script being \"automatically\" relocated in the first place.\n> \n> I'll then have to guess `SAGE_ROOT` if none of Sage's variables are defined. We also have two copies of the R script, one in `local/bin/`, and one in `local/lib/R/bin/`.\n\nGuessing `SAGE_ROOT` there is simply bullshit. Simply add a sanity check, pointing to `sage --R`, `install_scripts()` and perhaps `sage --sh` in case `SAGE_LOCAL` isn't defined.\n\nFurthermore:\n\n* Address / check the following (copied from [comment:ticket:10967:14]):\n\n```\nThe problem was with hard-coded paths, not the \npermissions.  Anyway, the fix was easy.  I opened all the files listed \nabove by George: \nsage/local/lib/R/bin/R \nsage/local/lib/R/bin/libtool \nsage/local/lib/R/etc/Makeconf \nsage/local/lib/R/etc/ldpath \nsage/local/lib/R/etc/Renviron \nsage/local/bin/R \nand edited obvious lines containing hardcoded paths (using find- \nreplace-all at once). \n```\n\n\n* Change `libR.pc` to use either `${pc_top_builddir}` or `$${SAGE_ROOT}`. (In the former case, perhaps also set `PC_TOP_BUILD_DIR` to `$SAGE_ROOT`, or prepend `$SAGE_ROOT:`, unless it is already contained.)",
    "created_at": "2011-08-21T00:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93872",
    "user": "leif"
}
```

Replying to [comment:8 leif]:
> [Note to myself:] 

> 
> The problem is that removing any reference to `SAGE_ROOT` and `SAGE_LOCAL` disables the script being "automatically" relocated in the first place.
> 
> I'll then have to guess `SAGE_ROOT` if none of Sage's variables are defined. We also have two copies of the R script, one in `local/bin/`, and one in `local/lib/R/bin/`.

Guessing `SAGE_ROOT` there is simply bullshit. Simply add a sanity check, pointing to `sage --R`, `install_scripts()` and perhaps `sage --sh` in case `SAGE_LOCAL` isn't defined.

Furthermore:

* Address / check the following (copied from [comment:ticket:10967:14]):

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


* Change `libR.pc` to use either `${pc_top_builddir}` or `$${SAGE_ROOT}`. (In the former case, perhaps also set `PC_TOP_BUILD_DIR` to `$SAGE_ROOT`, or prepend `$SAGE_ROOT:`, unless it is already contained.)



---

archive/issue_comments_093873.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n>  * Change `libR.pc` to use either `${pc_top_builddir}` or `$${SAGE_ROOT}`. (In the former case, perhaps also set `PC_TOP_BUILD_DIR` to `$SAGE_ROOT`, or prepend `$SAGE_ROOT:`, unless it is already contained.)\n\nShould read:\n\n* Change `libR.pc` to use either `${pc_top_builddir}` or `$${SAGE_ROOT}`. (In the former case, set `PKG_CONFIG_TOP_BUILD_DIR` to `$SAGE_ROOT` unless it is already, perhaps issuing a warning in case it isn't, or especially if its setting differs.) \n\n  Also prepend `$SAGE_ROOT/local/lib/pkgconfig` to `PKG_CONFIG_PATH`, unless it is already contained. Warn if `PKG_CONFIG_PATH` is empty, then set it to `$SAGE_ROOT/local/lib/pkgconfig`.",
    "created_at": "2011-08-21T02:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93873",
    "user": "leif"
}
```

Replying to [comment:9 leif]:
>  * Change `libR.pc` to use either `${pc_top_builddir}` or `$${SAGE_ROOT}`. (In the former case, perhaps also set `PC_TOP_BUILD_DIR` to `$SAGE_ROOT`, or prepend `$SAGE_ROOT:`, unless it is already contained.)

Should read:

* Change `libR.pc` to use either `${pc_top_builddir}` or `$${SAGE_ROOT}`. (In the former case, set `PKG_CONFIG_TOP_BUILD_DIR` to `$SAGE_ROOT` unless it is already, perhaps issuing a warning in case it isn't, or especially if its setting differs.) 

  Also prepend `$SAGE_ROOT/local/lib/pkgconfig` to `PKG_CONFIG_PATH`, unless it is already contained. Warn if `PKG_CONFIG_PATH` is empty, then set it to `$SAGE_ROOT/local/lib/pkgconfig`.



---

archive/issue_comments_093874.json:
```json
{
    "body": "Changing keywords from \"R spkg R.sh.in libR.pc pkg-config hard-coded package installation R_HOME_DIR\" to \"R spkg R.sh.in libR.pc pkg-config hard-coded package installation R_HOME_DIR sd32\".",
    "created_at": "2011-08-24T23:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93874",
    "user": "was"
}
```

Changing keywords from "R spkg R.sh.in libR.pc pkg-config hard-coded package installation R_HOME_DIR" to "R spkg R.sh.in libR.pc pkg-config hard-coded package installation R_HOME_DIR sd32".



---

archive/issue_comments_093875.json:
```json
{
    "body": "Changing keywords from \"R spkg R.sh.in libR.pc pkg-config hard-coded package installation R_HOME_DIR sd32\" to \"R spkg R.sh.in libR.pc pkg-config hard-coded package installation R_HOME_DIR sd32 r-project\".",
    "created_at": "2011-11-20T01:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93875",
    "user": "kcrisman"
}
```

Changing keywords from "R spkg R.sh.in libR.pc pkg-config hard-coded package installation R_HOME_DIR sd32" to "R spkg R.sh.in libR.pc pkg-config hard-coded package installation R_HOME_DIR sd32 r-project".



---

archive/issue_comments_093876.json:
```json
{
    "body": "This problem prevents Sage from being relocatable on Solaris, or at least on the skynet machines mark and mark2: if I build Sage, then move the entire Sage directory, then run `sage` so the relocation scripts get executed, and then run `sage -R`, I get an error:\n\n```\n$ ./sage -R\nld.so.1: R: fatal: libgcc_s.so.1: version `GCC_4.3.0' not found (required by file /usr/local/gcc-4.7.0/sparc-SunOS-ultrasparc3/lib/libgomp.so.1)\nld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory\n/home/palmieri/mark2/sage-5.4.rc2-7797/spkg/bin/sage: line 457: 28710 Killed                  \"$SAGE_LOCAL/bin/R\" \"$@\"\n```\n\nI tried just modifying local/bin/R and local/lib/R/bin/R, replacing the hard-coded paths with `$SAGE_ROOT`, but I still got an error.",
    "created_at": "2012-10-26T16:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93876",
    "user": "jhpalmieri"
}
```

This problem prevents Sage from being relocatable on Solaris, or at least on the skynet machines mark and mark2: if I build Sage, then move the entire Sage directory, then run `sage` so the relocation scripts get executed, and then run `sage -R`, I get an error:

```
$ ./sage -R
ld.so.1: R: fatal: libgcc_s.so.1: version `GCC_4.3.0' not found (required by file /usr/local/gcc-4.7.0/sparc-SunOS-ultrasparc3/lib/libgomp.so.1)
ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory
/home/palmieri/mark2/sage-5.4.rc2-7797/spkg/bin/sage: line 457: 28710 Killed                  "$SAGE_LOCAL/bin/R" "$@"
```

I tried just modifying local/bin/R and local/lib/R/bin/R, replacing the hard-coded paths with `$SAGE_ROOT`, but I still got an error.



---

archive/issue_comments_093877.json:
```json
{
    "body": "I doubt this is related to the original topic at all.  The setup on skynet's Solaris machines is (or used to be) quite broken, as there are outdated versions of shared libraries left around in typical paths, and some R scripts insist on messing up your paths such that the former gets relevant.\n\nUnfortunately I don't recall what the exact problem was, and how I managed to work around it, just that I had to [and *somehow* successfully did]; I think this problem appeared with, or was related to, [the installation of] GCC 4.7.0.  In case I am right, changing `PATH` and/or `LD_LIBRARY_PATH` should \"solve\" the issue.\n\nSorry for not being of much help here, at least right now... ;-)",
    "created_at": "2012-10-26T19:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93877",
    "user": "leif"
}
```

I doubt this is related to the original topic at all.  The setup on skynet's Solaris machines is (or used to be) quite broken, as there are outdated versions of shared libraries left around in typical paths, and some R scripts insist on messing up your paths such that the former gets relevant.

Unfortunately I don't recall what the exact problem was, and how I managed to work around it, just that I had to [and *somehow* successfully did]; I think this problem appeared with, or was related to, [the installation of] GCC 4.7.0.  In case I am right, changing `PATH` and/or `LD_LIBRARY_PATH` should "solve" the issue.

Sorry for not being of much help here, at least right now... ;-)



---

archive/issue_comments_093878.json:
```json
{
    "body": "Well, if the problems on mark are not related, then for this ticket, we could just add some lines at the end of spkg-install:\n\n```\n# Make R relocatable by using \"$SAGE_ROOT\" instead of the hardcoded path.\nsed -e \"s|$SAGE_ROOT|\\$SAGE_ROOT/|\" \"$SAGE_LOCAL/bin/R\" > \"$SAGE_LOCAL/bin/R.tmp\" && mv \"$SAGE_LOCAL/bin/R.tmp\" \"$SAGE_LOCAL/bin/R\" && chmod a+x \"$SAGE_LOCAL/bin/R\"\nsed -e \"s|$SAGE_ROOT|\\$SAGE_ROOT/|\" \"$SAGE_LOCAL/lib/R/bin/R\" > \"$SAGE_LOCAL/lib/R/bin/R.tmp\" && mv \"$SAGE_LOCAL/lib/R/bin/R.tmp\" \"$SAGE_LOCAL/lib/R/bin/R\" && chmod a+x \"$SAGE_LOCAL/lib/R/bin/R\"\n```\n\n(It's too bad that the `-i` flag for sed is not portable.) `libR.pc` already uses SAGE_ROOT. What else needs to be done?",
    "created_at": "2012-10-26T19:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93878",
    "user": "jhpalmieri"
}
```

Well, if the problems on mark are not related, then for this ticket, we could just add some lines at the end of spkg-install:

```
# Make R relocatable by using "$SAGE_ROOT" instead of the hardcoded path.
sed -e "s|$SAGE_ROOT|\$SAGE_ROOT/|" "$SAGE_LOCAL/bin/R" > "$SAGE_LOCAL/bin/R.tmp" && mv "$SAGE_LOCAL/bin/R.tmp" "$SAGE_LOCAL/bin/R" && chmod a+x "$SAGE_LOCAL/bin/R"
sed -e "s|$SAGE_ROOT|\$SAGE_ROOT/|" "$SAGE_LOCAL/lib/R/bin/R" > "$SAGE_LOCAL/lib/R/bin/R.tmp" && mv "$SAGE_LOCAL/lib/R/bin/R.tmp" "$SAGE_LOCAL/lib/R/bin/R" && chmod a+x "$SAGE_LOCAL/lib/R/bin/R"
```

(It's too bad that the `-i` flag for sed is not portable.) `libR.pc` already uses SAGE_ROOT. What else needs to be done?



---

archive/issue_comments_093879.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-10-26T20:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93879",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093880.json:
```json
{
    "body": "I've posted a new spkg, along with the corresponding patch.",
    "created_at": "2012-10-26T20:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93880",
    "user": "jhpalmieri"
}
```

I've posted a new spkg, along with the corresponding patch.



---

archive/issue_comments_093881.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n>  * Address / check the following (copied from [comment:ticket:10967:14]):\n> {{{\n> The problem was with hard-coded paths, not the \n> permissions.  Anyway, the fix was easy.  I opened all the files listed \n> above by George: \n> sage/local/lib/R/bin/R \n> sage/local/lib/R/bin/libtool \n> sage/local/lib/R/etc/Makeconf \n> sage/local/lib/R/etc/ldpath \n> sage/local/lib/R/etc/Renviron \n> sage/local/bin/R \n> and edited obvious lines containing hardcoded paths (using find- \n> replace-all at once). \n> }}}\nIt's easy enough to add these to the \"for\" loop that I added to spkg-install, so I might as well do that. For what it's worth, the binary files `Rscript` in both local/bin and local/lib/R/bin also have the path hard-coded in them, but I don't know how to fix this, or whether it's important. When are those files used?",
    "created_at": "2012-10-26T20:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93881",
    "user": "jhpalmieri"
}
```

Replying to [comment:9 leif]:
>  * Address / check the following (copied from [comment:ticket:10967:14]):
> {{{
> The problem was with hard-coded paths, not the 
> permissions.  Anyway, the fix was easy.  I opened all the files listed 
> above by George: 
> sage/local/lib/R/bin/R 
> sage/local/lib/R/bin/libtool 
> sage/local/lib/R/etc/Makeconf 
> sage/local/lib/R/etc/ldpath 
> sage/local/lib/R/etc/Renviron 
> sage/local/bin/R 
> and edited obvious lines containing hardcoded paths (using find- 
> replace-all at once). 
> }}}
It's easy enough to add these to the "for" loop that I added to spkg-install, so I might as well do that. For what it's worth, the binary files `Rscript` in both local/bin and local/lib/R/bin also have the path hard-coded in them, but I don't know how to fix this, or whether it's important. When are those files used?



---

archive/issue_comments_093882.json:
```json
{
    "body": "Attachment [trac_9668-r.patch](tarball://root/attachments/some-uuid/ticket9668/trac_9668-r.patch) by jhpalmieri created at 2012-10-26 21:07:50\n\npatch for R spkg; for review only",
    "created_at": "2012-10-26T21:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93882",
    "user": "jhpalmieri"
}
```

Attachment [trac_9668-r.patch](tarball://root/attachments/some-uuid/ticket9668/trac_9668-r.patch) by jhpalmieri created at 2012-10-26 21:07:50

patch for R spkg; for review only



---

archive/issue_comments_093883.json:
```json
{
    "body": "This patch for the spkg makes sense to me, anyway.\n\nDid you end up changing the libR.pc stuff in comment:10?  Or was that done elsewhere?",
    "created_at": "2013-01-03T21:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93883",
    "user": "kcrisman"
}
```

This patch for the spkg makes sense to me, anyway.

Did you end up changing the libR.pc stuff in comment:10?  Or was that done elsewhere?



---

archive/issue_comments_093884.json:
```json
{
    "body": "The \".pc\" files are handled by the `sage-location` script, I think. In any case, I believe that if you run `make build` on a fresh Sage tarball, then libR.pc should be in good shape.",
    "created_at": "2013-01-03T21:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93884",
    "user": "jhpalmieri"
}
```

The ".pc" files are handled by the `sage-location` script, I think. In any case, I believe that if you run `make build` on a fresh Sage tarball, then libR.pc should be in good shape.



---

archive/issue_comments_093885.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-03T21:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93885",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093886.json:
```json
{
    "body": "This looks good, and I now recall the sage-location discussion.  I think this is ready to go; it behaves as advertised.   I can't check whether this fixes the problems on Solaris directly, but it should fix the problem in the original post too - well, if such a person were to upgrade the spkg without just downloading a new Sage.",
    "created_at": "2013-01-03T21:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93886",
    "user": "kcrisman"
}
```

This looks good, and I now recall the sage-location discussion.  I think this is ready to go; it behaves as advertised.   I can't check whether this fixes the problems on Solaris directly, but it should fix the problem in the original post too - well, if such a person were to upgrade the spkg without just downloading a new Sage.



---

archive/issue_comments_093887.json:
```json
{
    "body": "A slight correction to what I said before: just doing `make build` doesn't fix libR.pc, but running Sage once takes care of it.",
    "created_at": "2013-01-03T22:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93887",
    "user": "jhpalmieri"
}
```

A slight correction to what I said before: just doing `make build` doesn't fix libR.pc, but running Sage once takes care of it.



---

archive/issue_comments_093888.json:
```json
{
    "body": "Or anything else that triggers `sage-location` (nowadays, any spkg upgrade even), yes.",
    "created_at": "2013-01-04T01:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93888",
    "user": "kcrisman"
}
```

Or anything else that triggers `sage-location` (nowadays, any spkg upgrade even), yes.



---

archive/issue_comments_093889.json:
```json
{
    "body": "I think using `sed` for this is very fragile, as any special characters in `$SAGE_ROOT` might cause this script to malfunction. A better solution would be to patch the R sources. This is already partially done (see `R.sh.patch` in the R sources) to allow for basic relocation of R, but apparently installing R packages doesn't work.",
    "created_at": "2013-01-04T12:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93889",
    "user": "jdemeyer"
}
```

I think using `sed` for this is very fragile, as any special characters in `$SAGE_ROOT` might cause this script to malfunction. A better solution would be to patch the R sources. This is already partially done (see `R.sh.patch` in the R sources) to allow for basic relocation of R, but apparently installing R packages doesn't work.



---

archive/issue_comments_093890.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-01-04T12:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93890",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093891.json:
```json
{
    "body": "Replying to [comment:25 jdemeyer]:\n> I think using `sed` for this is very fragile, as any special characters in `$SAGE_ROOT` might cause this script to malfunction. A better \nOut of curiosity, do we have any current restrictions on the characters in `$SAGE_ROOT`?  I feel like we already don't allow whitespace, though that might be an old memory.  Does Sage work in non-ASCII paths as well, say with Cyrillic characters?",
    "created_at": "2013-01-04T14:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93891",
    "user": "kcrisman"
}
```

Replying to [comment:25 jdemeyer]:
> I think using `sed` for this is very fragile, as any special characters in `$SAGE_ROOT` might cause this script to malfunction. A better 
Out of curiosity, do we have any current restrictions on the characters in `$SAGE_ROOT`?  I feel like we already don't allow whitespace, though that might be an old memory.  Does Sage work in non-ASCII paths as well, say with Cyrillic characters?



---

archive/issue_comments_093892.json:
```json
{
    "body": "Replying to [comment:26 kcrisman]:\n> Out of curiosity, do we have any current restrictions on the characters in `$SAGE_ROOT`?\nWe certainly do, although only \"no spaces\" is documented.\n\nBut I doubt Sage will work correctly with a directory like `/home/jdemeyer/.#|\"+*=`@`$'` (which is a valid UNIX filename)",
    "created_at": "2013-01-04T15:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93892",
    "user": "jdemeyer"
}
```

Replying to [comment:26 kcrisman]:
> Out of curiosity, do we have any current restrictions on the characters in `$SAGE_ROOT`?
We certainly do, although only "no spaces" is documented.

But I doubt Sage will work correctly with a directory like `/home/jdemeyer/.#|"+*=`@`$'` (which is a valid UNIX filename)



---

archive/issue_comments_093893.json:
```json
{
    "body": "> > Out of curiosity, do we have any current restrictions on the characters in `$SAGE_ROOT`?\n> We certainly do, although only \"no spaces\" is documented.\n> \n> But I doubt Sage will work correctly with a directory like `/home/jdemeyer/.#|\"+*=`@`$'` (which is a valid UNIX filename)\nYou sound like you're arguing that we might as well use `sed` :-)  If I wasn't lazy I'd try to grep through other spkgs to see if it's used elsewhere - I'm almost sure I've seen it in use before...",
    "created_at": "2013-01-04T15:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93893",
    "user": "kcrisman"
}
```

> > Out of curiosity, do we have any current restrictions on the characters in `$SAGE_ROOT`?
> We certainly do, although only "no spaces" is documented.
> 
> But I doubt Sage will work correctly with a directory like `/home/jdemeyer/.#|"+*=`@`$'` (which is a valid UNIX filename)
You sound like you're arguing that we might as well use `sed` :-)  If I wasn't lazy I'd try to grep through other spkgs to see if it's used elsewhere - I'm almost sure I've seen it in use before...



---

archive/issue_comments_093894.json:
```json
{
    "body": "Attachment [trac_9668-r.v2.patch](tarball://root/attachments/some-uuid/ticket9668/trac_9668-r.v2.patch) by jhpalmieri created at 2013-02-01 02:12:11\n\npatch for R spkg; for review only",
    "created_at": "2013-02-01T02:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93894",
    "user": "jhpalmieri"
}
```

Attachment [trac_9668-r.v2.patch](tarball://root/attachments/some-uuid/ticket9668/trac_9668-r.v2.patch) by jhpalmieri created at 2013-02-01 02:12:11

patch for R spkg; for review only



---

archive/issue_comments_093895.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-02-01T02:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93895",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_093896.json:
```json
{
    "body": "Here is another attempt at fixing this.",
    "created_at": "2013-02-01T02:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93896",
    "user": "jhpalmieri"
}
```

Here is another attempt at fixing this.



---

archive/issue_comments_093897.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-02-01T06:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93897",
    "user": "jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093898.json:
```json
{
    "body": "Wishful thinking: I accidentally set this to \"positive review\". Oops.\n\nI think the changes in [attachment:trac_9668-r.v2.patch] could be polished a bit, but I'm not going to bother until people agree with the general approach.",
    "created_at": "2013-02-01T06:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93898",
    "user": "jhpalmieri"
}
```

Wishful thinking: I accidentally set this to "positive review". Oops.

I think the changes in [attachment:trac_9668-r.v2.patch] could be polished a bit, but I'm not going to bother until people agree with the general approach.



---

archive/issue_comments_093899.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-02-01T06:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93899",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093900.json:
```json
{
    "body": "I don't like this at all:\n\n```\n./configure --prefix=\"\\$SAGE_LOCAL\"\n```\n\nIf it works, you're probably relying on a bug. Why is it needed?\n\nAlso, the first hunk in `Makefile.in.patch` is not needed.\n\nIn any case, this needs to be rebased as R has been upgraded.",
    "created_at": "2013-03-16T22:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93900",
    "user": "jdemeyer"
}
```

I don't like this at all:

```
./configure --prefix="\$SAGE_LOCAL"
```

If it works, you're probably relying on a bug. Why is it needed?

Also, the first hunk in `Makefile.in.patch` is not needed.

In any case, this needs to be rebased as R has been upgraded.



---

archive/issue_comments_093901.json:
```json
{
    "body": "Replying to [comment:32 jdemeyer]:\n> I don't like this at all:\n> {{{\n> ./configure --prefix=\"\\$SAGE_LOCAL\"\n> }}}\n> If it works, you're probably relying on a bug. Why is it needed?\n\nIf I remember correctly, the prefix directory gets written into various of the files in `SAGE_LOCAL/lib/R/bin/`, so using `\\$SAGE_LOCAL` instead of `$SAGE_LOCAL` means that \"$SAGE_LOCAL\" gets written verbatim to the file, instead of expanded first and then written. This makes those files relocatable.\n\nWhy don't you like it?",
    "created_at": "2013-03-16T23:55:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93901",
    "user": "jhpalmieri"
}
```

Replying to [comment:32 jdemeyer]:
> I don't like this at all:
> {{{
> ./configure --prefix="\$SAGE_LOCAL"
> }}}
> If it works, you're probably relying on a bug. Why is it needed?

If I remember correctly, the prefix directory gets written into various of the files in `SAGE_LOCAL/lib/R/bin/`, so using `\$SAGE_LOCAL` instead of `$SAGE_LOCAL` means that "$SAGE_LOCAL" gets written verbatim to the file, instead of expanded first and then written. This makes those files relocatable.

Why don't you like it?



---

archive/issue_comments_093902.json:
```json
{
    "body": "Replying to [comment:33 jhpalmieri]:\n> Why don't you like it?\nBecause the fact that it works looks like a bug rather than a feature.",
    "created_at": "2013-03-17T10:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93902",
    "user": "jdemeyer"
}
```

Replying to [comment:33 jhpalmieri]:
> Why don't you like it?
Because the fact that it works looks like a bug rather than a feature.



---

archive/issue_comments_093903.json:
```json
{
    "body": "If you look at `src/scripts/R.sh.in`, it has lines like\n\n```\n        R_HOME_DIR=\"@prefix@/${libnn}/R\"\n```\n\nMy understanding is that `prefix` gets set by the configure script, stored in `Makefile.conf`, and then read by `src/scripts/Makefile` so this variable's value can get used when making the R script. In particular, the R people are deliberately using the `prefix` variable here. So it looks like their design decision, not a bug. But I'm not sure I understand your point.",
    "created_at": "2013-03-17T15:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93903",
    "user": "jhpalmieri"
}
```

If you look at `src/scripts/R.sh.in`, it has lines like

```
        R_HOME_DIR="@prefix@/${libnn}/R"
```

My understanding is that `prefix` gets set by the configure script, stored in `Makefile.conf`, and then read by `src/scripts/Makefile` so this variable's value can get used when making the R script. In particular, the R people are deliberately using the `prefix` variable here. So it looks like their design decision, not a bug. But I'm not sure I understand your point.



---

archive/issue_comments_093904.json:
```json
{
    "body": "Replying to [comment:35 jhpalmieri]:\n> If you look at `src/scripts/R.sh.in`, it has lines like\n> {{{\n>         R_HOME_DIR=\"`@`prefix`@`/${libnn}/R\"\n> }}}\nThis line is completely irrelevant, as we already patch `R.sh.in` to overwrite `R_HOME_DIR`.",
    "created_at": "2013-03-17T15:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93904",
    "user": "jdemeyer"
}
```

Replying to [comment:35 jhpalmieri]:
> If you look at `src/scripts/R.sh.in`, it has lines like
> {{{
>         R_HOME_DIR="`@`prefix`@`/${libnn}/R"
> }}}
This line is completely irrelevant, as we already patch `R.sh.in` to overwrite `R_HOME_DIR`.



---

archive/issue_comments_093905.json:
```json
{
    "body": "Attachment [trac_9668-r.v3.patch](tarball://root/attachments/some-uuid/ticket9668/trac_9668-r.v3.patch) by jhpalmieri created at 2013-03-18 01:02:42",
    "created_at": "2013-03-18T01:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93905",
    "user": "jhpalmieri"
}
```

Attachment [trac_9668-r.v3.patch](tarball://root/attachments/some-uuid/ticket9668/trac_9668-r.v3.patch) by jhpalmieri created at 2013-03-18 01:02:42



---

archive/issue_comments_093906.json:
```json
{
    "body": "I'll post a new version of the spkg when sage.math is back up. I've attached the patch. This has the effect of changing lines in `local/bin/R` (and the corresponding file `local/lib/R/bin/R`) from\n\n```\nR_SHARE_DIR=.../sage-5.8.beta4/local/lib/R/share\nexport R_SHARE_DIR\nR_INCLUDE_DIR=.../sage-5.8.beta4/local/lib/R/include\nexport R_INCLUDE_DIR\nR_DOC_DIR=.../sage-5.8.beta4/local/lib/R/doc\nexport R_DOC_DIR\n```\n\nto\n\n```\nR_SHARE_DIR=\"${R_HOME_DIR}/share\"\nexport R_SHARE_DIR\nR_INCLUDE_DIR=\"${R_HOME_DIR}/include\"\nexport R_INCLUDE_DIR\nR_DOC_DIR=\"${R_HOME_DIR}/doc\"\nexport R_DOC_DIR\n```\n\nWith this change, running `sage -R` and then `install.packages(\"automap\")` seems to work.",
    "created_at": "2013-03-18T01:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93906",
    "user": "jhpalmieri"
}
```

I'll post a new version of the spkg when sage.math is back up. I've attached the patch. This has the effect of changing lines in `local/bin/R` (and the corresponding file `local/lib/R/bin/R`) from

```
R_SHARE_DIR=.../sage-5.8.beta4/local/lib/R/share
export R_SHARE_DIR
R_INCLUDE_DIR=.../sage-5.8.beta4/local/lib/R/include
export R_INCLUDE_DIR
R_DOC_DIR=.../sage-5.8.beta4/local/lib/R/doc
export R_DOC_DIR
```

to

```
R_SHARE_DIR="${R_HOME_DIR}/share"
export R_SHARE_DIR
R_INCLUDE_DIR="${R_HOME_DIR}/include"
export R_INCLUDE_DIR
R_DOC_DIR="${R_HOME_DIR}/doc"
export R_DOC_DIR
```

With this change, running `sage -R` and then `install.packages("automap")` seems to work.



---

archive/issue_comments_093907.json:
```json
{
    "body": "New spkg posted.",
    "created_at": "2013-03-18T17:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93907",
    "user": "jhpalmieri"
}
```

New spkg posted.



---

archive/issue_comments_093908.json:
```json
{
    "body": "Replying to [comment:37 jhpalmieri]:\n> I'll post a new version of the spkg when sage.math is back up.\n\nReplying to [comment:38 jhpalmieri]:\n> New spkg posted.\n\nI still cannot log into sage.math... ;-)",
    "created_at": "2013-03-18T18:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93908",
    "user": "leif"
}
```

Replying to [comment:37 jhpalmieri]:
> I'll post a new version of the spkg when sage.math is back up.

Replying to [comment:38 jhpalmieri]:
> New spkg posted.

I still cannot log into sage.math... ;-)



---

archive/issue_comments_093909.json:
```json
{
    "body": "Replying to [comment:39 leif]:\n> Replying to [comment:37 jhpalmieri]:\n> > I'll post a new version of the spkg when sage.math is back up.\n> \n> Replying to [comment:38 jhpalmieri]:\n> > New spkg posted.\n> \n> I still cannot log into sage.math... ;-)\n\nI did an `scp` to boxen. If you want, I can try to keep my promise by posting the new version (again) when sage.math comes back up...",
    "created_at": "2013-03-18T18:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93909",
    "user": "jhpalmieri"
}
```

Replying to [comment:39 leif]:
> Replying to [comment:37 jhpalmieri]:
> > I'll post a new version of the spkg when sage.math is back up.
> 
> Replying to [comment:38 jhpalmieri]:
> > New spkg posted.
> 
> I still cannot log into sage.math... ;-)

I did an `scp` to boxen. If you want, I can try to keep my promise by posting the new version (again) when sage.math comes back up...



---

archive/issue_comments_093910.json:
```json
{
    "body": "For what it's worth, someone reported on [ask.sagemath.org](http://ask.sagemath.org/question/2476/cant-install-r-packages-in-sage) that this spkg fixed their problem with installing an R package.",
    "created_at": "2013-04-16T17:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93910",
    "user": "jhpalmieri"
}
```

For what it's worth, someone reported on [ask.sagemath.org](http://ask.sagemath.org/question/2476/cant-install-r-packages-in-sage) that this spkg fixed their problem with installing an R package.



---

archive/issue_comments_093911.json:
```json
{
    "body": "I think that sounds like a positive review, combined with Jeroen's good comments... What do you think?",
    "created_at": "2013-04-16T17:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93911",
    "user": "kcrisman"
}
```

I think that sounds like a positive review, combined with Jeroen's good comments... What do you think?



---

archive/issue_comments_093912.json:
```json
{
    "body": "I think that someone should confirm that with the new spkg, in the script `local/bin/R`, the variables `R_SHARE_DIR`, `R_INCLUDE_DIR`, and `R_DOC_DIR` are now defined in terms of `R_HOME_DIR` rather than being hard-coded paths as they are with the current spkg.",
    "created_at": "2013-04-16T17:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93912",
    "user": "jhpalmieri"
}
```

I think that someone should confirm that with the new spkg, in the script `local/bin/R`, the variables `R_SHARE_DIR`, `R_INCLUDE_DIR`, and `R_DOC_DIR` are now defined in terms of `R_HOME_DIR` rather than being hard-coded paths as they are with the current spkg.



---

archive/issue_comments_093913.json:
```json
{
    "body": "> I think that someone should confirm that with the new spkg, in the script `local/bin/R`, the variables `R_SHARE_DIR`, `R_INCLUDE_DIR`, and `R_DOC_DIR` are now defined in terms of `R_HOME_DIR` rather than being hard-coded paths as they are with the current spkg.\nI can do this.",
    "created_at": "2013-04-16T19:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93913",
    "user": "kcrisman"
}
```

> I think that someone should confirm that with the new spkg, in the script `local/bin/R`, the variables `R_SHARE_DIR`, `R_INCLUDE_DIR`, and `R_DOC_DIR` are now defined in terms of `R_HOME_DIR` rather than being hard-coded paths as they are with the current spkg.
I can do this.



---

archive/issue_comments_093914.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-16T19:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93914",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093915.json:
```json
{
    "body": "I confirmed that moving a Sage install (not just binary) caused installing an R package to fail with precisely the problems one would expect if these were incorrectly defined (e.g. \n\n```\nWarning: R include directory is empty -- perhaps need to install R-devel.rpm or similar\n```\n\nwith appropriate nonexistent directory referenced).  The script `local/bin/R` had the (now incorrect) paths.  \n\nThen installing this spkg and retrying caused success, and `local/bin/R` looks right now too.  Nice work!",
    "created_at": "2013-04-16T19:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93915",
    "user": "kcrisman"
}
```

I confirmed that moving a Sage install (not just binary) caused installing an R package to fail with precisely the problems one would expect if these were incorrectly defined (e.g. 

```
Warning: R include directory is empty -- perhaps need to install R-devel.rpm or similar
```

with appropriate nonexistent directory referenced).  The script `local/bin/R` had the (now incorrect) paths.  

Then installing this spkg and retrying caused success, and `local/bin/R` looks right now too.  Nice work!



---

archive/issue_comments_093916.json:
```json
{
    "body": "One question, though... when I move Sage back and run Sage, it doesn't change `R_HOME_DIR` back.\n\n```\nR_HOME_DIR=/Users/.../Downloads/tempR/sage-5.9.beta5/local/lib/R\n```\n\nwhen it should be\n\n```\nR_HOME_DIR=/Users/.../Downloads/sage-5.9.beta5/local/lib/R\n```\n\nSo this was changed, presumably, when I reinstalled the spkg.  It doesn't impact installing new R packages, by the way, nor functionality of R.\n\nIn particular, moving a *different* Sage installation and starting Sage changes some things, but doesn't change the location of `R_HOME_DIR` in `local/bin/R`.    I'm not sure why that doesn't affect functionality, but presumably this should somehow be taken care of.  On this ticket?",
    "created_at": "2013-04-16T20:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93916",
    "user": "kcrisman"
}
```

One question, though... when I move Sage back and run Sage, it doesn't change `R_HOME_DIR` back.

```
R_HOME_DIR=/Users/.../Downloads/tempR/sage-5.9.beta5/local/lib/R
```

when it should be

```
R_HOME_DIR=/Users/.../Downloads/sage-5.9.beta5/local/lib/R
```

So this was changed, presumably, when I reinstalled the spkg.  It doesn't impact installing new R packages, by the way, nor functionality of R.

In particular, moving a *different* Sage installation and starting Sage changes some things, but doesn't change the location of `R_HOME_DIR` in `local/bin/R`.    I'm not sure why that doesn't affect functionality, but presumably this should somehow be taken care of.  On this ticket?



---

archive/issue_comments_093917.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2013-04-16T20:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93917",
    "user": "kcrisman"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_093918.json:
```json
{
    "body": "It took me a little while to understand this, too. Right before the lines defining `R_SHARE_DIR`, etc., there are lines\n\n```sh\nif test x$SAGE_BUILDING_R = x; then\n    R_HOME_DIR=\"$SAGE_LOCAL/lib/R/\"\nfi\n```\n\nIf you're not *building* the R spkg, then this will be executed, overriding the hard-coded path earlier in the script, and setting `R_HOME_DIR` to the desired portable setting. I don't know R, so I don't know how to test this: if you run `sage -R`, can you execute some R command to tell you the current setting of `R_HOME_DIR`?",
    "created_at": "2013-04-16T22:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93918",
    "user": "jhpalmieri"
}
```

It took me a little while to understand this, too. Right before the lines defining `R_SHARE_DIR`, etc., there are lines

```sh
if test x$SAGE_BUILDING_R = x; then
    R_HOME_DIR="$SAGE_LOCAL/lib/R/"
fi
```

If you're not *building* the R spkg, then this will be executed, overriding the hard-coded path earlier in the script, and setting `R_HOME_DIR` to the desired portable setting. I don't know R, so I don't know how to test this: if you run `sage -R`, can you execute some R command to tell you the current setting of `R_HOME_DIR`?



---

archive/issue_comments_093919.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-04-17T01:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93919",
    "user": "kcrisman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_093920.json:
```json
{
    "body": "Well, that is a Sage-specific thing, I think, but we have\n\n```\nR_HOME=\"${R_HOME_DIR}\"\n```\n\nlater on and also\n\n```\n$ ./sage -R RHOME\n/Users/.../Downloads/sage-5.9.beta5/local/lib/R/\n```\n\nSo all is well, I think.",
    "created_at": "2013-04-17T01:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93920",
    "user": "kcrisman"
}
```

Well, that is a Sage-specific thing, I think, but we have

```
R_HOME="${R_HOME_DIR}"
```

later on and also

```
$ ./sage -R RHOME
/Users/.../Downloads/sage-5.9.beta5/local/lib/R/
```

So all is well, I think.



---

archive/issue_comments_093921.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-17T01:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93921",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093922.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-04-18T10:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9668#issuecomment-93922",
    "user": "jdemeyer"
}
```

Resolution: fixed
