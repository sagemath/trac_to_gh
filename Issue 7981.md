# Issue 7981: animate ignores options to show that are passed up from the plot command

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-01-18 18:39:50

Assignee: was

CC:  wcauchois

This animate command shouldn't ignore the options to show() that are passed through by the plot command (here the options are ymin and ymax):


```
sage: var('t')
sage: damped_oscillator = 41/311*sqrt(311)*e^(-3/8*t)*sin(1/8*sqrt(311)*t) + 3*e^(-3/8*t)*cos(1/8*sqrt(311)*t)
sage: animate([plot( lambda x: damped_oscillator( t = x + k ), -1/2, 3*pi, ymin=-2, ymax=3.5 ) for k in srange( 0, pi, 0.3 ) ]).show()
```


Thanks to   	
Johann Myrkraverk Oskarsson for reporting this.


---

Attachment


---

Comment by jason created at 2010-01-19 00:15:40

Changing status from new to needs_review.


---

Comment by jason created at 2010-01-19 00:16:54

Bill and Karl-Dieter,

You two might be interested in this.  Karl-Dieter, you wrote the original code that passed show options around, I believe.  I just made the consolidation happen in .save() instead of .show().


---

Comment by jason created at 2010-01-19 05:27:34

This fixes #7524.


---

Comment by kcrisman created at 2010-01-19 18:53:20

Umm... I find that unlikely, though I may have broken something inadvertently.


---

Comment by timdumol created at 2010-01-20 13:51:42

Doctesting on plot.py results in 2 errors:

{{[
sage -t  "devel/sage-ref/sage/plot/plot.py"                 
 --leak-resolution=high --log-socket=127.0.0.1 --leak-check=full --num-callers=25 --suppressions=/opt/sage-4.3.rc0.O0/local/lib/valgrind/sage.supp 
**********************************************************************                                                                             
File "/home/timdumol/sage-4.3.1.alpha0/devel/sage-ref/sage/plot/plot.py", line 1925:                                                               
    sage: c.show(figsize=[5,5], xmin=-1, xmax=3, ymin=-1, ymax=3)                   sage: point((-1,1),pointsize=30, color='red')                  
Exception raised:                                                                                                                                  
    Traceback (most recent call last):                                                                                                             
      File "/home/timdumol/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test                                                  
        self.run_one_example(test, example, filename, compileflags)                                                                                
      File "/home/timdumol/sage-4.3.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example                                                
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                                                             
      File "/home/timdumol/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example                                               
        compileflags, 1) in test.globs                                                                                                             
      File "<doctest __main__.example_37[5]>", line 1                                                                                              
         c.show(figsize=[Integer(5),Integer(5)], xmin=-Integer(1), xmax=Integer(3), ymin=-Integer(1), ymax=Integer(3))                   sage: point((-Integer(1),Integer(1)),pointsize=Integer(30), color='red')###line 1925:                                                                                                                  
    sage: c.show(figsize=[5,5], xmin=-1, xmax=3, ymin=-1, ymax=3)                   sage: point((-1,1),pointsize=30, color='red')                                       
                                                                                                                                           ^                            
     SyntaxError: invalid syntax                                                                                                                                        
**********************************************************************
File "/home/timdumol/sage-4.3.1.alpha0/devel/sage-ref/sage/plot/plot.py", line 1930:
    sage: c.save(DOCTEST_MODE_FILE)
Exception raised:
    Traceback (most recent call last):
      File "/home/timdumol/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/timdumol/sage-4.3.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/timdumol/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_37[7]>", line 1, in <module>
        c.save(DOCTEST_MODE_FILE)###line 1930:
    sage: c.save(DOCTEST_MODE_FILE)
    NameError: name 'DOCTEST_MODE_FILE' is not defined
**********************************************************************
1 items had failures:
   2 of   8 in __main__.example_37
}}}


---

Comment by timdumol created at 2010-01-20 13:51:42

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-11-10 16:16:56

Here is another effect of this, I think:


```
plot(x,(x,0,1),aspect_ratio=1).save('test.png')
```

does not save a graph with aspect ratio 1.


---

Comment by novoselt created at 2010-11-19 03:54:18

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-11-19 03:54:18

I have just wrote a patch fixing the issue for `save` (which is quite annoying in conjunction with SageTeX) and then found this ticket. Since the original patch does not apply cleanly on sage-4.6.alpha1, I posted my patch, but I have incorporated Jason's changes to `show` to eliminate double processing of options.

I have changed call parameters to `save` since it is not documented why one would ever need `savenow=False`. If I want to save later, shouldn't I call `save` later?-) Also it does not make sense in my opinion to use any extra positional arguments in this function except for the file name. I realize that this is a backward-incompatible change, but all long tests pass with this patch.


