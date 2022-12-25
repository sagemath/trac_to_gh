# Issue 7981: animate ignores options to show that are passed up from the plot command

archive/issues_007981.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  wcauchois\n\nThis animate command shouldn't ignore the options to show() that are passed through by the plot command (here the options are ymin and ymax):\n\n\n```\nsage: var('t')\nsage: damped_oscillator = 41/311*sqrt(311)*e^(-3/8*t)*sin(1/8*sqrt(311)*t) + 3*e^(-3/8*t)*cos(1/8*sqrt(311)*t)\nsage: animate([plot( lambda x: damped_oscillator( t = x + k ), -1/2, 3*pi, ymin=-2, ymax=3.5 ) for k in srange( 0, pi, 0.3 ) ]).show()\n```\n\n\nThanks to   \t\nJohann Myrkraverk Oskarsson for reporting this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7981\n\n",
    "created_at": "2010-01-18T18:39:50Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "animate ignores options to show that are passed up from the plot command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7981",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  wcauchois

This animate command shouldn't ignore the options to show() that are passed through by the plot command (here the options are ymin and ymax):


```
sage: var('t')
sage: damped_oscillator = 41/311*sqrt(311)*e^(-3/8*t)*sin(1/8*sqrt(311)*t) + 3*e^(-3/8*t)*cos(1/8*sqrt(311)*t)
sage: animate([plot( lambda x: damped_oscillator( t = x + k ), -1/2, 3*pi, ymin=-2, ymax=3.5 ) for k in srange( 0, pi, 0.3 ) ]).show()
```


Thanks to   	
Johann Myrkraverk Oskarsson for reporting this.

Issue created by migration from https://trac.sagemath.org/ticket/7981





---

