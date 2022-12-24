# Issue 8150: various fixes in sage/groups/ and sage/interfaces needed for GAP 4.4.12

archive/issues_008150.json:
```json
{
    "body": "Assignee: joyner\n\nvarious fixes needed to move to GAP 4.4.12, mostly concerning\nTESTS:: and EXAMPLES::\nDue to apparent changes in GAP internals, some things like the order\nof irreducible characters of a group can change from a previous\nrelease. I made comparisons in docstrings as foolproof as possible.\n\nThese changes actually would also work for 4.4.10 (not tested, but pretty sure)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8150\n\n",
    "created_at": "2010-02-02T09:08:14Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "various fixes in sage/groups/ and sage/interfaces needed for GAP 4.4.12",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8150",
    "user": "@dimpase"
}
```
Assignee: joyner

various fixes needed to move to GAP 4.4.12, mostly concerning
TESTS:: and EXAMPLES::
Due to apparent changes in GAP internals, some things like the order
of irreducible characters of a group can change from a previous
release. I made comparisons in docstrings as foolproof as possible.

These changes actually would also work for 4.4.10 (not tested, but pretty sure)

Issue created by migration from https://trac.sagemath.org/ticket/8150





---

archive/issue_comments_071640.json:
```json
{
    "body": "Attachment [13804.patch](tarball://root/attachments/some-uuid/ticket8150/13804.patch) by @dimpase created at 2010-02-02 09:09:22",
    "created_at": "2010-02-02T09:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71640",
    "user": "@dimpase"
}
```

Attachment [13804.patch](tarball://root/attachments/some-uuid/ticket8150/13804.patch) by @dimpase created at 2010-02-02 09:09:22



---

archive/issue_comments_071641.json:
```json
{
    "body": "`# random order` is preferable to `#not tested`. I think a lot of these could be tested in sensible ways. For example, if word_problem returned a list of *tuples* rather than lists (which is more natural), then one could do\n\n\n```\nsage: w = word_problem([a*b,a*c], b*c)\nsage: set(w) == set([(a*b, 1), (a*c, 1)])\n```\n\n\nEven better, \n\n\n```\nsage: w = word_problem([a*b,a*c], b*c); w # random solution\n[[a*b, 1], [a*c, 1]]\nsage: w == prod(g^e for g,e in w)\nTrue\n```\n\n\nwhich demonstrates that w is indeed a solution. \n\nAlso, it's clearer to us any and all instead of reduce, if you need to. Having huge blocks of `#not tested` should be avoided unless there's no clean way around it.",
    "created_at": "2010-02-02T12:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71641",
    "user": "@robertwb"
}
```

`# random order` is preferable to `#not tested`. I think a lot of these could be tested in sensible ways. For example, if word_problem returned a list of *tuples* rather than lists (which is more natural), then one could do


```
sage: w = word_problem([a*b,a*c], b*c)
sage: set(w) == set([(a*b, 1), (a*c, 1)])
```


Even better, 


```
sage: w = word_problem([a*b,a*c], b*c); w # random solution
[[a*b, 1], [a*c, 1]]
sage: w == prod(g^e for g,e in w)
True
```


which demonstrates that w is indeed a solution. 

Also, it's clearer to us any and all instead of reduce, if you need to. Having huge blocks of `#not tested` should be avoided unless there's no clean way around it.



---

archive/issue_comments_071642.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-02T13:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71642",
    "user": "@dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071643.json:
```json
{
    "body": "Replying to [comment:1 robertwb]:\n> `# random order` is preferable to `#not tested`. \nI can change this, no problem.\n\n> I think a lot of these could be tested in sensible ways. For example, if word_problem returned a list of *tuples* rather than lists (which is more natural), then one could do\n> \n\n```\n sage: w = word_problem([a*b,a*c], b*c)\n sage: set(w) == set([(a*b, 1), (a*c, 1)])\n }}}\n\nThis would mean a redesign. It is doable, I suppose, but I do not know the reason for the original decision to have a list of lists. And I don't see this as urgent, as this would give, at best, a better readable code. \n\n> \n> Even better, \n> \n{{{\n sage: w = word_problem([a*b,a*c], b*c); w # random solution\n [[a*b, 1], [a*c, 1]]\n sage: w == prod(g^e for g,e in w)\n True\n}}}\n> \n> which demonstrates that w is indeed a solution. \n\nwell, this is not working, at least not presently:\n\n{{{\ndima@boxen:~/sage$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\n| Sage Version 4.3.2.alpha1, Release Date: 2010-01-31                |\n| Type notebook() for the GUI, and license() for information.        |\nsage: G.<a,b,c> = AbelianGroup(3,[2,3,4])\nsage: w = word_problem([a*b,a*c], b*c)\nsage: w == prod(g^e for g,e in w)\nFalse\nsage: gap_version()\n'4.4.12'\n}}}\n\n> \n> Also, it's clearer to us any and all instead of reduce, if you need to. Having huge blocks of `#not tested` should be avoided unless there's no clean way around it.\n\nThere is no clean way around them without a major redesign.",
    "created_at": "2010-02-02T13:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71643",
    "user": "@dimpase"
}
```

Replying to [comment:1 robertwb]:
> `# random order` is preferable to `#not tested`. 
I can change this, no problem.

