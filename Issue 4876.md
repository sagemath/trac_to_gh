# Issue 4876: replace the two kash3 optional spkg's by a single optional spkg that works on both Linux and OS X, and gives a graceful message on other systems

archive/issues_004876.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4876\n\n",
    "created_at": "2008-12-24T19:55:15Z",
    "labels": [
        "packages",
        "major",
        "bug"
    ],
    "title": "replace the two kash3 optional spkg's by a single optional spkg that works on both Linux and OS X, and gives a graceful message on other systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4876",
    "user": "was"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/4876





---

archive/issue_comments_036917.json:
```json
{
    "body": "Also:\n* create an hg repo in the spkg\n* make the spkg-install script way more robust (more checks for error conditions)\n* put the SPKG.txt in the format described here: http://wiki.sagemath.org/SPKG_Audit",
    "created_at": "2008-12-24T20:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4876#issuecomment-36917",
    "user": "was"
}
```

Also:
* create an hg repo in the spkg
* make the spkg-install script way more robust (more checks for error conditions)
* put the SPKG.txt in the format described here: http://wiki.sagemath.org/SPKG_Audit



---

archive/issue_comments_036918.json:
```json
{
    "body": "To test this, you can do\n\n  sage -i http://sage.math.washington.edu/home/was/patches/kash3-2008-07-31.spkg\n\non both a linux and OS X box.  Then do \"sage -kash\" to see if it works.  Then look do \n\n```\ntar xf SAGE_ROOT/spkg/optional/kash3-2008-07-31.spkg\ncd kash3-2008-07-31\n# look around\n```\n",
    "created_at": "2008-12-24T20:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4876#issuecomment-36918",
    "user": "was"
}
```

To test this, you can do

  sage -i http://sage.math.washington.edu/home/was/patches/kash3-2008-07-31.spkg

on both a linux and OS X box.  Then do "sage -kash" to see if it works.  Then look do 

```
tar xf SAGE_ROOT/spkg/optional/kash3-2008-07-31.spkg
cd kash3-2008-07-31
# look around
```




---

archive/issue_comments_036919.json:
```json
{
    "body": "By the way, I checked and the OS X binary is \"universal\", in that it works on both PowerPC and Intel OS X 10.5 boxes.",
    "created_at": "2008-12-24T20:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4876#issuecomment-36919",
    "user": "was"
}
```

By the way, I checked and the OS X binary is "universal", in that it works on both PowerPC and Intel OS X 10.5 boxes.



---

archive/issue_comments_036920.json:
```json
{
    "body": "(This spkg won't work on itaniums correctly yet.  But it is still a massive improvement over the current kash spkg's.)",
    "created_at": "2008-12-24T20:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4876#issuecomment-36920",
    "user": "was"
}
```

(This spkg won't work on itaniums correctly yet.  But it is still a massive improvement over the current kash spkg's.)



---

archive/issue_comments_036921.json:
```json
{
    "body": "NOTE: I've already posted this to the package repo, so all this needs is an official review.  I posted this, since it's clearly better than the kash spkg I made 3 years ago, which was all that was there.",
    "created_at": "2008-12-24T20:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4876#issuecomment-36921",
    "user": "was"
}
```

NOTE: I've already posted this to the package repo, so all this needs is an official review.  I posted this, since it's clearly better than the kash spkg I made 3 years ago, which was all that was there.



---

archive/issue_comments_036922.json:
```json
{
    "body": "The package installed on Fedora 9 without problems.\n\nThe examples of\n\n[http://www.math.tu-berlin.de/~kant/KASH/pdf/kash3intro.pdf](http://www.math.tu-berlin.de/~kant/KASH/pdf/kash3intro.pdf)\n\nwork.\n\nLooks good to me (the linux binaries), I don't have a mac to test.\n\nJaap",
    "created_at": "2008-12-24T22:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4876#issuecomment-36922",
    "user": "jsp"
}
```

The package installed on Fedora 9 without problems.

The examples of

[http://www.math.tu-berlin.de/~kant/KASH/pdf/kash3intro.pdf](http://www.math.tu-berlin.de/~kant/KASH/pdf/kash3intro.pdf)

work.

Looks good to me (the linux binaries), I don't have a mac to test.

Jaap



---

archive/issue_comments_036923.json:
```json
{
    "body": "For the record: The spkg has already been uploaded to the optional spkg repo.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-26T17:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4876#issuecomment-36923",
    "user": "mabshoff"
}
```

For the record: The spkg has already been uploaded to the optional spkg repo.

Cheers,

Michael



---

archive/issue_comments_036924.json:
```json
{
    "body": "Ok, since no one has complained let's change this to a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-01T05:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4876#issuecomment-36924",
    "user": "mabshoff"
}
```

Ok, since no one has complained let's change this to a positive review.

Cheers,

Michael



---

archive/issue_comments_036925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-01T05:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4876#issuecomment-36925",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036926.json:
```json
{
    "body": "Merged in the Sage 3.4.1 release cycle (at least officially :))\n\nCheers,\n\nMichael",
    "created_at": "2009-04-01T05:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4876#issuecomment-36926",
    "user": "mabshoff"
}
```

Merged in the Sage 3.4.1 release cycle (at least officially :))

Cheers,

Michael



---

archive/issue_comments_036927.json:
```json
{
    "body": "Changing component from packages to optional packages.",
    "created_at": "2009-04-01T05:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4876#issuecomment-36927",
    "user": "mabshoff"
}
```

Changing component from packages to optional packages.