archive/issue_comments_069519.json:
```json
{
    "body": "Attachment [trac-7981-show_options.patch](tarball://root/attachments/some-uuid/ticket7981/trac-7981-show_options.patch) by @jasongrout created at 2010-01-19 00:15:40",
    "created_at": "2010-01-19T00:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69519",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7981-show_options.patch](tarball://root/attachments/some-uuid/ticket7981/trac-7981-show_options.patch) by @jasongrout created at 2010-01-19 00:15:40



---

archive/issue_comments_069520.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T00:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69520",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069521.json:
```json
{
    "body": "Bill and Karl-Dieter,\n\nYou two might be interested in this.  Karl-Dieter, you wrote the original code that passed show options around, I believe.  I just made the consolidation happen in .save() instead of .show().",
    "created_at": "2010-01-19T00:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69521",
    "user": "https://github.com/jasongrout"
}
```

Bill and Karl-Dieter,

You two might be interested in this.  Karl-Dieter, you wrote the original code that passed show options around, I believe.  I just made the consolidation happen in .save() instead of .show().



---

archive/issue_comments_069522.json:
```json
{
    "body": "This fixes #7524.",
    "created_at": "2010-01-19T05:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69522",
    "user": "https://github.com/jasongrout"
}
```

This fixes #7524.



---

archive/issue_comments_069523.json:
```json
{
    "body": "Umm... I find that unlikely, though I may have broken something inadvertently.",
    "created_at": "2010-01-19T18:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69523",
    "user": "https://github.com/kcrisman"
}
```

Umm... I find that unlikely, though I may have broken something inadvertently.



---

archive/issue_comments_069524.json:
```json
{
    "body": "Doctesting on plot.py results in 2 errors:\n\n{{[\nsage -t  \"devel/sage-ref/sage/plot/plot.py\"                 \n --leak-resolution=high --log-socket=127.0.0.1 --leak-check=full --num-callers=25 --suppressions=/opt/sage-4.3.rc0.O0/local/lib/valgrind/sage.supp \n**********************************************************************                                                                             \nFile \"/home/timdumol/sage-4.3.1.alpha0/devel/sage-ref/sage/plot/plot.py\", line 1925:                                                               \n    sage: c.show(figsize=[5,5], xmin=-1, xmax=3, ymin=-1, ymax=3)                   sage: point((-1,1),pointsize=30, color='red')                  \nException raised:                                                                                                                                  \n    Traceback (most recent call last):                                                                                                             \n      File \"/home/timdumol/sage-4.3.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test                                                  \n        self.run_one_example(test, example, filename, compileflags)                                                                                \n      File \"/home/timdumol/sage-4.3.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example                                                \n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                                                             \n      File \"/home/timdumol/sage-4.3.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example                                               \n        compileflags, 1) in test.globs                                                                                                             \n      File \"<doctest __main__.example_37[5]>\", line 1                                                                                              \n         c.show(figsize=[Integer(5),Integer(5)], xmin=-Integer(1), xmax=Integer(3), ymin=-Integer(1), ymax=Integer(3))                   sage: point((-Integer(1),Integer(1)),pointsize=Integer(30), color='red')###line 1925:                                                                                                                  \n    sage: c.show(figsize=[5,5], xmin=-1, xmax=3, ymin=-1, ymax=3)                   sage: point((-1,1),pointsize=30, color='red')                                       \n                                                                                                                                           ^                            \n     SyntaxError: invalid syntax                                                                                                                                        \n**********************************************************************\nFile \"/home/timdumol/sage-4.3.1.alpha0/devel/sage-ref/sage/plot/plot.py\", line 1930:\n    sage: c.save(DOCTEST_MODE_FILE)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/timdumol/sage-4.3.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/timdumol/sage-4.3.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/timdumol/sage-4.3.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_37[7]>\", line 1, in <module>\n        c.save(DOCTEST_MODE_FILE)###line 1930:\n    sage: c.save(DOCTEST_MODE_FILE)\n    NameError: name 'DOCTEST_MODE_FILE' is not defined\n**********************************************************************\n1 items had failures:\n   2 of   8 in __main__.example_37\n}}}",
    "created_at": "2010-01-20T13:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69524",
    "user": "https://github.com/TimDumol"
}
```

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

archive/issue_comments_069525.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T13:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69525",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069526.json:
```json
{
    "body": "Here is another effect of this, I think:\n\n\n```\nplot(x,(x,0,1),aspect_ratio=1).save('test.png')\n```\n\ndoes not save a graph with aspect ratio 1.",
    "created_at": "2010-11-10T16:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69526",
    "user": "https://github.com/jasongrout"
}
```

Here is another effect of this, I think:


```
plot(x,(x,0,1),aspect_ratio=1).save('test.png')
```

does not save a graph with aspect ratio 1.



---

archive/issue_comments_069527.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-19T03:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69527",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069528.json:
```json
{
    "body": "I have just wrote a patch fixing the issue for `save` (which is quite annoying in conjunction with SageTeX) and then found this ticket. Since the original patch does not apply cleanly on sage-4.6.alpha1, I posted my patch, but I have incorporated Jason's changes to `show` to eliminate double processing of options.\n\nI have changed call parameters to `save` since it is not documented why one would ever need `savenow=False`. If I want to save later, shouldn't I call `save` later?-) Also it does not make sense in my opinion to use any extra positional arguments in this function except for the file name. I realize that this is a backward-incompatible change, but all long tests pass with this patch.",
    "created_at": "2010-11-19T03:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69528",
    "user": "https://github.com/novoselt"
}
```

I have just wrote a patch fixing the issue for `save` (which is quite annoying in conjunction with SageTeX) and then found this ticket. Since the original patch does not apply cleanly on sage-4.6.alpha1, I posted my patch, but I have incorporated Jason's changes to `show` to eliminate double processing of options.

I have changed call parameters to `save` since it is not documented why one would ever need `savenow=False`. If I want to save later, shouldn't I call `save` later?-) Also it does not make sense in my opinion to use any extra positional arguments in this function except for the file name. I realize that this is a backward-incompatible change, but all long tests pass with this patch.



---

archive/issue_comments_069529.json:
```json
{
    "body": "Made it possible to apply the new patch after #10291 (which is now positively reviewed).",
    "created_at": "2010-11-26T16:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69529",
    "user": "https://github.com/novoselt"
}
```

Made it possible to apply the new patch after #10291 (which is now positively reviewed).



---

archive/issue_comments_069530.json:
```json
{
    "body": "For the buildbot\n\nApply trac-7981-save_ignores_preset_plotting_options.patch",
    "created_at": "2010-12-05T18:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69530",
    "user": "https://github.com/novoselt"
}
```

For the buildbot

Apply trac-7981-save_ignores_preset_plotting_options.patch



---

archive/issue_comments_069531.json:
```json
{
    "body": "Changing assignee from @williamstein to @novoselt.",
    "created_at": "2010-12-05T18:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69531",
    "user": "https://github.com/novoselt"
}
```

Changing assignee from @williamstein to @novoselt.



---

archive/issue_comments_069532.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-12T01:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69532",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069533.json:
```json
{
    "body": "This seems to work, and all doctests in the module plot (not just the file) pass.\n\nSadly it didn't also fix #10244, so I will try to figure that out if I can.\n\nPositive review.",
    "created_at": "2011-01-12T01:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69533",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This seems to work, and all doctests in the module plot (not just the file) pass.

Sadly it didn't also fix #10244, so I will try to figure that out if I can.

Positive review.



---

archive/issue_comments_069534.json:
```json
{
    "body": "Just out of curiosity, what is the 'backward-incompatible' change you mention?   Which extra positional arguments - like dpi?  (Though Jason also got rid of that - I wonder why?)  \n\nI guess I mean to ask whether this is a good such change; usually there is a deprecation period.  After all, doctests catch very few of our use cases :)  What is wrong with the usual `*args,**kwds` syntax? \n\nAs for `savenow`, it looks like with it being `False` we could still create a Sage object.  You are right that it seems a little redundant, though!\n\nAlso, this needs a doctest (it's in the original patch) to show that animate options actually work, at least in theory (if one looked at it and ran the optional tests).  So... needs work.  Sorry :(",
    "created_at": "2011-01-12T20:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69534",
    "user": "https://github.com/kcrisman"
}
```

Just out of curiosity, what is the 'backward-incompatible' change you mention?   Which extra positional arguments - like dpi?  (Though Jason also got rid of that - I wonder why?)  

I guess I mean to ask whether this is a good such change; usually there is a deprecation period.  After all, doctests catch very few of our use cases :)  What is wrong with the usual `*args,**kwds` syntax? 

