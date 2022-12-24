# Issue 8042: problem with modular symbols in eclib

archive/issues_008042.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  cremona\n\nKeywords: eclib modular symbols\n\n\n```\nE = EllipticCurve('858k2')\nfrom sage.libs.cremona.newforms import ECModularSymbol\nECModularSymbol(E)\n```\n\n\nproduces \n\n\n```\nFile \"newforms.pyx\", line 60, in sage.libs.cremona.newforms.ECModularSymbol.__init__ (sage/libs/cremona/newforms.cpp:1804)\nOverflowError: value too large to convert to int\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8042\n\n",
    "created_at": "2010-01-23T00:14:37Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "problem with modular symbols in eclib",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8042",
    "user": "wuthrich"
}
```
Assignee: craigcitro

CC:  cremona

Keywords: eclib modular symbols


```
E = EllipticCurve('858k2')
from sage.libs.cremona.newforms import ECModularSymbol
ECModularSymbol(E)
```


produces 


```
File "newforms.pyx", line 60, in sage.libs.cremona.newforms.ECModularSymbol.__init__ (sage/libs/cremona/newforms.cpp:1804)
OverflowError: value too large to convert to int
```


Issue created by migration from https://trac.sagemath.org/ticket/8042





---

archive/issue_comments_070279.json:
```json
{
    "body": "Well, I can tell you what's going wrong here, and ways to work around it -- but I'll wait until I'm more coherent to post a patch.\n\nHere's what's happening: despite the fact that you're on a 64-bit machine, C says `sizeof(int)` is still `4`. However, Python knows it's a 64-bit box, so Python's `int` type is now a full 64 bits. So in the bit of code you called, and in several places in the NTL interface, we convert from Python `int`s to C `int`s. That's the underlying problem: we really want to be using `long` in this case, because it actually has room to store the values we care about. The NTL `ZZ` constructor is more than happy to take a long as input, so there's also no problem there.\n\nThe easiest fix is just to switch the type of the constructor in `sage/libs/cremona/defs.pxi` ... here's a diff:\n\n```\ndiff -r 868098cc41e9 sage/libs/cremona/defs.pxi\n--- a/sage/libs/cremona/defs.pxi        Sat Jan 23 00:06:24 2010 -0800\n+++ b/sage/libs/cremona/defs.pxi        Sat Jan 23 00:18:48 2010 -0800\n@@ -1,7 +1,7 @@\n cdef extern from \"eclib/interface.h\":\n     ctypedef struct bigint:  #eclib uses NTL in Sage -- we call Cremona's \"bigint\" ZZ_c.\n         pass\n-    ZZ_c new_bigint \"to_ZZ\"(int)\n+    ZZ_c new_bigint \"to_ZZ\"(long)\n     int I2int(ZZ_c)\n \n cdef extern from \"eclib/bigrat.h\":\n```\n\nThat fixes the issue. \n\nHowever, I suspect that this is something that pops up elsewhere -- so I'd like to at least look a few other places and fix this issue there, too. For instance, we have exactly the same issue in the NTL interface ... and it's easy enough to fix there, too.",
    "created_at": "2010-01-23T08:23:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8042#issuecomment-70279",
    "user": "craigcitro"
}
```

Well, I can tell you what's going wrong here, and ways to work around it -- but I'll wait until I'm more coherent to post a patch.

Here's what's happening: despite the fact that you're on a 64-bit machine, C says `sizeof(int)` is still `4`. However, Python knows it's a 64-bit box, so Python's `int` type is now a full 64 bits. So in the bit of code you called, and in several places in the NTL interface, we convert from Python `int`s to C `int`s. That's the underlying problem: we really want to be using `long` in this case, because it actually has room to store the values we care about. The NTL `ZZ` constructor is more than happy to take a long as input, so there's also no problem there.

The easiest fix is just to switch the type of the constructor in `sage/libs/cremona/defs.pxi` ... here's a diff:

```
diff -r 868098cc41e9 sage/libs/cremona/defs.pxi
--- a/sage/libs/cremona/defs.pxi        Sat Jan 23 00:06:24 2010 -0800
+++ b/sage/libs/cremona/defs.pxi        Sat Jan 23 00:18:48 2010 -0800
@@ -1,7 +1,7 @@
 cdef extern from "eclib/interface.h":
     ctypedef struct bigint:  #eclib uses NTL in Sage -- we call Cremona's "bigint" ZZ_c.
         pass
-    ZZ_c new_bigint "to_ZZ"(int)
+    ZZ_c new_bigint "to_ZZ"(long)
     int I2int(ZZ_c)
 
 cdef extern from "eclib/bigrat.h":
