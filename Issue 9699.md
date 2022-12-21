# Issue 9699: Barycentric embedding for planar graphs.

Issue created by migration from Trac.

Original creator: fidelbarrera

Original creation time: 2010-08-06 19:24:42

Assignee: jason, ncohen, rlm

CC:  rlm boothby

Positions of vertices returned by planar_layout can be set to have the vertices of an equilateral triangle as exterior vertices.


---

Comment by fidelbarrera created at 2010-08-06 19:26:33

Changing status from new to needs_review.


---

Comment by fidelbarrera created at 2010-08-07 00:20:14

Updated patch, it includes an example.


---

Attachment


---

Comment by rlm created at 2010-08-07 12:00:41

I wonder if the default for `barycentric` shouldn't be True instead of False. It looks a bit nicer that way, so why not make it the default?


---

Attachment

Please apply instead of trac_9699.patch.


---

Comment by fidelbarrera created at 2010-08-08 02:02:42

Replying to [comment:3 rlm]:
> I wonder if the default for `barycentric` shouldn't be True instead of False. It looks a bit nicer that way, so why not make it the default?

The option `barycentric` is now set to True by default.


---

Comment by fidelbarrera created at 2010-08-08 02:06:38

Replying to [comment:3 rlm]:
> I wonder if the default for `barycentric` shouldn't be True instead of False. It looks a bit nicer that way, so why not make it the default?

Sorry, I forgot to be more specific. Please apply trac_9699_2.patch instead of trac_9699.patch.


In trac_9699_2.patch the option `barycentric` is now set to be True by default.


---

Comment by ncohen created at 2010-09-05 07:49:07

Well, if such an option is the default, shouldn't we just replace the actual code with it ? As these barycentric coordinates are as valid as the previous ones in the general case, I except the code used by barycentric = False never to be used again... `:-p`

What about just replacing the current code to compute barycentric coordinates, and add this information as notes in the documentation ?

Nathann


---

Comment by ncohen created at 2010-09-05 07:49:07

Changing status from needs_review to needs_info.


---

Comment by fidelbarrera created at 2010-09-13 01:45:28

Replying to [comment:6 ncohen]:

> Well, if such an option is the default, shouldn't we just replace the actual code with it ?

I think the previous implementation features interesting properties. It provided a straightline embedding in an O(n) by O(n) grid, so in particular all the coordinates are integers. Would you still suggest to replace the code completely?

Fidel


---

Comment by fidelbarrera created at 2010-09-13 01:45:28

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2010-09-13 07:08:42

> I think the previous implementation features interesting properties. It provided a straightline embedding in an O(n) by O(n) grid, so in particular all the coordinates are integers. Would you still suggest to replace the code completely?

No, not anymore... But now I would suggest to mention these properties in the docstring. Sorry for asking it this late, but I am concerned about avoiding to have in Sage at the same time two pieces of code doing the same thing in different ways, and writing it in such a way that one of them is never used.. That's why I wondered whether it would be better to completely replace the current implementation with yours instead of having two version. If the current version has properties that yours do not have, then you are right : it should remain available, but this is not very useful if nobody knows these properties exists.... Hence, where you documented the keyword ``barycentric`` 


```
- ``barycentric`` - whether or not to use barycentric coordinates. 
```


it would be nice to also mention that setting it to ``None`` means having an embedding in a O(n)*O(n) grid with integer coordinates, as you just taught me.. Otherwise it's very unlikely people would disable a feature with no computation time to earn...nothing `:-)`

Nathann


---

Attachment

Please apply instead of previous patches.


---

Comment by fidelbarrera created at 2010-09-22 04:09:08

Replying to [comment:8 ncohen]:

> But now I would suggest to mention these properties in the docstring.

These properties are now mentioned in the docstring :)

Fidel


---

Comment by ncohen created at 2010-09-22 08:14:46

Hello !!

I noticed a typo in your patch 

```
then coordinates will bi in the grid. 
```


So I first wrote a small one to fix it, then ended up fixing one or two other docstrings, or adding to them the information you had put in the first description or ``barycentric``.. Well, if somebody can test my patch, he can set this ticket to "positive review", as yours is good to go !

Thanksssssssssssssss ! :-)

Nathann


---

Attachment

Doctest fail:


