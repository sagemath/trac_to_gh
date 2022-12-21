# Issue 9269: clean up #optional tags in sage/graphs

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2010-06-18 22:49:34

Assignee: mvngu

See

http://groups.google.com/group/sage-devel/browse_thread/thread/71d958feced948af


---

Attachment


---

Comment by rlm created at 2010-06-18 22:51:37

Changing status from new to needs_review.


---

Attachment

Why has CPLEX been removed from some tags and not others?


---

Comment by ncohen created at 2010-06-20 18:19:50

Cplex has been left where it was explicitely required : for the method solve_cplex for example, which is only compiled when CBC has been compiled with Cplex itself.

Its other occurences are of a different kind : I named it as it was one of the three solver available, though there is no way to install Cplex in Sage without installing Cbc before :-)

Thank you Robert !!!

Nathann


---

Comment by ncohen created at 2010-06-20 18:19:50

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-06-20 20:34:08

Two comments: first, this won't work with `-only-optional` without the patch from #9272: any line marked `# optional - TAGS` in which TAGS contains capital letters can't be tested with `-only-optional` because of a bug in sage-doctest.  So was this actually tested?  I'm suspicious...

Second, lines marked `# optional - GLPK, CBC` require `-only-optional=GLPK,CBC` to run: using `-only-optional=GLPK` won't run them.  That is, if you include several tags on an "optional" line, they are combined using "and", not "or".  I don't think that is what's intended here.  Should we leave it as is, or change it somehow?  Or at least document it somewhere in the file?


---

Comment by rlm created at 2010-06-20 22:31:38

Replying to [comment:4 jhpalmieri]:
> Two comments: first, this won't work with `-only-optional` without the patch from #9272: any line marked `# optional - TAGS` in which TAGS contains capital letters can't be tested with `-only-optional` because of a bug in sage-doctest.  So was this actually tested?  I'm suspicious...

I did test this, and I found something slightly different from what you claim: the script takes the tags in the doctest and converts them to lower case, while not doing the same for the command line arguments. So the combination `# optional - BLAH` plus `-only-optional=blah` works, while neither `# optional - BLAH` plus `-only-optional=BLAH` nor `# optional - blah` plus `-only-optional=BLAH` works.

> Second, lines marked `# optional - GLPK, CBC` require `-only-optional=GLPK,CBC` to run: using `-only-optional=GLPK` won't run them.  That is, if you include several tags on an "optional" line, they are combined using "and", not "or".  I don't think that is what's intended here.  Should we leave it as is, or change it somehow?  Or at least document it somewhere in the file?

In my recent sage-devel post, I mentioned that there is no support for `OR` in this scheme. My solution was to have doctests requiring GLPK or CBC to have both listed, and to use `-only-optional=glpk,cbc` when either is installed.

I meant to remove CPLEX from *all* the tests, since there is no cplex package.


---

Comment by jhpalmieri created at 2010-06-20 22:46:17

Replying to [comment:5 rlm]:

> I did test this, 

(Yes, but you weren't the reviewer.)

> and I found something slightly different from what you claim: the script takes the tags in the doctest and converts them to lower case, while not doing the same for the command line arguments. So the combination `# optional - BLAH` plus `-only-optional=blah` works, while neither `# optional - BLAH` plus `-only-optional=BLAH` nor `# optional - blah` plus `-only-optional=BLAH` works.

You're right, I mixed this up here (but I think I got it right on #9272).
 
> In my recent sage-devel post, I mentioned that there is no support for `OR` in this scheme. My solution was to have doctests requiring GLPK or CBC to have both listed, and to use `-only-optional=glpk,cbc` when either is installed.

Right, my question is whether we should put a comment about this at the top of the affected files, or do we just trust people to know how to use "-only-optional"?
 
> I meant to remove CPLEX from *all* the tests, since there is no cplex package.

I think this flag probably still belongs in `mip_cplex.pyx`, if no place else.  Someone might have CPLEX installed separately from Sage, and having a mechanism to test is not a bad idea.  ("optional" tags don't need to correspond to packages, like `# optional - internet` or `# optional - Mathematica`.)


---

Comment by ncohen created at 2010-06-21 05:54:10

Hmmm.... It looks like I was much less attentive to this patch than you were O_o

Actually, I just trusted the problem was that an #optional comment must only contain this very keyword, followed by the names of the packages, and that this motivated the whole patch.

Just in case you wonder, when I write patches using LP, I usually use -optional without any argument, so that all optional packages are tested. Besides, I do not like to see all the optional flags pass successfully the first time (exactly because I do nt know if all of them were tested), so when it happens I usually change the result of a command to see whether Sage "sees" it :-)

Do yo think this patch needs to be modified, John ?

Nathann


---

Comment by jhpalmieri created at 2010-06-21 15:39:11

> Do yo think this patch needs to be modified, John ?

I'm guessing that you have either GLPK or CBC installed, or both.  Could you just test that "sage -t -only-optional=glpk,cbc ..." works on the affected files?  In more detail:

 - "sage -t -only-optional=glpk ..."  should finish instantly, because it shouldn't run any tests.

 - "sage -t -only-optional=glpk,cbc  ..."  should *not* finish instantly, and all tests should pass.

I've checked this without GLPK and CBC installed, and the second of these fails a bunch of tests, as it should.


---

Comment by ncohen created at 2010-06-21 15:44:46

Hello !!!

It is exactly as you said ! Well, except for several errors in generic_graph.py, but this is just because of the recent NetworkX update and is already fixed in #9230.

Nathann


---

Comment by jhpalmieri created at 2010-06-21 17:17:02

Okay, that's good enough for me.  Thanks for checking that.


---

Comment by rlm created at 2010-06-29 16:45:29

Resolution: fixed
