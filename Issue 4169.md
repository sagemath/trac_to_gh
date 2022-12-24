# Issue 4169: [with spkg and patch, needs review] zn_poly 0.9 and hypellfrob 2.1.1

archive/issues_004169.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  tabbott\n\nUpdate to `zn_poly` version 0.9.\n\nAlso included is a minor patch for hypellfrob (this is necessary since hypellfrob was using `zn_poly` internals in a naughty way --- bad design on my part, and now fixed).\n\nYou need to install the spkg first, then apply the hypellfrob patch and force a rebuild (touch {{{devel/sage/sage/schemes/hyperelliptic_curves/hypellfrob.pyx if necessary).\n\nIssue created by migration from https://trac.sagemath.org/ticket/4169\n\n",
    "created_at": "2008-09-22T19:02:41Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with spkg and patch, needs review] zn_poly 0.9 and hypellfrob 2.1.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4169",
    "user": "dmharvey"
}
```
Assignee: mabshoff

CC:  tabbott

Update to `zn_poly` version 0.9.

Also included is a minor patch for hypellfrob (this is necessary since hypellfrob was using `zn_poly` internals in a naughty way --- bad design on my part, and now fixed).

You need to install the spkg first, then apply the hypellfrob patch and force a rebuild (touch {{{devel/sage/sage/schemes/hyperelliptic_curves/hypellfrob.pyx if necessary).

Issue created by migration from https://trac.sagemath.org/ticket/4169





---

archive/issue_comments_030258.json:
```json
{
    "body": "Attachment [hypellfrob-2.1.1.patch](tarball://root/attachments/some-uuid/ticket4169/hypellfrob-2.1.1.patch) by dmharvey created at 2008-09-22 19:04:06",
    "created_at": "2008-09-22T19:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4169#issuecomment-30258",
    "user": "dmharvey"
}
```

Attachment [hypellfrob-2.1.1.patch](tarball://root/attachments/some-uuid/ticket4169/hypellfrob-2.1.1.patch) by dmharvey created at 2008-09-22 19:04:06



---

archive/issue_comments_030259.json:
```json
{
    "body": "Hi David, I can review this ticket. One somehow related question: Would it make sense to use znpoly for `GF(p)['x']` and `IntegersModRing(n)['x']` ?",
    "created_at": "2008-09-22T19:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4169#issuecomment-30259",
    "user": "malb"
}
```

Hi David, I can review this ticket. One somehow related question: Would it make sense to use znpoly for `GF(p)['x']` and `IntegersModRing(n)['x']` ?



---

archive/issue_comments_030260.json:
```json
{
    "body": "Thanks malb.\n\nProbably not a good idea to use it as the backend yet. I'm working on it, and that's my eventual goal, but whereas multiplication and middle product are pretty good, division support is still poor.",
    "created_at": "2008-09-22T21:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4169#issuecomment-30260",
    "user": "dmharvey"
}
```

Thanks malb.

Probably not a good idea to use it as the backend yet. I'm working on it, and that's my eventual goal, but whereas multiplication and middle product are pretty good, division support is still poor.



---

archive/issue_comments_030261.json:
```json
{
    "body": "Hi David,\n\ndid you valgrind this or will I have to do it? :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-22T23:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4169#issuecomment-30261",
    "user": "mabshoff"
}
```

Hi David,

did you valgrind this or will I have to do it? :)

Cheers,

Michael



---

archive/issue_comments_030262.json:
```json
{
    "body": "I valgrinded (valground?) \"make check\" on sage.math, but not the full \"test all\" and not from within sage. There was a single leak of 2500 bytes, which is in GMP's mpn_random2 function, which is not used outside the test suite.",
    "created_at": "2008-09-22T23:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4169#issuecomment-30262",
    "user": "dmharvey"
}
```

I valgrinded (valground?) "make check" on sage.math, but not the full "test all" and not from within sage. There was a single leak of 2500 bytes, which is in GMP's mpn_random2 function, which is not used outside the test suite.



---

archive/issue_comments_030263.json:
```json
{
    "body": "The SPKG installs cleanly and looks good (hg status, SPKG.txt). Patch applies cleanly against 3.1.2 (I'm not on any alpha yet). `sage -tp2 sage/schemes` passes.",
    "created_at": "2008-09-24T11:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4169#issuecomment-30263",
    "user": "malb"
}
```

The SPKG installs cleanly and looks good (hg status, SPKG.txt). Patch applies cleanly against 3.1.2 (I'm not on any alpha yet). `sage -tp2 sage/schemes` passes.



---

archive/issue_comments_030264.json:
```json
{
    "body": "A couple remarks:\n\n* Please do not attach spkgs to trac, instead link them from some webspace.\n* The version patches by Tim break on every BSD and Solaris where we do not use the GNU ld per default. We now work around this by linking gld to ld, but this is *not* a long term solution. Sage in general does not benefit from versioned libraries, indeed they case a bunch of problems when linking extensions, due to the links the archives get larger and on top of that it makes the memory address space on Cygwin even more scare, so I intend to remove every one of those version patches in the future. Those patches should be moved into the Debian packaging directory or alternatively you should provide a makefile target for not versioned libraries.\n* My OSX 64 bit fixes are not in the spkg since this one was based on 0.8.p1, not p2. Please make sure that in the future you case new spkgs on the latest one in Sage. I have fixed the OSX 64 bit missing bits in 0.9.p0 and for now left the versioned library code in makemakefile.py. I intend to remove that code in the future or add a *BSD/Solaris makefile target. Using versioned libraries should be optional.\n* Feel free to add the minimal patch that adds 64 bit OSX support to your repo. If LDFLAGS was actually used when linking on OSX we do not need a separate target like\n\n```\n+print \"libzn_poly.dylib64: $(LIBOBJS)\"\n+print \"\\t$(CC) -m64 -single_module -fPIC -dynamiclib -o libzn_poly.dylib $(LIBOBJS) $(LIBS)\"\n+print\n```\n\n\nBut it is late, so I will take the easy way out instead of fixing the problem the right way :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T08:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4169#issuecomment-30264",
    "user": "mabshoff"
}
```

A couple remarks:

* Please do not attach spkgs to trac, instead link them from some webspace.
* The version patches by Tim break on every BSD and Solaris where we do not use the GNU ld per default. We now work around this by linking gld to ld, but this is *not* a long term solution. Sage in general does not benefit from versioned libraries, indeed they case a bunch of problems when linking extensions, due to the links the archives get larger and on top of that it makes the memory address space on Cygwin even more scare, so I intend to remove every one of those version patches in the future. Those patches should be moved into the Debian packaging directory or alternatively you should provide a makefile target for not versioned libraries.
* My OSX 64 bit fixes are not in the spkg since this one was based on 0.8.p1, not p2. Please make sure that in the future you case new spkgs on the latest one in Sage. I have fixed the OSX 64 bit missing bits in 0.9.p0 and for now left the versioned library code in makemakefile.py. I intend to remove that code in the future or add a *BSD/Solaris makefile target. Using versioned libraries should be optional.
* Feel free to add the minimal patch that adds 64 bit OSX support to your repo. If LDFLAGS was actually used when linking on OSX we do not need a separate target like

```
+print "libzn_poly.dylib64: $(LIBOBJS)"
+print "\t$(CC) -m64 -single_module -fPIC -dynamiclib -o libzn_poly.dylib $(LIBOBJS) $(LIBS)"
+print
```


But it is late, so I will take the easy way out instead of fixing the problem the right way :)

Cheers,

Michael



---

archive/issue_comments_030265.json:
```json
{
    "body": "David,\n\nan updated spkg can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/zn_poly-0.9.p0.spkg\n\nIt contains the 64 bit OSX fixes and some small fixes to spkg-install. Please make sure to base your next spkg on this one ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T09:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4169#issuecomment-30265",
    "user": "mabshoff"
}
```

David,

an updated spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/zn_poly-0.9.p0.spkg

It contains the 64 bit OSX fixes and some small fixes to spkg-install. Please make sure to base your next spkg on this one ;)

Cheers,

Michael



---

archive/issue_comments_030266.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-26T09:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4169#issuecomment-30266",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030267.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-26T09:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4169#issuecomment-30267",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_030268.json:
```json
{
    "body": "Replying to [comment:7 mabshoff]:\n>  * The version patches by Tim break on every BSD and Solaris \n\nI don't really understand the issues here, and I see malb has just opened a thread on sage-devel, so I'll leave this to the experts to thrash out, and I'll be sure to follow their recommendations in future :-)\n\n>  * My OSX 64 bit fixes are not in the spkg since this one was based on 0.8.p1, not p2. Please make sure that in the future you case new spkgs on the latest one in Sage.\n\nOops, sorry about that.\n\ndavid",
    "created_at": "2008-09-26T12:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4169#issuecomment-30268",
    "user": "dmharvey"
}
```

Replying to [comment:7 mabshoff]:
>  * The version patches by Tim break on every BSD and Solaris 

I don't really understand the issues here, and I see malb has just opened a thread on sage-devel, so I'll leave this to the experts to thrash out, and I'll be sure to follow their recommendations in future :-)

>  * My OSX 64 bit fixes are not in the spkg since this one was based on 0.8.p1, not p2. Please make sure that in the future you case new spkgs on the latest one in Sage.

Oops, sorry about that.

david
