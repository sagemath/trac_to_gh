# Issue 8906: Optional package for gap3

archive/issues_008906.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  burcin andrew.mathas\n\nKeywords: gap3\n\nHere is an spkg wich contains a patched version of gap3 that compiles on linux/x86 and macosx/x86.\n\n[http://thales.math.uqam.ca/~robado/gap3-0.3.spkg](http://thales.math.uqam.ca/~robado/gap3-0.3.spkg)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8906\n\n",
    "created_at": "2010-05-06T14:07:54Z",
    "labels": [
        "packages: optional",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.9",
    "title": "Optional package for gap3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8906",
    "user": "mrobado"
}
```
Assignee: tbd

CC:  burcin andrew.mathas

Keywords: gap3

Here is an spkg wich contains a patched version of gap3 that compiles on linux/x86 and macosx/x86.

[http://thales.math.uqam.ca/~robado/gap3-0.3.spkg](http://thales.math.uqam.ca/~robado/gap3-0.3.spkg)

Issue created by migration from https://trac.sagemath.org/ticket/8906





---

archive/issue_comments_081984.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-06T16:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81984",
    "user": "burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_081985.json:
```json
{
    "body": "Thanks a lot for the package, and a good example of how to write `spkg-install` in Python.\n\nHere are a few comments:\n* Version numbers for the GAP4 package are of the form gap-4.4.10.p17, so we should name this gap.3.4.4.p0 and keep increasing the \"patch level\" at the end for updates.\n* The package has a single mercurial repository at the top, which contains spkg-install, SPKG.txt, etc. and the GAP3 source files. The convention is to keep two separate repositories, one with only \"packaging\" material, spkg-install and so on, another one to track changes to the upstream sources.\n* Does GAP3 have a test suite? Can we add an spkg-check which runs this? Another option is to copy the spkg-check which just tries to start GAP from the spkg mentioned in comment:9:ticket:8380.\n* SPKG.txt should be based on the template here: http://wiki.sagemath.org/spkgTemplate\n  In particular:\n  * the changelog should have an entry conforming to the standard\n  * TODO list (in the file TODO) should be moved in the SPKG.txt\n  * There should be an explanation of what changes were made to the upstream sources, even though they are already documented in the mercurial repository log.\n  * SPKG.txt should note that src/bin/gap.sh hardcodes version `gap3r4p4` in the `GAP_DIR` variable\n* I don't see why these lines at the end of `spkg-install` are necessary:\n {{{\n if not os.path.exists(gap3_base):\n     os.makedirs(gap3_base)\n }}}",
    "created_at": "2010-05-06T16:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81985",
    "user": "burcin"
}
```

Thanks a lot for the package, and a good example of how to write `spkg-install` in Python.

Here are a few comments:
* Version numbers for the GAP4 package are of the form gap-4.4.10.p17, so we should name this gap.3.4.4.p0 and keep increasing the "patch level" at the end for updates.
* The package has a single mercurial repository at the top, which contains spkg-install, SPKG.txt, etc. and the GAP3 source files. The convention is to keep two separate repositories, one with only "packaging" material, spkg-install and so on, another one to track changes to the upstream sources.
* Does GAP3 have a test suite? Can we add an spkg-check which runs this? Another option is to copy the spkg-check which just tries to start GAP from the spkg mentioned in comment:9:ticket:8380.
* SPKG.txt should be based on the template here: http://wiki.sagemath.org/spkgTemplate
  In particular:
  * the changelog should have an entry conforming to the standard
  * TODO list (in the file TODO) should be moved in the SPKG.txt
  * There should be an explanation of what changes were made to the upstream sources, even though they are already documented in the mercurial repository log.
  * SPKG.txt should note that src/bin/gap.sh hardcodes version `gap3r4p4` in the `GAP_DIR` variable
* I don't see why these lines at the end of `spkg-install` are necessary:
 {{{
 if not os.path.exists(gap3_base):
     os.makedirs(gap3_base)
 }}}



---

archive/issue_comments_081986.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-06T21:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81986",
    "user": "mrobado"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081987.json:
```json
{
    "body": "I uploaded a new version of the package with the issues fixed at this address [http://thales.math.uqam.ca/~robado/gap-3.4.4.p0.spkg](http://thales.math.uqam.ca/~robado/gap-3.4.4.p0.spkg) . Maybe we should merge this package with the one posted on #8380.",
    "created_at": "2010-05-06T21:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81987",
    "user": "mrobado"
}
```

I uploaded a new version of the package with the issues fixed at this address [http://thales.math.uqam.ca/~robado/gap-3.4.4.p0.spkg](http://thales.math.uqam.ca/~robado/gap-3.4.4.p0.spkg) . Maybe we should merge this package with the one posted on #8380.



---

archive/issue_comments_081988.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-06T21:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81988",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081989.json:
```json
{
    "body": "I don't know what the exact requirements for an optional package are. Especially the difference between an optional and an experimental package is not clear to me. I can't find them anywhere in the documentation either.\n\nThe package at http://thales.math.uqam.ca/~robado/gap-3.4.4.p0.spkg looks good to me, switching to positive review. :)",
    "created_at": "2010-05-06T21:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81989",
    "user": "burcin"
}
```

I don't know what the exact requirements for an optional package are. Especially the difference between an optional and an experimental package is not clear to me. I can't find them anywhere in the documentation either.

The package at http://thales.math.uqam.ca/~robado/gap-3.4.4.p0.spkg looks good to me, switching to positive review. :)



---

archive/issue_comments_081990.json:
```json
{
    "body": "Some problems with gap-3.4.4.p0.spkg:\n\n1. All changes have not been checked in:\n {{{#!sh\n[mvngu`@`sage gap-3.4.4.p0]$ hg status\nM SPKG.txt\n? spkg-check\n }}}\n You must check in all changes.\n1. The license file `COPYING` needs to go under the directory `src/`.\n2. The directory `src/` contains one package within another:\n {{{#!sh\n[mvngu`@`sage src]$ pwd\n/home/mvngu/spkg/optional/gap/gap-3.4.4.p0/src\n[mvngu`@`sage src]$ ls\nbin            description12  description4  description8  grp  sml  tom\ndescription1   description13  description5  description9  htm  src  tst\ndescription10  description2   description6  doc           lib  tbl  two\ndescription11  description3   description7  etc           pkg  thr  utl\n[mvngu`@`sage src]$ ls src\nagcollec.c     description12  function.c     pcpresen.c  record.h    tietze.h\nagcollec.h     description13  function.h     pcpresen.h  scanner.c   tom\naggroup.c      description2   gap.c          permutat.c  scanner.h   tst\naggroup.h      description3   gasman.c       permutat.h  set.c       two\nbin            description4   gasman.h       pkg         set.h       unknown.c\nblister.c      description5   grp            plist.c     sml         unknown.h\nblister.h      description6   htm            plist.h     src         utl\ncoding.c       description7   idents.c       polynom.c   statemen.c  vecffe.c\ncoding.h       description8   idents.h       polynom.h   statemen.h  vecffe.h\ncostab.c       description9   integer.c      range.c     string.c    vector.c\ncostab.h       doc            integer.h      range.h     string.h    vector.h\ncyclotom.c     etc            lib            rational.c  system.c    word.c\ncyclotom.h     eval.c         list.c         rational.h  system.h    word.h\ndescription1   eval.h         list.h         read.c      tbl\ndescription10  finfield.c     Makefile       read.h      thr\ndescription11  finfield.h     Makefile.orig  record.c    tietze.c\n }}}\n1. You don't have any patches on top of the upstream GAP 3 package, so you need to start the spkg numbering at `gap-3.4.4.spkg`, not at `gap-3.4.4.p0.spkg`. The name `gap-3.4.4.p0.spkg` implies that you have a patch to be applied on top of the upstream GAP 3 package. See this chapter [Producing New Sage Packages](http://www.sagemath.org/doc/developer/producing_spkgs.html) and chapter [Patching a Sage Package](http://www.sagemath.org/doc/developer/patching_spkgs.html) of the Developer's Guide.",
    "created_at": "2010-05-08T22:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81990",
    "user": "mvngu"
}
```

Some problems with gap-3.4.4.p0.spkg:

1. All changes have not been checked in:
 {{{#!sh
[mvngu`@`sage gap-3.4.4.p0]$ hg status
M SPKG.txt
? spkg-check
 }}}
 You must check in all changes.
1. The license file `COPYING` needs to go under the directory `src/`.
2. The directory `src/` contains one package within another:
 {{{#!sh
[mvngu`@`sage src]$ pwd
/home/mvngu/spkg/optional/gap/gap-3.4.4.p0/src
[mvngu`@`sage src]$ ls
bin            description12  description4  description8  grp  sml  tom
description1   description13  description5  description9  htm  src  tst
description10  description2   description6  doc           lib  tbl  two
description11  description3   description7  etc           pkg  thr  utl
[mvngu`@`sage src]$ ls src
agcollec.c     description12  function.c     pcpresen.c  record.h    tietze.h
agcollec.h     description13  function.h     pcpresen.h  scanner.c   tom
aggroup.c      description2   gap.c          permutat.c  scanner.h   tst
aggroup.h      description3   gasman.c       permutat.h  set.c       two
bin            description4   gasman.h       pkg         set.h       unknown.c
blister.c      description5   grp            plist.c     sml         unknown.h
blister.h      description6   htm            plist.h     src         utl
coding.c       description7   idents.c       polynom.c   statemen.c  vecffe.c
coding.h       description8   idents.h       polynom.h   statemen.h  vecffe.h
costab.c       description9   integer.c      range.c     string.c    vector.c
costab.h       doc            integer.h      range.h     string.h    vector.h
cyclotom.c     etc            lib            rational.c  system.c    word.c
cyclotom.h     eval.c         list.c         rational.h  system.h    word.h
description1   eval.h         list.h         read.c      tbl
description10  finfield.c     Makefile       read.h      thr
description11  finfield.h     Makefile.orig  record.c    tietze.c
 }}}
1. You don't have any patches on top of the upstream GAP 3 package, so you need to start the spkg numbering at `gap-3.4.4.spkg`, not at `gap-3.4.4.p0.spkg`. The name `gap-3.4.4.p0.spkg` implies that you have a patch to be applied on top of the upstream GAP 3 package. See this chapter [Producing New Sage Packages](http://www.sagemath.org/doc/developer/producing_spkgs.html) and chapter [Patching a Sage Package](http://www.sagemath.org/doc/developer/patching_spkgs.html) of the Developer's Guide.



---

archive/issue_comments_081991.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-05-08T22:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81991",
    "user": "mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081992.json:
```json
{
    "body": "Hi Minh,\n\nReplying to [comment:4 mvngu]:\n> Some problems with gap-3.4.4.p0.spkg:\n> \n>  1. All changes have not been checked in:\n>  {{{\n> #!sh\n> [mvngu`@`sage gap-3.4.4.p0]$ hg status\n> M SPKG.txt\n> ? spkg-check\n>  }}}\n>  You must check in all changes.\n>  1. The license file `COPYING` needs to go under the directory `src/`.\n\nFair enough, I didn't check these again myself. Note that the COPYING file doesn't exist in the original gap3 distribution. We decided to make one after it took us a while to discover the license has a non-commercial use restriction.\n\n>  1. The directory `src/` contains one package within another:\n\nThis is just how the gap3 source is laid out. There are gap library files, and gap packages in the other directories. I don't see why this is a problem.\n\n>  1. You don't have any patches on top of the upstream GAP 3 package, so you need to start the spkg numbering at `gap-3.4.4.spkg`, not at `gap-3.4.4.p0.spkg`. The name `gap-3.4.4.p0.spkg` implies that you have a patch to be applied on top of the upstream GAP 3 package.\n\nWhat is in the spkg is very far from the original gap3 distribution. The changes couldn't be tracked with patches, so there is a mercurial repository in the src directory. Marco did a tremendous job creating a GAP package which actually compiles and works on different platforms, and includes the latest versions of various GAP packages still being maintained.\n\n\nI agree with your points 1 and 2, but IMHO 3 and 4 are not problems that need to be addressed before this is accepted.\n\nThanks. \n\nBurcin",
    "created_at": "2010-05-08T23:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81992",
    "user": "burcin"
}
```

Hi Minh,

Replying to [comment:4 mvngu]:
> Some problems with gap-3.4.4.p0.spkg:
> 
>  1. All changes have not been checked in:
>  {{{
> #!sh
> [mvngu`@`sage gap-3.4.4.p0]$ hg status
> M SPKG.txt
> ? spkg-check
>  }}}
>  You must check in all changes.
>  1. The license file `COPYING` needs to go under the directory `src/`.

Fair enough, I didn't check these again myself. Note that the COPYING file doesn't exist in the original gap3 distribution. We decided to make one after it took us a while to discover the license has a non-commercial use restriction.

>  1. The directory `src/` contains one package within another:

This is just how the gap3 source is laid out. There are gap library files, and gap packages in the other directories. I don't see why this is a problem.

>  1. You don't have any patches on top of the upstream GAP 3 package, so you need to start the spkg numbering at `gap-3.4.4.spkg`, not at `gap-3.4.4.p0.spkg`. The name `gap-3.4.4.p0.spkg` implies that you have a patch to be applied on top of the upstream GAP 3 package.

What is in the spkg is very far from the original gap3 distribution. The changes couldn't be tracked with patches, so there is a mercurial repository in the src directory. Marco did a tremendous job creating a GAP package which actually compiles and works on different platforms, and includes the latest versions of various GAP packages still being maintained.


I agree with your points 1 and 2, but IMHO 3 and 4 are not problems that need to be addressed before this is accepted.

Thanks. 

Burcin



---

archive/issue_comments_081993.json:
```json
{
    "body": "Replying to [comment:5 burcin]:\n> Note that the COPYING file doesn't exist in the original gap3 distribution. We decided to make one after it took us a while to discover the license has a non-commercial use restriction.\n\nCould you document that in the file `SPKG.txt`? Future reviewers/maintainers might not know about this.\n\n\n\n\n> >  1. The directory `src/` contains one package within another:\n> \n> This is just how the gap3 source is laid out. There are gap library files, and gap packages in the other directories. I don't see why this is a problem.\n\nCould you document that in the file `SPKG.txt`? Future reviewers/maintainers might not know about this.\n\n\n\n\n\n> What is in the spkg is very far from the original gap3 distribution. The changes couldn't be tracked with patches, so there is a mercurial repository in the src directory. \n\nCould you document that in the file `SPKG.txt`? Future reviewers/maintainers might not know about this.\n\n\n\nAs you can tell, I raised the above objections because the file `SPKG.txt` did not document the reasons why the spkg was structured as given.",
    "created_at": "2010-05-08T23:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81993",
    "user": "mvngu"
}
```

Replying to [comment:5 burcin]:
> Note that the COPYING file doesn't exist in the original gap3 distribution. We decided to make one after it took us a while to discover the license has a non-commercial use restriction.

Could you document that in the file `SPKG.txt`? Future reviewers/maintainers might not know about this.




> >  1. The directory `src/` contains one package within another:
> 
> This is just how the gap3 source is laid out. There are gap library files, and gap packages in the other directories. I don't see why this is a problem.

Could you document that in the file `SPKG.txt`? Future reviewers/maintainers might not know about this.





> What is in the spkg is very far from the original gap3 distribution. The changes couldn't be tracked with patches, so there is a mercurial repository in the src directory. 

Could you document that in the file `SPKG.txt`? Future reviewers/maintainers might not know about this.



As you can tell, I raised the above objections because the file `SPKG.txt` did not document the reasons why the spkg was structured as given.



---

archive/issue_comments_081994.json:
```json
{
    "body": "Hi!\n\nThanks Marco for your work!\n\nWith Jean-Michel, we have merged Marco's changes into our original spkg (with the changes to the sources upstreamed in Jean's distribution). We will upload the result shortly here.\n\nAbout the spkg name. Since the gap3 spkg is completely different from the gap4 one, and is supposed to cohabit with it, I would argue for calling the spkg gap3-???? to make a clear distinction. It is further based on Jean's gap3 distribution. So, would you recommend:\ncalling it `gap3-jm2.spkg` or `gap3-3.4.4-jm2.spkg` ?\n\nJean would prefer the first option, since anyway gap3's version has not changed since 1997, and won't ever change again.",
    "created_at": "2010-06-17T21:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81994",
    "user": "nthiery"
}
```

Hi!

Thanks Marco for your work!

With Jean-Michel, we have merged Marco's changes into our original spkg (with the changes to the sources upstreamed in Jean's distribution). We will upload the result shortly here.

About the spkg name. Since the gap3 spkg is completely different from the gap4 one, and is supposed to cohabit with it, I would argue for calling the spkg gap3-???? to make a clear distinction. It is further based on Jean's gap3 distribution. So, would you recommend:
calling it `gap3-jm2.spkg` or `gap3-3.4.4-jm2.spkg` ?

Jean would prefer the first option, since anyway gap3's version has not changed since 1997, and won't ever change again.



---

archive/issue_comments_081995.json:
```json
{
    "body": "Hi!\n\nI just obtained the following with gap3 on winxp1 (win XP + cygwin host in the Sage build farm):\n\n\n```\ngap> W := CoxeterGroup(\"E\",8);\nCoxeterGroup(\"E\",8)\ngap> Size(W);                \n696729600\n```\n\n\nFor the record: I did not have Sage installed, so I did not try directly the spkg. Instead, I built and ran it by hand, using something like:\n\n\n```\ntar xvf gap3-jm2.spkg\ncd gap3-jm2/src/src\nmake ibm-i386-linux-gcc\ncd ..\ncp src/gap.exe bin\n<EDIT bin/gap.sh>\nbin/gap.sh\n```\n\n\nIn bin/gap.sh, I set GAP_PRG=gap.exe, and downgraded GAP_MEM=512m to GAP_MEM=64m (otherwise I was getting an error Gasman: can not get memory for the initial workspace).\n\nSo I assume that it should be easy to adapt the spkg to also work on windows+cygwin once sage will be more publicly available there (windows 7 still to be tested).",
    "created_at": "2010-06-22T21:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81995",
    "user": "nthiery"
}
```

Hi!

I just obtained the following with gap3 on winxp1 (win XP + cygwin host in the Sage build farm):


```
gap> W := CoxeterGroup("E",8);
CoxeterGroup("E",8)
gap> Size(W);                
696729600
```


For the record: I did not have Sage installed, so I did not try directly the spkg. Instead, I built and ran it by hand, using something like:


```
tar xvf gap3-jm2.spkg
cd gap3-jm2/src/src
make ibm-i386-linux-gcc
cd ..
cp src/gap.exe bin
<EDIT bin/gap.sh>
bin/gap.sh
```


In bin/gap.sh, I set GAP_PRG=gap.exe, and downgraded GAP_MEM=512m to GAP_MEM=64m (otherwise I was getting an error Gasman: can not get memory for the initial workspace).

So I assume that it should be easy to adapt the spkg to also work on windows+cygwin once sage will be more publicly available there (windows 7 still to be tested).



---

archive/issue_comments_081996.json:
```json
{
    "body": "What is the status of this spkg? I've used this with several versions of sage with Ubuntu and MacOSX (pre-Lion), and I have had no problems. I would be great if this appeared in the optional spkg list.\n\n[Aside: the trac preview claims I deleted the dependencies, but I did not.]",
    "created_at": "2011-08-24T17:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81996",
    "user": "saliola"
}
```

What is the status of this spkg? I've used this with several versions of sage with Ubuntu and MacOSX (pre-Lion), and I have had no problems. I would be great if this appeared in the optional spkg list.

[Aside: the trac preview claims I deleted the dependencies, but I did not.]



---

archive/issue_comments_081997.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-08-24T17:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81997",
    "user": "saliola"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_081998.json:
```json
{
    "body": "Is anyone still working on this spkg?  I'm interested in being able to use CHEVIE from Sage....",
    "created_at": "2015-05-14T02:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81998",
    "user": "roed"
}
```

Is anyone still working on this spkg?  I'm interested in being able to use CHEVIE from Sage....



---

archive/issue_comments_081999.json:
```json
{
    "body": "It would be great to make this an official package!\n\nI tried the spkg quickly on two machines and it didn't work on either:\n\n- I tried `sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg` on Mac OSX and got an error\n\n```\nimac: sage --version\nSage Version 6.2, Release Date: 2014-05-06\n\nimac: sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg\nAttempting to download package gap3-jm2\n>>> Trying to download http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg\n[............................................................]\ngap3-jm2\n====================================================\nExtracting package /Users/saliola/Applications/sage/upstream/gap3-jm2.spkg\n-rw-r--r--  1 saliola  staff  12234482 May 14 21:16 /Users/saliola/Applications/sage/upstream/gap3-jm2.spkg\nFinished extraction\n****************************************************\nHost system:\nDarwin imac.local 14.3.0 Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64 x86_64\n****************************************************\nC compiler: gcc\nC compiler version:\nUsing built-in specs.\nCOLLECT_GCC=/Users/saliola/Applications/sage/local/bin/gcc\nCOLLECT_LTO_WRAPPER=/Users/saliola/Applications/sage/local/libexec/gcc/x86_64-apple-darwin12.5.0/4.7.3/lto-wrapper\nTarget: x86_64-apple-darwin12.5.0\nConfigured with: ../src/configure --prefix=/Users/saliola/Applications/sage/local --with-local-prefix=/Users/saliola/Applications/sage/local --with-gmp=/Users/saliola/Applications/sage/local --with-mpfr=/Users/saliola/Applications/sage/local --with-mpc=/Users/saliola/Applications/sage/local --with-system-zlib --disable-multilib --disable-nls  \nThread model: posix\ngcc version 4.7.3 (GCC) \n****************************************************\ndyld: Symbol not found: _sqlite3_intarray_bind\n  Referenced from: /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData\n  Expected in: /Users/saliola/Applications/sage/local/lib/libsqlite3.dylib\n in /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData\nmake: error: unable to locate xcodebuild, please make sure the path to the Xcode folder is set correctly!\nmake: error: You can set the path to the Xcode folder using /usr/bin/xcode-select -switch\nCompiling target macosx-gcc-686-optimized\n18176\nError compiling Gap3\n```\n\n\n- I tried `sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg` with on Ubuntu 14.04 and got an error\n\n```\nT7600: sage --version\nExecuting: /home/saliola/Applications/sage/sage\nSageMath Version 6.7.beta2, Release Date: 2015-04-21\n\nT7600: sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg\nExecuting: /home/saliola/Applications/sage/sage\nAttempting to download package gap3-jm2\n>>> Trying to download http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg\n[............................................................]\ngap3-jm2\n====================================================\nExtracting package /home/saliola/Applications/sage/upstream/gap3-jm2.spkg\n-rw-rw-r-- 1 saliola saliola 12234482 May 14 21:14 /home/saliola/Applications/sage/upstream/gap3-jm2.spkg\nFinished extraction\n****************************************************\nHost system:\nLinux T7600 3.13.0-45-generic #74-Ubuntu SMP Tue Jan 13 19:36:28 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux\n****************************************************\nC compiler: gcc\nC compiler version:\nUsing built-in specs.\nCOLLECT_GCC=/usr/bin/gcc\nCOLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/4.8/lto-wrapper\nTarget: x86_64-linux-gnu\nConfigured with: ../src/configure -v --with-pkgversion='Ubuntu 4.8.2-19ubuntu1' --with-bugurl=file:///usr/share/doc/gcc-4.8/README.Bugs --enable-languages=c,c++,java,go,d,fortran,objc,obj-c++ --prefix=/usr --program-suffix=-4.8 --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.8 --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --enable-gnu-unique-object --disable-libmudflap --enable-plugin --with-system-zlib --disable-browser-plugin --enable-java-awt=gtk --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-4.8-amd64/jre --enable-java-home --with-jvm-root-dir=/usr/lib/jvm/java-1.5.0-gcj-4.8-amd64 --with-jvm-jar-dir=/usr/lib/jvm-exports/java-1.5.0-gcj-4.8-amd64 --with-arch-directory=amd64 --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --enable-objc-gc --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu\nThread model: posix\ngcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) \n****************************************************\nmake[1]: Entering directory `/home/saliola/Applications/sage/local/var/tmp/sage/build/gap3-jm2/src/src'\ngcc -m32 -O3 -fomit-frame-pointer -pipe -fno-strength-reduce -march=i686 -DCPU=686 -g -O2 -DSYS_IS_USG -DSYS_HAS_TIME_PROTO -DSYS_HAS_SIGNAL_PROTO -DSYS_HAS_IOCTL_PROTO   -c -o system.o system.c\nIn file included from /usr/include/features.h:398:0,\n                 from /usr/include/ctype.h:25,\n                 from system.h:241,\n                 from system.c:157:\n/usr/include/x86_64-linux-gnu/gnu/stubs.h:7:27: fatal error: gnu/stubs-32.h: No such file or directory\n # include <gnu/stubs-32.h>\n                           ^\ncompilation terminated.\nmake[1]: *** [system.o] Error 1\nmake[1]: Leaving directory `/home/saliola/Applications/sage/local/var/tmp/sage/build/gap3-jm2/src/src'\nmake: *** [ibm-i386-linux-gcc-optimized] Error 2\nCompiling target ibm-i386-linux-gcc-optimized\n512\nError compiling Gap3\n\n```\n",
    "created_at": "2015-05-15T01:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-81999",
    "user": "saliola"
}
```

It would be great to make this an official package!

I tried the spkg quickly on two machines and it didn't work on either:

- I tried `sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg` on Mac OSX and got an error

```
imac: sage --version
Sage Version 6.2, Release Date: 2014-05-06

imac: sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg
Attempting to download package gap3-jm2
>>> Trying to download http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg
[............................................................]
gap3-jm2
====================================================
Extracting package /Users/saliola/Applications/sage/upstream/gap3-jm2.spkg
-rw-r--r--  1 saliola  staff  12234482 May 14 21:16 /Users/saliola/Applications/sage/upstream/gap3-jm2.spkg
Finished extraction
****************************************************
Host system:
Darwin imac.local 14.3.0 Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64 x86_64
****************************************************
C compiler: gcc
C compiler version:
Using built-in specs.
COLLECT_GCC=/Users/saliola/Applications/sage/local/bin/gcc
COLLECT_LTO_WRAPPER=/Users/saliola/Applications/sage/local/libexec/gcc/x86_64-apple-darwin12.5.0/4.7.3/lto-wrapper
Target: x86_64-apple-darwin12.5.0
Configured with: ../src/configure --prefix=/Users/saliola/Applications/sage/local --with-local-prefix=/Users/saliola/Applications/sage/local --with-gmp=/Users/saliola/Applications/sage/local --with-mpfr=/Users/saliola/Applications/sage/local --with-mpc=/Users/saliola/Applications/sage/local --with-system-zlib --disable-multilib --disable-nls  
Thread model: posix
gcc version 4.7.3 (GCC) 
****************************************************
dyld: Symbol not found: _sqlite3_intarray_bind
  Referenced from: /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
  Expected in: /Users/saliola/Applications/sage/local/lib/libsqlite3.dylib
 in /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
make: error: unable to locate xcodebuild, please make sure the path to the Xcode folder is set correctly!
make: error: You can set the path to the Xcode folder using /usr/bin/xcode-select -switch
Compiling target macosx-gcc-686-optimized
18176
Error compiling Gap3
```


- I tried `sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg` with on Ubuntu 14.04 and got an error

```
T7600: sage --version
Executing: /home/saliola/Applications/sage/sage
SageMath Version 6.7.beta2, Release Date: 2015-04-21

T7600: sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg
Executing: /home/saliola/Applications/sage/sage
Attempting to download package gap3-jm2
>>> Trying to download http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg
[............................................................]
gap3-jm2
====================================================
Extracting package /home/saliola/Applications/sage/upstream/gap3-jm2.spkg
-rw-rw-r-- 1 saliola saliola 12234482 May 14 21:14 /home/saliola/Applications/sage/upstream/gap3-jm2.spkg
Finished extraction
****************************************************
Host system:
Linux T7600 3.13.0-45-generic #74-Ubuntu SMP Tue Jan 13 19:36:28 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
****************************************************
C compiler: gcc
C compiler version:
Using built-in specs.
COLLECT_GCC=/usr/bin/gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/4.8/lto-wrapper
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 4.8.2-19ubuntu1' --with-bugurl=file:///usr/share/doc/gcc-4.8/README.Bugs --enable-languages=c,c++,java,go,d,fortran,objc,obj-c++ --prefix=/usr --program-suffix=-4.8 --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.8 --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --enable-gnu-unique-object --disable-libmudflap --enable-plugin --with-system-zlib --disable-browser-plugin --enable-java-awt=gtk --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-4.8-amd64/jre --enable-java-home --with-jvm-root-dir=/usr/lib/jvm/java-1.5.0-gcj-4.8-amd64 --with-jvm-jar-dir=/usr/lib/jvm-exports/java-1.5.0-gcj-4.8-amd64 --with-arch-directory=amd64 --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --enable-objc-gc --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) 
****************************************************
make[1]: Entering directory `/home/saliola/Applications/sage/local/var/tmp/sage/build/gap3-jm2/src/src'
gcc -m32 -O3 -fomit-frame-pointer -pipe -fno-strength-reduce -march=i686 -DCPU=686 -g -O2 -DSYS_IS_USG -DSYS_HAS_TIME_PROTO -DSYS_HAS_SIGNAL_PROTO -DSYS_HAS_IOCTL_PROTO   -c -o system.o system.c
In file included from /usr/include/features.h:398:0,
                 from /usr/include/ctype.h:25,
                 from system.h:241,
                 from system.c:157:
/usr/include/x86_64-linux-gnu/gnu/stubs.h:7:27: fatal error: gnu/stubs-32.h: No such file or directory
 # include <gnu/stubs-32.h>
                           ^
compilation terminated.
make[1]: *** [system.o] Error 1
make[1]: Leaving directory `/home/saliola/Applications/sage/local/var/tmp/sage/build/gap3-jm2/src/src'
make: *** [ibm-i386-linux-gcc-optimized] Error 2
Compiling target ibm-i386-linux-gcc-optimized
512
Error compiling Gap3

```




---

archive/issue_comments_082000.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2015-05-15T01:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82000",
    "user": "saliola"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_082001.json:
```json
{
    "body": "It may very well be that the problems with the above are related to unmet system-wide dependencies / configurations, but we should figure them out and update the installation instructions appropriately since I can compile Sage on these systems.",
    "created_at": "2015-05-15T01:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82001",
    "user": "saliola"
}
```

It may very well be that the problems with the above are related to unmet system-wide dependencies / configurations, but we should figure them out and update the installation instructions appropriately since I can compile Sage on these systems.



---

archive/issue_comments_082002.json:
```json
{
    "body": "Replying to [comment:15 roed]:\n> Is anyone still working on this spkg?  I'm interested in being able to use CHEVIE from Sage....\n\nTo get yourself up and running quickly without waiting for this spkg to be finalized, just install GAP3 system-wide using one of the following options and you should be good to go.\n\n- http://www.math.rwth-aachen.de/~Frank.Luebeck/gap/GAP3\n\n- http://people.math.jussieu.fr/~jmichel/chevie/chevie.html",
    "created_at": "2015-05-15T01:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82002",
    "user": "saliola"
}
```

Replying to [comment:15 roed]:
> Is anyone still working on this spkg?  I'm interested in being able to use CHEVIE from Sage....

To get yourself up and running quickly without waiting for this spkg to be finalized, just install GAP3 system-wide using one of the following options and you should be good to go.

- http://www.math.rwth-aachen.de/~Frank.Luebeck/gap/GAP3

- http://people.math.jussieu.fr/~jmichel/chevie/chevie.html



---

archive/issue_comments_082003.json:
```json
{
    "body": "Franco and Nicolas, do you plan to make the aim of this ticket happen? It would be great to have for #11187 which I would like to have finished soon.\n\nThanks, Christian",
    "created_at": "2015-06-18T19:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82003",
    "user": "stumpc5"
}
```

Franco and Nicolas, do you plan to make the aim of this ticket happen? It would be great to have for #11187 which I would like to have finished soon.

Thanks, Christian



---

archive/issue_comments_082004.json:
```json
{
    "body": "Nicolas, what do you think? Should we package this? If so, which version (Luebeck's or Michel's)?\n\nAlso, what would be required to maintain this over time? Test it with every stable release of Sage? It would be good to have a plan going forward on maintaining this package.",
    "created_at": "2015-06-18T19:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82004",
    "user": "saliola"
}
```

Nicolas, what do you think? Should we package this? If so, which version (Luebeck's or Michel's)?

Also, what would be required to maintain this over time? Test it with every stable release of Sage? It would be good to have a plan going forward on maintaining this package.



---

archive/issue_comments_082005.json:
```json
{
    "body": "I'd vote for Jean Michel's last version since I regularly send him bug reports in the `chevie` code (found through the code now in #11187, and usually in dark corners of complex reflection group computations) and which he then very quickly fixes and provides on his webside.",
    "created_at": "2015-06-18T19:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82005",
    "user": "stumpc5"
}
```

I'd vote for Jean Michel's last version since I regularly send him bug reports in the `chevie` code (found through the code now in #11187, and usually in dark corners of complex reflection group computations) and which he then very quickly fixes and provides on his webside.



---

archive/issue_comments_082006.json:
```json
{
    "body": "I agree it would be good to have. Alas I don't have the manpower to work on this.\n\nI would go for Jean Michel's version indeed. I believe the main stopgap is to make this compile reasonably robustly. The compilation error in comment:16 on Ubuntu is a missing dependency: since gap3 is 32bit it needs to be compiled with the 32bits C library headers. See\ne.g. http://www.cyberciti.biz/tips/compile-32bit-application-using-gcc-64-bit-linux.html for details.",
    "created_at": "2015-06-20T12:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82006",
    "user": "nthiery"
}
```

I agree it would be good to have. Alas I don't have the manpower to work on this.

I would go for Jean Michel's version indeed. I believe the main stopgap is to make this compile reasonably robustly. The compilation error in comment:16 on Ubuntu is a missing dependency: since gap3 is 32bit it needs to be compiled with the 32bits C library headers. See
e.g. http://www.cyberciti.biz/tips/compile-32bit-application-using-gcc-64-bit-linux.html for details.



---

archive/issue_comments_082007.json:
```json
{
    "body": "I could try doing it, but I'd be glad if you were taking that over, Franco... Christian",
    "created_at": "2015-06-20T16:17:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82007",
    "user": "stumpc5"
}
```

I could try doing it, but I'd be glad if you were taking that over, Franco... Christian



---

archive/issue_comments_082008.json:
```json
{
    "body": "From what I gather from [Frank Leubeck's site](http://www.math.rwth-aachen.de/~Frank.Luebeck/gap/GAP3/index.html):\n* Frank Leubeck's package includes some optimizations and is statically linked;\n* Jean Michel's version has a newer version of CHEVIE;\n* Andrew Mathas provided a Makefile target to compile GAP3 on Mac OSX machines.\n\nI guess these should all be combined at some point?\n\nI'm adding Andrew Mathas to the CC list. Andrew, what is your opinion on this?",
    "created_at": "2015-06-23T01:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82008",
    "user": "saliola"
}
```

From what I gather from [Frank Leubeck's site](http://www.math.rwth-aachen.de/~Frank.Luebeck/gap/GAP3/index.html):
* Frank Leubeck's package includes some optimizations and is statically linked;
* Jean Michel's version has a newer version of CHEVIE;
* Andrew Mathas provided a Makefile target to compile GAP3 on Mac OSX machines.

I guess these should all be combined at some point?

I'm adding Andrew Mathas to the CC list. Andrew, what is your opinion on this?



---

archive/issue_comments_082009.json:
```json
{
    "body": "So Franco -- are we going to do something here?",
    "created_at": "2015-07-20T12:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82009",
    "user": "stumpc5"
}
```

So Franco -- are we going to do something here?



---

archive/issue_comments_082010.json:
```json
{
    "body": "OK, so besides the fact that I don't know what I am doing, I think this is ready for review.\n\nHere is what you have to do to test this.\n\n1. Checkout this branch: use your favourite method; for instance, with git-trac,\n\n```\ngit trac checkout 8906\n```\n\n\n2. Download the upstream tarball http://webusers.imj-prg.fr/~jean.michel/gap3/gap3-jm5.tar.gz and copy it into `SAGE_ROOT/upstream`; or just run the following commands:\n\n```\ncd $(sage --root)/upstream\ncurl -O http://webusers.imj-prg.fr/~jean.michel/gap3/gap3-jm5.tar.gz\n```\n\n\n3. Install the spkg:\n\n```\nsage -i gap3\n```\n\n\n**Question:** where do I put the upstream tarball so that people don't have to do step 2?\n\n----\nNew commits:",
    "created_at": "2015-07-25T03:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82010",
    "user": "saliola"
}
```

OK, so besides the fact that I don't know what I am doing, I think this is ready for review.

Here is what you have to do to test this.

1. Checkout this branch: use your favourite method; for instance, with git-trac,

```
git trac checkout 8906
```


2. Download the upstream tarball http://webusers.imj-prg.fr/~jean.michel/gap3/gap3-jm5.tar.gz and copy it into `SAGE_ROOT/upstream`; or just run the following commands:

```
cd $(sage --root)/upstream
curl -O http://webusers.imj-prg.fr/~jean.michel/gap3/gap3-jm5.tar.gz
```


3. Install the spkg:

```
sage -i gap3
```


**Question:** where do I put the upstream tarball so that people don't have to do step 2?

----
New commits:



---

archive/issue_comments_082011.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-07-25T03:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82011",
    "user": "saliola"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082012.json:
```json
{
    "body": "So is that tarball the official release and the one you want mirrored once this ticket is merged? If so, then please add it to the ticket description. The release manager will add it to the tarball mirror list so a user will only have to do `sage -i gap3` once this is merged.",
    "created_at": "2015-07-25T15:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82012",
    "user": "tscrim"
}
```

So is that tarball the official release and the one you want mirrored once this ticket is merged? If so, then please add it to the ticket description. The release manager will add it to the tarball mirror list so a user will only have to do `sage -i gap3` once this is merged.



---

archive/issue_comments_082013.json:
```json
{
    "body": "I am certainly not the right one to do a review since I don't know either whether everything is correct here. Nevertheless, it seems to work like a charm, thanks for preparing it!\n\nDo you know why the first call of `gap3` doesn't appear to work properly?\n\n\n```\n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502 SageMath Version 6.8.rc1, Release Date: 2015-07-22                 \u2502\n\u2502 Type \"notebook()\" for the browser-based notebook interface.        \u2502\n\u2502 Type \"help()\" for help.                                            \u2502\n\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n\u250f\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\n\u2503 Warning: this is a prerelease version, and it may be unstable.     \u2503\n\u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u251b\nsage: gap3\nGap3\nsage: gap3.execute(\"1+1\")\n''\nsage: gap3.execute(\"1+1\")\n'2'\nsage: \n```\n",
    "created_at": "2015-07-26T22:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82013",
    "user": "stumpc5"
}
```

I am certainly not the right one to do a review since I don't know either whether everything is correct here. Nevertheless, it seems to work like a charm, thanks for preparing it!

Do you know why the first call of `gap3` doesn't appear to work properly?


```
┌────────────────────────────────────────────────────────────────────┐
│ SageMath Version 6.8.rc1, Release Date: 2015-07-22                 │
│ Type "notebook()" for the browser-based notebook interface.        │
│ Type "help()" for help.                                            │
└────────────────────────────────────────────────────────────────────┘
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Warning: this is a prerelease version, and it may be unstable.     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
sage: gap3
Gap3
sage: gap3.execute("1+1")
''
sage: gap3.execute("1+1")
'2'
sage: 
```




---

archive/issue_comments_082014.json:
```json
{
    "body": "As this is confusing the only running patchbot, I temporarily put this into 'needs_info'",
    "created_at": "2015-07-30T12:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82014",
    "user": "chapoton"
}
```

As this is confusing the only running patchbot, I temporarily put this into 'needs_info'



---

archive/issue_comments_082015.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2015-07-30T12:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82015",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_082016.json:
```json
{
    "body": "Replying to [comment:29 stumpc5]:\n> I am certainly not the right one to do a review since I don't know either whether everything is correct here. Nevertheless, it seems to work like a charm, thanks for preparing it!\n> \n> Do you know why the first call of `gap3` doesn't appear to work properly?\n> \n> {{{\n> \u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n> \u2502 [SageMath](SageMath) Version 6.8.rc1, Release Date: 2015-07-22                 \u2502\n> \u2502 Type \"notebook()\" for the browser-based notebook interface.        \u2502\n> \u2502 Type \"help()\" for help.                                            \u2502\n> \u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n> \u250f\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\n> \u2503 Warning: this is a prerelease version, and it may be unstable.     \u2503\n> \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u251b\n> sage: gap3\n> Gap3\n> sage: gap3.execute(\"1+1\")\n> ''\n> sage: gap3.execute(\"1+1\")\n> '2'\n> sage: \n> }}}\n\nThis is not an issue with the proposed SPKG. In fact, it is a problem even with the first proposed SPKG from Marco Robado.\n\nSo this should be a separate ticket.\n\nEdit: I created a ticket: #18971.",
    "created_at": "2015-07-30T22:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82016",
    "user": "saliola"
}
```

Replying to [comment:29 stumpc5]:
> I am certainly not the right one to do a review since I don't know either whether everything is correct here. Nevertheless, it seems to work like a charm, thanks for preparing it!
> 
> Do you know why the first call of `gap3` doesn't appear to work properly?
> 
> {{{
> ┌────────────────────────────────────────────────────────────────────┐
> │ [SageMath](SageMath) Version 6.8.rc1, Release Date: 2015-07-22                 │
> │ Type "notebook()" for the browser-based notebook interface.        │
> │ Type "help()" for help.                                            │
> └────────────────────────────────────────────────────────────────────┘
> ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
> ┃ Warning: this is a prerelease version, and it may be unstable.     ┃
> ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
> sage: gap3
> Gap3
> sage: gap3.execute("1+1")
> ''
> sage: gap3.execute("1+1")
> '2'
> sage: 
> }}}

This is not an issue with the proposed SPKG. In fact, it is a problem even with the first proposed SPKG from Marco Robado.

So this should be a separate ticket.

Edit: I created a ticket: #18971.



---

archive/issue_comments_082017.json:
```json
{
    "body": "Replying to [comment:30 chapoton]:\n> As this is confusing the only running patchbot, I temporarily put this into 'needs_info'\n\nOK, but this still \"needs review\". :-)",
    "created_at": "2015-07-30T22:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82017",
    "user": "saliola"
}
```

Replying to [comment:30 chapoton]:
> As this is confusing the only running patchbot, I temporarily put this into 'needs_info'

OK, but this still "needs review". :-)



---

archive/issue_comments_082018.json:
```json
{
    "body": "Replying to [comment:28 tscrim]:\n> So is that tarball the official release and the one you want mirrored once this ticket is merged? If so, then please add it to the ticket description. The release manager will add it to the tarball mirror list so a user will only have to do `sage -i gap3` once this is merged.\n\nThanks, Travis. I'll modify the description.",
    "created_at": "2015-07-30T22:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82018",
    "user": "saliola"
}
```

Replying to [comment:28 tscrim]:
> So is that tarball the official release and the one you want mirrored once this ticket is merged? If so, then please add it to the ticket description. The release manager will add it to the tarball mirror list so a user will only have to do `sage -i gap3` once this is merged.

Thanks, Travis. I'll modify the description.



---

archive/issue_comments_082019.json:
```json
{
    "body": "> Replying to [comment:28 tscrim]: Thanks, Travis. I'll modify the description.\n\nHi there -- is anything missing here (except a positive review) in order to get this merged? tscrim, would you be able to do the review if necessary? Thanks, Christian",
    "created_at": "2015-08-24T09:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82019",
    "user": "stumpc5"
}
```

> Replying to [comment:28 tscrim]: Thanks, Travis. I'll modify the description.

Hi there -- is anything missing here (except a positive review) in order to get this merged? tscrim, would you be able to do the review if necessary? Thanks, Christian



---

archive/issue_comments_082020.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2015-08-31T15:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82020",
    "user": "chapoton"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_082021.json:
```json
{
    "body": "please someone put this into positive review",
    "created_at": "2015-08-31T15:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82021",
    "user": "chapoton"
}
```

please someone put this into positive review



---

archive/issue_comments_082022.json:
```json
{
    "body": "It seems to work as it is supposed to. Also, the files and their content are as described to be at http://doc.sagemath.org/html/en/developer/packaging.html#directory-structure.\n\nI think it is ready to go!",
    "created_at": "2015-09-01T19:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82022",
    "user": "stumpc5"
}
```

It seems to work as it is supposed to. Also, the files and their content are as described to be at http://doc.sagemath.org/html/en/developer/packaging.html#directory-structure.

I think it is ready to go!



---

archive/issue_comments_082023.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-09-01T19:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82023",
    "user": "stumpc5"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082024.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-09-02T17:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82024",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_082025.json:
```json
{
    "body": "there is a lot of crud left in bin/ subdir.",
    "created_at": "2015-09-08T18:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82025",
    "user": "dimpase"
}
```

there is a lot of crud left in bin/ subdir.



---

archive/issue_comments_082026.json:
```json
{
    "body": "this is scary. This package distributes executables. IMHO it should have never been accepted this way.",
    "created_at": "2015-09-08T18:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82026",
    "user": "dimpase"
}
```

this is scary. This package distributes executables. IMHO it should have never been accepted this way.



---

archive/issue_comments_082027.json:
```json
{
    "body": "Having said that, I can also point out that some packages included only contain executables for x86_64, while they are advertised to be included regardless of the platform.",
    "created_at": "2015-09-08T18:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82027",
    "user": "dimpase"
}
```

Having said that, I can also point out that some packages included only contain executables for x86_64, while they are advertised to be included regardless of the platform.



---

archive/issue_comments_082028.json:
```json
{
    "body": "(this was reverted in #19164)",
    "created_at": "2015-09-09T21:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82028",
    "user": "ncohen"
}
```

(this was reverted in #19164)



---

archive/issue_comments_082029.json:
```json
{
    "body": "Replying to [comment:31 saliola]:\n> Replying to [comment:29 stumpc5]:\n> > I am certainly not the right one to do a review since I don't know either whether everything is correct here. Nevertheless, it seems to work like a charm, thanks for preparing it!\n> > \n> > Do you know why the first call of `gap3` doesn't appear to work properly?\n> > \n> > {{{\n> > \u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n> > \u2502 [SageMath](SageMath) Version 6.8.rc1, Release Date: 2015-07-22                 \u2502\n> > \u2502 Type \"notebook()\" for the browser-based notebook interface.        \u2502\n> > \u2502 Type \"help()\" for help.                                            \u2502\n> > \u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n> > \u250f\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\n> > \u2503 Warning: this is a prerelease version, and it may be unstable.     \u2503\n> > \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u251b\n> > sage: gap3\n> > Gap3\n> > sage: gap3.execute(\"1+1\")\n> > ''\n> > sage: gap3.execute(\"1+1\")\n> > '2'\n> > sage: \n> > }}}\n> \n> This is not an issue with the proposed SPKG. In fact, it is a problem even with the first proposed SPKG from Marco Robado.\n> \n> So this should be a separate ticket.\n> \n> Edit: I created a ticket: #18971.\n\nFixed in #23142.",
    "created_at": "2017-06-06T21:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8906#issuecomment-82029",
    "user": "nthiery"
}
```

Replying to [comment:31 saliola]:
> Replying to [comment:29 stumpc5]:
> > I am certainly not the right one to do a review since I don't know either whether everything is correct here. Nevertheless, it seems to work like a charm, thanks for preparing it!
> > 
> > Do you know why the first call of `gap3` doesn't appear to work properly?
> > 
> > {{{
> > ┌────────────────────────────────────────────────────────────────────┐
> > │ [SageMath](SageMath) Version 6.8.rc1, Release Date: 2015-07-22                 │
> > │ Type "notebook()" for the browser-based notebook interface.        │
> > │ Type "help()" for help.                                            │
> > └────────────────────────────────────────────────────────────────────┘
> > ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
> > ┃ Warning: this is a prerelease version, and it may be unstable.     ┃
> > ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
> > sage: gap3
> > Gap3
> > sage: gap3.execute("1+1")
> > ''
> > sage: gap3.execute("1+1")
> > '2'
> > sage: 
> > }}}
> 
> This is not an issue with the proposed SPKG. In fact, it is a problem even with the first proposed SPKG from Marco Robado.
> 
> So this should be a separate ticket.
> 
> Edit: I created a ticket: #18971.

Fixed in #23142.
