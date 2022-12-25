# Issue 4148: Upgrade to givaro-3.2.13rc1

archive/issues_004148.json:
```json
{
    "body": "Assignee: @ClementPernet\n\nUpgrade the givaro spkg to upstream version 3.2.13rc1.\nThis is required for the resolution of ticket #4147 and is therefore a defect.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4148\n\n",
    "created_at": "2008-09-19T00:39:53Z",
    "labels": [
        "component: finite rings",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Upgrade to givaro-3.2.13rc1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4148",
    "user": "https://github.com/ClementPernet"
}
```
Assignee: @ClementPernet

Upgrade the givaro spkg to upstream version 3.2.13rc1.
This is required for the resolution of ticket #4147 and is therefore a defect.

Issue created by migration from https://trac.sagemath.org/ticket/4148





---

archive/issue_comments_030042.json:
```json
{
    "body": "The proposed spkg is here:\n[http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc1.spkg](http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc1.spkg)\n\nAlready succesfully tested on sage.math and on my x86_32 Linux box.",
    "created_at": "2008-09-19T00:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4148#issuecomment-30042",
    "user": "https://github.com/ClementPernet"
}
```

The proposed spkg is here:
[http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc1.spkg](http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc1.spkg)

Already succesfully tested on sage.math and on my x86_32 Linux box.



---

archive/issue_comments_030043.json:
```json
{
    "body": "I have a pb compiling givaro on PPC-OSX, because endianness parameter __BYTE_ORDER is not defined there. I am working on it.",
    "created_at": "2008-09-19T01:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4148#issuecomment-30043",
    "user": "https://github.com/ClementPernet"
}
```

I have a pb compiling givaro on PPC-OSX, because endianness parameter __BYTE_ORDER is not defined there. I am working on it.



---

archive/issue_comments_030044.json:
```json
{
    "body": "I changed the endianess detection in Givaro, which fixed the problem.\nThe new spkg is here:\n\n[http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc2.spkg](http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc2.spkg)",
    "created_at": "2008-09-19T02:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4148#issuecomment-30044",
    "user": "https://github.com/ClementPernet"
}
```

I changed the endianess detection in Givaro, which fixed the problem.
The new spkg is here:

[http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc2.spkg](http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc2.spkg)



---

