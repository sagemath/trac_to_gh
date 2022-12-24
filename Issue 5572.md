# Issue 5572: fast_callable improvements (followup for #5093)

archive/issues_005572.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @robertwb @TimDumol @eviatarbach @novoselt @orlitzky\n\nThe code at #5093 is very good and ready to go in, but there are several improvements that have been suggested and agreed work on at a later date. They are posted here so we can merge and close the other ticket. \n\nSpecifically, \n\nNot fixed:\n\n* Robert's suggestion: an option that uses a fast domain, if it's there, but ignores the domain parameter if it's not (I don't mind the idea, and the implementation is easy; what should the syntax be? Part of my problem picking a syntax is that I don't want to promise that a specialized interpreter is always faster than the Python-object interpreter, so I don't particularly want to use the word \"fast\" in any option names.)\n\n* fast_callable on list,tuple,vector,matrix arguments\n\n* any interaction with #5413 (my plan is to wait until either #5093 or #5413 gets a positive review, then fix the other one to match)\n\n* fast_callable on constant arguments (waiting for a spec from Jason!)\n\n* fast_callable of a zero multivariate polynomial returns a zero of the base ring, without paying attention to the types of the arguments\n\nIssue created by migration from https://trac.sagemath.org/ticket/5572\n\n",
    "created_at": "2009-03-19T23:55:25Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "fast_callable improvements (followup for #5093)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5572",
    "user": "@robertwb"
}
```
Assignee: somebody

CC:  @robertwb @TimDumol @eviatarbach @novoselt @orlitzky

The code at #5093 is very good and ready to go in, but there are several improvements that have been suggested and agreed work on at a later date. They are posted here so we can merge and close the other ticket. 

Specifically, 

Not fixed:

* Robert's suggestion: an option that uses a fast domain, if it's there, but ignores the domain parameter if it's not (I don't mind the idea, and the implementation is easy; what should the syntax be? Part of my problem picking a syntax is that I don't want to promise that a specialized interpreter is always faster than the Python-object interpreter, so I don't particularly want to use the word "fast" in any option names.)

* fast_callable on list,tuple,vector,matrix arguments

* any interaction with #5413 (my plan is to wait until either #5093 or #5413 gets a positive review, then fix the other one to match)

* fast_callable on constant arguments (waiting for a spec from Jason!)

* fast_callable of a zero multivariate polynomial returns a zero of the base ring, without paying attention to the types of the arguments

Issue created by migration from https://trac.sagemath.org/ticket/5572





---

archive/issue_comments_043409.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2009-03-26T02:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43409",
    "user": "cwitty"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_043410.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-26T02:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43410",
    "user": "cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043411.json:
```json
{
    "body": "More fast_callable improvements:\n\n* domain=float is the same as domain=RDF, but domain=complex is not the same as domain=CDF.  Make domain=complex use the same interpreter as domain=CDF\n\n* if g is a callable expression, then fast_callable(g) should use g.args() for the variables, not g.variables().  Hmm...or maybe return an error if g.args() is not equal to g.variables(), since every variable really does have to be satisfied.",
    "created_at": "2009-09-24T19:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43411",
    "user": "@jasongrout"
}
```

More fast_callable improvements:

* domain=float is the same as domain=RDF, but domain=complex is not the same as domain=CDF.  Make domain=complex use the same interpreter as domain=CDF

* if g is a callable expression, then fast_callable(g) should use g.args() for the variables, not g.variables().  Hmm...or maybe return an error if g.args() is not equal to g.variables(), since every variable really does have to be satisfied.



---

archive/issue_comments_043412.json:
```json
{
    "body": "Both good points. At least g.variables() should be a subset of g.args().",
    "created_at": "2009-09-24T20:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43412",
    "user": "@robertwb"
}
```

Both good points. At least g.variables() should be a subset of g.args().



---

archive/issue_comments_043413.json:
```json
{
    "body": "Replying to [comment:2 jason]:\n\n>  * if g is a callable expression, then fast_callable(g) should use g.args() for the variables, not g.variables().  Hmm...or maybe return an error if g.args() is not equal to g.variables(), since every variable really does have to be satisfied.\n\n#7512 may take care of this.",
    "created_at": "2010-04-24T06:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43413",
    "user": "@jasongrout"
}
```

Replying to [comment:2 jason]:

>  * if g is a callable expression, then fast_callable(g) should use g.args() for the variables, not g.variables().  Hmm...or maybe return an error if g.args() is not equal to g.variables(), since every variable really does have to be satisfied.

#7512 may take care of this.



---

archive/issue_comments_043414.json:
```json
{
    "body": "Attachment [improve_fast_callable.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.patch) by @jasongrout created at 2010-04-24 11:35:19\n\nThis is a big patch to fast_callable which \n\n* makes it work for lists/tuples like fast_float does\n* adds lots of _fast_callable_ methods to make it work on a lot of different constant objects (integers/rationals/RDF/RR/CDF/CC)\n* refactors the code a bit\n* in general replaces calls to fast_float with calls to fast_callable.\n \nThe patch also breaks some things---it's still a work in progress.",
    "created_at": "2010-04-24T11:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43414",
    "user": "@jasongrout"
}
```

Attachment [improve_fast_callable.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.patch) by @jasongrout created at 2010-04-24 11:35:19

This is a big patch to fast_callable which 

* makes it work for lists/tuples like fast_float does
* adds lots of _fast_callable_ methods to make it work on a lot of different constant objects (integers/rationals/RDF/RR/CDF/CC)
* refactors the code a bit
* in general replaces calls to fast_float with calls to fast_callable.
 
The patch also breaks some things---it's still a work in progress.



---

archive/issue_comments_043415.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2010-04-24T11:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43415",
    "user": "@jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_043416.json:
```json
{
    "body": "Attachment [fast_callable_complex.patch](tarball://root/attachments/some-uuid/ticket5572/fast_callable_complex.patch) by @jasongrout created at 2010-04-24 11:36:40\n\nThe second patch is a broken attempt at streamlining the complex support since Cython now supports C99 complex numbers.",
    "created_at": "2010-04-24T11:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43416",
    "user": "@jasongrout"
}
```

Attachment [fast_callable_complex.patch](tarball://root/attachments/some-uuid/ticket5572/fast_callable_complex.patch) by @jasongrout created at 2010-04-24 11:36:40

The second patch is a broken attempt at streamlining the complex support since Cython now supports C99 complex numbers.



---

archive/issue_comments_043417.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-04-24T11:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43417",
    "user": "@jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_043418.json:
```json
{
    "body": "CCing: robertwb since fast_float was his idea originally\n\ntimdumol since he's expressed interest in working on this sort of thing.\n\nThe two patches need work at this point.  In particular, the improvements patch needs docs added/changed, and ptestlong needs to be run to check for breakage.\n\nThe complex number patch needs an overhaul, as I think it's completely broken at this point.  The complex number patch is not necessary for resolving the issues on this ticket.",
    "created_at": "2010-04-26T11:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43418",
    "user": "@jasongrout"
}
```

CCing: robertwb since fast_float was his idea originally

timdumol since he's expressed interest in working on this sort of thing.

The two patches need work at this point.  In particular, the improvements patch needs docs added/changed, and ptestlong needs to be run to check for breakage.

The complex number patch needs an overhaul, as I think it's completely broken at this point.  The complex number patch is not necessary for resolving the issues on this ticket.



---

archive/issue_comments_043419.json:
```json
{
    "body": "#8450 would be a good ticket to (trivially) fix after this ticket moves plotting solely over to fast_callable.",
    "created_at": "2010-04-26T12:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43419",
    "user": "@jasongrout"
}
```

#8450 would be a good ticket to (trivially) fix after this ticket moves plotting solely over to fast_callable.



---

archive/issue_comments_043420.json:
```json
{
    "body": "rebase to 4.4.1",
    "created_at": "2010-05-04T05:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43420",
    "user": "@jasongrout"
}
```

rebase to 4.4.1



---

archive/issue_comments_043421.json:
```json
{
    "body": "Attachment [improve_fast_callable.2.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.2.patch) by @jasongrout created at 2010-05-26 19:36:52\n\nI think it might be best just to fix #7512 in this ticket.",
    "created_at": "2010-05-26T19:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43421",
    "user": "@jasongrout"
}
```

Attachment [improve_fast_callable.2.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.2.patch) by @jasongrout created at 2010-05-26 19:36:52

I think it might be best just to fix #7512 in this ticket.



---

archive/issue_comments_043422.json:
```json
{
    "body": "Attachment [improve_fast_callable.3.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.3.patch) by @jasongrout created at 2010-05-27 07:55:39\n\napply instead of previous patches",
    "created_at": "2010-05-27T07:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43422",
    "user": "@jasongrout"
}
```

Attachment [improve_fast_callable.3.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.3.patch) by @jasongrout created at 2010-05-27 07:55:39

apply instead of previous patches



---

archive/issue_comments_043423.json:
```json
{
    "body": "Still not done.  A clean design still needs to happen for fast_callable on symbolics without specified variables, and the nvars option seems like a hack to make plotting work with lambda functions (since we now match the argument names of lambda functions by default).",
    "created_at": "2010-05-27T07:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43423",
    "user": "@jasongrout"
}
```

Still not done.  A clean design still needs to happen for fast_callable on symbolics without specified variables, and the nvars option seems like a hack to make plotting work with lambda functions (since we now match the argument names of lambda functions by default).



---

archive/issue_comments_043424.json:
```json
{
    "body": "Also, something should be done to put fast_float back (and its file) as a convenience method.",
    "created_at": "2010-05-27T08:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43424",
    "user": "@jasongrout"
}
```

Also, something should be done to put fast_float back (and its file) as a convenience method.



---

archive/issue_comments_043425.json:
```json
{
    "body": "Attachment [improve_fast_callable.4.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.4.patch) by @jasongrout created at 2010-05-27 08:27:03\n\napply instead of previous patches (now doctests in plot/*.py[x] pass)",
    "created_at": "2010-05-27T08:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43425",
    "user": "@jasongrout"
}
```

Attachment [improve_fast_callable.4.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.4.patch) by @jasongrout created at 2010-05-27 08:27:03

apply instead of previous patches (now doctests in plot/*.py[x] pass)



---

archive/issue_comments_043426.json:
```json
{
    "body": "apply instead of previous patches (now almost all doctests in plot/plot3d/ pass)",
    "created_at": "2010-05-27T19:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43426",
    "user": "@jasongrout"
}
```

apply instead of previous patches (now almost all doctests in plot/plot3d/ pass)



---

archive/issue_comments_043427.json:
```json
{
    "body": "Attachment [improve_fast_callable.5.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.5.patch) by @jasongrout created at 2010-05-27 19:31:27\n\nI had to rework some of the transformation code because the returned function often did not have the same keyword arguments as the original function, which throws off plotting.",
    "created_at": "2010-05-27T19:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43427",
    "user": "@jasongrout"
}
```

Attachment [improve_fast_callable.5.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.5.patch) by @jasongrout created at 2010-05-27 19:31:27

I had to rework some of the transformation code because the returned function often did not have the same keyword arguments as the original function, which throws off plotting.



---

archive/issue_comments_043428.json:
```json
{
    "body": "Attachment [improve_fast_callable.6.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.6.patch) by @jasongrout created at 2010-05-28 06:20:39\n\napply instead of previous patches (fixed a bunch of stuff so even more doctests pass)",
    "created_at": "2010-05-28T06:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43428",
    "user": "@jasongrout"
}
```

Attachment [improve_fast_callable.6.patch](tarball://root/attachments/some-uuid/ticket5572/improve_fast_callable.6.patch) by @jasongrout created at 2010-05-28 06:20:39

apply instead of previous patches (fixed a bunch of stuff so even more doctests pass)



---

archive/issue_comments_043429.json:
```json
{
    "body": "To delete the fast_eval.so file from the build directory (necessary so that the cython fast_eval is eliminated when testing), do:\n\n\n```\ncd $SAGE_ROOT/devel/sage/build\nfind . -name fast_eval.so | xargs rm\n```\n",
    "created_at": "2010-09-05T01:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43429",
    "user": "@jasongrout"
}
```

To delete the fast_eval.so file from the build directory (necessary so that the cython fast_eval is eliminated when testing), do:


```
cd $SAGE_ROOT/devel/sage/build
find . -name fast_eval.so | xargs rm
```




---

archive/issue_comments_043430.json:
```json
{
    "body": "Progress report: my current patch queue has the following failures on `make ptestlong` on Sage 4.5.2:\n\n\n```\n\tsage -t  -long 4.5.2/devel/sage/sage/structure/sage_object.pyx # 1 doctests failed\n\tsage -t  -long 4.5.2/devel/sage/sage/ext/fast_callable.pyx # Exception from doctest framework\n\tsage -t  -long 4.5.2/devel/sage/sage/rings/polynomial/polynomial_element.pyx # 9 doctests failed\n\tsage -t  -long 4.5.2/devel/sage/sage/stats/hmm/distributions.pyx # 1 doctests failed\n\n```\n",
    "created_at": "2010-09-05T02:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43430",
    "user": "@jasongrout"
}
```

Progress report: my current patch queue has the following failures on `make ptestlong` on Sage 4.5.2:


```
	sage -t  -long 4.5.2/devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
	sage -t  -long 4.5.2/devel/sage/sage/ext/fast_callable.pyx # Exception from doctest framework
	sage -t  -long 4.5.2/devel/sage/sage/rings/polynomial/polynomial_element.pyx # 9 doctests failed
	sage -t  -long 4.5.2/devel/sage/sage/stats/hmm/distributions.pyx # 1 doctests failed

