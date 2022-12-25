# Issue 5278: On modern fedora 64 installs, sage exists frequently when omalloc things there is no memory left

archive/issues_005278.json:
```json
{
    "body": "Assignee: cwitty\n\nThis is show-stopper bug for using Sage on any modern install of Fedora.  It was discussed a lot in sage-devel.\n\nTo replicate this issue, install Sage on fedora 64-bit and run a doctest a few times.  Every so often (maybe 20% chance) it will exit with this error:\n\n```\nerror: no more memory\nSystem 0k:0k Appl 0k/0k Malloc 0k/0k Valloc 0k/0k Pages 0/0 Regions 0:0\n```\n\n\nTracing this through with print statements I found that this happens around line 370 of singular.spkg's omalloc/omAllocSystem.c (something similar was posted to sage-devel):\n\n```\nvoid* omAllocFromSystem(size_t size)\n{ \n  void* ptr;\n\n  ptr = OM_MALLOC_FROM_SYSTEM(size);\n  if (ptr == NULL)\n  { \n    OM_MEMORY_LOW_HOOK();\n    ptr = OM_MALLOC_FROM_SYSTEM(size);\n    if (ptr == NULL)\n         BOOM (crash handler called!)\n```\n\n\nThe first thing that is suspicious is that OM_MALLOC_FROM_SYSTEM is called, fails, and then is called again... for now reason.  That is very hackish code.  Tracing that through it seemed to me that OM_MALLOC_FROM_SYSTEM should just be the system malloc.\nTo test that theory I modified the above code as follows:\nvoid* omAllocFromSystem(size_t size)\n{ \n  void* ptr;\n\n  ptr = OM_MALLOC_FROM_SYSTEM(size);\n  if (ptr == NULL)\n  { \n    OM_MEMORY_LOW_HOOK();\n    ptr = OM_MALLOC_FROM_SYSTEM(size);\n    if (ptr == NULL)\n       ptr = malloc(size);\n       if (ptr == NULL)\n         BOOM (crash handler called!)\n}}}\n\nAfter making that change, the problem vanishes (for me) and doctesting works fine again, at least for me.  I haven't tested doctesting the whole tree.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5278\n\n",
    "created_at": "2009-02-15T18:35:51Z",
    "labels": [
        "component: misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "On modern fedora 64 installs, sage exists frequently when omalloc things there is no memory left",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5278",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

This is show-stopper bug for using Sage on any modern install of Fedora.  It was discussed a lot in sage-devel.

To replicate this issue, install Sage on fedora 64-bit and run a doctest a few times.  Every so often (maybe 20% chance) it will exit with this error:

```
error: no more memory
System 0k:0k Appl 0k/0k Malloc 0k/0k Valloc 0k/0k Pages 0/0 Regions 0:0
```


Tracing this through with print statements I found that this happens around line 370 of singular.spkg's omalloc/omAllocSystem.c (something similar was posted to sage-devel):

```
void* omAllocFromSystem(size_t size)
{ 
  void* ptr;

  ptr = OM_MALLOC_FROM_SYSTEM(size);
  if (ptr == NULL)
  { 
    OM_MEMORY_LOW_HOOK();
    ptr = OM_MALLOC_FROM_SYSTEM(size);
    if (ptr == NULL)
         BOOM (crash handler called!)
```


The first thing that is suspicious is that OM_MALLOC_FROM_SYSTEM is called, fails, and then is called again... for now reason.  That is very hackish code.  Tracing that through it seemed to me that OM_MALLOC_FROM_SYSTEM should just be the system malloc.
To test that theory I modified the above code as follows:
void* omAllocFromSystem(size_t size)
{ 
  void* ptr;

  ptr = OM_MALLOC_FROM_SYSTEM(size);
  if (ptr == NULL)
  { 
    OM_MEMORY_LOW_HOOK();
    ptr = OM_MALLOC_FROM_SYSTEM(size);
    if (ptr == NULL)
       ptr = malloc(size);
       if (ptr == NULL)
         BOOM (crash handler called!)
}}}

After making that change, the problem vanishes (for me) and doctesting works fine again, at least for me.  I haven't tested doctesting the whole tree.

Issue created by migration from https://trac.sagemath.org/ticket/5278





---

archive/issue_comments_040420.json:
```json
{
    "body": "> The first thing that is suspicious is that OM_MALLOC_FROM_SYSTEM is called, fails, and then is called again... for no reason.  That is very hackish code.\n\nI expect the idea is that OM_MEMORY_LOW_HOOK empties caches, etc., to free up memory before it tries again.  That seems like a good idea in theory; I have no idea if it actually does anything in Singular.\n\nAlso, if it thinks it's trying to allocate memory using sbrk, it may also think that it can free memory using sbrk, so this might have introduced a memory leak.  (If so, it may still be a good temporary fix... memory leaks are better than immediate crashes, IMHO.)",
    "created_at": "2009-02-15T19:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40420",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

> The first thing that is suspicious is that OM_MALLOC_FROM_SYSTEM is called, fails, and then is called again... for no reason.  That is very hackish code.

I expect the idea is that OM_MEMORY_LOW_HOOK empties caches, etc., to free up memory before it tries again.  That seems like a good idea in theory; I have no idea if it actually does anything in Singular.

Also, if it thinks it's trying to allocate memory using sbrk, it may also think that it can free memory using sbrk, so this might have introduced a memory leak.  (If so, it may still be a good temporary fix... memory leaks are better than immediate crashes, IMHO.)



---

archive/issue_comments_040421.json:
```json
{
    "body": "Hi all,\n\nI currently do not have access to Fedora or any Linux system at the moment, let alone a 64-bit system. But I do have seen some odd queer things in my past \"low level C years\" on embedded systems with all sort of crap architectures and compilers.\n\nMy proposals here would be to poke around along the lines of:\n\n- Is \"NULL\" really what you think here?\n\n- Do we compare against what we want to compare against?\n\nGiven a box, I would test certain code alternatives to \"if (ptr == NULL)\" as:\n\n```\nif (ptr == (void *)NULL)\n```\n\n\n```\nif (ptr == (void *)0x0)\n```\n\n\n```\nif ((void* )ptr == (void*)0x0)\n```\n\n\nI have seen environments where exactly one version was the one to be taken. And sometimes one has to read the assembler code to see what a compiler can wreak havoc to 100% correct ANSI C code ... but I have never read the GNU assembler language docs.\n\nAs far as \"hackish\" concerns, I think I can do worse than the above code:\n\n```\ndo {;} while(NULL == (ptr = OM_MALLOC_FROM_SYSTEM(size)));\n```\n\n\nBut seriously, from what I see perhaps all we need is to start some sort of timer in the \"OM_MEMORY_LOW_HOOK();\" to let the system recover from a situation where it couldn't give us the needed free memory on our first request. Or some other system-related magic that ensures that --- provided the memory is avaible at all :-) --- makes sure that the following call will be successful.\nThis C code does not seem to me so very hackish, after all, but even nicely customizable by the obvious hooks and macros.\n\nYeah, probably it's a good idea to check what the OM_MEMORY_LOW_HOOK() macro does do right now.\n\nCheers,gsw",
    "created_at": "2009-02-15T20:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40421",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hi all,

I currently do not have access to Fedora or any Linux system at the moment, let alone a 64-bit system. But I do have seen some odd queer things in my past "low level C years" on embedded systems with all sort of crap architectures and compilers.

My proposals here would be to poke around along the lines of:

- Is "NULL" really what you think here?

- Do we compare against what we want to compare against?

Given a box, I would test certain code alternatives to "if (ptr == NULL)" as:

```
if (ptr == (void *)NULL)
```


```
if (ptr == (void *)0x0)
```


```
if ((void* )ptr == (void*)0x0)
```


I have seen environments where exactly one version was the one to be taken. And sometimes one has to read the assembler code to see what a compiler can wreak havoc to 100% correct ANSI C code ... but I have never read the GNU assembler language docs.

As far as "hackish" concerns, I think I can do worse than the above code:

```
do {;} while(NULL == (ptr = OM_MALLOC_FROM_SYSTEM(size)));
```


But seriously, from what I see perhaps all we need is to start some sort of timer in the "OM_MEMORY_LOW_HOOK();" to let the system recover from a situation where it couldn't give us the needed free memory on our first request. Or some other system-related magic that ensures that --- provided the memory is avaible at all :-) --- makes sure that the following call will be successful.
This C code does not seem to me so very hackish, after all, but even nicely customizable by the obvious hooks and macros.

Yeah, probably it's a good idea to check what the OM_MEMORY_LOW_HOOK() macro does do right now.

Cheers,gsw



---

archive/issue_comments_040422.json:
```json
{
    "body": "> Also, if it thinks it's trying to allocate memory using sbrk, \n> it may also think that it can free memory using sbrk, so this \n> might have introduced a memory leak. (If so, it may still be \n> a good temporary fix... memory leaks are better than immediate crashes, IMHO.) \n\nSingular fails on a call to the OM_MALLOC_FROM_SYSTEM macro.  That macro is -- as the name suggests -- just supposed to be malloc *not* sbrk.  And, if you just look at the source you see:\n\n```\n#define OM_MALLOC_FROM_SYSTEM   OM_MALLOC_MALLOC\n```\n\nand in some places\n\n```\n#define OM_MALLOC_MALLOC   malloc\n```\n\nbut in other places:\n\n```\n#define OM_MALLOC_MALLOC   mALLOc\n```\n\nAnd mALLOc is define internally in various places to be\n\n```\ndlmalloc.h:#define mALLOc               __libc_malloc\ndlmalloc.h:#define mALLOc               malloc\n```\n\nbut it never has anything whatever to do with sbrk as far as I can tell.\n\nI'm actually puzzled since reading the source it seems to me that OM_MALLOC_FROM_SYSTEM should just be malloc.  However, obviously it isn't or my hack wouldn't fix the problem.  Notice that using OM_MALLOC_FROM_SYSTEM instead of malloc again in my hack does *not* fix the problem.",
    "created_at": "2009-02-16T03:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40422",
    "user": "https://github.com/williamstein"
}
```

> Also, if it thinks it's trying to allocate memory using sbrk, 
> it may also think that it can free memory using sbrk, so this 
> might have introduced a memory leak. (If so, it may still be 
> a good temporary fix... memory leaks are better than immediate crashes, IMHO.) 

Singular fails on a call to the OM_MALLOC_FROM_SYSTEM macro.  That macro is -- as the name suggests -- just supposed to be malloc *not* sbrk.  And, if you just look at the source you see:

```
#define OM_MALLOC_FROM_SYSTEM   OM_MALLOC_MALLOC
```

and in some places

```
#define OM_MALLOC_MALLOC   malloc
```

but in other places:

```
#define OM_MALLOC_MALLOC   mALLOc
```

And mALLOc is define internally in various places to be

```
dlmalloc.h:#define mALLOc               __libc_malloc
dlmalloc.h:#define mALLOc               malloc
```

but it never has anything whatever to do with sbrk as far as I can tell.

I'm actually puzzled since reading the source it seems to me that OM_MALLOC_FROM_SYSTEM should just be malloc.  However, obviously it isn't or my hack wouldn't fix the problem.  Notice that using OM_MALLOC_FROM_SYSTEM instead of malloc again in my hack does *not* fix the problem.



---

archive/issue_comments_040423.json:
```json
{
    "body": "But it looks like mALLOc might also be a regular function, defined in dlmalloc.c.  And that function calls malloc_extend_top(), which calls MORECORE, which may be defined to be sbrk.",
    "created_at": "2009-02-16T05:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40423",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

But it looks like mALLOc might also be a regular function, defined in dlmalloc.c.  And that function calls malloc_extend_top(), which calls MORECORE, which may be defined to be sbrk.



---

archive/issue_comments_040424.json:
```json
{
    "body": "Well, I tracked down one instance of this.  omalloc says there is no memory left when sbrk() (which is a wrapper for brk()) fails, like this:\n\n```\n23475 brk(0x22e6030)                    = 0x22e0000\n23475 brk(0x22e6030)                    = 0x22e0000\n```\n\nHere, brk() is trying (and failing) to allocate the memory between 0x22e0000 and 0x22e6030.\n\nThe reason is that the memory is already allocated, to hold a shared library.  Earlier in the same trace, we see:\n\n```\n23475 open(\"/scratch/wstein/sage-3.3.rc0/local/lib/python2.5/lib-dynload/grp.so\", O_RDONLY) = 9\n23475 read(9, \"\\177ELF\\2\\1\\1\\0\\0\\0\\0\\0\\0\\0\\0\\0\\3\\0>\\0\\1\\0\\0\\0\\200\\f\\0\\0\\0\\0\\0\\0@\"..., 832) = 832\n23475 fstat(9, {st_mode=S_IFREG|0755, st_size=24578, ...}) = 0\n23475 mmap(NULL, 2104704, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 9, 0) = 0x22e2000\n23475 mprotect(0x22e4000, 2093056, PROT_NONE) = 0\n23475 mmap(0x24e3000, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 9, 0x1000) = 0x24e3000\n```\n\n\nThe return value of the first mmap() shows that it has allocated its memory at 0x22e2000, squarely in the range that brk() is trying to allocate.  So brk() is correct to fail here.\n\nThe question is why mmap() is picking addresses in the range just above the current brk(), and -- more to the point -- whether there is something we can do to change its policy.",
    "created_at": "2009-02-16T07:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40424",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Well, I tracked down one instance of this.  omalloc says there is no memory left when sbrk() (which is a wrapper for brk()) fails, like this:

```
23475 brk(0x22e6030)                    = 0x22e0000
23475 brk(0x22e6030)                    = 0x22e0000
```

Here, brk() is trying (and failing) to allocate the memory between 0x22e0000 and 0x22e6030.

The reason is that the memory is already allocated, to hold a shared library.  Earlier in the same trace, we see:

```
23475 open("/scratch/wstein/sage-3.3.rc0/local/lib/python2.5/lib-dynload/grp.so", O_RDONLY) = 9
23475 read(9, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\200\f\0\0\0\0\0\0@"..., 832) = 832
23475 fstat(9, {st_mode=S_IFREG|0755, st_size=24578, ...}) = 0
23475 mmap(NULL, 2104704, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 9, 0) = 0x22e2000
23475 mprotect(0x22e4000, 2093056, PROT_NONE) = 0
23475 mmap(0x24e3000, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 9, 0x1000) = 0x24e3000
```


The return value of the first mmap() shows that it has allocated its memory at 0x22e2000, squarely in the range that brk() is trying to allocate.  So brk() is correct to fail here.

The question is why mmap() is picking addresses in the range just above the current brk(), and -- more to the point -- whether there is something we can do to change its policy.



---

archive/issue_comments_040425.json:
```json
{
    "body": "There is even this evil doing:\n\n```\n#define malloc  mALLOc\n```\n\nAnyway, I have an idea I'd like to test, but using the time shift, you in America might be faster. It's replacing the lines 1371-1374 of the file \"omMalloc.c\" (that seems to be the one of three almost identical files that is actually compiled):\n\n```\n    /* Try to extend */\n    malloc_extend_top(nb);\n    if ( (remainder_size = chunksize(top) - nb) < (long)MINSIZE)\n      return 0; /* propagate failure */\n```\n\nwith the following lines of code:\n\n```\n    /* Try to extend */\n    malloc_extend_top(nb);\n    if ( (remainder_size = chunksize(top) - nb) < (long)MINSIZE)\n    {\n#if HAVE_MMAP\n      /* On failure try to use mmap (again, or if small: for the first time!) */\n      if ((victim = mmap_chunk(nb)) != 0)\n      {\n        return chunk2mem(victim);\n      }\n#endif\n      return 0; /* propagate failure */\n    }\n```\n\nUnfortunately, I didn't find it easy to provide a \"real\" patch via hg/diff.",
    "created_at": "2009-02-17T22:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40425",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

There is even this evil doing:

```
#define malloc  mALLOc
```

Anyway, I have an idea I'd like to test, but using the time shift, you in America might be faster. It's replacing the lines 1371-1374 of the file "omMalloc.c" (that seems to be the one of three almost identical files that is actually compiled):

```
    /* Try to extend */
    malloc_extend_top(nb);
    if ( (remainder_size = chunksize(top) - nb) < (long)MINSIZE)
      return 0; /* propagate failure */
```

with the following lines of code:

```
    /* Try to extend */
    malloc_extend_top(nb);
    if ( (remainder_size = chunksize(top) - nb) < (long)MINSIZE)
    {
#if HAVE_MMAP
      /* On failure try to use mmap (again, or if small: for the first time!) */
      if ((victim = mmap_chunk(nb)) != 0)
      {
        return chunk2mem(victim);
      }
#endif
      return 0; /* propagate failure */
    }
```

Unfortunately, I didn't find it easy to provide a "real" patch via hg/diff.



---

archive/issue_comments_040426.json:
```json
{
    "body": "Well, one has to patch that other file \"dlmalloc.c\", because in the make run, it is copied over \"omMalloc.c\".",
    "created_at": "2009-02-19T21:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40426",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Well, one has to patch that other file "dlmalloc.c", because in the make run, it is copied over "omMalloc.c".



---

archive/issue_comments_040427.json:
```json
{
    "body": "A first quick test did show no difference in behaviour (for the #4181 problem on my MacIntel 32bit). But I am unsure whether I did build the new patched code correctly, resp. whether it was really executed in the end.\n\nThat means I have to instrument the code changes (e.g. printf) and look deeper into where in a library that goes etc.",
    "created_at": "2009-02-20T07:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40427",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

A first quick test did show no difference in behaviour (for the #4181 problem on my MacIntel 32bit). But I am unsure whether I did build the new patched code correctly, resp. whether it was really executed in the end.

That means I have to instrument the code changes (e.g. printf) and look deeper into where in a library that goes etc.



---

archive/issue_comments_040428.json:
```json
{
    "body": "For the record:\n\nIt is plausibe that the underlying problem is the same one as the one underlying ticket #3760: namely that the dlmalloc v2.6.5 from 1998 that Singular/omalloc rely on is simply too old and does not work well on certain modern systems.\n\nI have seen both in the code as well as in historical comments from newer dlmalloc versions that dlmalloc v2.6.5, if sbrk() does not give it more memory, would *not* try to use mmap() as a backup. Only from v2.7.0 on, dlmalloc does this.\n\nThis would make up a perfect explanation for the problem described here!",
    "created_at": "2009-02-23T08:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40428",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

For the record:

It is plausibe that the underlying problem is the same one as the one underlying ticket #3760: namely that the dlmalloc v2.6.5 from 1998 that Singular/omalloc rely on is simply too old and does not work well on certain modern systems.

I have seen both in the code as well as in historical comments from newer dlmalloc versions that dlmalloc v2.6.5, if sbrk() does not give it more memory, would *not* try to use mmap() as a backup. Only from v2.7.0 on, dlmalloc does this.

This would make up a perfect explanation for the problem described here!



---

archive/issue_comments_040429.json:
```json
{
    "body": "This is fixed by #4181 and in addition the application of the patch at \n\n http://bugs.python.org/file10517/fix-unicode-listdir.patch\n\nto the pyhton.spkg. I will post an updated python.spkg. With these two updates I get:\n\n```\nAll tests passed!\nTotal time for all tests: 3130.8 seconds\n```\n\non the FC 10 box where it all blew up:\n\n```\nwstein@fedora64:/scratch/wstein/sage-3.3.rc0$ uname -a\nLinux fedora64 2.6.27.12-170.2.5.fc10.x86_64 #1 SMP Wed Jan 21 01:33:24 EST 2009 x86_64 x86_64 x86_64 GNU/Linux\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-23T22:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40429",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is fixed by #4181 and in addition the application of the patch at 

 http://bugs.python.org/file10517/fix-unicode-listdir.patch

to the pyhton.spkg. I will post an updated python.spkg. With these two updates I get:

```
All tests passed!
Total time for all tests: 3130.8 seconds
```

on the FC 10 box where it all blew up:

```
wstein@fedora64:/scratch/wstein/sage-3.3.rc0$ uname -a
Linux fedora64 2.6.27.12-170.2.5.fc10.x86_64 #1 SMP Wed Jan 21 01:33:24 EST 2009 x86_64 x86_64 x86_64 GNU/Linux
```


Cheers,

Michael



---

archive/issue_comments_040430.json:
```json
{
    "body": "An updated python.spkg is now at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.4/alpha0/python-2.5.2.p9.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T22:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40430",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

An updated python.spkg is now at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4/alpha0/python-2.5.2.p9.spkg

Cheers,

Michael



---

archive/issue_comments_040431.json:
```json
{
    "body": "Looks good.  Great work on this fix!",
    "created_at": "2009-02-24T22:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40431",
    "user": "https://github.com/mwhansen"
}
```

Looks good.  Great work on this fix!



---

archive/issue_comments_040432.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2009-02-24T22:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40432",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_040433.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-24T22:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40433",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040434.json:
```json
{
    "body": "I change the subject of the ticket since this is a followup issue after the libSingular problem was fixed by Georg via another ticket. Credit has been distributed via #3760, #5344 and #4181. Please check in the 3.4.alpha0 release notes that I got it all right :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T22:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40434",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I change the subject of the ticket since this is a followup issue after the libSingular problem was fixed by Georg via another ticket. Credit has been distributed via #3760, #5344 and #4181. Please check in the 3.4.alpha0 release notes that I got it all right :)

Cheers,

Michael



---

archive/issue_comments_040435.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T22:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40435",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael



---

archive/issue_events_012257.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-24T22:16:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5278#event-12257"
}
```



---

archive/issue_comments_040436.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T22:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5278#issuecomment-40436",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
