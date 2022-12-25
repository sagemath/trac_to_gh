# Issue 7071: palp-1.1.p1 ignores CC variable and uses gcc, so fails with Sun Studio.

archive/issues_007071.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @orlitzky\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha4\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used #7021\n\nThis is one of the many packages that ignore the setting of the variable CC. \n\n```\npalp-1.1.p1/src/GNUmakefile\npalp-1.1.p1/src/mori.c\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nmake[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/palp-1.1.p1/src'\ngcc -O3 -g -W -Wall -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE   -c -o poly.o poly.c\ngcc -O3 -g -W -Wall -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE   -c -o Coord.o Coord.c\ngcc -O3 -g -W -Wall -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE   -c -o Rat.o Rat.c\ngcc -O3 -g -W -Wall -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE   -c -o Vertex.o Vertex.c\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7071\n\n",
    "created_at": "2009-09-29T13:27:04Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "palp-1.1.p1 ignores CC variable and uses gcc, so fails with Sun Studio.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7071",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @orlitzky

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha4
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used #7021

This is one of the many packages that ignore the setting of the variable CC. 

```
palp-1.1.p1/src/GNUmakefile
palp-1.1.p1/src/mori.c
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/palp-1.1.p1/src'
gcc -O3 -g -W -Wall -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE   -c -o poly.o poly.c
gcc -O3 -g -W -Wall -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE   -c -o Coord.o Coord.c
gcc -O3 -g -W -Wall -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE   -c -o Rat.o Rat.c
gcc -O3 -g -W -Wall -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE   -c -o Vertex.o Vertex.c

```


Issue created by migration from https://trac.sagemath.org/ticket/7071





---

archive/issue_comments_058371.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-02-09T14:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58371",
    "user": "https://github.com/ohanar"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058372.json:
```json
{
    "body": "Attachment [palp-1.1.p4.patch](tarball://root/attachments/some-uuid/ticket7071/palp-1.1.p4.patch) by @ohanar created at 2012-02-09 14:46:10\n\nfor review purposes",
    "created_at": "2012-02-09T14:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58372",
    "user": "https://github.com/ohanar"
}
```

