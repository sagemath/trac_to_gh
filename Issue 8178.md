# Issue 8178: zn_poly fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes

archive/issues_008178.json:
```json
{
    "body": "Assignee: drkirkby\n\nSetting SAGE64=yes has only effect in this package in OSX Darwin.\n\nTo let this work on Open Solaris and evt. other platforms we changed\nspkg-install and patches/makemakefile.py a little bit.\n\nA patch is coming up.\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8178\n\n",
    "created_at": "2010-02-03T18:58:37Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "zn_poly fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8178",
    "user": "https://github.com/jaapspies"
}
```
Assignee: drkirkby

Setting SAGE64=yes has only effect in this package in OSX Darwin.

To let this work on Open Solaris and evt. other platforms we changed
spkg-install and patches/makemakefile.py a little bit.

A patch is coming up.

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8178





---

archive/issue_comments_071940.json:
```json
{
    "body": "Attachment [zn_poly-0.9.p2.patch](tarball://root/attachments/some-uuid/ticket8178/zn_poly-0.9.p2.patch) by @jaapspies created at 2010-02-03 19:36:24",
    "created_at": "2010-02-03T19:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71940",
    "user": "https://github.com/jaapspies"
}
```

Attachment [zn_poly-0.9.p2.patch](tarball://root/attachments/some-uuid/ticket8178/zn_poly-0.9.p2.patch) by @jaapspies created at 2010-02-03 19:36:24



---

archive/issue_comments_071941.json:
```json
{
    "body": "The spkg can be found here:\n\n[http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p2.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p2.spkg)\n\n\n```\njaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ file local/lib/libzn_poly*\nlocal/lib/libzn_poly-0.9.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\nlocal/lib/libzn_poly.a:\tcurrent ar archive, not a dynamic executable or shared object\nlocal/lib/libzn_poly.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n\n```\n\n\nJaap",
    "created_at": "2010-02-03T19:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71941",
    "user": "https://github.com/jaapspies"
}
```

The spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p2.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p2.spkg)


```
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ file local/lib/libzn_poly*
local/lib/libzn_poly-0.9.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libzn_poly.a:	current ar archive, not a dynamic executable or shared object
local/lib/libzn_poly.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped

```


Jaap



---

archive/issue_comments_071942.json:
```json
{
    "body": "Changing assignee from drkirkby to @jaapspies.",
    "created_at": "2010-02-03T19:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71942",
    "user": "https://github.com/jaapspies"
}
```

Changing assignee from drkirkby to @jaapspies.



---

archive/issue_comments_071943.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T19:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71943",
    "user": "https://github.com/jaapspies"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071944.json:
