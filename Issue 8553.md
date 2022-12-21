# Issue 8553: Minor bugs in solve() if dictionary result requested

Issue created by migration from Trac.

Original creator: leif

Original creation time: 2010-03-17 15:39:40

Assignee: leif

CC:  schilly mhansen burcin jason kcrisman

Keywords: solve, solution_dict

solve() raises an index error on empty solutions if solution dictionary was requested; returns empty list instead of empty dictionary in other cases.


---

Comment by leif created at 2010-03-17 15:54:04


```
sage: x=var('x')
sage: x
x
sage: solve([0==1], x, solution_dict = True)
[]
sage: solve([x==0, 0==1], x, solution_dict = True)
[]
sage: solve([(x == 0), (x == 1)], x, solution_dict = True)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
...
IndexError: list index out of range
```



---

Comment by leif created at 2010-03-17 16:39:28

Changing status from new to needs_review.


---

Attachment


---

Comment by schilly created at 2010-03-17 17:41:08

Changing status from needs_review to positive_review.


---

Comment by schilly created at 2010-03-17 17:41:08

patch works for 4.3.4.rc0 and looks fine. i would just like to see a "TESTS::" header for the additional doctests and a line referring to this ticket, smth. like "this fixes the problem reported in ticket #8553".


---

Comment by mhansen created at 2010-03-17 19:49:10

Style-wise, this


```
{} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
```


should be


```
{} if kwds.get('solution_dict', False) is True else []
```



---

Comment by mhansen created at 2010-03-17 19:57:43

Or even 


```
{} if kwds.get('solution_dict', False) else []
```


if you want to be a bit more lax with inputs.


---

Comment by leif created at 2010-03-17 20:55:27

Replying to [comment:6 mhansen]:
> Or even 
> 
> {{{
> {} if kwds.get('solution_dict', False) else []
> }}}
> 
> if you want to be a bit more lax with inputs.

Please correct me, but I do not see any difference to your former suggestion.
In what sense does this relax the inputs?


---

Comment by mhansen created at 2010-03-17 20:58:37

In the first cases, passing in solution_dict=1 would be the same as passing in solution_dict=False.  In the second case, solution_dict=1 would be the same as solution_dict=True.


---

Comment by leif created at 2010-03-17 21:11:51

Replying to [comment:8 mhansen]:
> In the first cases, passing in solution_dict=1 would be the same as passing in solution_dict=False.  In the second case, solution_dict=1 would be the same as solution_dict=True.


That's perhaps what one would expect.

But `solution_dict=1` evaluates to `True` in all versions, while `solution_dict=42` surprisingly evaluates to `False`, even in your latter version.


---

Comment by mhansen created at 2010-03-17 21:24:39


```
sage: kwds = {'solution_dict': 42}
sage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
{}
sage: {} if kwds.get('solution_dict', False) is True else []
[]
sage: {} if kwds.get('solution_dict', False) else []
{}
sage: kwds = {'solution_dict': 42r}
sage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
[]
sage: {} if kwds.get('solution_dict', False) is True else []
[]
sage: {} if kwds.get('solution_dict', False) else []
{}
```



---

Comment by leif created at 2010-03-17 21:28:32

I have to corrct myself: `1` gives `True` only in the first (because of `==` comparison) and the last implementation.


---

Comment by leif created at 2010-03-17 21:43:57


```
sage: kwds = {'solution_dict': 42}
sage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
[]
sage: {} if kwds.get('solution_dict', False) is True else []
[]
sage: {} if kwds.get('solution_dict', False) else []
{}
sage: sage: kwds = {'solution_dict': 42r}
sage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
[]
sage: {} if kwds.get('solution_dict', False) is True else []
[]
sage: {} if kwds.get('solution_dict', False) else []
{}

```

4.3.4.alpha1

Notice the difference in the first case; 42 is not true for me ;-)


---

Comment by leif created at 2010-03-17 21:52:41


```
sage: kwds = {'solution_dict': 42}                                         
sage: print kwds                  
{'solution_dict': 42}
sage: sage: kwds = {'solution_dict': 42r}                                  
sage: print kwds                         
{'solution_dict': 42}

```

Preparser issue?


---

