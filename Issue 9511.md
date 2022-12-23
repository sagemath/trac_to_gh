# Issue 9511: Suggestion to upgrade givaro 3.3.1 and 3.3.2 [with patch]

archive/issues_009511.json:
```json
{
    "body": "Assignee: cpernet\n\nCC:  zimmerma jpflori\n\nIn the Mandriva sagemath package I use the attached patch. It did work with sagemath 4.4 and givaro 3.3.1, and still works with sagemath 4.4.4 and givaro 3.3.2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9511\n\n",
    "created_at": "2010-07-15T19:51:16Z",
    "labels": [
        "finite rings",
        "minor",
        "enhancement"
    ],
    "title": "Suggestion to upgrade givaro 3.3.1 and 3.3.2 [with patch]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9511",
    "user": "pcpa"
}
```
Assignee: cpernet

CC:  zimmerma jpflori

In the Mandriva sagemath package I use the attached patch. It did work with sagemath 4.4 and givaro 3.3.1, and still works with sagemath 4.4.4 and givaro 3.3.2.

Issue created by migration from https://trac.sagemath.org/ticket/9511





---

archive/issue_comments_091389.json:
```json
{
    "body": "I'm currently working on the upgrade to givaro-3.3.3rc0 together with linbox-1.1.7, since this later version of linbox required very recent changes in givaro (only in 3.3.3rc0).",
    "created_at": "2010-07-15T19:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91389",
    "user": "cpernet"
}
```

I'm currently working on the upgrade to givaro-3.3.3rc0 together with linbox-1.1.7, since this later version of linbox required very recent changes in givaro (only in 3.3.3rc0).



---

archive/issue_comments_091390.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-23T02:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91390",
    "user": "malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091391.json:
```json
{
    "body": "Note this upgrade won't work unless LinBox is upgraded as well.",
    "created_at": "2011-08-23T04:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91391",
    "user": "malb"
}
```

Note this upgrade won't work unless LinBox is upgraded as well.



---

archive/issue_comments_091392.json:
```json
{
    "body": "Replying to [comment:6 malb]:\n> Note this upgrade won't work unless LinBox is upgraded as well.\nI was going to say that, not to mention we need a givaro-3.3.xx spkg too.",
    "created_at": "2011-08-23T04:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91392",
    "user": "fbissey"
}
```

Replying to [comment:6 malb]:
> Note this upgrade won't work unless LinBox is upgraded as well.
I was going to say that, not to mention we need a givaro-3.3.xx spkg too.



---

archive/issue_comments_091393.json:
```json
{
    "body": "spkg that I missed in the description somehow. linbox in a new ticket?",
    "created_at": "2011-08-23T04:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91393",
    "user": "fbissey"
}
```

spkg that I missed in the description somehow. linbox in a new ticket?



---

archive/issue_comments_091394.json:
```json
{
    "body": "Yep, I opened #11718 for that but I just accidentally killed the last three hours of pretty boring & tedious work trying to compile 1.1.7. So it'll take a while until I upload an SPKG there.",
    "created_at": "2011-08-23T04:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91394",
    "user": "malb"
}
```

Yep, I opened #11718 for that but I just accidentally killed the last three hours of pretty boring & tedious work trying to compile 1.1.7. So it'll take a while until I upload an SPKG there.



---

archive/issue_comments_091395.json:
```json
{
    "body": "**Status update:**\n\nWe get errors like this\n\n\n```\n/sage-4.7.1/local/include/givaro/givzpz16table1.inl:424: error: \u2018UINT32_MAX\u2019 was not declared in this scope\n```\n\n\non *sage.math* unless we explicitly pass `-D__STDC_LIMIT_MACROS` in `spkg-install`. This works but is weird because Givaro does set `__STDC_LIMIT_MACROS` before it includes `<stdint.h>`. Also, I do not have this problem my local machine (running 64-bit Debian/GNU Linux)",
    "created_at": "2011-08-23T18:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91395",
    "user": "malb"
}
```

**Status update:**

We get errors like this


```
/sage-4.7.1/local/include/givaro/givzpz16table1.inl:424: error: ‘UINT32_MAX’ was not declared in this scope
```


on *sage.math* unless we explicitly pass `-D__STDC_LIMIT_MACROS` in `spkg-install`. This works but is weird because Givaro does set `__STDC_LIMIT_MACROS` before it includes `<stdint.h>`. Also, I do not have this problem my local machine (running 64-bit Debian/GNU Linux)



---

archive/issue_comments_091396.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-08-23T18:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91396",
    "user": "malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_091397.json:
```json
{
    "body": "Just for the record:\n\nThere's a Givaro 3.2.13.rc1.p4 spkg with a couple of fixes at #12761 (currently still needing review).",
    "created_at": "2012-04-22T01:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91397",
    "user": "leif"
}
```

Just for the record:

There's a Givaro 3.2.13.rc1.p4 spkg with a couple of fixes at #12761 (currently still needing review).



---

archive/issue_comments_091398.json:
```json
{
    "body": "I am feeling ambitious today (Brice from the LinBox team is in shouting distance) so I decided to give this update business another try. Givaro 3.6.0 is the easy part so here it is.",
    "created_at": "2012-06-06T19:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91398",
    "user": "malb"
}
```

I am feeling ambitious today (Brice from the LinBox team is in shouting distance) so I decided to give this update business another try. Givaro 3.6.0 is the easy part so here it is.



---

