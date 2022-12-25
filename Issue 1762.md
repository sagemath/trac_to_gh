# Issue 1762: Create optional graphviz package

archive/issues_001762.json:
```json
{
    "body": "Assignee: @rlmill\n\nGraphviz is licensed under the Common Public License Version 1.0, which is incompatible with the GPL. ([see wikipedia](http://en.wikipedia.org/wiki/Common_Public_License))  So, we can't distribute graphviz packaged with Sage, but we can distribute it separately.\n\nThe dependencies are rather numerous, but most are optional. Of note, GD and libpng are already included in Sage. [http://www.graphviz.org/doc/build.html](http://www.graphviz.org/doc/build.html)\n\nIssue created by migration from https://trac.sagemath.org/ticket/1762\n\n",
    "created_at": "2008-01-12T04:42:08Z",
    "labels": [
        "component: graph theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Create optional graphviz package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1762",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: @rlmill

Graphviz is licensed under the Common Public License Version 1.0, which is incompatible with the GPL. ([see wikipedia](http://en.wikipedia.org/wiki/Common_Public_License))  So, we can't distribute graphviz packaged with Sage, but we can distribute it separately.

The dependencies are rather numerous, but most are optional. Of note, GD and libpng are already included in Sage. [http://www.graphviz.org/doc/build.html](http://www.graphviz.org/doc/build.html)

Issue created by migration from https://trac.sagemath.org/ticket/1762





---

archive/issue_comments_011095.json:
```json
{
    "body": "Here is a broken spkg:\n\nhttp://sage.math.washington.edu/home/rlmill/graphviz-broken-2.16.1.spkg\n\nIt fails to find the libpng library, because it is looking for `libpng12.dylib`, and the files are `libpng12.la` and `libpng12.a` instead. I bet there are more problems with the spkg, too, besides just missing an SPKG.txt. But this gets the ball rolling...",
    "created_at": "2008-01-19T01:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1762#issuecomment-11095",
    "user": "https://github.com/rlmill"
}
```

Here is a broken spkg:

http://sage.math.washington.edu/home/rlmill/graphviz-broken-2.16.1.spkg

It fails to find the libpng library, because it is looking for `libpng12.dylib`, and the files are `libpng12.la` and `libpng12.a` instead. I bet there are more problems with the spkg, too, besides just missing an SPKG.txt. But this gets the ball rolling...



---

archive/issue_comments_011096.json:
```json
{
    "body": "I will look into this tomorrow. The problem that needs to be solved is autoconf.ac or something alike. I also think that the issue we need to solve is making python work with out libpng.dylib on 10.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-19T04:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1762#issuecomment-11096",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will look into this tomorrow. The problem that needs to be solved is autoconf.ac or something alike. I also think that the issue we need to solve is making python work with out libpng.dylib on 10.4.

Cheers,

Michael



---

archive/issue_comments_011097.json:
```json
{
    "body": "Some comments:\n\n1. On lines 106-110 of `configure.ac`, they basically assume that .dylib is the only type of library name. Who knows where else this kind of assumption will cause trouble...\n\n2. They use this on lines 351-353 of\n\nhttp://www.graphviz.org/pub/graphviz/CURRENT/doxygen/html/gvconfig_8c-source.html\n\n3. The variable name \"DARWIN_DYLIB\" is used only by graphviz- don't be fooled!\n\n4. Seems like a fix that should go upstream...",
    "created_at": "2008-01-19T05:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1762#issuecomment-11097",
    "user": "https://github.com/rlmill"
}
```

Some comments:

1. On lines 106-110 of `configure.ac`, they basically assume that .dylib is the only type of library name. Who knows where else this kind of assumption will cause trouble...

2. They use this on lines 351-353 of

http://www.graphviz.org/pub/graphviz/CURRENT/doxygen/html/gvconfig_8c-source.html

3. The variable name "DARWIN_DYLIB" is used only by graphviz- don't be fooled!

4. Seems like a fix that should go upstream...



---

archive/issue_comments_011098.json:
```json
{
    "body": "Yeah, forgot about the existence of:\n\nhttps://networkx.lanl.gov/wiki/pygraphviz",
    "created_at": "2008-01-19T21:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1762#issuecomment-11098",
    "user": "https://github.com/rlmill"
}
```

Yeah, forgot about the existence of:

https://networkx.lanl.gov/wiki/pygraphviz



---

archive/issue_comments_011099.json:
```json
{
    "body": "Oh, but pygraphviz still depends on graphviz...",
    "created_at": "2008-01-19T21:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1762#issuecomment-11099",
    "user": "https://github.com/rlmill"
}
```

Oh, but pygraphviz still depends on graphviz...



---

archive/issue_comments_011100.json:
```json
{
    "body": "As an alternate solution, I've found a package called OGDF -- a GPL2/3 C++ package for drawing graphs:\n\nhttp://www.ogdf.net/\n\nthis will take more work to wrap, but ultimately solves the problem better.",
    "created_at": "2008-03-17T17:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1762#issuecomment-11100",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

As an alternate solution, I've found a package called OGDF -- a GPL2/3 C++ package for drawing graphs:

http://www.ogdf.net/

this will take more work to wrap, but ultimately solves the problem better.



---

archive/issue_comments_011101.json:
```json
{
    "body": "I am fixing all the issue I am seeing. #3274 fixes the OSX compile, so we ought to be good.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-23T00:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1762#issuecomment-11101",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am fixing all the issue I am seeing. #3274 fixes the OSX compile, so we ought to be good.

Cheers,

Michael



---

archive/issue_comments_011102.json:
```json
{
    "body": "this patch fixes the OSX build issue",
    "created_at": "2008-05-23T00:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1762#issuecomment-11102",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

this patch fixes the OSX build issue



---

archive/issue_comments_011103.json:
```json
{
    "body": "Attachment [trac_1762_cleanup.patch](tarball://root/attachments/some-uuid/ticket1762/trac_1762_cleanup.patch) by mabshoff created at 2008-05-23 01:09:46\n\nThe updated optional spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2//rc0/graphviz-2.16.1.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-05-23T01:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1762#issuecomment-11103",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_1762_cleanup.patch](tarball://root/attachments/some-uuid/ticket1762/trac_1762_cleanup.patch) by mabshoff created at 2008-05-23 01:09:46

The updated optional spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2//rc0/graphviz-2.16.1.p0.spkg

Cheers,

Michael



---

archive/issue_comments_011104.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-23T01:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1762#issuecomment-11104",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001920.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-23T01:41:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1762#event-1920"
}
```



---

archive/issue_comments_011105.json:
```json
{
    "body": "The spkg has been uploaded to the optional spkg repo.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-23T01:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1762#issuecomment-11105",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg has been uploaded to the optional spkg repo.

Cheers,

Michael
