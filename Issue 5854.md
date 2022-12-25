# Issue 5854: [with patch, with spkg, needs review] Include Michael Stoll's ratpoints in Sage

archive/issues_005854.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @JohnCremona\n\nThe spkg is located here:\n\nhttp://sage.math.washington.edu/home/rlmill/ratpoints-2.1.1.spkg\n\n(The final version for review was created 22 April 2009-- there were previous versions by the same file name, but this one can be identified as the one possessing an SPKG.txt file.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5854\n\n",
    "created_at": "2009-04-22T15:17:52Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, with spkg, needs review] Include Michael Stoll's ratpoints in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5854",
    "user": "https://github.com/rlmill"
}
```
Assignee: @williamstein

CC:  @JohnCremona

The spkg is located here:

http://sage.math.washington.edu/home/rlmill/ratpoints-2.1.1.spkg

(The final version for review was created 22 April 2009-- there were previous versions by the same file name, but this one can be identified as the one possessing an SPKG.txt file.)

Issue created by migration from https://trac.sagemath.org/ticket/5854





---

archive/issue_comments_046145.json:
```json
{
    "body": "Attachment [trac_5854-ratpoints.patch](tarball://root/attachments/some-uuid/ticket5854/trac_5854-ratpoints.patch) by @rlmill created at 2009-04-22 15:18:16",
    "created_at": "2009-04-22T15:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46145",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5854-ratpoints.patch](tarball://root/attachments/some-uuid/ticket5854/trac_5854-ratpoints.patch) by @rlmill created at 2009-04-22 15:18:16



---

archive/issue_comments_046146.json:
```json
{
    "body": "This spkg needs a formal vote and some more widespread testing. I am also curious about the MSVC build, but we can try that in person.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T18:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46146",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This spkg needs a formal vote and some more widespread testing. I am also curious about the MSVC build, but we can try that in person.

Cheers,

Michael



---

archive/issue_comments_046147.json:
```json
{
    "body": "Another thing: Why is the dependency on the header commented out?:\n\n```\n \t386\t    Extension('sage.libs.ratpoints', \n \t387\t              sources = [\"sage/libs/ratpoints.pyx\"], \n \t388\t              #depends = [SAGE_ROOT + 'local/include/ratpoints.h'], \n \t389\t              libraries = [\"ratpoints\", \"gmp\"]),\n```\nAnd another question: What is the long term plan here with eclib? Will it use ratpoints in the future?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T18:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46147",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Another thing: Why is the dependency on the header commented out?:

```
 	386	    Extension('sage.libs.ratpoints', 
 	387	              sources = ["sage/libs/ratpoints.pyx"], 
 	388	              #depends = [SAGE_ROOT + 'local/include/ratpoints.h'], 
 	389	              libraries = ["ratpoints", "gmp"]),
```
And another question: What is the long term plan here with eclib? Will it use ratpoints in the future?

Cheers,

Michael



---

archive/issue_comments_046148.json:
```json
{
    "body": "And while I am at it:\n\n* SPKG.txt is missing the license section. Since the code is GPL V2+ again now it would be nice to mention\n* src is under version control - any reason to do that in the spkg since this should be clean upstream? Given the size I don't mind too much, but it is unusual.  \n* there is one PDF in src that isn't in the repo - in case we want src under hg you should put that PDF in .hgignore.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T19:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46148",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And while I am at it:

* SPKG.txt is missing the license section. Since the code is GPL V2+ again now it would be nice to mention
* src is under version control - any reason to do that in the spkg since this should be clean upstream? Given the size I don't mind too much, but it is unusual.  
* there is one PDF in src that isn't in the repo - in case we want src under hg you should put that PDF in .hgignore.

Cheers,

Michael



---

archive/issue_comments_046149.json:
```json
{
    "body": "* SPKG.txt was based directly on the one for eclib, so anything wrong with this one will be wrong with that one too.\n  * `src` was under version control originally because I found a bug and fixed it, but Michael Stoll has merged that fix upstream. I suppose there's no reason now.\n  * The depends line is commented out to demonstrate that it is automatically picked up somewhere, and thus not needed...",
    "created_at": "2009-04-22T20:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46149",
    "user": "https://github.com/rlmill"
}
```

* SPKG.txt was based directly on the one for eclib, so anything wrong with this one will be wrong with that one too.
  * `src` was under version control originally because I found a bug and fixed it, but Michael Stoll has merged that fix upstream. I suppose there's no reason now.
  * The depends line is commented out to demonstrate that it is automatically picked up somewhere, and thus not needed...



---

archive/issue_comments_046150.json:
```json
{
    "body": "Replying to [comment:4 rlm]:\n>  * SPKG.txt was based directly on the one for eclib, so anything wrong with this one will be wrong with that one too.\n\n\nYes, that needs to be fixed, too.\n\n>  * `src` was under version control originally because I found a bug and fixed it, but Michael Stoll has merged that fix upstream. I suppose there's no reason now.\n\n\nGood. Can you post an SPKG that has a clean .hg and .hgignore, i.e. just get rid of the old .hg and check the relevant bits back in again.\n\n>  * The depends line is commented out to demonstrate that it is automatically picked up somewhere, and thus not needed...\n\n\nHmmm, does rebuilding the spkg lead to \"sage -b\" rebuilding the extension? That does surprise me and I would be curious what this triggers.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T21:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46150",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 rlm]:
>  * SPKG.txt was based directly on the one for eclib, so anything wrong with this one will be wrong with that one too.


Yes, that needs to be fixed, too.

>  * `src` was under version control originally because I found a bug and fixed it, but Michael Stoll has merged that fix upstream. I suppose there's no reason now.


Good. Can you post an SPKG that has a clean .hg and .hgignore, i.e. just get rid of the old .hg and check the relevant bits back in again.

>  * The depends line is commented out to demonstrate that it is automatically picked up somewhere, and thus not needed...


Hmmm, does rebuilding the spkg lead to "sage -b" rebuilding the extension? That does surprise me and I would be curious what this triggers.

Cheers,

Michael



---

archive/issue_comments_046151.json:
```json
{
    "body": "Since this ticket is relevant to eclib (I believe in sage-nt John mentioned that he had looked into using ratpoints from eclib again and that the current library interface worked, but my collection is a little hazy here) I am CCing him to keep him uptodate on this development. Once ratpoints is in Sage I consider it desirable to use the library from eclib unless there is some unforeseen technical reason not to do it.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T21:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46151",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since this ticket is relevant to eclib (I believe in sage-nt John mentioned that he had looked into using ratpoints from eclib again and that the current library interface worked, but my collection is a little hazy here) I am CCing him to keep him uptodate on this development. Once ratpoints is in Sage I consider it desirable to use the library from eclib unless there is some unforeseen technical reason not to do it.

Cheers,

Michael



---

archive/issue_comments_046152.json:
```json
{
    "body": "Replying to [comment:6 mabshoff]:\n> Since this ticket is relevant to eclib (I believe in sage-nt John mentioned that he had looked into using ratpoints from eclib again and that the current library interface worked, but my collection is a little hazy here) I am CCing him to keep him uptodate on this development. Once ratpoints is in Sage I consider it desirable to use the library from eclib unless there is some unforeseen technical reason not to do it.\n> \n> Cheers,\n> \n> Michael\n\n\nThanks.  It is not quite as easy as that, and one part of eclib will need to be rewritten to use this library, but it has all the ingredients which I needs so that is possible and would only take a day or too.  That would also mean that *either* I put in a compiler switch to eclib Makefiles to tell it to use ratpoints instead of its own code, *or* I rely on ratpoints for ever, which gives people who download mwrank by itself will have something else they need to install first (as well as NTL and pari).",
    "created_at": "2009-04-23T08:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46152",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:6 mabshoff]:
> Since this ticket is relevant to eclib (I believe in sage-nt John mentioned that he had looked into using ratpoints from eclib again and that the current library interface worked, but my collection is a little hazy here) I am CCing him to keep him uptodate on this development. Once ratpoints is in Sage I consider it desirable to use the library from eclib unless there is some unforeseen technical reason not to do it.
> 
> Cheers,
> 
> Michael


Thanks.  It is not quite as easy as that, and one part of eclib will need to be rewritten to use this library, but it has all the ingredients which I needs so that is possible and would only take a day or too.  That would also mean that *either* I put in a compiler switch to eclib Makefiles to tell it to use ratpoints instead of its own code, *or* I rely on ratpoints for ever, which gives people who download mwrank by itself will have something else they need to install first (as well as NTL and pari).



---

archive/issue_comments_046153.json:
```json
{
    "body": "What is the correct procedure for testing this.  Is it: (1) install the spkg using \"sage -f\" (2) apply the patch to a clone and do \"sage -b\" (3) do a \"sage -t\" on sage/libs/ratpoints.pyx (and try the functions in there at will) ?",
    "created_at": "2009-04-29T11:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46153",
    "user": "https://github.com/JohnCremona"
}
```

What is the correct procedure for testing this.  Is it: (1) install the spkg using "sage -f" (2) apply the patch to a clone and do "sage -b" (3) do a "sage -t" on sage/libs/ratpoints.pyx (and try the functions in there at will) ?



---

archive/issue_comments_046154.json:
```json
{
    "body": "Replying to [comment:8 cremona]:\n\nMostly:\n\n> (and try the functions in there at will) ?\n\n\nSomeone should run a valgrind session to check my code and Michael Stoll's code both for leaks. I'll try to get to this today or tomorrow.",
    "created_at": "2009-04-29T14:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46154",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:8 cremona]:

Mostly:

> (and try the functions in there at will) ?


Someone should run a valgrind session to check my code and Michael Stoll's code both for leaks. I'll try to get to this today or tomorrow.



---

archive/issue_comments_046155.json:
```json
{
    "body": "Partial review:  I ran valgrind on ratpoints's own test function and it does reasonably well:\n\n```\nmasgaj@host-56-150%valgrind ./rptest > rptest.out\n==4873== Memcheck, a memory error detector.\n==4873== Copyright (C) 2002-2007, and GNU GPL'd, by Julian Seward et al.\n==4873== Using LibVEX rev 1804, a library for dynamic binary translation.\n==4873== Copyright (C) 2004-2007, and GNU GPL'd, by OpenWorks LLP.\n==4873== Using valgrind-3.3.0, a dynamic binary instrumentation framework.\n==4873== Copyright (C) 2000-2007, and GNU GPL'd, by Julian Seward et al.\n==4873== For more details, rerun with: -v\n==4873==\n==4873==\n==4873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 5 from 1)\n==4873== malloc/free: in use at exit: 11,204 bytes in 44 blocks.\n==4873== malloc/free: 91,051 allocs, 91,007 frees, 2,895,144 bytes allocated.\n==4873== For counts of detected errors, rerun with: -v\n==4873== searching for pointers to 44 not-freed blocks.\n==4873== checked 128,328 bytes.\n==4873==\n==4873== LEAK SUMMARY:\n==4873==    definitely lost: 11,176 bytes in 37 blocks.\n==4873==      possibly lost: 0 bytes in 0 blocks.\n==4873==    still reachable: 28 bytes in 7 blocks.\n==4873==         suppressed: 0 bytes in 0 blocks.\n==4873== Rerun with --leak-check=full to see details of leaked memory.\n```\n\nPerhaps Michael (A) can say whether the leak is significant?  If so we could ask Michael (S) to fix it.",
    "created_at": "2009-04-29T15:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46155",
    "user": "https://github.com/JohnCremona"
}
```

Partial review:  I ran valgrind on ratpoints's own test function and it does reasonably well:

```
masgaj@host-56-150%valgrind ./rptest > rptest.out
==4873== Memcheck, a memory error detector.
==4873== Copyright (C) 2002-2007, and GNU GPL'd, by Julian Seward et al.
==4873== Using LibVEX rev 1804, a library for dynamic binary translation.
==4873== Copyright (C) 2004-2007, and GNU GPL'd, by OpenWorks LLP.
==4873== Using valgrind-3.3.0, a dynamic binary instrumentation framework.
==4873== Copyright (C) 2000-2007, and GNU GPL'd, by Julian Seward et al.
==4873== For more details, rerun with: -v
==4873==
==4873==
==4873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 5 from 1)
==4873== malloc/free: in use at exit: 11,204 bytes in 44 blocks.
==4873== malloc/free: 91,051 allocs, 91,007 frees, 2,895,144 bytes allocated.
==4873== For counts of detected errors, rerun with: -v
==4873== searching for pointers to 44 not-freed blocks.
==4873== checked 128,328 bytes.
==4873==
==4873== LEAK SUMMARY:
==4873==    definitely lost: 11,176 bytes in 37 blocks.
==4873==      possibly lost: 0 bytes in 0 blocks.
==4873==    still reachable: 28 bytes in 7 blocks.
==4873==         suppressed: 0 bytes in 0 blocks.
==4873== Rerun with --leak-check=full to see details of leaked memory.
```

Perhaps Michael (A) can say whether the leak is significant?  If so we could ask Michael (S) to fix it.



---

archive/issue_comments_046156.json:
```json
{
    "body": "John,\n\nSince you've been using Michael Stoll's test suite, do you think you could make an `spkg-check` for this spkg which runs these?",
    "created_at": "2009-04-29T15:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46156",
    "user": "https://github.com/rlmill"
}
```

John,

Since you've been using Michael Stoll's test suite, do you think you could make an `spkg-check` for this spkg which runs these?



---

archive/issue_comments_046157.json:
```json
{
    "body": "PS - Any leaks in \"definitely lost\" is never good...\n\nCan you attach/link to the full valgrind logs?",
    "created_at": "2009-04-29T16:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46157",
    "user": "https://github.com/rlmill"
}
```

PS - Any leaks in "definitely lost" is never good...

Can you attach/link to the full valgrind logs?



---

archive/issue_comments_046158.json:
```json
{
    "body": "Replying to [comment:12 rlm]:\n> PS - Any leaks in \"definitely lost\" is never good...\n> \n> Can you attach/link to the full valgrind logs?\n\n\nI will if you tell me what flags to put on the valgrind command line....",
    "created_at": "2009-04-29T16:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46158",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:12 rlm]:
> PS - Any leaks in "definitely lost" is never good...
> 
> Can you attach/link to the full valgrind logs?


I will if you tell me what flags to put on the valgrind command line....



---

archive/issue_comments_046159.json:
```json
{
    "body": "Build works on Sage-3.4.2, but not on Sage-4.0.alpha0. Build log is attached.",
    "created_at": "2009-05-21T15:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46159",
    "user": "https://github.com/rlmill"
}
```

Build works on Sage-3.4.2, but not on Sage-4.0.alpha0. Build log is attached.



---

archive/issue_comments_046160.json:
```json
{
    "body": "The build issues seem resolved in Sage-4.0.rc0.",
    "created_at": "2009-05-22T05:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46160",
    "user": "https://github.com/rlmill"
}
```

The build issues seem resolved in Sage-4.0.rc0.



---

archive/issue_comments_046161.json:
```json
{
    "body": "I checked that the spkg installs fine on 4.0.2 and the patch applies and tests pass.\n\nThere were some other issues raised by mabshoff, but as I am not an expert on spkgs I do not know if these are enough to stop the ticket from being merged.  So I am giving it a positive review.",
    "created_at": "2009-06-19T20:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46161",
    "user": "https://github.com/JohnCremona"
}
```

I checked that the spkg installs fine on 4.0.2 and the patch applies and tests pass.

There were some other issues raised by mabshoff, but as I am not an expert on spkgs I do not know if these are enough to stop the ticket from being merged.  So I am giving it a positive review.



---

archive/issue_comments_046162.json:
```json
{
    "body": "Wait, there are still memory leaks in 2.1.1. I will update the spkg to 2.1.2 (which fixes the leaks we found at Dagstuhl) in the next few days, once I get some time to do so.",
    "created_at": "2009-06-19T21:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46162",
    "user": "https://github.com/rlmill"
}
```

Wait, there are still memory leaks in 2.1.1. I will update the spkg to 2.1.2 (which fixes the leaks we found at Dagstuhl) in the next few days, once I get some time to do so.



---

archive/issue_comments_046163.json:
```json
{
    "body": "Latest version is at:\n\nhttp://sage.math.washington.edu/home/rlmill/ratpoints-2.1.2.spkg\n\nIt also addresses the issues raised by mabshoff.\n\nJohn-- Can you sign off on this?",
    "created_at": "2009-06-19T23:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46163",
    "user": "https://github.com/rlmill"
}
```

Latest version is at:

http://sage.math.washington.edu/home/rlmill/ratpoints-2.1.2.spkg

It also addresses the issues raised by mabshoff.

John-- Can you sign off on this?



---

archive/issue_comments_046164.json:
```json
{
    "body": "New spkg built fine for me, and the patch passed tests.",
    "created_at": "2009-06-20T08:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46164",
    "user": "https://github.com/JohnCremona"
}
```

New spkg built fine for me, and the patch passed tests.



---

archive/issue_comments_046165.json:
```json
{
    "body": "I have been using this for real as I try to fix #6381, since this should make it very much faster to find integral points in an interval.  But for that we need to expose the parameter b_high to the sage function ratpoints().  So I am adding to the patch to allow this.",
    "created_at": "2009-06-22T14:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46165",
    "user": "https://github.com/JohnCremona"
}
```

I have been using this for real as I try to fix #6381, since this should make it very much faster to find integral points in an interval.  But for that we need to expose the parameter b_high to the sage function ratpoints().  So I am adding to the patch to allow this.



---

archive/issue_events_013778.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-02T22:00:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5854#event-13778"
}
```



---

archive/issue_comments_046166.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T22:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5854#issuecomment-46166",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