Attachment [palp-1.1.p4.patch](tarball://root/attachments/some-uuid/ticket7071/palp-1.1.p4.patch) by @ohanar created at 2012-02-09 14:46:10

for review purposes



---

archive/issue_comments_058373.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-02-25T23:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58373",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_058374.json:
```json
{
    "body": "Can we pass CFLAGS, too? That will allow us to get rid of that horrible `sed`. Might as well fix the \"xyes\" test also",
    "created_at": "2012-02-25T23:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58374",
    "user": "https://github.com/orlitzky"
}
```

Can we pass CFLAGS, too? That will allow us to get rid of that horrible `sed`. Might as well fix the "xyes" test also



---

archive/issue_comments_058375.json:
```json
{
    "body": "Palp 2 is out and I have a preliminary spkg at #12055. Please base your work on the new version.",
    "created_at": "2012-02-26T19:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58375",
    "user": "https://github.com/vbraun"
}
```

Palp 2 is out and I have a preliminary spkg at #12055. Please base your work on the new version.



---

archive/issue_comments_058376.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-27T00:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58376",
    "user": "https://github.com/ohanar"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_058377.json:
```json
{
    "body": "ok, I've based my changes off of the new version at #12055 and have made `CFLAGS` respected as well.",
    "created_at": "2012-02-27T00:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58377",
    "user": "https://github.com/ohanar"
}
```

ok, I've based my changes off of the new version at #12055 and have made `CFLAGS` respected as well.



---

archive/issue_comments_058378.json:
```json
{
    "body": "Attachment [palp-2.0.p1.patch](tarball://root/attachments/some-uuid/ticket7071/palp-2.0.p1.patch) by @ohanar created at 2012-02-27 00:35:26\n\nfor review purposes",
    "created_at": "2012-02-27T00:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58378",
    "user": "https://github.com/ohanar"
}
```

Attachment [palp-2.0.p1.patch](tarball://root/attachments/some-uuid/ticket7071/palp-2.0.p1.patch) by @ohanar created at 2012-02-27 00:35:26

for review purposes



---

archive/issue_comments_058379.json:
```json
{
    "body": "Looks good!",
    "created_at": "2012-02-27T01:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58379",
    "user": "https://github.com/vbraun"
}
```

Looks good!



---

archive/issue_comments_058380.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-27T01:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58380",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058381.json:
```json
{
    "body": "Patch from #12055 needs to be applied",
    "created_at": "2012-02-27T01:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58381",
    "user": "https://github.com/vbraun"
}
```

Patch from #12055 needs to be applied



---

archive/issue_comments_058382.json:
```json
{
    "body": "Attachment [trac-12055-SAGELOCAL_BIN.patch](tarball://root/attachments/some-uuid/ticket7071/trac-12055-SAGELOCAL_BIN.patch) by @vbraun created at 2012-02-27 01:09:59\n\nI've switched the old ticket #12055 to invalid to not make Jeroen replace the spkg twice. But we still need the patch to the Sage library from there.",
    "created_at": "2012-02-27T01:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58382",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac-12055-SAGELOCAL_BIN.patch](tarball://root/attachments/some-uuid/ticket7071/trac-12055-SAGELOCAL_BIN.patch) by @vbraun created at 2012-02-27 01:09:59

I've switched the old ticket #12055 to invalid to not make Jeroen replace the spkg twice. But we still need the patch to the Sage library from there.



---

archive/issue_comments_058383.json:
```json
{
    "body": "Replying to [comment:2 mjo]:\n> Can we pass CFLAGS, too? That will allow us to get rid of that horrible `sed`. Might as well fix the \"xyes\" test also\n\nThe \"xyes\" test, as it is called above, is the safest, most portable way to test for a string, as other methods, like the proposed change, can fail under obscure conditions. One might argue they don't fail with modern versions of bash, but IMHO is it worthwhile to write scripts which will always work under all conditions. The original code will always work - the proposed change is less portable. I suggest you take a look at the scripts created by autoconf. You will find they use a similar method to what was in Sage, as it is known to always work. \n\nAs such, I believe the change is a retrograde step. \n\nDave",
    "created_at": "2012-02-28T22:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58383",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:2 mjo]:
> Can we pass CFLAGS, too? That will allow us to get rid of that horrible `sed`. Might as well fix the "xyes" test also

The "xyes" test, as it is called above, is the safest, most portable way to test for a string, as other methods, like the proposed change, can fail under obscure conditions. One might argue they don't fail with modern versions of bash, but IMHO is it worthwhile to write scripts which will always work under all conditions. The original code will always work - the proposed change is less portable. I suggest you take a look at the scripts created by autoconf. You will find they use a similar method to what was in Sage, as it is known to always work. 

As such, I believe the change is a retrograde step. 

Dave



---

archive/issue_comments_058384.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-02-28T22:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58384",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_058385.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-03-02T22:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58385",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_058386.json:
```json
{
    "body": "I disagree. The xblah test makes it more difficult to read the test, which both increases the chance for errors as well as the long-term maintenance effort. \n\nA quick survey shows that at least half of the Sage spkgs use the simplified test, so clearly nobody has yet encountered a shell ancient enough to not work. I'm pretty sure many upstream sources use simplified tests, too, so there is basically no hope of ever compiling Sage on such a system without installing a shell that isn't from the middle ages. Autotools output really is a totally different issue, since their scripts are autogenerated readability is not an issue (and usually is pretty bad, in fact).\n\nIf you disagree we can discuss this on the sage-devel, but its such a pervasive issue throughout Sage that it doesn't really matter if we use the simplified test in one spkg more or less.",
    "created_at": "2012-03-02T22:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58386",
    "user": "https://github.com/vbraun"
}
```

I disagree. The xblah test makes it more difficult to read the test, which both increases the chance for errors as well as the long-term maintenance effort. 

A quick survey shows that at least half of the Sage spkgs use the simplified test, so clearly nobody has yet encountered a shell ancient enough to not work. I'm pretty sure many upstream sources use simplified tests, too, so there is basically no hope of ever compiling Sage on such a system without installing a shell that isn't from the middle ages. Autotools output really is a totally different issue, since their scripts are autogenerated readability is not an issue (and usually is pretty bad, in fact).

If you disagree we can discuss this on the sage-devel, but its such a pervasive issue throughout Sage that it doesn't really matter if we use the simplified test in one spkg more or less.



---

archive/issue_events_007293.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-03-04T21:19:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7071#event-7293"
}
```



---

archive/issue_comments_058387.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-04T21:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7071#issuecomment-58387",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