As for `savenow`, it looks like with it being `False` we could still create a Sage object.  You are right that it seems a little redundant, though!

Also, this needs a doctest (it's in the original patch) to show that animate options actually work, at least in theory (if one looked at it and ran the optional tests).  So... needs work.  Sorry :(



---

archive/issue_comments_069535.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-12T20:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69535",
    "user": "https://github.com/kcrisman"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_069536.json:
```json
{
    "body": "Replying to [comment:13 kcrisman]:\n> Just out of curiosity, what is the 'backward-incompatible' change you mention?   Which extra positional arguments - like dpi?  (Though Jason also got rid of that - I wonder why?)  \n\nI don't remember exactly what I meant, but probably it was changing parameters of `save`.\n\n> I guess I mean to ask whether this is a good such change; usually there is a deprecation period.  After all, doctests catch very few of our use cases :)  What is wrong with the usual `*args,**kwds` syntax? \n\nI think that it makes the syntax of save cleaner and easier to understand (and document for that matter). As was recently mentioned on sage-devel, one should use common sense when deciding whether to deprecate something or change immediately, I think that these changes fall into the latter category ;-) As for `*args` I just think that it is a bad practice to call functions with 20 or so possible parameters listing them without names.\n\n> As for `savenow`, it looks like with it being `False` we could still create a Sage object.  You are right that it seems a little redundant, though!\n\nIsn't it a bug that `save` saves something in some cases when `savenow=False`?..\n\n> Also, this needs a doctest (it's in the original patch) to show that animate options actually work, at least in theory (if one looked at it and ran the optional tests).  So... needs work.  Sorry :(\n\nI added the doctest. Was it the only reason for \"needs work\" or you would like to have `save` parameters changed as well?",
    "created_at": "2011-01-13T03:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69536",
    "user": "https://github.com/novoselt"
}
```

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

archive/issue_comments_069537.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-13T03:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69537",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069538.json:
```json
{
    "body": "Attachment [trac-7981-save_ignores_preset_plotting_options.patch](tarball://root/attachments/some-uuid/ticket7981/trac-7981-save_ignores_preset_plotting_options.patch) by @novoselt created at 2011-01-13 03:18:03\n\nAlternative patch",
    "created_at": "2011-01-13T03:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69538",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac-7981-save_ignores_preset_plotting_options.patch](tarball://root/attachments/some-uuid/ticket7981/trac-7981-save_ignores_preset_plotting_options.patch) by @novoselt created at 2011-01-13 03:18:03

Alternative patch



---

archive/issue_comments_069539.json:
```json
{
    "body": "For the confused buildbot:\n\nApply trac-7981-save_ignores_preset_plotting_options.patch",
    "created_at": "2011-01-13T03:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69539",
    "user": "https://github.com/novoselt"
}
```

For the confused buildbot:

Apply trac-7981-save_ignores_preset_plotting_options.patch



---

archive/issue_comments_069540.json:
```json
{
    "body": "Replying to [comment:14 novoselt]:\n> Replying to [comment:13 kcrisman]:\n> I think that it makes the syntax of save cleaner and easier to understand (and document for that matter). As was recently mentioned on sage-devel, one should use common sense when deciding whether to deprecate something or change immediately, I think that these changes fall into the latter category ;-) \nYeah, these two make sense.  It looks like dpi will still work, given `SHOW_OPTIONS`.  \n\n>As for `*args` I just think that it is a bad practice to call functions with 20 or so possible parameters listing them without names.\nOkay, I see what's going on here now.  Especially since the order would be open to suspicion!\n\n> > As for `savenow`, it looks like with it being `False` we could still create a Sage object.  You are right that it seems a little redundant, though!\n> \n> Isn't it a bug that `save` saves something in some cases when `savenow=False`?..\n\nNo, just an undocumented feature!  Since it doesn't save a *graphic*.  I agree this seems odd, though, so not complaining.\n\n> > Also, this needs a doctest (it's in the original patch) to show that animate options actually work, at least in theory (if one looked at it and ran the optional tests).  So... needs work.  Sorry :(\n> \n> I added the doctest. Was it the only reason for \"needs work\" or you would like to have `save` parameters changed as well?\n\nNo, assuming this still applies by the buildbot, and since you've explained the parameter issue fine, that's okay.  The only reason I felt justified in overruling the original positive review was because it didn't actually include the doctest, though I had the other questions as well.",
    "created_at": "2011-01-13T03:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69540",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:14 novoselt]:
> Replying to [comment:13 kcrisman]:
> I think that it makes the syntax of save cleaner and easier to understand (and document for that matter). As was recently mentioned on sage-devel, one should use common sense when deciding whether to deprecate something or change immediately, I think that these changes fall into the latter category ;-) 
Yeah, these two make sense.  It looks like dpi will still work, given `SHOW_OPTIONS`.  

