# Issue 9269: clean up #optional tags in sage/graphs

archive/issues_009269.json:
```json
{
    "body": "Assignee: mvngu\n\nSee\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/71d958feced948af\n\nIssue created by migration from https://trac.sagemath.org/ticket/9269\n\n",
    "created_at": "2010-06-18T22:49:34Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "clean up #optional tags in sage/graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9269",
    "user": "@rlmill"
}
```
Assignee: mvngu

See

http://groups.google.com/group/sage-devel/browse_thread/thread/71d958feced948af

Issue created by migration from https://trac.sagemath.org/ticket/9269





---

archive/issue_comments_087303.json:
```json
{
    "body": "Attachment [trac_9269.patch](tarball://root/attachments/some-uuid/ticket9269/trac_9269.patch) by @rlmill created at 2010-06-18 22:50:21",
    "created_at": "2010-06-18T22:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87303",
    "user": "@rlmill"
}
```

Attachment [trac_9269.patch](tarball://root/attachments/some-uuid/ticket9269/trac_9269.patch) by @rlmill created at 2010-06-18 22:50:21



---

archive/issue_comments_087304.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-18T22:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87304",
    "user": "@rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087305.json:
```json
{
    "body": "Attachment [trac_9269-part2.patch](tarball://root/attachments/some-uuid/ticket9269/trac_9269-part2.patch) by @jhpalmieri created at 2010-06-19 18:12:19\n\nWhy has CPLEX been removed from some tags and not others?",
    "created_at": "2010-06-19T18:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87305",
    "user": "@jhpalmieri"
}
```

Attachment [trac_9269-part2.patch](tarball://root/attachments/some-uuid/ticket9269/trac_9269-part2.patch) by @jhpalmieri created at 2010-06-19 18:12:19

Why has CPLEX been removed from some tags and not others?



---

archive/issue_comments_087306.json:
```json
{
    "body": "Cplex has been left where it was explicitely required : for the method solve_cplex for example, which is only compiled when CBC has been compiled with Cplex itself.\n\nIts other occurences are of a different kind : I named it as it was one of the three solver available, though there is no way to install Cplex in Sage without installing Cbc before :-)\n\nThank you Robert !!!\n\nNathann",
    "created_at": "2010-06-20T18:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87306",
    "user": "@nathanncohen"
}
```

Cplex has been left where it was explicitely required : for the method solve_cplex for example, which is only compiled when CBC has been compiled with Cplex itself.

Its other occurences are of a different kind : I named it as it was one of the three solver available, though there is no way to install Cplex in Sage without installing Cbc before :-)

Thank you Robert !!!

Nathann



---

archive/issue_comments_087307.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-20T18:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87307",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087308.json:
```json
{
    "body": "Two comments: first, this won't work with `-only-optional` without the patch from #9272: any line marked `# optional - TAGS` in which TAGS contains capital letters can't be tested with `-only-optional` because of a bug in sage-doctest.  So was this actually tested?  I'm suspicious...\n\nSecond, lines marked `# optional - GLPK, CBC` require `-only-optional=GLPK,CBC` to run: using `-only-optional=GLPK` won't run them.  That is, if you include several tags on an \"optional\" line, they are combined using \"and\", not \"or\".  I don't think that is what's intended here.  Should we leave it as is, or change it somehow?  Or at least document it somewhere in the file?",
    "created_at": "2010-06-20T20:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87308",
    "user": "@jhpalmieri"
}
```

Two comments: first, this won't work with `-only-optional` without the patch from #9272: any line marked `# optional - TAGS` in which TAGS contains capital letters can't be tested with `-only-optional` because of a bug in sage-doctest.  So was this actually tested?  I'm suspicious...

Second, lines marked `# optional - GLPK, CBC` require `-only-optional=GLPK,CBC` to run: using `-only-optional=GLPK` won't run them.  That is, if you include several tags on an "optional" line, they are combined using "and", not "or".  I don't think that is what's intended here.  Should we leave it as is, or change it somehow?  Or at least document it somewhere in the file?



