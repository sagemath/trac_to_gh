# Issue 6032: split boost-1.34.1.cropped off the polybori.spkg

archive/issues_006032.json:
```json
{
    "body": "Assignee: mabshoff\n\nTo make it easier to update boost it should be split off the polybori.spkg. Some time in the future we should also update to a more current release. \n\nNote the following should be added to SPKG.txt since it makes the creation of the cropped boost automatic:\n\n```\nextract BoRing.tar.gz in src\nextract boost-jam-3.1.14.tar.gz in src\ncopy cropped boost to src/boost_${BOOST_VER}.cropped\n\tcreate cropped boost with\n\tbcp --boost=boost_1_34_1 --scan PolyBoRi/M4RI/* PolyBoRi/polybori/include/* PolyBoRi/groebner/src/* PolyBoRi/PyPolyBoRi/* ../boost/t/boost_new/\n\n\tboost build subset\n\ttar jcvf boost.build.crop.tar.bz2 tools/build/v2/{kernel,util,build,tools,*.jam} boost-build.jam project-root.jam Jamfile.v2 Jamrules\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6032\n\n",
    "created_at": "2009-05-12T18:11:48Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "split boost-1.34.1.cropped off the polybori.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6032",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

To make it easier to update boost it should be split off the polybori.spkg. Some time in the future we should also update to a more current release. 

Note the following should be added to SPKG.txt since it makes the creation of the cropped boost automatic:

```
extract BoRing.tar.gz in src
extract boost-jam-3.1.14.tar.gz in src
copy cropped boost to src/boost_${BOOST_VER}.cropped
	create cropped boost with
	bcp --boost=boost_1_34_1 --scan PolyBoRi/M4RI/* PolyBoRi/polybori/include/* PolyBoRi/groebner/src/* PolyBoRi/PyPolyBoRi/* ../boost/t/boost_new/

	boost build subset
	tar jcvf boost.build.crop.tar.bz2 tools/build/v2/{kernel,util,build,tools,*.jam} boost-build.jam project-root.jam Jamfile.v2 Jamrules
```


Issue created by migration from https://trac.sagemath.org/ticket/6032





---

archive/issue_comments_047935.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-12T18:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6032#issuecomment-47935",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047936.json:
```json
{
    "body": "Two spkgs are at\n\n* http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/boost-cropped-1.34.1.spkg\n* http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/polybori-0.5rc.p7.spkg\n\nYou also need to apply the patches for install and deps.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T12:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6032#issuecomment-47936",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Two spkgs are at

* http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/boost-cropped-1.34.1.spkg
* http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/polybori-0.5rc.p7.spkg

You also need to apply the patches for install and deps.

Cheers,

Michael



---

archive/issue_comments_047937.json:
```json
{
    "body": "Attachment [install-boost-cropped.patch](tarball://root/attachments/some-uuid/ticket6032/install-boost-cropped.patch) by mabshoff created at 2009-05-15 12:42:53",
    "created_at": "2009-05-15T12:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6032#issuecomment-47937",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [install-boost-cropped.patch](tarball://root/attachments/some-uuid/ticket6032/install-boost-cropped.patch) by mabshoff created at 2009-05-15 12:42:53



---

archive/issue_comments_047938.json:
```json
{
    "body": "Attachment [deps-boost-cropped.patch](tarball://root/attachments/some-uuid/ticket6032/deps-boost-cropped.patch) by mabshoff created at 2009-05-15 12:42:59",
    "created_at": "2009-05-15T12:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6032#issuecomment-47938",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [deps-boost-cropped.patch](tarball://root/attachments/some-uuid/ticket6032/deps-boost-cropped.patch) by mabshoff created at 2009-05-15 12:42:59



---

archive/issue_comments_047939.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-05-15T20:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6032#issuecomment-47939",
    "user": "https://github.com/malb"
}
```

Looks good.



---

archive/issue_comments_047940.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-16T00:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6032#issuecomment-47940",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_014169.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-16T00:21:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6032",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6032#event-14169"
}
```



---

archive/issue_comments_047941.json:
```json
{
    "body": "Merged both spkgs and both patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-16T00:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6032#issuecomment-47941",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both spkgs and both patches in Sage 4.0.alpha0.

Cheers,

Michael