archive/issue_comments_091399.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-06-18T09:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91399",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091400.json:
```json
{
    "body": "Updated so that the number theory doctest in the \"French book\" is deterministic.",
    "created_at": "2012-06-18T09:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91400",
    "user": "malb"
}
```

Updated so that the number theory doctest in the "French book" is deterministic.



---

archive/issue_comments_091401.json:
```json
{
    "body": "The permissions of `spkg-install` and `SPKG.txt` should be fixed to make Jeroen happy ;-)",
    "created_at": "2012-06-18T11:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91401",
    "user": "vbraun"
}
```

The permissions of `spkg-install` and `SPKG.txt` should be fixed to make Jeroen happy ;-)



---

archive/issue_comments_091402.json:
```json
{
    "body": "Fixed to 755 and 644 respectively.",
    "created_at": "2012-06-18T11:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91402",
    "user": "malb"
}
```

Fixed to 755 and 644 respectively.



---

archive/issue_comments_091403.json:
```json
{
    "body": "Patch doesn't apply on top of the m4ri update (#12840, #12841).\n\nAlso, `Set([r for r in R])` should be just `Set(R)` or (even better in case there are duplicate elements) `sorted(R)`",
    "created_at": "2012-06-18T11:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91403",
    "user": "vbraun"
}
```

Patch doesn't apply on top of the m4ri update (#12840, #12841).

Also, `Set([r for r in R])` should be just `Set(R)` or (even better in case there are duplicate elements) `sorted(R)`



---

archive/issue_comments_091404.json:
```json
{
    "body": "Replying to [comment:20 vbraun]:\n> Patch doesn't apply on top of the m4ri update (#12840, #12841).\n\nThat's weird, I have it applied here:\n\n\n```\n$ hg qap                                                                                                                        [r16883 mq:5/5 sage-linbox.patch -  1:09PM]\ntrac_12840_m4ri_new_version.patch\ntrac_12841_m4rie_new_version.patch\ntrac_9511_givaro_3_6_x.patch\nmatrix_modn_dense_no_linbox.patch\nsage-linbox.patch\n```\n\n \n> Also, `Set([r for r in R])` should be just `Set(R)` or (even better in case there are duplicate elements) `sorted(R)` \n\nI just copied what Paul Zimmermann suggested as a fix for the book. Paul is CCed, so if he agrees, I'll change the doctest accordingly.",
    "created_at": "2012-06-18T12:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91404",
    "user": "malb"
}
```

Replying to [comment:20 vbraun]:
> Patch doesn't apply on top of the m4ri update (#12840, #12841).

That's weird, I have it applied here:


```
$ hg qap                                                                                                                        [r16883 mq:5/5 sage-linbox.patch -  1:09PM]
trac_12840_m4ri_new_version.patch
trac_12841_m4rie_new_version.patch
trac_9511_givaro_3_6_x.patch
matrix_modn_dense_no_linbox.patch
sage-linbox.patch
```

 
> Also, `Set([r for r in R])` should be just `Set(R)` or (even better in case there are duplicate elements) `sorted(R)` 

I just copied what Paul Zimmermann suggested as a fix for the book. Paul is CCed, so if he agrees, I'll change the doctest accordingly.



---

archive/issue_comments_091405.json:
```json
{
    "body": "Where does the line \n\n```\n              depends = [SAGE_INC + 'givaro/givconfig.h']), \n```\n\nin your `module_list.py` come from? Its not in sage-5.1.beta3.\n\nAlso (and perhaps related), #11718 is no longer a dependency for this ticket right?",
    "created_at": "2012-06-18T12:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91405",
    "user": "vbraun"
}
```

Where does the line 

```
              depends = [SAGE_INC + 'givaro/givconfig.h']), 
```

in your `module_list.py` come from? Its not in sage-5.1.beta3.

Also (and perhaps related), #11718 is no longer a dependency for this ticket right?



---

archive/issue_comments_091406.json:
```json
{
    "body": "Replying to [comment:22 vbraun]:\n> Where does the line \n> {{{\n>               depends = [SAGE_INC + 'givaro/givconfig.h']), \n> }}}\n> in your `module_list.py` come from? Its not in sage-5.1.beta3.\n\nIt's from \n\nhttp://trac.sagemath.org/sage_trac/attachment/ticket/12761/12761_givaro_depends.patch\n\nwhich was merged in 5.0.1.rc1.\n> Also (and perhaps related), #11718 is no longer a dependency for this ticket right?\n\nRight, fixed that.",
    "created_at": "2012-06-18T13:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91406",
    "user": "malb"
}
```

Replying to [comment:22 vbraun]:
> Where does the line 
> {{{
>               depends = [SAGE_INC + 'givaro/givconfig.h']), 
> }}}
> in your `module_list.py` come from? Its not in sage-5.1.beta3.

It's from 

http://trac.sagemath.org/sage_trac/attachment/ticket/12761/12761_givaro_depends.patch

which was merged in 5.0.1.rc1.
> Also (and perhaps related), #11718 is no longer a dependency for this ticket right?

Right, fixed that.



---

archive/issue_comments_091407.json:
```json
{
    "body": "Why is #12883 a dependency? Its the other way round, this ticket is a dependency for #12883 or not?",
    "created_at": "2012-06-18T13:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91407",
    "user": "vbraun"
}
```

Why is #12883 a dependency? Its the other way round, this ticket is a dependency for #12883 or not?



---

archive/issue_comments_091408.json:
```json
{
    "body": "Both tickets depend on each other, you cannot have one without the other.  Givaro upgrade implies LinBox upgrade and LinBox upgrade implies Givaro upgrade. Perhaps it would be cleaner to merge them?",
    "created_at": "2012-06-18T13:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91408",
    "user": "malb"
}
```

