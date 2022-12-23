# Issue 4433: [with patch, needs review] Replace factorial with a symbolic version

Issue created by migration from https://trac.sagemath.org/ticket/4433

Original creator: whuss

Original creation time: 2008-11-03 20:07:01

Assignee: burcin

This patch depends on #4432. It replaces the factorial in sage.rings.arith with the symbolic
version of #4432 in sage.calculus.calculus.

For now sage.rings.arith.factorial is just renamed to factorial_numeric, otherwise I got
circular imports at Sage startup.

The patch is against sage-3.2alpha1.

After applying this patch plus the patches at #4432 all doctests passed.

A sample session:


```
sage: gamma(x/2)(x=5)
3*sqrt(pi)/4

sage: f = factorial(x + factorial(y))
sage: maxima(f).sage()
factorial(factorial(y) + x)

sage: f(y=x)(x=3)
362880
```





---

Attachment


---

Comment by whuss created at 2008-11-03 20:13:20

Changing assignee from burcin to whuss.


---

Comment by whuss created at 2008-11-04 07:41:29

Changing type from defect to enhancement.


---

Comment by mhansen created at 2008-11-04 21:03:40

I don't understand the purpose of converting everything to use the new factorial function defined in calculus.all since none of the existing code needed any of the functionality it provides.


---

Attachment


---

Comment by whuss created at 2008-11-05 16:39:57

I wanted to remove the factorial in rings.arith completely, because I think it is confusing
to have to different factorial functions at the toplevel. Also Sage doesn't do this for the
other symbolic functions like sin().

In the previous version rings.arith.factorial_numeric() was just there because I had not yet
solved the problem of circular imports at Sage startup.

Now second patch that I just uploaded fixes this problem. Now there is only the factorial
in calculus.all.

With both patches applied to sage-3.2alpha1 all doctests pass for me.


---

Comment by mabshoff created at 2008-11-05 17:11:21

A couple remarks:

 * the first patch removes "!" from the list of tokens which we used to ignore up to now. Now it changes meaning to be factorial, but I am not so sure it is a good idea since we use to explicitly forbid it. I don't know the reason why we did that, so see my comment below.
 * the second patch removes fact() [nee factorial_numeric()] from arith.py, but policy is to deprecate removed functions, especially something as simple and long existing like fact() in that file cannot be just removed. See "def dynkin_diagram(t)" in combinat/root_system/dynkin_diagram.py for an good example on how to use deprecation in Sage. 

Especially the "!" change should be discussed on [sage-devel] since that is a rather fundamental change. I also cannot find a single occurrence of "!" in the docstring or tests, but maybe I  overlooked something. *If* the patch is merged with the "!" change it needs to be doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-05 17:13:01

And a final comment about calculus.py: That file is rather large and messy, so there are various people who think that the file should be split up in the future. "New symbolics" might be just what is required there in the long term.

Cheers,

Michael


---

Comment by mhansen created at 2008-11-05 17:15:55

We also shouldn't get rid of the documentation and algorithm keyword in sage.rings.arith.factorial just because.  Overall, I'd recommend just leaving it as is and not importing it to the top level.


---

Comment by mabshoff created at 2008-11-05 21:45:22

Mike Hansen just pointed out to me in IRC that the "!" is used on the Maxima side, so I was wrong and you can disregard my comment about that.

Cheers,

Michael


---

Attachment

supersedes the previous two patches


---

Comment by whuss created at 2008-11-06 12:49:56

In the new patch sage.rings.arith.factorial is kept but deprecated.


---

Comment by whuss created at 2008-11-06 13:35:16

The other issues should by fixed by the latest patch for #4432.


---

Comment by mabshoff created at 2008-11-21 09:29:32

Since there is a new patch up here this one needs review again.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-28 07:28:57

Resolution: fixed


---

Comment by mabshoff created at 2008-11-28 07:28:57

Fixed by #4432 in Sage 3.2.1.rc0


---

Comment by mabshoff created at 2008-11-28 07:30:13

The positive review stems from the review of the cumulative patch at #4432.

Cheers,

Michael
