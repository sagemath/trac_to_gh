# Issue 2617: solve() can return undefined points as "solutions"

Issue created by migration from https://trac.sagemath.org/ticket/2617

Original creator: cwitty

Original creation time: 2008-03-20 20:22:24

Assignee: was

Consider the following examples (reported by Dean Moore here: http://groups.google.com/group/sage-support/browse_thread/thread/5555e780a76b3343#)

```
sage: solve(sin(x^2)/x == 0)
[x == 0]
sage: solve(sin(x^2)/x^2 == 0)
[x == 0]
sage: solve(sin(x^2)/x^3 == 0)
[x == 0]
```

None of these functions are even defined at x=0, so that should not be returned as a solution.  (The first two functions can be extended to x=0 by taking limits, in which case x=0 is a solution to the first one but not the second; the third function has a vertical asymptote at x=0.)


---

Comment by mabshoff created at 2008-04-12 18:18:11

Is this a bug in Maxima? In that case we should report those to them? This also seams like a fairly serious issue, so I am elevating this to critical.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-12 18:18:11

Changing priority from major to critical.


---

Comment by kcrisman created at 2009-08-26 15:42:57

This is a Maxima bug as of 5.16.3, and has been reported there as 2845005 (see [http://sourceforge.net/tracker/?func=detail&aid=2845005&group_id=4933&atid=104933](http://sourceforge.net/tracker/?func=detail&aid=2845005&group_id=4933&atid=104933)).


---

Comment by robert.marik created at 2009-10-08 06:24:10

Perhaps related issue is also that the solving acot(x) == 0 ends with error message "The number 0 isn't in the domain of cot"

The online tool Mathatmatical Assistant on Web ( http://user.mendelu.cz/marik/maw/index.php?lang=en&form=main ) has a wrapper for maxima's solve ( http://mathassistant.cvs.sourceforge.net/viewvc/mathassistant/maw/common/maw_solve.mac?revision=1.14&view=markup )

I hope, it could be used also in Sage. I'll try it, hope within a week.


---

Comment by kcrisman created at 2009-10-08 13:47:46

Replying to [comment:3 robert.marik]:
> Perhaps related issue is also that the solving acot(x) == 0 ends with error message "The number 0 isn't in the domain of cot"
> 

No, this is an appropriate error message (it's from Maxima, not Sage). There are no solutions to acot(x)==0, at least over the reals (and presumably over the complex field as well?).  Now that we know about that error, it would be easy to put a catch in for something like that error message and return 
sage: solve(acot(x),x)
[]
instead.  Feel free to open a ticket for that and put me in the cc: field.  

But this is unrelated to the issue in the ticket, which is a genuine Maxima bug, as far as I can tell.


---

Comment by kcrisman created at 2009-12-22 19:44:55

Replying to [comment:4 kcrisman]:
> Replying to [comment:3 robert.marik]:
> > Perhaps related issue is also that the solving acot(x) == 0 ends with error message "The number 0 isn't in the domain of cot"
> > 
> 
> No, this is an appropriate error message (it's from Maxima, not Sage). There are no solutions to acot(x)==0, at least over the reals (and presumably over the complex field as well?).  Now that we know about that error, it would be easy to put a catch in for something like that error message and return 
> sage: solve(acot(x),x)
> []
This will be addressed (not the main point of this ticket) in the patch for #7745.  The main point is still a bug in Maxima 5.20.1.


---

Comment by robert.marik created at 2009-12-22 22:50:03

I had an idea to introduce new option to solve, which 


1. Takes only explicit solutions


2. Substitutes into equation and if an error appears, removes this "solution" from the list. 



The problem in this approach is, that for example ln(0)=-Infinity in Sage and so x=0 will be still reported as a solution of x/ln(x)=0. The problem could be solved by substituting values in Maxima and not in Sage, but I am still thinking on some cleaner solution. And still  have no idea what should be returned as solution of x*ln(x-3) == 0. Distinguish in this new option, if the user works in real domain or in complex doman? Something like check_domain = False, True, or 'real'?




Any idea?


---

Comment by kcrisman created at 2009-12-24 03:21:19

As it turns out, to_poly_solve can handle this sort of thing (see in Maxima the share/contrib/rtest_to_poly_solver.mac line 1092).  But we would have to figure out a way to interpret the if statements properly (for instance, to note that twice an integer plus one is not zero).

```
/* Sage Ticket 2617; see also Sage mailing list 18 March 2008 */

nicedummies(to_poly_solve(sin(x^2)/x,x));
%union(%if(2*%z0+1 # 0,[x = -sqrt(2*%pi*%z0+%pi)],%union()),
             %if(2*%z0+1 # 0,[x = sqrt(2*%pi*%z0+%pi)],%union()),
             %if(%z1 # 0,[x = -sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()),
             %if(%z1 # 0,[x = sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()))$

nicedummies(to_poly_solve(sin(x^2)/x^2,x));
%union(%if(2*%z0+1 # 0,[x = -sqrt(2*%pi*%z0+%pi)],%union()),
             %if(2*%z0+1 # 0,[x = sqrt(2*%pi*%z0+%pi)],%union()),
             %if(%z1 # 0,[x = -sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()),
             %if(%z1 # 0,[x = sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()))$

nicedummies(to_poly_solve(sin(x^2)/x^3,x));
%union(%if(2*%z0+1 # 0,[x = -sqrt(2*%pi*%z0+%pi)],%union()),
             %if(2*%z0+1 # 0,[x = sqrt(2*%pi*%z0+%pi)],%union()),
             %if(%z1 # 0,[x = -sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()),
             %if(%z1 # 0,[x = sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()))$
```



---

Comment by kcrisman created at 2011-06-15 21:21:49

Changing priority from critical to major.


---

Comment by zonova created at 2016-05-20 21:46:39

SO, has this issue been fixed yet? What of kcrisman and robert.marik's suggestions? Also is there a reason that there is no branch to edit?


---

Comment by kcrisman created at 2016-05-23 13:58:25

Presumably not fixed.  No branch because no one has posted one yet - if you have a fix you can be the first to post a branch!


---

Comment by zonova created at 2016-11-27 05:29:20

kcrisman, in your post (from 7 years ago) you had mentioned to_poly_solve in maxima's share/contrib. It's been a while since then, so it is not located there anymore. I couldn't find it anywhere in Maxima's source on github though, so i wasn't sure if it was still used at all. Does sage/maxima use it at all? 

I've been looking at several old tickets, all involving solving equations. One was using find_root, which uses scipy, and the other had to do with solve just like this one. I think it would be best to just have one, no? As far as I can tell, they do about the same thing, and they both have issues. On a similar note, if to_poly_solve resolves this issue, then maybe we should use that for all equation solving?


---

Comment by kcrisman created at 2016-11-28 15:50:20

We definitely have that method and it is still in Maxima.  Looks like it moved to [https://sourceforge.net/p/maxima/code/ci/master/tree/share/to_poly_solve/](https://sourceforge.net/p/maxima/code/ci/master/tree/share/to_poly_solve/).

However, `find_root` is explicitly supposed to be a numerical solver, while `solve` is supposed to be an exact solver.  Because `to_poly_solve` sometimes returns numerical answers in rare situations, there could be some overlap.  Also, `to_poly_solve` is not what we want for all solving, because it changes some other things and of course might take longer for simple ones.  It has a specific purpose, but that is not a general purpose.

On the other hand, if sympy can now solve everything Maxima does, one could try to switch the default algorithm to use that instead.  I don't know if we're at that point, though.


---

Comment by @Torrencem created at 2019-07-07 17:31:06

This has still been an issue, and so I've implemented an optional solution

You can pass the optional argument (`check_domain`) to `solve`, which will tell it to check each solution it finds with SymPy to see if it's NaN. I added some documentation and an example.

I ran (on my machine) all the current doc-tests with the new argument to make sure it accepts all their solutions, and it does, but I believe it significantly slows down the function, so probably should not end up defaulting to `True` without some more considerations / optimizations (especially since `solve` is widely used)

See the added documentation example:


```
sage: solve((x^2 - 1)/(sin(x - 1)) == 0, x, check_domain=True)
[x == -1]
```

----
New commits:


---

Comment by @Torrencem created at 2019-07-07 17:31:06

Changing status from new to needs_review.


---

Comment by embray created at 2019-12-30 14:48:17

Ticket retargeted after milestone closed


---

Comment by vdelecroix created at 2020-02-22 15:34:57

On 9.1.beta5 we get something else than the ticket description

```
sage: solve(sin(x^2)/x == 0)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-1-e922184d1fd1> in <module>()
----> 1 solve(sin(x**Integer(2))/x == Integer(0))

/opt/sage/local/lib/python3.7/site-packages/sage/symbolic/relation.py in solve(f, *args, **kwds)
   1016         x = args
   1017     else:
-> 1018         x = args[0]
   1019     if isinstance(x, (list, tuple)):
   1020         for i in x:

IndexError: tuple index out of range
```



---

Comment by vdelecroix created at 2020-02-22 15:39:59

Your solution is somehow complicated and provides a wrong answer. Why not prefer

```
sage: solve(sin(x^2)/x^3 == 0, x, algorithm="sympy")
Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))
```



---

Comment by vdelecroix created at 2020-02-22 15:39:59

Changing status from needs_review to needs_info.


---

Comment by @varenyamBakshi created at 2020-02-22 17:54:25

Replying to [comment:22 vdelecroix]:
> Your solution is somehow complicated and provides a wrong answer. Why not prefer
> {{{
> sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm="sympy")
> Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))
> }}}

the syntax you are providing is not user friendly. I would prefer the previous syntax.


---

Comment by @Shlokatadistance created at 2020-03-02 15:36:31

Replying to [comment:22 vdelecroix]:
> Your solution is somehow complicated and provides a wrong answer. Why not prefer
> {{{
> sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm="sympy")
> Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))
> }}}
I think the syntax simplicity can be judged in the later stages, I do want to ask are you able to obtain the answer from this? because I can't seem to be getting this work, even after a certain modification, such as additional functions for testing and new variable.


---

Comment by vdelecroix created at 2020-03-02 15:39:12

Replying to [comment:24 gh-Shlokatadistance]:
> Replying to [comment:22 vdelecroix]:
> > Your solution is somehow complicated and provides a wrong answer. Why not prefer
> > {{{
> > sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm="sympy")
> > Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))
> > }}}
> I think the syntax simplicity can be judged in the later stages, I do want to ask are you able to obtain the answer from this? because I can't seem to be getting this work, even after a certain modification, such as additional functions for testing and new variable.

