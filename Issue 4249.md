# Issue 4249: Inconsistency in number field integral bases

archive/issues_004249.json:
```json
{
    "body": "Assignee: was\n\nCC:  \"maite aranes\" <m.t.aranes@warwick.ac.uk>\n\nKeywords: number fields\n\nThis is unacceptable (in  my opinion):\n\n```\nsage: K.<a>=NumberField(x^2+23)\nsage: K.integral_basis()\n[1, 1/2*a + 1/2]\nsage: K.ring_of_integers().basis()\n[1/2*a + 1/2, a]\n```\n\n\nI think these should be the same.  The problem is that K.integral_basis() gets the basis from pari, but when the ring_of_integers is constructed it uses that basis in the constructions but then creates its own, different, basis!\n\nSuggested solution:  make the existing integral_basis() function an internal one used by the ring_of_integers() function only, and have K.integra_basis() return the basis of the ring of integers instead.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4249\n\n",
    "created_at": "2008-10-07T11:21:35Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Inconsistency in number field integral bases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4249",
    "user": "cremona"
}
```
Assignee: was

CC:  "maite aranes" <m.t.aranes@warwick.ac.uk>

Keywords: number fields

This is unacceptable (in  my opinion):

```
sage: K.<a>=NumberField(x^2+23)
sage: K.integral_basis()
[1, 1/2*a + 1/2]
sage: K.ring_of_integers().basis()
[1/2*a + 1/2, a]
```


I think these should be the same.  The problem is that K.integral_basis() gets the basis from pari, but when the ring_of_integers is constructed it uses that basis in the constructions but then creates its own, different, basis!

Suggested solution:  make the existing integral_basis() function an internal one used by the ring_of_integers() function only, and have K.integra_basis() return the basis of the ring of integers instead.

Issue created by migration from https://trac.sagemath.org/ticket/4249





---

archive/issue_comments_030888.json:
```json
{
    "body": "I strongly agree with John Cremona's suggested fix.",
    "created_at": "2008-10-08T04:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30888",
    "user": "was"
}
```

I strongly agree with John Cremona's suggested fix.



---

archive/issue_comments_030889.json:
```json
{
    "body": "Attachment [sage-4249.patch](tarball://root/attachments/some-uuid/ticket4249/sage-4249.patch) by cremona created at 2008-10-14 20:46:43",
    "created_at": "2008-10-14T20:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30889",
    "user": "cremona"
}
```

