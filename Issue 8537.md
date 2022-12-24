# Issue 8537: Update Open MPI package to latest - Sage version is 3 years old!

archive/issues_008537.json:
```json
{
    "body": "Assignee: tbd\n\nSage has an Open MPI optional package, which uses version 1.1.4 of Open MPI. This was released on Jan 30, 2007, so is more than 3 years old. It fails to build on Solaris - see #8522.\n\nThe optional package is very different to most other Sage packages, which shows its age. \n\n* No SPKG.txt\n* No Mercurial repository\n* Sources sit in top-level directory, not in a 'src' subdirectory. \n\nI'll create a package based on the latest version of Open MPI, which is version 1.4.1, which was released 15th January 2010.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8537\n\n",
    "created_at": "2010-03-14T21:53:51Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "title": "Update Open MPI package to latest - Sage version is 3 years old!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8537",
    "user": "drkirkby"
}
```
Assignee: tbd

Sage has an Open MPI optional package, which uses version 1.1.4 of Open MPI. This was released on Jan 30, 2007, so is more than 3 years old. It fails to build on Solaris - see #8522.

The optional package is very different to most other Sage packages, which shows its age. 

* No SPKG.txt
* No Mercurial repository
* Sources sit in top-level directory, not in a 'src' subdirectory. 

I'll create a package based on the latest version of Open MPI, which is version 1.4.1, which was released 15th January 2010.

Issue created by migration from https://trac.sagemath.org/ticket/8537





---

archive/issue_comments_077165.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-03-14T23:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77165",
    "user": "was"
}
```

Resolution: duplicate



---

archive/issue_comments_077166.json:
```json
{
    "body": "This is a dup of #8455, as a search for \"update mpi\" in trac shows.",
    "created_at": "2010-03-14T23:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77166",
    "user": "was"
}
```

This is a dup of #8455, as a search for "update mpi" in trac shows.



---

archive/issue_comments_077167.json:
```json
{
    "body": "Actually, #8455 is for MPIR and not MPI :-)",
    "created_at": "2010-03-14T23:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77167",
    "user": "mhansen"
}
```

Actually, #8455 is for MPIR and not MPI :-)



---

archive/issue_comments_077168.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-03-14T23:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77168",
    "user": "mhansen"
}
```

Changing status from closed to new.



---

archive/issue_comments_077169.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2010-03-14T23:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77169",
    "user": "mhansen"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_077170.json:
```json
{
    "body": "From wstein:\n\nI think the builds options are relevant to building the optional sage spkg that depends on mpi, namely mpi4py. If somebody updates openmpi, they might make sure mpi4py also works with the new version.",
    "created_at": "2010-03-14T23:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77170",
    "user": "mhansen"
}
```

From wstein:

I think the builds options are relevant to building the optional sage spkg that depends on mpi, namely mpi4py. If somebody updates openmpi, they might make sure mpi4py also works with the new version.



---