---

Comment by novoselt created at 2010-11-26 16:43:02

Made it possible to apply the new patch after #10291 (which is now positively reviewed).


---

Comment by novoselt created at 2010-12-05 18:37:10

For the buildbot

Apply trac-7981-save_ignores_preset_plotting_options.patch


---

Comment by novoselt created at 2010-12-05 18:37:10

Changing assignee from was to novoselt.


---

Comment by mhampton created at 2011-01-12 01:09:54

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2011-01-12 01:09:54

This seems to work, and all doctests in the module plot (not just the file) pass.

Sadly it didn't also fix #10244, so I will try to figure that out if I can.

Positive review.


---

Comment by kcrisman created at 2011-01-12 20:43:33

Just out of curiosity, what is the 'backward-incompatible' change you mention?   Which extra positional arguments - like dpi?  (Though Jason also got rid of that - I wonder why?)  

I guess I mean to ask whether this is a good such change; usually there is a deprecation period.  After all, doctests catch very few of our use cases :)  What is wrong with the usual `*args,**kwds` syntax? 

As for `savenow`, it looks like with it being `False` we could still create a Sage object.  You are right that it seems a little redundant, though!

Also, this needs a doctest (it's in the original patch) to show that animate options actually work, at least in theory (if one looked at it and ran the optional tests).  So... needs work.  Sorry :(


---

Comment by kcrisman created at 2011-01-12 20:43:33

Changing status from positive_review to needs_work.


---

Comment by novoselt created at 2011-01-13 03:17:30

Replying to [comment:13 kcrisman]:
> Just out of curiosity, what is the 'backward-incompatible' change you mention?   Which extra positional arguments - like dpi?  (Though Jason also got rid of that - I wonder why?)  

I don't remember exactly what I meant, but probably it was changing parameters of `save`.

> I guess I mean to ask whether this is a good such change; usually there is a deprecation period.  After all, doctests catch very few of our use cases :)  What is wrong with the usual `*args,**kwds` syntax? 

I think that it makes the syntax of save cleaner and easier to understand (and document for that matter). As was recently mentioned on sage-devel, one should use common sense when deciding whether to deprecate something or change immediately, I think that these changes fall into the latter category ;-) As for `*args` I just think that it is a bad practice to call functions with 20 or so possible parameters listing them without names.

> As for `savenow`, it looks like with it being `False` we could still create a Sage object.  You are right that it seems a little redundant, though!

Isn't it a bug that `save` saves something in some cases when `savenow=False`?..

> Also, this needs a doctest (it's in the original patch) to show that animate options actually work, at least in theory (if one looked at it and ran the optional tests).  So... needs work.  Sorry :(

I added the doctest. Was it the only reason for "needs work" or you would like to have `save` parameters changed as well?


---

Comment by novoselt created at 2011-01-13 03:17:30

Changing status from needs_work to needs_review.


---

Attachment

Alternative patch


---

Comment by novoselt created at 2011-01-13 03:19:33

For the confused buildbot:

Apply trac-7981-save_ignores_preset_plotting_options.patch


---

Comment by kcrisman created at 2011-01-13 03:30:23

Replying to [comment:14 novoselt]:
> Replying to [comment:13 kcrisman]:
> I think that it makes the syntax of save cleaner and easier to understand (and document for that matter). As was recently mentioned on sage-devel, one should use common sense when deciding whether to deprecate something or change immediately, I think that these changes fall into the latter category ;-) 
Yeah, these two make sense.  It looks like dpi will still work, given `SHOW_OPTIONS`.  

>As for `*args` I just think that it is a bad practice to call functions with 20 or so possible parameters listing them without names.
Okay, I see what's going on here now.  Especially since the order would be open to suspicion!

> > As for `savenow`, it looks like with it being `False` we could still create a Sage object.  You are right that it seems a little redundant, though!
> 
> Isn't it a bug that `save` saves something in some cases when `savenow=False`?..

No, just an undocumented feature!  Since it doesn't save a _graphic_.  I agree this seems odd, though, so not complaining.

