# Issue 6371: implement Riemann theta functions

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-20 18:15:55

Assignee: jkantor

CC:  cswiercz fredrik.johannson mstreng jpflori slelievre

Keywords: riemann theta klein

In the theory of differential equations and abelian varieties, Riemann theta functions and there relatives play an important role.  Implement these in sage!


---

Attachment


---

Comment by ncalexan created at 2009-06-20 18:43:03

I want to make sure this code doesn't get lost.  It's very much [needs work] -- I don't think all tests are tagged `optional` and `long` correctly.  I'm not certain that the output is correct to very high accuracy, either -- magma and mathematica disagree, and maple is too slow to evaluate to high precision.

Fredrik, somewhere in here there are lots of calls to the incomplete gamma function.  I used low precision as much as possible as you will see, because I don't really need high precision, I just need large outputs.

Chris, this applies against 4.0.2.alpha1 at least.  Documentation and testing appreciated!


---

Comment by ncalexan created at 2009-06-20 18:59:57

Marco, you might be interested in this work in progress code too.


---

Comment by fredrik.johansson created at 2009-06-21 18:40:20

Is double precision sufficient? Are the arguments large, integers or half-integers? In either case, very fast evaluation of the incomplete gamma function should be possible.


---

Comment by was created at 2009-06-26 13:23:39

To use this, type

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/6371/trac_6371-riemann-theta.patch')
sage: quit

sage -br

