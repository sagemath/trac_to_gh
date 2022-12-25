# Issue 4793: Update lcalc to the new upstream 1.2

archive/issues_004793.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @JohnCremona ylchapuy drkirkby\n\nAs the summary says. This should be done at the same time as the update to the latest stable pari.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4793\n\n",
    "created_at": "2008-12-14T07:45:09Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "Update lcalc to the new upstream 1.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4793",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @JohnCremona ylchapuy drkirkby

As the summary says. This should be done at the same time as the update to the latest stable pari.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4793





---

archive/issue_comments_036255.json:
```json
{
    "body": "See ticket #5396 for upgrading lcalc to version 1.23",
    "created_at": "2009-10-01T06:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36255",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See ticket #5396 for upgrading lcalc to version 1.23



---

archive/issue_comments_036256.json:
```json
{
    "body": "I am attaching a spkg for lcalc.\n\nhttp://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-1.23.spkg\n\nThis spkg is result of last last few discussion in #5396",
    "created_at": "2010-03-17T19:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36256",
    "user": "https://github.com/rishikesha"
}
```

I am attaching a spkg for lcalc.

http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-1.23.spkg

This spkg is result of last last few discussion in #5396



---

archive/issue_comments_036257.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-17T19:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36257",
    "user": "https://github.com/rishikesha"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036258.json:
```json
{
    "body": "I split the spkg  from lcalc wrapper. The discussion on spkg was becoming longer and digressing from the wrapper itself.",
    "created_at": "2010-03-17T19:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36258",
    "user": "https://github.com/rishikesha"
}
```

I split the spkg  from lcalc wrapper. The discussion on spkg was becoming longer and digressing from the wrapper itself.



---

archive/issue_comments_036259.json:
```json
{
    "body": "Changing assignee from mabshoff to @rishikesha.",
    "created_at": "2010-03-17T19:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36259",
    "user": "https://github.com/rishikesha"
}
```

Changing assignee from mabshoff to @rishikesha.



---

archive/issue_comments_036260.json:
```json
{
    "body": "All the headers should be copied to a subdir of local/include (given they might clash with others).",
    "created_at": "2010-03-24T18:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36260",
    "user": "https://github.com/robertwb"
}
```

All the headers should be copied to a subdir of local/include (given they might clash with others).



---

archive/issue_comments_036261.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-24T18:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36261",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_036262.json:
```json
{
    "body": "Also has issues on OS X \n\n\n```\ndyld: lazy symbol binding failed: Symbol not found: ___gmpn_lshift\n  Referenced from: /Users/robertwb/sage/sage-4.0/local/lib//libpari-gmp.dylib\n  Expected in: flat namespace\n```\n\n\nwhen running tests in sage/lfunctions/lcalc.py",
    "created_at": "2010-03-24T18:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36262",
    "user": "https://github.com/robertwb"
}
```

Also has issues on OS X 


```
dyld: lazy symbol binding failed: Symbol not found: ___gmpn_lshift
  Referenced from: /Users/robertwb/sage/sage-4.0/local/lib//libpari-gmp.dylib
  Expected in: flat namespace
