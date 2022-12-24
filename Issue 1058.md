# Issue 1058: the mwrank interface barfs on bad input

archive/issues_001058.json:
```json
{
    "body": "Assignee: was\n\nKeywords: mwrank\n\nIf give mwrank any invalid input, the running process quits, and you get a pexpect error, since Sage never restarts mwrank:\n\n# the a-list needs to be all integers\nsage: E = EllipticCurve( [0, 0, 0, 0, -675/4])\nsage: E.rank()\nException (click to the left for traceback):\n...\n# this should be valid\nsage: F = EllipticCurve( [0, 0, 1, 0, -169])\n# ... but calling mwrank again makes everything fail\nsage: F.rank()\nException (click to the left for traceback):\n...\n\nIssue created by migration from https://trac.sagemath.org/ticket/1058\n\n",
    "created_at": "2007-11-02T00:17:02Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "the mwrank interface barfs on bad input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1058",
    "user": "moretti"
}
```
Assignee: was

Keywords: mwrank

If give mwrank any invalid input, the running process quits, and you get a pexpect error, since Sage never restarts mwrank:

# the a-list needs to be all integers
sage: E = EllipticCurve( [0, 0, 0, 0, -675/4])
sage: E.rank()
Exception (click to the left for traceback):
...
# this should be valid
sage: F = EllipticCurve( [0, 0, 1, 0, -169])
# ... but calling mwrank again makes everything fail
sage: F.rank()
Exception (click to the left for traceback):
...

Issue created by migration from https://trac.sagemath.org/ticket/1058





---

archive/issue_comments_006431.json:
```json
{
    "body": "Changing assignee from was to moretti.",
    "created_at": "2007-11-02T00:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1058#issuecomment-6431",
    "user": "moretti"
}
```

Changing assignee from was to moretti.



---

archive/issue_comments_006432.json:
```json
{
    "body": "Changing assignee from moretti to cremona.",
    "created_at": "2007-11-21T10:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1058#issuecomment-6432",
    "user": "cremona"
}
```

Changing assignee from moretti to cremona.



---

archive/issue_comments_006433.json:
```json
{
    "body": "There are two separate things here.\n\nFirst:  it would be entirely reasonable to expect mwrank to allow rational input and not just integer.  At the moment (2007-11-21) that is not supported, but it could be, and I hope to add that functionality when sorting out the more serious #1233.\n\nSecond:  The wrapper which sends elliptic curves to mwrank attempts to coerce the coefficients to ints.  (This is what causes the above examples to fail).  But it also seems to have some silly (though documented) side-effects, such as \n\n```\nmwrank_EllipticCurve([1.2,3.4])\ny^2 = x^3 + x + 3\n```\n\nwhere the floating point inputs have been rounded down.  This behaviour has no conceivable use, so I would suggest changing the wrapper to require the inputs to be rational.",
    "created_at": "2007-11-21T10:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1058#issuecomment-6433",
    "user": "cremona"
}
```

There are two separate things here.

First:  it would be entirely reasonable to expect mwrank to allow rational input and not just integer.  At the moment (2007-11-21) that is not supported, but it could be, and I hope to add that functionality when sorting out the more serious #1233.

Second:  The wrapper which sends elliptic curves to mwrank attempts to coerce the coefficients to ints.  (This is what causes the above examples to fail).  But it also seems to have some silly (though documented) side-effects, such as 

```
mwrank_EllipticCurve([1.2,3.4])
y^2 = x^3 + x + 3
```

where the floating point inputs have been rounded down.  This behaviour has no conceivable use, so I would suggest changing the wrapper to require the inputs to be rational.



---

archive/issue_comments_006434.json:
```json
{
    "body": "eclib-20071231.spkg  is an updated version of cremona*.spkg which allows elliptic curves as input with rational (as opposed to just integer) coefficients.\n\nThe Sage interface to the library functions for mwrank (etc) will need to be adapted to handle this.  I expect that is best done as part of the complete rewrite of the Sage-mwrank interface which WAS recently mentioned as desirable.\n\nThe new package may be downloaded from http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20071231.spkg\n\nJohn Cremona",
    "created_at": "2007-12-31T16:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1058#issuecomment-6434",
    "user": "cremona"
}
```

