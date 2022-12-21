# Issue 7936: Calculus constructions mix explicit calls to maxima

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-01-15 17:35:41

Assignee: mvngu

See http://www.sagemath.org.nyud.net/doc/constructions/calculus.html


---

Comment by wdj created at 2010-01-15 23:16:58

From an email `[sage-support] error in documentation "Construction"` on 2010-01-15:


```
Hi everyone,

I just checked out one of  first page in the "Constructions" page:

http://www.sagemath.org.nyud.net/doc/constructions/calculus.html

Just after the first example "Differentiation"

sage: var('x k w')
(x, k, w)
sage: f = x^3 * e^(k*x) * sin(w*x); f
x^3*e^(k*x)*sin(w*x)
sage: f.diff(x)
k*x^3*e^(k*x)*sin(w*x) + w*x^3*e^(k*x)*cos(w*x) + 3*x^2*e^(k*x)*sin
(w*x)
sage: latex(f.diff(x))
k x^{3} e^{\left(k x\right)} \sin\left(w x\right) + w x^{3} e^{\left(k
x\right)} \cos\left(w x\right) + 3 \, x^{2} e^{\left(k x\right)} \sin
\left(w x\right)

there is

"If you type view(f.diff('x')) another... "

When I do that, I get a long error message, which could frighten off
(it is the first example...). With "view(f.diff(x))" it works.
However, if the function is defined via

f = maxima(....)

then both ways work:   view(f.diff('x')),  view(f.diff(x))

I don't know if this is intended, but at least on the website it
should be changed, not to get the error.

Greets,
Stefan
```



---

Attachment

apply to sage-main; based on Sage 4.3.1.alpha2


---

Comment by mvngu created at 2010-01-16 05:32:08

apply to examples/ repository; based on Sage 4.3.1.alpha2


---

Attachment

Here are two patches, which should fix errors in the calculus chapter of the Constructions document. Apply the patch `trac_7936-constructions.patch` to the repository `sage-main`. The second patch applies to the `examples/` directory, which is separate from `sage-main`. But before applying the second patch, the release manager needs to remove a junk file:

```
[mvngu`@`boxen examples]$ pwd
/dev/shm/mvngu/sage-4.3.1.alpha2-7936-maxima/examples
[mvngu`@`boxen examples]$ hg st
? .hgtags.orig
[mvngu`@`boxen examples]$ rm .hgtags.orig 
[mvngu`@`boxen examples]$ hg st
```



---

Comment by mvngu created at 2010-01-16 05:33:40

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-01-16 09:24:39

It would be really nice if that whole constructions page could be written without any explicit calls to maxima at all--not sure how much of that is possible, but for derivatives, integrals, and power series it certainly is. 

Also, nearly every example involves Piecewise, which doesn't play nicely with all the symbolic stuff (nor does it make for concise examples).


---

Comment by kcrisman created at 2010-01-18 16:02:05

The constructions document is quasi-deprecated in any case, as it dates from over two years ago, I believe.  wdj wanted to make a new 'cookbook' document which replaced it, but no one has had time to do so.  Of course, if the whole constructions document were updated, that would be great!  I agree that if one is serious about that, though, one would have to remove Piecewise stuff, as at the time that was one of the better-implemented function types but now is waiting on someone to add them to Pynac.


---

Comment by was created at 2010-01-18 22:23:36

> The constructions document is quasi-deprecated in any case, as it dates from over two years ago,

Two years?   It from at least *four* years ago!  It was mostly written around the time of Sage 1.0, or earlier.  It needs a total rewrite.  When it was written, explicit calls to maxima were the only way to do any calculus.


---

Comment by kcrisman created at 2010-01-19 13:12:28

Replying to [comment:5 was]:
> > The constructions document is quasi-deprecated in any case, as it dates from over two years ago,
> 
> Two years?   It from at least *four* years ago!  It was mostly written around the time of Sage 1.0, or earlier.  It needs a total rewrite.  When it was written, explicit calls to maxima were the only way to do any calculus. 

Like I said, _over_ two years ago :)


---

Comment by kcrisman created at 2010-01-19 13:12:28

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-02-02 05:38:17

Is this fixed by #8132?


---

Comment by wdj created at 2010-02-03 00:32:45

Replying to [comment:7 mvngu]:
> Is this fixed by #8132?

No, unfortunately, I don't think so.