Both tickets depend on each other, you cannot have one without the other.  Givaro upgrade implies LinBox upgrade and LinBox upgrade implies Givaro upgrade. Perhaps it would be cleaner to merge them?



---

archive/issue_comments_091409.json:
```json
{
    "body": "Lets leave it at the current state but in general its probably best to avoid cyclic dependencies....",
    "created_at": "2012-06-18T13:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91409",
    "user": "vbraun"
}
```

Lets leave it at the current state but in general its probably best to avoid cyclic dependencies....



---

archive/issue_comments_091410.json:
```json
{
    "body": "Replying to [comment:20 vbraun]:\n> Also, `Set([r for r in R])` should be just `Set(R)` or (even better in case there are duplicate elements) `sorted(R)` \n\nI prefer to leave `Set([r for r in R])` which is more explicit (in my opinion) and to make\nthe changes minimal in the book. There are no duplicate elements here (in a finite field).\n\nPaul",
    "created_at": "2012-06-18T13:46:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91410",
    "user": "zimmerma"
}
```

Replying to [comment:20 vbraun]:
> Also, `Set([r for r in R])` should be just `Set(R)` or (even better in case there are duplicate elements) `sorted(R)` 

I prefer to leave `Set([r for r in R])` which is more explicit (in my opinion) and to make
the changes minimal in the book. There are no duplicate elements here (in a finite field).

Paul



---

archive/issue_comments_091411.json:
```json
{
    "body": "The identity list comprehension doesn't add anything to the understanding here. Why not\n\n```\nSet([ s for s in [r for r in R]))\n```\n\nto make it really really explicit? :-P  \n\nIf anything, this teaches bad habits. The only valid argument imho is that nobody is going to actually look into the sage.tests directory to learn how to use Sage. So I don't really care here but I would never let this stand in a doctest that is visible in the manual.",
    "created_at": "2012-06-18T14:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91411",
    "user": "vbraun"
}
```

The identity list comprehension doesn't add anything to the understanding here. Why not

```
Set([ s for s in [r for r in R]))
```

to make it really really explicit? :-P  

If anything, this teaches bad habits. The only valid argument imho is that nobody is going to actually look into the sage.tests directory to learn how to use Sage. So I don't really care here but I would never let this stand in a doctest that is visible in the manual.



---

archive/issue_comments_091412.json:
```json
{
    "body": "I'm getting testing failures on sage-5.1.beta5 (this worked fine on beta3, but the `cholesky()` method is new in beta5):\n\n```\n[vbraun@volker-desktop matrix]$ sage -t sage/matrix/matrix2.pyx\nsage -t  \"devel/sage-main/sage/matrix/matrix2.pyx\"          \n**********************************************************************\nFile \"/home/vbraun/opt/sage-5.1.beta5/devel/sage-main/sage/matrix/matrix2.pyx\", line 9813:\n    sage: L\nExpected:\n    [            3             0             0]\n    [    4*a^2 + 1             1             0]\n    [      3*a + 2 a^2 + 2*a + 3             3]\nGot:\n    [            2             0             0]\n    [      a^2 + 4             1             0]\n    [      2*a + 3 a^2 + 2*a + 3             2]\n**********************************************************************\n1 items had failures:\n   1 of  65 in __main__.example_105\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/vbraun/.sage//tmp/matrix2_12014.py\n\t [12.8 s]\n```\n",
    "created_at": "2012-06-21T15:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91412",
    "user": "vbraun"
}
```

I'm getting testing failures on sage-5.1.beta5 (this worked fine on beta3, but the `cholesky()` method is new in beta5):

```
[vbraun@volker-desktop matrix]$ sage -t sage/matrix/matrix2.pyx
sage -t  "devel/sage-main/sage/matrix/matrix2.pyx"          
**********************************************************************
File "/home/vbraun/opt/sage-5.1.beta5/devel/sage-main/sage/matrix/matrix2.pyx", line 9813:
    sage: L
Expected:
    [            3             0             0]
    [    4*a^2 + 1             1             0]
    [      3*a + 2 a^2 + 2*a + 3             3]
Got:
    [            2             0             0]
    [      a^2 + 4             1             0]
    [      2*a + 3 a^2 + 2*a + 3             2]
**********************************************************************
1 items had failures:
   1 of  65 in __main__.example_105
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/vbraun/.sage//tmp/matrix2_12014.py
	 [12.8 s]
