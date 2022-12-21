# Issue 6320: optional doctest failure -- combinat crystal code

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 14:50:46

Assignee: tbd

CC:  tscrim

I have dot2tex installed but this doctest in combinat still fails:

```
wstein`@`sage:~/build/sage-4.0.2.alpha3$ which dot2tex
/usr/bin/dot2tex
wstein`@`sage:~/build/sage-4.0.2.alpha3$ ./sage -t -long --optional devel/sage/sage/combinat/crystals/crystals.py
sage -t -long --optional "devel/sage/sage/combinat/crystals/crystals.py"

**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage/sage/combinat/crystals/crystals.py", line 344:
    sage: C.latex_file('/tmp/test.tex') #optional requires dot2tex
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[3]>", line 1, in <module>
        C.latex_file('/tmp/test.tex') #optional requires dot2tex###line 344:
    sage: C.latex_file('/tmp/test.tex') #optional requires dot2tex
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 363, in latex_file
        f.write(header + self.latex() + footer)
    TypeError: cannot concatenate 'str' and 'NoneType' objects
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage/sage/combinat/crystals/crystals.py", line 422:
    sage: C.latex() #optional requires dot2tex
Expected nothing
Got:
    dot2tex not available.  Install after running 'sage -sh'
**********************************************************************
2 items had failures:
   1 of   4 in __main__.example_10
   1 of   4 in __main__.example_13
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_crystals.py
         [7.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long --optional "devel/sage/sage/combinat/crystals/crystals.py"
Total time for all tests: 7.2 seconds
wstein`@`sage:~/build/sage-4.0.2.alpha3$ 


```



---

Comment by bump created at 2009-06-16 15:22:19

Dot2tex may be installed on your system but still sage can't find it. You
probably don't want `/usr/bin/dot2tex` but rather `$SAGEROOT/local/bin/dot2tex`.

To install dot2tex start `sage -sh` then install pydot, pyparsing and dot2tex
by going to their source directories and running `python setup.py install`.

There is some discussion of making dot2tex a sage spkg here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/f682107dcc4ee3f2/ddea890fc5513d81?hl=en&lnk=gst&q=dot2tex#ddea890fc5513d81


---

Comment by slabbe created at 2016-09-26 13:10:45

Changing status from new to needs_review.


---

Comment by slabbe created at 2016-09-26 13:10:45

On 7.4.beta5, running


```
./sage -t -l --optional=sage,dot2tex,graphviz src/sage/combinat/crystals/crystals.py
```


gives


```
Running doctests with ID 2016-09-26-15-08-12-8d82066d.
Git branch: 21490
Using --optional=dot2tex,graphviz,sage
Doctesting 1 file.
sage -t --long --warn-long 42.7 src/sage/combinat/crystals/crystals.py
    [25 tests, 0.75 s]
----------------------------------------------------------------------
All tests passed!
----------------------------------------------------------------------
Total time for all tests: 0.8 seconds
    cpu time: 1.0 seconds
    cumulative wall time: 0.7 seconds
```


Should we close this ticket?


---

Comment by jdemeyer created at 2016-09-26 13:19:27

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-01-21 18:03:11

Resolution: invalid