I give a positive review to the first patch. I don't understand the second patch. I'm giving the first a positive review though. Fell free to reverse my vote back to needs review, but I'm marking it for now as needs info. The instructions for patch 2 are just completely unclear to me.


---

Comment by wdj created at 2010-02-03 00:32:45

Changing status from needs_work to needs_info.


---

Comment by mvngu created at 2010-02-03 00:56:23

Replying to [comment:8 wdj]:
> I give a positive review to the first patch. 

I think the attachment [trac_7936-constructions.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-constructions.patch) is now superseded by #8132. No need to use that patch anymore.





> I don't understand the second patch. The instructions for patch 2 are just completely unclear to me.

Without the attachment [trac_7936-desolvers.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-desolvers.patch) applied to the repository `examples/calculus`, I get an error when loading the file `desolvers.sage`:

```
[mvngu`@`mod calculus]$ pwd
/dev/shm/mvngu/sage-4.3.2.alpha1-sage.math/examples/calculus
[mvngu`@`mod calculus]$ ls
desolvers.py    eulers_method.sage  newton_raphson.sage
desolvers.sage  field_plot2d.sage   README.txt
[mvngu`@`mod calculus]$ ../../sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: load "desolvers.sage"
------------------------------------------------------------
   File "<string>", line 147
     #maxima.eval(cmd)
                     ^
SyntaxError: invalid syntax
```

Now apply the patch [trac_7936-desolvers.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-desolvers.patch) to the repository `examples/calculus` to resolve this syntax error:

```
[mvngu`@`mod calculus]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7936/trac_7936-desolvers.patch && hg qpush
adding trac_7936-desolvers.patch to series file
applying trac_7936-desolvers.patch
now at: trac_7936-desolvers.patch
[mvngu`@`mod calculus]$ ../../sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: load "desolvers.sage"
sage: des=["'diff(x(t),t)=-4*y(t)","'diff(y(t),t)=-x(t)"]
sage: vars = ["t","x","y"]
sage: desolve_system(des,vars)
[x(t)=(2*y(0)+x(0))*%e^-(2*t)/2-(2*y(0)-x(0))*%e^(2*t)/2,y(t)=(2*y(0)-x(0))*%e^(2*t)/4+(2*y(0)+x(0))*%e^-(2*t)/4]
```



---

Comment by wdj created at 2010-02-03 02:10:24

Thanks for explaining that about the second patch.

desolvers.sage can be removed now since Robert Marik has kindly implemented everything in it in sage already.

Can you just delete the file, Minh?


---

Comment by kcrisman created at 2010-02-03 03:36:37

Replying to [comment:10 wdj]:
> Thanks for explaining that about the second patch.
> 
> desolvers.sage can be removed now since Robert Marik has kindly implemented everything in it in sage already.
> 
> Can you just delete the file, Minh?

I just want to point out also that William is probably going to get rid of the examples directory in the near future - as usual, I do not have the URL for that discussion :) so the sooner we explicitly know it's not necessary, the better.


---

Comment by kcrisman created at 2010-04-20 13:46:39

I can verify that desolvers.sage and euler_method.sage from this directory are completely taken care of by the changes of Robert, and some of field_plot2d.sage is also now in the plot/plot_field.py file (maybe not all of it, but maybe not all is needed?).  I think the stuff in newton_raphson.sage probably should be jettisoned or somehow put in one of the sage/calculus files.  

wdj, what do you think?   Probably we can just about delete that whole directory.  What do you think is worth putting into the main Sage library?


---

Comment by wdj created at 2010-04-20 14:04:32

Replying to [comment:12 kcrisman]:
> I can verify that desolvers.sage and euler_method.sage from this directory are completely taken care of by the changes of Robert, and some of field_plot2d.sage is also now in the plot/plot_field.py file (maybe not all of it, but maybe not all is needed?).  I think the stuff in newton_raphson.sage probably should be jettisoned or somehow put in one of the sage/calculus files.  
> 
> wdj, what do you think?   Probably we can just about delete that whole directory.  What do you think is worth putting into the main Sage library?


Agreed. delete it. newton_raphson is so simple, it is easy to just post to the wiki or something anyway. Thanks for looking at this!


---

Comment by kcrisman created at 2010-04-28 02:41:25

Okay, this patch, applied to the examples/ repository, should take of this.  Needs review.  wdj, why don't you go ahead and look at the newton-raphson examples on the interact part of the Wiki and see if that essentially has that, otherwise can you think of an appropriate place to store it?  

