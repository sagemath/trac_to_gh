# Issue 7288: Gomory-Hu Trees

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-25 09:14:14

Assignee: rlm

CC:  abmasse

See http://en.wikipedia.org/wiki/Gomory%E2%80%93Hu_tree.

Gomory-Hu tree are a classical decomposition of the edge connectivity of graphs, and this is not very long to write when one has a function for min-st-cut, which should hopefully be merged soon (ticket #6680)...

Nathann


---

Comment by ncohen created at 2010-01-19 08:29:17

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-01-19 08:29:17

Here it is ! :-)


---

Comment by ncohen created at 2010-02-23 16:31:50

After a few comments from Alexandre... Thanks ! ;-)

Nathann


---

Comment by abmasse created at 2010-02-23 17:44:58

Nathann, there is something really weird: the patch I see with trac is not the same as the one I download. Maybe the server is down ? Could you upload it again just to be sure ? Thanks.


---

Comment by abmasse created at 2010-02-23 20:33:30

Never mind, Firefox wasn't refreshing the page properly.


---

Comment by abmasse created at 2010-02-23 21:29:49

Hello again !
I tested your patch with ``sage -t generic_graph.py graph.py`` and it works ok, but when I type ``sage -t -optional generic_graph.py graph.py``, I get the following:

```
[~/Applications/sage/devel/sage-t7288/sage/graphs]$ sage -t generic_graph.py graph.py
sage -t  "devel/sage-t7288/sage/graphs/generic_graph.py"    
	 [35.4 s]
sage -t  "devel/sage-t7288/sage/graphs/graph.py"            
	 [14.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 50.3 seconds
[~/Applications/sage/devel/sage-t7288/sage/graphs]$ sage -t -optional generic_graph.py graph.py
sage -t -optional "devel/sage-t7288/sage/graphs/generic_graph.py"
1 variables fixed
1 variables fixed
1 variables fixed
1 variables fixed
3 variables fixed
3 variables fixed
3 variables fixed
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t7288/sage/graphs/generic_graph.py", line 3795:
    sage: [cardinal, flow_graph] = g.flow('s','t',integer=True,value_only=False) # optional - requries GLPK or CBC
Exception raised:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_65[9]>", line 1, in <module>
        [cardinal, flow_graph] = g.flow('s','t',integer=True,value_only=False) # optional - requries GLPK or CBC###line 3795:
    sage: [cardinal, flow_graph] = g.flow('s','t',integer=True,value_only=False) # optional - requries GLPK or CBC
      File "/Users/alexandre/Applications/sage/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 3818, in flow
        p.set_objective(flow_sum(x))
      File "mip.pyx", line 615, in sage.numerical.mip.MixedIntegerLinearProgram.set_objective (sage/numerical/mip.c:5170)
    AttributeError: 'int' object has no attribute 'f'
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t7288/sage/graphs/generic_graph.py", line 3796:
    sage: flow_graph.delete_vertices(['s','t'])                                  # optional - requries GLPK or CBC
Exception raised:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_65[10]>", line 1, in <module>
        flow_graph.delete_vertices(['s','t'])                                  # optional - requries GLPK or CBC###line 3796:
    sage: flow_graph.delete_vertices(['s','t'])                                  # optional - requries GLPK or CBC
    NameError: name 'flow_graph' is not defined
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t7288/sage/graphs/generic_graph.py", line 3797:
    sage: len(flow_graph.edges(labels=None))                                     # optional - requries GLPK or CBC
Exception raised:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_65[11]>", line 1, in <module>
        len(flow_graph.edges(labels=None))                                     # optional - requries GLPK or CBC###line 3797:
    sage: len(flow_graph.edges(labels=None))                                     # optional - requries GLPK or CBC
    NameError: name 'flow_graph' is not defined
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-t7288/sage/graphs/generic_graph.py", line 3954:
    sage: g.vertex_disjoint_paths(0,1) # optional - requires GLPK or CBC
Exception raised:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_67[3]>", line 1, in <module>
        g.vertex_disjoint_paths(Integer(0),Integer(1)) # optional - requires GLPK or CBC###line 3954:
    sage: g.vertex_disjoint_paths(0,1) # optional - requires GLPK or CBC
      File "/Users/alexandre/Applications/sage/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 3958, in vertex_disjoint_paths
        [obj, flow_graph] = self.flow(s,t,value_only=False, integer=True, use_edge_labels=False, vertex_bound=True)
      File "/Users/alexandre/Applications/sage/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 3843, in flow
        [p.add_constraint([flow[X][v] for X in g[v]],max=1) for v in g if v!=x and v!=y]
      File "mip.pyx", line 670, in sage.numerical.mip.MixedIntegerLinearProgram.add_constraint (sage/numerical/mip.c:5484)
    AttributeError: 'list' object has no attribute 'f'
**********************************************************************
2 items had failures:
   3 of  12 in __main__.example_65
   1 of   4 in __main__.example_67
***Test Failed*** 4 failures.
For whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_generic_graph.py
	 [37.8 s]
sage -t -optional "devel/sage-t7288/sage/graphs/graph.py"   
	 [17.0 s]
 
----------------------------------------------------------------------
The following tests failed:
```


