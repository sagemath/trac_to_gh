# Issue 5814: %prun doesn't work in the notebook

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-04-17 21:50:36

Assignee: boothby




---

Comment by was created at 2009-04-18 07:06:55

Changing type from defect to enhancement.


---

Comment by was created at 2009-04-18 07:06:55

I'm changing this to an enhancement.  It's not a bug that "random" ipython features don't work in the notebook.  There's no reason they should until they get implemented.

The prun functionality -- which is really the python profiler -- could be used in the notebook by people who know enough about how the profiler works under the hood.  %prun is just IPython's wrapper around Python's standard profiler to make it easier to use.


---

Comment by tkluck created at 2012-08-07 14:53:10

Here's a branch that implements this feature. Feedback appreciated!

https://github.com/tkluck/sagenb/commits/support_prun


---

Comment by tkluck created at 2012-08-07 14:53:10

Changing status from new to needs_review.


---

Comment by kini created at 2012-08-10 09:17:41

Changing status from needs_review to positive_review.


---

Comment by kini created at 2012-08-10 09:17:41

Thanks, tkluck. I see you made a pull request at https://github.com/sagemath/sagenb/pull/91 . Please continue any review process there :)

I'm marking this ticket as invalid.


---

Comment by jdemeyer created at 2012-08-15 07:56:37

Resolution: invalid


---

Attachment

It turns out that this does need to be tackled in the sage library itself. It is possible to add a `prun` object there, which will be automatically used without having to do any special handling in the notebook. I've closed my pull request for the notebook and am reopening this ticket.


---

Comment by tkluck created at 2012-09-05 12:58:16

Changing assignee from boothby to tkluck.


---

Comment by jdemeyer created at 2012-09-11 11:58:14

Resolution changed from invalid to 


---

Comment by jdemeyer created at 2012-09-11 11:58:14

Changing status from closed to new.


---

Comment by tkluck created at 2012-09-11 14:43:13

Changing status from new to needs_review.


---

Comment by tscrim created at 2013-02-12 00:46:50

Just wanting to make sure that this patch ready for review, there are a few people here at Sage Days 45 that would like this feature. (Also do you know someone who would have the expertise to do a full review?)

My quick comment is that you'll need to give doctests to your functions.

Thanks,

Travis


---

Attachment


---

Comment by tkluck created at 2013-03-11 15:51:13

Thanks for your comment, Travis. I just added the doctests. I'm not sure whether any special expertise is necessary, so please go ahead and give this a try.


---

Attachment


---

Comment by tscrim created at 2013-04-01 18:06:13

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2013-04-01 18:06:13

Hey Timo,

I've uploaded a small review patch which fixes the doctests and gives full coverage. Thank you for the patch.

Best,

Travis


```
sage -t ../misc/prun.py
    [6 tests, 0.0 s]
----------------------------------------------------------------------
All tests passed!
----------------------------------------------------------------------
Total time for all tests: 0.2 seconds
    cpu time: 0.0 seconds
    cumulative wall time: 0.0 seconds
```



---

Comment by nbruin created at 2013-04-01 18:44:02

It's probably outside the scope of this ticket, but the _really_ useful thing would be if `%prun ...` in the notebook would return an interactive browser for the `Stat` object that is returned by `cProfile().runctx(...)`. While a basic printout of profiling data gives some indication, one usually needs to dig around a little in the data to find what the real bottleneck is (see where most calls come from, switch between cumulative and proper time, etc.)

Writing such a browser might be a nice exercise for a student who is interested in interface programming. I bet there are good profiler browsers around to get inspiration from.

A tool I haven't used yet but looks like a decent effort is [runsnakerun](https://pypi.python.org/pypi/RunSnakeRun). Duplicating that effort for the sage notebook might not seem like such a smart idea. Perhaps we can make the tool more easily accessible from sage? Given that it uses wxPython that might not be so very easily done ... I ended up installing it using OS tools, meaning that I _have_ to write the profile data to a file and analyse it separately.


