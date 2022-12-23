# Issue 8844: add missing libraries to module_list for Cygwin

archive/issues_008844.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  leif robertwb\n\nCygwin is a lot pickier about missing symbols so more libraries need to be linked in to the extension modules.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8844\n\n",
    "created_at": "2010-05-03T04:53:40Z",
    "labels": [
        "Cygwin",
        "major",
        "bug"
    ],
    "title": "add missing libraries to module_list for Cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8844",
    "user": "mhansen"
}
```
Assignee: tbd

CC:  leif robertwb

Cygwin is a lot pickier about missing symbols so more libraries need to be linked in to the extension modules.

Issue created by migration from https://trac.sagemath.org/ticket/8844





---

archive/issue_comments_081301.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-03T13:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81301",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_081302.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-03T13:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81302",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081303.json:
```json
{
    "body": "Changing component from cygwin to build.",
    "created_at": "2010-05-19T22:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81303",
    "user": "mhansen"
}
```

Changing component from cygwin to build.



---

archive/issue_comments_081304.json:
```json
{
    "body": "`s/'png'/'png12'/` (once).",
    "created_at": "2010-05-20T02:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81304",
    "user": "leif"
}
```

`s/'png'/'png12'/` (once).



---

archive/issue_comments_081305.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-20T02:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81305",
    "user": "leif"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081306.json:
```json
{
    "body": "(Or we should create symbolic links from `libpng.so*` to `libpng12.so*`.)",
    "created_at": "2010-05-20T02:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81306",
    "user": "leif"
}
```

(Or we should create symbolic links from `libpng.so*` to `libpng12.so*`.)



---

archive/issue_comments_081307.json:
```json
{
    "body": "Symbolic links don't work for linking libraries in Cygwin.",
    "created_at": "2010-05-20T02:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81307",
    "user": "mhansen"
}
```

Symbolic links don't work for linking libraries in Cygwin.



---

archive/issue_comments_081308.json:
```json
{
    "body": "Reviewer patch, s/png/png12/ once as mentioned",
    "created_at": "2010-05-20T07:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81308",
    "user": "leif"
}
```

Reviewer patch, s/png/png12/ once as mentioned



---

archive/issue_comments_081309.json:
```json
{
    "body": "Attachment\n\nNow **trying** to rebase #7987 on this one...",
    "created_at": "2010-05-20T07:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81309",
    "user": "leif"
}
```

Attachment

Now **trying** to rebase #7987 on this one...



---

archive/issue_comments_081310.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-20T07:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81310",
    "user": "leif"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081311.json:
```json
{
    "body": "Changing keywords from \"\" to \"missing library, unresolved symbol\".",
    "created_at": "2010-05-20T18:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81311",
    "user": "leif"
}
```

Changing keywords from "" to "missing library, unresolved symbol".



---

archive/issue_comments_081312.json:
```json
{
    "body": "Works for OpenSuSE 11.2: http://groups.google.com/group/sage-devel/msg/1078faf7f0c6ec48\n\n(And most probably will for Fedora 13, too, which is released in a few days.)",
    "created_at": "2010-05-20T18:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81312",
    "user": "leif"
}
```

Works for OpenSuSE 11.2: http://groups.google.com/group/sage-devel/msg/1078faf7f0c6ec48

(And most probably will for Fedora 13, too, which is released in a few days.)



---

archive/issue_comments_081313.json:
```json
{
    "body": "It seems the whole Sage library build process needs clean-ups...\n(i.e. `local/bin/sage-build`, `devel/sage/module_list.py`, `devel/sage/setup.py`, and perhaps `devel/sage/c_lib/SConstruct`)\n\nBtw, at least all Sage library C files (of course including those generated by `cython`) compile with gcc and `-std=c99 [-pedantic]`, though not really standard-conformant. (C++ files currently don't, neither with `-std=c++98` nor `c++0x`.)",
    "created_at": "2010-05-22T10:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81313",
    "user": "leif"
}
```

It seems the whole Sage library build process needs clean-ups...
(i.e. `local/bin/sage-build`, `devel/sage/module_list.py`, `devel/sage/setup.py`, and perhaps `devel/sage/c_lib/SConstruct`)

Btw, at least all Sage library C files (of course including those generated by `cython`) compile with gcc and `-std=c99 [-pedantic]`, though not really standard-conformant. (C++ files currently don't, neither with `-std=c++98` nor `c++0x`.)



---

archive/issue_comments_081314.json:
```json
{
    "body": "Thanks for the review patch.  We'll hopefully get this merged this evening.",
    "created_at": "2010-05-25T22:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81314",
    "user": "mhansen"
}
```

Thanks for the review patch.  We'll hopefully get this merged this evening.



---

archive/issue_comments_081315.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-26T01:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81315",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_081316.json:
```json
{
    "body": "The reviewer patch actually breaks things on Cygwin.  It should be reverted.",
    "created_at": "2010-05-27T23:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81316",
    "user": "mhansen"
}
```

The reviewer patch actually breaks things on Cygwin.  It should be reverted.



---

archive/issue_comments_081317.json:
```json
{
    "body": "Replying to [comment:13 mhansen]:\n> The reviewer patch actually breaks things on Cygwin.  It should be reverted.\n\nHow can that be? At least on Linux, there's no `libpng.so`, just `libpng12.so`, so reverting it wouldn't build on other systems.",
    "created_at": "2010-05-28T03:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81317",
    "user": "leif"
}
```

Replying to [comment:13 mhansen]:
> The reviewer patch actually breaks things on Cygwin.  It should be reverted.

How can that be? At least on Linux, there's no `libpng.so`, just `libpng12.so`, so reverting it wouldn't build on other systems.



---

archive/issue_comments_081318.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n> Btw, at least all Sage library C files (of course including those generated by `cython`) compile with gcc and `-std=c99 [-pedantic]`, though not really standard-conformant. (C++ files currently don't, neither with `-std=c++98` nor `c++0x`.)\n> \n>  \n\nThe problem with c_lib/SConstruct is that nobody to my knowledge knows SCons well. I know it needs something to add the -m64 flag to CFLAGS, CXXFLAGS and LDFLAGS on platforms other than OS X (darwin). Something like (untested)\n\n\n```\nif env['PLATFORM'] != \"darwin\" and os.environ['SAGE64']==\"yes\" \n        env.Append( CFLAGS=\"-O2 -g -m64\" )\n        env.Append( CXXFLAGS=\"-O2 -g -m64\" )\n        env.Append( LINKFLAGS=\"-m64\" )\n```\n\n\nThis seems a problem in general with Sage and SCons - nobody really knows what they are doing with it. \n\nDave",
    "created_at": "2010-06-03T15:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81318",
    "user": "drkirkby"
}
```

Replying to [comment:9 leif]:
> Btw, at least all Sage library C files (of course including those generated by `cython`) compile with gcc and `-std=c99 [-pedantic]`, though not really standard-conformant. (C++ files currently don't, neither with `-std=c++98` nor `c++0x`.)
> 
>  

The problem with c_lib/SConstruct is that nobody to my knowledge knows SCons well. I know it needs something to add the -m64 flag to CFLAGS, CXXFLAGS and LDFLAGS on platforms other than OS X (darwin). Something like (untested)


```
if env['PLATFORM'] != "darwin" and os.environ['SAGE64']=="yes" 
        env.Append( CFLAGS="-O2 -g -m64" )
        env.Append( CXXFLAGS="-O2 -g -m64" )
        env.Append( LINKFLAGS="-m64" )
