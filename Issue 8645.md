# Issue 8645: maxima package fails to install ECL library

archive/issues_008645.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @nbruin @williamstein mvngu @qed777 @jdemeyer\n\nKeywords: maxima, ecl\n\nWith the recent ECL update #8275, maxima package doesn't install the ECL library (which was added in #7287). The library is built, but put in an unexpected location. Here is the end of the log:\n\n\n```\n;;; Note: Invoking external command:\n;;;   ranlib /home/burcin/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/libmaxima.a\n;;; Note: Invoking external command:\n;;;   gcc \"-I/home/burcin/sage/sage-4.3.2/local/include/\"  -I/home/burcin/sage/sage-4.3.2/local/include -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64  -O2  -g  -Wall  -fPIC  -Dlinux -O -w -c \"/tmp/ECLINITEsuxJJ.c\" -o \"/tmp/ECLINITEsuxJJ.o\"\n;;; Note: Invoking external command:\n;;;   gcc -o \"/home/burcin/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/maxima.fasb\" -L\"/home/burcin/sage/sage-4.3.2/local/lib/\" \"/tmp/ECLINITEsuxJJ.o\" \"/home/burcin/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/libmaxima.a\"   -shared  -L/home/burcin/sage/sage-4.3.2/local/lib  -L/home/burcin/sage/sage-4.3.2/local/lib  -lecl  -lgmp -lgc -ldl  -lm \ninstalling Maxima library as /home/burcin/sage/sage-4.3.2/local/lib/ecl//maxima.fas\ncp: cannot stat `maxima.fasb': No such file or directory\n\nreal    3m15.250s\nuser    2m34.586s\nsys     0m19.645s\nSuccessfully installed maxima-5.20.1\n```\n\n\nNote that the return value of the cp command is not checked.\n\nThe files are here:\n\n\n```\nburcin@karr ~/sage/sage-4.3.2 $ ls ~/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/\nlibmaxima.a  maxima.fasb  \n```\n\n\nAny ideas why?\n\nIssue created by migration from https://trac.sagemath.org/ticket/8645\n\n",
    "created_at": "2010-04-02T22:58:34Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "maxima package fails to install ECL library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8645",
    "user": "https://github.com/burcin"
}
```
Assignee: @aghitza

CC:  @nbruin @williamstein mvngu @qed777 @jdemeyer

Keywords: maxima, ecl

With the recent ECL update #8275, maxima package doesn't install the ECL library (which was added in #7287). The library is built, but put in an unexpected location. Here is the end of the log:


```
;;; Note: Invoking external command:
;;;   ranlib /home/burcin/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/libmaxima.a
;;; Note: Invoking external command:
;;;   gcc "-I/home/burcin/sage/sage-4.3.2/local/include/"  -I/home/burcin/sage/sage-4.3.2/local/include -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64  -O2  -g  -Wall  -fPIC  -Dlinux -O -w -c "/tmp/ECLINITEsuxJJ.c" -o "/tmp/ECLINITEsuxJJ.o"
;;; Note: Invoking external command:
;;;   gcc -o "/home/burcin/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/maxima.fasb" -L"/home/burcin/sage/sage-4.3.2/local/lib/" "/tmp/ECLINITEsuxJJ.o" "/home/burcin/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/libmaxima.a"   -shared  -L/home/burcin/sage/sage-4.3.2/local/lib  -L/home/burcin/sage/sage-4.3.2/local/lib  -lecl  -lgmp -lgc -ldl  -lm 
installing Maxima library as /home/burcin/sage/sage-4.3.2/local/lib/ecl//maxima.fas
cp: cannot stat `maxima.fasb': No such file or directory

real    3m15.250s
user    2m34.586s
sys     0m19.645s
Successfully installed maxima-5.20.1
```


Note that the return value of the cp command is not checked.

The files are here:


```
burcin@karr ~/sage/sage-4.3.2 $ ls ~/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/
libmaxima.a  maxima.fasb  
```


Any ideas why?

Issue created by migration from https://trac.sagemath.org/ticket/8645





---

archive/issue_comments_078275.json:
```json
{
    "body": "Changing assignee from @aghitza to tbd.",
    "created_at": "2010-04-10T09:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78275",
    "user": "https://github.com/burcin"
}
```

Changing assignee from @aghitza to tbd.



---

archive/issue_comments_078276.json:
```json
{
    "body": "Changing component from algebra to packages.",
    "created_at": "2010-04-10T09:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78276",
    "user": "https://github.com/burcin"
}
```

Changing component from algebra to packages.



---

