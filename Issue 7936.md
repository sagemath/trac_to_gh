# Issue 7936: Calculus constructions mix explicit calls to maxima

archive/issues_007936.json:
```json
{
    "body": "Assignee: mvngu\n\nSee http://www.sagemath.org.nyud.net/doc/constructions/calculus.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/7936\n\n",
    "created_at": "2010-01-15T17:35:41Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "Calculus constructions mix explicit calls to maxima",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7936",
    "user": "robertwb"
}
```
Assignee: mvngu

See http://www.sagemath.org.nyud.net/doc/constructions/calculus.html

Issue created by migration from https://trac.sagemath.org/ticket/7936





---

archive/issue_comments_069173.json:
```json
{
    "body": "From an email `[sage-support] error in documentation \"Construction\"` on 2010-01-15:\n\n\n```\nHi everyone,\n\nI just checked out one of  first page in the \"Constructions\" page:\n\nhttp://www.sagemath.org.nyud.net/doc/constructions/calculus.html\n\nJust after the first example \"Differentiation\"\n\nsage: var('x k w')\n(x, k, w)\nsage: f = x^3 * e^(k*x) * sin(w*x); f\nx^3*e^(k*x)*sin(w*x)\nsage: f.diff(x)\nk*x^3*e^(k*x)*sin(w*x) + w*x^3*e^(k*x)*cos(w*x) + 3*x^2*e^(k*x)*sin\n(w*x)\nsage: latex(f.diff(x))\nk x^{3} e^{\\left(k x\\right)} \\sin\\left(w x\\right) + w x^{3} e^{\\left(k\nx\\right)} \\cos\\left(w x\\right) + 3 \\, x^{2} e^{\\left(k x\\right)} \\sin\n\\left(w x\\right)\n\nthere is\n\n\"If you type view(f.diff('x')) another... \"\n\nWhen I do that, I get a long error message, which could frighten off\n(it is the first example...). With \"view(f.diff(x))\" it works.\nHowever, if the function is defined via\n\nf = maxima(....)\n\nthen both ways work:   view(f.diff('x')),  view(f.diff(x))\n\nI don't know if this is intended, but at least on the website it\nshould be changed, not to get the error.\n\nGreets,\nStefan\n```\n",
    "created_at": "2010-01-15T23:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69173",
    "user": "wdj"
}
```

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

archive/issue_comments_069174.json:
```json
{
    "body": "Attachment\n\napply to sage-main; based on Sage 4.3.1.alpha2",
    "created_at": "2010-01-16T05:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69174",
    "user": "mvngu"
}
```

Attachment

apply to sage-main; based on Sage 4.3.1.alpha2



---

archive/issue_comments_069175.json:
```json
{
    "body": "apply to examples/ repository; based on Sage 4.3.1.alpha2",
    "created_at": "2010-01-16T05:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69175",
    "user": "mvngu"
}
```

apply to examples/ repository; based on Sage 4.3.1.alpha2



---

archive/issue_comments_069176.json:
```json
{
    "body": "Attachment\n\nHere are two patches, which should fix errors in the calculus chapter of the Constructions document. Apply the patch `trac_7936-constructions.patch` to the repository `sage-main`. The second patch applies to the `examples/` directory, which is separate from `sage-main`. But before applying the second patch, the release manager needs to remove a junk file:\n\n```\n[mvngu@boxen examples]$ pwd\n/dev/shm/mvngu/sage-4.3.1.alpha2-7936-maxima/examples\n[mvngu@boxen examples]$ hg st\n? .hgtags.orig\n[mvngu@boxen examples]$ rm .hgtags.orig \n[mvngu@boxen examples]$ hg st\n```\n",
    "created_at": "2010-01-16T05:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69176",
    "user": "mvngu"
}
```

Attachment

Here are two patches, which should fix errors in the calculus chapter of the Constructions document. Apply the patch `trac_7936-constructions.patch` to the repository `sage-main`. The second patch applies to the `examples/` directory, which is separate from `sage-main`. But before applying the second patch, the release manager needs to remove a junk file:

```
[mvngu@boxen examples]$ pwd
/dev/shm/mvngu/sage-4.3.1.alpha2-7936-maxima/examples
[mvngu@boxen examples]$ hg st
? .hgtags.orig
[mvngu@boxen examples]$ rm .hgtags.orig 
[mvngu@boxen examples]$ hg st
```




---

archive/issue_comments_069177.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T05:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69177",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069178.json:
```json
{
    "body": "It would be really nice if that whole constructions page could be written without any explicit calls to maxima at all--not sure how much of that is possible, but for derivatives, integrals, and power series it certainly is. \n\nAlso, nearly every example involves Piecewise, which doesn't play nicely with all the symbolic stuff (nor does it make for concise examples).",
    "created_at": "2010-01-16T09:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69178",
    "user": "robertwb"
}
```

It would be really nice if that whole constructions page could be written without any explicit calls to maxima at all--not sure how much of that is possible, but for derivatives, integrals, and power series it certainly is. 

Also, nearly every example involves Piecewise, which doesn't play nicely with all the symbolic stuff (nor does it make for concise examples).



---

archive/issue_comments_069179.json:
```json
{
    "body": "The constructions document is quasi-deprecated in any case, as it dates from over two years ago, I believe.  wdj wanted to make a new 'cookbook' document which replaced it, but no one has had time to do so.  Of course, if the whole constructions document were updated, that would be great!  I agree that if one is serious about that, though, one would have to remove Piecewise stuff, as at the time that was one of the better-implemented function types but now is waiting on someone to add them to Pynac.",
    "created_at": "2010-01-18T16:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69179",
    "user": "kcrisman"
}
```

The constructions document is quasi-deprecated in any case, as it dates from over two years ago, I believe.  wdj wanted to make a new 'cookbook' document which replaced it, but no one has had time to do so.  Of course, if the whole constructions document were updated, that would be great!  I agree that if one is serious about that, though, one would have to remove Piecewise stuff, as at the time that was one of the better-implemented function types but now is waiting on someone to add them to Pynac.



---

archive/issue_comments_069180.json:
```json
{
    "body": "> The constructions document is quasi-deprecated in any case, as it dates from over two years ago,\n\nTwo years?   It from at least *four* years ago!  It was mostly written around the time of Sage 1.0, or earlier.  It needs a total rewrite.  When it was written, explicit calls to maxima were the only way to do any calculus.",
    "created_at": "2010-01-18T22:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69180",
    "user": "was"
}
```

> The constructions document is quasi-deprecated in any case, as it dates from over two years ago,

Two years?   It from at least *four* years ago!  It was mostly written around the time of Sage 1.0, or earlier.  It needs a total rewrite.  When it was written, explicit calls to maxima were the only way to do any calculus.



---

archive/issue_comments_069181.json:
```json
{
    "body": "Replying to [comment:5 was]:\n> > The constructions document is quasi-deprecated in any case, as it dates from over two years ago,\n> \n> Two years?   It from at least *four* years ago!  It was mostly written around the time of Sage 1.0, or earlier.  It needs a total rewrite.  When it was written, explicit calls to maxima were the only way to do any calculus. \n\nLike I said, *over* two years ago :)",
    "created_at": "2010-01-19T13:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69181",
    "user": "kcrisman"
}
```

Replying to [comment:5 was]:
> > The constructions document is quasi-deprecated in any case, as it dates from over two years ago,
> 
> Two years?   It from at least *four* years ago!  It was mostly written around the time of Sage 1.0, or earlier.  It needs a total rewrite.  When it was written, explicit calls to maxima were the only way to do any calculus. 

Like I said, *over* two years ago :)



---

archive/issue_comments_069182.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-19T13:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69182",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069183.json:
```json
{
    "body": "Is this fixed by #8132?",
    "created_at": "2010-02-02T05:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69183",
    "user": "mvngu"
}
```

Is this fixed by #8132?



---

archive/issue_comments_069184.json:
```json
{
    "body": "Replying to [comment:7 mvngu]:\n> Is this fixed by #8132?\n\nNo, unfortunately, I don't think so.\n\nI give a positive review to the first patch. I don't understand the second patch. I'm giving the first a positive review though. Fell free to reverse my vote back to needs review, but I'm marking it for now as needs info. The instructions for patch 2 are just completely unclear to me.",
    "created_at": "2010-02-03T00:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69184",
    "user": "wdj"
}
```

Replying to [comment:7 mvngu]:
> Is this fixed by #8132?

No, unfortunately, I don't think so.

I give a positive review to the first patch. I don't understand the second patch. I'm giving the first a positive review though. Fell free to reverse my vote back to needs review, but I'm marking it for now as needs info. The instructions for patch 2 are just completely unclear to me.



---

archive/issue_comments_069185.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-02-03T00:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69185",
    "user": "wdj"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_069186.json:
```json
{
    "body": "Replying to [comment:8 wdj]:\n> I give a positive review to the first patch. \n\nI think the attachment [trac_7936-constructions.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-constructions.patch) is now superseded by #8132. No need to use that patch anymore.\n\n\n\n\n\n> I don't understand the second patch. The instructions for patch 2 are just completely unclear to me.\n\nWithout the attachment [trac_7936-desolvers.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-desolvers.patch) applied to the repository `examples/calculus`, I get an error when loading the file `desolvers.sage`:\n\n```\n[mvngu@mod calculus]$ pwd\n/dev/shm/mvngu/sage-4.3.2.alpha1-sage.math/examples/calculus\n[mvngu@mod calculus]$ ls\ndesolvers.py    eulers_method.sage  newton_raphson.sage\ndesolvers.sage  field_plot2d.sage   README.txt\n[mvngu@mod calculus]$ ../../sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: load \"desolvers.sage\"\n------------------------------------------------------------\n   File \"<string>\", line 147\n     #maxima.eval(cmd)\n                     ^\nSyntaxError: invalid syntax\n```\n\nNow apply the patch [trac_7936-desolvers.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-desolvers.patch) to the repository `examples/calculus` to resolve this syntax error:\n\n```\n[mvngu@mod calculus]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7936/trac_7936-desolvers.patch && hg qpush\nadding trac_7936-desolvers.patch to series file\napplying trac_7936-desolvers.patch\nnow at: trac_7936-desolvers.patch\n[mvngu@mod calculus]$ ../../sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: load \"desolvers.sage\"\nsage: des=[\"'diff(x(t),t)=-4*y(t)\",\"'diff(y(t),t)=-x(t)\"]\nsage: vars = [\"t\",\"x\",\"y\"]\nsage: desolve_system(des,vars)\n[x(t)=(2*y(0)+x(0))*%e^-(2*t)/2-(2*y(0)-x(0))*%e^(2*t)/2,y(t)=(2*y(0)-x(0))*%e^(2*t)/4+(2*y(0)+x(0))*%e^-(2*t)/4]\n```\n",
    "created_at": "2010-02-03T00:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69186",
    "user": "mvngu"
}
```

Replying to [comment:8 wdj]:
> I give a positive review to the first patch. 

I think the attachment [trac_7936-constructions.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-constructions.patch) is now superseded by #8132. No need to use that patch anymore.





> I don't understand the second patch. The instructions for patch 2 are just completely unclear to me.

Without the attachment [trac_7936-desolvers.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-desolvers.patch) applied to the repository `examples/calculus`, I get an error when loading the file `desolvers.sage`:

```
[mvngu@mod calculus]$ pwd
/dev/shm/mvngu/sage-4.3.2.alpha1-sage.math/examples/calculus
[mvngu@mod calculus]$ ls
desolvers.py    eulers_method.sage  newton_raphson.sage
desolvers.sage  field_plot2d.sage   README.txt
[mvngu@mod calculus]$ ../../sage
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
[mvngu@mod calculus]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7936/trac_7936-desolvers.patch && hg qpush
adding trac_7936-desolvers.patch to series file
applying trac_7936-desolvers.patch
now at: trac_7936-desolvers.patch
[mvngu@mod calculus]$ ../../sage
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