```




---

archive/issue_comments_091413.json:
```json
{
    "body": "Compiles fine, but one failure with the testsuite on mark/skynet (SPARC solaris)\n\n```\n/bin/bash ../libtool --tag=CXX   --mode=link g++ -O0 -Wall -g -DNDEBUG -UGIVARO_DEBUG -UDEBUG -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include  -fPIC -I\"/home/vbraun/opt/mark/sage-5.1.beta3/local/include\" -static   -o te\nst-trunc test-trunc.o  -L../src -L../src/.libs -lgivaro -L/home/vbraun/opt/mark/sage-5.1.beta3/local//lib -lgmpxx -lgmp -L/home/vbraun/opt/mark/sage-5.1.beta3/local//lib -lgmpxx -lgmp\nlibtool: link: g++ -O0 -Wall -g -DNDEBUG -UGIVARO_DEBUG -UDEBUG -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include -fPIC -I/home/vbraun/opt/mark/sage-5.1.beta3/local/include -o test-trunc test-trunc.o  -L../src -L../src/.l\nibs /home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/src/.libs/libgivaro.a -L/home/vbraun/opt/mark/sage-5.1.beta3/local//lib /home/vbraun/opt/mark/sage-5.1.beta3/local/lib/libgmpxx.so /home/vbraun/opt/mark/sag\ne-5.1.beta3/local/lib/libstdc++.so -lm /home/vbraun/opt/mark/sage-5.1.beta3/local/lib/libgmp.so -Wl,-R -Wl,/home/vbraun/opt/mark/sage-5.1.beta3/local/lib -Wl,-R -Wl,/home/vbraun/opt/mark/sage-5.1.beta3/local/lib\nld: warning: file /home/vbraun/opt/mark/sage-5.1.beta3/local//lib/libstdc++.so: linked to /home/vbraun/opt/mark/sage-5.1.beta3/local/lib/libstdc++.so: attempted multiple inclusion of file\ng++ -DHAVE_CONFIG_H -I. -I..  -I..  -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include -I../src/kernel/system -I../src/kernel/memory -I../src/kernel/zpz -I../src/kernel/integer -I../src/kernel -I../src/library/poly1 -I../s\nrc/kernel/bstruct -I../src/library/tools  -O0 -Wall -g -DNDEBUG -UGIVARO_DEBUG -UDEBUG -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include  -fPIC -I\"/home/vbraun/opt/mark/sage-5.1.beta3/local/include\" -c -o test-crt.o test-\ncrt.C\n```\n\nlooks good but then further down\n\n```\nPASS: test-trunc\n/bin/bash: line 5: 12309 Bus Error               (core dumped) ${dir}$tst\nFAIL: test-crt\nPASS: test-geom\nPASS: test-integer\nPASS: test-conversion\nPASS: test-ratrecon\n=============================================\n1 of 12 tests failed\nPlease report to Jean-Guillaume.Dumas@imag.fr\n=============================================\nmake[3]: *** [check-TESTS] Error 1\nmake[3]: Leaving directory `/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests'\nmake[2]: *** [check-am] Error 2\nmake[2]: Leaving directory `/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests'\nmake[1]: *** [check-recursive] Error 1\nmake[1]: Leaving directory `/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests'\nmake: *** [check-recursive] Error 1\nError while running the Givaro testsuite ... exiting\n```\n",
    "created_at": "2012-06-22T12:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91413",
    "user": "vbraun"
}
```

Compiles fine, but one failure with the testsuite on mark/skynet (SPARC solaris)

```
/bin/bash ../libtool --tag=CXX   --mode=link g++ -O0 -Wall -g -DNDEBUG -UGIVARO_DEBUG -UDEBUG -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include  -fPIC -I"/home/vbraun/opt/mark/sage-5.1.beta3/local/include" -static   -o te
st-trunc test-trunc.o  -L../src -L../src/.libs -lgivaro -L/home/vbraun/opt/mark/sage-5.1.beta3/local//lib -lgmpxx -lgmp -L/home/vbraun/opt/mark/sage-5.1.beta3/local//lib -lgmpxx -lgmp
libtool: link: g++ -O0 -Wall -g -DNDEBUG -UGIVARO_DEBUG -UDEBUG -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include -fPIC -I/home/vbraun/opt/mark/sage-5.1.beta3/local/include -o test-trunc test-trunc.o  -L../src -L../src/.l
ibs /home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/src/.libs/libgivaro.a -L/home/vbraun/opt/mark/sage-5.1.beta3/local//lib /home/vbraun/opt/mark/sage-5.1.beta3/local/lib/libgmpxx.so /home/vbraun/opt/mark/sag
e-5.1.beta3/local/lib/libstdc++.so -lm /home/vbraun/opt/mark/sage-5.1.beta3/local/lib/libgmp.so -Wl,-R -Wl,/home/vbraun/opt/mark/sage-5.1.beta3/local/lib -Wl,-R -Wl,/home/vbraun/opt/mark/sage-5.1.beta3/local/lib
ld: warning: file /home/vbraun/opt/mark/sage-5.1.beta3/local//lib/libstdc++.so: linked to /home/vbraun/opt/mark/sage-5.1.beta3/local/lib/libstdc++.so: attempted multiple inclusion of file
g++ -DHAVE_CONFIG_H -I. -I..  -I..  -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include -I../src/kernel/system -I../src/kernel/memory -I../src/kernel/zpz -I../src/kernel/integer -I../src/kernel -I../src/library/poly1 -I../s
rc/kernel/bstruct -I../src/library/tools  -O0 -Wall -g -DNDEBUG -UGIVARO_DEBUG -UDEBUG -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include  -fPIC -I"/home/vbraun/opt/mark/sage-5.1.beta3/local/include" -c -o test-crt.o test-
crt.C
```

looks good but then further down

```
PASS: test-trunc
/bin/bash: line 5: 12309 Bus Error               (core dumped) ${dir}$tst
FAIL: test-crt
PASS: test-geom
PASS: test-integer
PASS: test-conversion
PASS: test-ratrecon
=============================================
1 of 12 tests failed
Please report to Jean-Guillaume.Dumas@imag.fr
=============================================
make[3]: *** [check-TESTS] Error 1
make[3]: Leaving directory `/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests'
make[2]: *** [check-am] Error 2
make[2]: Leaving directory `/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests'
make[1]: *** [check-recursive] Error 1
make[1]: Leaving directory `/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests'
make: *** [check-recursive] Error 1
Error while running the Givaro testsuite ... exiting
```




---

