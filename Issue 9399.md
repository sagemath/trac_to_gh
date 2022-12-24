# Issue 9399: Remove Sun-specific junk in rings/finite_rings/stdint.h

archive/issues_009399.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies @jhpalmieri\n\nThe file has this in it \n\n\n\n```\n#if defined(__sun)\ntypedef int int_fast32_t;\ntypedef long long int_fast64_t;\n#else\n#include <stdint.h>\n#endif\n\n#define INTEGER_MOD_INT32_LIMIT 46341          //  = ceil(sqrt(2^31-1))\n#define INTEGER_MOD_INT64_LIMIT 2147483647     //  = 2^31-1 for now, should be 3037000500LL = ceil(sqrt(2^63-1))\n```\n\n\nI can only assume someone added this Sun-specific code for a very old version of Solaris. Any Solaris 10 release will include the header file  <stdint.h>, so there is no need to have this. \n\nThe code as it stands conflicts with a Solaris header file, which defines int_fast64_t as being a 'long' and not a 'long long' in 64-bit mode. The code as show is only valid for 32-bit. \n\nThe following will save a few bytes, and will go further to advance the stage of a 64-bit Solaris port. \n\n\n```\n#include <stdint.h>\n\n#define INTEGER_MOD_INT32_LIMIT 46341          //  = ceil(sqrt(2^31-1))\n#define INTEGER_MOD_INT64_LIMIT 2147483647     //  = 2^31-1 for now, should be 3037000500LL = ceil(sqrt(2^63-1))\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9399\n\n",
    "created_at": "2010-07-01T01:22:19Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Remove Sun-specific junk in rings/finite_rings/stdint.h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9399",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies @jhpalmieri

The file has this in it 



```
#if defined(__sun)
typedef int int_fast32_t;
typedef long long int_fast64_t;
#else
#include <stdint.h>
#endif

#define INTEGER_MOD_INT32_LIMIT 46341          //  = ceil(sqrt(2^31-1))
#define INTEGER_MOD_INT64_LIMIT 2147483647     //  = 2^31-1 for now, should be 3037000500LL = ceil(sqrt(2^63-1))
```


I can only assume someone added this Sun-specific code for a very old version of Solaris. Any Solaris 10 release will include the header file  <stdint.h>, so there is no need to have this. 

The code as it stands conflicts with a Solaris header file, which defines int_fast64_t as being a 'long' and not a 'long long' in 64-bit mode. The code as show is only valid for 32-bit. 

The following will save a few bytes, and will go further to advance the stage of a 64-bit Solaris port. 


```
#include <stdint.h>

#define INTEGER_MOD_INT32_LIMIT 46341          //  = ceil(sqrt(2^31-1))
#define INTEGER_MOD_INT64_LIMIT 2147483647     //  = 2^31-1 for now, should be 3037000500LL = ceil(sqrt(2^63-1))
```


Issue created by migration from https://trac.sagemath.org/ticket/9399





---

archive/issue_comments_089523.json:
```json
{
    "body": "With the attached patch, Sage builds on both 32-bit SPARC (like t2) in 32-bit and on OpenSolaris as 64-bit. I can only assume this was added at some point in the past to attempt to build Sage on Solaris 9, which would not have this header file. But even Solaris 10 03/05 (the first verison of Solaris 10) has this header file\n\nDave",
    "created_at": "2010-07-01T12:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9399#issuecomment-89523",
    "user": "drkirkby"
}
```

With the attached patch, Sage builds on both 32-bit SPARC (like t2) in 32-bit and on OpenSolaris as 64-bit. I can only assume this was added at some point in the past to attempt to build Sage on Solaris 9, which would not have this header file. But even Solaris 10 03/05 (the first verison of Solaris 10) has this header file

Dave



---

archive/issue_comments_089524.json:
```json
{
    "body": "Attachment [9399.patch](tarball://root/attachments/some-uuid/ticket9399/9399.patch) by drkirkby created at 2010-07-01 12:48:30\n\nEnsure the header file is included on all systems, not excluding Solaris as before.",
    "created_at": "2010-07-01T12:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9399#issuecomment-89524",
    "user": "drkirkby"
}
```

Attachment [9399.patch](tarball://root/attachments/some-uuid/ticket9399/9399.patch) by drkirkby created at 2010-07-01 12:48:30

Ensure the header file is included on all systems, not excluding Solaris as before.



---

archive/issue_comments_089525.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-01T12:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9399#issuecomment-89525",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089526.json:
```json
{
    "body": "1. patch applied on skynet/taurus to sage-4.4.4.1\n2. ./sage -b done\n3. make testall\n\nAll test passed.  Postive review!",
    "created_at": "2010-07-02T14:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9399#issuecomment-89526",
    "user": "mariah"
}
```

1. patch applied on skynet/taurus to sage-4.4.4.1
2. ./sage -b done
3. make testall

All test passed.  Postive review!



---

archive/issue_comments_089527.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-02T14:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9399#issuecomment-89527",
    "user": "mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089528.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-08T19:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9399#issuecomment-89528",
    "user": "@rlmill"
}
```

Resolution: fixed