Attachment [sage-4249.patch](tarball://root/attachments/some-uuid/ticket4249/sage-4249.patch) by cremona created at 2008-10-14 20:46:43



---

archive/issue_comments_030890.json:
```json
{
    "body": "The attached patch (which applies to 3.1.3) does what was proposed.  All doctests in sage/rings/number_fields/ pass *except* for a couple in totallyreal_rel.py where one of the totally real quadratic extensions of Q(sqrt(5)) is now missing.  I do not know why but suggest that there might be a bug in that file, so will ask John Voight to look into it.",
    "created_at": "2008-10-14T20:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30890",
    "user": "cremona"
}
```

The attached patch (which applies to 3.1.3) does what was proposed.  All doctests in sage/rings/number_fields/ pass *except* for a couple in totallyreal_rel.py where one of the totally real quadratic extensions of Q(sqrt(5)) is now missing.  I do not know why but suggest that there might be a bug in that file, so will ask John Voight to look into it.



---

archive/issue_comments_030891.json:
```json
{
    "body": "I can't test this yet because I can't apply the patch to 3.1.2, and the upgrade is apparently not yet working.  I'm worried about all of the changes to reduced_basis which resulted from the change, but will have a look ASAP.  JV",
    "created_at": "2008-10-14T22:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30891",
    "user": "jvoight"
}
```

I can't test this yet because I can't apply the patch to 3.1.2, and the upgrade is apparently not yet working.  I'm worried about all of the changes to reduced_basis which resulted from the change, but will have a look ASAP.  JV



---

archive/issue_comments_030892.json:
```json
{
    "body": "Thanks John.  I put \"not ready for review\" since we don't yet know exactly what is going on.  John",
    "created_at": "2008-10-15T06:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30892",
    "user": "cremona"
}
```

Thanks John.  I put "not ready for review" since we don't yet know exactly what is going on.  John



---

archive/issue_comments_030893.json:
```json
{
    "body": "Hm.  John, what bug exactly were you getting?  I just applied your sage-4249.patch to a clean build of sage-3.1.3 and it indeed gives me 21 totally real quadratic extensions of Q(sqrt(5)) with discriminant <= 10^4.  In particular, for this example the output of F.reduced_basis() does not seem to change after the patch, and so I would not expect anything to change.\n\nJV",
    "created_at": "2008-10-16T00:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30893",
    "user": "jvoight"
}
```

Hm.  John, what bug exactly were you getting?  I just applied your sage-4249.patch to a clean build of sage-3.1.3 and it indeed gives me 21 totally real quadratic extensions of Q(sqrt(5)) with discriminant <= 10^4.  In particular, for this example the output of F.reduced_basis() does not seem to change after the patch, and so I would not expect anything to change.

JV



---

archive/issue_comments_030894.json:
```json
{
    "body": "When I apply my patch to 3.1.3 I get this (testing all files in number_field):\n\n```\n******************************\nFile \"/home/john/sage-3.1.3/tmp/totallyreal_rel.py\", line 658:\n    sage: [ f[0] for f in ls ]\nExpected:\n    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7225, 7600, 7625, 8000, 8525, 8725, 9225]\nGot:\n    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7600, 7625, 8000, 8525, 8725, 9225]\n**********************************************************************\nFile \"/home/john/sage-3.1.3/tmp/totallyreal_rel.py\", line 661:\n    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]\nExpected:\n    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, True, False, False, True, False, False, False]\nGot:\n    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, False, False, True, False, False, False]\n**********************************************************************\n1 items had failures:\n   2 of  12 in __main__.example_6\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/john/sage-3.1.3/tmp/.doctest_totallyreal_rel.py\n```\n",
    "created_at": "2008-10-16T05:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30894",
    "user": "cremona"
}
```

When I apply my patch to 3.1.3 I get this (testing all files in number_field):

```
******************************
File "/home/john/sage-3.1.3/tmp/totallyreal_rel.py", line 658:
    sage: [ f[0] for f in ls ]
Expected:
    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7225, 7600, 7625, 8000, 8525, 8725, 9225]
Got:
    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7600, 7625, 8000, 8525, 8725, 9225]
**********************************************************************
File "/home/john/sage-3.1.3/tmp/totallyreal_rel.py", line 661:
    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]
Expected:
    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, True, False, False, True, False, False, False]
Got:
    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, False, False, True, False, False, False]