archive/issue_comments_078277.json:
```json
{
    "body": "I checked and between maxima 5.19 and maxima 5.20 none of the \"lisp\" files have changed in src/src, so it seems very unlikely that the change in location of maxima.fasb is due to the maxima upgrade.\n\nOn the other hand, between ECL 9 and ECL 10, there seems to be a lot of activity in the ASDF module, which is responsible for the building:\n\nhttp://ecls.cvs.sourceforge.net/viewvc/ecls/ecl/src/CHANGELOG?view=markup\n\nso I can easily believe that the cause is here.\n\nIn particular, they are advertising a new option \":move-here\" which allows the destination to be specified. I tried this with the presently packaged ECL 10.2.1 without luck, so perhaps upgrading ECL would be a good idea (and then hope they don't touch ASDF for a while).\n\nOn the plus side: The \"fasb\" file type is always recognised by ECL 10.4.2, so the ugly (and risky?) renaming should not be necessary anymore.\n\nIf after upgrading you still can't manage getting maxima.fasb in a sane location, perhaps drop Juanjo a line.",
    "created_at": "2010-04-13T22:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78277",
    "user": "https://github.com/nbruin"
}
```

I checked and between maxima 5.19 and maxima 5.20 none of the "lisp" files have changed in src/src, so it seems very unlikely that the change in location of maxima.fasb is due to the maxima upgrade.

On the other hand, between ECL 9 and ECL 10, there seems to be a lot of activity in the ASDF module, which is responsible for the building:

http://ecls.cvs.sourceforge.net/viewvc/ecls/ecl/src/CHANGELOG?view=markup

so I can easily believe that the cause is here.