```json
{
    "body": "To avoid the risk of messing something up for everyone, I would make the chances in patches/makemakefile.py to specific to Solaris on 64-bit.",
    "created_at": "2010-02-04T17:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71944",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

To avoid the risk of messing something up for everyone, I would make the chances in patches/makemakefile.py to specific to Solaris on 64-bit.



---

archive/issue_comments_071945.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-04T17:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71945",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071946.json:
```json
{
    "body": "Attachment [libpng-1.2.35.p0+.patch](tarball://root/attachments/some-uuid/ticket8178/libpng-1.2.35.p0+.patch) by @jaapspies created at 2010-02-04 18:55:16\n\nReplying to [comment:3 drkirkby]:\n> To avoid the risk of messing something up for everyone, I would make the chances in patches/makemakefile.py to specific to Solaris on 64-bit. \n\n\n\nI think it is pritty harmless to add $LDFLAGS here. If you don't agree I leave this one to you. I've enough of -m64 :)\n\nJaap",
    "created_at": "2010-02-04T18:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71946",
    "user": "https://github.com/jaapspies"
}
```

Attachment [libpng-1.2.35.p0+.patch](tarball://root/attachments/some-uuid/ticket8178/libpng-1.2.35.p0+.patch) by @jaapspies created at 2010-02-04 18:55:16

Replying to [comment:3 drkirkby]:
> To avoid the risk of messing something up for everyone, I would make the chances in patches/makemakefile.py to specific to Solaris on 64-bit. 



I think it is pritty harmless to add $LDFLAGS here. If you don't agree I leave this one to you. I've enough of -m64 :)

Jaap



---

archive/issue_comments_071947.json:
```json
{
    "body": "And oops, I was on the wrong page. How can I remove an attachement?\n\nJaap",
    "created_at": "2010-02-04T18:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71947",
    "user": "https://github.com/jaapspies"
}
```

And oops, I was on the wrong page. How can I remove an attachement?

Jaap



---

archive/issue_comments_071948.json:
```json
{
    "body": "Changing assignee from @jaapspies to drkirkby.",
    "created_at": "2010-02-04T19:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71948",
    "user": "https://github.com/jaapspies"
}
```

Changing assignee from @jaapspies to drkirkby.



---

archive/issue_comments_071949.json:
```json
{
    "body": "Accidently changed owner to jsp. This happens while scrolling down the page with\nthe mouse wheel.\n\nJaap",
    "created_at": "2010-02-04T19:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71949",
    "user": "https://github.com/jaapspies"
}
```

Accidently changed owner to jsp. This happens while scrolling down the page with
the mouse wheel.

Jaap



---

archive/issue_comments_071950.json:
```json
{
    "body": "Unless this has been checked on several systems, I would prefer not to commit it now.",
    "created_at": "2010-02-04T19:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71950",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Unless this has been checked on several systems, I would prefer not to commit it now.



---

archive/issue_comments_071951.json:
```json
{
    "body": "One more comment. Look at this from the spkg-install file:\n\n\n```\nif [ \"x$SAGE64\" = xyes ]; then\n   echo \"64 bit build\"\n   CFLAGS=\"-O3 -g -m64 -fPIC -L.\"; export CFLAGS\n   LDFLAGS=\"-m64 \"; export LDFLAGS\n   cp patches/makemakefile.py src/makemakefile.py\nelif [ `uname` = \"SunOS\" -a \"`ld  --version  2>&1  | grep GNU`\" = \"\"  ]; then\n   # Change -soname to -h if the Sun linker is used. \n   sed 's/-soname/-h/g' src/makemakefile.py > /tmp/makemakefile.py.$$\n   mv /tmp/makemakefile.py.$$ src/makemakefile.py\n   CFLAGS=\"-fPIC -O3 -L.\"; export CFLAGS\n   LDFLAGS=\"\"; export LDFLAGS\nelse\n   CFLAGS=\"-fPIC -O3 -L.\"; export CFLAGS\n   LDFLAGS=\"\"; export LDFLAGS\nfi\n\n```\n\nYou see LDFAGS is empty except when SAGE64=yes. For now Darwin and SunOS x64 64 bit.\n\nOnly in this case the patches/makemakefile.py is copied. The darwin case is resolved first (even without using the LDFLAGS :) ), see the makefile.\n\nRemains the building of the .so file in our case and that definitely needs the\nLDFLAGS set to -m64.\n\nIf you don't accept this reasoning, I rest my case.\n\n\nCheers,\n\nJaap",
    "created_at": "2010-02-04T20:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71951",
    "user": "https://github.com/jaapspies"
}
```

One more comment. Look at this from the spkg-install file:


```
if [ "x$SAGE64" = xyes ]; then
   echo "64 bit build"
   CFLAGS="-O3 -g -m64 -fPIC -L."; export CFLAGS
   LDFLAGS="-m64 "; export LDFLAGS
   cp patches/makemakefile.py src/makemakefile.py
elif [ `uname` = "SunOS" -a "`ld  --version  2>&1  | grep GNU`" = ""  ]; then
   # Change -soname to -h if the Sun linker is used. 
   sed 's/-soname/-h/g' src/makemakefile.py > /tmp/makemakefile.py.$$
   mv /tmp/makemakefile.py.$$ src/makemakefile.py
   CFLAGS="-fPIC -O3 -L."; export CFLAGS
   LDFLAGS=""; export LDFLAGS
else
   CFLAGS="-fPIC -O3 -L."; export CFLAGS
   LDFLAGS=""; export LDFLAGS
fi

```

You see LDFAGS is empty except when SAGE64=yes. For now Darwin and SunOS x64 64 bit.

Only in this case the patches/makemakefile.py is copied. The darwin case is resolved first (even without using the LDFLAGS :) ), see the makefile.

Remains the building of the .so file in our case and that definitely needs the
LDFLAGS set to -m64.

If you don't accept this reasoning, I rest my case.


Cheers,

Jaap



---

archive/issue_comments_071952.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-04T20:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71952",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071953.json:
```json
{
    "body": "OK, I accept your reasoning. However #8280 got .p2 first, so you will need to create a version against that. \n\nOnce you have done that, I'll convert this to a positive review. \n\nDave",
    "created_at": "2010-02-21T00:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71953",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

OK, I accept your reasoning. However #8280 got .p2 first, so you will need to create a version against that. 

Once you have done that, I'll convert this to a positive review. 

Dave



---

archive/issue_comments_071954.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-21T00:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71954",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071955.json:
```json
{
    "body": "Attachment [zn_poly-0.9.p3.patch](tarball://root/attachments/some-uuid/ticket8178/zn_poly-0.9.p3.patch) by @jaapspies created at 2010-02-21 17:52:25\n\nThe new spkg can be found here:\n\n[http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg)\n\nSee also the new attachment.\n\nJaap",
    "created_at": "2010-02-21T17:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71955",
    "user": "https://github.com/jaapspies"
}
```

Attachment [zn_poly-0.9.p3.patch](tarball://root/attachments/some-uuid/ticket8178/zn_poly-0.9.p3.patch) by @jaapspies created at 2010-02-21 17:52:25

The new spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg)

See also the new attachment.

Jaap



---

archive/issue_comments_071956.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-21T17:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71956",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071957.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-21T23:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71957",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019581.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T23:16:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8178#event-19581"
}
```



---

archive/issue_comments_071958.json:
```json
{
    "body": "Merged [zn_poly-0.9.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg) in the standard spkg repository.",
    "created_at": "2010-03-02T23:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71958",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [zn_poly-0.9.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg) in the standard spkg repository.



---

archive/issue_comments_071959.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T23:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-71959",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