>As for `*args` I just think that it is a bad practice to call functions with 20 or so possible parameters listing them without names.
Okay, I see what's going on here now.  Especially since the order would be open to suspicion!

> > As for `savenow`, it looks like with it being `False` we could still create a Sage object.  You are right that it seems a little redundant, though!
> 
> Isn't it a bug that `save` saves something in some cases when `savenow=False`?..

No, just an undocumented feature!  Since it doesn't save a *graphic*.  I agree this seems odd, though, so not complaining.

> > Also, this needs a doctest (it's in the original patch) to show that animate options actually work, at least in theory (if one looked at it and ran the optional tests).  So... needs work.  Sorry :(
> 
> I added the doctest. Was it the only reason for "needs work" or you would like to have `save` parameters changed as well?

No, assuming this still applies by the buildbot, and since you've explained the parameter issue fine, that's okay.  The only reason I felt justified in overruling the original positive review was because it didn't actually include the doctest, though I had the other questions as well.



---

archive/issue_comments_069541.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-13T03:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69541",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019092.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-13T04:59:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7981#event-19092"
}
```



---

archive/issue_comments_069542.json:
```json
{
    "body": "There is a trivial error in this patch that however causes it to fail doctests.\n\n```\nWe check that Trac #7981 is fixed:: \n\n    sage: animate([plot(sin(x + float(k), (0, 2*pi), ymin=-5, ymax=5)) \n    ...            for k in srange(0,2*pi,0.3)]).show() # optional\n```\n\nNotice that there is a parenthesis missing after `float(k)` which instead comes after `ymax=5`.  Patch coming up.",
    "created_at": "2011-01-14T02:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69542",
    "user": "https://github.com/kcrisman"
}
```

There is a trivial error in this patch that however causes it to fail doctests.

```
We check that Trac #7981 is fixed:: 

    sage: animate([plot(sin(x + float(k), (0, 2*pi), ymin=-5, ymax=5)) 
    ...            for k in srange(0,2*pi,0.3)]).show() # optional