Note that I installed CBC so this is not an installation problem. I don't really understand where the error comes from. Do you think you could correct it ? As soon as it is done, I'll resume the review.


---

Comment by abmasse created at 2010-02-23 21:29:49

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-02-24 15:38:06

I'm really sorry, but these bugs have also been fixed already... It is done in a very important patch, still waiting for review :

http://trac.sagemath.org/sage_trac/ticket/7311

This can not really be included in the present patch, though... :-/

Nathann


---

Comment by abmasse created at 2010-02-24 16:17:41

Alright, so we have to wait for the ticket #7311 to be reviewed. Could you precise in the description of this ticket which other tickets it depends on ? This way, it will be easier to review.


---

Comment by ncohen created at 2010-02-25 12:31:42

Changing status from needs_work to needs_review.


---

Comment by abmasse created at 2010-03-05 14:53:18

Changing status from needs_review to needs_work.


---

Comment by abmasse created at 2010-03-05 14:53:18

Hello, Nathann !
I looked at your patch and I'm getting more and more used to what it does. I just added a patch that change many different small things in the docstrings and in the code, but these are only formatting changes. I assume you won't agree with all of them (a lot are based on my style of programming, though I tried to respect yours as much as I could ;)) so feel free to put anything back to what it was if you don't agree.

Before I resume the review, I have some comments/questions on your code.

1. Around line 3109 of the file generic_graph.py, you write

```
[p.add_constraint(v[x] + b[x][y] - v[y], min=0, max=0) for (x,y) in g.edges(labels=None)]
```

Maybe I'm wrong, but it seems it would be more readable and more efficient to simply write a `for` loop doing the same work. It is strange to create a list that you won't use anymore in the function. There are two other lines like this in the functions `vertex_cut` and `vertex_cover`. I understand you do it to save a line, but is it really worth it (maybe it is and you know why !) ?

2. The output of the function `edge_cut` and `vertex_cut` are either real numbers or lists. Wouldn't it be better to return real numbers or tuple instead ? There is no reason to use a list representation and tuples are closer to the mathematical notation.

3. I changed a variable with name `l` by `label` since the letter `l` looks very much like the number `1`.

4. In the Gomory-Hu function, you have a parameter `vertices` that you state is not useful for the user : doesn't it mean you should remove it ? I understand that you need this parameter for recursion purposes, but the user shouldn't see it ! You should create a private function doing all the work and another public one calling the private one with the initial parameter set accordingly.

That's all for now. The rest seems fine, but I'll pay more attention to it once you've answered. Don't forget to apply my patch on top of yours before making any change !


---

Comment by ncohen created at 2010-03-06 15:15:00

Hello !!

1. It was indeed just to save a line. At some point, I believed it made the code more readable, as one can directly look at the added constraint, while the "implicit" iterators are written later, but in the end it just looks like a sick way to write it ;-)

2. I really do not mind. So in the end, if you think tuples would be better in this case, this sounds to me like a perfectly good reason to make it so ! ;-)

3. +1

4. Well. I am a bit lazy, and I thought writing a new function, + new docstrings just to avoid one parameter (which appears in the proof of the result, by the way) was a bit too much.. But same thing here : if you think this should be removed, I see no reason why it should stay...

5. Your fixes in the docstrings : I agree with most of them, but I do not know what your way of writing INPUT: sections looks like when the reference is generated. I would like to compare the two :-)

With the comments you made, it sounds like I should rewrite some parts of the code and sen a new patch, merged with the one you sent. Before doing it, can you tell me whether you have "pending" modifications on this patch ? If so, could you update your patch ? I will then take it, mix it with mine, and bring to the code the modifications you requested, but it would not be a good idea to do it now if you are also working on the same parts of the code...

Thank you again ! :-)

Nathann


---

Comment by abmasse created at 2010-03-06 15:36:48

I won't touch the patch anymore. Moreover, instead of submitting a completely new one, you can simply add one on top of mine.

If I have to make any other change, I'll do it after you've submitted a new patch.

I think next time will be a positive review. Sorry for making you work. As for item 4, I know it's time consuming to write two complete doctests, but it is really more readable for the user.


---

Comment by ncohen created at 2010-03-08 17:18:12

What about this one ? :-)

(it includes your fixes)

Nathann


---

Comment by ncohen created at 2010-03-08 17:18:12

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-03-08 23:42:32

This one is a new update. It includes the previous one, plus the bugfixes you requested. It is to be applied after #7311, which also fixed several errors.