**********************************************************************
1 items had failures:
   2 of  12 in __main__.example_6
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/john/sage-3.1.3/tmp/.doctest_totallyreal_rel.py
```




---

archive/issue_comments_030895.json:
```json
{
    "body": "Huh.  Applying the patch on sage.math (on 3.1.3) gives:\n   {{{\n   sage: F.<t> = NumberField(x^2-5)\n   sage: enumerate_totallyreal_fields_rel?\n   sage: ls = enumerate_totallyreal_fields_rel(F, 2, 10^4)\n   sage: enumerate_totallyreal_fields_rel?\n   sage: [ f[0] for f in ls ]\n   [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525,\n   5125, 5225, 5725, 6125, 7225, 7600, 7625, 8000, 8525, 8725,\n   9225]\n   }}}\nNot really sure what could be causing this, unless it's an ugly platform-dependent precision issue or something.",
    "created_at": "2008-10-16T23:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30895",
    "user": "jvoight"
}
```

Huh.  Applying the patch on sage.math (on 3.1.3) gives:
   {{{
   sage: F.<t> = NumberField(x^2-5)
   sage: enumerate_totallyreal_fields_rel?
   sage: ls = enumerate_totallyreal_fields_rel(F, 2, 10^4)
   sage: enumerate_totallyreal_fields_rel?
   sage: [ f[0] for f in ls ]
   [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525,
   5125, 5225, 5725, 6125, 7225, 7600, 7625, 8000, 8525, 8725,
   9225]
   }}}
Not really sure what could be causing this, unless it's an ugly platform-dependent precision issue or something.



---

archive/issue_comments_030896.json:
```json
{
    "body": "I agree, it is likely to be a precision issue.  My laptop is 32-bit while sage.math is 64.",
    "created_at": "2008-10-17T06:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30896",
    "user": "cremona"
}
```

I agree, it is likely to be a precision issue.  My laptop is 32-bit while sage.math is 64.



---

archive/issue_comments_030897.json:
```json
{
    "body": "I downloaded a clean 3.1.3 and installed it on a 32-bit Ubuntu and it again worked fine.  I'm not sure what's going on.  JV",
    "created_at": "2008-10-20T00:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30897",
    "user": "jvoight"
}
```

I downloaded a clean 3.1.3 and installed it on a 32-bit Ubuntu and it again worked fine.  I'm not sure what's going on.  JV



---

archive/issue_comments_030898.json:
```json
{
    "body": "Replying to [comment:10 jvoight]:\n> I downloaded a clean 3.1.3 and installed it on a 32-bit Ubuntu and it again worked fine.  I'm not sure what's going on.  JV\n\nNor me.  I just tried again on a fresh 3.1.4 and got the same problem as before.\n\nI think we need to ask someone else to help with this!  JEC",
    "created_at": "2008-10-20T11:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30898",
    "user": "cremona"
}
```

Replying to [comment:10 jvoight]:
> I downloaded a clean 3.1.3 and installed it on a 32-bit Ubuntu and it again worked fine.  I'm not sure what's going on.  JV

Nor me.  I just tried again on a fresh 3.1.4 and got the same problem as before.

I think we need to ask someone else to help with this!  JEC



---

archive/issue_comments_030899.json:
```json
{
    "body": "Hi John,\n\nI'm hoping to tackle this at Sage Days 11, or at least find someone willing to help.  What system are you using?  Maybe I can find someone with the same system so as to reproduce the bug...\n\nJV",
    "created_at": "2008-11-06T15:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30899",
    "user": "jvoight"
}
```

Hi John,

I'm hoping to tackle this at Sage Days 11, or at least find someone willing to help.  What system are you using?  Maybe I can find someone with the same system so as to reproduce the bug...

JV



---

archive/issue_comments_030900.json:
```json
{
    "body": "Replying to [comment:12 jvoight]:\n> Hi John,\n> \n> I'm hoping to tackle this at Sage Days 11, or at least find someone willing to help.  What system are you using?  Maybe I can find someone with the same system so as to reproduce the bug...\n> \n> JV\n\nIt was probably my laptop (ubuntu linux 8.04 etc).  As I have just built 3.2.alpha3 on a couple of other machines, I'll test my patch on those and see what happens.  Watch this space...",
    "created_at": "2008-11-06T15:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30900",
    "user": "cremona"
}
```

Replying to [comment:12 jvoight]:
> Hi John,
> 
> I'm hoping to tackle this at Sage Days 11, or at least find someone willing to help.  What system are you using?  Maybe I can find someone with the same system so as to reproduce the bug...
> 
> JV

It was probably my laptop (ubuntu linux 8.04 etc).  As I have just built 3.2.alpha3 on a couple of other machines, I'll test my patch on those and see what happens.  Watch this space...



---

archive/issue_comments_030901.json:
```json
{
    "body": "I applied my patch to 3.2.alpha3 on two machines, a 32-bit Suse linux and a 64-bit ubuntu.\nOn both machines two files failed doctests:\n\n1.  sage -t  devel/sage-intpts/sage/rings/number_field/number_field.py\n2.  sage -t  devel/sage-intpts/sage/rings/number_field/totallyreal_rel.py\n\nIn totallrel_rel.py we get this:\n\n```\nsage -t  devel/sage-intpts/sage/rings/number_field/totallyreal_rel.py**********************************************************************\nFile \"/home/jec/sage-3.2.alpha3/tmp/totallyreal_rel.py\", line 658:\n    sage: [ f[0] for f in ls ]\nExpected:\n    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7225, 7600, 7625, 8000, 8525, 8725, 9225]\nGot:\n    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7600, 7625, 8000, 8525, 8725, 9225]\n**********************************************************************\nFile \"/home/jec/sage-3.2.alpha3/tmp/totallyreal_rel.py\", line 661:\n    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]\nExpected:\n    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, True, False, False, True, False, False, False]\nGot:\n    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, False, False, True, False, False, False]\n**********************************************************************\n```\n\nwhich looks like what I got before.  In number_field.py we get this:\n\n```\nsage -t  local/sage-3.2.alpha3/devel/sage-intbasis/sage/rings/number_field//number_field.py**********************************************************************\nFile \"/local/jec/sage-3.2.alpha3/tmp/number_field.py\", line 2742:\n    sage: F.reduced_gram_matrix(prec=128)\nExpected:\n    [   4.0000000000000000000000000000000000000   0.00000000000000000000000000000000000000    1.9999999999999999999999999999999999037 -1.0684680000000000000000000000000000000e6]\n    [  0.00000000000000000000000000000000000000    46721.539331563218381658483353092335550    11488.910026551724275122749703614966768 -1.1228558200864828963821803781091898982e7]\n    [   1.9999999999999999999999999999999999037    11488.910026551724275122749703614966768  5.5658915310500611768713076521847709187e8  8.0619179090987317435751641503958312826e9]\n    [-1.0684680000000000000000000000000000000e6 -1.1228558200864828963821803781091898982e7  8.0619179090987317435751641503958312826e9 5.8711879006497804783677635022079228656e12]\nGot:\n    [   4.0000000000000000000000000000000000000   0.00000000000000000000000000000000000000 -2.1369320000000000000000000000000000000e6 -3.3122478000000000000000000000000000000e7]\n    [  0.00000000000000000000000000000000000000    46721.539331563218381658483353092335550 -2.2467769057394530109094755223395819322e7 -3.4807276041138450473611629088647496430e8]\n    [-2.1369320000000000000000000000000000000e6 -2.2467769057394530109094755223395819322e7 7.0704243186034907491782135494859351061e12 1.1256636615786237006027526953641297995e14]\n    [-3.3122478000000000000000000000000000000e7 -3.4807276041138450473611629088647496430e8 1.1256636615786237006027526953641297995e14 1.7923838231014970520503146603069479547e15]\n\n```\n\nwhich is new.  I find it slightly encouraging that my 32- and 64-bit tests both give exactly the same above (as each other).  I guess that this second discrepancy will be fixed by just changing the Expected doctest output, but the first one really is a bug since a field which should be returned is not.",
    "created_at": "2008-11-06T15:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30901",
    "user": "cremona"
}
```

I applied my patch to 3.2.alpha3 on two machines, a 32-bit Suse linux and a 64-bit ubuntu.
On both machines two files failed doctests:

1.  sage -t  devel/sage-intpts/sage/rings/number_field/number_field.py
2.  sage -t  devel/sage-intpts/sage/rings/number_field/totallyreal_rel.py

In totallrel_rel.py we get this:

```
sage -t  devel/sage-intpts/sage/rings/number_field/totallyreal_rel.py**********************************************************************
File "/home/jec/sage-3.2.alpha3/tmp/totallyreal_rel.py", line 658:
    sage: [ f[0] for f in ls ]