sage: now you have the new code
```



---

Comment by cswiercz created at 2010-12-10 18:02:11

Changing assignee from jkantor to cswiercz.


---

Comment by cswiercz created at 2010-12-10 18:07:08

Over the past month or two I've done considerable work vetting out the bugs and errors in the above code. Within a week or so I hope to post a replacement patch. Hence, the change of owner. I'll keep everyone who's interested posted on my progress.

A word of warning, though: since I know a lot of people who are interested in my getting Riemann theta into Sage as soon as possible I had to strip Shimura phi, Siegel theta, and Klein P. I'm not qualified to review / bug fix that part of the code. I hope this is okay with the original authors and people who are interested in seeing this patch resolved. Perhaps we can move these implementations into a new patch once Riemann theta is implemented.

Again, I'll be posting a replacement patch sometime within the next two weeks or so.


---

Comment by ncalexan created at 2010-12-10 18:18:31

> A word of warning, though: since I know a lot of people who are interested in my getting Riemann theta into Sage as soon as possible I had to strip Shimura phi, Siegel theta, and Klein P. I'm not qualified to review / bug fix that part of the code. I hope this is okay with the original authors and people who are interested in seeing this patch resolved.

I am the original author, and I think this is a very reasonable decision!  You should know that I use "Siegel theta" and "Riemann theta" interchangeably.  Riemann theta often seems to mean just with characteristics (0, 0, ..., 0) and Siegel theta seems to be a Mathematica-ism.  Whatever we decide on is (probably) fine by me.

> Perhaps we can move these implementations into a new patch once Riemann theta is implemented.

These bits are interesting for my research, but probably are not all that interesting more generally.  Cut them for now.

Thanks for you efforts, Chris!


---

Comment by cswiercz created at 2010-12-10 18:31:08

> I am the original author, and I think this is a very reasonable decision!  You should know that I use "Siegel theta" and "Riemann theta" interchangeably.  Riemann theta often seems to mean just with characteristics (0, 0, ..., 0) and Siegel theta seems to be a Mathematica-ism.  Whatever we decide on is (probably) fine by me.
> Thanks for you efforts, Chris!

Huzzah! Thank _you_ for your help!


---

Attachment

Replacement for first patch by ncalexan


---

Comment by cswiercz created at 2011-03-25 00:10:22

Changing status from needs_work to needs_review.


---

Comment by cswiercz created at 2011-03-25 00:10:22

Note that the second patch is meant to replace the first. Many many changes were made!


---

Comment by cswiercz created at 2011-03-28 18:01:31

Changing status from needs_review to needs_work.


---

Comment by cswiercz created at 2011-03-28 18:01:31

Some clarifications and fine tuning needs to be made to the documentation.


---

Comment by cswiercz created at 2011-03-28 18:21:51

Part 2 of the replacement patch. Includes documentation fixes.


---

Attachment


---

Comment by cswiercz created at 2011-03-28 18:22:31

Changing status from needs_work to needs_review.


---

Comment by cswiercz created at 2011-03-28 18:31:52

Minor last-minute bug.


---

Attachment

(for patchbot)

Apply 

 * [attachment:trac_6371-riemann-theta-REPLACEMENT.patch]

 * [attachment:trac_6371-riemann-theta-REPLACEMENT-PART2.patch]

 * [attachment:trac_6371_riemann-theta-REPLACEMENT-PART3.patch]


---

Comment by mstreng created at 2011-03-28 19:31:41

Patchbot doesn't seem to get the message. New attempt: Apply trac_6371-riemann-theta-REPLACEMENT.patch, trac_6371-riemann-theta-REPLACEMENT-PART2.patch, trac_6371_riemann-theta-REPLACEMENT-PART3.patch


---

Comment by cswiercz created at 2011-03-28 19:47:12

Replying to [comment:13 mstreng]:
> Patchbot doesn't seem to get the message. New attempt: Apply trac_6371-riemann-theta-REPLACEMENT.patch, trac_6371-riemann-theta-REPLACEMENT-PART2.patch, trac_6371_riemann-theta-REPLACEMENT-PART3.patch

I tried just deleting the first patch called "trac_6371-riemann-theta.patch" but I don't have permissions to do so. I'm also unfamiliar with how to tell patchbot to ignore certain patches.

A manual importing of the three patches using ``sage -hg import <the patch>`` results in no issues.


---

Comment by cswiercz created at 2011-03-28 21:20:01

More documentation fixes.


---

Attachment


---

Comment by mstreng created at 2011-03-29 09:18:12

doctest failures (details emailed to author)


---

Comment by mstreng created at 2011-03-29 09:18:12

Changing status from needs_review to needs_work.


---

Comment by cswiercz created at 2011-03-29 20:50:55

Fixed derivative calculation errors that resulted in incorrect doctests.


---

Attachment

Fixed issues with computing derivatives that resulted in doctest failures. Minor documentation fixes as well.


---

Comment by cswiercz created at 2011-03-29 20:51:59

Changing status from needs_work to needs_review.


---

Comment by cswiercz created at 2011-10-27 15:31:56

With further examples, I noticed that there were some calculation issues. Traced this back to mixture of notation under Heil's transformation. Rewriting good chunk of the code using only the notation from "Computing Riemann Theta Functions" by Deconinck et. al.


---

Comment by cswiercz created at 2011-10-27 15:31:56

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by cswiercz created at 2011-12-07 19:06:45

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by bern4rd created at 2011-12-07 19:48:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-12-10 10:42:30

I get a doctest failure in `devel/sage/sage/all.py`


---

Comment by jdemeyer created at 2011-12-10 10:42:30

Changing status from positive_review to needs_work.


---

Comment by cswiercz created at 2011-12-10 20:01:55

Replying to [comment:27 jdemeyer]:
> I get a doctest failure in `devel/sage/sage/all.py`

I see. The error is:


```

sage -t  "devel/sage-6371/sage/all.py"                      
**********************************************************************
File "/home/cswiercz/sage-4.7.1/devel/sage-6371/sage/all.py", line 17:
    sage: len(frames)
Expected:
    11
Got:
    26
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/cswiercz/.sage//tmp/all_20664.py
	 [3.4 s]