> I think a lot of these could be tested in sensible ways. For example, if word_problem returned a list of *tuples* rather than lists (which is more natural), then one could do
> 

```
 sage: w = word_problem([a*b,a*c], b*c)
 sage: set(w) == set([(a*b, 1), (a*c, 1)])
 }}}

This would mean a redesign. It is doable, I suppose, but I do not know the reason for the original decision to have a list of lists. And I don't see this as urgent, as this would give, at best, a better readable code. 

> 
> Even better, 
> 
{{{
 sage: w = word_problem([a*b,a*c], b*c); w # random solution
 [[a*b, 1], [a*c, 1]]
 sage: w == prod(g^e for g,e in w)
 True
}}}
> 
> which demonstrates that w is indeed a solution. 

well, this is not working, at least not presently:

{{{
dima@boxen:~/sage$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
| Sage Version 4.3.2.alpha1, Release Date: 2010-01-31                |
| Type notebook() for the GUI, and license() for information.        |
sage: G.<a,b,c> = AbelianGroup(3,[2,3,4])
sage: w = word_problem([a*b,a*c], b*c)
sage: w == prod(g^e for g,e in w)
False
sage: gap_version()
'4.4.12'
}}}

> 
> Also, it's clearer to us any and all instead of reduce, if you need to. Having huge blocks of `#not tested` should be avoided unless there's no clean way around it.

There is no clean way around them without a major redesign.



---

archive/issue_comments_071644.json:
```json
{
    "body": "What Robert meant was:\n\n```\nsage: G.<a,b,c> = AbelianGroup(3,[2,3,4])\nsage: w = word_problem([a*b,a*c], b*c)\nsage: b*c == prod(g^e for g,e in w)\nTrue\n```\n",
    "created_at": "2010-02-02T13:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71644",
    "user": "ylchapuy"
}
```

What Robert meant was:

```
sage: G.<a,b,c> = AbelianGroup(3,[2,3,4])
sage: w = word_problem([a*b,a*c], b*c)
sage: b*c == prod(g^e for g,e in w)
True
```




---

archive/issue_comments_071645.json:
```json
{
    "body": "> These changes actually would also work for 4.4.10 (not tested, but pretty sure)\n\nI applied the patch and tested this. Yes, this is basically correct, except for the gap.version() tests.\n\nI now will test the patch after the 4.4.12 spkg is applied.",
    "created_at": "2010-02-02T20:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71645",
    "user": "@wdjoyner"
}
```

> These changes actually would also work for 4.4.10 (not tested, but pretty sure)

I applied the patch and tested this. Yes, this is basically correct, except for the gap.version() tests.

I now will test the patch after the 4.4.12 spkg is applied.



---

archive/issue_comments_071646.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-02T20:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71646",
    "user": "@robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071647.json:
```json
{
    "body": "It's just not a question of whether it passes tests, having huge blocks of `# not tested` is undesireable as well. There have been better suggestions on the mailing list which should be incorporated into this patch.",
    "created_at": "2010-02-02T20:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71647",
    "user": "@robertwb"
}
```

It's just not a question of whether it passes tests, having huge blocks of `# not tested` is undesireable as well. There have been better suggestions on the mailing list which should be incorporated into this patch.



---

