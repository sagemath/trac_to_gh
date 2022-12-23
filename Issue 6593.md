# Issue 6593: WordMorphism: doctest failure in Fedora

Issue created by migration from https://trac.sagemath.org/ticket/6593

Original creator: slabbe

Original creation time: 2009-07-22 16:31:05

Assignee: slabbe

CC:  sage-combinat jsp

Keywords: word morphism

When sage-4.1.1.alpha0 was released (see http://groups.google.com/group/sage-devel/browse_thread/thread/267a2cb90085536b?hl=en), the following problem was reported :


```
Same here on Fedora 10 and Fedora 11, 32 bit.

In addition both in a fresh install and in an upgrade:

sage -t  "devel/sage/sage/combinat/words/morphism.py"
**********************************************************************
File "/home/jaap/Download/sage-4.1/devel/sage/sage/combinat/words/morphism.py", line 616:
     sage: m.extend_by(n)
Expected:
     Morphism from Words over Ordered Alphabet ['a', 'b', 0, 1] to Words over Ordered Alphabet ['a', 'b', 0, 1]
Got:
     Morphism from Words over Ordered Alphabet [0, 1, 'a', 'b'] to Words over Ordered Alphabet [0, 1, 'a', 'b']
**********************************************************************
File "/home/jaap/Download/sage-4.1/devel/sage/sage/combinat/words/morphism.py", line 618:
     sage: n.extend_by(m)
Expected:
     Morphism from Words over Ordered Alphabet ['a', 'b', 0, 1] to Words over Ordered Alphabet ['a', 'b', 0, 1, 5]
Got:
     Morphism from Words over Ordered Alphabet [0, 1, 'a', 'b'] to Words over Ordered Alphabet [0, 1, 5, 'a', 'b']
**********************************************************************
1 items had failures:
    2 of  10 in __main__.example_11
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/jaap/Download/sage-4.1/tmp/.doctest_morphism.py
         [3.2 s]
exit code: 1024

Jaap 
```



---

Attachment


---

Comment by slabbe created at 2009-07-22 17:11:03

Changing status from new to assigned.


---

Comment by slabbe created at 2009-07-22 17:16:11

The patch simply use the print statement which call the `__str__` instead of `__repr__`. The `__str__` sorts the string enumeration before printing it so that it should print the same way on Fedora or on other system.


---

Comment by jsp created at 2009-07-22 21:54:57

After applying the patch in Fedora 11, 32 bit:


```
[jaap@paix sage-4.1.1.alpha0]$ ./sage -t "devel/sage/sage/combinat/words/morphism.py"
sage -t  "devel/sage/sage/combinat/words/morphism.py"       
	 [4.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.9 seconds

```



Jaap


---

Comment by mvngu created at 2009-07-23 06:04:57

Resolution: fixed