archive/issue_comments_091414.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-06-24T15:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91414",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_091415.json:
```json
{
    "body": "I rebased the patch to 5.1.beta5. In particular, this patch removes the line from `matrix2.pyx` that producses the offending output\n\n```\nsage -t  \"devel/sage-main/sage/matrix/matrix2.pyx\"          \n**********************************************************************\nFile \"/home/vbraun/opt/sage-5.1.beta5/devel/sage-main/sage/matrix/matrix2.pyx\", line 9813:\n    sage: L\nExpected:\n    [            3             0             0]\n    [    4*a^2 + 1             1             0]\n    [      3*a + 2 a^2 + 2*a + 3             3]\nGot:\n    [            2             0             0]\n    [      a^2 + 4             1             0]\n    [      2*a + 3 a^2 + 2*a + 3             2]\n**********************************************************************\n```\n\nThe Cholesky decomposition is not unique over finite fields and we shouldn't test for the output (which can be random depending on which square-root is chosen) but test for L*L<sup>T</sup> == A. This is done by the line after the line removed in this patch. Hence, correctness is checked. Note that I discussed this off-list Rob Beezer who is the author of the line removed in this patch.",
    "created_at": "2012-06-24T15:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91415",
    "user": "malb"
}
```

I rebased the patch to 5.1.beta5. In particular, this patch removes the line from `matrix2.pyx` that producses the offending output

```
sage -t  "devel/sage-main/sage/matrix/matrix2.pyx"          
**********************************************************************
File "/home/vbraun/opt/sage-5.1.beta5/devel/sage-main/sage/matrix/matrix2.pyx", line 9813:
    sage: L
Expected:
    [            3             0             0]
    [    4*a^2 + 1             1             0]
    [      3*a + 2 a^2 + 2*a + 3             3]
Got:
    [            2             0             0]
    [      a^2 + 4             1             0]
    [      2*a + 3 a^2 + 2*a + 3             2]
