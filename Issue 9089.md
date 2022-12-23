# Issue 9089: Graphics3dGroup __add__ modifies its arguments

Issue created by migration from https://trac.sagemath.org/ticket/9089

Original creator: jason

Original creation time: 2010-05-29 20:21:42

Assignee: AlexGhitza

CC:  robertwb mhampton kcrisman slabbe ppurka

In an attempt to optimize, in some cases the __add__ method of Graphics3dGroup modifies its arguments instead of returning a new Graphics3dGroup object.  This breaks the user expectation, as illustrated below:


```
a=point3d([1,0,0])+point3d([0,1,0])
b=point3d([0,0,1])
a # shows 2 points
a+b # shows all 3 points
a # Now this shows 3 points!!!
```


The attached patch deletes the offending optimization.  If fast summing is needed, then the user can either create a Graphics3dGroup object themselves, or use something like `sage.misc.misc.balanced_sum`


---

Comment by jason created at 2010-05-29 20:21:55

Changing component from algebra to graphics.


---

Comment by jason created at 2010-05-29 20:21:55

Changing assignee from AlexGhitza to jason, was.


---

Attachment

Credit goes to Ben Woodruff for reporting this issue.


---

Comment by jason created at 2010-05-29 20:42:55

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-06-01 09:50:05

Do you have any stats on how much this affects performance?


---

Comment by jason created at 2010-06-02 20:26:48

Before patch:


```
sage: from sage.misc.misc import balanced_sum
sage: from sage.plot.plot3d.base import Graphics3dGroup
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=sum(lines)
625 loops, best of 3: 82.1 µs per loop
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=balanced_sum(lines)
625 loops, best of 3: 455 µs per loop
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=Graphics3dGroup(lines)
625 loops, best of 3: 179 µs per loop
```



After patch:


```

sage: from sage.misc.misc import balanced_sum
sage: from sage.plot.plot3d.base import Graphics3dGroup
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=sum(lines)
625 loops, best of 3: 1.48 ms per loop
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=balanced_sum(lines)
625 loops, best of 3: 1.45 ms per loop
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=Graphics3dGroup(lines)
625 loops, best of 3: 180 µs per loop

```


So, as could be expected, performance of sum is impacted quite a bit.  However, I would still say that the current behavior is wrong, and correctness trumps speed, especially if the overall total speed is still quite fast.


---

Comment by jason created at 2010-06-02 20:30:45

Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.


---

Comment by robertwb created at 2010-06-02 20:50:20

Replying to [comment:5 jason]:
> Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.

That's a great idea! (Certainly a new ticket.)


---

Comment by jason created at 2010-06-02 20:53:36

Replying to [comment:6 robertwb]:
> Replying to [comment:5 jason]:
> > Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.
> 
> That's a great idea! (Certainly a new ticket.)

Actually, I just checked, and something like it is already being done.  If you do sum(something,...), then if something has a sum method, it is called: something.sum(...).  Of course, this won't work with lists or generators.

Anyways, feel free to review this ticket!


---

Comment by jason created at 2010-06-02 22:26:08

Okay, the sum stuff is at #9115


---

Comment by jason created at 2010-06-15 14:14:00

ping about reviewing this bug fix.  There has been several times in the past few weeks that this bug has caught me.


---

Comment by kcrisman created at 2010-06-15 17:08:03

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-06-15 17:08:03

Looks ok.  

```
sage: len(G)
2
```

in the old example as desired, inheritance is correct.  Currently building doc to make sure looks right... okay. Should `:meth:__add__` point to the method in `sage.plot.plot3d.base.Graphics3d`via hyperlink?  Otherwise positive review, though of course the speed thing would be great to take care of if #9115 becomes available.


---

Comment by davidloeffler created at 2010-06-30 21:33:55

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-06-30 21:33:55

I'm getting a doctest failure with this patch on 4.5.alpha1:

```
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot.py", line 428:
    sage: g.show()
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-4.5.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[11]>", line 1, in <module>
        g.show()###line 428:
    sage: g.show()
      File "base.pyx", line 1081, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:10184)
      File "base.pyx", line 524, in sage.plot.plot3d.base.Graphics3d.tachyon (sage/plot/plot3d/base.c:4785)
      File "base.pyx", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)
      File "base.pyx", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)
      File "base.pyx", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)
      File "base.pyx", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13387)
    TypeError: reduce() of empty sequence with no initial value
**********************************************************************
```


Also, if I install this together with the patches at #9066 I get a bunch more failures coming in:

```
sage -t  -long devel/sage/sage/plot/plot3d/shapes2.py # 5 doctests failed
```



---

Attachment

apply on top of previous patches


---

Comment by jason created at 2010-09-07 17:54:37

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-09-07 17:54:37

The errors should be taken care of now: on 4.5.2, plot/*.py* and plot/plot3d/*.py* all pass doctests.  Apply the two patches on top of each other.


---

Comment by jason created at 2010-09-22 06:13:24

Ping to someone to look at this.  I believe I corrected all of the failing doctests.


---

Comment by davidloeffler created at 2010-09-22 09:29:17

Looks OK to me. I don't use the graphics code myself; but it had a positive review before I grumbled about failing doctests, and I can confirm that the doctests are now fixed, so I feel that merits giving it a positive review again.


---

Comment by davidloeffler created at 2010-09-22 09:29:17

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-09-22 15:33:25

Thanks.  This bug hit me again yesterday.


---

Comment by davidloeffler created at 2010-09-23 12:31:40

Hang on a minute. I was lazy and ran long doctests on graphics and only short doctests on everything else, so I missed a weird side-effect of this patch: if you install the two patches above on vanilla 4.6.alpha1 and do

```
sage -t -long sage/combinat/root_system/weyl_group.py
```

then you get an infinite loop:

```
File "/storage/masiao/sage-4.6.alpha1/devel/sage-hacking/sage/combinat/root_system/weyl_group.py", line 27:
    sage: d.show3d(color_by_label=True, edge_size=0.01, vertex_size=0.03) #long time (less than one minute)
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-4.6.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[7]>", line 1, in <module>
        d.show3d(color_by_label=True, edge_size=RealNumber('0.01'), vertex_size=RealNumber('0.03')) #long time (less than one minute)###line 27:
    sage: d.show3d(color_by_label=True, edge_size=0.01, vertex_size=0.03) #long time (less than one minute)
      File "/storage/masiao/sage-4.6.alpha1/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 12407, in show3d
        color_by_label=color_by_label, **kwds).show()
      File "base.pyx", line 1048, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:9726)
      File "base.pyx", line 953, in sage.plot.plot3d.base.Graphics3d._process_viewing_options (sage/plot/plot3d/base.c:9519)
      File "base.pyx", line 198, in sage.plot.plot3d.base.Graphics3d._determine_frame_aspect_ratio (sage/plot/plot3d/base.c:3307)
      File "base.pyx", line 214, in sage.plot.plot3d.base.Graphics3d._safe_bounding_box (sage/plot/plot3d/base.c:3460)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
[ ... ]
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12234)
    RuntimeError: maximum recursion depth exceeded in __subclasscheck__
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_weyl_group.py
         [41.9 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-hacking/sage/combinat/root_system/weyl_group.py"
Total time for all tests: 41.9 seconds
```


Apologies for my sloppiness in not having caught this bug earlier.


---

Comment by davidloeffler created at 2010-09-23 12:31:40

Changing status from positive_review to needs_work.


---

Comment by jason created at 2010-09-23 12:45:33

Replying to [comment:16 davidloeffler]:


> Apologies for my sloppiness in not having caught this bug earlier.

Well, please accept my apologies for not thinking we had to check ptestlong.  I'll fix it and run ptestlong before posting a new patch!

Thanks for your patience.


---

Comment by chapoton created at 2015-03-18 20:54:46

solved in #17258


---

Comment by chapoton created at 2015-03-18 20:54:46

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2015-03-18 21:11:19

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-03-21 09:30:42

Resolution: fixed