archive/issue_comments_077171.json:
```json
{
    "body": "I've created a ticket to update mpi4py - #8538, as that is very old too. I'll try to test the two packages together. \n\nThe old version of openmpi used these configure options:\n\n\n```\n./configure --prefix=\"$SAGE_LOCAL\" --with-f90-max-array-dim=0 --disable-mpi-f77 \n--disable-mpi-f90 --with-mpi-f90-size=trivial\n```\n\n\nI'll look as whether these are all needed, as both openmpi and mpi4py are several years old. \n\nDave",
    "created_at": "2010-03-15T00:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77171",
    "user": "drkirkby"
}
```

I've created a ticket to update mpi4py - #8538, as that is very old too. I'll try to test the two packages together. 

The old version of openmpi used these configure options:


```
./configure --prefix="$SAGE_LOCAL" --with-f90-max-array-dim=0 --disable-mpi-f77 
--disable-mpi-f90 --with-mpi-f90-size=trivial
```


I'll look as whether these are all needed, as both openmpi and mpi4py are several years old. 

Dave



---

archive/issue_comments_077172.json:
```json
{
    "body": "Since I need mpi4py for a seminar and the current version didn't build on our multigpu machine, I had an urge to update openmpi and mpi4py.\n\nThe new package can be found under http://code.google.com/p/spkg-upload/downloads/detail?name=openmpi-1.4.3.spkg\nand is tested on ubuntu 10.04\n\n**Remark:** Before Install one has to remove other installations of openmpi or else get troubles.\nThe current spkg install holds a lot of remove statements a better solution would be great.\nAlso one has to update mpi4py.",
    "created_at": "2011-01-07T00:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77172",
    "user": "maldun"
}
```

Since I need mpi4py for a seminar and the current version didn't build on our multigpu machine, I had an urge to update openmpi and mpi4py.

The new package can be found under http://code.google.com/p/spkg-upload/downloads/detail?name=openmpi-1.4.3.spkg
and is tested on ubuntu 10.04

**Remark:** Before Install one has to remove other installations of openmpi or else get troubles.
The current spkg install holds a lot of remove statements a better solution would be great.
Also one has to update mpi4py.



---

archive/issue_comments_077173.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-01-07T00:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77173",
    "user": "maldun"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_077174.json:
```json
{
    "body": "Attachment [spkg-install](tarball://root/attachments/some-uuid/ticket8537/spkg-install) by maldun created at 2011-01-07 00:18:41\n\ncurrent spkg install",
    "created_at": "2011-01-07T00:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77174",
    "user": "maldun"
}
```

Attachment [spkg-install](tarball://root/attachments/some-uuid/ticket8537/spkg-install) by maldun created at 2011-01-07 00:18:41

current spkg install



---

archive/issue_comments_077175.json:
```json
{
    "body": "Thanks for updating everything!\n\nI think you should be using `rm -f` to delete the old versions. The current `spkg-install` will fail to install if you don't already have the old openmpi lying around.\n\nYou should always use `$MAKE` because somebody might have set `MAKE=/path/gnu-make` or so. Do you need to disable parallel make? Then set `MAKE=\"$MAKE -j 1\"`\n\nDoes mpi4py or anything else need the fortran API? If no, why not disable it in the configure. If yes, is there any way we can make it call `sage_fortran` as the compiler?",
    "created_at": "2011-01-10T17:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77175",
    "user": "vbraun"
}
```

Thanks for updating everything!

I think you should be using `rm -f` to delete the old versions. The current `spkg-install` will fail to install if you don't already have the old openmpi lying around.

You should always use `$MAKE` because somebody might have set `MAKE=/path/gnu-make` or so. Do you need to disable parallel make? Then set `MAKE="$MAKE -j 1"`

Does mpi4py or anything else need the fortran API? If no, why not disable it in the configure. If yes, is there any way we can make it call `sage_fortran` as the compiler?



---

archive/issue_comments_077176.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-01-11T12:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77176",
    "user": "maldun"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_077177.json:
```json
{
    "body": "Replying to [comment:8 vbraun]:\n> Thanks for updating everything!\n> \n> I think you should be using `rm -f` to delete the old versions. The current `spkg-install` will fail to install if you don't already have the old openmpi lying around.\n> \n> You should always use `$MAKE` because somebody might have set `MAKE=/path/gnu-make` or so. Do you need to disable parallel make? Then set `MAKE=\"$MAKE -j 1\"`\n> \n> Does mpi4py or anything else need the fortran API? If no, why not disable it in the configure. If yes, is there any way we can make it call `sage_fortran` as the compiler?\n> \n\nThanks for all the information!\n\nI changed everything to your advices. rm worked without -f but I added it just to be sure.\nAlso found an unnecessary rm statement. The fortran things were already outcommented but I removed them completely, to avoid confusion.\nI upload a the new spkg-install to see the difference",
    "created_at": "2011-01-11T12:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77177",
    "user": "maldun"
}
```

Replying to [comment:8 vbraun]:
> Thanks for updating everything!
> 
> I think you should be using `rm -f` to delete the old versions. The current `spkg-install` will fail to install if you don't already have the old openmpi lying around.
> 
> You should always use `$MAKE` because somebody might have set `MAKE=/path/gnu-make` or so. Do you need to disable parallel make? Then set `MAKE="$MAKE -j 1"`
> 
> Does mpi4py or anything else need the fortran API? If no, why not disable it in the configure. If yes, is there any way we can make it call `sage_fortran` as the compiler?
> 

Thanks for all the information!

I changed everything to your advices. rm worked without -f but I added it just to be sure.
Also found an unnecessary rm statement. The fortran things were already outcommented but I removed them completely, to avoid confusion.
I upload a the new spkg-install to see the difference



---

archive/issue_comments_077178.json:
```json
{
    "body": "new spkg-install for reference",
    "created_at": "2011-01-11T12:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77178",
    "user": "maldun"
}
```

new spkg-install for reference



---

archive/issue_comments_077179.json:
```json
{
    "body": "Attachment [spkg-install.2](tarball://root/attachments/some-uuid/ticket8537/spkg-install.2) by vbraun created at 2011-01-11 21:59:52\n\nNice! Functionality-wise it is all good. But would you mind filling in the `SPKG.txt` according to the template in the developer manual? See\n\nhttp://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt\n\nThat'll give us a place to record future changes etc. You could also add `.*~` to the `.hgignore` so that mercurial doesn't complain about emacs backup files.\n\nBest wishes,\nVolker",
    "created_at": "2011-01-11T21:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77179",
    "user": "vbraun"
}
```

Attachment [spkg-install.2](tarball://root/attachments/some-uuid/ticket8537/spkg-install.2) by vbraun created at 2011-01-11 21:59:52

Nice! Functionality-wise it is all good. But would you mind filling in the `SPKG.txt` according to the template in the developer manual? See

http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt

That'll give us a place to record future changes etc. You could also add `.*~` to the `.hgignore` so that mercurial doesn't complain about emacs backup files.

Best wishes,
Volker



---

archive/issue_comments_077180.json:
```json
{
    "body": "Replying to [comment:10 vbraun]:\n> Nice! Functionality-wise it is all good. But would you mind filling in the `SPKG.txt` according to the template in the developer manual? See\n> \n> http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt\n> \n> That'll give us a place to record future changes etc. You could also add `.*~` to the `.hgignore` so that mercurial doesn't complain about emacs backup files.\n> \n> Best wishes,\n> Volker\n\nOK something went wrong with the SPKG.txt when packing, perhaps I deleted it accidentally or something else went wrong. In addition I can't upload the new version on the spkg-upload site...\n\nYou can download the corrected version now under: http://computational-sage.googlecode.com/files/openmpi-1.4.3.spkg\n\nI hope everything is now correct, and thanks for the hint with the .hgignore!\n\nCheers,\nStefan",
    "created_at": "2011-01-11T23:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77180",
    "user": "maldun"
}
```

Replying to [comment:10 vbraun]:
> Nice! Functionality-wise it is all good. But would you mind filling in the `SPKG.txt` according to the template in the developer manual? See
> 
> http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt
> 
> That'll give us a place to record future changes etc. You could also add `.*~` to the `.hgignore` so that mercurial doesn't complain about emacs backup files.
> 
> Best wishes,
> Volker

OK something went wrong with the SPKG.txt when packing, perhaps I deleted it accidentally or something else went wrong. In addition I can't upload the new version on the spkg-upload site...

You can download the corrected version now under: http://computational-sage.googlecode.com/files/openmpi-1.4.3.spkg

I hope everything is now correct, and thanks for the hint with the .hgignore!

Cheers,
Stefan



---

archive/issue_comments_077181.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-11T23:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77181",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077182.json:
```json
{
    "body": "Looks great!",
    "created_at": "2011-01-11T23:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77182",
    "user": "vbraun"
}
```

Looks great!



---

archive/issue_comments_077183.json:
```json
{
    "body": "I just tested in on Solaris and the export + set variable construct seems to be a bash-ism and not portable to other shells:\n\n```\n$ export MAKE=\"$MAKE -j 1\"\nMAKE= -j 1: is not an identifier\n$ MAKE=\"$MAKE -j 1\"\n$ export MAKE\n```\n\n\nThe best fix is to change the first line of spkg-install to \n\n```/usr/bin/env bash\n```\n\nAlmost all spkgs use that anyways.\n\nI've made that change to the openmpi spkg and put the result here:\n\nhttp://www.stp.dias.ie/~vbraun/Sage/spkg/openmpi-1.4.3.spkg\n\nSince thats a minor change I'll leave it as positive review.\n\nFor the record, compile still fails on Solaris (as with the previous version). This issue is tracked in #8522: Optional package openmpi-1.1.4 fails to install on Solaris 10 SPARC",
    "created_at": "2011-01-12T02:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77183",
    "user": "vbraun"
}
```

I just tested in on Solaris and the export + set variable construct seems to be a bash-ism and not portable to other shells:

```
$ export MAKE="$MAKE -j 1"
MAKE= -j 1: is not an identifier
$ MAKE="$MAKE -j 1"
$ export MAKE
```


The best fix is to change the first line of spkg-install to 

```/usr/bin/env bash
```

Almost all spkgs use that anyways.

I've made that change to the openmpi spkg and put the result here:

http://www.stp.dias.ie/~vbraun/Sage/spkg/openmpi-1.4.3.spkg

Since thats a minor change I'll leave it as positive review.

For the record, compile still fails on Solaris (as with the previous version). This issue is tracked in #8522: Optional package openmpi-1.1.4 fails to install on Solaris 10 SPARC



---

archive/issue_comments_077184.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-02-06T09:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8537#issuecomment-77184",
    "user": "jdemeyer"
}
```

Resolution: fixed