```
sage -t -long ./sage/graphs/generic_graph.py
**********************************************************************
File "/home/rlmill/sage-4.6/devel/sage-main/sage/graphs/generic_graph.py", line 2620:
    sage: g.layout(layout = "planar", save_pos = True)
Expected:
    {0: [1, 1], 1: [2, 2], 2: [3, 2], 3: [1, 4], 4: [5, 1], 5: [0, 5], 6: [1, 0]}
Got:
    {0: (-0.433012701892, -0.25), 1: (1.11022302463e-16, -7.40148683083e-17), 2: (0.144337567297, 0.25), 3: (0.433012701892, -0.25), 4: [0.0, 1.0], 5: [0.866025403784, -0.5], 6: [-0.866025403784, -0.5]}
**********************************************************************
```


Also, all of the positions should be the same format: here some are tuples and others are lists.


---

Comment by rlm created at 2010-11-11 13:15:42

Changing status from needs_review to needs_work.


---

Attachment

Please apply instead of previous patches.


---

Comment by fidelbarrera created at 2010-11-21 04:04:09

Changing status from needs_work to needs_review.


---

Comment by fidelbarrera created at 2010-11-21 04:04:09

Hello,

The patch file trac_9699_4.patch includes a fix to the doctest fail. It also includes a fix to the problem having tuples and lists for the positions. Now, all of the positions are lists.

Fidel


---

Comment by rlm created at 2010-11-26 16:23:57

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-26 22:25:49

Has this been tested on various systems?  The kind of output like

```
{0: [0.0, 1.0], 1: [0.866025403784, -0.5], 2: [-0.866025403784, -0.5], 3: [0.433012701892, -0.25], 4: [-0.288675134595, -1.85037170771e-16], 5: [0.288675134595, 3.70074341542e-17], 6: [0.144337567297, 0.25]}
```

has a tendency of being quite system-dependent because of precision issues.

In any case, if all you did was add an option, why did the output change?


---

Comment by jdemeyer created at 2010-11-26 22:25:49

Changing status from positive_review to needs_info.


---

Comment by fidelbarrera created at 2010-11-26 23:16:13

Replying to [comment:15 jdemeyer]:
> Has this been tested on various systems?  
I have not tested it on various systems.

> In any case, if all you did was add an option, why did the output change?

The option barycentric was no just added, it was made the default option, as suggested by rlm in 

[http://trac.sagemath.org/sage_trac/ticket/9699?replyto=15#comment:3](http://trac.sagemath.org/sage_trac/ticket/9699?replyto=15#comment:3)


---

Comment by rlm created at 2010-11-26 23:39:19

Replying to [comment:15 jdemeyer]:
> {{{
> {0: [0.0, 1.0], 1: [0.866025403784, -0.5], 2: [-0.866025403784, -0.5], 3: [0.433012701892, -0.25], 4: [-0.288675134595, -1.85037170771e-16], 5: [0.288675134595, 3.70074341542e-17], 6: [0.144337567297, 0.25]}
> }}}

Jeroen is right. You should replace things like `0.866025403784` with `0.86...` so that numerical issues don't crop up.


---

Comment by rlm created at 2010-11-26 23:39:19

Changing status from needs_info to needs_work.


---

Comment by fidelbarrera created at 2010-11-27 04:31:22

Please apply instead of previous patches.


---

Comment by fidelbarrera created at 2010-11-27 04:33:49

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:17 rlm]: 
> Jeroen is right. You should replace things like `0.866025403784` with `0.86...` so that numerical issues don't crop up. 

Replaced things like `0.866025403784` with `0.86...`.

Please see trac_9699_5.patch instead of previous versions.


---

Comment by rlm created at 2010-11-28 16:32:57

Okay, I tested all long doctests on a 64 bit Linux machine, and all passed. I also tested long doctests in `sage/graphs` on a 32 bit Linux machine, and again all tests pass. Things look good.


---

Comment by rlm created at 2010-11-28 16:32:57

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-11-28 16:59:57

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-11-28 16:59:57

It seems I pressed submit too soon. Indeed all tests pass on the 64 bit system.

However on the 32-bit system, things seem to freeze at the following test:

```
Trying:
    g = graphs.BalancedTree(Integer(3),Integer(4))###line 2658:_sage_    >>> g = graphs.BalancedTree(3,4)
Expecting nothing
ok
Trying:
    g.set_planar_positions(test=True)###line 2659:_sage_    >>> g.set_planar_positions(test=True)
Expecting:
    True
```



---

Comment by rlm created at 2010-11-28 17:12:13

Ugh. Once again I spoke too soon.

The real problem is just that the doctests take *much* longer after the patch than before.

On the 32 bit system it went from 243.2 s for `generic_graph.py` up to 623.8 s after the patch.

On the (much faster) 64 bit system it was 130.4 s before and 441.2 s after.

This definitely counts as a regression, and I can't let things through with so much of a slowdown.