```

Notice that there is a parenthesis missing after `float(k)` which instead comes after `ymax=5`.  Patch coming up.



---

archive/issue_comments_069543.json:
```json
{
    "body": "Okay, now for sure positive review.  \n\nTo buildbot - apply trac-7981-save_ignores_preset_plotting_options.patch and trac_7981-reviewer.patch.",
    "created_at": "2011-01-14T02:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69543",
    "user": "https://github.com/kcrisman"
}
```

Okay, now for sure positive review.  

To buildbot - apply trac-7981-save_ignores_preset_plotting_options.patch and trac_7981-reviewer.patch.



---

archive/issue_comments_069544.json:
```json
{
    "body": "Just FYI - still applies fine on 4.6.2.alpha0.",
    "created_at": "2011-01-15T03:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69544",
    "user": "https://github.com/kcrisman"
}
```

Just FYI - still applies fine on 4.6.2.alpha0.



---

archive/issue_comments_069545.json:
```json
{
    "body": "reviewer patch",
    "created_at": "2011-01-17T18:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69545",
    "user": "https://github.com/kcrisman"
}
```

reviewer patch



---

archive/issue_comments_069546.json:
```json
{
    "body": "Attachment [trac_7981-reviewer.patch](tarball://root/attachments/some-uuid/ticket7981/trac_7981-reviewer.patch) by @kcrisman created at 2011-01-17 18:42:01\n\nJust an update - apparently \n\n```\nsage: animate([plot(sin(x + float(k)), (0, 2*pi), ymin=-5, ymax=5)\n...            for k in srange(0,2*pi,0.3)]).show() # optional\n```\n\ndoes not obey the optional test, for it created a new file (I must have ImageMagick!).  We don't create non-temp new files in doctests, though, so this had to be changed.  New reviewer patch fixes this as well, maintains positive review.  Should not affect the plot patches which depend on this.",
    "created_at": "2011-01-17T18:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69546",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_7981-reviewer.patch](tarball://root/attachments/some-uuid/ticket7981/trac_7981-reviewer.patch) by @kcrisman created at 2011-01-17 18:42:01

Just an update - apparently 

```
sage: animate([plot(sin(x + float(k)), (0, 2*pi), ymin=-5, ymax=5)
...            for k in srange(0,2*pi,0.3)]).show() # optional
```

does not obey the optional test, for it created a new file (I must have ImageMagick!).  We don't create non-temp new files in doctests, though, so this had to be changed.  New reviewer patch fixes this as well, maintains positive review.  Should not affect the plot patches which depend on this.



---

archive/issue_comments_069547.json:
```json
{
    "body": "Maybe you should document in the file what you just said in your comment.  Also make it clear why the test is tagged optional.",
    "created_at": "2011-01-17T20:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69547",
    "user": "https://github.com/jdemeyer"
}
```

Maybe you should document in the file what you just said in your comment.  Also make it clear why the test is tagged optional.



---

archive/issue_comments_069548.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-17T20:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69548",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_069549.json:
```json
{
    "body": "Hmm, but in many places in this file it says why such things are optional.   In fact, *earlier in the same docstring* the first occurrence of `.show()` explains this:\n\n```\n        sage: a.show()          # optional -- requires convert command\n```\n\nas well as several lines later\n\n```\n        sage: a.show() # optional -- requires convert command\n```\n\nso hopefully one wouldn't need to do it a third time in three paragraphs.  Especially since it's a `TEST`.\n\nAlso, the actual issue with creating a file I have posted to sage-devel about; it's not 100% clear to me that this is a bug.  It just happened to have a bad effect here, which I changed from Andrey's patch.  But it's orthogonal to the ticket.\n\nSo putting back to 'needs review'.  I hope you will agree with me that this is in fact still worthy of positive review.\n\nNow, of course there is in the doctesting framework the issue that one can do optional tests with only certain keywords, so if one has `convert` one could run them with that keyword.  But in that case, the entire file `animate.py` is replete with violations of this, and I feel that should be a separate ticket.",
    "created_at": "2011-01-17T20:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69549",
    "user": "https://github.com/kcrisman"
}
```

Hmm, but in many places in this file it says why such things are optional.   In fact, *earlier in the same docstring* the first occurrence of `.show()` explains this:

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

archive/issue_comments_069550.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-17T20:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69550",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069551.json:
```json
{
    "body": "Replying to [comment:23 kcrisman]:\n> Hmm, but in many places in this file it says why such things are optional.   In fact, *earlier in the same docstring* the first occurrence of `.show()` explains this:\n> {{{\n>         sage: a.show()          # optional -- requires convert command\n> }}}\n> as well as several lines later\n> {{{\n>         sage: a.show() # optional -- requires convert command\n> }}}\n> so hopefully one wouldn't need to do it a third time in three paragraphs.  Especially since it's a `TEST`.\n\nPersonally, I would write it a third time.  On the other hand, I don't care too much.  So if you feel like you're happy with the patch as-is, then that's fine for me.",
    "created_at": "2011-01-18T13:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69551",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:23 kcrisman]:
> Hmm, but in many places in this file it says why such things are optional.   In fact, *earlier in the same docstring* the first occurrence of `.show()` explains this:
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

archive/issue_comments_069552.json:
```json
{
    "body": "> > so hopefully one wouldn't need to do it a third time in three paragraphs.  Especially since it's a `TEST`.\n> \n> Personally, I would write it a third time.  On the other hand, I don't care too much.  So if you feel like you're happy with the patch as-is, then that's fine for me.\n\nYes, I am.  This issue is pretty important, and the other issue is somewhat orthogonal.  I've opened another ticket for the issue about the optional keyword - this is now #10655.",
    "created_at": "2011-01-18T14:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69552",
    "user": "https://github.com/kcrisman"
}
```

> > so hopefully one wouldn't need to do it a third time in three paragraphs.  Especially since it's a `TEST`.
> 
> Personally, I would write it a third time.  On the other hand, I don't care too much.  So if you feel like you're happy with the patch as-is, then that's fine for me.

Yes, I am.  This issue is pretty important, and the other issue is somewhat orthogonal.  I've opened another ticket for the issue about the optional keyword - this is now #10655.



---

archive/issue_comments_069553.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-18T14:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69553",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069554.json:
```json
{
    "body": "'This issue' meaning this ticket itself, of course :-)",
    "created_at": "2011-01-18T14:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69554",
    "user": "https://github.com/kcrisman"
}
```

'This issue' meaning this ticket itself, of course :-)



---

archive/issue_comments_069555.json:
```json
{
    "body": "Please specify which patches have to be applied.",
    "created_at": "2011-01-19T01:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69555",
    "user": "https://github.com/jdemeyer"
}
```

Please specify which patches have to be applied.



---

archive/issue_comments_069556.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2011-01-19T01:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69556",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_069557.json:
```json
{
    "body": "Please apply trac-7981-save_ignores_preset_plotting_options.patch and trac_7981-reviewer.patch",
    "created_at": "2011-01-19T01:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69557",
    "user": "https://github.com/novoselt"
}
```

Please apply trac-7981-save_ignores_preset_plotting_options.patch and trac_7981-reviewer.patch



---

archive/issue_comments_069558.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-01-19T01:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69558",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_069559.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-19T01:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69559",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069560.json:
```json
{
    "body": "Replying to [comment:27 jdemeyer]:\n> Please specify which patches have to be applied.\nJust FYI, this was already noted in [comment:19 comment 19].",
    "created_at": "2011-01-19T02:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69560",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:27 jdemeyer]:
> Please specify which patches have to be applied.
Just FYI, this was already noted in [comment:19 comment 19].



---

archive/issue_comments_069561.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7981#issuecomment-69561",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_019093.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-25T08:13:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7981",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7981#event-19093"
}
```
