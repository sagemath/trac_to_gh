# Issue 1259: readline miscompiles on OSX 10.5.[1]

archive/issues_001259.json:
```json
{
    "body": "Assignee: mabshoff\n\nJustin Walker reports:\n\n```\nThe only problem with the build is this, with readline:\n\nConfigured with: /var/tmp/gcc/gcc-5465~16/src/configure --disable-\nchecking -enable-werror --prefix=/usr --mandir=/share/man --enable-\nlanguages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/\n$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/\nlib --build=i686-apple-darwin9 --with-arch=apple --with-tune=generic  \n--host=i686-apple-darwin9 --target=i686-apple-darwin9\nThread model: posix\ngcc version 4.0.1 (Apple Inc. build 5465)\ni686-apple-darwin9-gcc-4.0.1: -compatibility_version only allowed  \nwith -dynamiclib\ni686-apple-darwin9-gcc-4.0.1: -compatibility_version only allowed  \nwith -dynamiclib\nmake[3]: *** [libreadline.5.2.dylib] Error 1\nmake[3]: *** Waiting for unfinished jobs....\nmake[3]: *** [libhistory.5.2.dylib] Error 1\nmake[2]: [install-shared] Error 2 (ignored)\n\nFWIW, this same error crops up in a standalone build of readline, but  \nit kills the build.  Sage seems to be unconcerned.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1259\n\n",
    "created_at": "2007-11-25T04:34:31Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "readline miscompiles on OSX 10.5.[1]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1259",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Justin Walker reports:

```
The only problem with the build is this, with readline:

Configured with: /var/tmp/gcc/gcc-5465~16/src/configure --disable-
checking -enable-werror --prefix=/usr --mandir=/share/man --enable-
languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/
$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/
lib --build=i686-apple-darwin9 --with-arch=apple --with-tune=generic  
--host=i686-apple-darwin9 --target=i686-apple-darwin9
Thread model: posix
gcc version 4.0.1 (Apple Inc. build 5465)
i686-apple-darwin9-gcc-4.0.1: -compatibility_version only allowed  
with -dynamiclib
i686-apple-darwin9-gcc-4.0.1: -compatibility_version only allowed  
with -dynamiclib
make[3]: *** [libreadline.5.2.dylib] Error 1
make[3]: *** Waiting for unfinished jobs....
make[3]: *** [libhistory.5.2.dylib] Error 1
make[2]: [install-shared] Error 2 (ignored)

FWIW, this same error crops up in a standalone build of readline, but  
it kills the build.  Sage seems to be unconcerned.
```


Issue created by migration from https://trac.sagemath.org/ticket/1259





---

archive/issue_comments_007850.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-25T04:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1259#issuecomment-7850",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007851.json:
```json
{
    "body": "The same issue applies to termcap. On 10.5 we end up with only static libraries.",
    "created_at": "2008-01-17T01:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1259#issuecomment-7851",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The same issue applies to termcap. On 10.5 we end up with only static libraries.



---

archive/issue_comments_007852.json:
```json
{
    "body": "Craig Citro says:\n\n```\nSince we're mentioning it, there's a known issue with the readline\nbuild on certain platforms, which you can spot by looking at your\ninstall.log at the section where readline gets installed. I don't know\nwhy these would be related, and Michael Abshoff is suspicious -- which\nprobably means I'm wrong :) -- but if I were motivated to look, I'd\nprobably start there. This is trac ticket #1259. It's easy to get the\nbuild problems to go away, but I'm not sure if it's the \"right\" way to\ndo so -- if you untar the readline package, go into src/support, and\nlook at shobj-conf. If you edit line 145 to say:\n\ndarwin[89]*)\n\nand line 174 to start with\n\n     darwin[789]*)\n\nthen it builds with no errors. However, if you look at what you're\ndoing, you're basically just telling the builder to use the same\noptions for 10.5 (which is what I assume Darwin9 is?) as it uses on\nDarwin 8. I have absolutely no idea whether or not that's a wise idea.\n\nOnce one does this, you could try rebuilding all of Sage with the new\nreadline package, and seeing if you get the same troubles.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-28T05:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1259#issuecomment-7852",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Craig Citro says:

```
Since we're mentioning it, there's a known issue with the readline
build on certain platforms, which you can spot by looking at your
install.log at the section where readline gets installed. I don't know
why these would be related, and Michael Abshoff is suspicious -- which
probably means I'm wrong :) -- but if I were motivated to look, I'd
probably start there. This is trac ticket #1259. It's easy to get the
build problems to go away, but I'm not sure if it's the "right" way to
do so -- if you untar the readline package, go into src/support, and
look at shobj-conf. If you edit line 145 to say:

darwin[89]*)

and line 174 to start with

     darwin[789]*)

then it builds with no errors. However, if you look at what you're
doing, you're basically just telling the builder to use the same
options for 10.5 (which is what I assume Darwin9 is?) as it uses on
Darwin 8. I have absolutely no idea whether or not that's a wise idea.

Once one does this, you could try rebuilding all of Sage with the new
readline package, and seeing if you get the same troubles.
```


Cheers,

Michael



---

archive/issue_comments_007853.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-02-24T01:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1259#issuecomment-7853",
    "user": "https://github.com/craigcitro"
}
```

Resolution: duplicate



---

archive/issue_comments_007854.json:
```json
{
    "body": "This is going to be fixed with #2282.",
    "created_at": "2008-02-24T01:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1259#issuecomment-7854",
    "user": "https://github.com/craigcitro"
}
```

This is going to be fixed with #2282.