Expected:
    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7225, 7600, 7625, 8000, 8525, 8725, 9225]
Got:
    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7600, 7625, 8000, 8525, 8725, 9225]
**********************************************************************
File "/home/jec/sage-3.2.alpha3/tmp/totallyreal_rel.py", line 661:
    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]
Expected:
    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, True, False, False, True, False, False, False]
Got:
    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, False, False, True, False, False, False]
**********************************************************************
```

which looks like what I got before.  In number_field.py we get this:

```
sage -t  local/sage-3.2.alpha3/devel/sage-intbasis/sage/rings/number_field//number_field.py**********************************************************************
File "/local/jec/sage-3.2.alpha3/tmp/number_field.py", line 2742:
    sage: F.reduced_gram_matrix(prec=128)
Expected:
    [   4.0000000000000000000000000000000000000   0.00000000000000000000000000000000000000    1.9999999999999999999999999999999999037 -1.0684680000000000000000000000000000000e6]
    [  0.00000000000000000000000000000000000000    46721.539331563218381658483353092335550    11488.910026551724275122749703614966768 -1.1228558200864828963821803781091898982e7]
    [   1.9999999999999999999999999999999999037    11488.910026551724275122749703614966768  5.5658915310500611768713076521847709187e8  8.0619179090987317435751641503958312826e9]
    [-1.0684680000000000000000000000000000000e6 -1.1228558200864828963821803781091898982e7  8.0619179090987317435751641503958312826e9 5.8711879006497804783677635022079228656e12]