```


However, I'm not qualified to make a fix since I don't really understand the purpose of this test. Does anyone on cc: know what's going on in this file and why my Riemann Theta code would affect it?


---

Comment by was created at 2011-12-10 20:17:36

Chris:  Have you read #10570?   That explains what this test is about and why it is important.  Your code evidently gets imported when Sage starts up, and does something potentially leaky.


---

Comment by cswiercz created at 2011-12-10 20:42:31

Replying to [comment:29 was]:
> Chris:  Have you read #10570?   That explains what this test is about and why it is important.  Your code evidently gets imported when Sage starts up, and does something potentially leaky. 

Yes, I read this ticket but I'm not sure how to resolve the "potential leakiness".

One candidate for where this issue might be coming from is my use of a class constructor. I have some code in `riemann_theta.py` in the following form:


```
def RiemannTheta_Constructor(foo, bar):
    class RiemannTheta(Function_RiemannTheta):
        def __init__(...):
            self.foo = foo
            self.bar = bar
            Function_RiemannTheta.__init__()

    return RiemannTheta(...)

RiemannTheta = RiemannTheta_Constructor

class Function_RiemannTheta(BuiltinFunction):
   ...
```


I needed to do things this way so I could parameterize `RiemannTheta` by things such as directional derivative and Riemann matrix. Otherwise, things behave not as expected due to the way `BuiltinFunction` behaves. (For example, two instances of `RiemannTheta` would share the same Riemann matrix or derivatives.) With the above code structure I found that these issues don't arise and two instances of `RiemannTheta` behaved independently as expected.

I'd hate to introduce memory leaks due to my lack of understanding of `BuiltinFunction`. (Granted, the documentation for creating classes that inherit `BuiltinFunction` is severely lacking as well.) However, I don't see how I'd start fixing the issue aside from increasing `len(frames)` in the error message above from 11 to 26. Any suggested resources on how I could better perform what I'm doing in the class and function construction above? Again, the `BuiltinFunction` documentation wasn't helpful beyond copying what preexisting inheritors in `sage.functions` do.


---

Comment by mstreng created at 2012-01-12 12:48:49

I don't know much about `BuiltinFunction`, but I suspect that it isn't meant for what you are trying to do. All the examples that I know of `BuiltinFunction` are single fixed functions, independent of any parameters, such as cos, min, max, `IndefiniteIntegral`, Gamma, dirac_delta, etc.

Your objects however depend on a parameter Omega, and are functions only of z. They are maps `theta(Omega): CC^g --> CC : z |--> theta(z)`. This will not be a "built-in function of Sage" for every Omega, so it does not sound to me like this should be a `BuiltinFunction` object. Maybe the memory leak is caused by this.

The function `theta: CC^g x H_g --> CC : (z, Omega) |--> theta(z, Omega)` definitely make sense as a built-in function, but not a function `theta(Omega) : CC^g --> C` that depends on Omega. In other words, if you have a function for which Omega is not a parameter but an actual variable, then that would make a good built-in function.

ps. Could you make sure you break the lines in the patch at 79 characters?


---

Comment by cswiercz created at 2012-01-18 18:48:23

Hello mstreng,

Replying to [comment:31 mstreng]:
> I don't know much about `BuiltinFunction`, but I suspect that it isn't meant for what you are trying to do. All the examples that I know of `BuiltinFunction` are single fixed functions, independent of any parameters, such as cos, min, max, `IndefiniteIntegral`, Gamma, dirac_delta, etc.

It was my misunderstanding that `BuiltinFunction` is necessary for doing symbolic manipulation. My only reason for using it is so I can compute derivatives, etc. If you know of an alternate way to enable symbolics then I'd love to hear about it!

> Your objects however depend on a parameter Omega, and are functions only of z. They are maps `theta(Omega): CC^g --> CC : z |--> theta(z)`. This will not be a "built-in function of Sage" for every Omega, so it does not sound to me like this should be a `BuiltinFunction` object. Maybe the memory leak is caused by this.

I'll experiment with the code and see if this is an issue.

In practice, $\Omega$ is treated more as a parameter than an argument of the Riemann theta function. That is, $\Omega$ is usually fixed and $z$ varies. Several users of my code would like to see this behavior be reflected by having the Riemann theta function be "initialized" by this matrix.

However, if memory leaks are unavoidable in this context then I suppose I'll just have to make $\Omega$ behave like an argument no different from $z$.

> The function `theta: CC^g x H_g --> CC : (z, Omega) |--> theta(z, Omega)` definitely make sense as a built-in function, but not a function `theta(Omega) : CC^g --> C` that depends on Omega. In other words, if you have a function for which Omega is not a parameter but an actual variable, then that would make a good built-in function.

Makes sense.

> ps. Could you make sure you break the lines in the patch at 79 characters?

Of course! (As an in-terminal emacs user I usually try to do this anyway.)


---

Comment by mstreng created at 2012-01-18 19:31:00

Hi Chris,

Replying to [comment:32 cswiercz]:
> If you know of an alternate way to enable symbolics then I'd love to hear about it!

I don't: I've never implemented any of them.

> In practice, $\Omega$ is treated more as a parameter than an argument of the Riemann theta function. That is, $\Omega$ is usually fixed and $z$ varies.

:) Actually, when I use theta functions in my research, Omega is usually the variable and z is usually some fixed vector in with entries in QQ.

Anyway, what is the (programming technical) reason for having objects that depend on Omega? Is there some kind of caching involved? Some part of the algorithm that depends on Omega only and that you only want to do once?

Marco


---

Comment by cswiercz created at 2012-01-18 21:02:21

Marco,

> :) Actually, when I use theta functions in my research, Omega is usually the variable and z is usually some fixed vector in with entries in QQ.
> 
> Anyway, what is the (programming technical) reason for having objects that depend on Omega? Is there some kind of caching involved? Some part of the algorithm that depends on Omega only and that you only want to do once?

Interesting. I've only seen one other instance in which Omega was varied: it was in the context of solving particular boundary value problems.) If you don't mind, do you have a paper you can send me about your work? (cswiercz [at] gmail ]dot[ com)

I agree that there should be no distinction between the two parameters. From what I understood about `BuiltinFunction}}, though, the purpose of distinguishing Omega as a parameter is to make it easy to send symbolic output. Since I initially made this decision, however, I've learned more about the way Sage ({{{BuiltinFuncion`?) handles inputs and determines if they're symbolic. A rewriting of the way arguments are sent to `RiemannTheta` should be possible.

