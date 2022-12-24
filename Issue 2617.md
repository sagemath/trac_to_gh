# Issue 2617: solve() can return undefined points as "solutions"

archive/issues_002617.json:
```json
{
    "body": "Assignee: @williamstein\n\nConsider the following examples (reported by Dean Moore here: http://groups.google.com/group/sage-support/browse_thread/thread/5555e780a76b3343#)\n\n```\nsage: solve(sin(x^2)/x == 0)\n[x == 0]\nsage: solve(sin(x^2)/x^2 == 0)\n[x == 0]\nsage: solve(sin(x^2)/x^3 == 0)\n[x == 0]\n```\n\nNone of these functions are even defined at x=0, so that should not be returned as a solution.  (The first two functions can be extended to x=0 by taking limits, in which case x=0 is a solution to the first one but not the second; the third function has a vertical asymptote at x=0.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2617\n\n",
    "created_at": "2008-03-20T20:22:24Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "solve() can return undefined points as \"solutions\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2617",
    "user": "cwitty"
}
```
Assignee: @williamstein

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

Issue created by migration from https://trac.sagemath.org/ticket/2617





---

archive/issue_comments_017960.json:
```json
{
    "body": "Is this a bug in Maxima? In that case we should report those to them? This also seams like a fairly serious issue, so I am elevating this to critical.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-12T18:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17960",
    "user": "mabshoff"
}
```

Is this a bug in Maxima? In that case we should report those to them? This also seams like a fairly serious issue, so I am elevating this to critical.

Cheers,

Michael



---

archive/issue_comments_017961.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-04-12T18:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17961",
    "user": "mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_017962.json:
```json
{
    "body": "This is a Maxima bug as of 5.16.3, and has been reported there as 2845005 (see [http://sourceforge.net/tracker/?func=detail&aid=2845005&group_id=4933&atid=104933](http://sourceforge.net/tracker/?func=detail&aid=2845005&group_id=4933&atid=104933)).",
    "created_at": "2009-08-26T15:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17962",
    "user": "@kcrisman"
}
```