Got:
    [   4.0000000000000000000000000000000000000   0.00000000000000000000000000000000000000 -2.1369320000000000000000000000000000000e6 -3.3122478000000000000000000000000000000e7]
    [  0.00000000000000000000000000000000000000    46721.539331563218381658483353092335550 -2.2467769057394530109094755223395819322e7 -3.4807276041138450473611629088647496430e8]
    [-2.1369320000000000000000000000000000000e6 -2.2467769057394530109094755223395819322e7 7.0704243186034907491782135494859351061e12 1.1256636615786237006027526953641297995e14]
    [-3.3122478000000000000000000000000000000e7 -3.4807276041138450473611629088647496430e8 1.1256636615786237006027526953641297995e14 1.7923838231014970520503146603069479547e15]

```

which is new.  I find it slightly encouraging that my 32- and 64-bit tests both give exactly the same above (as each other).  I guess that this second discrepancy will be fixed by just changing the Expected doctest output, but the first one really is a bug since a field which should be returned is not.



---

archive/issue_comments_030902.json:
```json
{
    "body": "Argh!  Tried the patch on sage.math on 3.2.alpha3, still can't reproduce the error!  \n\n\n```\njvoight@sage:~/sage-3.2.alpha3$ ./sage -t ./devel/sage/sage/rings/number_field/totallyreal_rel.py\nsage -t  devel/sage/sage/rings/number_field/totallyreal_rel.py\n         [4.5 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.5 seconds}}}\n\nI'll see if I can find someone here in Austin.  (I have some ideas about what may be going on, but I can't check any of them!)  JV",
    "created_at": "2008-11-09T00:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30902",
    "user": "jvoight"
}
```

Argh!  Tried the patch on sage.math on 3.2.alpha3, still can't reproduce the error!  


```
jvoight@sage:~/sage-3.2.alpha3$ ./sage -t ./devel/sage/sage/rings/number_field/totallyreal_rel.py
sage -t  devel/sage/sage/rings/number_field/totallyreal_rel.py
         [4.5 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.5 seconds}}}

I'll see if I can find someone here in Austin.  (I have some ideas about what may be going on, but I can't check any of them!)  JV



---

archive/issue_comments_030903.json:
```json
{
    "body": "Attached patch fixes the issue. It turns out that John Cremona's fix actually exposed a small bug in `integral_elements_with_trace`, which has been fixed and renamed. \n\nThis was written with John Voight.",
    "created_at": "2008-11-09T02:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30903",
    "user": "craigcitro"
}
```

Attached patch fixes the issue. It turns out that John Cremona's fix actually exposed a small bug in `integral_elements_with_trace`, which has been fixed and renamed. 

This was written with John Voight.



---

archive/issue_comments_030904.json:
```json
{
    "body": "Whoops. Forgot that we had to look at John's original patch, too. :)",
    "created_at": "2008-11-09T03:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30904",
    "user": "craigcitro"
}
```

