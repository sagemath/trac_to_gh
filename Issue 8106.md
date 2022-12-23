# Issue 8106: Minor update on $SAGE_ROOT/README.txt

Issue created by migration from https://trac.sagemath.org/ticket/8106

Original creator: GokhanSever

Original creation time: 2010-01-28 05:04:01

Assignee: mvngu

Keywords: test check

There should be a warning added to this description. Such as:

Please be aware that a failure in execution of an individual test suite could terminate your build process. Use with caution. In case of your build terminated try building SAGE without running the tests.


```
   If you want to run the test suite for each individual spkg as it is
   installed, type

       export SAGE_CHECK="yes"

   before starting the Sage build. This will run each test suite and
   will raise an error if any failures occur. 
```


See the discussion in context : http://groups.google.com/group/sage-devel/t/cf328879542463a4



---

Comment by mvngu created at 2010-02-14 19:04:51

See ticket #7484 for an updated README.txt that fixes the issue reported here.


---

Comment by kcrisman created at 2014-11-20 15:53:34

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-11-20 15:53:34

Yes, this did.


---

Comment by kcrisman created at 2014-11-20 15:53:39

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-11-28 20:59:09

Resolution: duplicate
