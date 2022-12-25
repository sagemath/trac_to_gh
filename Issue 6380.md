# Issue 6380: [with patch, needs review] Allow NTL to build on Solaris with Sun or GNU linker

archive/issues_006380.json:
```json
{
    "body": "Assignee: drkirkby\n\nKeywords: solaris ntl makefile GNUism\n\nAlthough the ntl-5.4.2.p7 package would build on Solaris 10 with gcc 4.4.0 if the gcc was configured to use the GNU linker from binutils, the package would not build with the gcc if the compiler was configured to use the Sun linker, with the following options:\n\n--with-ld=/usr/ccs/bin/ld --without-gnu-ld \n\nThe part of the makefile executed when building a shared library would fail if the Sun linker was used. The makefile specified the same output filename twice, but in a way the Sun linker would not tolerate. \n\nThis patch simply removes a very small bit of code (just \"-Wl,-soname,lib`cat DIRNAME`.so \"), which allows NTL to build properly, irrespective of the linker that is being used. \n\nPlease see \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/ntl/\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6380\n\n",
    "created_at": "2009-06-21T21:59:34Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, needs review] Allow NTL to build on Solaris with Sun or GNU linker",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6380",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

Keywords: solaris ntl makefile GNUism

Although the ntl-5.4.2.p7 package would build on Solaris 10 with gcc 4.4.0 if the gcc was configured to use the GNU linker from binutils, the package would not build with the gcc if the compiler was configured to use the Sun linker, with the following options:

--with-ld=/usr/ccs/bin/ld --without-gnu-ld 

The part of the makefile executed when building a shared library would fail if the Sun linker was used. The makefile specified the same output filename twice, but in a way the Sun linker would not tolerate. 

This patch simply removes a very small bit of code (just "-Wl,-soname,lib`cat DIRNAME`.so "), which allows NTL to build properly, irrespective of the linker that is being used. 

Please see 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ntl/



Issue created by migration from https://trac.sagemath.org/ticket/6380





---

archive/issue_comments_050974.json:
```json
{
    "body": "Positive review, though I didn't test it with the Sun linker, it looks very sensible and doesn't break things.  \n\nAn spkg with the changes checked into the repo and a typo fixed is now here:\n\n  http://sage.math.washington.edu/home/wstein/patches/ntl-5.4.2.p8.spkg",
    "created_at": "2009-06-21T23:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6380#issuecomment-50974",
    "user": "https://github.com/williamstein"
}
```

Positive review, though I didn't test it with the Sun linker, it looks very sensible and doesn't break things.  

An spkg with the changes checked into the repo and a typo fixed is now here:

  http://sage.math.washington.edu/home/wstein/patches/ntl-5.4.2.p8.spkg



---

archive/issue_comments_050975.json:
```json
{
    "body": "Unfortunately, another ticket already got \"p8\", and the changes here need to be reapplied to that spkg.",
    "created_at": "2009-07-02T23:30:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6380#issuecomment-50975",
    "user": "https://github.com/rlmill"
}
```

Unfortunately, another ticket already got "p8", and the changes here need to be reapplied to that spkg.



---

archive/issue_comments_050976.json:
```json
{
    "body": "Replying to [comment:2 rlm]:\n> Unfortunately, another ticket already got \"p8\", and the changes here need to be reapplied to that spkg.\n\nThat spkg is available here:\n\nhttp://sage.math.washington.edu/home/rlmill/ntl-5.4.2.p8.spkg",
    "created_at": "2009-07-02T23:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6380#issuecomment-50976",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:2 rlm]:
> Unfortunately, another ticket already got "p8", and the changes here need to be reapplied to that spkg.

That spkg is available here:

http://sage.math.washington.edu/home/rlmill/ntl-5.4.2.p8.spkg



---