**********************************************************************
```

The Cholesky decomposition is not unique over finite fields and we shouldn't test for the output (which can be random depending on which square-root is chosen) but test for L*L<sup>T</sup> == A. This is done by the line after the line removed in this patch. Hence, correctness is checked. Note that I discussed this off-list Rob Beezer who is the author of the line removed in this patch.



---

archive/issue_comments_091416.json:
```json
{
    "body": "Replying to [comment:32 vbraun]:\n> {{{\n> PASS: test-trunc\n> /bin/bash: line 5: 12309 Bus Error               (core dumped) ${dir}$tst\n> FAIL: test-crt\n> }}}\n\nShall we set this to **needs work** then? What's our policy for stuff like this?",
    "created_at": "2012-06-24T15:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91416",
    "user": "malb"
}
```

Replying to [comment:32 vbraun]:
> {{{
> PASS: test-trunc
> /bin/bash: line 5: 12309 Bus Error               (core dumped) ${dir}$tst
> FAIL: test-crt
> }}}

Shall we set this to **needs work** then? What's our policy for stuff like this?



---

archive/issue_comments_091417.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-06-24T15:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91417",
    "user": "vbraun"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_091418.json:
```json
{
    "body": "I talked to Jean-Guillaume and he gave me an experimental patch but it didn't help. Here is the gdb backtrace\n\n```\n-bash-3.00$ /home/vbraun/opt/mark/gdb-7.4.1/gdb/gdb test-crt\nGNU gdb (GDB) 7.4.1\nCopyright (C) 2012 Free Software Foundation, Inc.\nLicense GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.  Type \"show copying\"\nand \"show warranty\" for details.\nThis GDB was configured as \"sparc-sun-solaris2.10\".\nFor bug reporting instructions, please see:\n<http://www.gnu.org/software/gdb/bugs/>...\nReading symbols from\n/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests/test-crt...done.\n(gdb) run\nStarting program:\n/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests/test-crt\n[Thread debugging using libthread_db enabled]\n[New Thread 1 (LWP 1)]\n\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread 1 (LWP 1)]\n0x00029030 in Givaro::GFqDom<long>::GFqDom (this=0x7eaec, F=...)\n   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givgfq.h:100\n100                     _dcharacteristic = F._dcharacteristic;\n(gdb) bt\n#0  0x00029030 in Givaro::GFqDom<long>::GFqDom (this=0x7eaec, F=...)\n   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givgfq.h:100\n#1  0x00033c3c in Givaro::GivaroMM<Givaro::GFqDom<long> >::initone\n(p=0x7eaec, V=...)\n   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givaromm.h:297\n#2  0x00031110 in Givaro::GivaroMM<Givaro::GFqDom<long> >::initialize\n(bloc=0x7eaec, s=15, V=...)\n   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givaromm.h:300\n#3  0x000268f8 in Givaro::Array0<Givaro::GFqDom<long> >::build\n(this=0xffbff890, s=15, t=...)\n   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givarray0.inl:30\n#4  0x00021ad0 in Givaro::Array0<Givaro::GFqDom<long> >::Array0\n(this=0xffbff890, s=15)\n   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givarray0.inl:39\n#5  0x0001bf04 in tmain<Givaro::GFqDom<long> > (argc=1,\nargv=0xffbffb3c, generator=...) at test-crt.C:49\n#6  0x00013d00 in main (argc=1, argv=0xffbffb3c) at test-crt.C:151\n(gdb) l\n95              {\n96                      zero = F.zero;\n97                      one = F.one;\n98                      mOne = F.mOne;\n99                      _characteristic = F._characteristic;\n100                     _dcharacteristic = F._dcharacteristic;\n101                     _exponent = F._exponent;\n102                     _irred = F._irred;\n103                     _q = F._q;\n104                     _qm1 = F._qm1;\n```\n\nI think we should at least wait a bit more if he can come up with a working patch.",
    "created_at": "2012-06-24T15:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91418",
    "user": "vbraun"
}
```

I talked to Jean-Guillaume and he gave me an experimental patch but it didn't help. Here is the gdb backtrace

```
-bash-3.00$ /home/vbraun/opt/mark/gdb-7.4.1/gdb/gdb test-crt
GNU gdb (GDB) 7.4.1
Copyright (C) 2012 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "sparc-sun-solaris2.10".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from
/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests/test-crt...done.
(gdb) run
Starting program:
/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests/test-crt
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 1 (LWP 1)]
0x00029030 in Givaro::GFqDom<long>::GFqDom (this=0x7eaec, F=...)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givgfq.h:100
100                     _dcharacteristic = F._dcharacteristic;
(gdb) bt
#0  0x00029030 in Givaro::GFqDom<long>::GFqDom (this=0x7eaec, F=...)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givgfq.h:100
#1  0x00033c3c in Givaro::GivaroMM<Givaro::GFqDom<long> >::initone
(p=0x7eaec, V=...)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givaromm.h:297
#2  0x00031110 in Givaro::GivaroMM<Givaro::GFqDom<long> >::initialize
(bloc=0x7eaec, s=15, V=...)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givaromm.h:300
#3  0x000268f8 in Givaro::Array0<Givaro::GFqDom<long> >::build
(this=0xffbff890, s=15, t=...)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givarray0.inl:30
#4  0x00021ad0 in Givaro::Array0<Givaro::GFqDom<long> >::Array0
(this=0xffbff890, s=15)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givarray0.inl:39
#5  0x0001bf04 in tmain<Givaro::GFqDom<long> > (argc=1,
argv=0xffbffb3c, generator=...) at test-crt.C:49
#6  0x00013d00 in main (argc=1, argv=0xffbffb3c) at test-crt.C:151
(gdb) l
95              {
96                      zero = F.zero;
97                      one = F.one;
98                      mOne = F.mOne;
99                      _characteristic = F._characteristic;
100                     _dcharacteristic = F._dcharacteristic;
101                     _exponent = F._exponent;
102                     _irred = F._irred;
103                     _q = F._q;
104                     _qm1 = F._qm1;
```

I think we should at least wait a bit more if he can come up with a working patch.



---

archive/issue_comments_091419.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-06-25T21:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91419",
    "user": "vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_091420.json:
```json
{
    "body": "The alignment problem stems from the use of placement new in the Givaro array class. Since we currently do not use that in Sage, there is no reason to delay this ticket further. I've created another ticket (#13164) to deal with the SPARC failure.\n\nPositive review.",
    "created_at": "2012-06-25T21:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91420",
    "user": "vbraun"
}
```

The alignment problem stems from the use of placement new in the Givaro array class. Since we currently do not use that in Sage, there is no reason to delay this ticket further. I've created another ticket (#13164) to deal with the SPARC failure.

Positive review.



---

archive/issue_comments_091421.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-06-26T15:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91421",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_091422.json:
```json
{
    "body": "From the spkg-install:\n\n```\nif [ -f \"$SAGE_ROOT\"/devel/sage/sage/rings/polynomial/multi_polynomial_ideal_libsingular.pyx ]; then\n    echo \"Touching extensions linked against Givaro\"\n    touch \"$SAGE_ROOT\"/devel/sage/sage/rings/finite_field_givaro.pyx\n    touch \"$SAGE_ROOT\"/devel/sage/sage/libs/linbox/linbox.pyx\n    touch \"$SAGE_ROOT\"/devel/sage/sage/libs/singular/singular.pyx\n    touch \"$SAGE_ROOT\"/devel/sage/sage/matrix/matrix_mpolynomial_dense.pyx\n    touch \"$SAGE_ROOT\"/devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx\n    touch \"$SAGE_ROOT\"/devel/sage/sage/rings/polynomial/multi_polynomial_ideal_libsingular.pyx\nfi\n```\n\nSo **THIS** is the reason why `sage/rings/finite_field_givaro.pyx` magically reappears once in a while. This file has been renamed a long time ago but whenever you reinstall givaro it is recreated. Our setup stuff does take care of recompiling dependent Cython classes, so this whole section is useless. Can you take it out before we ship it?",
    "created_at": "2012-06-26T15:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91422",
    "user": "vbraun"
}
```

From the spkg-install:

```
if [ -f "$SAGE_ROOT"/devel/sage/sage/rings/polynomial/multi_polynomial_ideal_libsingular.pyx ]; then
    echo "Touching extensions linked against Givaro"
    touch "$SAGE_ROOT"/devel/sage/sage/rings/finite_field_givaro.pyx
    touch "$SAGE_ROOT"/devel/sage/sage/libs/linbox/linbox.pyx
    touch "$SAGE_ROOT"/devel/sage/sage/libs/singular/singular.pyx
    touch "$SAGE_ROOT"/devel/sage/sage/matrix/matrix_mpolynomial_dense.pyx
    touch "$SAGE_ROOT"/devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx
    touch "$SAGE_ROOT"/devel/sage/sage/rings/polynomial/multi_polynomial_ideal_libsingular.pyx
fi
```

So **THIS** is the reason why `sage/rings/finite_field_givaro.pyx` magically reappears once in a while. This file has been renamed a long time ago but whenever you reinstall givaro it is recreated. Our setup stuff does take care of recompiling dependent Cython classes, so this whole section is useless. Can you take it out before we ship it?



---

archive/issue_comments_091423.json:
```json
{
    "body": "Fixed\n\n  https://bitbucket.org/malb/givaro-spkg/changeset/a7631e395f36\n\nI also uploaded a new SPKG.",
    "created_at": "2012-06-26T16:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91423",
    "user": "malb"
}
```

Fixed

  https://bitbucket.org/malb/givaro-spkg/changeset/a7631e395f36

I also uploaded a new SPKG.



---

archive/issue_comments_091424.json:
```json
{
    "body": "Your repository isn't public, I think. I get an error when following the link.",
    "created_at": "2012-06-26T18:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91424",
    "user": "vbraun"
}
```

Your repository isn't public, I think. I get an error when following the link.



---

archive/issue_comments_091425.json:
```json
{
    "body": "Ok looks good!",
    "created_at": "2012-06-26T19:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91425",
    "user": "vbraun"
}
```

Ok looks good!



---

archive/issue_comments_091426.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-06-26T19:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91426",
    "user": "vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_091427.json:
```json
{
    "body": "Replying to [comment:39 vbraun]:\n> So **THIS** is the reason why `sage/rings/finite_field_givaro.pyx` magically reappears once in a while. This file has been renamed a long time ago but whenever you reinstall givaro it is recreated. Our setup stuff does take care of recompiling dependent Cython classes, so this whole section is useless. Can you take it out before we ship it?\n\nThis was supposed to be fixed in #12761 (merged in sage-5.0.1.rc1 and sage-5.1.beta4 and clearly mentioned in the comments and dependencies of this ticket!), so your spkg should be rebased to that.",
    "created_at": "2012-06-27T07:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91427",
    "user": "jdemeyer"
}
```

Replying to [comment:39 vbraun]:
> So **THIS** is the reason why `sage/rings/finite_field_givaro.pyx` magically reappears once in a while. This file has been renamed a long time ago but whenever you reinstall givaro it is recreated. Our setup stuff does take care of recompiling dependent Cython classes, so this whole section is useless. Can you take it out before we ship it?

This was supposed to be fixed in #12761 (merged in sage-5.0.1.rc1 and sage-5.1.beta4 and clearly mentioned in the comments and dependencies of this ticket!), so your spkg should be rebased to that.



---

archive/issue_comments_091428.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-06-27T07:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91428",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_091429.json:
```json
{
    "body": "I've merged the two SPKGs here:\n\n  https://bitbucket.org/malb/givaro-spkg/changeset/9b0324505f18\n\nI've also uploaded a new SPKG (MD5: `7db046ff7fcb737234e41fcb2e15f94f`).\n\nNote that Givaro 3.7.0 is GCC 4.7. compliant (at least it compiles on my machine which has GCC 4.7).",
    "created_at": "2012-06-27T10:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91429",
    "user": "malb"
}
```

I've merged the two SPKGs here:

  https://bitbucket.org/malb/givaro-spkg/changeset/9b0324505f18

I've also uploaded a new SPKG (MD5: `7db046ff7fcb737234e41fcb2e15f94f`).

Note that Givaro 3.7.0 is GCC 4.7. compliant (at least it compiles on my machine which has GCC 4.7).



---

archive/issue_comments_091430.json:
```json
{
    "body": "What about `givtablelimits.h.patch`? Arguable we don't care about Cygwin any more but then it seems like it can't hurt either. Opinions?",
    "created_at": "2012-06-27T10:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91430",
    "user": "vbraun"
}
```

What about `givtablelimits.h.patch`? Arguable we don't care about Cygwin any more but then it seems like it can't hurt either. Opinions?



---

archive/issue_comments_091431.json:
```json
{
    "body": "TBH, I don't care either way.",
    "created_at": "2012-06-27T15:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91431",
    "user": "malb"
}
```

TBH, I don't care either way.



---

archive/issue_comments_091432.json:
```json
{
    "body": "Replying to [comment:46 malb]:\n> TBH, I don't care either way.\nWell, if you *remove* a patch, you should have a reason for it...",
    "created_at": "2012-06-27T15:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91432",
    "user": "jdemeyer"
}
```

Replying to [comment:46 malb]:
> TBH, I don't care either way.
Well, if you *remove* a patch, you should have a reason for it...



---

archive/issue_comments_091433.json:
```json
{
    "body": "I'm fine without the Cygwin patch, its rather ugly ihmo.",
    "created_at": "2012-06-27T15:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91433",
    "user": "vbraun"
}
```

I'm fine without the Cygwin patch, its rather ugly ihmo.



---

archive/issue_comments_091434.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-06-27T15:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91434",
    "user": "vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_091435.json:
```json
{
    "body": "Diff between the 3.2.13.p0 (#12761) and 3.7.0 givaro spkgs. For review only.",
    "created_at": "2012-06-27T20:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91435",
    "user": "jdemeyer"
}
```

Diff between the 3.2.13.p0 (#12761) and 3.7.0 givaro spkgs. For review only.



---

archive/issue_comments_091436.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-06-27T20:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91436",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_091437.json:
```json
{
    "body": "Attachment\n\nYou should keep the\n\n```\necho >&2 Error\n```\n\ninstead of \n\n```\necho Error\n```\n\nand also the Cygwin patch and the `$SAGE_LOCAL` quoting (i.e. don't undo something from givaro-3.2.13 unless you have a reason too).",
    "created_at": "2012-06-27T20:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91437",
    "user": "jdemeyer"
}
```

Attachment

You should keep the

```
echo >&2 Error
```

instead of 

```
echo Error
```

and also the Cygwin patch and the `$SAGE_LOCAL` quoting (i.e. don't undo something from givaro-3.2.13 unless you have a reason too).



---

archive/issue_comments_091438.json:
```json
{
    "body": "Quote and echo business fixed in:\n\n  https://bitbucket.org/malb/givaro-spkg/changeset/d9b1505bb161\n\nAs far as I can tell Cygwin fixes are not needed any more:\n\n  https://lists.gnu.org/archive/html/bug-gnulib/2010-03/msg00217.html",
    "created_at": "2012-06-27T21:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91438",
    "user": "malb"
}
```

Quote and echo business fixed in:

  https://bitbucket.org/malb/givaro-spkg/changeset/d9b1505bb161

As far as I can tell Cygwin fixes are not needed any more:

  https://lists.gnu.org/archive/html/bug-gnulib/2010-03/msg00217.html



---

archive/issue_comments_091439.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-06-27T21:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91439",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091440.json:
```json
{
    "body": "Looks good to me!",
    "created_at": "2012-06-27T21:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91440",
    "user": "vbraun"
}
```

Looks good to me!



---

archive/issue_comments_091441.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-27T21:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91441",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091442.json:
```json
{
    "body": "This needs to be rebased to [sage-5.3.beta1](http://boxen.math.washington.edu/home/release/sage-5.3.beta1/) (to be released very soon).",
    "created_at": "2012-08-12T21:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91442",
    "user": "jdemeyer"
}
```

This needs to be rebased to [sage-5.3.beta1](http://boxen.math.washington.edu/home/release/sage-5.3.beta1/) (to be released very soon).



---

archive/issue_comments_091443.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-08-12T21:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91443",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_091444.json:
```json
{
    "body": "Rebased patch",
    "created_at": "2012-08-14T02:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91444",
    "user": "vbraun"
}
```

Rebased patch



---

archive/issue_comments_091445.json:
```json
{
    "body": "Attachment\n\nRebased patch for sage-5.3.beta1. Just a trivial rebase in `module_list.py`.",
    "created_at": "2012-08-14T02:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91445",
    "user": "vbraun"
}
```

Attachment

Rebased patch for sage-5.3.beta1. Just a trivial rebase in `module_list.py`.



---

archive/issue_comments_091446.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-08-14T02:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91446",
    "user": "vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_091447.json:
```json
{
    "body": "Volker, could you tag the last hg commit here as well?",
    "created_at": "2012-08-20T22:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91447",
    "user": "jpflori"
}
```

Volker, could you tag the last hg commit here as well?



---

archive/issue_comments_091448.json:
```json
{
    "body": "I thought that Jeroen's scripts for Sage releases added those tags automatically, but I'm not sure.",
    "created_at": "2012-08-20T22:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91448",
    "user": "jhpalmieri"
}
```

I thought that Jeroen's scripts for Sage releases added those tags automatically, but I'm not sure.



---

archive/issue_comments_091449.json:
```json
{
    "body": "I haven't made any changes to the spkg yet, so I'm not going to partake in the bikeshedding here. The Sage developer guide contains nothing about mandatory hg tagging. In fact, since we frequently make changes in response to reviews before releasing the spkg, really only the release manager can set the tag.",
    "created_at": "2012-08-21T02:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91449",
    "user": "vbraun"
}
```

I haven't made any changes to the spkg yet, so I'm not going to partake in the bikeshedding here. The Sage developer guide contains nothing about mandatory hg tagging. In fact, since we frequently make changes in response to reviews before releasing the spkg, really only the release manager can set the tag.



---

archive/issue_comments_091450.json:
```json
{
    "body": "Replying to [comment:60 jhpalmieri]:\n> I thought that Jeroen's scripts for Sage releases added those tags automatically\nIndeed.",
    "created_at": "2012-08-21T09:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91450",
    "user": "jdemeyer"
}
```

Replying to [comment:60 jhpalmieri]:
> I thought that Jeroen's scripts for Sage releases added those tags automatically
Indeed.



---

archive/issue_comments_091451.json:
```json
{
    "body": "Superseded by #13164.",
    "created_at": "2012-08-24T12:06:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91451",
    "user": "vbraun"
}
```

Superseded by #13164.



---

archive/issue_comments_091452.json:
```json
{
    "body": "Is the Sage library patch still necessary? If so, maybe it should be moved to #13164 and this ticket should be closed as a duplicate.",
    "created_at": "2012-08-24T15:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91452",
    "user": "jhpalmieri"
}
```

Is the Sage library patch still necessary? If so, maybe it should be moved to #13164 and this ticket should be closed as a duplicate.



---

archive/issue_comments_091453.json:
```json
{
    "body": "I did not try without it (in fact I did but without the linbox patches as well, by mistake), but with it there are no errors.",
    "created_at": "2012-08-24T15:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91453",
    "user": "jpflori"
}
```

I did not try without it (in fact I did but without the linbox patches as well, by mistake), but with it there are no errors.



---

archive/issue_comments_091454.json:
```json
{
    "body": "Superseded by #13164, close this ticket as duplicate.",
    "created_at": "2012-08-25T17:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91454",
    "user": "vbraun"
}
```

Superseded by #13164, close this ticket as duplicate.



---

archive/issue_comments_091455.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-09-05T09:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9511#issuecomment-91455",
    "user": "jdemeyer"
}
```

Resolution: duplicate