Also see #7494 on removing all of this examples/ directory.


---

Comment by kcrisman created at 2010-04-28 02:41:25

Changing status from needs_info to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-05-08 22:52:37

Do I only need to apply [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch)?


---

Comment by kcrisman created at 2010-05-09 00:12:45

Replying to [comment:15 mvngu]:
> Do I only need to apply [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch)?
I think so.   Someone should check the interact wiki and make sure that the essence of the Newton-Raphson example is captured in the interacts already there which are about that.  Recall that this needs review, though, so you (or someone) would need to formally give this positive review at least.


---

Comment by wdj created at 2010-05-11 14:02:14

Replying to [comment:14 kcrisman]:
> Okay, this patch, applied to the examples/ repository, should take of this.  Needs review.  
> wdj, why don't you go ahead and look at the newton-raphson examples on the interact 
> part of the Wiki and see if that essentially has that, otherwise can you think of an appropriate place to store it?  


Looks good to me. I also copied the file to 
http://boxen.math.washington.edu/home/wdj/sagefiles/


> 
> Also see #7494 on removing all of this examples/ directory.


---

Comment by wdj created at 2010-05-11 14:03:38

Replying to [comment:16 kcrisman]:
> Replying to [comment:15 mvngu]:
> > Do I only need to apply [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch)?
> I think so.   Someone should check the interact wiki and make sure that the essence of the 
> Newton-Raphson example is captured in the interacts already there which are about that.  Recall 
> that this needs review, though, so you (or someone) would need to formally give this positive review at least.  

This patch does not apply to 4.4.2.a0 for me. Does anyone else have this problem?


---

Comment by wdj created at 2010-05-11 14:03:38

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2010-05-11 15:23:50

You have to apply it "manually" (using ./sage -hg, unfortunately) to the examples/ directory.  There is no hg_examples :(


---

Comment by kcrisman created at 2010-05-11 15:23:50

Changing status from needs_info to needs_review.


---

Comment by wdj created at 2010-05-11 15:55:23

Replying to [comment:19 kcrisman]:
> You have to apply it "manually" (using ./sage -hg, unfortunately) to the examples/ directory.  There is no hg_examples :(

Can you tell me exactly the command to use to apply the patch Please?

sage -hg ????


---

Comment by kcrisman created at 2010-05-11 16:02:09

I'll use ... to indicate the rest of the path until the Sage folder.

```
cd .../sage-4.4.1/examples/
~/.../sage-4.4.1/sage -hg log | less  # gives you the log, which is very boring :)
~/.../sage-4.4.1/sage -hg import http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7936/trac_7936-no-calc-examples.patch
~/.../sage-4.4.1/sage -hg log | less  # gives you the log, which should now indicate the patch was applied.
```

And if you go in ./sage/examples/calculus/ now, it should be empty.  The release manager would have to remove the empty folder by hand, I think.

I agree that it is very annoying that one has to do this without hg_sage - it took me a long time to figure out how to do it - but eventually the examples directory will cease to exist and so that won't be a problem.  This is just a first step.


---

Comment by wdj created at 2010-05-11 19:55:41

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-05-11 19:55:41

Replying to [comment:21 kcrisman]:
> I'll use ... to indicate the rest of the path until the Sage folder.
> {{{
> cd .../sage-4.4.1/examples/
> ~/.../sage-4.4.1/sage -hg log | less  # gives you the log, which is very boring :)
> ~/.../sage-4.4.1/sage -hg import http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7936/trac_7936-no-calc-examples.patch
> ~/.../sage-4.4.1/sage -hg log | less  # gives you the log, which should now indicate the patch was applied.
> }}}
> And if you go in ./sage/examples/calculus/ now, it should be empty.  The release manager would have to remove the empty folder by hand, I think.
> 
> I agree that it is very annoying that one has to do this without hg_sage - it took me a long time to figure out how to do it - but eventually the examples directory will cease to exist and so that won't be a problem.  This is just a first step.


Thanks very much! 

This applies fine to 4.4.2.a0 and sage -testall passes (except for unrelated failures in interfaces/r.py and misc/sagedoc.py).


---

Comment by mvngu created at 2010-05-12 22:45:33

Merged [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch) in examples repository.


---

Comment by mvngu created at 2010-05-12 22:45:33

Resolution: fixed