archive/issue_comments_071648.json:
```json
{
    "body": "Replying to [comment:5 robertwb]:\n> It's just not a question of whether it passes tests, having huge blocks of `# not tested` is \n> undesireable as well. There have been better suggestions on the mailing list which should \n> be incorporated into this patch. \n\nI hadn't noticed this but in any case\n\n\n```\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/doc/en/constructions/polynomials.rst\"\n        sage -t  \"devel/sage/sage/graphs/generic_graph.py\"\n        sage -t  \"devel/sage/sage/misc/sage_eval.py\"\n        sage -t  \"devel/sage/sage/rings/number_field/number_field.py\"\n        sage -t  \"devel/sage/sage/rings/number_field/number_field_element.pyx\"\n        sage -t  \"devel/sage/sage/structure/element_wrapper.py\" # Segfault\n```\n\n\nFor example,\n\n\n```\nsage -t  \"devel/sage/sage/graphs/generic_graph.py\"          \n**********************************************************************\nFile \"/Users/wdj/sagefiles/sage-4.3.2.alpha1/devel/sage/sage/graphs/generic_graph.py\", line 10222:\n    sage: M.determinant()\nExpected:\n    -712483534798848\nGot:\n    712483534798848\n**********************************************************************\n1 items had failures:\n   1 of  44 in __main__.example_179\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/wdj/.sage//tmp/.doctest_generic_graph.py\n         [28.4 s]\n```\n",
    "created_at": "2010-02-02T22:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71648",
    "user": "@wdjoyner"
}
```

Replying to [comment:5 robertwb]:
> It's just not a question of whether it passes tests, having huge blocks of `# not tested` is 
> undesireable as well. There have been better suggestions on the mailing list which should 
> be incorporated into this patch. 

I hadn't noticed this but in any case


```
The following tests failed:


        sage -t  "devel/sage/doc/en/constructions/polynomials.rst"
        sage -t  "devel/sage/sage/graphs/generic_graph.py"
        sage -t  "devel/sage/sage/misc/sage_eval.py"
        sage -t  "devel/sage/sage/rings/number_field/number_field.py"
        sage -t  "devel/sage/sage/rings/number_field/number_field_element.pyx"
        sage -t  "devel/sage/sage/structure/element_wrapper.py" # Segfault
```


For example,


```
sage -t  "devel/sage/sage/graphs/generic_graph.py"          
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.2.alpha1/devel/sage/sage/graphs/generic_graph.py", line 10222:
    sage: M.determinant()
Expected:
    -712483534798848
Got:
    712483534798848
**********************************************************************
1 items had failures:
   1 of  44 in __main__.example_179
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/wdj/.sage//tmp/.doctest_generic_graph.py
         [28.4 s]
```




---

archive/issue_comments_071649.json:
```json
{
    "body": "Replying to [comment:6 wdj]:\n[...]\n> I hadn't noticed this but in any case\n> \n\n```\nThe following tests failed:\n \n         sage -t  \"devel/sage/doc/en/constructions/polynomials.rst\"\n         sage -t  \"devel/sage/sage/graphs/generic_graph.py\"\n         sage -t  \"devel/sage/sage/misc/sage_eval.py\"\n         sage -t  \"devel/sage/sage/rings/number_field/number_field.py\"\n         sage -t  \"devel/sage/sage/rings/number_field/number_field_element.pyx\"\n         sage -t  \"devel/sage/sage/structure/element_wrapper.py\" # Segfault\n```\n\n\nthe first 5 are trivial to fix (already done). I am unable to reproduce\nthe last one:\n\n\n```\ndima@boxen:~/sage$ ./sage -t -long devel/sage/sage/structure/element_wrapper.py \nsage -t -long \"devel/sage/sage/structure/element_wrapper.py\"\n\t [4.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\n```\n\n\nAre we testing on the same codebase?\n(4.3.2.alpha1 with my gap-4.4.12 and other related (database_gap and gap_packages) spkgs)\n\nWhat hardware/OS/compiler? \nhere:\n\n```\nLinux boxen 2.6.24-24-server #1 SMP Sat Aug 22 00:59:57 UTC 2009 x86_64 GNU/Linux\ngcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu4)\n```\n",
    "created_at": "2010-02-03T04:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71649",
    "user": "@dimpase"
}
```

Replying to [comment:6 wdj]:
[...]
> I hadn't noticed this but in any case
> 

```
The following tests failed:
 
         sage -t  "devel/sage/doc/en/constructions/polynomials.rst"
         sage -t  "devel/sage/sage/graphs/generic_graph.py"
         sage -t  "devel/sage/sage/misc/sage_eval.py"
         sage -t  "devel/sage/sage/rings/number_field/number_field.py"
         sage -t  "devel/sage/sage/rings/number_field/number_field_element.pyx"
         sage -t  "devel/sage/sage/structure/element_wrapper.py" # Segfault
```


the first 5 are trivial to fix (already done). I am unable to reproduce
the last one:


```
dima@boxen:~/sage$ ./sage -t -long devel/sage/sage/structure/element_wrapper.py 
sage -t -long "devel/sage/sage/structure/element_wrapper.py"
	 [4.7 s]
 