Comment by schilly created at 2010-03-17 22:00:08

Replying to [comment:13 leif]:
> Preparser issue?

no, that's a feature and notice there is an "r" behind the 42! 

```
sage: preparse('42r + 42')
'42 + Integer(42)'
```



---

Comment by leif created at 2010-03-17 23:21:01

Replying to [comment:14 schilly]:

Ok, but I still don't understand the different behavior of Mike's and my machine:


```
sage: kwds = {'solution_dict': 42}
sage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
```


While Mike gets the empty set, I get the empty list, and if the doctests passed on your 4.3.4.rc0, your version behaves like my 4.3.4.alpha1 (on Ubuntu 9.04 x86_64), because I added the `solution_dict=42` case with an expected empty *list*.


---

Comment by leif created at 2010-03-18 00:10:29

Replying to [comment:15 leif]:

I still get the empty *list* for the code above with 4.3.4.rc0 (just built on Ubuntu 9.04 x86_64), but I'll update the patch to the latter suggested version (with the 42-testcase changed, i.e. *inverted*!).


---

Attachment

Apply *either* the first *or* the second patch, *not both*.


---

Comment by burcin created at 2010-03-18 16:42:30

Changing status from positive_review to needs_work.


---

Comment by burcin created at 2010-03-18 16:42:30

AFAICT, `solve` returns a list of possible solutions to the given equality. When the `solution_dict` parameter is `True`, this list is populated by dictionaries instead of symbolic relations.

With this reasoning the current behavior of returning an empty list if we can't find any solutions even if the `solution_dict` parameter is `True` seems correct to me.

IMHO, the only thing that needs to be fixed is the `IndexError` when there is no solution. Comments?


---

Comment by schilly created at 2010-03-18 17:41:37

Replying to [comment:18 burcin]:
> IMHO, the only thing that needs to be fixed is the `IndexError` when there is no solution. Comments?

Yes please, I don't get it why this is so complicated! All unrelated issues should be discussed off-ticket.


---

Comment by leif created at 2010-03-18 17:43:18

Replying to [comment:18 burcin]:
> AFAICT, `solve` returns a list of possible solutions to the given equality. When the `solution_dict` parameter is `True`, this list is populated by dictionaries instead of symbolic relations.
> 
> With this reasoning the current behavior of returning an empty list if we can't find any solutions even if the `solution_dict` parameter is `True` seems correct to me.

That's really a matter of design; one could equally well specify the function to return a list containing an empty dictionary in that case; i.e., the current specification is not precise (and that's not the only one).

But you're right, unless we change the _informal_ "prototype" (its signature), it should in any case return a *_list* of something_.


I'd change the patch to reflect whatever behavior you want... ;-)

-Leif


---

Comment by leif created at 2010-03-18 17:47:17

Replying to [comment:19 schilly]:
> Replying to [comment:18 burcin]:
> > IMHO, the only thing that needs to be fixed is the `IndexError` when there is no solution. Comments?
> 
> Yes please, I don't get it why this is so complicated! All unrelated issues should be discussed off-ticket.

So we'd change the ticket description and the patch to only address and fix the index error?

Ok for me.


---

Comment by burcin created at 2010-04-05 13:20:28

Hi Leif,

Replying to [comment:21 leif]:
> So we'd change the ticket description and the patch to only address and fix the index error?
> 
> Ok for me.

Can you provide a patch that fixes the `IndexError` problem? If we get this reviewed in the next few days it might still make it to the next release.


---

Attachment


---

Comment by leif created at 2010-04-06 05:11:20

Sorry, unable to delete the previous patches; *apply only the last one*.

 * `IndexError` issue fixed.
 * Type of parameter `solution_dict` relaxed as suggested by Mike Hansen (now consistent; also in `expression.pyx`/`Expression.solve()`).
 * (More) Doctests added.
 * Description made more clear. Some typos fixed.


---

Comment by leif created at 2010-04-06 05:11:20

Changing status from needs_work to needs_review.


---

Attachment

Rebase on sage-4.4.alpha0.


---

Comment by timdumol created at 2010-04-18 07:57:00

Works perfectly after this rebase. Positive review, but someone has to review this rebase first.


---

Attachment

revised version of Leif's patch


---

