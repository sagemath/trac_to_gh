# Issue 8178: zn_poly fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes

archive/issues_008178.json:
```json
{
    "body": "Assignee: drkirkby\n\nSetting SAGE64=yes has only effect in this package in OSX Darwin.\n\nTo let this work on Open Solaris and evt. other platforms we changed\nspkg-install and patches/makemakefile.py a little bit.\n\nA patch is coming up.\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8178\n\n",
    "created_at": "2010-02-03T18:58:37Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "zn_poly fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8178",
    "user": "jsp"
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

archive/issue_comments_072062.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-02-03T19:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72062",
    "user": "jsp"
}
```

Attachment



---

archive/issue_comments_072063.json:
```json
{
    "body": "The spkg can be found here:\n\n[http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p2.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p2.spkg)\n\n\n\n```\njaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ file local/lib/libzn_poly*\nlocal/lib/libzn_poly-0.9.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\nlocal/lib/libzn_poly.a:\tcurrent ar archive, not a dynamic executable or shared object\nlocal/lib/libzn_poly.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n\n```\n\n\n\nJaap",
    "created_at": "2010-02-03T19:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72063",
    "user": "jsp"
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

archive/issue_comments_072064.json:
```json
{
    "body": "Changing assignee from drkirkby to jsp.",
    "created_at": "2010-02-03T19:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72064",
    "user": "jsp"
}
```

Changing assignee from drkirkby to jsp.



---

archive/issue_comments_072065.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T19:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72065",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072066.json:
```json
{
    "body": "To avoid the risk of messing something up for everyone, I would make the chances in patches/makemakefile.py to specific to Solaris on 64-bit.",
    "created_at": "2010-02-04T17:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72066",
    "user": "drkirkby"
}
```

To avoid the risk of messing something up for everyone, I would make the chances in patches/makemakefile.py to specific to Solaris on 64-bit.



---

archive/issue_comments_072067.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-04T17:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72067",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072068.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:3 drkirkby]:\n> To avoid the risk of messing something up for everyone, I would make the chances in patches/makemakefile.py to specific to Solaris on 64-bit. \n\n\nI think it is pritty harmless to add $LDFLAGS here. If you don't agree I leave this one to you. I've enough of -m64 :)\n\nJaap",
    "created_at": "2010-02-04T18:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72068",
    "user": "jsp"
}
```

Attachment

Replying to [comment:3 drkirkby]:
> To avoid the risk of messing something up for everyone, I would make the chances in patches/makemakefile.py to specific to Solaris on 64-bit. 


I think it is pritty harmless to add $LDFLAGS here. If you don't agree I leave this one to you. I've enough of -m64 :)

Jaap



---

archive/issue_comments_072069.json:
```json
{
    "body": "And oops, I was on the wrong page. How can I remove an attachement?\n\nJaap",
    "created_at": "2010-02-04T18:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72069",
    "user": "jsp"
}
```

And oops, I was on the wrong page. How can I remove an attachement?

Jaap



---

archive/issue_comments_072070.json:
```json
{
    "body": "Changing assignee from jsp to drkirkby.",
    "created_at": "2010-02-04T19:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72070",
    "user": "jsp"
}
```

Changing assignee from jsp to drkirkby.



---

archive/issue_comments_072071.json:
```json
{
    "body": "Accidently changed owner to jsp. This happens while scrolling down the page with\nthe mouse wheel.\n\nJaap",
    "created_at": "2010-02-04T19:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72071",
    "user": "jsp"
}
```

Accidently changed owner to jsp. This happens while scrolling down the page with
the mouse wheel.

Jaap



---

archive/issue_comments_072072.json:
```json
{
    "body": "Unless this has been checked on several systems, I would prefer not to commit it now.",
    "created_at": "2010-02-04T19:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72072",
    "user": "drkirkby"
}
```

Unless this has been checked on several systems, I would prefer not to commit it now.



---

archive/issue_comments_072073.json:
```json
{
    "body": "One more comment. Look at this from the spkg-install file:\n\n\n\n```\nif [ \"x$SAGE64\" = xyes ]; then\n   echo \"64 bit build\"\n   CFLAGS=\"-O3 -g -m64 -fPIC -L.\"; export CFLAGS\n   LDFLAGS=\"-m64 \"; export LDFLAGS\n   cp patches/makemakefile.py src/makemakefile.py\nelif [ `uname` = \"SunOS\" -a \"`ld  --version  2>&1  | grep GNU`\" = \"\"  ]; then\n   # Change -soname to -h if the Sun linker is used. \n   sed 's/-soname/-h/g' src/makemakefile.py > /tmp/makemakefile.py.$$\n   mv /tmp/makemakefile.py.$$ src/makemakefile.py\n   CFLAGS=\"-fPIC -O3 -L.\"; export CFLAGS\n   LDFLAGS=\"\"; export LDFLAGS\nelse\n   CFLAGS=\"-fPIC -O3 -L.\"; export CFLAGS\n   LDFLAGS=\"\"; export LDFLAGS\nfi\n\n```\n\n\nYou see LDFAGS is empty except when SAGE64=yes. For now Darwin and SunOS x64 64 bit.\n\nOnly in this case the patches/makemakefile.py is copied. The darwin case is resolved first (even without using the LDFLAGS :) ), see the makefile.\n\nRemains the building of the .so file in our case and that definitely needs the\nLDFLAGS set to -m64.\n\nIf you don't accept this reasoning, I rest my case.\n\n\nCheers,\n\nJaap",
    "created_at": "2010-02-04T20:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72073",
    "user": "jsp"
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

archive/issue_comments_072074.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-04T20:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72074",
    "user": "jsp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072075.json:
```json
{
    "body": "OK, I accept your reasoning. However #8280 got .p2 first, so you will need to create a version against that. \n\nOnce you have done that, I'll convert this to a positive review. \n\nDave",
    "created_at": "2010-02-21T00:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72075",
    "user": "drkirkby"
}
```

OK, I accept your reasoning. However #8280 got .p2 first, so you will need to create a version against that. 

Once you have done that, I'll convert this to a positive review. 

Dave



---

archive/issue_comments_072076.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-21T00:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72076",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072077.json:
```json
{
    "body": "Attachment\n\nThe new spkg can be found here:\n\n[http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg)\n\nSee also the new attachment.\n\nJaap",
    "created_at": "2010-02-21T17:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72077",
    "user": "jsp"
}
```

Attachment

The new spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg)

See also the new attachment.

Jaap



---

archive/issue_comments_072078.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-21T17:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72078",
    "user": "jsp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072079.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-21T23:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72079",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072080.json:
```json
{
    "body": "Merged [zn_poly-0.9.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg) in the standard spkg repository.",
    "created_at": "2010-03-02T23:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72080",
    "user": "mvngu"
}
```

Merged [zn_poly-0.9.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg) in the standard spkg repository.



---

archive/issue_comments_072081.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T23:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8178#issuecomment-72081",
    "user": "mvngu"
}
```

Resolution: fixed