archive/issue_comments_069187.json:
```json
{
    "body": "Thanks for explaining that about the second patch.\n\ndesolvers.sage can be removed now since Robert Marik has kindly implemented everything in it in sage already.\n\nCan you just delete the file, Minh?",
    "created_at": "2010-02-03T02:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69187",
    "user": "wdj"
}
```

Thanks for explaining that about the second patch.

desolvers.sage can be removed now since Robert Marik has kindly implemented everything in it in sage already.

Can you just delete the file, Minh?



---

archive/issue_comments_069188.json:
```json
{
    "body": "Replying to [comment:10 wdj]:\n> Thanks for explaining that about the second patch.\n> \n> desolvers.sage can be removed now since Robert Marik has kindly implemented everything in it in sage already.\n> \n> Can you just delete the file, Minh?\n\nI just want to point out also that William is probably going to get rid of the examples directory in the near future - as usual, I do not have the URL for that discussion :) so the sooner we explicitly know it's not necessary, the better.",
    "created_at": "2010-02-03T03:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69188",
    "user": "kcrisman"
}
```

Replying to [comment:10 wdj]:
> Thanks for explaining that about the second patch.
> 
> desolvers.sage can be removed now since Robert Marik has kindly implemented everything in it in sage already.
> 
> Can you just delete the file, Minh?

