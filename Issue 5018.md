# Issue 5018: lrs optional package improvements

archive/issues_005018.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: lrs, polyhedra, polytopes\n\nIn order to move the lrs package closer to being included as a standard package, I have added a couple of tests to the makefile.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5018\n\n",
    "created_at": "2009-01-18T20:22:03Z",
    "labels": [
        "packages: optional",
        "minor",
        "enhancement"
    ],
    "title": "lrs optional package improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5018",
    "user": "mhampton"
}
```
Assignee: mabshoff

Keywords: lrs, polyhedra, polytopes

In order to move the lrs package closer to being included as a standard package, I have added a couple of tests to the makefile.

Issue created by migration from https://trac.sagemath.org/ticket/5018





---

archive/issue_comments_038230.json:
```json
{
    "body": "My current candidate is at:\nhttp://sage.math.washington.edu/home/mhampton/lrs-4.2b.p1.spkg",
    "created_at": "2009-01-18T20:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5018#issuecomment-38230",
    "user": "mhampton"
}
```

My current candidate is at:
http://sage.math.washington.edu/home/mhampton/lrs-4.2b.p1.spkg



---

archive/issue_comments_038231.json:
```json
{
    "body": "A couple remarks:\n\n* the spkg is missing an hg repo. Please check in everything but src\n* SPKG.txt does not conform to the standard - see the SpkgTemplate in the wiki \n* spkg-install needs to be executable\n* spkg-check is missing, when you add it please run `make check` with it\n* for the make check target: create foo.expected and direct the result from test foo into foo.result. Then diff, i.e. do not create the expected result in the script\n* the makefile should have a make install target\n* the makefile still uses `gcc -O3 -static` - this should be set via CC and CFLAGS for example\n\nNot all of the above have to be fixed to get a positive review from me, but it would be nice to get those all fixed. The missing hg repo and an updated SPKG.txt should *really* be done.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T01:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5018#issuecomment-38231",
    "user": "mabshoff"
}
```

A couple remarks:

* the spkg is missing an hg repo. Please check in everything but src
* SPKG.txt does not conform to the standard - see the SpkgTemplate in the wiki 
* spkg-install needs to be executable
* spkg-check is missing, when you add it please run `make check` with it
* for the make check target: create foo.expected and direct the result from test foo into foo.result. Then diff, i.e. do not create the expected result in the script
* the makefile should have a make install target
* the makefile still uses `gcc -O3 -static` - this should be set via CC and CFLAGS for example

Not all of the above have to be fixed to get a positive review from me, but it would be nice to get those all fixed. The missing hg repo and an updated SPKG.txt should *really* be done.

Cheers,

Michael



---

archive/issue_comments_038232.json:
```json
{
    "body": "I think I have addressed the concerns above, except that I did not add the CC and CFLAGS macros, because I was not sure how to do that for all the compilation cases in the makefile.  The updated version is that the same link as before.",
    "created_at": "2009-01-19T04:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5018#issuecomment-38232",
    "user": "mhampton"
}
```

I think I have addressed the concerns above, except that I did not add the CC and CFLAGS macros, because I was not sure how to do that for all the compilation cases in the makefile.  The updated version is that the same link as before.



---

archive/issue_comments_038233.json:
```json
{
    "body": "This spkg is enough of an improvement to warrant a positive review. Much remains to be done, but this can be addressed via subsequent spkgs.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T06:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5018#issuecomment-38233",
    "user": "mabshoff"
}
```

This spkg is enough of an improvement to warrant a positive review. Much remains to be done, but this can be addressed via subsequent spkgs.

Cheers,

Michael



---

archive/issue_comments_038234.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T06:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5018#issuecomment-38234",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038235.json:
```json
{
    "body": "Uploaded in the optional spkg repo in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T06:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5018#issuecomment-38235",
    "user": "mabshoff"
}
```

Uploaded in the optional spkg repo in Sage 3.3.alpha4.

Cheers,

Michael
