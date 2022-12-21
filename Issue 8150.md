# Issue 8150: various fixes in sage/groups/ and sage/interfaces needed for GAP 4.4.12

Issue created by migration from Trac.

Original creator: dimpase

Original creation time: 2010-02-02 09:08:14

Assignee: joyner

various fixes needed to move to GAP 4.4.12, mostly concerning
TESTS:: and EXAMPLES::
Due to apparent changes in GAP internals, some things like the order
of irreducible characters of a group can change from a previous
release. I made comparisons in docstrings as foolproof as possible.

These changes actually would also work for 4.4.10 (not tested, but pretty sure)


---

Attachment


---

Comment by robertwb created at 2010-02-02 12:43:09

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

Comment by dimpase created at 2010-02-02 13:02:26

Changing status from new to needs_review.


---

Comment by dimpase created at 2010-02-02 13:02:26

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
dima`@`boxen:~/sage$ ./sage
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

Comment by ylchapuy created at 2010-02-02 13:39:22

What Robert meant was:

```
sage: G.<a,b,c> = AbelianGroup(3,[2,3,4])
sage: w = word_problem([a*b,a*c], b*c)
sage: b*c == prod(g^e for g,e in w)
True
```



---

Comment by wdj created at 2010-02-02 20:47:15

> These changes actually would also work for 4.4.10 (not tested, but pretty sure)

I applied the patch and tested this. Yes, this is basically correct, except for the gap.version() tests.

I now will test the patch after the 4.4.12 spkg is applied.


---

Comment by robertwb created at 2010-02-02 20:57:17

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2010-02-02 20:57:17

It's just not a question of whether it passes tests, having huge blocks of `# not tested` is undesireable as well. There have been better suggestions on the mailing list which should be incorporated into this patch.


---

Comment by wdj created at 2010-02-02 22:48:39

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

Comment by dimpase created at 2010-02-03 04:41:10

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
dima`@`boxen:~/sage$ ./sage -t -long devel/sage/sage/structure/element_wrapper.py 
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

Comment by wdj created at 2010-02-03 11:41:05

Sorry, I should have added that the last failure I reported was unrelated (it was on a mac 10.6.2, where this segfault wasthe only failure on a clean install of 4.3.2.a1). Looks like you have fixed everything then!

Let me know when a new patch is available and if I should apply it on top of the old patch or not.


---

Attachment

update patch - apply after 13804


---

Comment by dimpase created at 2010-02-03 12:35:34

Replying to [comment:8 wdj]:
> Sorry, I should have added that the last failure I reported was unrelated (it was on a mac 10.6.2, where this segfault wasthe only failure on a clean install of 4.3.2.a1). Looks like you have fixed everything then!
> 
> Let me know when a new patch is available and if I should apply it on top of the old patch or not.

just uploaded new patch 13805 here, that should be applied on top of 13804.
Note that these updates are now gap-4.4.12-only - they will break 4.4.10!

This should be it...


---

Comment by dimpase created at 2010-02-03 12:35:34

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2010-02-03 18:25:55

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-02-03 18:25:55

With both patches applied (and the 4.4.12 gap spkg) , this now passes sage -testall except for the segfault already reported.

Positive review but maybe this should be tested on other platforms?

Thanks Dima!


---

Comment by robertwb created at 2010-02-03 20:52:04

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

Comment by robertwb created at 2010-02-03 20:52:04

Changing status from positive_review to needs_work.


---

Comment by dimpase created at 2010-02-04 05:51:59

updated patch - replaces 13804 and 13805


---

Comment by dimpase created at 2010-02-04 05:58:52

Changing status from needs_work to needs_review.


---

Attachment

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

Comment by wdj created at 2010-02-04 12:36:13

Sorry Robert, I guess I misunderstood and should not have given it the positive review.

I'm retesting the new patch now.


---

Comment by wdj created at 2010-02-04 14:24:54

Passes as before. 

I'll leave it to Robert Bradshaw now to decide if it should receive a positive review.


---

Comment by robertwb created at 2010-02-04 18:26:03

Looks very good now. I agree that the irreducible_characters one is ugly enough to go in TESTS, and thanks wdj for running all the tests again. I say it's ready to go in.


---

Comment by robertwb created at 2010-02-04 18:26:03

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-17 20:53:36

Resolution: fixed


---

Comment by mvngu created at 2010-02-17 20:53:36

Merged [trac-8150.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8150/trac-8150.patch) with a sensible commit message containing the ticket number.