archive/issue_comments_030045.json:
```json
{
    "body": "Spkg looks good to me. I added some code to touch the extensions linked against Givaro so they are automatically rebuild when doing a \"sage -b\". The updated spkg is in\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha0/givaro-3.2.13rc1.spkg\n\nPositive review, but I am doing some more build testing to be sure the spkg actually works.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-20T01:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4148#issuecomment-30045",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg looks good to me. I added some code to touch the extensions linked against Givaro so they are automatically rebuild when doing a "sage -b". The updated spkg is in

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha0/givaro-3.2.13rc1.spkg

Positive review, but I am doing some more build testing to be sure the spkg actually works.

Cheers,

Michael



---

archive/issue_comments_030046.json:
```json
{
    "body": "Hhm, this spkg blows up on OSX 10.4 PPC as well as OSX 10.5 Intel with\n\n```\nMaking install in rational\n/bin/sh ../../../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I../../.. -I../../..   -I../../../src/kernel/integer -I../../../src/kernel -I../../../src/kernel/system -I../../../src/kernel/memory   -I/Users/mabshoff/sage-3.1.2.rc2/local//include  -fPIC -I\"/Users/mabshoff/sage-3.1.2.rc2/local/include\" -MT givratcstor.lo -MD -MP -MF .deps/givratcstor.Tpo -c -o givratcstor.lo givratcstor.C\n g++ -DHAVE_CONFIG_H -I. -I../../.. -I../../.. -I../../../src/kernel/integer -I../../../src/kernel -I../../../src/kernel/system -I../../../src/kernel/memory -I/Users/mabshoff/sage-3.1.2.rc2/local//include -fPIC -I/Users/mabshoff/sage-3.1.2.rc2/local/include -MT givratcstor.lo -MD -MP -MF .deps/givratcstor.Tpo -c givratcstor.C  -fno-common -DPIC -o .libs/givratcstor.o\ngivratcstor.C:45: error: declaration of \u2018uint64 ieee::mantissa\u2019\ngivratcstor.C:42: error: conflicts with previous declaration \u2018uint64 ieee::mantissa\u2019\ngivratcstor.C:46: error: declaration of \u2018uint64 ieee::exponent\u2019\ngivratcstor.C:41: error: conflicts with previous declaration \u2018uint64 ieee::exponent\u2019\ngivratcstor.C:47: error: declaration of \u2018uint64 ieee::negative\u2019\ngivratcstor.C:40: error: conflicts with previous declaration \u2018uint64 ieee::negative\u2019\nmake[5]: *** [givratcstor.lo] Error 1\nmake[4]: *** [install-recursive] Error 1\nmake[3]: *** [install-recursive] Error 1\nmake[2]: *** [install-recursive] Error 1\nError installing givaro\n```\n\nPlease make sure to base this spkg off the one I link above by the same name as yours.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-20T02:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4148#issuecomment-30046",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hhm, this spkg blows up on OSX 10.4 PPC as well as OSX 10.5 Intel with

```
Making install in rational
/bin/sh ../../../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I../../.. -I../../..   -I../../../src/kernel/integer -I../../../src/kernel -I../../../src/kernel/system -I../../../src/kernel/memory   -I/Users/mabshoff/sage-3.1.2.rc2/local//include  -fPIC -I"/Users/mabshoff/sage-3.1.2.rc2/local/include" -MT givratcstor.lo -MD -MP -MF .deps/givratcstor.Tpo -c -o givratcstor.lo givratcstor.C
 g++ -DHAVE_CONFIG_H -I. -I../../.. -I../../.. -I../../../src/kernel/integer -I../../../src/kernel -I../../../src/kernel/system -I../../../src/kernel/memory -I/Users/mabshoff/sage-3.1.2.rc2/local//include -fPIC -I/Users/mabshoff/sage-3.1.2.rc2/local/include -MT givratcstor.lo -MD -MP -MF .deps/givratcstor.Tpo -c givratcstor.C  -fno-common -DPIC -o .libs/givratcstor.o
givratcstor.C:45: error: declaration of ‘uint64 ieee::mantissa’
givratcstor.C:42: error: conflicts with previous declaration ‘uint64 ieee::mantissa’
givratcstor.C:46: error: declaration of ‘uint64 ieee::exponent’
givratcstor.C:41: error: conflicts with previous declaration ‘uint64 ieee::exponent’
givratcstor.C:47: error: declaration of ‘uint64 ieee::negative’
givratcstor.C:40: error: conflicts with previous declaration ‘uint64 ieee::negative’
make[5]: *** [givratcstor.lo] Error 1
make[4]: *** [install-recursive] Error 1
make[3]: *** [install-recursive] Error 1
make[2]: *** [install-recursive] Error 1
Error installing givaro
```

Please make sure to base this spkg off the one I link above by the same name as yours.

Cheers,

Michael



---

archive/issue_comments_030047.json:
```json
{
    "body": "Ok, the problem boils down to byte order detection being broken on OSX it seems:\n\n```\n#if     __BYTE_ORDER == __BIG_ENDIAN\n            uint64 negative:1;\n            uint64 exponent:11;\n            uint64 mantissa:52;\n#endif                          /* Big endian.  */\n#if     __BYTE_ORDER == __LITTLE_ENDIAN\n            uint64 mantissa:52;\n            uint64 exponent:11;\n            uint64 negative:1;\n#endif                          /* Little endian.  */\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-09-20T02:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4148#issuecomment-30047",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, the problem boils down to byte order detection being broken on OSX it seems:

```
#if     __BYTE_ORDER == __BIG_ENDIAN
            uint64 negative:1;
            uint64 exponent:11;
            uint64 mantissa:52;
#endif                          /* Big endian.  */
#if     __BYTE_ORDER == __LITTLE_ENDIAN
            uint64 mantissa:52;
            uint64 exponent:11;
            uint64 negative:1;
#endif                          /* Little endian.  */
```


Cheers,

Michael



---

archive/issue_comments_030048.json:
```json
{
    "body": "Ooops, as Clement just pointed out to me I picked the wrong spkg. The one at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha0/givaro-3.2.13rc2.spkg\n\nbased on his spkg has the extension rebuild fix and builds fine for me and passes doctests on various platforms from OSX, Linux in various flavors and Solaris. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-20T02:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4148#issuecomment-30048",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ooops, as Clement just pointed out to me I picked the wrong spkg. The one at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha0/givaro-3.2.13rc2.spkg

based on his spkg has the extension rebuild fix and builds fine for me and passes doctests on various platforms from OSX, Linux in various flavors and Solaris. Positive review.

Cheers,

Michael



---

archive/issue_comments_030049.json:
```json
{
    "body": "This is rc2 :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-20T02:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4148#issuecomment-30049",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is rc2 :)

Cheers,

Michael



---

archive/issue_comments_030050.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha0",
    "created_at": "2008-09-20T02:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4148#issuecomment-30050",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha0



---

archive/issue_comments_030051.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-20T02:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4148#issuecomment-30051",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