```


when running tests in sage/lfunctions/lcalc.py



---

archive/issue_comments_036263.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-25T04:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36263",
    "user": "https://github.com/rishikesha"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_036264.json:
```json
{
    "body": "This spkg has been tested on OSX, linux and Solaris. The header files are now installed in $SAGE_LOCAL/include/lcalc\n\nhttp://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-1.23.spkg",
    "created_at": "2010-03-25T04:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36264",
    "user": "https://github.com/rishikesha"
}
```

This spkg has been tested on OSX, linux and Solaris. The header files are now installed in $SAGE_LOCAL/include/lcalc

http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-1.23.spkg



---

archive/issue_comments_036265.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-26T00:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36265",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_036266.json:
```json
{
    "body": "Hi,\nthere are a few problems with spkg-install, which don't reflect how Sage is currently being built. \n\n* You said on #5396 \"One more thing- I've also cleaned up my makefile a bit, and, in the source, got rid of depreciated headers and unused variables.\" Did you notice that your Makefile is being overwritten, by the following line:\n  {{{\n  cp ../../patches/Makefile.sage Makefile\n  }}}\n  Are those changes appropriate? But looking at your own Makefile, I see still see options to  suppress warnings messages. \n   * -Wa,-W is designed to suppress warnings from the assembler, which fails if the Sun assembler is used. (That's why I had to re-write part of your makefile before). \n   * -Wno-deprecate is designed to suppress warnings about depreciated headers. \n\nA few more things. \n\n* Don't bother checking for SAGE_FORTRAN_LIB, as it is tested in the 'prereq' script. \n* Don't bother checking for SAGE_FORTRAN, as again prereq takes care of that. \n* Don't bother checking if the GNU and Sun compilers are mixed - that is taken care of elsewhere. \n* The line:\n  {{{\n  echo \"Building a 32-bit version of lcalc\"\n  }}}\n\n  is incorrect, as some systems build 64-bit by default, and so the lack of a -m64 flag does not imply a 32-bit build. \n* The line:\n  {{{\n  if [ \"x$SAGE64\" = \"xyes\" ] || [ \"x$SAGE64\" = \"x1\" ]  ; then\n  }}}\ncan be simplified to \n  {{{\n  if [ \"x$SAGE64\" = xyes ] ; then\n  }}}\n\nas SAGE64 can only be unset, set to 'yes' or set to 'no' - any other combination is not permitted. \n \nAre there any self-tests of this package? If so, it should have a spkg-check too, but of course, if there are no self-tests, then that is inappropriate. \n\nDave",
    "created_at": "2010-03-26T00:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36266",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Hi,
there are a few problems with spkg-install, which don't reflect how Sage is currently being built. 

* You said on #5396 "One more thing- I've also cleaned up my makefile a bit, and, in the source, got rid of depreciated headers and unused variables." Did you notice that your Makefile is being overwritten, by the following line:
  {{{
  cp ../../patches/Makefile.sage Makefile
  }}}
  Are those changes appropriate? But looking at your own Makefile, I see still see options to  suppress warnings messages. 
   * -Wa,-W is designed to suppress warnings from the assembler, which fails if the Sun assembler is used. (That's why I had to re-write part of your makefile before). 
   * -Wno-deprecate is designed to suppress warnings about depreciated headers. 

A few more things. 

* Don't bother checking for SAGE_FORTRAN_LIB, as it is tested in the 'prereq' script. 
* Don't bother checking for SAGE_FORTRAN, as again prereq takes care of that. 
* Don't bother checking if the GNU and Sun compilers are mixed - that is taken care of elsewhere. 
* The line:
  {{{
  echo "Building a 32-bit version of lcalc"
  }}}

  is incorrect, as some systems build 64-bit by default, and so the lack of a -m64 flag does not imply a 32-bit build. 
* The line:
  {{{
  if [ "x$SAGE64" = "xyes" ] || [ "x$SAGE64" = "x1" ]  ; then
  }}}
can be simplified to 
  {{{
  if [ "x$SAGE64" = xyes ] ; then
  }}}

as SAGE64 can only be unset, set to 'yes' or set to 'no' - any other combination is not permitted. 
 
Are there any self-tests of this package? If so, it should have a spkg-check too, but of course, if there are no self-tests, then that is inappropriate. 

Dave



---

archive/issue_comments_036267.json:
```json
{
    "body": "Replying to [comment:12 drkirkby]:\n> Hi,\n> there are a few problems with spkg-install, which don't reflect how Sage is currently being built. \n> \n>  * You said on #5396 \"One more thing- I've also cleaned up my makefile a bit, and, in the source, got rid of depreciated headers and unused variables.\" Did you notice that your Makefile is being overwritten, by the following line:\n>   {{{\n>   cp ../../patches/Makefile.sage Makefile\n>   }}}\n>   Are those changes appropriate? But looking at your own Makefile, I see still see options to  suppress warnings messages. \n>     * -Wa,-W is designed to suppress warnings from the assembler, which fails if the Sun assembler is used. (That's why I had to re-write part of your makefile before). \n>     * -Wno-deprecate is designed to suppress warnings about depreciated headers. \n\n\nPlease see what the package does. I have not made any changes to original Makefile, only to Makefile.sage\n\n> \n> A few more things. \n> \n\nI took the old spkg-install and added what I needed. I did not change what ever happened else where, so the person who changed those should have changed this prereq in lcalc spkg. This includes everything below. I am changing status to needs review.\n\n>  * Don't bother checking for SAGE_FORTRAN_LIB, as it is tested in the 'prereq' script. \n>  * Don't bother checking for SAGE_FORTRAN, as again prereq takes care of that. \n>  * Don't bother checking if the GNU and Sun compilers are mixed - that is taken care of elsewhere. \n>  * The line:\n>   {{{\n>    echo \"Building a 32-bit version of lcalc\"\n>   }}}\n> \n>    is incorrect, as some systems build 64-bit by default, and so the lack of a -m64 flag does not imply a 32-bit build. \n>  * The line:\n>   {{{\n>   if [ \"x$SAGE64\" = \"xyes\" ] || [ \"x$SAGE64\" = \"x1\" ]  ; then\n>   }}}\n> can be simplified to \n>   {{{\n>   if [ \"x$SAGE64\" = xyes ] ; then\n>   }}}\n> \n> as SAGE64 can only be unset, set to 'yes' or set to 'no' - any other combination is not permitted. \n>  \n> Are there any self-tests of this package? If so, it should have a spkg-check too, but of course, if there are no self-tests, then that is inappropriate. \n> \n> Dave \n> \n>",
    "created_at": "2010-03-26T15:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36267",
    "user": "https://github.com/rishikesha"
}
```

Replying to [comment:12 drkirkby]:
> Hi,
> there are a few problems with spkg-install, which don't reflect how Sage is currently being built. 
> 
>  * You said on #5396 "One more thing- I've also cleaned up my makefile a bit, and, in the source, got rid of depreciated headers and unused variables." Did you notice that your Makefile is being overwritten, by the following line:
>   {{{
>   cp ../../patches/Makefile.sage Makefile
>   }}}
>   Are those changes appropriate? But looking at your own Makefile, I see still see options to  suppress warnings messages. 
>     * -Wa,-W is designed to suppress warnings from the assembler, which fails if the Sun assembler is used. (That's why I had to re-write part of your makefile before). 
>     * -Wno-deprecate is designed to suppress warnings about depreciated headers. 


Please see what the package does. I have not made any changes to original Makefile, only to Makefile.sage

> 
> A few more things. 
> 

I took the old spkg-install and added what I needed. I did not change what ever happened else where, so the person who changed those should have changed this prereq in lcalc spkg. This includes everything below. I am changing status to needs review.

>  * Don't bother checking for SAGE_FORTRAN_LIB, as it is tested in the 'prereq' script. 
>  * Don't bother checking for SAGE_FORTRAN, as again prereq takes care of that. 
>  * Don't bother checking if the GNU and Sun compilers are mixed - that is taken care of elsewhere. 
>  * The line:
>   {{{
>    echo "Building a 32-bit version of lcalc"
>   }}}
> 
>    is incorrect, as some systems build 64-bit by default, and so the lack of a -m64 flag does not imply a 32-bit build. 
>  * The line:
>   {{{
>   if [ "x$SAGE64" = "xyes" ] || [ "x$SAGE64" = "x1" ]  ; then
>   }}}
> can be simplified to 
>   {{{
>   if [ "x$SAGE64" = xyes ] ; then
>   }}}
> 
> as SAGE64 can only be unset, set to 'yes' or set to 'no' - any other combination is not permitted. 
>  
> Are there any self-tests of this package? If so, it should have a spkg-check too, but of course, if there are no self-tests, then that is inappropriate. 
> 
> Dave 
> 
>



---

archive/issue_comments_036268.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-26T15:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36268",
    "user": "https://github.com/rishikesha"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_036269.json:
```json
{
    "body": "Hi David,\n\nThe command \"hg annotate\" is helpful in clarifying the above issues.   Let me give you a tutorial about how that command works. Doing \n\n```\nhg annotate spkg-install |grep FORTRAN\n```\n\nyields that changeset 22 added all the FORTRAN stuff you're complaining about:\n\n```\nchangeset:   22:c7e7606b574d\nuser:        David Kirkby <david.kirkby@onetel.net>\ndate:        Tue Sep 15 07:41:31 2009 -0700\nsummary:     trac #6609: don't pass GNU flags directly to the Sun assembler\n```\n\n\nYou also state you added this in the SPKG.txt:\n\n```\n### lcalc-20080205.p3 (David kirkby, 15th September, 2009)\n * A general tidy-up/improvement in many ways, including:\n...\n * Check that the C, C++ and Fortran compilers are not a mix of Sun and GNU\n```\n\n\nYour comment about\n\n```\n    * The line:\n\n         echo \"Building a 32-bit version of lcalc\"\n\n        is incorrect, as some systems build 64-bit by default, and so the lack of a -m64 flag does not imply a 32-bit build.\n\n```\n\nis also a complaint about code that you added in patch 22.\n\nSo you are currently complaining about and rejecting Rishi's spkg based entirely on problems that you introduced in the spkg. \n\nThus I don't think all (any?) of your complaints are valid. \n\nI'll work with Rishi and Mike Hansen today to get this spkg in.  Since you clearly don't like many of the changes you introduced in changeset 22, I encourage you to create a new trac ticket to remove those changes from say the next version of lcalc.  Then Rishi (who should be the official package maintainer -- Rishi: you may add yourself as such in SPKG.txt) can make those changes.\n\n -- William",
    "created_at": "2010-03-26T16:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36269",
    "user": "https://github.com/williamstein"
}
```

Hi David,

The command "hg annotate" is helpful in clarifying the above issues.   Let me give you a tutorial about how that command works. Doing 

```
hg annotate spkg-install |grep FORTRAN
```

yields that changeset 22 added all the FORTRAN stuff you're complaining about:

```
changeset:   22:c7e7606b574d
user:        David Kirkby <david.kirkby@onetel.net>
date:        Tue Sep 15 07:41:31 2009 -0700
summary:     trac #6609: don't pass GNU flags directly to the Sun assembler
```


You also state you added this in the SPKG.txt:

```
### lcalc-20080205.p3 (David kirkby, 15th September, 2009)
 * A general tidy-up/improvement in many ways, including:
...
 * Check that the C, C++ and Fortran compilers are not a mix of Sun and GNU
```


Your comment about

```
    * The line:

         echo "Building a 32-bit version of lcalc"

        is incorrect, as some systems build 64-bit by default, and so the lack of a -m64 flag does not imply a 32-bit build.

```

is also a complaint about code that you added in patch 22.

So you are currently complaining about and rejecting Rishi's spkg based entirely on problems that you introduced in the spkg. 

Thus I don't think all (any?) of your complaints are valid. 

I'll work with Rishi and Mike Hansen today to get this spkg in.  Since you clearly don't like many of the changes you introduced in changeset 22, I encourage you to create a new trac ticket to remove those changes from say the next version of lcalc.  Then Rishi (who should be the official package maintainer -- Rishi: you may add yourself as such in SPKG.txt) can make those changes.

 -- William



---

archive/issue_comments_036270.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-26T18:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36270",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_036271.json:
```json
{
    "body": "I merged this in as lcalc-20100428-1.23.spkg , since using lcalc-1.23.spkg would break the version number ordering and upgrade system.",
    "created_at": "2010-04-28T19:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36271",
    "user": "https://github.com/williamstein"
}
```

I merged this in as lcalc-20100428-1.23.spkg , since using lcalc-1.23.spkg would break the version number ordering and upgrade system.



---

archive/issue_events_005036.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-04-28T19:29:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4793#event-5036"
}
```



---

archive/issue_comments_036272.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-28T19:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4793#issuecomment-36272",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
