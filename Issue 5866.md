# Issue 5866: Fix freetype build on systems where make is not GNU make.

archive/issues_005866.json:
```json
{
    "body": "Assignee: mabshoff\n\nChange 'make' to ${MAKE} - is the recommended way to recursively invoke make to ensure that the subordinate make is the same as the parent make (and also ensures that the two make instances will communicate on things like '-jX').\n\nExplicitly export the parent make into the configure script.\n\nThese changes avoid problems on systems like FreeBSD where make is not GNU make.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5866\n\n",
    "created_at": "2009-04-23T06:51:35Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "title": "Fix freetype build on systems where make is not GNU make.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5866",
    "user": "pjeremy"
}
```
Assignee: mabshoff

Change 'make' to ${MAKE} - is the recommended way to recursively invoke make to ensure that the subordinate make is the same as the parent make (and also ensures that the two make instances will communicate on things like '-jX').

Explicitly export the parent make into the configure script.

These changes avoid problems on systems like FreeBSD where make is not GNU make.

Issue created by migration from https://trac.sagemath.org/ticket/5866





---

archive/issue_comments_046337.json:
```json
{
    "body": "Attachment [freetype-2.3.5.p0.patch](tarball://root/attachments/some-uuid/ticket5866/freetype-2.3.5.p0.patch) by pjeremy created at 2009-04-23 06:53:28",
    "created_at": "2009-04-23T06:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5866#issuecomment-46337",
    "user": "pjeremy"
}
```

Attachment [freetype-2.3.5.p0.patch](tarball://root/attachments/some-uuid/ticket5866/freetype-2.3.5.p0.patch) by pjeremy created at 2009-04-23 06:53:28



---

archive/issue_comments_046338.json:
```json
{
    "body": "I will work on integrating this tomorrow.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5866#issuecomment-46338",
    "user": "mabshoff"
}
```

I will work on integrating this tomorrow.

Cheers,

Michael



---

archive/issue_comments_046339.json:
```json
{
    "body": "Looks good to me.\n\nThe spkg with this change incorporated can be found at http://sage.math.washington.edu/home/mhansen/freetype-2.3.5.p1.spkg",
    "created_at": "2009-06-20T02:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5866#issuecomment-46339",
    "user": "mhansen"
}
```

Looks good to me.

The spkg with this change incorporated can be found at http://sage.math.washington.edu/home/mhansen/freetype-2.3.5.p1.spkg



---

archive/issue_comments_046340.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T02:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5866#issuecomment-46340",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046341.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-06-20T02:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5866#issuecomment-46341",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_046342.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T22:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5866#issuecomment-46342",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_046343.json:
```json
{
    "body": "I'll create a new ticket for this issue, but I thought it useful to add to this ticket. \n\nI tried to update freetype to the latest version (2.3.12), but the build fails with:\n\n\n```\nlibtool: link: (cd \"/export/home/drkirkby/32/sage-4.4.3/spkg/build/freetype-2.3.12/src/objs/.libs\" && rm \"libfreetype.so.6\" && ln -s \"libfreetype.so.6.4.0\" \"libfreetype.so.6\")\nlibfreetype.so.6: No such file or directory\nmake: *** [/export/home/drkirkby/32/sage-4.4.3/spkg/build/freetype-2.3.12/src/objs/libfreetype.la] Error 2\n\nreal    3m16.562s\nuser    2m54.021s\nsys     0m22.112s\nsage: An error occurred while installing freetype-2.3.12\n```\n\n\nChanging spkg-install to \n\n\n```\nif [ \"x`uname`\" != xSunOS ] ; then \n   GNUMAKE=${MAKE} ./configure --prefix=\"$SAGE_LOCAL\"\nelse\n  ./configure --prefix=\"$SAGE_LOCAL\"\nfi\n```\n\n\nallows the latest freetype to build on Solaris 10 on SPARC.",
    "created_at": "2010-06-10T07:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5866#issuecomment-46343",
    "user": "drkirkby"
}
```

I'll create a new ticket for this issue, but I thought it useful to add to this ticket. 

I tried to update freetype to the latest version (2.3.12), but the build fails with:


```
libtool: link: (cd "/export/home/drkirkby/32/sage-4.4.3/spkg/build/freetype-2.3.12/src/objs/.libs" && rm "libfreetype.so.6" && ln -s "libfreetype.so.6.4.0" "libfreetype.so.6")
libfreetype.so.6: No such file or directory
make: *** [/export/home/drkirkby/32/sage-4.4.3/spkg/build/freetype-2.3.12/src/objs/libfreetype.la] Error 2

real    3m16.562s
user    2m54.021s
sys     0m22.112s
sage: An error occurred while installing freetype-2.3.12
```


Changing spkg-install to 


```
if [ "x`uname`" != xSunOS ] ; then 
   GNUMAKE=${MAKE} ./configure --prefix="$SAGE_LOCAL"
else
  ./configure --prefix="$SAGE_LOCAL"
fi
```


allows the latest freetype to build on Solaris 10 on SPARC.



---

archive/issue_comments_046344.json:
```json
{
    "body": "I should have added that 'make' is a version of GNU make on Solaris, as Sun's make will never build Sage. The MAKE environment variable was not set. \n\nDave",
    "created_at": "2010-06-10T07:34:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5866#issuecomment-46344",
    "user": "drkirkby"
}
```

I should have added that 'make' is a version of GNU make on Solaris, as Sun's make will never build Sage. The MAKE environment variable was not set. 

Dave