```


This seems a problem in general with Sage and SCons - nobody really knows what they are doing with it. 

Dave



---

archive/issue_comments_081319.json:
```json
{
    "body": "Replying to [comment:15 drkirkby]:\n> Replying to [comment:9 leif]:\n> > Btw, at least all Sage library C files (of course including those generated by `cython`) compile with gcc and `-std=c99 [-pedantic]`, though not really standard-conformant. (C++ files currently don't, neither with `-std=c++98` nor `c++0x`.)\n> > \n> >  \n> \n> The problem with c_lib/SConstruct is that nobody to my knowledge knows SCons well. I know it needs something to add the -m64 flag to CFLAGS, CXXFLAGS and LDFLAGS on platforms other than OS X (darwin). Something like (untested)\n> \n> {{{\n> if env['PLATFORM'] != \"darwin\" and os.environ['SAGE64']==\"yes\" \n>         env.Append( CFLAGS=\"-O2 -g -m64\" )\n>         env.Append( CXXFLAGS=\"-O2 -g -m64\" )\n>         env.Append( LINKFLAGS=\"-m64\" )\n> }}}\n> \n> This seems a problem in general with Sage and SCons - nobody really knows what they are doing with it. \n> \n> Dave \n\n\nOops, I posted my comment about SCons under the wrong comment. It was meant to be under that of leif, who wrote:\n\n*It seems the whole Sage library build process needs clean-ups... (i.e. local/bin/sage-build, devel/sage/module_list.py, devel/sage/setup.py, and perhaps devel/sage/c_lib/SConstruct)*\n\nDave",
    "created_at": "2010-06-03T15:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81319",
    "user": "drkirkby"
}
```

Replying to [comment:15 drkirkby]:
> Replying to [comment:9 leif]:
> > Btw, at least all Sage library C files (of course including those generated by `cython`) compile with gcc and `-std=c99 [-pedantic]`, though not really standard-conformant. (C++ files currently don't, neither with `-std=c++98` nor `c++0x`.)
> > 
> >  
> 
> The problem with c_lib/SConstruct is that nobody to my knowledge knows SCons well. I know it needs something to add the -m64 flag to CFLAGS, CXXFLAGS and LDFLAGS on platforms other than OS X (darwin). Something like (untested)
> 
> {{{
> if env['PLATFORM'] != "darwin" and os.environ['SAGE64']=="yes" 
>         env.Append( CFLAGS="-O2 -g -m64" )
>         env.Append( CXXFLAGS="-O2 -g -m64" )
>         env.Append( LINKFLAGS="-m64" )
> }}}
> 
> This seems a problem in general with Sage and SCons - nobody really knows what they are doing with it. 
> 
> Dave 


Oops, I posted my comment about SCons under the wrong comment. It was meant to be under that of leif, who wrote:

*It seems the whole Sage library build process needs clean-ups... (i.e. local/bin/sage-build, devel/sage/module_list.py, devel/sage/setup.py, and perhaps devel/sage/c_lib/SConstruct)*

Dave



---

archive/issue_comments_081320.json:
```json
{
    "body": "Did anybody remember why `gmp` was added as dependency to the various `symbolic` modules? I don't believe those actually depend on `gmp`. This change is partially responsible for #19602.",
    "created_at": "2015-11-20T11:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81320",
    "user": "jdemeyer"
}
```

Did anybody remember why `gmp` was added as dependency to the various `symbolic` modules? I don't believe those actually depend on `gmp`. This change is partially responsible for #19602.



---

archive/issue_comments_081321.json:
```json
{
    "body": "The linked thread does mention some problems with `gmp`, but not in the `symbolic` modules.\n\nPS for `@`was: the fact that I'm even *able* to ask this question is because I can check the git history to see where this dependency was added. This is exactly what open development is about.",
    "created_at": "2015-11-20T11:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81321",
    "user": "jdemeyer"
}
```

The linked thread does mention some problems with `gmp`, but not in the `symbolic` modules.

PS for `@`was: the fact that I'm even *able* to ask this question is because I can check the git history to see where this dependency was added. This is exactly what open development is about.



---

archive/issue_comments_081322.json:
```json
{
    "body": "Replying to [comment:17 jdemeyer]:\n> Did anybody remember why `gmp` was added as dependency to the various `symbolic` modules? I don't believe those actually depend on `gmp`.\n\nI can only guess this was some kind of overkill, caused by confusing the `pynac` *extension module* with the external Pynac library `libpynac`.  While the former indeed uses GMP and hence needs to get linked with it (*and* in addition `libpynac`), the latter does not.",
    "created_at": "2015-11-20T15:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8844#issuecomment-81322",
    "user": "leif"
}
```

Replying to [comment:17 jdemeyer]:
> Did anybody remember why `gmp` was added as dependency to the various `symbolic` modules? I don't believe those actually depend on `gmp`.

I can only guess this was some kind of overkill, caused by confusing the `pynac` *extension module* with the external Pynac library `libpynac`.  While the former indeed uses GMP and hence needs to get linked with it (*and* in addition `libpynac`), the latter does not.
