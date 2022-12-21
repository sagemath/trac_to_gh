# Issue 9715: Failing doctest in even_hole_free

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-08-10 03:37:28

Assignee: jason, ncohen, rlm

CC:  dkirkby jason mpatel

As reported on :

http://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a

The only random part being the graph generation, it shouldn't be hard to find a workaround....


```
>> sage -t  devel/sage-main/sage/graphs/graph.py
>> **********************************************************************
>> File "/Volumes/E/sage-4.5.2.rc0/devel/sage-main/sage/graphs/graph.py",
>> line 1347:
>>     sage: cycle.order() % 2 == 0
>> Exception raised:
>>     Traceback (most recent call last):
>>       File "/Volumes/E/sage-4.5.2.rc0/local/bin/ncadoctest.py", line
>> 1231, in run_one_test
>>         self.run_one_example(test, example, filename, compileflags)
>>       File "/Volumes/E/sage-4.5.2.rc0/local/bin/sagedoctest.py", line
>> 38, in run_one_example
>>         OrigDocTestRunner.run_one_example(self, test, example,
>> filename, compileflags)
>>       File "/Volumes/E/sage-4.5.2.rc0/local/bin/ncadoctest.py", line
>> 1172, in run_one_example
>>         compileflags, 1) in test.globs
>>       File "<doctest __main__.example_6[9]>", line 1, in <module>
>>         cycle.order() % Integer(2) == Integer(0)###line 1347:
>>     sage: cycle.order() % 2 == 0
>>     AttributeError: 'bool' object has no attribute 'order' 
```


Nathann



---

Attachment


---

Comment by ncohen created at 2010-08-10 04:15:53

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-08-10 04:15:53

With this, the docstring does not depend on any -- possibly rare -- probabilistic event. Good to know that the docstrings reports errors that do not appear on 100 000 trials though. `:-D`

Nathann


---

Comment by ncohen created at 2010-10-19 14:41:52

This ticket is now invalid because of #10081 and #9422

Nathann


---

Comment by mpatel created at 2010-10-19 21:54:43

Resolution: duplicate


---

Comment by mpatel created at 2010-10-19 21:54:43

Replying to [comment:2 ncohen]:
> This ticket is now invalid because of #10081 and #9422

Also related: #9925.