This is a Maxima bug as of 5.16.3, and has been reported there as 2845005 (see [http://sourceforge.net/tracker/?func=detail&aid=2845005&group_id=4933&atid=104933](http://sourceforge.net/tracker/?func=detail&aid=2845005&group_id=4933&atid=104933)).



---

archive/issue_comments_017963.json:
```json
{
    "body": "Perhaps related issue is also that the solving acot(x) == 0 ends with error message \"The number 0 isn't in the domain of cot\"\n\nThe online tool Mathatmatical Assistant on Web ( http://user.mendelu.cz/marik/maw/index.php?lang=en&form=main ) has a wrapper for maxima's solve ( http://mathassistant.cvs.sourceforge.net/viewvc/mathassistant/maw/common/maw_solve.mac?revision=1.14&view=markup )\n\nI hope, it could be used also in Sage. I'll try it, hope within a week.",
    "created_at": "2009-10-08T06:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17963",
    "user": "@robert-marik"
}
```

Perhaps related issue is also that the solving acot(x) == 0 ends with error message "The number 0 isn't in the domain of cot"

The online tool Mathatmatical Assistant on Web ( http://user.mendelu.cz/marik/maw/index.php?lang=en&form=main ) has a wrapper for maxima's solve ( http://mathassistant.cvs.sourceforge.net/viewvc/mathassistant/maw/common/maw_solve.mac?revision=1.14&view=markup )

I hope, it could be used also in Sage. I'll try it, hope within a week.



---

archive/issue_comments_017964.json:
```json
{
    "body": "Replying to [comment:3 robert.marik]:\n> Perhaps related issue is also that the solving acot(x) == 0 ends with error message \"The number 0 isn't in the domain of cot\"\n> \n\nNo, this is an appropriate error message (it's from Maxima, not Sage). There are no solutions to acot(x)==0, at least over the reals (and presumably over the complex field as well?).  Now that we know about that error, it would be easy to put a catch in for something like that error message and return \nsage: solve(acot(x),x)\n[]\ninstead.  Feel free to open a ticket for that and put me in the cc: field.  \n\nBut this is unrelated to the issue in the ticket, which is a genuine Maxima bug, as far as I can tell.",
    "created_at": "2009-10-08T13:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17964",
    "user": "@kcrisman"
}
```

Replying to [comment:3 robert.marik]:
> Perhaps related issue is also that the solving acot(x) == 0 ends with error message "The number 0 isn't in the domain of cot"
> 

No, this is an appropriate error message (it's from Maxima, not Sage). There are no solutions to acot(x)==0, at least over the reals (and presumably over the complex field as well?).  Now that we know about that error, it would be easy to put a catch in for something like that error message and return 
sage: solve(acot(x),x)
[]
instead.  Feel free to open a ticket for that and put me in the cc: field.  

But this is unrelated to the issue in the ticket, which is a genuine Maxima bug, as far as I can tell.



---

archive/issue_comments_017965.json:
```json
{
    "body": "Replying to [comment:4 kcrisman]:\n> Replying to [comment:3 robert.marik]:\n> > Perhaps related issue is also that the solving acot(x) == 0 ends with error message \"The number 0 isn't in the domain of cot\"\n> > \n> \n> No, this is an appropriate error message (it's from Maxima, not Sage). There are no solutions to acot(x)==0, at least over the reals (and presumably over the complex field as well?).  Now that we know about that error, it would be easy to put a catch in for something like that error message and return \n> sage: solve(acot(x),x)\n> []\nThis will be addressed (not the main point of this ticket) in the patch for #7745.  The main point is still a bug in Maxima 5.20.1.",
    "created_at": "2009-12-22T19:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17965",
    "user": "@kcrisman"
}
```

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

archive/issue_comments_017966.json:
```json
{
    "body": "I had an idea to introduce new option to solve, which \n\n\n1. Takes only explicit solutions\n\n\n2. Substitutes into equation and if an error appears, removes this \"solution\" from the list. \n\n\n\nThe problem in this approach is, that for example ln(0)=-Infinity in Sage and so x=0 will be still reported as a solution of x/ln(x)=0. The problem could be solved by substituting values in Maxima and not in Sage, but I am still thinking on some cleaner solution. And still  have no idea what should be returned as solution of x*ln(x-3) == 0. Distinguish in this new option, if the user works in real domain or in complex doman? Something like check_domain = False, True, or 'real'?\n\n\n\n\nAny idea?",
    "created_at": "2009-12-22T22:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17966",
    "user": "@robert-marik"
}
```

I had an idea to introduce new option to solve, which 


1. Takes only explicit solutions


2. Substitutes into equation and if an error appears, removes this "solution" from the list. 



The problem in this approach is, that for example ln(0)=-Infinity in Sage and so x=0 will be still reported as a solution of x/ln(x)=0. The problem could be solved by substituting values in Maxima and not in Sage, but I am still thinking on some cleaner solution. And still  have no idea what should be returned as solution of x*ln(x-3) == 0. Distinguish in this new option, if the user works in real domain or in complex doman? Something like check_domain = False, True, or 'real'?




Any idea?



---

archive/issue_comments_017967.json:
```json
{
    "body": "As it turns out, to_poly_solve can handle this sort of thing (see in Maxima the share/contrib/rtest_to_poly_solver.mac line 1092).  But we would have to figure out a way to interpret the if statements properly (for instance, to note that twice an integer plus one is not zero).\n\n```\n/* Sage Ticket 2617; see also Sage mailing list 18 March 2008 */\n\nnicedummies(to_poly_solve(sin(x^2)/x,x));\n%union(%if(2*%z0+1 # 0,[x = -sqrt(2*%pi*%z0+%pi)],%union()),\n             %if(2*%z0+1 # 0,[x = sqrt(2*%pi*%z0+%pi)],%union()),\n             %if(%z1 # 0,[x = -sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()),\n             %if(%z1 # 0,[x = sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()))$\n\nnicedummies(to_poly_solve(sin(x^2)/x^2,x));\n%union(%if(2*%z0+1 # 0,[x = -sqrt(2*%pi*%z0+%pi)],%union()),\n             %if(2*%z0+1 # 0,[x = sqrt(2*%pi*%z0+%pi)],%union()),\n             %if(%z1 # 0,[x = -sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()),\n             %if(%z1 # 0,[x = sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()))$\n\nnicedummies(to_poly_solve(sin(x^2)/x^3,x));\n%union(%if(2*%z0+1 # 0,[x = -sqrt(2*%pi*%z0+%pi)],%union()),\n             %if(2*%z0+1 # 0,[x = sqrt(2*%pi*%z0+%pi)],%union()),\n             %if(%z1 # 0,[x = -sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()),\n             %if(%z1 # 0,[x = sqrt(2)*sqrt(%pi)*sqrt(%z1)],%union()))$\n```\n",
    "created_at": "2009-12-24T03:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17967",
    "user": "@kcrisman"
}
```

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

archive/issue_comments_017968.json:
```json
{
    "body": "Changing priority from critical to major.",
    "created_at": "2011-06-15T21:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17968",
    "user": "@kcrisman"
}
```

Changing priority from critical to major.



---

archive/issue_comments_017969.json:
```json
{
    "body": "SO, has this issue been fixed yet? What of kcrisman and robert.marik's suggestions? Also is there a reason that there is no branch to edit?",
    "created_at": "2016-05-20T21:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17969",
    "user": "zonova"
}
```

SO, has this issue been fixed yet? What of kcrisman and robert.marik's suggestions? Also is there a reason that there is no branch to edit?



---

archive/issue_comments_017970.json:
```json
{
    "body": "Presumably not fixed.  No branch because no one has posted one yet - if you have a fix you can be the first to post a branch!",
    "created_at": "2016-05-23T13:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17970",
    "user": "@kcrisman"
}
```

Presumably not fixed.  No branch because no one has posted one yet - if you have a fix you can be the first to post a branch!



---

archive/issue_comments_017971.json:
```json
{
    "body": "kcrisman, in your post (from 7 years ago) you had mentioned to_poly_solve in maxima's share/contrib. It's been a while since then, so it is not located there anymore. I couldn't find it anywhere in Maxima's source on github though, so i wasn't sure if it was still used at all. Does sage/maxima use it at all? \n\nI've been looking at several old tickets, all involving solving equations. One was using find_root, which uses scipy, and the other had to do with solve just like this one. I think it would be best to just have one, no? As far as I can tell, they do about the same thing, and they both have issues. On a similar note, if to_poly_solve resolves this issue, then maybe we should use that for all equation solving?",
    "created_at": "2016-11-27T05:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17971",
    "user": "zonova"
}
```

kcrisman, in your post (from 7 years ago) you had mentioned to_poly_solve in maxima's share/contrib. It's been a while since then, so it is not located there anymore. I couldn't find it anywhere in Maxima's source on github though, so i wasn't sure if it was still used at all. Does sage/maxima use it at all? 

I've been looking at several old tickets, all involving solving equations. One was using find_root, which uses scipy, and the other had to do with solve just like this one. I think it would be best to just have one, no? As far as I can tell, they do about the same thing, and they both have issues. On a similar note, if to_poly_solve resolves this issue, then maybe we should use that for all equation solving?



---

archive/issue_comments_017972.json:
```json
{
    "body": "We definitely have that method and it is still in Maxima.  Looks like it moved to [https://sourceforge.net/p/maxima/code/ci/master/tree/share/to_poly_solve/](https://sourceforge.net/p/maxima/code/ci/master/tree/share/to_poly_solve/).\n\nHowever, `find_root` is explicitly supposed to be a numerical solver, while `solve` is supposed to be an exact solver.  Because `to_poly_solve` sometimes returns numerical answers in rare situations, there could be some overlap.  Also, `to_poly_solve` is not what we want for all solving, because it changes some other things and of course might take longer for simple ones.  It has a specific purpose, but that is not a general purpose.\n\nOn the other hand, if sympy can now solve everything Maxima does, one could try to switch the default algorithm to use that instead.  I don't know if we're at that point, though.",
    "created_at": "2016-11-28T15:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17972",
    "user": "@kcrisman"
}
```

We definitely have that method and it is still in Maxima.  Looks like it moved to [https://sourceforge.net/p/maxima/code/ci/master/tree/share/to_poly_solve/](https://sourceforge.net/p/maxima/code/ci/master/tree/share/to_poly_solve/).

However, `find_root` is explicitly supposed to be a numerical solver, while `solve` is supposed to be an exact solver.  Because `to_poly_solve` sometimes returns numerical answers in rare situations, there could be some overlap.  Also, `to_poly_solve` is not what we want for all solving, because it changes some other things and of course might take longer for simple ones.  It has a specific purpose, but that is not a general purpose.

On the other hand, if sympy can now solve everything Maxima does, one could try to switch the default algorithm to use that instead.  I don't know if we're at that point, though.



---

archive/issue_comments_017973.json:
```json
{
    "body": "This has still been an issue, and so I've implemented an optional solution\n\nYou can pass the optional argument (`check_domain`) to `solve`, which will tell it to check each solution it finds with SymPy to see if it's NaN. I added some documentation and an example.\n\nI ran (on my machine) all the current doc-tests with the new argument to make sure it accepts all their solutions, and it does, but I believe it significantly slows down the function, so probably should not end up defaulting to `True` without some more considerations / optimizations (especially since `solve` is widely used)\n\nSee the added documentation example:\n\n\n```\nsage: solve((x^2 - 1)/(sin(x - 1)) == 0, x, check_domain=True)\n[x == -1]\n```\n\n----\nNew commits:",
    "created_at": "2019-07-07T17:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17973",
    "user": "@Torrencem"
}
```

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

archive/issue_comments_017974.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-07-07T17:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17974",
    "user": "@Torrencem"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_017975.json:
```json
{
    "body": "Ticket retargeted after milestone closed",
    "created_at": "2019-12-30T14:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17975",
    "user": "@embray"
}
```

Ticket retargeted after milestone closed



---

archive/issue_comments_017976.json:
```json
{
    "body": "On 9.1.beta5 we get something else than the ticket description\n\n```\nsage: solve(sin(x^2)/x == 0)\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n<ipython-input-1-e922184d1fd1> in <module>()\n----> 1 solve(sin(x**Integer(2))/x == Integer(0))\n\n/opt/sage/local/lib/python3.7/site-packages/sage/symbolic/relation.py in solve(f, *args, **kwds)\n   1016         x = args\n   1017     else:\n-> 1018         x = args[0]\n   1019     if isinstance(x, (list, tuple)):\n   1020         for i in x:\n\nIndexError: tuple index out of range\n```\n",
    "created_at": "2020-02-22T15:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17976",
    "user": "@videlec"
}
```

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

archive/issue_comments_017977.json:
```json
{
    "body": "Your solution is somehow complicated and provides a wrong answer. Why not prefer\n\n```\nsage: solve(sin(x^2)/x^3 == 0, x, algorithm=\"sympy\")\nComplement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))\n```\n",
    "created_at": "2020-02-22T15:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17977",
    "user": "@videlec"
}
```

Your solution is somehow complicated and provides a wrong answer. Why not prefer

```
sage: solve(sin(x^2)/x^3 == 0, x, algorithm="sympy")
Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))
```




---

archive/issue_comments_017978.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2020-02-22T15:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17978",
    "user": "@videlec"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_017979.json:
```json
{
    "body": "Replying to [comment:22 vdelecroix]:\n> Your solution is somehow complicated and provides a wrong answer. Why not prefer\n> {{{\n> sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm=\"sympy\")\n> Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))\n> }}}\n\nthe syntax you are providing is not user friendly. I would prefer the previous syntax.",
    "created_at": "2020-02-22T17:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17979",
    "user": "@varenyamBakshi"
}
```

Replying to [comment:22 vdelecroix]:
> Your solution is somehow complicated and provides a wrong answer. Why not prefer
> {{{
> sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm="sympy")
> Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))
> }}}

the syntax you are providing is not user friendly. I would prefer the previous syntax.



---

archive/issue_comments_017980.json:
```json
{
    "body": "Replying to [comment:22 vdelecroix]:\n> Your solution is somehow complicated and provides a wrong answer. Why not prefer\n> {{{\n> sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm=\"sympy\")\n> Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))\n> }}}\nI think the syntax simplicity can be judged in the later stages, I do want to ask are you able to obtain the answer from this? because I can't seem to be getting this work, even after a certain modification, such as additional functions for testing and new variable.",
    "created_at": "2020-03-02T15:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17980",
    "user": "@Shlokatadistance"
}
```

Replying to [comment:22 vdelecroix]:
> Your solution is somehow complicated and provides a wrong answer. Why not prefer
> {{{
> sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm="sympy")
> Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))
> }}}
I think the syntax simplicity can be judged in the later stages, I do want to ask are you able to obtain the answer from this? because I can't seem to be getting this work, even after a certain modification, such as additional functions for testing and new variable.



---

archive/issue_comments_017981.json:
```json
{
    "body": "Replying to [comment:24 gh-Shlokatadistance]:\n> Replying to [comment:22 vdelecroix]:\n> > Your solution is somehow complicated and provides a wrong answer. Why not prefer\n> > {{{\n> > sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm=\"sympy\")\n> > Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))\n> > }}}\n> I think the syntax simplicity can be judged in the later stages, I do want to ask are you able to obtain the answer from this? because I can't seem to be getting this work, even after a certain modification, such as additional functions for testing and new variable.\n\nI don't understand your question. `Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))` is the answer. Not in a very nice form, but a valid answer.",
    "created_at": "2020-03-02T15:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17981",
    "user": "@videlec"
}
```

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

archive/issue_comments_017982.json:
```json
{
    "body": "Replying to [comment:25 vdelecroix]:\n> Replying to [comment:24 gh-Shlokatadistance]:\n> > Replying to [comment:22 vdelecroix]:\n> > > Your solution is somehow complicated and provides a wrong answer. Why not prefer\n> > > {{{\n> > > sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm=\"sympy\")\n> > > Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))\n> > > }}}\n> > I think the syntax simplicity can be judged in the later stages, I do want to ask are you able to obtain the answer from this? because I can't seem to be getting this work, even after a certain modification, such as additional functions for testing and new variable.\n> \n> I don't understand your question. `Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))` is the answer. Not in a very nice form, but a valid answer.\n\nAhh my bad, I was trying to obtain a more numeric based answer, I did see that the second statement did resemble the solution",
    "created_at": "2020-03-02T16:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17982",
    "user": "@Shlokatadistance"
}
```

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

archive/issue_comments_017983.json:
```json
{
    "body": "Replying to [comment:26 gh-Shlokatadistance]:\n> Replying to [comment:25 vdelecroix]:\n> > Replying to [comment:24 gh-Shlokatadistance]:\n> > > Replying to [comment:22 vdelecroix]:\n> > > > Your solution is somehow complicated and provides a wrong answer. Why not prefer\n> > > > {{{\n> > > > sage: solve(sin(x<sup>2)/x</sup>3 == 0, x, algorithm=\"sympy\")\n> > > > Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))\n> > > > }}}\n> > > I think the syntax simplicity can be judged in the later stages, I do want to ask are you able to obtain the answer from this? because I can't seem to be getting this work, even after a certain modification, such as additional functions for testing and new variable.\n> > \n> > I don't understand your question. `Complement(ConditionSet(x, Eq(sin(x**2), 0), Complexes), FiniteSet(0))` is the answer. Not in a very nice form, but a valid answer.\n> \n> Ahh my bad, I was trying to obtain a more numeric based answer, I did see that the second statement did resemble the solution\n\nIdeally, it should be possible to convert it to the parametrized set `{sqrt(2*n*pi): n in ZZ \\ {0}}`.",
    "created_at": "2020-03-02T16:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17983",
    "user": "@videlec"
}
```

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

archive/issue_comments_017984.json:
```json
{
    "body": "Yes exactly, from what I reckon the procedure is simply returning like a set, and I think that has to do with the way the conditions were defined. I think by providing a few other cases on the same will help us resolve this issue, something along the lines of\n\n```\ndef condition_set():\n   for x in solution_set # this can be solution set for our trigonometric functions\n       a = solve(the given problem)\n       ans = pi_set(a) # pi_set is the set of our pi value, based on a random value\n      return ans\n```\n\nSomething along these lines , of course this is just a suggestion",
    "created_at": "2020-03-21T19:38:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17984",
    "user": "@Shlokatadistance"
}
```

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

archive/issue_comments_017985.json:
```json
{
    "body": "Moving this ticket to 9.4, as it seems unlikely that it will be merged in 9.3, which is in the release candidate stage",
    "created_at": "2021-04-02T20:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17985",
    "user": "@mkoeppe"
}
```

Moving this ticket to 9.4, as it seems unlikely that it will be merged in 9.3, which is in the release candidate stage



---

archive/issue_comments_017986.json:
```json
{
    "body": "Setting a new milestone for this ticket based on a cursory review.",
    "created_at": "2021-07-19T00:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17986",
    "user": "@mkoeppe"
}
```

Setting a new milestone for this ticket based on a cursory review.



---

archive/issue_comments_017987.json:
```json
{
    "body": "Stalled in `needs_review` or `needs_info`; likely won't make it into Sage 9.5.",
    "created_at": "2021-12-18T19:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2617#issuecomment-17987",
    "user": "@mkoeppe"
}
```

Stalled in `needs_review` or `needs_info`; likely won't make it into Sage 9.5.