With those two applied, everything should test nicely :-)

Nathann


---

Comment by abmasse created at 2010-03-11 00:22:22

Great ! All non optional tests passed, as well as optional ones ! You really fixed every error. I will give another look to your patch tomorrow, but this should easily be a positive review.

Thank you for your patience !


---

Comment by abmasse created at 2010-03-11 15:52:59

Some questions/comments:

1. You said you merged my patch with yours, but there seems to miss many modifications I did on the docstring. Does it mean that you don't agree with it ?

2. Following 1, I think you should at least add an OUTPUT field, especially for the functions `edge_cut`, `vertex_cut`. It is important that the user knows what he's going to have returned when using your functions.

3. The same comment about returning tuples instead of lists. I agree with you that this is minor, but I think there is a reason why the two data structures exist in Python. Tuples seem more immutable while lists are dynamical. Here, you return fixed things that shouldn't be modified.

4. I insist on the point that the `vertices` parameter should be hidden. I think this is important... the signature of the function is a very important feature to understand what the function does.

If you agree with that and since you've put a lot of work since the beginning, I have no problem at all to change all these by myself.

Another remark : when merging my changes, it's better to create another patch that applies on top of your changes and on mine at the same time. This way, one can visualize more easily what each of us did and when. This can very simply realized with mercurial. You only need to apply, say, the two first patches, and then create a new patch with `hg qnew` that applies on top of both the first patches.

So as soon as you tell me that I can make some changes, I'll do them, but I don't want to work for nothing, so I'll wait till you answer.

Note that I tested the new functions and I agree with what they do, everything works fine, it's just the documentation and some code choices that I want to discuss.


---

Comment by ncohen created at 2010-03-11 16:55:20

Hem.... How can I say this ?....

I did not ignore your remarks... If I remember correctly, I addressed them all, including the documentation and your fixes... I just uploaded a wrong file, or did not generate the patch properly.... And I had the good idea to delete the branch containing the modifications since, which means I'm in for writing them again ^^;

I'm really sorry, you will have what you asked for as soon as possible.

Nathann


---

Comment by ncohen created at 2010-03-11 16:55:26

Changing status from needs_review to needs_work.


---

Comment by abmasse created at 2010-03-11 19:23:05

Don't worry about that !

If I may suggest, maybe you could get back your initial patch and apply mine (which is still available on trac). Then you could only add the few doctests that you added to fix the failing tests.


---

Comment by ncohen created at 2010-03-12 08:39:01

Hello !!!

Here is the patch I should have sent you last time... Actually, I did the job a bit better this time, as I replaced each occurence of the lists [p.add_constraint...] I could find in the code, so there should be none left :-)

It still fixes all doctest bugs, and it splits the gomory_hu function, and it includes your patch, and it should be fine, though as I told you over email I made a mistake when applying the patches and I can not give you, as you asked, a patch to apply on top of yours, but another patch with contains all of it.. :-/

I'll read hg's manual again, just to be sure ;-)

Nathan


---

Comment by ncohen created at 2010-03-12 08:39:01

Changing status from needs_work to needs_review.


---

Attachment

Minor doc fixes -- apply on top of Nathann's patch


---

Comment by abmasse created at 2010-03-12 23:40:14

I reviewed the patch for what I expect will be the last time ;)

I did the following tests. First, I compiled from source two versions of sage-4.3.3. Then I installed CBC and GLPK on one of the versions (call this version the `optional` one) while not installing it on the other (call that one `basic`). Then, I applied the two patches of #7311 on both versions and Nathann's patch for #7288.

I tested all sage with the command `sage -testall` on the `basic` version. All tests passed. On the other hand, I tested both the `sage/numerical` and `sage/graphs` folders with the command `sage -t -optional`. Once again, all tests passed ! (I also had to install the package Nauty which is also needed for optional tests).

Finally, I made some minor changes, touching only the documentation and some comments in the code. I restested all and the results were the same. I also looked at the documentation generated by Sphinx. Everything seemed fine.

Note that other part of codes were also modified by Nathann's patch, but it only concerns doctests that were failing, so that the graph folder will be stable in Sage as soon as #7311 and #7288 are merged ! (There were some optional tests failing even before applying any patch !!!)

To conclude, I give this ticket a positive review, as soon as Nathann confirms he agrees with my changes.

Great work !


---

Comment by ncohen created at 2010-03-13 07:54:07

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-03-13 07:54:07

I see no reason to refuse any of them ! Thank you veeeeeery much for your help with this patch.. Not all of them can claim they have been so thoroughly tested :-)

Nathann


---

Comment by jhpalmieri created at 2010-04-15 05:58:32

Merged in 4.4.alpha0:

 - trac_7288.patch
 - trac_7288_review-abm.patch


---

Comment by jhpalmieri created at 2010-04-15 05:58:32

Resolution: fixed
