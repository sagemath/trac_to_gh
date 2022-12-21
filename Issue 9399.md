# Issue 9399: Remove Sun-specific junk in rings/finite_rings/stdint.h

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-07-01 01:22:19

Assignee: drkirkby

CC:  jsp jhpalmieri

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



---

Comment by drkirkby created at 2010-07-01 12:47:22

With the attached patch, Sage builds on both 32-bit SPARC (like t2) in 32-bit and on OpenSolaris as 64-bit. I can only assume this was added at some point in the past to attempt to build Sage on Solaris 9, which would not have this header file. But even Solaris 10 03/05 (the first verison of Solaris 10) has this header file

Dave


---

Attachment

Ensure the header file is included on all systems, not excluding Solaris as before.


---

Comment by drkirkby created at 2010-07-01 12:48:45

Changing status from new to needs_review.


---

Comment by mariah created at 2010-07-02 14:07:05

1. patch applied on skynet/taurus to sage-4.4.4.1
2. ./sage -b done
3. make testall

All test passed.  Postive review!


---

Comment by mariah created at 2010-07-02 14:07:05

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-08 19:07:14

Resolution: fixed
