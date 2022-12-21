# Issue 4600: followup issue on sage -only_optional

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-24 00:52:26

Assignee: mabshoff


```
16:47 < wstein> mabshoff -- there is definitely an "issue" with only-optional.
16:48 < mabshoff> ok
16:48 < mabshoff> What is it?
16:48 < wstein> e.g., if you do
16:48 < wstein> sage: x = 5
16:48 < wstein> sage: y = x + 2 # optional - gap
16:48 < wstein> sage: y   # optional -gap
16:48 < wstein> 7
16:49 < wstein> Then if you don't include the gap tag it will actually doctest:
16:49 < wstein> sage: x = 5
16:49 < wstein> 7
16:49 < mabshoff> Yes, that is why it should run the block
16:49 < wstein> which will fail.
16:49 < mabshoff> ok
16:49 < wstein> The problem is that it is including output when it shouldn't.
16:49 < mabshoff> true
16:49 < wstein> i'll make another ticket.
16:49 < wstein> I have to fix this to manage working on the magma interface.
```



---

Comment by was created at 2008-11-24 05:34:19

For the referee -- here is a file, and me verifying that the -only_optional and -optional options work correctly.   I don't think this can go into the actual doctest framework for Sage.   However, that isn't really needed since the actual optional doctests in actual code passing is test enough (stuff like below gets or will be used all over in the doctest framework). 

```
wstein`@`ubuntu:~/sage/tmp$ more a.py
"""
sage: x = 5
sage: y = x + 2 # optional - gap
sage: y         # optional - gap
8
sage: 2 + 3     # optional - magma
5
"""
wstein`@`ubuntu:~/sage/tmp$ sage -t -only_optional=gap a.py
sage -t -only_optional=gap tmp/a.py                         **********************************************************************
File "/home/wstein/sage/tmp/a.py", line 4:
    : y         # optional - gap
Expected:
    8
Got:
    7
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/sage/tmp/.doctest_a.py
	 [1.6 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -only_optional=gap tmp/a.py
Total time for all tests: 1.6 seconds
wstein`@`ubuntu:~/sage/tmp$ sage -t a.py
sage -t  tmp/a.py                                           
	 [1.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 1.6 seconds
wstein`@`ubuntu:~/sage/tmp$ sage -t -only_optional=magma a.py
sage -t -only_optional=magma tmp/a.py                       
	 [1.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 1.6 seconds
wstein`@`ubuntu:~/sage/tmp$ sage -t -only_optional=magma,gap a.py
sage -t -only_optional=magma,gap tmp/a.py                   **********************************************************************
File "/home/wstein/sage/tmp/a.py", line 4:
    : y         # optional - gap
Expected:
    8
Got:
    7
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/sage/tmp/.doctest_a.py
	 [1.7 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -only_optional=magma,gap tmp/a.py
Total time for all tests: 1.7 seconds
wstein`@`ubuntu:~/sage/tmp$ sage -t -optional a.py
sage -t -optional tmp/a.py                                  **********************************************************************
File "/home/wstein/sage/tmp/a.py", line 4:
    : y         # optional - gap
Expected:
    8
Got:
    7
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/sage/tmp/.doctest_a.py
	 [1.7 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -optional tmp/a.py
Total time for all tests: 1.7 seconds
wstein`@`ubuntu:~/sage/tmp$ 
```



---

Comment by was created at 2008-11-24 05:39:47

With the attached patch and #4601 applied to sage-3.2.1.alpha0, I get:

```
$ cd devel/sage/sage/
$ sage -t -only_optional=magma * 
...
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 207.7 seconds
```



---

Attachment

this patch to the scripts repo should fix everything.


---

Comment by mabshoff created at 2008-11-24 21:52:35

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-24 22:43:25

Merged in Sage 3.2.1.alpha1


---

Comment by mabshoff created at 2008-11-24 22:43:25

Resolution: fixed