> > Also, this needs a doctest (it's in the original patch) to show that animate options actually work, at least in theory (if one looked at it and ran the optional tests).  So... needs work.  Sorry :(
> 
> I added the doctest. Was it the only reason for "needs work" or you would like to have `save` parameters changed as well?

No, assuming this still applies by the buildbot, and since you've explained the parameter issue fine, that's okay.  The only reason I felt justified in overruling the original positive review was because it didn't actually include the doctest, though I had the other questions as well.


---

Comment by kcrisman created at 2011-01-13 03:30:23

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-01-14 02:18:49

There is a trivial error in this patch that however causes it to fail doctests.

```
We check that Trac #7981 is fixed:: 

    sage: animate([plot(sin(x + float(k), (0, 2*pi), ymin=-5, ymax=5)) 
    ...            for k in srange(0,2*pi,0.3)]).show() # optional
```

Notice that there is a parenthesis missing after `float(k)` which instead comes after `ymax=5`.  Patch coming up.


---

Comment by kcrisman created at 2011-01-14 02:28:02

Okay, now for sure positive review.  

To buildbot - apply trac-7981-save_ignores_preset_plotting_options.patch and trac_7981-reviewer.patch.


---

Comment by kcrisman created at 2011-01-15 03:21:00

Just FYI - still applies fine on 4.6.2.alpha0.


---

Comment by kcrisman created at 2011-01-17 18:40:07

reviewer patch


---

Attachment

Just an update - apparently 

```
sage: animate([plot(sin(x + float(k)), (0, 2*pi), ymin=-5, ymax=5)
...            for k in srange(0,2*pi,0.3)]).show() # optional
```

does not obey the optional test, for it created a new file (I must have ImageMagick!).  We don't create non-temp new files in doctests, though, so this had to be changed.  New reviewer patch fixes this as well, maintains positive review.  Should not affect the plot patches which depend on this.


---

Comment by jdemeyer created at 2011-01-17 20:44:21

Maybe you should document in the file what you just said in your comment.  Also make it clear why the test is tagged optional.


---

Comment by jdemeyer created at 2011-01-17 20:44:21

Changing status from positive_review to needs_work.


---

Comment by kcrisman created at 2011-01-17 20:58:53

Hmm, but in many places in this file it says why such things are optional.   In fact, _earlier in the same docstring_ the first occurrence of `.show()` explains this:

```
        sage: a.show()          # optional -- requires convert command
```

as well as several lines later

```
        sage: a.show() # optional -- requires convert command
```

so hopefully one wouldn't need to do it a third time in three paragraphs.  Especially since it's a `TEST`.

Also, the actual issue with creating a file I have posted to sage-devel about; it's not 100% clear to me that this is a bug.  It just happened to have a bad effect here, which I changed from Andrey's patch.  But it's orthogonal to the ticket.

So putting back to 'needs review'.  I hope you will agree with me that this is in fact still worthy of positive review.

Now, of course there is in the doctesting framework the issue that one can do optional tests with only certain keywords, so if one has `convert` one could run them with that keyword.  But in that case, the entire file `animate.py` is replete with violations of this, and I feel that should be a separate ticket.


---

Comment by kcrisman created at 2011-01-17 20:58:53

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-01-18 13:03:26

Replying to [comment:23 kcrisman]:
> Hmm, but in many places in this file it says why such things are optional.   In fact, _earlier in the same docstring_ the first occurrence of `.show()` explains this:
> {{{
>         sage: a.show()          # optional -- requires convert command
> }}}
> as well as several lines later
> {{{
>         sage: a.show() # optional -- requires convert command
> }}}
> so hopefully one wouldn't need to do it a third time in three paragraphs.  Especially since it's a `TEST`.

Personally, I would write it a third time.  On the other hand, I don't care too much.  So if you feel like you're happy with the patch as-is, then that's fine for me.


---

Comment by kcrisman created at 2011-01-18 14:19:26

> > so hopefully one wouldn't need to do it a third time in three paragraphs.  Especially since it's a `TEST`.
> 
> Personally, I would write it a third time.  On the other hand, I don't care too much.  So if you feel like you're happy with the patch as-is, then that's fine for me.

Yes, I am.  This issue is pretty important, and the other issue is somewhat orthogonal.  I've opened another ticket for the issue about the optional keyword - this is now #10655.


---

Comment by kcrisman created at 2011-01-18 14:19:26

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-01-18 14:20:00

'This issue' meaning this ticket itself, of course :-)


---

Comment by jdemeyer created at 2011-01-19 01:35:49

Please specify which patches have to be applied.


---

Comment by jdemeyer created at 2011-01-19 01:35:49

Changing status from positive_review to needs_info.


---

Comment by novoselt created at 2011-01-19 01:45:51

Please apply trac-7981-save_ignores_preset_plotting_options.patch and trac_7981-reviewer.patch


---

Comment by novoselt created at 2011-01-19 01:45:51

Changing status from needs_info to needs_review.


---

Comment by novoselt created at 2011-01-19 01:46:05

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-01-19 02:10:56

Replying to [comment:27 jdemeyer]:
> Please specify which patches have to be applied.
Just FYI, this was already noted in [comment:19 comment 19].


---

Comment by jdemeyer created at 2011-01-25 08:13:57

Resolution: fixed