In particular, they are advertising a new option ":move-here" which allows the destination to be specified. I tried this with the presently packaged ECL 10.2.1 without luck, so perhaps upgrading ECL would be a good idea (and then hope they don't touch ASDF for a while).

On the plus side: The "fasb" file type is always recognised by ECL 10.4.2, so the ugly (and risky?) renaming should not be necessary anymore.

If after upgrading you still can't manage getting maxima.fasb in a sane location, perhaps drop Juanjo a line.



---

archive/issue_comments_078278.json:
```json
{
    "body": "This may be of some help. I tried building with ECL 10.4.1. As announced in\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/e094589b2d99be8a/ab26bd29b3a8990a\nwe need a patch (attached there) to Maxima 5.20.1 to let it build.\n\nThe following instruction *should* do the trick\n\n```\n(require 'asdf)\n(load \"maxima-build.lisp\")\n(asdf:make-build :maxima :type :fasl :move-here \".\")\n```\n\nbut for me they lead to an error\n\n```\nCannot rename the file #P\"/home/nbruin/.cache/common-lisp/ecl-10.4.1-linux-x86-64/usr/local/sage/4.3.4/spkg/build/maxima-5.20.1/src/src/maxima.fasb\" to #P\"/usr/local/sage/4.3.4/spkg/build/maxima-5.20.1/src/src/maxima.fasb\".\nExplanation: Invalid cross-device link.\n```\n\nThis error message indicates:\n* that ECL is trying to do exactly the right thing\n* that it's trying to do the move with a hard link, which it shouldn't try. That's a straightforward error, which will probably be fixed in ECL 10.4.2.\n\nSo my guess is that this issue should be fixable quite soon by upgrading.\n\nOh, and the line\n\n```\ncp maxima.fasb $ECLLIB/maxima.fas\n```\n\nshould be changed to\n\n```\ncp maxima.fasb $ECLLIB || echo \"Failed to build maxima.fasb\"; exit 1\n```\n\nso that errors like this get caught next time and because ECL 10.4 supposedly natively recognizes .fasb files.",
    "created_at": "2010-04-14T06:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78278",
    "user": "https://github.com/nbruin"
}
```

This may be of some help. I tried building with ECL 10.4.1. As announced in
http://groups.google.com/group/sage-devel/browse_thread/thread/e094589b2d99be8a/ab26bd29b3a8990a
we need a patch (attached there) to Maxima 5.20.1 to let it build.

The following instruction *should* do the trick

```
(require 'asdf)
(load "maxima-build.lisp")
(asdf:make-build :maxima :type :fasl :move-here ".")
```

but for me they lead to an error

```
Cannot rename the file #P"/home/nbruin/.cache/common-lisp/ecl-10.4.1-linux-x86-64/usr/local/sage/4.3.4/spkg/build/maxima-5.20.1/src/src/maxima.fasb" to #P"/usr/local/sage/4.3.4/spkg/build/maxima-5.20.1/src/src/maxima.fasb".
Explanation: Invalid cross-device link.
```

This error message indicates:
* that ECL is trying to do exactly the right thing
* that it's trying to do the move with a hard link, which it shouldn't try. That's a straightforward error, which will probably be fixed in ECL 10.4.2.

So my guess is that this issue should be fixable quite soon by upgrading.

Oh, and the line

```
cp maxima.fasb $ECLLIB/maxima.fas
```

should be changed to

```
cp maxima.fasb $ECLLIB || echo "Failed to build maxima.fasb"; exit 1
```

so that errors like this get caught next time and because ECL 10.4 supposedly natively recognizes .fasb files.



---

archive/issue_comments_078279.json:
```json
{
    "body": "This should solve the problem:\n\n```\nmkdir ./lisp-cache\n```\n\nthen in lisp:\n\n```\n(require 'asdf)\n(setf asdf::*user-cache* (truename \"./lisp-cache\"))\n(load \"maxima-build.lisp\")\n(asdf:make-build :maxima :type :fasl :move-here \".\")\n```\n\n\n* this directory is guaranteed to be on the same file system\n* the cache is not accidentally on a slower (/home) file system\n* the cache gets wiped when spkg/build/maxima-5.20.1 does.\n* no interference with a possible cache that the user privately might have in ecl\n\nSo, what needs to be done is:\n\n* upgrade to ecl 10.4.1\n* patch Maxima to build with ecl 10.4.1\n* patch maxima's spkg-install with the above changes so that maxima.fasb gets built in the right place.",
    "created_at": "2010-04-14T15:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78279",
    "user": "https://github.com/nbruin"
}
```

This should solve the problem:

```
mkdir ./lisp-cache
```

then in lisp:

```
(require 'asdf)
(setf asdf::*user-cache* (truename "./lisp-cache"))
(load "maxima-build.lisp")
(asdf:make-build :maxima :type :fasl :move-here ".")
```


* this directory is guaranteed to be on the same file system
* the cache is not accidentally on a slower (/home) file system
* the cache gets wiped when spkg/build/maxima-5.20.1 does.
* no interference with a possible cache that the user privately might have in ecl

So, what needs to be done is:

* upgrade to ecl 10.4.1
* patch Maxima to build with ecl 10.4.1
* patch maxima's spkg-install with the above changes so that maxima.fasb gets built in the right place.



---

archive/issue_comments_078280.json:
```json
{
    "body": "patch for ecl-10.4.1.spkg",
    "created_at": "2010-04-15T05:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78280",
    "user": "https://github.com/nbruin"
}
```

patch for ecl-10.4.1.spkg



---

archive/issue_comments_078281.json:
```json
{
    "body": "Attachment [maxima-5.20.1.p1.patch](tarball://root/attachments/some-uuid/ticket8645/maxima-5.20.1.p1.patch) by @nbruin created at 2010-04-15 05:41:53\n\npatch for maxima-5.20.1.p1.spkg",
    "created_at": "2010-04-15T05:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78281",
    "user": "https://github.com/nbruin"
}
```

Attachment [maxima-5.20.1.p1.patch](tarball://root/attachments/some-uuid/ticket8645/maxima-5.20.1.p1.patch) by @nbruin created at 2010-04-15 05:41:53

patch for maxima-5.20.1.p1.spkg



---

archive/issue_comments_078282.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-15T05:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78282",
    "user": "https://github.com/nbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078283.json:
```json
{
    "body": "Updated spkgs up at\n\nhttp://sage.math.washington.edu/home/nbruin/ecl-10.4.1.spkg\n\nhttp://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg\n\nI haven't extensively tested them but at least on sage.math they seem to work and changes are small otherwise. Someone probably wants to test maxima on ecl-10.4.1 extensively (although maxima is part of the regular ecl buildfarm testsuite)\n\nFor reference, I have also attached the patches for the spkgs. *These are already applied to the above spkgs*.",
    "created_at": "2010-04-15T05:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78283",
    "user": "https://github.com/nbruin"
}
```

Updated spkgs up at

http://sage.math.washington.edu/home/nbruin/ecl-10.4.1.spkg

http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg

I haven't extensively tested them but at least on sage.math they seem to work and changes are small otherwise. Someone probably wants to test maxima on ecl-10.4.1 extensively (although maxima is part of the regular ecl buildfarm testsuite)

For reference, I have also attached the patches for the spkgs. *These are already applied to the above spkgs*.



---

archive/issue_comments_078284.json:
```json
{
    "body": "The maxima package at #8731 supersedes the maxima spkg here.",
    "created_at": "2010-04-20T19:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78284",
    "user": "https://github.com/jasongrout"
}
```

The maxima package at #8731 supersedes the maxima spkg here.



---

archive/issue_comments_078285.json:
```json
{
    "body": "Does this ECL package fix #7690?  The ecl update at #8808 claims to fix #7690.",
    "created_at": "2010-05-13T03:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78285",
    "user": "https://github.com/jasongrout"
}
```

Does this ECL package fix #7690?  The ecl update at #8808 claims to fix #7690.



---

archive/issue_comments_078286.json:
```json
{
    "body": "The src/ directory in the ecl spkg on this ticket is not the same as the ECL official sources (this spkg is missing several directories, like \"src/contrib/encodings\" and \"src/msvc\".  So I think #8808's ecl spkg supersedes the ecl spkg on this ticket.\n\nSo with that, I think this ticket should be closed, as the two spkgs listed on it are superseded elsewhere.",
    "created_at": "2010-05-13T04:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78286",
    "user": "https://github.com/jasongrout"
}
```

The src/ directory in the ecl spkg on this ticket is not the same as the ECL official sources (this spkg is missing several directories, like "src/contrib/encodings" and "src/msvc".  So I think #8808's ecl spkg supersedes the ecl spkg on this ticket.

So with that, I think this ticket should be closed, as the two spkgs listed on it are superseded elsewhere.



---

archive/issue_events_008814.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-13T07:28:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8645#event-8814"
}
```



---

archive/issue_comments_078287.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-05-13T07:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78287",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: invalid



---

archive/issue_comments_078288.json:
```json
{
    "body": "My apologies--#8808 was actually in error, and this spkg was correctly made.  I've corrected the mistake on #8951.  So really, this ticket should be closed as fixed, and #8808 should be closed as invalid.",
    "created_at": "2010-05-14T17:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78288",
    "user": "https://github.com/jasongrout"
}
```

My apologies--#8808 was actually in error, and this spkg was correctly made.  I've corrected the mistake on #8951.  So really, this ticket should be closed as fixed, and #8808 should be closed as invalid.



---

archive/issue_comments_078289.json:
```json
{
    "body": "Resolution changed from invalid to fixed",
    "created_at": "2010-05-14T21:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78289",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution changed from invalid to fixed



---

archive/issue_comments_078290.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-06-16T00:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78290",
    "user": "https://github.com/nbruin"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_078291.json:
```json
{
    "body": "This ticket was not merged in 4.4.2, so I'm reopening. The ecl spkg on #8951 supersedes the one here. However, the maxima spkg on #8731 is listed as \"needs work\" so declaring that the spkg there supersedes the one here is a bit premature. The only change in \n\nhttp://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg\n\nis to the way that maxima.fasb get built, copied and its existence tested, so reviewing that should be quick.",
    "created_at": "2010-06-16T00:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78291",
    "user": "https://github.com/nbruin"
}
```

This ticket was not merged in 4.4.2, so I'm reopening. The ecl spkg on #8951 supersedes the one here. However, the maxima spkg on #8731 is listed as "needs work" so declaring that the spkg there supersedes the one here is a bit premature. The only change in 

http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg

is to the way that maxima.fasb get built, copied and its existence tested, so reviewing that should be quick.



---

archive/issue_comments_078292.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-06-16T00:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78292",
    "user": "https://github.com/nbruin"
}
```

Changing status from closed to new.



---

archive/issue_events_008815.json:
```json
{
    "actor": "https://github.com/nbruin",
    "created_at": "2010-06-16T00:43:01Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8645#event-8815"
}
```



---

archive/issue_comments_078293.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-16T00:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78293",
    "user": "https://github.com/nbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078294.json:
```json
{
    "body": "I'm just building sage-4.4.4.alpha1 on Solaris 10 SPARC and will test this as soon as that is finished. What other machines has it been tested on? \n\nI can't spend any more time on this just now - my wife wants me to do something which is going to take a few hours. \n\nI think it is sensible to upgrade the maxima in this way, but there are various small changes to ECL which could (should) be merged into the ecl update. \n\nWould you consider making merging these patches \n\n* On #8951, the patch which removes the tmp files and has a minor (really cosmetic) changes to spkg-install. The removal of the tmp files is quite important, as it often stops builds on 't2'\n* On #8089 the patch to disable assembly code on OpenSolaris\n* On #9187 the patch to allow parallel building of .spkgs. \n\nI think if a new .spkg with ECL 10.4.1 is created, and the Maxima changed to work properly with that, then these should be merged. Then hopefully the maxima update can be separated. \n\nOne of the issues I will have reviewing this is the fact I don't know lisp, but I doubt many people will so I will do my best. \n\nBut just now I need to do other things. \n\nDave",
    "created_at": "2010-06-18T17:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78294",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm just building sage-4.4.4.alpha1 on Solaris 10 SPARC and will test this as soon as that is finished. What other machines has it been tested on? 

I can't spend any more time on this just now - my wife wants me to do something which is going to take a few hours. 

I think it is sensible to upgrade the maxima in this way, but there are various small changes to ECL which could (should) be merged into the ecl update. 

Would you consider making merging these patches 

* On #8951, the patch which removes the tmp files and has a minor (really cosmetic) changes to spkg-install. The removal of the tmp files is quite important, as it often stops builds on 't2'
* On #8089 the patch to disable assembly code on OpenSolaris
* On #9187 the patch to allow parallel building of .spkgs. 

I think if a new .spkg with ECL 10.4.1 is created, and the Maxima changed to work properly with that, then these should be merged. Then hopefully the maxima update can be separated. 

One of the issues I will have reviewing this is the fact I don't know lisp, but I doubt many people will so I will do my best. 

But just now I need to do other things. 

Dave



---

archive/issue_comments_078295.json:
```json
{
    "body": "If #9264 gets merged then this ticked can be closed as resolved.",
    "created_at": "2010-06-21T06:11:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78295",
    "user": "https://github.com/nbruin"
}
```

If #9264 gets merged then this ticked can be closed as resolved.



---

archive/issue_comments_078296.json:
```json
{
    "body": "Replying to [comment:16 nbruin]:\n> If #9264 gets merged then this ticked can be closed as resolved.\n\nAre you sure that is correct? #9264 only makes changes to ECL, not Maxima. So the revised Maxima package at  http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg must still be merged. What does not need merging is the ECL patch attached here, as that is covered by #9264\n\n\nDave",
    "created_at": "2010-06-21T09:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78296",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:16 nbruin]:
> If #9264 gets merged then this ticked can be closed as resolved.

Are you sure that is correct? #9264 only makes changes to ECL, not Maxima. So the revised Maxima package at  http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg must still be merged. What does not need merging is the ECL patch attached here, as that is covered by #9264


Dave



---

archive/issue_comments_078297.json:
```json
{
    "body": "Replying to [comment:17 drkirkby]:\n\n> Are you sure that is correct? #9264 only makes changes to ECL, not Maxima.\n\nExcept for the \"Important\" section and the comment in the positive review. Only upgrading ECL will lead to maxima not building, so no doctests will pass. A successful merge has to include a change to maxima.\n\n(incidentally, on #9264 it would have helped a lot if you had also run \"make test\" or \"make ptest\" after the successful build. One of the issues on #8731 was that it people were unsure whether the doctest failures were due to the ECL upgrade or the maxima upgrade. We now know it's just due to maxima 5.21 behaving differently)",
    "created_at": "2010-06-21T18:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78297",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:17 drkirkby]:

> Are you sure that is correct? #9264 only makes changes to ECL, not Maxima.

Except for the "Important" section and the comment in the positive review. Only upgrading ECL will lead to maxima not building, so no doctests will pass. A successful merge has to include a change to maxima.

(incidentally, on #9264 it would have helped a lot if you had also run "make test" or "make ptest" after the successful build. One of the issues on #8731 was that it people were unsure whether the doctest failures were due to the ECL upgrade or the maxima upgrade. We now know it's just due to maxima 5.21 behaving differently)



---

archive/issue_comments_078298.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-21T20:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78298",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078299.json:
```json
{
    "body": "Replying to [comment:18 nbruin]:\n> Replying to [comment:17 drkirkby]:\n> \n> > Are you sure that is correct? #9264 only makes changes to ECL, not Maxima.\n> \n> Except for the \"Important\" section and the comment in the positive review. Only upgrading ECL will lead to maxima not building, so no doctests will pass. A successful merge has to include a change to maxima.\n\n\nThat was my point - upgrading just ECL would not have worked. \n \n> (incidentally, on #9264 it would have helped a lot if you had also run \"make test\" or \"make ptest\" after the successful build. One of the issues on #8731 was that it people were unsure whether the doctest failures were due to the ECL upgrade or the maxima upgrade. We now know it's just due to maxima 5.21 behaving differently)\n\nOK, point taken. \n\nIt would be good if there was a list of doc tests associated with each package, so its possible to quickly test if changes break any tests. \n\nAnyway, positive review. \n\n == Note to release manager ==\nThis ticket, and #9264 need to be merged together. Merging  #9264 without this one will cause problems. \nDave \n\nDave",
    "created_at": "2010-06-21T20:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78299",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:18 nbruin]:
> Replying to [comment:17 drkirkby]:
> 
> > Are you sure that is correct? #9264 only makes changes to ECL, not Maxima.
> 
> Except for the "Important" section and the comment in the positive review. Only upgrading ECL will lead to maxima not building, so no doctests will pass. A successful merge has to include a change to maxima.


That was my point - upgrading just ECL would not have worked. 
 
> (incidentally, on #9264 it would have helped a lot if you had also run "make test" or "make ptest" after the successful build. One of the issues on #8731 was that it people were unsure whether the doctest failures were due to the ECL upgrade or the maxima upgrade. We now know it's just due to maxima 5.21 behaving differently)

OK, point taken. 

It would be good if there was a list of doc tests associated with each package, so its possible to quickly test if changes break any tests. 

Anyway, positive review. 

 == Note to release manager ==
This ticket, and #9264 need to be merged together. Merging  #9264 without this one will cause problems. 
Dave 

Dave



---

archive/issue_events_008816.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-06-25T15:46:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8645#event-8816"
}
```



---

archive/issue_comments_078300.json:
```json
{
    "body": "Applied http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg",
    "created_at": "2010-06-25T15:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78300",
    "user": "https://github.com/rlmill"
}
```

Applied http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg



---

archive/issue_comments_078301.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78301",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_078302.json:
```json
{
    "body": "Could any of the changes here be related to the problems at #9460?",
    "created_at": "2010-07-09T06:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78302",
    "user": "https://github.com/qed777"
}
```

Could any of the changes here be related to the problems at #9460?



---

archive/issue_comments_078303.json:
```json
{
    "body": "Replying to [comment:21 mpatel]:\n> Could any of the changes here be related to the problems at #9460?\nPossibly, though I don't recall seeing reports of this against sage-4.5.alpha0, which was when this ticket was merged. \n\nDave",
    "created_at": "2010-07-09T08:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78303",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:21 mpatel]:
> Could any of the changes here be related to the problems at #9460?
Possibly, though I don't recall seeing reports of this against sage-4.5.alpha0, which was when this ticket was merged. 

Dave



---

archive/issue_comments_078304.json:
```json
{
    "body": "Replying to [comment:22 drkirkby]:\n> Replying to [comment:21 mpatel]:\n> > Could any of the changes here be related to the problems at #9460?\n> Possibly, though I don't recall seeing reports of this against sage-4.5.alpha0, which was when this ticket was merged. \n\nWilliam, AFAIK, reported those failures on the first alpha in the 4.5 series that he tested. So it is quite possible.",
    "created_at": "2010-07-09T09:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78304",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:22 drkirkby]:
> Replying to [comment:21 mpatel]:
> > Could any of the changes here be related to the problems at #9460?
> Possibly, though I don't recall seeing reports of this against sage-4.5.alpha0, which was when this ticket was merged. 

William, AFAIK, reported those failures on the first alpha in the 4.5 series that he tested. So it is quite possible.



---

archive/issue_comments_078305.json:
```json
{
    "body": "Replying to [comment:23 rlm]:\n> Replying to [comment:22 drkirkby]:\n> > Replying to [comment:21 mpatel]:\n> > > Could any of the changes here be related to the problems at #9460?\n> > Possibly, though I don't recall seeing reports of this against sage-4.5.alpha0, which was when this ticket was merged. \n> \n> William, AFAIK, reported those failures on the first alpha in the 4.5 series that he tested. So it is quite possible.\n\nIn which case reverting this would be sensible, though it we be good if we could if we could find the circumstances in which the problem occurs - there is a note that it may occur only if Sage is built from a script. \n\nDave",
    "created_at": "2010-07-09T09:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78305",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:23 rlm]:
> Replying to [comment:22 drkirkby]:
> > Replying to [comment:21 mpatel]:
> > > Could any of the changes here be related to the problems at #9460?
> > Possibly, though I don't recall seeing reports of this against sage-4.5.alpha0, which was when this ticket was merged. 
> 
> William, AFAIK, reported those failures on the first alpha in the 4.5 series that he tested. So it is quite possible.

In which case reverting this would be sensible, though it we be good if we could if we could find the circumstances in which the problem occurs - there is a note that it may occur only if Sage is built from a script. 

Dave



---

archive/issue_comments_078306.json:
```json
{
    "body": "It seems that there are unchecked in changes in the spkg:\n\n```sh\n$ tar xvf sage-4.5.alpha4/spkg/standard/maxima-5.20.1.p1.spkg\n$ cd maxima-5.20.1.p1\n$ hg stat\n? patches/defsystem.lisp\n? patches/ecl-port.lisp\n```\n",
    "created_at": "2010-07-09T23:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78306",
    "user": "https://github.com/qed777"
}
```

It seems that there are unchecked in changes in the spkg:

```sh
$ tar xvf sage-4.5.alpha4/spkg/standard/maxima-5.20.1.p1.spkg
$ cd maxima-5.20.1.p1
$ hg stat
? patches/defsystem.lisp
? patches/ecl-port.lisp
```




---

archive/issue_comments_078307.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-07-11T19:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78307",
    "user": "https://github.com/rlmill"
}
```

Changing status from closed to new.



---

archive/issue_events_008817.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-11T19:13:57Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8645#event-8817"
}
```



---

archive/issue_comments_078308.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-07-11T19:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78308",
    "user": "https://github.com/rlmill"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_078309.json:
```json
{
    "body": "This is marked as minor, but I've found it causes Maxima to fail to install on bsd.math, so it breaks the build. \n\n\n```\n;;;   gcc -o \"/Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/ECL001STjrNf.fas\" -L\"/Users/kirkby/sage-4.5.alpha1/local/lib/\" \"/Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/ECL001STjrNf.o\"   -bundle  -L/Users/kirkby/sage-4.5.alpha1/local/lib -m64   -L/Users/kirkby/sage-4.5.alpha1/local/lib -m64   -lffi -lecl  -lgmp   -lm \n; loading system definition from\n; /Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/maxima.asd\n; into #<ASDF0 package>\n;;; Loading \"/Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/maxima.asd\"\n; registering #<SYSTEM :MAXIMA 4321128880> as MAXIMA\nAn error occurred during initialization:\nUnknown keyword :MOVE-HERE.\n\ninstalling Maxima library as /Users/kirkby/sage-4.5.alpha1/local/lib/ecl//maxima.fas\ncp: cannot stat `maxima.fasb': No such file or directory\n***********************************************************\nFailed to install maxima.fasb as a library\n***********************************************************\n\nreal\t4m45.305s\nuser\t3m35.767s\nsys\t0m41.909s\nsage: An error occurred while installing maxima-5.20.1.p1\n```\n\n\nThat's not a minor problem to me, if it stops Sage building.",
    "created_at": "2010-09-17T00:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78309",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This is marked as minor, but I've found it causes Maxima to fail to install on bsd.math, so it breaks the build. 


```
;;;   gcc -o "/Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/ECL001STjrNf.fas" -L"/Users/kirkby/sage-4.5.alpha1/local/lib/" "/Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/ECL001STjrNf.o"   -bundle  -L/Users/kirkby/sage-4.5.alpha1/local/lib -m64   -L/Users/kirkby/sage-4.5.alpha1/local/lib -m64   -lffi -lecl  -lgmp   -lm 
; loading system definition from
; /Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/maxima.asd
; into #<ASDF0 package>
;;; Loading "/Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/maxima.asd"
; registering #<SYSTEM :MAXIMA 4321128880> as MAXIMA
An error occurred during initialization:
Unknown keyword :MOVE-HERE.

installing Maxima library as /Users/kirkby/sage-4.5.alpha1/local/lib/ecl//maxima.fas
cp: cannot stat `maxima.fasb': No such file or directory
***********************************************************
Failed to install maxima.fasb as a library
***********************************************************

real	4m45.305s
user	3m35.767s
sys	0m41.909s
sage: An error occurred while installing maxima-5.20.1.p1
```


That's not a minor problem to me, if it stops Sage building.



---

archive/issue_comments_078310.json:
```json
{
    "body": "Replying to [comment:28 drkirkby]:\n\n```\n> Unknown keyword :MOVE-HERE.\n> \n> installing Maxima library as /Users/kirkby/sage-4.5.alpha1/local/lib/ecl//maxima.fas\n> cp: cannot stat `maxima.fasb': No such file or directory\n> ***********************************************************\n> Failed to install maxima.fasb as a library\n> ***********************************************************\n> \n> real\t4m45.305s\n> user\t3m35.767s\n> sys\t0m41.909s\n> sage: An error occurred while installing maxima-5.20.1.p1\n```\n\nThe package maxima-5.20.1.p1 is designed to be built on ecl 10.4.1 or later. In order to use the :MOVE-HERE keyword, I had to upgrade to ecl 10.4.1.\n\nI think sage is still shipping maxima-5.20.1.p0 with ecl 10.2.1, which silently fails to build maxima.fasb. Hence the original filing as \"minor\": a library that by default isn't used silently fails to build.",
    "created_at": "2010-09-18T03:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78310",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:28 drkirkby]:

```
> Unknown keyword :MOVE-HERE.
> 
> installing Maxima library as /Users/kirkby/sage-4.5.alpha1/local/lib/ecl//maxima.fas
> cp: cannot stat `maxima.fasb': No such file or directory
> ***********************************************************
> Failed to install maxima.fasb as a library
> ***********************************************************
> 
> real	4m45.305s
> user	3m35.767s
> sys	0m41.909s
> sage: An error occurred while installing maxima-5.20.1.p1
```

The package maxima-5.20.1.p1 is designed to be built on ecl 10.4.1 or later. In order to use the :MOVE-HERE keyword, I had to upgrade to ecl 10.4.1.

I think sage is still shipping maxima-5.20.1.p0 with ecl 10.2.1, which silently fails to build maxima.fasb. Hence the original filing as "minor": a library that by default isn't used silently fails to build.



---

archive/issue_comments_078311.json:
```json
{
    "body": "Thank you, it seem whenever we need to update we need to \n\n* Update maxima\n* Update ecl\n* Update the doctests\n\nwhich is a bit annoying. It often does not seem possible to update ecl or maxima independently.",
    "created_at": "2010-09-18T12:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78311",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thank you, it seem whenever we need to update we need to 

* Update maxima
* Update ecl
* Update the doctests

which is a bit annoying. It often does not seem possible to update ecl or maxima independently.



---

archive/issue_comments_078312.json:
```json
{
    "body": "I don't think that is true. I think maxima-5.20.1.p0 will build an executable on ecl 10.4.1 and will silently fail to build maxima.fasl, just as it does on ecl 10.2.1. Furthermore, I think maxima-5.20.1 on ecl 10.2.1 produces the same output as on 10.4.1 (given that the only changes between .p0 and .p1 had to do with building a by default unused library)\n\nThe fact that doctests for maxima have to be adjusted is a good thing. A bunch of those detect error conditions that are not errors in newer versions of maxima.\n\nBut in general, you'd expect dependent packages to be - you know - dependent :-).",
    "created_at": "2010-09-20T17:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78312",
    "user": "https://github.com/nbruin"
}
```

I don't think that is true. I think maxima-5.20.1.p0 will build an executable on ecl 10.4.1 and will silently fail to build maxima.fasl, just as it does on ecl 10.2.1. Furthermore, I think maxima-5.20.1 on ecl 10.2.1 produces the same output as on 10.4.1 (given that the only changes between .p0 and .p1 had to do with building a by default unused library)

The fact that doctests for maxima have to be adjusted is a good thing. A bunch of those detect error conditions that are not errors in newer versions of maxima.

But in general, you'd expect dependent packages to be - you know - dependent :-).



---

archive/issue_comments_078313.json:
```json
{
    "body": "Replying to [comment:31 nbruin]:\n> I don't think that is true. I think maxima-5.20.1.p0 will build an executable on ecl 10.4.1\nSorry, I take that back. That must have been before coffee. The point of \".p1\" was to fix library building and detect failure of it, but in the process needed an ecl upgrade (because 10.2.1 was a snapshot of the building system in flux), which required further patches to maxima (announced and supplied by Juanjo -- Maxima is part of the ECL test suite, so he knows when Maxima/ECL breaks)",
    "created_at": "2010-09-21T17:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78313",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:31 nbruin]:
> I don't think that is true. I think maxima-5.20.1.p0 will build an executable on ecl 10.4.1
Sorry, I take that back. That must have been before coffee. The point of ".p1" was to fix library building and detect failure of it, but in the process needed an ecl upgrade (because 10.2.1 was a snapshot of the building system in flux), which required further patches to maxima (announced and supplied by Juanjo -- Maxima is part of the ECL test suite, so he knows when Maxima/ECL breaks)



---

archive/issue_comments_078314.json:
```json
{
    "body": "Replying to [comment:31 nbruin]:\n> But in general, you'd expect dependent packages to be - you know - dependent :-).\n\nYes, but the current Sage build (and upgrade) process doesn't really reflect this... ;-)\n\n(We use `make`, but `sage-spkg` usually just reports a dependent package was already installed; our current scheme lacks version requirements almost completely.)\n\nFor the *rebuild dependent packages on upgrade* issue, there's #9896 (needs review; not limited to MacOS X). :)",
    "created_at": "2010-09-24T12:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78314",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:31 nbruin]:
> But in general, you'd expect dependent packages to be - you know - dependent :-).

Yes, but the current Sage build (and upgrade) process doesn't really reflect this... ;-)

(We use `make`, but `sage-spkg` usually just reports a dependent package was already installed; our current scheme lacks version requirements almost completely.)

For the *rebuild dependent packages on upgrade* issue, there's #9896 (needs review; not limited to MacOS X). :)



---

archive/issue_comments_078315.json:
```json
{
    "body": "#9538 might depend on that ticket.\n\nPaul",
    "created_at": "2010-09-27T09:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78315",
    "user": "https://github.com/zimmermann6"
}
```

#9538 might depend on that ticket.

Paul



---

archive/issue_comments_078316.json:
```json
{
    "body": "#10187 should fix this.",
    "created_at": "2010-11-18T16:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78316",
    "user": "https://github.com/kcrisman"
}
```

#10187 should fix this.



---

archive/issue_comments_078317.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-19T21:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78317",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078318.json:
```json
{
    "body": "To release manager: #10187 was closed quite a while ago, and there it is confirmed that this should close this.  Thanks!",
    "created_at": "2011-01-19T21:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78318",
    "user": "https://github.com/kcrisman"
}
```

To release manager: #10187 was closed quite a while ago, and there it is confirmed that this should close this.  Thanks!



---

archive/issue_comments_078319.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-01-19T22:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8645#issuecomment-78319",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_008818.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-19T22:11:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8645",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8645#event-8818"
}
```
