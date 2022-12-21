# Issue 5438: Incorrect documentation and/or functionality in plot filling

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-03-04 17:31:01

Assignee: was

CC:  whuss

Keywords: plot fill

The following example from documentation seems to work:


```
def b(n): return lambda x: bessel_J(n, x) + 0.5*(n-1)
plot([b(c) for c in [1..5]], 0, 40, fill = dict([(i, i+1) for i in [0..3]]))
```

but the behavior is the same as

```
def b(n): return lambda x: bessel_J(n, x) + 0.5*(n-1)
plot([b(c) for c in [1..5]], 0, 40, fill = dict([(i, 5) for i in [0..3]]))
```

or anything else that evaluates to True as the second element of the dict.  The proper behavior is 

```
def b(n): return lambda x: bessel_J(n, x) + 0.5*(n-1)
plot([b(c) for c in [1..5]], 0, 40, fill = dict([(i, [i+1]) for i in [0..3]]))
```

which is incidentally quite beautiful.

There are a few other such misleading/wrong example, and the documentation for how to use a dictionary which is a little confusing for people not familiar with Python yet

However, this is really related to a bug, namely that for some reason the option of plotting between a function and a line isn't parsing properly.  These should hopefully be easy to fix and are closely related enough that one ticket seemed appropriate.


---

Comment by kcrisman created at 2009-03-04 17:47:49

Changing assignee from was to kcrisman.


---

Comment by kcrisman created at 2009-03-04 17:47:49

Problem is that the first check in fill is for 

```
            if fill == 'axis' or fill == True:
```

and we have

```
sage: preparse('5==True')
'Integer(5)==True'
sage: 5==True
True
```

A change to 

```
            if fill == 'axis' or fill is True:
```

solves the problem, and then improving doc is easy.  I should be able to do this within a day or two.


---

Comment by kcrisman created at 2009-03-04 17:47:49

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-03-07 03:08:58

In addition to changing "==" to "is", this patch fixes a lot of minor issues in plot that I discovered while fixing this issue, mostly around documentation of the adaptive refinement, but also some weird bugs in error handling that nobody noticed since who sets verbose=1 on a regular basis?

I didn't add doctests for the change from (msg, x) to (msg, xi) since it refers to the line of code and I figured that is a big hassle to change every time the plot code is changed, but if a referee disagrees they may add some.  I also removed the final exceptions+=1 block in the generate_plot_points since it seemed to be redundant, but if that's wrong then bring it back.  Otherwise I think everything works.


---

Comment by wcauchois created at 2009-03-17 23:27:34

REFEREE REPORT:

Applies fine to Sage 3.4, and fixes the bug described in the ticket. The changes to the documentation also look solid. One thing I noticed is that plot.py fails two of its unit tests (related to generate_plot_points, on lines 3028 and 3031; maybe a modification to the adaptive refinement algorithm affected these tests?) -- but this problem is not related to the patch at hand, and is outstanding in the original version as well. By the way, that's a very pretty graph :).


---

Comment by mvngu created at 2009-03-19 01:53:17

After applying the patch *trac_5438.patch*, both of the following commands

```
plot(sin(x), xmin=-2*pi, xmax=2*pi, fill="0.5")
```

and

```
plot(sin(x), xmin=-2*pi, xmax=2*pi, fill=0.5)
```

produce the same looking plot. Notice that in the first command, the value for the fill option is the string `"0.5"`. In the second command, the value for the fill option is the number `0.5`. So for the fill option, if its value is a number given as a string, then the string is parsed for its numeric value. Is that intended?


---

Comment by kcrisman created at 2009-03-19 12:37:56

Replying to [comment:4 mvngu]:
> produce the same looking plot. Notice that in the first command, the value for the fill option is the string `"0.5"`. In the second command, the value for the fill option is the number `0.5`. So for the fill option, if its value is a number given as a string, then the string is parsed for its numeric value. Is that intended?

Hmm, I would say that the answer is yes, because I didn't change that part of the code:

```
sage: from sage.ext.fast_eval import fast_float, fast_float_constant, is_fast_float
sage: fill=3
sage: hasattr(fill,'__call__')
False
sage: float(fill)
3.0
sage: fill='3'
sage: hasattr(fill,'__call__')
False
sage: float(fill)
3.0
```

So since that string can be coerced to a float, apparently the original author intended this behavior (even if implicitly).  Which certainly seems reasonable to me; it's not clear that it should throw an exception, and I can't think of another reasonable legitimate interpretation.


---

Comment by wcauchois created at 2009-03-19 21:11:49

Replying to [comment:4 mvngu]:

My guess is there's a call to float(), intended to coerce numeric types, which inadvertently parses strings. Its common to do less extensive argument checking in a typeless language like Python, however, since the alternative would be infeasible. I doubt that the author intended this behavior, but it is relatively harmless.


---

Comment by mabshoff created at 2009-03-25 08:04:46

This doctest failure needs to be addressed:

```
sage -t -long devel/sage/sage/plot/plot.py
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py", line 3037:
    sage: [len(generate_plot_points(f, (-pi, pi), adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
Expected:
    [42, 67, 104]
Got:
    [36, 65, 91]
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py", line 3040:
    sage: [len(generate_plot_points(f, (-pi, pi), adaptive_recursion=i)) for i in [5, 10, 15]]
Expected:
    [34, 144, 897]
Got:
    [33, 131, 900]
**********************************************************************
```

It is also unclear to me if the changes here do not degrade the default plot settings since the now the adaptive plotting seems to generate fewer points.

Bill: Do not give positive reviews to any patch that causes doctest failures.

Cheers,

Michael


---

