# Issue 1649: [with patch and new spkg; with positive review] Updated eclib.spkg to  eclib-20071231.p0.spkg  or later

archive/issues_001649.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe new spkg can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/eclib-20071231.p0.spkg\n\nChangelog:\neclib-20071231.p0 (Michael Abshoff)\n* added Cygwin support\n* add spkg-check\n* install headers into $SAGE_LOCAL/eclib\n* delete $SAGE_LOCAL/include/cremona\n* chown $SAGE_LOCAL/include/eclib and files underneath\n\neclib-20071231 (John Cremona):\n* renamed to eclib\n* allows elliptic curves as input with rational (as opposed to just integer) coefficients.\n\nThis spkg still needs fixes to `mwrank.pyx` [expect a patch shortly] and is related to #1058.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1649\n\n",
    "closed_at": "2008-01-27T20:20:33Z",
    "created_at": "2007-12-31T23:59:03Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch and new spkg; with positive review] Updated eclib.spkg to  eclib-20071231.p0.spkg  or later",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1649",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The new spkg can be found at

http://sage.math.washington.edu/home/mabshoff/eclib-20071231.p0.spkg

Changelog:
eclib-20071231.p0 (Michael Abshoff)
* added Cygwin support
* add spkg-check
* install headers into $SAGE_LOCAL/eclib
* delete $SAGE_LOCAL/include/cremona
* chown $SAGE_LOCAL/include/eclib and files underneath

eclib-20071231 (John Cremona):
* renamed to eclib
* allows elliptic curves as input with rational (as opposed to just integer) coefficients.

This spkg still needs fixes to `mwrank.pyx` [expect a patch shortly] and is related to #1058.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1649





---

archive/issue_comments_010459.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-01T00:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010460.json:
```json
{
    "body": "I misunderstood John and the old interface no longer works. I had assumed that we needed to enhance the interface to take advantage of the new capabilities:\n\n```\ncc1plus: warning: command line option \"-Wstrict-prototypes\" is valid for Ada/C/ObjC but not for C++\nsage/libs/mwrank/wrap.cc: In function \u2018char* two_descent_getbasis(two_descent*)\u2019:\nsage/libs/mwrank/wrap.cc:246: error: invalid initialization of reference of type \u2018const std::vector<Point, std::allocator<Point> >&\u2019 from expression of type \u2018std::vector<P2Point, std::allocator<P2Point> >\u2019\nsage/libs/mwrank/wrap.cc:159: error: in passing argument 1 of \u2018char* point_vector_to_str(const std::vector<Point, std::allocator<Point> >&)\u2019\nerror: command 'gcc' failed with exit status 1\n```\n\nI haven't investigated how much effort it will be to fix this, but since there are more pressing bugs to fix for me I will step back and hope that somebody else will fix this.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-01T02:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10460",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I misunderstood John and the old interface no longer works. I had assumed that we needed to enhance the interface to take advantage of the new capabilities:

```
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
sage/libs/mwrank/wrap.cc: In function ‘char* two_descent_getbasis(two_descent*)’:
sage/libs/mwrank/wrap.cc:246: error: invalid initialization of reference of type ‘const std::vector<Point, std::allocator<Point> >&’ from expression of type ‘std::vector<P2Point, std::allocator<P2Point> >’
sage/libs/mwrank/wrap.cc:159: error: in passing argument 1 of ‘char* point_vector_to_str(const std::vector<Point, std::allocator<Point> >&)’
error: command 'gcc' failed with exit status 1
```

I haven't investigated how much effort it will be to fix this, but since there are more pressing bugs to fix for me I will step back and hope that somebody else will fix this.

Cheers,

Michael



---