----------------------------------------------------------------------
All tests passed!
```


Are we testing on the same codebase?
(4.3.2.alpha1 with my gap-4.4.12 and other related (database_gap and gap_packages) spkgs)

What hardware/OS/compiler? 
here:

```
Linux boxen 2.6.24-24-server #1 SMP Sat Aug 22 00:59:57 UTC 2009 x86_64 GNU/Linux
gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu4)
```




---

archive/issue_comments_071650.json:
```json
{
    "body": "Sorry, I should have added that the last failure I reported was unrelated (it was on a mac 10.6.2, where this segfault wasthe only failure on a clean install of 4.3.2.a1). Looks like you have fixed everything then!\n\nLet me know when a new patch is available and if I should apply it on top of the old patch or not.",
    "created_at": "2010-02-03T11:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71650",
    "user": "@wdjoyner"
}
```

Sorry, I should have added that the last failure I reported was unrelated (it was on a mac 10.6.2, where this segfault wasthe only failure on a clean install of 4.3.2.a1). Looks like you have fixed everything then!

Let me know when a new patch is available and if I should apply it on top of the old patch or not.



---

archive/issue_comments_071651.json:
```json
{
    "body": "Attachment [13805.patch](tarball://root/attachments/some-uuid/ticket8150/13805.patch) by @dimpase created at 2010-02-03 12:32:12\n\nupdate patch - apply after 13804",
    "created_at": "2010-02-03T12:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71651",
    "user": "@dimpase"
}
```

Attachment [13805.patch](tarball://root/attachments/some-uuid/ticket8150/13805.patch) by @dimpase created at 2010-02-03 12:32:12

update patch - apply after 13804



---

archive/issue_comments_071652.json:
```json
{
    "body": "Replying to [comment:8 wdj]:\n> Sorry, I should have added that the last failure I reported was unrelated (it was on a mac 10.6.2, where this segfault wasthe only failure on a clean install of 4.3.2.a1). Looks like you have fixed everything then!\n> \n> Let me know when a new patch is available and if I should apply it on top of the old patch or not.\n\njust uploaded new patch 13805 here, that should be applied on top of 13804.\nNote that these updates are now gap-4.4.12-only - they will break 4.4.10!\n\nThis should be it...",
    "created_at": "2010-02-03T12:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71652",
    "user": "@dimpase"
}
```

Replying to [comment:8 wdj]:
> Sorry, I should have added that the last failure I reported was unrelated (it was on a mac 10.6.2, where this segfault wasthe only failure on a clean install of 4.3.2.a1). Looks like you have fixed everything then!
> 
> Let me know when a new patch is available and if I should apply it on top of the old patch or not.

just uploaded new patch 13805 here, that should be applied on top of 13804.
Note that these updates are now gap-4.4.12-only - they will break 4.4.10!

This should be it...



---

archive/issue_comments_071653.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-03T12:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71653",
    "user": "@dimpase"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071654.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-03T18:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71654",
    "user": "@wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071655.json:
```json
{
    "body": "With both patches applied (and the 4.4.12 gap spkg) , this now passes sage -testall except for the segfault already reported.\n\nPositive review but maybe this should be tested on other platforms?\n\nThanks Dima!",
    "created_at": "2010-02-03T18:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71655",
    "user": "@wdjoyner"
}
```

With both patches applied (and the 4.4.12 gap spkg) , this now passes sage -testall except for the segfault already reported.

Positive review but maybe this should be tested on other platforms?

Thanks Dima!



---

archive/issue_comments_071656.json:
```json
{
    "body": "I think you misunderstood what I was going for. A test like\n\n\n```\n        sage: G.<a,b,c> = AbelianGroup(3,[2,3,4]); G \n        Multiplicative Abelian Group isomorphic to C2 x C3 x C4 \n        sage: w = word_problem([a*b,a*c], b*c); w  # random solution\n        [[a*b, 1], [a*c, 1]]   \n        sage: prod([x^i for x,i in w]) == a  \n        sage: True\n```\n\n\nis perfectly fine to have in the EXAMPLES section, perfectly illustrating the math and the implementation. Much preferable to having a separate TEST section and a bunch of examples with a #random or #not tested marker. (FYI, what the #random marker means is \"run this test, but ignore the output\" so you don't need it for the \"setup\" steps. Also, in terms of patch naming, 13804 is only unique to you--it's usually easier for others if the patches are named with the ticket number in them. \n\nI'm not trying to be overly judgmental, just trying to give advice that will make things better. I appreciate the work your putting into this!",
    "created_at": "2010-02-03T20:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71656",
    "user": "@robertwb"
}
```

I think you misunderstood what I was going for. A test like


```
        sage: G.<a,b,c> = AbelianGroup(3,[2,3,4]); G 
        Multiplicative Abelian Group isomorphic to C2 x C3 x C4 
        sage: w = word_problem([a*b,a*c], b*c); w  # random solution
        [[a*b, 1], [a*c, 1]]   
        sage: prod([x^i for x,i in w]) == a  
        sage: True