```




---

archive/issue_comments_043431.json:
```json
{
    "body": "(my patch queue is up at http://sage.math.washington.edu/home/jason/sage-4.5.2-patches and this ticket involves patches up to pickling.patch)",
    "created_at": "2010-09-05T03:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43431",
    "user": "@jasongrout"
}
```

(my patch queue is up at http://sage.math.washington.edu/home/jason/sage-4.5.2-patches and this ticket involves patches up to pickling.patch)



---

archive/issue_comments_043432.json:
```json
{
    "body": "What is the status of switching to `fast_callable`?  There seem to be a number of tickets which would benefit, not to mention the fact that `fast_float` has old-style documentation which looks bad in the command line :)  Plus, if `fast_float` is to be deprecated (even though it seems to use `fast_callable` under the hood) it would be helpful to start that process.  \n\nAnyway, just curious.",
    "created_at": "2011-06-24T14:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43432",
    "user": "@kcrisman"
}
```

What is the status of switching to `fast_callable`?  There seem to be a number of tickets which would benefit, not to mention the fact that `fast_float` has old-style documentation which looks bad in the command line :)  Plus, if `fast_float` is to be deprecated (even though it seems to use `fast_callable` under the hood) it would be helpful to start that process.  

Anyway, just curious.



---

archive/issue_comments_043433.json:
```json
{
    "body": "A long time ago I worked on the patches you see here; I believe that all of my work is here, anyway.  I probably won't have time to work on this this summer, due to notebook enhancements.  I'd like to make this one of the projects for next summer if someone hasn't beaten me to it by then.",
    "created_at": "2011-06-24T16:25:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43433",
    "user": "@jasongrout"
}
```

A long time ago I worked on the patches you see here; I believe that all of my work is here, anyway.  I probably won't have time to work on this this summer, due to notebook enhancements.  I'd like to make this one of the projects for next summer if someone hasn't beaten me to it by then.



---

archive/issue_comments_043434.json:
```json
{
    "body": "The problem is that I think my patch is too big and needs to be broken down into smaller patches that change less at each step.  It's been a long time, but I think I'm remembering that right.  Anyways, as noted above, my patch queue is up on sage.math and anyone is welcome to work on it.",
    "created_at": "2011-06-24T16:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43434",
    "user": "@jasongrout"
}
```

The problem is that I think my patch is too big and needs to be broken down into smaller patches that change less at each step.  It's been a long time, but I think I'm remembering that right.  Anyways, as noted above, my patch queue is up on sage.math and anyone is welcome to work on it.



---

archive/issue_comments_043435.json:
```json
{
    "body": "Can I just create a new patch to switch plotting to use `fast_callable`? Using `fast_float` causes big problems for plotting, namely that any point at which the function is complex at some value in the call stack fails to plot. For example, the plot of `abs(log(x))` will not show up for negative `x`, despite the output being guaranteed to be real, since `fast_float` will evaluate `log(x)` first and choke on the complex number.",
    "created_at": "2013-08-10T00:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43435",
    "user": "@eviatarbach"
}
```

Can I just create a new patch to switch plotting to use `fast_callable`? Using `fast_float` causes big problems for plotting, namely that any point at which the function is complex at some value in the call stack fails to plot. For example, the plot of `abs(log(x))` will not show up for negative `x`, despite the output being guaranteed to be real, since `fast_float` will evaluate `log(x)` first and choke on the complex number.



---

archive/issue_comments_043436.json:
```json
{
    "body": "Sounds fine to me.  Especially if all the doctests pass (including the new one or two that you write :).",
    "created_at": "2013-08-10T00:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43436",
    "user": "@jasongrout"
}
```

Sounds fine to me.  Especially if all the doctests pass (including the new one or two that you write :).



---

archive/issue_comments_043437.json:
```json
{
    "body": "Okay, thanks. This is now #15030, with a patch up.",
    "created_at": "2013-08-10T10:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43437",
    "user": "@eviatarbach"
}
```

Okay, thanks. This is now #15030, with a patch up.



---

archive/issue_comments_043438.json:
```json
{
    "body": "Note that #15030 is now merged.  How that does affect whatever else needs to happen here?",
    "created_at": "2014-04-21T13:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43438",
    "user": "@kcrisman"
}
```

Note that #15030 is now merged.  How that does affect whatever else needs to happen here?



---

archive/issue_comments_043439.json:
```json
{
    "body": "Anyone interested in the deprecation of `fast_float` can find relevant tickets at https://trac.sagemath.org/wiki/symbolics#fast_floatdeprecation",
    "created_at": "2018-01-14T08:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43439",
    "user": "@rwst"
}
```

Anyone interested in the deprecation of `fast_float` can find relevant tickets at https://trac.sagemath.org/wiki/symbolics#fast_floatdeprecation



---

archive/issue_comments_043440.json:
```json
{
    "body": "Without looking in detail I'd guess that implementing https://github.com/pynac/pynac/issues/8 will make `ex.subs()` a much faster alternative to `fast_callable`.",
    "created_at": "2018-01-14T13:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5572#issuecomment-43440",
    "user": "@rwst"
}
```

Without looking in detail I'd guess that implementing https://github.com/pynac/pynac/issues/8 will make `ex.subs()` a much faster alternative to `fast_callable`.