I'll see what I can do about restructuring the code. Thank you very much for your input and suggestions. I'll keep everyone posted on my (slow) progress.


---

Comment by chapoton created at 2015-03-10 22:15:55

I made a git branch from the patches, but it does not work. I have not tried to
find where problems are.
----
New commits:


---

Comment by git created at 2015-03-10 22:17:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-02-18 20:20:29

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-06-10 18:15:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-07-11 11:07:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-06-08 19:55:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2018-03-11 19:55:46

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nbruin created at 2021-02-25 07:47:40

A student will be doing a summer project towards getting Riemann theta functions, their directional derivatives, and characteristics into sage. Can we repurpose this ticket for that?


---

Comment by chapoton created at 2021-02-26 16:25:38

sure, good luck


---

Comment by mstreng created at 2021-02-27 12:28:32

sounds good to me


---

Comment by nbruin created at 2021-09-26 18:37:16

The work is done:

https://github.com/nbruin/RiemannTheta

I have for now published it as a separate pip-able package in the hope that makes it easier for non-sage developers to install it, use it, and comment on it, but eventually the proper place is probably within sage (it's not a lot of code and it's tightly bound to a lot of sage-specific functionality). So the question prior to making a branch for inclusion into sage:

 * functionality and correctness checks. We tried to be careful, but testing generally needs to be done by other people too to get a good idea of how the code performs more generally
 * where to put it into sage? (sage.numerical would be appropriate, or we could place it next to riemann_surfaces because theoretically that's what it's close too -- although of course theta functions are properties of complex lattices, not particularly of Riemann surfaces.
 * do riemann_theta and siegel_reduction go in the same spot?

Also, once it's in, where/how do we expose the functionality in the global namespace (if at all)? Note that the design is a little less ambitious than the cswiercz and no attempt is made to have an `SR` wrapper of the numerical tool. It does have the big advantage that, as far as I know, the code produces answers of the accuracy one can reasonably expect and does so with reasonable efficiency.