I don't understand your question. `Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))` is the answer. Not in a very nice form, but a valid answer.


---

Comment by @Shlokatadistance created at 2020-03-02 16:00:32

Replying to [comment:25 vdelecroix]:
> Replying to [comment:24 gh-Shlokatadistance]:
> > Replying to [comment:22 vdelecroix]:
> > > Your solution is somehow complicated and provides a wrong answer. Why not prefer
> > > {{{
> > > sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm="sympy")
> > > Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))
> > > }}}
> > I think the syntax simplicity can be judged in the later stages, I do want to ask are you able to obtain the answer from this? because I can't seem to be getting this work, even after a certain modification, such as additional functions for testing and new variable.
> 
> I don't understand your question. `Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))` is the answer. Not in a very nice form, but a valid answer.

Ahh my bad, I was trying to obtain a more numeric based answer, I did see that the second statement did resemble the solution


---

Comment by vdelecroix created at 2020-03-02 16:31:16

Replying to [comment:26 gh-Shlokatadistance]:
> Replying to [comment:25 vdelecroix]:
> > Replying to [comment:24 gh-Shlokatadistance]:
> > > Replying to [comment:22 vdelecroix]:
> > > > Your solution is somehow complicated and provides a wrong answer. Why not prefer
> > > > {{{
> > > > sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm="sympy")
> > > > Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))
> > > > }}}
> > > I think the syntax simplicity can be judged in the later stages, I do want to ask are you able to obtain the answer from this? because I can't seem to be getting this work, even after a certain modification, such as additional functions for testing and new variable.
> > 
> > I don't understand your question. `Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))` is the answer. Not in a very nice form, but a valid answer.
> 
> Ahh my bad, I was trying to obtain a more numeric based answer, I did see that the second statement did resemble the solution

Ideally, it should be possible to convert it to the parametrized set `{sqrt(2*n*pi): n in ZZ \ {0}}`.


---

Comment by @Shlokatadistance created at 2020-03-21 19:38:21

Yes exactly, from what I reckon the procedure is simply returning like a set, and I think that has to do with the way the conditions were defined. I think by providing a few other cases on the same will help us resolve this issue, something along the lines of

```
def condition_set():
   for x in solution_set # this can be solution set for our trigonometric functions
       a = solve(the given problem)
       ans = pi_set(a) # pi_set is the set of our pi value, based on a random value
      return ans
```

Something along these lines , of course this is just a suggestion


---

Comment by mkoeppe created at 2021-04-02 20:21:54

Moving this ticket to 9.4, as it seems unlikely that it will be merged in 9.3, which is in the release candidate stage


---

Comment by mkoeppe created at 2021-07-19 00:44:56

Setting a new milestone for this ticket based on a cursory review.


---

Comment by mkoeppe created at 2021-12-18 19:53:12

Stalled in `needs_review` or `needs_info`; likely won't make it into Sage 9.5.