Comment by wcauchois created at 2009-03-25 15:02:57

Replying to [comment:7 mabshoff]:
> This doctest failure needs to be addressed:
> {{{
> sage -t -long devel/sage/sage/plot/plot.py
> **********************************************************************
> File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py", line 3037:
>     sage: [len(generate_plot_points(f, (-pi, pi), adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
> Expected:
>     [42, 67, 104]
> Got:
>     [36, 65, 91]
> **********************************************************************
> File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py", line 3040:
>     sage: [len(generate_plot_points(f, (-pi, pi), adaptive_recursion=i)) for i in [5, 10, 15]]
> Expected:
>     [34, 144, 897]
> Got:
>     [33, 131, 900]
> **********************************************************************
> }}}
> It is also unclear to me if the changes here do not degrade the default plot settings since the now the adaptive plotting seems to generate fewer points.
> 
> Bill: Do not give positive reviews to any patch that causes doctest failures.
> 
> Cheers,
> 
> Michael

For some reason, I thought the bug in question was evident in the main branch as well, meaning it would have had nothing to do with this patch. I see now that this is not the case; I must have got branches confused. Thanks for catching my mistake :).

kcrisman: Might this bug have something to do with line 3037?


---

Comment by kcrisman created at 2009-03-25 16:04:37

Certainly line 3037 must be the issue.   This was done to be consistent with another place where a delta occurs, which after all had the correct _mathematical_ version of delta (since the number of plot points is actually n+1 for the usual definition of n in Riemann sums etc.).  I am sorry I didn't catch this earlier, but my computer consistently times out testing both calculus.py and plot.py, so I literally cannot catch these types of failed tests en masse.  I should have tried them by hand, though.

Anyway, I don't think it necessarily downgrades the adaptive plotting significantly.  Note that for i=15 in the second example it actually increases the plot_points by 3!  When I run the old code, incidentally, I get

```
sage: [len(generate_plot_points(f, (-pi, pi), adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[35, 51, 112]
```

which is better for some, worse for others.  Also note that this shows the test is _random_ so this should have been caught earlier, unless current_randstate().python_random().random is set earlier?  I'll set randomize=False for the test.

But really, this is all because of a missed typo on my part.  The original refactoring changed the default plot_points to 5 from 200 just for the sake of generate_plot_points, even though the plot_points from _plot is always passed to this in an actual plotting situation, with default remaining 200.  So I will have to go back in and clarify that anyway, in addition to fixing the doctest.  Yes, there will be a smaller number of points, but I think the randomness makes a big enough swing that it is better to be mathematically accurate and consistent.  E.g.:

Old:

```
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[689, 1145, 1978]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[707, 1138, 2004]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[704, 1137, 2020]
```

New:

```
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[704, 1091, 1949]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[679, 1148, 2015]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[704, 1121, 1981]
```

Old: 

```
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[697, 3235, 18312]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[693, 3357, 17117]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[700, 3815, 25313]
```

New:

```
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[691, 3054, 41501]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[692, 4039, 18385]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[708, 3125, 31209]
```

These differences seem negligible to me, given the wide variation in the randomness.  I'll try to get a new patch up soon clarifying all these things.


---

Comment by kcrisman created at 2009-03-29 02:53:59

Based on 3.4


---

Attachment

This has added doctest, clarified yet more stuff, changed f to f(x) in anticipation of the Pynac switch (since the doctests would happen outside of plotting), and also fixed one weird but inconsequential bug in the slope field plot (sqrt was imported twice, but only the second one counted - which was good, because symbolic is what you want there).  Hope this satisfies all concerns.


---

Comment by wcauchois created at 2009-03-31 18:47:58

REFEREE REPORT:

These changes seem to address the problems. Looks good to me -- all doctests passed. Positive review.


---

Comment by mabshoff created at 2009-04-01 01:36:15

This patch has rejects when attempting to merge it into my 3.4.1.rc0 merge tree:

```
sage-3.4.1.rc0/devel/sage$ patch -p1 --dry-run < trac_5438.patch 
patching file sage/plot/plot.py
Hunk #6 succeeded at 2688 (offset 9 lines).
Hunk #7 succeeded at 2908 (offset 9 lines).
Hunk #8 FAILED at 2931.
Hunk #9 succeeded at 2945 (offset 9 lines).
Hunk #10 succeeded at 2977 (offset 9 lines).
Hunk #11 succeeded at 2987 (offset 9 lines).
Hunk #12 FAILED at 3031.
Hunk #13 succeeded at 3061 (offset 9 lines).
Hunk #14 succeeded at 3082 (offset 9 lines).
Hunk #15 succeeded at 3101 (offset 9 lines).
2 out of 15 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
patching file sage/plot/plot_field.py
```

Once it is rebase the positive review can be restored provided it does pass doctests.

Cheers,

Michael


---

Comment by kcrisman created at 2009-04-28 01:15:52

Turns out somebody got to changing f to f(x) ahead of me, else all is same.


---

Comment by kcrisman created at 2009-04-28 01:16:22

Based on 3.4.2.alpha0


---

Attachment

Ok, if someone does inspect a couple of the plots before and after I am happy to merge this given that the number of points before and after is close enough.

Cheers,

Michael


---

Comment by wcauchois created at 2009-05-06 05:12:24

The plots look fine. This patch applies to Sage 3.4.2 and passes its doctests. Positive review.


---

Comment by mabshoff created at 2009-05-14 06:49:24

Resolution: fixed


---

Comment by mabshoff created at 2009-05-14 06:49:24

Merged trac_5438-rebase.patch  in Sage 4.0.alpha0.

Cheers,

Michael