archive/issue_comments_050977.json:
```json
{
    "body": "OK, I've made the changes. \n\nPlease see: \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/ntl-5.4.2.p9/ (different directory to last one)\n\nI created a patchfile which shows the differences from the last copy of 'mfile' otherwise the patch would be huge and uncomprehsible, as mfile has been changed so many times. There is actually a patch in the 'patches' directory. \n\nI just noticed I probably put the original and new files in the wrong order, as it looks like I've added stuff to the 'mfile' not taken it away. I have in fact just *removed*   -Wl,-soname,libcat DIRNAME.so\n\nFormally the line was:\n\t$(LINK_CXX) -fPIC -shared -Wl,-soname,lib`cat DIRNAME`.so -o lib`cat DIRNAME`.so $(OBJ) $(GMP_LIBDIR)\n\nnow it is \n\t$(LINK_CXX) -fPIC -shared -o lib`cat DIRNAME`.so $(OBJ) $(GMP_LIBDIR) $(GMP_LIB)",
    "created_at": "2009-07-09T21:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6380#issuecomment-50977",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

OK, I've made the changes. 

Please see: 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ntl-5.4.2.p9/ (different directory to last one)

I created a patchfile which shows the differences from the last copy of 'mfile' otherwise the patch would be huge and uncomprehsible, as mfile has been changed so many times. There is actually a patch in the 'patches' directory. 

I just noticed I probably put the original and new files in the wrong order, as it looks like I've added stuff to the 'mfile' not taken it away. I have in fact just *removed*   -Wl,-soname,libcat DIRNAME.so

Formally the line was:
	$(LINK_CXX) -fPIC -shared -Wl,-soname,lib`cat DIRNAME`.so -o lib`cat DIRNAME`.so $(OBJ) $(GMP_LIBDIR)

now it is 
	$(LINK_CXX) -fPIC -shared -o lib`cat DIRNAME`.so $(OBJ) $(GMP_LIBDIR) $(GMP_LIB)



---

archive/issue_comments_050978.json:
```json
{
    "body": "Replying to [comment:4 drkirkby]:\n> OK, I've made the changes. \n> \n> Please see: \n> \n> http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ntl-5.4.2.p9/ (different directory to last one)\nThe NTL spkg above contains some junk and changes were not checked in. I've checked in changes in David Kirkby's name. The updated spkg is available at\n\nhttp://sage.math.washington.edu/home/mvngu/patch/ntl-5.4.2.p9.spkg",
    "created_at": "2009-07-15T16:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6380#issuecomment-50978",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:4 drkirkby]:
> OK, I've made the changes. 
> 
> Please see: 
> 
> http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ntl-5.4.2.p9/ (different directory to last one)
The NTL spkg above contains some junk and changes were not checked in. I've checked in changes in David Kirkby's name. The updated spkg is available at

http://sage.math.washington.edu/home/mvngu/patch/ntl-5.4.2.p9.spkg



---

archive/issue_comments_050979.json:
```json
{
    "body": "After installing the NTL package at\n\nhttp://sage.math.washington.edu/home/mvngu/patch/ntl-5.4.2.p9.spkg\n\nand running doctests on all of the Sage library, I got this:\n\n```\nThe following tests failed:\n\n        sage -t -long devel/sage-main/sage/modular/hecke/morphism.py # 0 doctests failed\n        sage -t -long devel/sage-main/sage/categories/morphism.pyx # 0 doctests failed\n```\n\nThe funny thing is that it reports doctest failures, with \"0 doctests failed\". I reinstalled `ntl-5.4.2.p8.spkg` and ran all doctests again, and they passed. I then installed **ntl-5.4.2.p9.spkg** a second time, ran all doctests, and they now passed without any of those weird \"0 doctests failed\".",
    "created_at": "2009-07-15T17:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6380#issuecomment-50979",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

After installing the NTL package at

http://sage.math.washington.edu/home/mvngu/patch/ntl-5.4.2.p9.spkg

and running doctests on all of the Sage library, I got this:

```
The following tests failed:

        sage -t -long devel/sage-main/sage/modular/hecke/morphism.py # 0 doctests failed
        sage -t -long devel/sage-main/sage/categories/morphism.pyx # 0 doctests failed
```

The funny thing is that it reports doctest failures, with "0 doctests failed". I reinstalled `ntl-5.4.2.p8.spkg` and ran all doctests again, and they passed. I then installed **ntl-5.4.2.p9.spkg** a second time, ran all doctests, and they now passed without any of those weird "0 doctests failed".



---

archive/issue_comments_050980.json:
```json
{
    "body": "Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T10:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6380#issuecomment-50980",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_events_006628.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-16T21:27:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6380",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6380#event-6628"
}
```



---

archive/issue_comments_050981.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6380#issuecomment-50981",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