---

archive/issue_comments_087309.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> Two comments: first, this won't work with `-only-optional` without the patch from #9272: any line marked `# optional - TAGS` in which TAGS contains capital letters can't be tested with `-only-optional` because of a bug in sage-doctest.  So was this actually tested?  I'm suspicious...\n\nI did test this, and I found something slightly different from what you claim: the script takes the tags in the doctest and converts them to lower case, while not doing the same for the command line arguments. So the combination `# optional - BLAH` plus `-only-optional=blah` works, while neither `# optional - BLAH` plus `-only-optional=BLAH` nor `# optional - blah` plus `-only-optional=BLAH` works.\n\n> Second, lines marked `# optional - GLPK, CBC` require `-only-optional=GLPK,CBC` to run: using `-only-optional=GLPK` won't run them.  That is, if you include several tags on an \"optional\" line, they are combined using \"and\", not \"or\".  I don't think that is what's intended here.  Should we leave it as is, or change it somehow?  Or at least document it somewhere in the file?\n\nIn my recent sage-devel post, I mentioned that there is no support for `OR` in this scheme. My solution was to have doctests requiring GLPK or CBC to have both listed, and to use `-only-optional=glpk,cbc` when either is installed.\n\nI meant to remove CPLEX from *all* the tests, since there is no cplex package.",
    "created_at": "2010-06-20T22:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87309",
    "user": "@rlmill"
}
```

Replying to [comment:4 jhpalmieri]:
> Two comments: first, this won't work with `-only-optional` without the patch from #9272: any line marked `# optional - TAGS` in which TAGS contains capital letters can't be tested with `-only-optional` because of a bug in sage-doctest.  So was this actually tested?  I'm suspicious...

I did test this, and I found something slightly different from what you claim: the script takes the tags in the doctest and converts them to lower case, while not doing the same for the command line arguments. So the combination `# optional - BLAH` plus `-only-optional=blah` works, while neither `# optional - BLAH` plus `-only-optional=BLAH` nor `# optional - blah` plus `-only-optional=BLAH` works.

> Second, lines marked `# optional - GLPK, CBC` require `-only-optional=GLPK,CBC` to run: using `-only-optional=GLPK` won't run them.  That is, if you include several tags on an "optional" line, they are combined using "and", not "or".  I don't think that is what's intended here.  Should we leave it as is, or change it somehow?  Or at least document it somewhere in the file?

In my recent sage-devel post, I mentioned that there is no support for `OR` in this scheme. My solution was to have doctests requiring GLPK or CBC to have both listed, and to use `-only-optional=glpk,cbc` when either is installed.

I meant to remove CPLEX from *all* the tests, since there is no cplex package.



---

