# Issue 7825: pari-2.3.3.p5 compilation fails on FreeBSD/amd64

archive/issues_007825.json:
```json
{
    "body": "Assignee: @peterjeremy\n\nCC:  drkirkby @williamstein @craigcitro\n\nFreeBSD refers to the x86_64 architecture under its original name of 'amd64' so use this as an alias for x86_64.  The `-fPIC' fix is needed to correct:\n\n```\ngcc  -o libpari-gmp.so.2.3.3 -shared  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer  -Wl,-shared,-soname=libpari-gmp.so.2 mp.o mpinl.o Flx.o Qfb.o RgX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bibli1.o bibli2.o buch1.o buch2.o buch3.o buch4.o galconj.o gen1.o gen2.o gen3.o ifactor1.o perm.o polarit1.o polarit2.o polarit3.o rootpol.o subcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o default.o errmsg.o es.o init.o intnum.o members.o sumiter.o aprcl.o elldata.o elliptic.o galois.o groupid.o kummer.o mpqs.o nffactor.o part.o stark.o subfield.o thue.o -lc -lm -L/home/peter/sage/sage-4.3/local/lib -lgmp \n/usr/bin/ld: mp.o: relocation R_X86_64_32S can not be used when making a shared object; recompile with -fPIC\nmp.o: could not read symbols: Bad value\n*** Error code 1\n\nStop in /home/peter/sage/sage-4.3/spkg/build/pari-2.3.3.p5/src/Ofreebsd-amd64.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7825\n\n",
    "created_at": "2010-01-03T02:26:54Z",
    "labels": [
        "component: porting: bsd",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "pari-2.3.3.p5 compilation fails on FreeBSD/amd64",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7825",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: @peterjeremy

CC:  drkirkby @williamstein @craigcitro

FreeBSD refers to the x86_64 architecture under its original name of 'amd64' so use this as an alias for x86_64.  The `-fPIC' fix is needed to correct:

```
gcc  -o libpari-gmp.so.2.3.3 -shared  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer  -Wl,-shared,-soname=libpari-gmp.so.2 mp.o mpinl.o Flx.o Qfb.o RgX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bibli1.o bibli2.o buch1.o buch2.o buch3.o buch4.o galconj.o gen1.o gen2.o gen3.o ifactor1.o perm.o polarit1.o polarit2.o polarit3.o rootpol.o subcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o default.o errmsg.o es.o init.o intnum.o members.o sumiter.o aprcl.o elldata.o elliptic.o galois.o groupid.o kummer.o mpqs.o nffactor.o part.o stark.o subfield.o thue.o -lc -lm -L/home/peter/sage/sage-4.3/local/lib -lgmp 
/usr/bin/ld: mp.o: relocation R_X86_64_32S can not be used when making a shared object; recompile with -fPIC
mp.o: could not read symbols: Bad value
*** Error code 1

Stop in /home/peter/sage/sage-4.3/spkg/build/pari-2.3.3.p5/src/Ofreebsd-amd64.
```


Issue created by migration from https://trac.sagemath.org/ticket/7825





---

archive/issue_comments_067615.json:
```json
{
    "body": "Attachment [7825.pari.patch](tarball://root/attachments/some-uuid/ticket7825/7825.pari.patch) by @peterjeremy created at 2010-01-03 02:28:28",
    "created_at": "2010-01-03T02:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7825#issuecomment-67615",
    "user": "https://github.com/peterjeremy"
}
```

Attachment [7825.pari.patch](tarball://root/attachments/some-uuid/ticket7825/7825.pari.patch) by @peterjeremy created at 2010-01-03 02:28:28



---

archive/issue_comments_067616.json:
```json
{
    "body": "Hi Peter, \n\nThank you for cc'ing me. \n\nThe fix looks like it will resolve the FreeBSD issue, but there is an obvious problem with the SPARC platform on that line, as -fPIC will be selected there too, which may not always be appropriate. \n\nIf #7818 gets implemented, it will add a variable FPIC_FLAG which could be set once for any compiler. I don't know if you could change this so spkg-install has something like\n\n\n```\nFPIC_FLAG=-fPIC\n```\n\nthen use $FPIC_FLAG in pari-2.3.3.p5/patches/get_dlcflags. \n\nThat way, it should work today, and with simple removal of the one line from spkg-install, this could work with any compiler. \n\nOh why was there never a standard for compiler flags! Life would be so much easier. \n\nDave",
    "created_at": "2010-01-03T03:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7825#issuecomment-67616",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Hi Peter, 

Thank you for cc'ing me. 

The fix looks like it will resolve the FreeBSD issue, but there is an obvious problem with the SPARC platform on that line, as -fPIC will be selected there too, which may not always be appropriate. 

If #7818 gets implemented, it will add a variable FPIC_FLAG which could be set once for any compiler. I don't know if you could change this so spkg-install has something like


```
FPIC_FLAG=-fPIC
```

then use $FPIC_FLAG in pari-2.3.3.p5/patches/get_dlcflags. 

That way, it should work today, and with simple removal of the one line from spkg-install, this could work with any compiler. 

Oh why was there never a standard for compiler flags! Life would be so much easier. 

Dave



---

archive/issue_comments_067617.json:
```json
{
    "body": "Reported upstream as http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1022.\n\nRegarding Dave's comment above, get_dlcflags is part of pari and already has checks for GNU vs Sun CC.  My patch is inside a 'if test -n \"$__gnuc__\"' block.  If this test fails then '-KPIC' will be used on Solaris/SPARC.  I agree that #7818 represents a more general solution that would simplify get_dlcflags.",
    "created_at": "2010-01-03T03:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7825#issuecomment-67617",
    "user": "https://github.com/peterjeremy"
}
```

Reported upstream as http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1022.

Regarding Dave's comment above, get_dlcflags is part of pari and already has checks for GNU vs Sun CC.  My patch is inside a 'if test -n "$__gnuc__"' block.  If this test fails then '-KPIC' will be used on Solaris/SPARC.  I agree that #7818 represents a more general solution that would simplify get_dlcflags.



---

archive/issue_comments_067618.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T03:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7825#issuecomment-67618",
    "user": "https://github.com/peterjeremy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067619.json:
```json
{
    "body": "That looks good to me then. \n\nI'll give that positive review. \n\nBTW, I see you have __gnuc__ underlined in your comments. I assume you meant to put !__gnuc!__ The trick to avoiding the underlining is to put exclamation marks before the occurrence of the two underscores. Hence you need to do it twice here. That used to drive me round the twist sometimes, but I finally found out how to escape things like that. It also allows one to write VirtualBox without it comping out as VirtualBox, which I find a bit annoying. \n\nDave",
    "created_at": "2010-01-03T04:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7825#issuecomment-67619",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

That looks good to me then. 

I'll give that positive review. 

BTW, I see you have __gnuc__ underlined in your comments. I assume you meant to put !__gnuc!__ The trick to avoiding the underlining is to put exclamation marks before the occurrence of the two underscores. Hence you need to do it twice here. That used to drive me round the twist sometimes, but I finally found out how to escape things like that. It also allows one to write VirtualBox without it comping out as VirtualBox, which I find a bit annoying. 

Dave



---

archive/issue_comments_067620.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-03T04:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7825#issuecomment-67620",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008040.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-01-04T07:14:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7825",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7825#event-8040"
}
```



---

archive/issue_comments_067621.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T07:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7825#issuecomment-67621",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_067622.json:
```json
{
    "body": "I've made an SPKG out of this fix and merged it in 4.3.1.alpha0.  The spkg can be found at http://sage.math.washington.edu/home/mhansen/pari-2.3.3.p6.spkg",
    "created_at": "2010-01-04T07:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7825#issuecomment-67622",
    "user": "https://github.com/mwhansen"
}
```

I've made an SPKG out of this fix and merged it in 4.3.1.alpha0.  The spkg can be found at http://sage.math.washington.edu/home/mhansen/pari-2.3.3.p6.spkg



---

archive/issue_comments_067623.json:
```json
{
    "body": "I note the date in SPKG.txt was 2009 and not 2010. I'm just about to update this again, due to the SAGE64 issues (#7133), so I'll correct that then.",
    "created_at": "2010-01-05T22:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7825#issuecomment-67623",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I note the date in SPKG.txt was 2009 and not 2010. I'm just about to update this again, due to the SAGE64 issues (#7133), so I'll correct that then.
