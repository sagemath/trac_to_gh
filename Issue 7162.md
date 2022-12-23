# Issue 7162: maybe remove linking xpm into gd

archive/issues_007162.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  was drkirkby jsp\n\nI'm trying to build sage-4.1.2 on disk.math.washington.edu (opensolaris x86) and had to change the spkg-install of gd-2.0.35.p2:\n\n```\n# We explicitly disable X support, since (1) X is not a SAGE dependency,\n# and (2) the gd build fails on a lot of OS X PPC machines when X is enabled.\n./configure --prefix=\"$SAGE_LOCAL\" --without-jpeg --without-x --without-xpm --with-zlib=\"$SAGE_LOCAL\" --with-freetype=\"$SAGE_LOCAL\"\n```\n\n\nI added `--without-xpm`.\n\nMaybe we should make this standard?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7162\n\n",
    "created_at": "2009-10-08T20:07:15Z",
    "labels": [
        "porting: Solaris",
        "minor",
        "bug"
    ],
    "title": "maybe remove linking xpm into gd",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7162",
    "user": "was"
}
```
Assignee: tbd

CC:  was drkirkby jsp

I'm trying to build sage-4.1.2 on disk.math.washington.edu (opensolaris x86) and had to change the spkg-install of gd-2.0.35.p2:

```
# We explicitly disable X support, since (1) X is not a SAGE dependency,
# and (2) the gd build fails on a lot of OS X PPC machines when X is enabled.
./configure --prefix="$SAGE_LOCAL" --without-jpeg --without-x --without-xpm --with-zlib="$SAGE_LOCAL" --with-freetype="$SAGE_LOCAL"
```


I added `--without-xpm`.

Maybe we should make this standard?


Issue created by migration from https://trac.sagemath.org/ticket/7162





---

archive/issue_comments_059375.json:
```json
{
    "body": "It seems sensible to make it standard to me. \n\nIf you want to post a package, I'll review it.",
    "created_at": "2009-11-04T04:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59375",
    "user": "drkirkby"
}
```

It seems sensible to make it standard to me. 

If you want to post a package, I'll review it.



---

archive/issue_comments_059376.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T18:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59376",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059377.json:
```json
{
    "body": "Attachment\n\nA revised .spkg can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/gd-2.0.35.p3/gd-2.0.35.p3.spkg",
    "created_at": "2010-01-02T18:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59377",
    "user": "drkirkby"
}
```

Attachment

A revised .spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/gd-2.0.35.p3/gd-2.0.35.p3.spkg



---

archive/issue_comments_059378.json:
```json
{
    "body": "Replying to [comment:2 drkirkby]:\n> A revised .spkg can be found at \n> \n> http://boxen.math.washington.edu/home/kirkby/portability/gd-2.0.35.p3/gd-2.0.35.p3.spkg\n\nThis change make the build depend on setting export CFLAGS=-m64\n\nIs this a good thing to  do?\n\nJaap",
    "created_at": "2010-01-02T21:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59378",
    "user": "jsp"
}
```

Replying to [comment:2 drkirkby]:
> A revised .spkg can be found at 
> 
> http://boxen.math.washington.edu/home/kirkby/portability/gd-2.0.35.p3/gd-2.0.35.p3.spkg

This change make the build depend on setting export CFLAGS=-m64

Is this a good thing to  do?

Jaap



---

archive/issue_comments_059379.json:
```json
{
    "body": "Hi, \nyou have a point, but there was some logic to this. \n\nThe purpose of the ticket which William opened was to add \n\n\n```\n--without-xpm\n```\n\n\nto the line where the configure script it invoked. The ticket had nothing to to with SAGE64.\n\nI think whilst trying to build on Solaris in 64-bit mode, you should set CFLAGS and CXXFLAGS to include -m64, as that will allow **some** packages to build without making changes to their spkg-install files. This is one such package. \n\nI've written two scripts (#7505) which check what the compiler is (GCC, Sun Studio, HP, IBM etc). That ticket already has positive review. \n\nI've written an updated version of sage-env, #7818 which is awaiting review. That will uses those two script, determine the right compiler flag, then automatically export the right compiler flag to CFLAGS. \n\nAs such, I believe making only the change William suggested is sufficient in this case. Just export CFLAGS and CXXFLAGS to include -m64, and expect that in the next release or two, that will happen automatically for you. Doing this, will reduce somewhat the number of spkg-install files that need editing. \n\nDave",
    "created_at": "2010-01-02T22:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59379",
    "user": "drkirkby"
}
```

Hi, 
you have a point, but there was some logic to this. 

The purpose of the ticket which William opened was to add 


```
--without-xpm
```


to the line where the configure script it invoked. The ticket had nothing to to with SAGE64.

I think whilst trying to build on Solaris in 64-bit mode, you should set CFLAGS and CXXFLAGS to include -m64, as that will allow **some** packages to build without making changes to their spkg-install files. This is one such package. 

I've written two scripts (#7505) which check what the compiler is (GCC, Sun Studio, HP, IBM etc). That ticket already has positive review. 

I've written an updated version of sage-env, #7818 which is awaiting review. That will uses those two script, determine the right compiler flag, then automatically export the right compiler flag to CFLAGS. 

As such, I believe making only the change William suggested is sufficient in this case. Just export CFLAGS and CXXFLAGS to include -m64, and expect that in the next release or two, that will happen automatically for you. Doing this, will reduce somewhat the number of spkg-install files that need editing. 

Dave



---

archive/issue_comments_059380.json:
```json
{
    "body": "Ok, nobody is hurt here. People who are porting should know this.\n\nSo I give it a positive review.\n\nJaap",
    "created_at": "2010-01-02T23:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59380",
    "user": "jsp"
}
```

Ok, nobody is hurt here. People who are porting should know this.

So I give it a positive review.

Jaap



---

archive/issue_comments_059381.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-02T23:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59381",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T22:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59382",
    "user": "mhansen"
}
```

Resolution: fixed