archive/issue_comments_010461.json:
```json
{
    "body": "In http://groups.google.com/group/sage-devel/t/1b3e097ee29e7cf6 John has posted a link to an updated eclib.spkg at\n\nhttp://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20071231.p1.spkg\n\nTo quote:\n\n```\nThis version, which builds on mabshoff's eclib-20071231.p0.spkg,\nhandles the interface with NTL's ZZ_p class better (using a cached\nlist of ZZ_pContext's for those who know NTL) which should certailny\nbe a lot more efficient, and might even solve the problems people had\ntrying to compile this with gcc-4.3 (which I do not have).\n\nSince other parts of Sage use the ZZ_p class it might be worth using\nwhat I did here (in src/procs/gf.{h,cc}) elsewhere too.  I have a\nglobal object of type map<ZZ,ZZ_pContext> consisting of an in\ninitially empty list of pairs [p,c] where p is a prime and c is a\nZZ_pContext which stores the internal NTL data for working mod p.\nWhen I need to switch to a new modulus, instead of just calling\nZZ_p::init() each time (which was happening a lot of times for the\nsame p in programs such as mwrank), I look to see if that p has a\nsaved context and if so just restore it.  If not, is do ZZ_p::init and\nthen save the context.  So each prime only gets init'ed once.\n\nIt is possible that this will have solved other mysterious problems,\nsince the NTL documention (see http://www.shoup.net/ntl/doc/ZZ_p.txt)\nsays\n\n\"One should also not presume that things will work properly\nif the modulus is changed, but its value happens to be the same---\none should restore the same \"context\", from either a ZZ_pBak\nor a ZZ_pContext object.\"\n\nUp to now I *had* been making such a presumption.\n\nIt is still true that this spkg will not build correctly in Sage 2.9.1\n(or even 2.9.2) since there is a small change to the interface which\nrequires a similar small change to the wrapping code, but this has\nbeen put off at least until after the AMS meeting.  But it should\nbuild fine as a stand-alone package.\n\nJohn \n```\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T12:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10461",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

In http://groups.google.com/group/sage-devel/t/1b3e097ee29e7cf6 John has posted a link to an updated eclib.spkg at

http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20071231.p1.spkg

To quote:

```
This version, which builds on mabshoff's eclib-20071231.p0.spkg,
handles the interface with NTL's ZZ_p class better (using a cached
list of ZZ_pContext's for those who know NTL) which should certailny
be a lot more efficient, and might even solve the problems people had
trying to compile this with gcc-4.3 (which I do not have).

Since other parts of Sage use the ZZ_p class it might be worth using
what I did here (in src/procs/gf.{h,cc}) elsewhere too.  I have a
global object of type map<ZZ,ZZ_pContext> consisting of an in
initially empty list of pairs [p,c] where p is a prime and c is a
ZZ_pContext which stores the internal NTL data for working mod p.
When I need to switch to a new modulus, instead of just calling
ZZ_p::init() each time (which was happening a lot of times for the
same p in programs such as mwrank), I look to see if that p has a
saved context and if so just restore it.  If not, is do ZZ_p::init and
then save the context.  So each prime only gets init'ed once.

It is possible that this will have solved other mysterious problems,
since the NTL documention (see http://www.shoup.net/ntl/doc/ZZ_p.txt)
says

"One should also not presume that things will work properly
if the modulus is changed, but its value happens to be the same---
one should restore the same "context", from either a ZZ_pBak
or a ZZ_pContext object."

Up to now I *had* been making such a presumption.

It is still true that this spkg will not build correctly in Sage 2.9.1
(or even 2.9.2) since there is a small change to the interface which
requires a similar small change to the wrapping code, but this has
been put off at least until after the AMS meeting.  But it should
build fine as a stand-alone package.

John 
```

Cheers,

Michael



---

archive/issue_comments_010462.json:
```json
{
    "body": "This spkg should also fix #1650.",
    "created_at": "2008-01-27T03:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10462",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This spkg should also fix #1650.



---

archive/issue_comments_010463.json:
```json
{
    "body": "Note that an updated spkg by William is at #1650 that fixes the OSX build issue I introduced by fixing the Cygwin build :(\n\nCheers,\n\nMichael",
    "created_at": "2008-01-27T18:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10463",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Note that an updated spkg by William is at #1650 that fixes the OSX build issue I introduced by fixing the Cygwin build :(

Cheers,

Michael



---

archive/issue_comments_010464.json:
```json
{
    "body": "Attachment [trac-1649-update_mwrank_wrapper.patch](tarball://root/attachments/some-uuid/ticket1649/trac-1649-update_mwrank_wrapper.patch) by @williamstein created at 2008-01-27 19:16:04",
    "created_at": "2008-01-27T19:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10464",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1649-update_mwrank_wrapper.patch](tarball://root/attachments/some-uuid/ticket1649/trac-1649-update_mwrank_wrapper.patch) by @williamstein created at 2008-01-27 19:16:04



---

archive/issue_comments_010465.json:
```json
{
    "body": "I wrote \"needs review\", but I've run the doctests and all pass, and Cremona and\nI just worked on this together, so it's had two eyes.",
    "created_at": "2008-01-27T19:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10465",
    "user": "https://github.com/williamstein"
}
```

I wrote "needs review", but I've run the doctests and all pass, and Cremona and
I just worked on this together, so it's had two eyes.



---

archive/issue_comments_010466.json:
```json
{
    "body": "Patch looks good to me. The spkg from #1650 was merged.",
    "created_at": "2008-01-27T19:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10466",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. The spkg from #1650 was merged.



---

archive/issue_comments_010467.json:
```json
{
    "body": "Attachment [1649-part2.patch](tarball://root/attachments/some-uuid/ticket1649/1649-part2.patch) by @williamstein created at 2008-01-27 20:09:44",
    "created_at": "2008-01-27T20:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10467",
    "user": "https://github.com/williamstein"
}
```

Attachment [1649-part2.patch](tarball://root/attachments/some-uuid/ticket1649/1649-part2.patch) by @williamstein created at 2008-01-27 20:09:44



---

archive/issue_comments_010468.json:
```json
{
    "body": "The second patch looks good to me, too. I am doing a `sage -ba` to make sure everything still compiles.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-27T20:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10468",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The second patch looks good to me, too. I am doing a `sage -ba` to make sure everything still compiles.

Cheers,

Michael



---

archive/issue_comments_010469.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc2",
    "created_at": "2008-01-27T20:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10469",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc2



---

archive/issue_events_004080.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-27T20:20:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1649#event-4080"
}
```



---

archive/issue_comments_010470.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T20:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1649#issuecomment-10470",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
