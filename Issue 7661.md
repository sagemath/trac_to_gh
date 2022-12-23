# Issue 7661: maxima interface gives precedence to function dictionary instead of local variables

Issue created by migration from https://trac.sagemath.org/ticket/7661

Original creator: burcin

Original creation time: 2009-12-11 14:18:05

Assignee: was

CC:  robert.marik

Keywords: maxima

From the sage-devel thread:

http://groups.google.com/group/sage-devel/t/c89582242c83a349


```
On Fri, 11 Dec 2009 13:46:31 +0100
Nathann Cohen <nathann.cohen@gmail.com> wrote:

> sage: var('delta k')
> sage: m1=2*delta**2 + 2**2*delta*k
> sage: n=delta*k+2
> sage: m2=(2*delta)**2+(k-1)*4
> sage: m=(delta+delta*k-(delta-1))
> sage: ((m1/n)-(m2/n)).expand().simplify()
```


On 4.3.rc0, I get this:

```
TypeError: unsupported operand parent(s) for '*': 'Symbolic Ring' and
'<class 'sage.functions.generalized.FunctionDiracDelta'>'
```


The Maxima interface seems to give precedence to the global function
dictionary instead of the local variables when converting Maxima output
back to Sage expressions.

```
sage: dirac_delta(x)
dirac_delta(x)
sage: maxima(dirac_delta(x))
delta(x)
```



---

Comment by was created at 2010-01-30 23:28:06

People run into this all the time, evidently:

```
[15:21] --> SageWWW has joined this channel (~SageWWW@64.241.37.140).
[15:23] <SageWWW> hey guys.  what do you think about http://pastebin.ca/1772520
[15:24] <SageWWW> d = var('delta'), so now d is a reference to a sage.symbolic.expression.Expression
[15:25] <SageWWW> but when we try to add it to something else, it thinks its a sage.functions.generalized.FunctionDiracDelta
[15:27] <wstein> http://trac.sagemath.org/sage_trac/ticket/7661
```



---

Comment by eigenlambda created at 2010-01-31 07:10:34

sage: d = var('delta')
sage: e = d._maxima_()
sage: sage.calculus.calculus.symbolic_expression_from_maxima_element(e)
dirac_delta

somewhere in symbolic_expression_from_maxima_element(), the string from maxima is looked up in sage.calculus.calculus._syms, which by default has 'delta': dirac_delta .  So this is what's happening, next, SR() barfs on trying to turn dirac_delta into a symbolic expression, at which point people who just wanted their variable 'delta' back get confused and frustrated.

sage: del sage.calculus.calculus._syms['delta']
sage: sage.calculus.calculus.symbolic_expression_from_maxima_element(e)
delta

That may not be such a good idea, however, since what sage calls dirac_delta, maxima refers to as delta.  Nevertheless, since reset('delta') appears to remove delta from that dictionary, perhaps var('delta') should also do so?

Of course, what happens when someone does a Laplace transform with delta as a sage variable will then come out confusing and wrong.  At least the current behavior is merely broken.


---

Comment by burcin created at 2010-04-05 10:24:35

attachment:trac_7661-maxima_convert_back.patch fixes the problem reported above, and a similar problem with function conversions back from maxima reported in comment:2:ticket:8459.


---

Comment by burcin created at 2010-04-05 10:24:35

Changing priority from major to critical.


---

Comment by burcin created at 2010-04-05 10:24:35

Changing status from new to needs_review.


---

Attachment

I updated attachment:trac_7661-maxima_convert_back.patch to remove a doctest fix broken by a previous patch in my queue (#6949, `symbol...` line in sage/symbolic/ring.pyx).

This patch depends on #7748.


---

Comment by robert.marik created at 2010-04-09 08:15:04

Thanks for working onthis. Is #7748 the only prerequisity? I installed three patches as described at #7748 and got the following error

```
patching file sage/calculus/calculus.py
Hunk #3 succeeded at 1414 with fuzz 1 (offset -4 lines).
Hunk #5 FAILED at 1455
1 out of 14 hunks FAILED -- saving rejects to file sage/calculus/calculus.py.rej
abort: patch failed to apply
```



---

Comment by burcin created at 2010-04-09 10:46:48

AFAICT, #8237 also changes that code. Can you try with #8237 applied?

I'm sorry for the dependency hell we get into with these patches for every release. I don't know any way to automatically get a list of dependencies for a patch in my queue.

Thanks for your time Robert.


---

Comment by burcin created at 2010-04-09 10:46:48

Changing assignee from was to burcin.


---

Comment by robert.marik created at 2010-04-09 14:23:42

Hello Burcin

I think that two lines should be removed from the patch

```
global _syms 
_syms = sage.symbolic.pynac.symbol_table.get('maxima', {}) 
```


I updated your patch, it is now http://user.mendelu.cz/marik/sage/trac_7661-maxima_convert_back2.patch

If everything will work, I'll return in few (several) hours with positive review (tests in functions, interfaces, symbolics and calculus passed, now running all the test). 

Robert


---

Comment by burcin created at 2010-04-09 14:34:40

OK. That is one approach to solving this problem. Now we need to rebase the patch at #8237 so that it applies on top of these. Removing the offending hunk from `calculus.py` should be enough for that.

Note that your updated patch shows you as the author. I'd appreciate it if you changed that back.

Thanks.


---

Comment by robert.marik created at 2010-04-09 16:52:06

Sure, it was intended as temporary patch and from this reason I did not upload to trac server unless tested. I got some doctest failures in three files. See http://boxen.math.washington.edu/home/marik/ and the files a, b and c.

I think that b is simple to fix, but have no idea about a and c.


---

Comment by robert.marik created at 2010-04-09 16:52:06

Changing status from needs_review to needs_work.


---

Attachment

apply only this patch


---

Comment by burcin created at 2010-04-09 18:57:13

Thanks a lot for the quick feedback. 
 * `a` is because you have the pynac package from #8644 installed, but not the corresponding patch from #8565. 
 * `b` is a simple import problem, fixed by the updated attachment:trac_7661-maxima_convert_back.take2.patch
 * I can't reproduce `c` here. It doesn't seem to be related to the changes in ticket. Do you have any other patches applied?


---

Comment by robert.marik created at 2010-04-10 17:29:35

I tested it on a fresh install and seems that all a,b,c are resolved.
I am running all tests again, to be sure :)


---

Comment by robert.marik created at 2010-04-10 17:29:35

Changing status from needs_work to needs_review.


---

Comment by robert.marik created at 2010-04-10 19:31:20

Tests passed, postive review, thanks for fixing - very very usefull ticket.

Release manager: apply only trac_7661-maxima_convert_back.take2.patch


---

Comment by robert.marik created at 2010-04-10 19:31:20

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 20:15:35

Merged "trac_7661-maxima_convert_back.take2.patch" in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-15 20:15:35

Resolution: fixed