```

That fixes the issue. 

However, I suspect that this is something that pops up elsewhere -- so I'd like to at least look a few other places and fix this issue there, too. For instance, we have exactly the same issue in the NTL interface ... and it's easy enough to fix there, too.



---

archive/issue_comments_070280.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-24T07:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8042#issuecomment-70280",
    "user": "craigcitro"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070281.json:
```json
{
    "body": "Okay, I'm attaching a patch that amounts to making the fix that I described above. I'm cheating a little bit, and I'm also making the fix in the NTL interface, too -- arguably that should be another ticket, but given that it's the same root problem, and that John's code also runs through NTL (but not the Sage NTL interface), I think it's sensible enough.",
    "created_at": "2010-01-24T07:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8042#issuecomment-70281",
    "user": "craigcitro"
}
```

Okay, I'm attaching a patch that amounts to making the fix that I described above. I'm cheating a little bit, and I'm also making the fix in the NTL interface, too -- arguably that should be another ticket, but given that it's the same root problem, and that John's code also runs through NTL (but not the Sage NTL interface), I think it's sensible enough.



---

archive/issue_comments_070282.json:
```json
{
    "body": "Attachment [trac-8042.patch](tarball://root/attachments/some-uuid/ticket8042/trac-8042.patch) by craigcitro created at 2010-01-24 07:43:10",
    "created_at": "2010-01-24T07:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8042#issuecomment-70282",
    "user": "craigcitro"
}
```

Attachment [trac-8042.patch](tarball://root/attachments/some-uuid/ticket8042/trac-8042.patch) by craigcitro created at 2010-01-24 07:43:10



---

archive/issue_comments_070283.json:
```json
{
    "body": "Thanks a lot for the quick resolution. I am glad that you picked this up so quickly for I would not have found this error myself.\n\nI will do the test and review this afternoon - even if, as a non-specialists in the ntl interface, I am maybe not the right person to do this review.",
    "created_at": "2010-01-24T13:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8042#issuecomment-70283",
    "user": "wuthrich"
}
```

Thanks a lot for the quick resolution. I am glad that you picked this up so quickly for I would not have found this error myself.

I will do the test and review this afternoon - even if, as a non-specialists in the ntl interface, I am maybe not the right person to do this review.



---

archive/issue_comments_070284.json:
```json
{
    "body": "For info:  the only reason that I use the name \"bigint\" in my code is that I allow (or used to allow) LiDIA integers as an alternative to NTL ones, and had a common interface which worked with both.  But Sage's build of eclib only ever uses the NTL ints.  So as far as Sage is concerned, my bigints are the same as NTL's ZZ: not a wrapper for them, but the exact same type.\n\nThis should surely make it easier to interface between eclib (and its bigints which are just NTL ZZs) and Sage.  There is quite a lot of useful stuff in eclib which Sage does not yet interface to, which is a pity (e.g. solution of conics over Q).",
    "created_at": "2010-01-24T13:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8042#issuecomment-70284",
    "user": "cremona"
}
```

For info:  the only reason that I use the name "bigint" in my code is that I allow (or used to allow) LiDIA integers as an alternative to NTL ones, and had a common interface which worked with both.  But Sage's build of eclib only ever uses the NTL ints.  So as far as Sage is concerned, my bigints are the same as NTL's ZZ: not a wrapper for them, but the exact same type.

This should surely make it easier to interface between eclib (and its bigints which are just NTL ZZs) and Sage.  There is quite a lot of useful stuff in eclib which Sage does not yet interface to, which is a pity (e.g. solution of conics over Q).



---

archive/issue_comments_070285.json:
```json
{
    "body": "All the tests pass. So I give it a positive review.",
    "created_at": "2010-01-24T15:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8042#issuecomment-70285",
    "user": "wuthrich"
}
```

All the tests pass. So I give it a positive review.



---

archive/issue_comments_070286.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-24T15:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8042#issuecomment-70286",
    "user": "wuthrich"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070287.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-24T18:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8042#issuecomment-70287",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_070288.json:
```json
{
    "body": "Hi John -- based on your comments above, maybe you should make a new enhancement ticket for changes you'd like to see to the Sage/eclib interface? Or would you actually want them made to eclib itself? (Do you actually ever build against LiDIA?) Even if it's just broad strokes, it would be good to have down -- I'm sure I'm not the only one who would be happy to look at it at some point.",
    "created_at": "2010-01-25T19:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8042#issuecomment-70288",
    "user": "craigcitro"
}
```

Hi John -- based on your comments above, maybe you should make a new enhancement ticket for changes you'd like to see to the Sage/eclib interface? Or would you actually want them made to eclib itself? (Do you actually ever build against LiDIA?) Even if it's just broad strokes, it would be good to have down -- I'm sure I'm not the only one who would be happy to look at it at some point.



---

archive/issue_comments_070289.json:
```json
{
    "body": "That sounds like a good idea.  At the moment I am putting in some bug fixes into mwrank (so, part of eclib, but not in facte relevant to modular symbols), and after that is done Robert Miller and I will be working on the sage/eclib interface anyway.  So a ticket to develop the sage/eclib interface would be good to have in place.\n\nRegarding LiDIA, in effect I no longer support it, and it would be possible to recode mwrank to avoid this dual support.  That would not, of course, be difficult, but it would also not add any functionality, so it's not a high priority for me.  But it would be good to do that before doing much to the sage/eclib interface, since surely that would be easier if all the ZZs actually looked like the ZZs they really are!",
    "created_at": "2010-01-26T09:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8042#issuecomment-70289",
    "user": "cremona"
}
```

That sounds like a good idea.  At the moment I am putting in some bug fixes into mwrank (so, part of eclib, but not in facte relevant to modular symbols), and after that is done Robert Miller and I will be working on the sage/eclib interface anyway.  So a ticket to develop the sage/eclib interface would be good to have in place.

Regarding LiDIA, in effect I no longer support it, and it would be possible to recode mwrank to avoid this dual support.  That would not, of course, be difficult, but it would also not add any functionality, so it's not a high priority for me.  But it would be good to do that before doing much to the sage/eclib interface, since surely that would be easier if all the ZZs actually looked like the ZZs they really are!