I just want to point out also that William is probably going to get rid of the examples directory in the near future - as usual, I do not have the URL for that discussion :) so the sooner we explicitly know it's not necessary, the better.



---

archive/issue_comments_069189.json:
```json
{
    "body": "I can verify that desolvers.sage and euler_method.sage from this directory are completely taken care of by the changes of Robert, and some of field_plot2d.sage is also now in the plot/plot_field.py file (maybe not all of it, but maybe not all is needed?).  I think the stuff in newton_raphson.sage probably should be jettisoned or somehow put in one of the sage/calculus files.  \n\nwdj, what do you think?   Probably we can just about delete that whole directory.  What do you think is worth putting into the main Sage library?",
    "created_at": "2010-04-20T13:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69189",
    "user": "kcrisman"
}
```

I can verify that desolvers.sage and euler_method.sage from this directory are completely taken care of by the changes of Robert, and some of field_plot2d.sage is also now in the plot/plot_field.py file (maybe not all of it, but maybe not all is needed?).  I think the stuff in newton_raphson.sage probably should be jettisoned or somehow put in one of the sage/calculus files.  

wdj, what do you think?   Probably we can just about delete that whole directory.  What do you think is worth putting into the main Sage library?



---

archive/issue_comments_069190.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> I can verify that desolvers.sage and euler_method.sage from this directory are completely taken care of by the changes of Robert, and some of field_plot2d.sage is also now in the plot/plot_field.py file (maybe not all of it, but maybe not all is needed?).  I think the stuff in newton_raphson.sage probably should be jettisoned or somehow put in one of the sage/calculus files.  \n> \n> wdj, what do you think?   Probably we can just about delete that whole directory.  What do you think is worth putting into the main Sage library?\n\n\nAgreed. delete it. newton_raphson is so simple, it is easy to just post to the wiki or something anyway. Thanks for looking at this!",
    "created_at": "2010-04-20T14:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69190",
    "user": "wdj"
}
```

Replying to [comment:12 kcrisman]:
> I can verify that desolvers.sage and euler_method.sage from this directory are completely taken care of by the changes of Robert, and some of field_plot2d.sage is also now in the plot/plot_field.py file (maybe not all of it, but maybe not all is needed?).  I think the stuff in newton_raphson.sage probably should be jettisoned or somehow put in one of the sage/calculus files.  
> 
> wdj, what do you think?   Probably we can just about delete that whole directory.  What do you think is worth putting into the main Sage library?


Agreed. delete it. newton_raphson is so simple, it is easy to just post to the wiki or something anyway. Thanks for looking at this!



---

archive/issue_comments_069191.json:
```json
{
    "body": "Okay, this patch, applied to the examples/ repository, should take of this.  Needs review.  wdj, why don't you go ahead and look at the newton-raphson examples on the interact part of the Wiki and see if that essentially has that, otherwise can you think of an appropriate place to store it?  \n\nAlso see #7494 on removing all of this examples/ directory.",
    "created_at": "2010-04-28T02:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69191",
    "user": "kcrisman"
}
```

Okay, this patch, applied to the examples/ repository, should take of this.  Needs review.  wdj, why don't you go ahead and look at the newton-raphson examples on the interact part of the Wiki and see if that essentially has that, otherwise can you think of an appropriate place to store it?  

Also see #7494 on removing all of this examples/ directory.



---

archive/issue_comments_069192.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-04-28T02:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69192",
    "user": "kcrisman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_069193.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-28T02:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69193",
    "user": "kcrisman"
}
```