Whoops. Forgot that we had to look at John's original patch, too. :)



---

archive/issue_comments_030905.json:
```json
{
    "body": "Attachment [trac-4249-1a.patch](tarball://root/attachments/some-uuid/ticket4249/trac-4249-1a.patch) by craigcitro created at 2008-11-14 09:19:02",
    "created_at": "2008-11-14T09:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30905",
    "user": "craigcitro"
}
```

Attachment [trac-4249-1a.patch](tarball://root/attachments/some-uuid/ticket4249/trac-4249-1a.patch) by craigcitro created at 2008-11-14 09:19:02



---

archive/issue_comments_030906.json:
```json
{
    "body": "Attachment [trac-4249-pt2a.patch](tarball://root/attachments/some-uuid/ticket4249/trac-4249-pt2a.patch) by craigcitro created at 2008-11-14 09:22:08\n\nThis looks good! \n\nThe only complaints I had were one or two naming issues; in particular, I didn't see why `integral_basis_internal` should be visible when you tab complete. (The `internal` in the name really makes it seem weird.) So I've just corrected a few naming issues, and made a new patch. Then I rebased the patch John Voight and I wrote on top of this. So you should apply:\n\n\n```\nsage-4249.patch\ntrac-4249-1a.patch\ntrac-4249-pt2a.patch\n```\n\n\nin order. (I've deleted the old pt2 patch, just to help avoid confusion.)",
    "created_at": "2008-11-14T09:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30906",
    "user": "craigcitro"
}
```

Attachment [trac-4249-pt2a.patch](tarball://root/attachments/some-uuid/ticket4249/trac-4249-pt2a.patch) by craigcitro created at 2008-11-14 09:22:08

This looks good! 

The only complaints I had were one or two naming issues; in particular, I didn't see why `integral_basis_internal` should be visible when you tab complete. (The `internal` in the name really makes it seem weird.) So I've just corrected a few naming issues, and made a new patch. Then I rebased the patch John Voight and I wrote on top of this. So you should apply:


```
sage-4249.patch
trac-4249-1a.patch
trac-4249-pt2a.patch
```


in order. (I've deleted the old pt2 patch, just to help avoid confusion.)



---

archive/issue_comments_030907.json:
```json
{
    "body": "I strongly approve of the two new patches, which fix the bug which caused the totally_real_rel failure and also improve on my code design.  I tested them against 3.2.alpha3 and all was well (testing all in number_field/).\n\nSo I hope there's enough mutual positive reviewing here for these to be merged.\n\nIt would be even better if John V agreed!",
    "created_at": "2008-11-14T09:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30907",
    "user": "cremona"
}
```

I strongly approve of the two new patches, which fix the bug which caused the totally_real_rel failure and also improve on my code design.  I tested them against 3.2.alpha3 and all was well (testing all in number_field/).

So I hope there's enough mutual positive reviewing here for these to be merged.

It would be even better if John V agreed!



---

archive/issue_comments_030908.json:
```json
{
    "body": "Yes, definitely I agree.  Positive review.  JV",
    "created_at": "2008-11-14T14:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30908",
    "user": "jvoight"
}
```

Yes, definitely I agree.  Positive review.  JV



---

archive/issue_comments_030909.json:
```json
{
    "body": "There are some slight doctest failures to fix:\n\n```\nsage -t -long devel/sage/sage/rings/number_field/number_field.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/rings/number_field/number_field.py\", line 2653:\n    sage: F.reduced_basis(prec=96)\nExpected:\n    [1, alpha, alpha^2 - 15*alpha, alpha^3 - 16*alpha^2 + 469*alpha + 267109] \nGot:\n    [1, alpha, alpha^3 - 2*alpha^2 + 15*alpha, 16*alpha^3 - 31*alpha^2 + 469*alpha + 267109]\n\n**********************************************************************\n1 items had failures:\n   1 of   9 in __main__.example_73\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_number_field.py\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n\n\t [29.4 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long devel/sage/sage/rings/number_field/number_field.py\nTotal time for all tests: 29.4 seconds\nsage -t -long devel/doc/tut/tut.tex                         \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/doc/tut/tut.tex\", line 2179:\n    : K.integral_basis()\nExpected:\n    [1, a, 1/2*a^2 + 1/2*a]\nGot:\n    [1, 1/2*a^2 + 1/2*a, a^2]\n**********************************************************************\n1 items had failures:\n   1 of  11 in __main__.example_99\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_tut.py\n\t [25.2 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long devel/doc/tut/tut.tex\nTotal time for all tests: 25.2 seconds\nsage -t -long devel/doc/const/const.tex                     **********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/doc/const/const.tex\", line 3450:\n    : K.integral_basis()\nExpected:\n    [1, a, 1/2*a^2 + 1/2*a]\nGot:\n    [1, 1/2*a^2 + 1/2*a, a^2]\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_123\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_const.py\n\t [31.0 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long devel/doc/const/const.tex\nTotal time for all tests: 31.0 seconds\n```\n",
    "created_at": "2008-11-14T20:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30909",
    "user": "mabshoff"
}
```

There are some slight doctest failures to fix:

```
sage -t -long devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/rings/number_field/number_field.py", line 2653:
    sage: F.reduced_basis(prec=96)
Expected:
    [1, alpha, alpha^2 - 15*alpha, alpha^3 - 16*alpha^2 + 469*alpha + 267109] 
Got:
    [1, alpha, alpha^3 - 2*alpha^2 + 15*alpha, 16*alpha^3 - 31*alpha^2 + 469*alpha + 267109]

**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_73
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_number_field.py
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.

	 [29.4 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long devel/sage/sage/rings/number_field/number_field.py
Total time for all tests: 29.4 seconds
sage -t -long devel/doc/tut/tut.tex                         
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/doc/tut/tut.tex", line 2179:
    : K.integral_basis()
Expected:
    [1, a, 1/2*a^2 + 1/2*a]
Got:
    [1, 1/2*a^2 + 1/2*a, a^2]
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_99
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_tut.py
	 [25.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long devel/doc/tut/tut.tex
Total time for all tests: 25.2 seconds
sage -t -long devel/doc/const/const.tex                     **********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/doc/const/const.tex", line 3450:
    : K.integral_basis()
Expected:
    [1, a, 1/2*a^2 + 1/2*a]
Got:
    [1, 1/2*a^2 + 1/2*a, a^2]
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_123
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_const.py
	 [31.0 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long devel/doc/const/const.tex
Total time for all tests: 31.0 seconds
```




---

archive/issue_comments_030910.json:
```json
{
    "body": "Attachment [trac-4249-3.patch](tarball://root/attachments/some-uuid/ticket4249/trac-4249-3.patch) by cremona created at 2008-11-14 20:46:24",
    "created_at": "2008-11-14T20:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30910",
    "user": "cremona"
}
```

Attachment [trac-4249-3.patch](tarball://root/attachments/some-uuid/ticket4249/trac-4249-3.patch) by cremona created at 2008-11-14 20:46:24



---

archive/issue_comments_030911.json:
```json
{
    "body": "Attachment [trac-4249-doc.patch](tarball://root/attachments/some-uuid/ticket4249/trac-4249-doc.patch) by cremona created at 2008-11-14 20:47:10",
    "created_at": "2008-11-14T20:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30911",
    "user": "cremona"
}
```

Attachment [trac-4249-doc.patch](tarball://root/attachments/some-uuid/ticket4249/trac-4249-doc.patch) by cremona created at 2008-11-14 20:47:10



---

archive/issue_comments_030912.json:
```json
{
    "body": "Strange about that first one -- it was one where I had had different output on 32- and 64-bit machines, but now they are the same.  Fixed in trac-4249-3.patch.\n\nThe doc ones are in a separate patch  trac-4249-doc.patch which I hope can be dealt with: I did \"hg ci\" and then \"hg export tip\" from devel/doc.  For some reason the patch also affects patchlevel.tex.",
    "created_at": "2008-11-14T20:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30912",
    "user": "cremona"
}
```

Strange about that first one -- it was one where I had had different output on 32- and 64-bit machines, but now they are the same.  Fixed in trac-4249-3.patch.

The doc ones are in a separate patch  trac-4249-doc.patch which I hope can be dealt with: I did "hg ci" and then "hg export tip" from devel/doc.  For some reason the patch also affects patchlevel.tex.



---

archive/issue_comments_030913.json:
```json
{
    "body": "Yep, last patches look good.",
    "created_at": "2008-11-15T09:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30913",
    "user": "craigcitro"
}
```

Yep, last patches look good.



---

archive/issue_comments_030914.json:
```json
{
    "body": "What is the credit situation, i.e. authorship here: John Cremona, John Voight? Review Craig Citro?\n\nWhat about Aranes Maite?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-15T09:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30914",
    "user": "mabshoff"
}
```

What is the credit situation, i.e. authorship here: John Cremona, John Voight? Review Craig Citro?

What about Aranes Maite?

Cheers,

Michael



---

archive/issue_comments_030915.json:
```json
{
    "body": "I think John C wrote sage-4249.patch, I wrote trac-4249-1a.patch as part of the review, John Voight and I each wrote half of trac-4249-pt2a.patch and reviewed the other, and John Cremona also reviewed this patch. Then John Cremona wrote pt3 and the doc patch.\n\nEither that, or it was Col. Mustard in the study, with the candlestick. (I would be completely in favor of that actually appearing in the release notes.)\n\nI'm not sure if the original patch was written with Aranes Maite.",
    "created_at": "2008-11-15T09:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30915",
    "user": "craigcitro"
}
```

I think John C wrote sage-4249.patch, I wrote trac-4249-1a.patch as part of the review, John Voight and I each wrote half of trac-4249-pt2a.patch and reviewed the other, and John Cremona also reviewed this patch. Then John Cremona wrote pt3 and the doc patch.

Either that, or it was Col. Mustard in the study, with the candlestick. (I would be completely in favor of that actually appearing in the release notes.)

I'm not sure if the original patch was written with Aranes Maite.



---

archive/issue_comments_030916.json:
```json
{
    "body": "Replying to [comment:25 craigcitro]:\n> I think John C wrote sage-4249.patch, I wrote trac-4249-1a.patch as part of the review, John Voight and I each wrote half of trac-4249-pt2a.patch and reviewed the other, and John Cremona also reviewed this patch. Then John Cremona wrote pt3 and the doc patch.\n> \n\nThat is accurate as far as I am concerned.\n\n> Either that, or it was Col. Mustard in the study, with the candlestick. (I would be completely in favor of that actually appearing in the release notes.)\n> \n> I'm not sure if the original patch was written with Aranes Maite.\n\nNo, but she (my student) was the one who alerted me to the problem in the first place.",
    "created_at": "2008-11-15T10:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30916",
    "user": "cremona"
}
```

Replying to [comment:25 craigcitro]:
> I think John C wrote sage-4249.patch, I wrote trac-4249-1a.patch as part of the review, John Voight and I each wrote half of trac-4249-pt2a.patch and reviewed the other, and John Cremona also reviewed this patch. Then John Cremona wrote pt3 and the doc patch.
> 

That is accurate as far as I am concerned.

> Either that, or it was Col. Mustard in the study, with the candlestick. (I would be completely in favor of that actually appearing in the release notes.)
> 
> I'm not sure if the original patch was written with Aranes Maite.

No, but she (my student) was the one who alerted me to the problem in the first place.



---

archive/issue_comments_030917.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-15T10:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30917",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030918.json:
```json
{
    "body": "Merged all five patches in Sage 3.2.rc1",
    "created_at": "2008-11-15T10:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4249#issuecomment-30918",
    "user": "mabshoff"
}
```

Merged all five patches in Sage 3.2.rc1