archive/issue_comments_087310.json:
```json
{
    "body": "Replying to [comment:5 rlm]:\n\n> I did test this, \n\n(Yes, but you weren't the reviewer.)\n\n> and I found something slightly different from what you claim: the script takes the tags in the doctest and converts them to lower case, while not doing the same for the command line arguments. So the combination `# optional - BLAH` plus `-only-optional=blah` works, while neither `# optional - BLAH` plus `-only-optional=BLAH` nor `# optional - blah` plus `-only-optional=BLAH` works.\n\nYou're right, I mixed this up here (but I think I got it right on #9272).\n \n> In my recent sage-devel post, I mentioned that there is no support for `OR` in this scheme. My solution was to have doctests requiring GLPK or CBC to have both listed, and to use `-only-optional=glpk,cbc` when either is installed.\n\nRight, my question is whether we should put a comment about this at the top of the affected files, or do we just trust people to know how to use \"-only-optional\"?\n \n> I meant to remove CPLEX from *all* the tests, since there is no cplex package.\n\nI think this flag probably still belongs in `mip_cplex.pyx`, if no place else.  Someone might have CPLEX installed separately from Sage, and having a mechanism to test is not a bad idea.  (\"optional\" tags don't need to correspond to packages, like `# optional - internet` or `# optional - Mathematica`.)",
    "created_at": "2010-06-20T22:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87310",
    "user": "@jhpalmieri"
}
```

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

archive/issue_comments_087311.json:
```json
{
    "body": "Hmmm.... It looks like I was much less attentive to this patch than you were O_o\n\nActually, I just trusted the problem was that an #optional comment must only contain this very keyword, followed by the names of the packages, and that this motivated the whole patch.\n\nJust in case you wonder, when I write patches using LP, I usually use -optional without any argument, so that all optional packages are tested. Besides, I do not like to see all the optional flags pass successfully the first time (exactly because I do nt know if all of them were tested), so when it happens I usually change the result of a command to see whether Sage \"sees\" it :-)\n\nDo yo think this patch needs to be modified, John ?\n\nNathann",
    "created_at": "2010-06-21T05:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87311",
    "user": "@nathanncohen"
}
```

Hmmm.... It looks like I was much less attentive to this patch than you were O_o

Actually, I just trusted the problem was that an #optional comment must only contain this very keyword, followed by the names of the packages, and that this motivated the whole patch.

Just in case you wonder, when I write patches using LP, I usually use -optional without any argument, so that all optional packages are tested. Besides, I do not like to see all the optional flags pass successfully the first time (exactly because I do nt know if all of them were tested), so when it happens I usually change the result of a command to see whether Sage "sees" it :-)

Do yo think this patch needs to be modified, John ?

Nathann



---

archive/issue_comments_087312.json:
```json
{
    "body": "> Do yo think this patch needs to be modified, John ?\n\nI'm guessing that you have either GLPK or CBC installed, or both.  Could you just test that \"sage -t -only-optional=glpk,cbc ...\" works on the affected files?  In more detail:\n\n- \"sage -t -only-optional=glpk ...\"  should finish instantly, because it shouldn't run any tests.\n\n- \"sage -t -only-optional=glpk,cbc  ...\"  should *not* finish instantly, and all tests should pass.\n\nI've checked this without GLPK and CBC installed, and the second of these fails a bunch of tests, as it should.",
    "created_at": "2010-06-21T15:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87312",
    "user": "@jhpalmieri"
}
```

> Do yo think this patch needs to be modified, John ?

I'm guessing that you have either GLPK or CBC installed, or both.  Could you just test that "sage -t -only-optional=glpk,cbc ..." works on the affected files?  In more detail:

- "sage -t -only-optional=glpk ..."  should finish instantly, because it shouldn't run any tests.

- "sage -t -only-optional=glpk,cbc  ..."  should *not* finish instantly, and all tests should pass.

I've checked this without GLPK and CBC installed, and the second of these fails a bunch of tests, as it should.



---

archive/issue_comments_087313.json:
```json
{
    "body": "Hello !!!\n\nIt is exactly as you said ! Well, except for several errors in generic_graph.py, but this is just because of the recent NetworkX update and is already fixed in #9230.\n\nNathann",
    "created_at": "2010-06-21T15:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87313",
    "user": "@nathanncohen"
}
```

Hello !!!

It is exactly as you said ! Well, except for several errors in generic_graph.py, but this is just because of the recent NetworkX update and is already fixed in #9230.

Nathann



---

archive/issue_comments_087314.json:
```json
{
    "body": "Okay, that's good enough for me.  Thanks for checking that.",
    "created_at": "2010-06-21T17:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87314",
    "user": "@jhpalmieri"
}
```

Okay, that's good enough for me.  Thanks for checking that.



---

archive/issue_comments_087315.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9269#issuecomment-87315",
    "user": "@rlmill"
}
```

Resolution: fixed