---

Comment by tscrim created at 2013-04-03 12:59:59

Replying to [comment:12 nbruin]:
> It's probably outside the scope of this ticket, but the _really_ useful thing would be if `%prun ...` in the notebook would return an interactive browser for the `Stat` object that is returned by `cProfile().runctx(...)`. While a basic printout of profiling data gives some indication, one usually needs to dig around a little in the data to find what the real bottleneck is (see where most calls come from, switch between cumulative and proper time, etc.)

+1/2 since being able to read/interpret the raw data is a good skill to have IMO. However a graphical (or at least a tree structure) of the data is also very useful.
> 
> Writing such a browser might be a nice exercise for a student who is interested in interface programming. I bet there are good profiler browsers around to get inspiration from.

+1 here. I feel like we need a wiki page to keep a list of "good student projects"...

> A tool I haven't used yet but looks like a decent effort is [runsnakerun](https://pypi.python.org/pypi/RunSnakeRun). Duplicating that effort for the sage notebook might not seem like such a smart idea. Perhaps we can make the tool more easily accessible from sage? Given that it uses wxPython that might not be so very easily done ... I ended up installing it using OS tools, meaning that I _have_ to write the profile data to a file and analyse it separately.

I've seen runsnakerun used in a few places (although I haven't used it myself), and instead of duplicating it in the notebook, perhaps we could link it into sage (notebook) as some type of package? Actually...perhaps what we should do is have a variable/function which calls your favorite profiler on the executed command(s), something like:

```
%profile
2 + 2
```



---

Comment by jdemeyer created at 2013-04-04 11:46:18

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-04-04 11:46:18

The first patch isn't a proper HG changeset (patches should be generated using `hg export`, the second patch is fine).


---

Attachment


---

Comment by tscrim created at 2013-04-04 16:33:13

Changing status from needs_work to positive_review.


---

Comment by tscrim created at 2013-04-04 16:33:13

Fixed by combining all the patches into one. I hope that's okay.


---

Comment by tkluck created at 2013-04-05 05:35:34

Thanks for your work on this, Travis! Your changes look excellent.

I'm kind of surprised that you found 20 function calls where I had 3. I'll try that again later, but I trust you on it.


---

Comment by tscrim created at 2013-04-05 12:44:12

That also seemed to be what the patchbot was getting, but if you're still getting fewer function calls, then we will have to change the test slightly. I'm also running these from the command line where I know the preparser is replacing `1` with `Integer(1)` which is an extra function call. I'm guessing you were doing the testing from the notebook? I'm 99% certain the notebook is doing the same, but it might evaluating these _before_ it actually executes the `%prun` test...I'll do some tests later today too.

For patchbot:

Apply: trac_5814-prun_notebook-combined.patch


---

Comment by tscrim created at 2013-04-05 15:35:59

In the notebook I get 3 function calls

```
         3 function calls in 0.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.007    0.007    0.007    0.007 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

with the command line:

```
         3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

So it's something specific to the doctesting framework that's not reflected in sage while it's directly running (I've noticed this in a few other places before too).


---

Comment by jdemeyer created at 2013-04-06 14:50:17

Resolution: fixed


---

Comment by kcrisman created at 2014-10-22 16:24:16

Does this actually work in the notebook?  (Sometimes Ipython upgrades cause trouble with such magic.)  I just get

```
NameError: name 'prun' is not defined
```

in 6.3 and 6.4.beta6.


---

Comment by tscrim created at 2014-10-22 18:49:12

I'm almost sure it did...but it's been so long that I can be certain. Considering we were using iPython 0.13 or something like that at the time, I wouldn't be surprised if something broke along the way.


---

Comment by kcrisman created at 2014-10-22 19:00:42

Does it work for you now?


---

Comment by tscrim created at 2014-10-22 19:09:18

Nope.