```


is perfectly fine to have in the EXAMPLES section, perfectly illustrating the math and the implementation. Much preferable to having a separate TEST section and a bunch of examples with a #random or #not tested marker. (FYI, what the #random marker means is "run this test, but ignore the output" so you don't need it for the "setup" steps. Also, in terms of patch naming, 13804 is only unique to you--it's usually easier for others if the patches are named with the ticket number in them. 

I'm not trying to be overly judgmental, just trying to give advice that will make things better. I appreciate the work your putting into this!



---

archive/issue_comments_071657.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-03T20:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71657",
    "user": "@robertwb"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071658.json:
```json
{
    "body": "updated patch - replaces 13804 and 13805",
    "created_at": "2010-02-04T05:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71658",
    "user": "@dimpase"
}
```

updated patch - replaces 13804 and 13805



---

archive/issue_comments_071659.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-04T05:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71659",
    "user": "@dimpase"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071660.json:
```json
{
    "body": "Attachment [trac-8150.patch](tarball://root/attachments/some-uuid/ticket8150/trac-8150.patch) by @dimpase created at 2010-02-04 05:58:52\n\nReplying to [comment:11 robertwb]:\n> I think you misunderstood what I was going for. A test like\n[...] \n> \n> is perfectly fine to have in the EXAMPLES section, perfectly illustrating the math > and the implementation. \nI have fixed all this (only one TEST is left, in class_function.py, as I think it's\ntoo ugly to have in EXAMPLES) in just uploaded here cumulative patch named trac-8150. (so it subsumes the previous two that are to be discarded.)\nThe rest are re-done as you suggest.\nPlease take a look.",
    "created_at": "2010-02-04T05:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71660",
    "user": "@dimpase"
}
```

Attachment [trac-8150.patch](tarball://root/attachments/some-uuid/ticket8150/trac-8150.patch) by @dimpase created at 2010-02-04 05:58:52

Replying to [comment:11 robertwb]:
> I think you misunderstood what I was going for. A test like
[...] 
> 
> is perfectly fine to have in the EXAMPLES section, perfectly illustrating the math > and the implementation. 
I have fixed all this (only one TEST is left, in class_function.py, as I think it's
too ugly to have in EXAMPLES) in just uploaded here cumulative patch named trac-8150. (so it subsumes the previous two that are to be discarded.)
The rest are re-done as you suggest.
Please take a look.



---

archive/issue_comments_071661.json:
```json
{
    "body": "Sorry Robert, I guess I misunderstood and should not have given it the positive review.\n\nI'm retesting the new patch now.",
    "created_at": "2010-02-04T12:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71661",
    "user": "@wdjoyner"
}
```

Sorry Robert, I guess I misunderstood and should not have given it the positive review.

I'm retesting the new patch now.



---

archive/issue_comments_071662.json:
```json
{
    "body": "Passes as before. \n\nI'll leave it to Robert Bradshaw now to decide if it should receive a positive review.",
    "created_at": "2010-02-04T14:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71662",
    "user": "@wdjoyner"
}
```

Passes as before. 

I'll leave it to Robert Bradshaw now to decide if it should receive a positive review.



---

archive/issue_comments_071663.json:
```json
{
    "body": "Looks very good now. I agree that the irreducible_characters one is ugly enough to go in TESTS, and thanks wdj for running all the tests again. I say it's ready to go in.",
    "created_at": "2010-02-04T18:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71663",
    "user": "@robertwb"
}
```

Looks very good now. I agree that the irreducible_characters one is ugly enough to go in TESTS, and thanks wdj for running all the tests again. I say it's ready to go in.



---

archive/issue_comments_071664.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-04T18:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71664",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071665.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T20:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71665",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_071666.json:
```json
{
    "body": "Merged [trac-8150.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8150/trac-8150.patch) with a sensible commit message containing the ticket number.",
    "created_at": "2010-02-17T20:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8150#issuecomment-71666",
    "user": "mvngu"
}
```

Merged [trac-8150.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8150/trac-8150.patch) with a sensible commit message containing the ticket number.