Attachment



---

archive/issue_comments_069194.json:
```json
{
    "body": "Do I only need to apply [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch)?",
    "created_at": "2010-05-08T22:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69194",
    "user": "mvngu"
}
```

Do I only need to apply [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch)?



---

archive/issue_comments_069195.json:
```json
{
    "body": "Replying to [comment:15 mvngu]:\n> Do I only need to apply [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch)?\nI think so.   Someone should check the interact wiki and make sure that the essence of the Newton-Raphson example is captured in the interacts already there which are about that.  Recall that this needs review, though, so you (or someone) would need to formally give this positive review at least.",
    "created_at": "2010-05-09T00:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69195",
    "user": "kcrisman"
}
```

Replying to [comment:15 mvngu]:
> Do I only need to apply [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch)?
I think so.   Someone should check the interact wiki and make sure that the essence of the Newton-Raphson example is captured in the interacts already there which are about that.  Recall that this needs review, though, so you (or someone) would need to formally give this positive review at least.



---

archive/issue_comments_069196.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> Okay, this patch, applied to the examples/ repository, should take of this.  Needs review.  \n> wdj, why don't you go ahead and look at the newton-raphson examples on the interact \n> part of the Wiki and see if that essentially has that, otherwise can you think of an appropriate place to store it?  \n\n\nLooks good to me. I also copied the file to \nhttp://boxen.math.washington.edu/home/wdj/sagefiles/\n\n\n> \n> Also see #7494 on removing all of this examples/ directory.",
    "created_at": "2010-05-11T14:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69196",
    "user": "wdj"
}
```

Replying to [comment:14 kcrisman]:
> Okay, this patch, applied to the examples/ repository, should take of this.  Needs review.  
> wdj, why don't you go ahead and look at the newton-raphson examples on the interact 
> part of the Wiki and see if that essentially has that, otherwise can you think of an appropriate place to store it?  


Looks good to me. I also copied the file to 
http://boxen.math.washington.edu/home/wdj/sagefiles/


> 
> Also see #7494 on removing all of this examples/ directory.



---

archive/issue_comments_069197.json:
```json
{
    "body": "Replying to [comment:16 kcrisman]:\n> Replying to [comment:15 mvngu]:\n> > Do I only need to apply [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch)?\n> I think so.   Someone should check the interact wiki and make sure that the essence of the \n> Newton-Raphson example is captured in the interacts already there which are about that.  Recall \n> that this needs review, though, so you (or someone) would need to formally give this positive review at least.  \n\nThis patch does not apply to 4.4.2.a0 for me. Does anyone else have this problem?",
    "created_at": "2010-05-11T14:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69197",
    "user": "wdj"
}
```

Replying to [comment:16 kcrisman]:
> Replying to [comment:15 mvngu]:
> > Do I only need to apply [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch)?
> I think so.   Someone should check the interact wiki and make sure that the essence of the 
> Newton-Raphson example is captured in the interacts already there which are about that.  Recall 
> that this needs review, though, so you (or someone) would need to formally give this positive review at least.  

This patch does not apply to 4.4.2.a0 for me. Does anyone else have this problem?



---

archive/issue_comments_069198.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-05-11T14:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69198",
    "user": "wdj"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_069199.json:
```json
{
    "body": "You have to apply it \"manually\" (using ./sage -hg, unfortunately) to the examples/ directory.  There is no hg_examples :(",
    "created_at": "2010-05-11T15:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69199",
    "user": "kcrisman"
}
```

You have to apply it "manually" (using ./sage -hg, unfortunately) to the examples/ directory.  There is no hg_examples :(



---

archive/issue_comments_069200.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-05-11T15:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69200",
    "user": "kcrisman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_069201.json:
```json
{
    "body": "Replying to [comment:19 kcrisman]:\n> You have to apply it \"manually\" (using ./sage -hg, unfortunately) to the examples/ directory.  There is no hg_examples :(\n\nCan you tell me exactly the command to use to apply the patch Please?\n\nsage -hg ????",
    "created_at": "2010-05-11T15:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69201",
    "user": "wdj"
}
```

Replying to [comment:19 kcrisman]:
> You have to apply it "manually" (using ./sage -hg, unfortunately) to the examples/ directory.  There is no hg_examples :(

Can you tell me exactly the command to use to apply the patch Please?

sage -hg ????



---

archive/issue_comments_069202.json:
```json
{
    "body": "I'll use ... to indicate the rest of the path until the Sage folder.\n\n```\ncd .../sage-4.4.1/examples/\n~/.../sage-4.4.1/sage -hg log | less  # gives you the log, which is very boring :)\n~/.../sage-4.4.1/sage -hg import http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7936/trac_7936-no-calc-examples.patch\n~/.../sage-4.4.1/sage -hg log | less  # gives you the log, which should now indicate the patch was applied.\n```\n\nAnd if you go in ./sage/examples/calculus/ now, it should be empty.  The release manager would have to remove the empty folder by hand, I think.\n\nI agree that it is very annoying that one has to do this without hg_sage - it took me a long time to figure out how to do it - but eventually the examples directory will cease to exist and so that won't be a problem.  This is just a first step.",
    "created_at": "2010-05-11T16:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69202",
    "user": "kcrisman"
}
```

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

archive/issue_comments_069203.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-11T19:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69203",
    "user": "wdj"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069204.json:
```json
{
    "body": "Replying to [comment:21 kcrisman]:\n> I'll use ... to indicate the rest of the path until the Sage folder.\n> {{{\n> cd .../sage-4.4.1/examples/\n> ~/.../sage-4.4.1/sage -hg log | less  # gives you the log, which is very boring :)\n> ~/.../sage-4.4.1/sage -hg import http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7936/trac_7936-no-calc-examples.patch\n> ~/.../sage-4.4.1/sage -hg log | less  # gives you the log, which should now indicate the patch was applied.\n> }}}\n> And if you go in ./sage/examples/calculus/ now, it should be empty.  The release manager would have to remove the empty folder by hand, I think.\n> \n> I agree that it is very annoying that one has to do this without hg_sage - it took me a long time to figure out how to do it - but eventually the examples directory will cease to exist and so that won't be a problem.  This is just a first step.\n\n\nThanks very much! \n\nThis applies fine to 4.4.2.a0 and sage -testall passes (except for unrelated failures in interfaces/r.py and misc/sagedoc.py).",
    "created_at": "2010-05-11T19:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69204",
    "user": "wdj"
}
```

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

archive/issue_comments_069205.json:
```json
{
    "body": "Merged [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch) in examples repository.",
    "created_at": "2010-05-12T22:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69205",
    "user": "mvngu"
}
```

Merged [trac_7936-no-calc-examples.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7936/trac_7936-no-calc-examples.patch) in examples repository.



---

archive/issue_comments_069206.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-12T22:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7936#issuecomment-69206",
    "user": "mvngu"
}
```

Resolution: fixed