Comment by burcin created at 2010-05-05 01:42:53

reviewer's patch


---

Attachment

The doctests for using values that are taken to be True in Leif's patch added a few extra seconds to the time to test `sage/symbolic/relation.py`. I uploaded a revised version of Leif's patch, attachment:trac_8553_solve_fix_IndexError.3.patch, which cuts down on these examples.

attachment:trac_8553-review.patch adds a new test condition to check if the first argument is a list, after the statement that handles a single symbolic expression.

Can someone review my patch?


---

Comment by leif created at 2010-05-05 12:01:21

Replying to [comment:26 burcin]:
> The doctests for using values that are taken to be True in Leif's patch added a few extra seconds to the time to test `sage/symbolic/relation.py`.

:-) Adding `# optional` or `# long` would have been possible, too.

(Now the tests of Python `int`s vs. Sage's `Integer`s are omitted.)


---

Comment by burcin created at 2010-05-06 16:59:39

Replying to [comment:27 leif]:
> Replying to [comment:26 burcin]:
> > The doctests for using values that are taken to be True in Leif's patch added a few extra seconds to the time to test `sage/symbolic/relation.py`.
> 
> :-) Adding `# optional` or `# long` would have been possible, too.
> 
> (Now the tests of Python `int`s vs. Sage's `Integer`s are omitted.)

Since they weren't testing the functionality of `solve()`, but a convenience in Python, I think it's OK if they are not so extensive. I run doctests on these files very often, so it's rather important that even the long tests take a reasonable time.

Can you review my changes BTW?


---

Comment by leif created at 2010-05-26 16:44:47

Changing keywords from "solve, solution_dict" to "solve, solution_dict, beginner".


---

Comment by leif created at 2010-06-07 17:04:36

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-06-07 17:04:36

Replying to [comment:28 burcin]:
> Can you review my changes BTW? 

`m.to_poly_solve(variables)` might be called twice.

Btw, I think the patch should be finally reviewed by someone else, not me, as I'm one of the authors.


---

Comment by kcrisman created at 2011-05-18 13:15:02

Just for reference, see [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/d54b283435a8ed4b/1eab51e2561da568) for another report of this.


---

Comment by kcrisman created at 2011-05-18 16:04:43

Changing status from needs_work to positive_review.


---

Comment by kcrisman created at 2011-05-18 16:04:43

Replying to [comment:30 leif]:
> Replying to [comment:28 burcin]:
> > Can you review my changes BTW? 
> 
> `m.to_poly_solve(variables)` might be called twice.

It is, but only in the unusual situation that Maxima's solve gave an error and `to_poly_solve` gave the empty list.  More to the point, this was there before, and should be a different ticket.

> Btw, I think the patch should be finally reviewed by someone else, not me, as I'm one of the authors.
>  
Not at all - usually it is appropriate to review a reviewer patch.  This reviewer patch really is pretty minimally invasive, and in fact provides a much more useful error message.

It is true that 

```
sage: solve(x==1,x,solution_dict=int(3))
[{x: 1}]
sage: solve([0==1],x,solution_dict=int(3))
[]
sage: solve(0==1,x,solution_dict=int(3))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/karl-dietercrisman/Downloads/sage-4.7.rc1/<ipython console> in <module>()

/Users/karl-dietercrisman/Downloads/sage-4.7.rc1/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in solve(f, *args, **kwds)
    652 
    653     if not isinstance(f, (list, tuple)):
--> 654         raise TypeError("The first argument must be a symbolic expression or a list of symbolic expressions.")
    655 
    656     if len(f)==1 and is_Expression(f[0]):

TypeError: The first argument must be a symbolic expression or a list of symbolic expressions.
```

which is not ideal.  However, this is still better behavior than the mysterious message about bools and len before, so that could be another ticket.  

In any case, this (somewhat surprisingly) still applies fine to 4.7.rc2!  And does what it says.  And passes tests. Positive review.


---

Comment by jdemeyer created at 2011-06-01 07:16:08

Resolution: fixed


---

Comment by leif created at 2011-07-22 19:57:05

For the sagebot:

Apply [attachment:trac_8553_solve_fix_IndexError.3.patch] [attachment:trac_8553-review.patch]