eclib-20071231.spkg  is an updated version of cremona*.spkg which allows elliptic curves as input with rational (as opposed to just integer) coefficients.

The Sage interface to the library functions for mwrank (etc) will need to be adapted to handle this.  I expect that is best done as part of the complete rewrite of the Sage-mwrank interface which WAS recently mentioned as desirable.

The new package may be downloaded from http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20071231.spkg

John Cremona



---

archive/issue_comments_006435.json:
```json
{
    "body": "I am looking into this. The upgrade will be non-trivial since we potentially need to delete old headers, fix some includes in the interface and so on. But I think it will be merged in 2.9.2.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-31T17:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1058#issuecomment-6435",
    "user": "mabshoff"
}
```

I am looking into this. The upgrade will be non-trivial since we potentially need to delete old headers, fix some includes in the interface and so on. But I think it will be merged in 2.9.2.

Cheers,

Michael



---

archive/issue_comments_006436.json:
```json
{
    "body": "An updated eclib.spkg can be found at:\n\nhttp://sage.math.washington.edu/home/mabshoff/eclib-20071231.p0.spkg\n\nChangelog:\n\n* added Cygwin support\n* add spkg-check\n* install headers into $SAGE_LOCAL/eclib\n* delete $SAGE_LOCAL/include/cremona\n* chown $SAGE_LOCAL/include/eclib and files underneath\n\nThis spkg breaks compilation of `mwrank.pyx` for now, expect a patch shortly. Since the Sage interface needs updates I split the spkg update off to #1649. \n\nCheers,\n\nMichael",
    "created_at": "2008-01-01T00:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1058#issuecomment-6436",
    "user": "mabshoff"
}
```

An updated eclib.spkg can be found at:

http://sage.math.washington.edu/home/mabshoff/eclib-20071231.p0.spkg

Changelog:

* added Cygwin support
* add spkg-check
* install headers into $SAGE_LOCAL/eclib
* delete $SAGE_LOCAL/include/cremona
* chown $SAGE_LOCAL/include/eclib and files underneath

This spkg breaks compilation of `mwrank.pyx` for now, expect a patch shortly. Since the Sage interface needs updates I split the spkg update off to #1649. 

Cheers,

Michael



---

archive/issue_comments_006437.json:
```json
{
    "body": "Ok, I tried fixing the interface problems, but it isn't as simple as I thought.\n\nGiving up for now, I need to fix other, more urgent bugs for this release cycle.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-02T08:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1058#issuecomment-6437",
    "user": "mabshoff"
}
```

Ok, I tried fixing the interface problems, but it isn't as simple as I thought.

Giving up for now, I need to fix other, more urgent bugs for this release cycle.

Cheers,

Michael



---

archive/issue_comments_006438.json:
```json
{
    "body": "Attachment [trac-1058.patch](tarball://root/attachments/some-uuid/ticket1058/trac-1058.patch) by was created at 2008-01-27 19:31:27",
    "created_at": "2008-01-27T19:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1058#issuecomment-6438",
    "user": "was"
}
```

Attachment [trac-1058.patch](tarball://root/attachments/some-uuid/ticket1058/trac-1058.patch) by was created at 2008-01-27 19:31:27



---

archive/issue_comments_006439.json:
```json
{
    "body": "Patch passes doctests. Note that the patch needs the updated eclib.spkg and the patches from #1649 to work. Second Positive review.",
    "created_at": "2008-01-27T20:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1058#issuecomment-6439",
    "user": "mabshoff"
}
```

Patch passes doctests. Note that the patch needs the updated eclib.spkg and the patches from #1649 to work. Second Positive review.



---

archive/issue_comments_006440.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T20:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1058#issuecomment-6440",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006441.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc2",
    "created_at": "2008-01-27T20:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1058#issuecomment-6441",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc2
