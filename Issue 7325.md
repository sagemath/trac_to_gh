# Issue 7325: Sage cannot solve inequalities

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2009-10-27 21:47:53

Assignee: tbd

CC:  mhansen

Keywords: relation, symbolics, inequality, solve

There is no interface to solvers of inequalities available in Maxima.


---

Attachment


---

Comment by robert.marik created at 2009-10-27 21:51:14

The patch is a simple interface to two Maxima solvers. 

For one inequality we use solve_rat_ineq from Maxima and for one or more inequalities written as list we use fourier_elim from Maxima.


---

Comment by robert.marik created at 2009-10-27 21:51:14

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-10-28 00:59:55

Please note that #7155 also was about this - always check if a ticket already exists.  I have closed this.

Does this depend (for instance, for parsing 1#0) on any other tickets?  It is usually best if one builds on other Sage capacity, current or forthcoming.

REVIEW:
The basic idea behind this ticket is good.  There is a new global solve_ineq (which could eventually be called from solve if it detects inequalities?), and two different inequality solvers for the univariate and multivariate cases.  So in general, this is on the right track.

However, the implementation of the univariate solve is nearly all in one gigantic Maxima/Lisp command, as far as I can tell, and that makes it incredibly hard to read for the typical Sage/Python programmer.  It is not clear why the various options are there, nor what they do, because of this.  At the very least, the one gigantic command should be separated into smaller pieces, with comments, so that any future person can figure them out.

The output style makes sense, but many more examples would be welcome.  Is it possible that some of the stuff in the first example could be made easier using a little bit of Maxima parsing (e.g., sage.calculus.calculus.from_string_to_symbolic or whatever)?

Also, there are some nonstandard things.  *opts should probably be made more explicit - what are the options or keywords, exactly, that are expected?  All the line breaks make the code harder, not easier to read; Pythonic indentation should be used.  There are also some typos or slightly ungrammatical English (which is fine for a first patch, but a reviewer should eventually check), and the documentation is not in the normal markup format (see other examples, including in the same file, for prototypes, including blank lines and the :: stuff, or see the Sage developer's [guide](http://www.sagemath.org/doc/developer/)).  

All that said, assuming it works (which I trust it does, but am not currently checking since I can't understand the code), this will be a valuable addition to Sage, particularly since it has a framework that will allow addition of other inequality solving options - such as the upcoming improved to_poly_solve of Maxima, or one or more of the various linear programming solvers now included in Sage per default.


---

Comment by kcrisman created at 2009-10-28 00:59:55

Changing status from needs_review to needs_work.


---

Comment by robert.marik created at 2009-10-30 12:27:46

Many thanks for valuable comments. I am still newbie in this and I'll try to improve patch according to your suggestions. 

It was intended as nothing more than interface to commands available in Maxima. 

Btw: This one huge lisp command comes also from Maxima -- it is nothing more than a fix for the bug [SF 2882408](http://sourceforge.net/tracker/?func=detail&aid=2882408&group_id=4933&atid=104933) and should be removed after fixing this Maxima bug. Hence only few lines remain, like in other interfaces to Maxima commands.


---

Comment by robert.marik created at 2009-11-09 23:09:29

New patch. Before applying this patch, you are strongly recomended to update the file 
local/share/maxima/5.19.1/share/contrib/solve_rat_ineq.mac to [fixed version](http://maxima.cvs.sourceforge.net/viewvc/*checkout*/maxima/maxima/share/contrib/solve_rat_ineq.mac?revision=1.8).

The package does not parse maxima's output involwing 'not equal', like x#0. Perhaps trac #1163 or another trac resolve this problem later.


---

Comment by robert.marik created at 2009-11-09 23:09:29

Changing status from needs_work to needs_review.


---

Comment by robert.marik created at 2009-11-09 23:10:20

apply only this patch


---

Attachment

apply only this patch


---

Comment by kcrisman created at 2009-11-10 03:04:48

Changing status from needs_review to needs_work.


---

Attachment

#1163 has now been updated to parse not equal, at least hopefully; ideally, this patch would be able to use that - or one could open a new ticket.  

As for the current patch, it is a vast improvement on the previous one for readability.  There are still a few formatting things - for INPUT and OUTPUT I think only : is needed, not ::, for instance.  For solve_ineq_univar and solve_ineq_fourier, the output should probably be formatted as a list, like the input is.  The input in solve_ineq (one could say, "an inequality or list of inequalities" or something like that) should not make it look like one can put in ineq twice.

Perhaps this should come with a new Maxima spkg?  It does not pass tests upon being applied to 4.2.1.alpha0, and this is a prerequisite for inclusion of a patch.  However, probably this only requires a change to the spkg by applying the patch mentioned above - in fact, the current Maxima has a (now unnecessary, as it happens) patch on it too, and so probably one can follow that example for how to get them to apply that way (rather than packaging up a whole new one).  See the [Sage developers' guide](http://www.sagemath.org/doc/developer/), especially the part about [new spkgs](http://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg-file).


---

Comment by robert.marik created at 2009-11-11 13:49:25

Changing status from needs_work to needs_review.


---

Comment by robert.marik created at 2009-11-11 13:49:25

The updated spkg package for Maxima is at [http://user.mendelu.cz/marik/sage/maxima-5.19.1.p1.spkg](http://user.mendelu.cz/marik/sage/maxima-5.19.1.p1.spkg).
Install this new spkg to make examples introduced in patch work (they are choosen to ensure that the file solve_rat_ineq.mac has been fixed).

The updated patch is trac-7325-inequalities-3.patch

Apply only this patch


---

Attachment

Apply only thisd patch and update maxima spkg (the link is in discussion, message from November 11 2009)


---

Comment by kcrisman created at 2009-11-17 19:56:27

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-11-17 19:56:27

Positive review!  Apparently a couple things changed in terms of the Maxima (for the better) on this spkg, so I rearranged the doctests to indicate this, and I added a few doctests at the top of the file, copied from below, so it is easy to see on the reference guide.  Otherwise, nice!   

To release manager: apply only 'final' patch.


---

Attachment

Based on 4.2.1, apply only this patch and the spkg.


---

Comment by mvngu created at 2009-12-03 01:49:54

An updated Maxima spkg is available at

http://sage.math.washington.edu/home/mhansen/maxima-5.19.1.p2.spkg

A related ticket is #7287.


---

Comment by mvngu created at 2009-12-03 01:52:16

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2009-12-03 01:52:16

With the new Maxima spkg and the patch `trac_7325-final.patch`, I got these failures:

```
[mvngu`@`sage sage-4.3.alpha0-maxima]$ ./sage -t -long devel/sage-main/sage/symbolic/relation.py 
sage -t -long "devel/sage-main/sage/symbolic/relation.py"   
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py", line 152:
    sage: solve_ineq([log(x)>log(y)])
Expected:
    [y < x, 0 < y]
Got:
    [0 < y, y < x, 0 < x]
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py", line 909:
    sage: solve_ineq_fourier([x+y<9,x-y>4])
Expected:
    [y + 4 < x, x < -y + 9, y < (5/2)]
Got:
    [y < min(x - 4, -x + 9)]
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py", line 918:
    sage: solve_ineq_fourier([log(x)>log(y)])
Expected:
    [y < x, 0 < y]
Got:
    [0 < y, y < x, 0 < x]
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/devel/sage-main/sage/symbolic/relation.py", line 999:
    sage: solve_ineq([x+y<9,x-y>3])
Expected:
    [y + 3 < x, x < -y + 9, y < 3]
Got:
    [y < min(x - 3, -x + 9)]
**********************************************************************
3 items had failures:
   1 of 117 in __main__.example_0
   2 of   8 in __main__.example_7
   1 of   8 in __main__.example_8
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_relation.py
         [6.9 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-main/sage/symbolic/relation.py"
```



---

Comment by kcrisman created at 2009-12-03 02:52:05

This is weird.  Can you check this on a couple different platforms?  The -final patch was changed precisely because the Maxima results had changed for me, so maybe there is something different going on here.

Also, what ticket does the Maxima upgrade belong to, if any?


---

Comment by kcrisman created at 2009-12-03 03:05:13

Replying to [comment:10 kcrisman]:
> This is weird.  Can you check this on a couple different platforms?  The -final patch was changed precisely because the Maxima results had changed for me, so maybe there is something different going on here.
> 
> Also, what ticket does the Maxima upgrade belong to, if any?

Sorry, this question was answered on another ticket - I see, it has the ECL and this change in it.  Great!  Incidentally, Maxima should have another point release soon, which means we would get a fair number of new fixes that way as well.


---

Comment by robert.marik created at 2009-12-04 21:36:22

Replying to [comment:9 mvngu]:
> With the new Maxima spkg and the patch `trac_7325-final.patch`, I got these failures:

This follows probably from updated version of fourier elimination in Maxima. The answers are correct and equivalent to previous answers. I think that it is sufficient to fix the tests and to fix the following message from solve command

```
NotImplementedError: solving only implemented for equalities
```


I'll update the patches after testing on 4.3.rc1

what about to replace output of 

```
solve_ineq(x^2>-1)
```

from 

```
'all'
```

to 

```
x>-Infinity
```

?


---

Attachment

apply after trac_7325-final.patch


---

Comment by robert.marik created at 2009-12-05 21:49:12

Changing status from needs_work to needs_review.


---

Comment by robert.marik created at 2009-12-09 21:58:15

btw: with sage 4.3. you need not to install new Maxima spkg, install only final and final-2 patches. Tested on rc1.


---

Comment by kcrisman created at 2009-12-21 02:11:47

Does this all work well with the new Maxima (see [http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7](http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7) as well?  Sorry for not having time to review this carefully yet.


---

Comment by robert.marik created at 2009-12-21 06:12:55

Replying to [comment:15 kcrisman]:
> Does this all work well with the new Maxima (see [http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7](http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7) as well?  

Not tested on Maxima 5.20.1 - this version is not available in Sage and ticket #7745 is not closed yet.


---

Attachment

Merged two final patches and rebased for Sage 4.3. Apply only this patch.


---

Attachment

Merged both final patches and rebased for Sage 4.3.


---

Comment by robert.marik created at 2009-12-27 18:11:52

I had some problems with trac server and by accident inserted the patch two times. Both are identical, apply only trac_7325_rebased_4.3.patch . Thanks.


---

Comment by robert.marik created at 2009-12-27 18:44:35

Works well also with Maxima 5.20.1. (However, the patch #7745 does not install cleanly with tha patch for this ticket and some parts have to be fixed manualy.)


---

Comment by kcrisman created at 2010-01-08 16:13:46

I will hopefully soon have time to actually test this - thanks for your patience!  Here are a few things to keep in mind for when you rebase to 4.3.1.alpha1 (as #7745 is now merged).

0. Rebase, of course :)

1. I think I agree that x>-Infinity is much more "Sage-like", or maybe `[x>-Infinity]` would be more in keeping with the other solutions.   Good thought.  Or maybe `[x>-Infinity, x<Infinity]` ?  I'm not sure about that.

2. Probably ```special cases``` shouldn't be in the quoting environment.  In fact, [] and the above are both lists, so you would just need to clarify what they mean.

3. Something similar should happen with multivariate.  Here, there is also a small inconsistency involved - `[0 < y, y < x, 0 < x]` for multivariate, but `[This is the Trac macro *0 < y, y < x, 0 < x* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0 < y, y < x, 0 < x-macro)` seems to be the univariate result type.  

4. In calculus/calculus.py, there is the following code:

```
maxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(to_poly_solver)', 'load(simplify_sum)'],
                script_subdirectory=None)
```

Maybe the initialization of solve_rat_ineq and fourier_elim should be there?   Otherwise we are trying to load this with every attempt at a solve_ineq, which seems inefficient.

5. Looking at things, I wonder if it would be possible (without too many bugs) to actually implement ineq.solve(), not just solve(ineq) - that is, in relation.py and expression.py, rather than having solve() gag on inequalities, have it at least try the solve_ineq and just catch any exceptions that are raised and instead raise a NotImplementedError for that particular inequality.  I wonder?

But as before, a great addition to Sage - just trying to get the maximum benefit from this ticket!  Thanks again.


---

Comment by kcrisman created at 2010-01-08 16:13:46

Changing status from needs_review to needs_work.


---

Comment by robert.marik created at 2010-01-08 21:01:07

Replying to [comment:19 kcrisman]:
> 
> 4. In calculus/calculus.py, there is the following code:
> {{{
> maxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(to_poly_solver)', 'load(simplify_sum)'],
>                 script_subdirectory=None)
> }}}
> Maybe the initialization of solve_rat_ineq and fourier_elim should be there?   Otherwise we are trying to load this with every attempt at a solve_ineq, which seems inefficient.

I think that it is inefficient to load a bundle of packages whenever Maxima starts. This makes computations provided by Maxima slower. Perhaps we could use some variable swhich stores information, whether solvers of inequality have been used or no. 


And thanks for the other comments.


---

Comment by mhansen created at 2010-01-08 21:13:32

Replying to [comment:20 robert.marik]:
> I think that it is inefficient to load a bundle of packages whenever Maxima starts. This makes computations provided by Maxima slower. Perhaps we could use some variable swhich stores information, whether solvers of inequality have been used or no. 

Could you explain how loading these packages makes Maxima's computations slower?  I'm not sure I follow.


---

Comment by kcrisman created at 2010-01-08 21:15:29

> > 4. In calculus/calculus.py, there is the following code:
> > {{{
> > maxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(to_poly_solver)', 'load(simplify_sum)'],
> >                 script_subdirectory=None)
> > }}}
> > Maybe the initialization of solve_rat_ineq and fourier_elim should be there?   Otherwise we are trying to load this with every attempt at a solve_ineq, which seems inefficient.
> 
> I think that it is inefficient to load a bundle of packages whenever Maxima starts. This makes computations provided by Maxima slower. Perhaps we could use some variable swhich stores information, whether solvers of inequality have been used or no. 
> 

If you think that is a good way of doing it, then we should also do this for the loading of simplify_sum and to_poly_solve, because certainly they would be in the same boat.  Does checking a boolean sound appropriate?  If you do that here, then I would be happy to do it in the other places.

To mhansen: I think robert.marik is referring to the making it a slightly slower startup, not the actual computations.  It's true that loading tons of packages would eventually slow that down if someone just wanted to get an integral.


---

Comment by robert.marik created at 2010-01-22 15:18:25

Rebased and improved, apply only this patch, added support for (x^2-1>0).solve(x)


---

Comment by robert.marik created at 2010-01-22 15:29:57

Changing status from needs_work to needs_review.


---

Attachment

The last patch solves (I hope) the problems from above.

I found a Maxima bug when solving x^4+2>0 - the problem is from Maxima (and not related to this ticket) and should be easy to fix. Reported at Maxima forum, will be reported on SF with a solution how to fix (in few days or weeks).


---

Comment by robert.marik created at 2010-01-22 20:51:10

Just for the record: the problem related to inequality

```
sage:(x^4+2>0).solve(x)
[This is the Trac macro *x > -* that was inherited from the migration called with arguments (-1)^)](https://trac.sagemath.org/wiki/WikiMacros#x > --macro)
```

is caused by a known [bug](http://sourceforge.net/tracker/?func=detail&aid=2786017&group_id=4933&atid=104933) in algsys and should be fixed [soon](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29593).


---

Comment by kcrisman created at 2010-01-23 01:43:36

Robert,

Overall this is really good now.  One possible thing is what the best way to implement the checking for whether things are already loaded - I have no idea whether this is more efficient than before or not, truthfully, I probably should have brought it up.  The other is that usually one imports maxima from sage.calculus.calculus and then one doesn't have to always check the parents.  But since this is new code and not slowing down old code, that can wait - it's really time we have this.

I am still waiting for 4.3.1 to make check on my dev machine, but once it does I will try this out once again and add a tiny reviewer patch - there is a one-character typo, for instance.  Thanks for all your hard work on this!

Replying to [comment:24 robert.marik]:
> Just for the record: the problem related to inequality
> {{{
> sage:(x^4+2>0).solve(x)
> [This is the Trac macro *x > -* that was inherited from the migration called with arguments (-1)<sup>)](https://trac.sagemath.org/wiki/WikiMacros#x > --macro)
> }}}
> is caused by a known [bug](http://sourceforge.net/tracker/?func=detail&aid=2786017&group_id=4933&atid=104933) in algsys and should be fixed [soon](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29593).
Can you open a ticket for this and put it as "Reported upstream, " etc.?  Even though it's not a Sage bug, we might as well track it - I don't see the need to upgrade Maxima every time they fix a minor bug that affects Sage, but if there is a ticket for it then when there are enough such tickets that are resolved upstream we will see the need to upgrade.


---

Comment by kcrisman created at 2010-01-23 03:13:32

Hmm, weird in line 5932 (the log(x) log(y) solving inequality) I get a doctest error, where instead of three conditions, I get the (simpler) equivalent two conditions 0<y, y<x or whatever.  If I instead add the condition [y,x], I get the result in the doctest, while [x,y] gives the result that is documented for [x,y].  The same happens on the one with the min in the same doctests.  Could the reason be the same as you mentioned above (changes in the fourier_elim, yet again), or perhaps truly a platform issue (I am on Macintel)?

Aargh, it was so close!  But I am sure this can be easily resolved.  I do like the way you dealt with the "or" things, by the way.  It would be nice to wrap that for understanding general Maxima results (like from to_poly_solve), obviously not in this ticket.


---

Comment by kcrisman created at 2010-01-23 03:13:32

Changing status from needs_review to needs_work.


---

Comment by robert.marik created at 2010-01-26 12:39:13

Changing status from needs_work to needs_review.


---

Comment by robert.marik created at 2010-01-26 12:39:13

I do not know why doctests failed. Perhaps some nonstandard settings in my .maxima file. Anyway, I replaced the doctests with simpler ones.

There is one related bug which has been fixed in Maxima CVS: #8078


---

Comment by kcrisman created at 2010-01-26 13:30:05

Replying to [comment:27 robert.marik]:
> I do not know why doctests failed. Perhaps some nonstandard settings in my .maxima file. Anyway, I replaced the doctests with simpler ones.
No, we should document behavior like this so that people aren't confused; until it's 100% clear why it's happening, we shouldn't cover it up.  If I get some time, I will try to track it down using sage.math and my own box; you have clearly done enough work on this patch to deserve a break :)

> There is one related bug which has been fixed in Maxima CVS: #8078
Yes, thanks for reporting that one.


---

Comment by burcin created at 2010-01-26 15:54:12

There seems to be something wrong with attachment:trac_7325_2_rebased_for_4.3.1.patch. It contains two similar patches, with distinct headers etc. I didn't check if they are identical copies of the same patch.


---

Comment by robert.marik created at 2010-01-26 18:16:07

Changing status from needs_review to needs_work.


---

Comment by robert.marik created at 2010-01-26 18:16:07

oops, i was not aware of the fact that if I use hg_sage.export() and the file exists, the output is attached to the end of the file. I will check everything and prepare new patch.


---

Comment by robert.marik created at 2010-01-26 18:54:05

apply only this patch


---

Attachment

Replying to [comment:29 burcin]:
> There seems to be something wrong with attachment:trac_7325_2_rebased_for_4.3.1.patch. It contains two similar patches, with distinct headers etc. I didn't check if they are identical copies of the same patch.

Fixed, thanks. Robert


---

Comment by robert.marik created at 2010-01-26 18:55:29

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-01-29 20:14:54

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-01-29 20:14:54

There were some additional examples which still were platform-dependent.  This is really weird, I have to say!    In particular, the following

```
                try:
                    return(solve_ineq(self)) # trying solve_ineq_univar
                except:
                    pass
                try:
                    return(solve_ineq([self])) # trying solve_ineq_fourier
```

means that exp.solve(x) ignores the x.  However, I don't know that that is really worth changing since it still gives correct answers.

This patch should do it, hopefully it applies to alpha0.  The only changes were in doctests to ensure it passes, and to explain what is going on.  Perhaps it is in Maxima itself that this platform-dependence happens, but I don't have time to check this.

Also corrected two minor typos.


---

Comment by kcrisman created at 2010-01-29 20:16:33

Based on 4.3.1


---

Attachment

And as always, "apply only this patch".  :)


---

Comment by robert.marik created at 2010-01-29 20:46:09

Replying to [comment:32 kcrisman]:
> There were some additional examples which still were platform-dependent.  This is really weird, I have to say!    In particular, the following
> {{{
>                 try:
>                     return(solve_ineq(self)) # trying solve_ineq_univar
>                 except:
>                     pass
>                 try:
>                     return(solve_ineq([self])) # trying solve_ineq_fourier
> }}}
> means that exp.solve(x) ignores the x.  However, I don't know that that is really worth changing since it still gives correct answers.

Perhaps to explain in more details what happens for ineq.solve(x):

* ineq has not equality sign, the previous version of solve command raised error, the new version excutes the code above

* we try solve_ineq(self), i.e. we use the Maxima's solve_rat_ineq. This raises error if there are more than one variable and if the solve_rat_ineq is not polynomial or quotient of two polynomial (after moving right hand side to the left and simplifying). Hence this function does not need the name of the variable on input. this is because solve_rat_ineq handles rational inequalities better than fourier_elim


---

Comment by kcrisman created at 2010-01-30 02:28:50

Replying to [comment:34 robert.marik]:
> Replying to [comment:32 kcrisman]:
> > There were some additional examples which still were platform-dependent.  This is really weird, I have to say!    In particular, the following
> > {{{
> >                 try:
> >                     return(solve_ineq(self)) # trying solve_ineq_univar
> >                 except:
> >                     pass
> >                 try:
> >                     return(solve_ineq([self])) # trying solve_ineq_fourier
> > }}}
> > means that exp.solve(x) ignores the x.  However, I don't know that that is really worth changing since it still gives correct answers.
> 
> Perhaps to explain in more details what happens for ineq.solve(x):
> 
> * ineq has not equality sign, the previous version of solve command raised error, the new version excutes the code above

Oh, yes, I understand, I am just suggesting that in the future solve itself (not just solve_ineq) could take the variable given into account as well.

> 
> * we try solve_ineq(self), i.e. we use the Maxima's solve_rat_ineq. This raises error if there are more than one variable and if the solve_rat_ineq is not polynomial or quotient of two polynomial (after moving right hand side to the left and simplifying). Hence this function does not need the name of the variable on input. this is because solve_rat_ineq handles rational inequalities better than fourier_elim
> 

Yes, of course.  Again, just suggesting that in the future (because the variable order matters for some reason) that the variables could fit in here in the future.  It's still great work!

Incidentally, on Linux:

```
sage: set((x,y))
set([y, x])
```

On Mac:

```
sage: set((x,y))
set([x, y])
```

So that is why we are seeing these changes.  Probably something other than set could solve this issue, so I may open a new ticket for that.


---

Comment by mvngu created at 2010-01-30 23:39:14

Merged only [trac_7325-final-for-real.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7325/trac_7325-final-for-real.patch).


---

Comment by mvngu created at 2010-01-30 23:39:14

Resolution: fixed
