# Issue 8754: sagenb -- add "how to test" directions to the sagenb README.txt

Issue created by migration from https://trac.sagemath.org/ticket/8754

Original creator: was

Original creation time: 2010-04-24 21:00:55

Assignee: jason, was

CC:  chapoton


```
1. Doctest: 
       sage -t -sagenb 
2. Run the Selenium test suite:
       sage -python sagenb/testing/run_tests.py 

To use Selenium, you must visit http://seleniumhq.org/download/ and:

      * Download and extract Selenium RC ("the Selenium Remote Control")

      * Run it as follows on Linux:
             $ cd /path/to/selenium-remote-control-1.0.3/selenium-server-1.0.3
             $ java -jar selenium-server.jar
             $ cd /path/to/sagenb-0.8/src/sagenb
             $ sage  -python sagenb/testing/run_tests.py

      * Run it as follows on OS X:
             $ cd /path/to/selenium-remote-control-1.0.3/selenium-server-1.0.3
             $ cd /path/to/sagenb-0.8/src/sagenb
             $ sage
             sage: import sagenb.testing.run_tests as rt 
             sage: rt.setup_tests('localhost', False, '*firefox')
             sage: rt.run_any()
```


That the instructions for OS X are different is probably a bug. 




---

Comment by was created at 2010-04-25 00:41:39

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2010-04-25 00:56:49

Changing status from needs_review to positive_review.


---

Attachment

Added a development section.  Replaces the last patch


---

Attachment

Newest Version.  Added a "Reviewing Patches" section.  Apply only this.


---

Comment by mpatel created at 2010-07-23 06:44:11

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-07-23 06:44:11

Should someone review the latest patch?  I noticed two minor problems:

 * `dwnload`
 * An extra `*` in `b) * Run it as follows:`

Also, should the reviewing section first refer in some way to steps 1,2,3, and/or 6 of the development section?


---

Comment by kcrisman created at 2014-09-16 21:34:18

Reported "upstream" at https://github.com/sagemath/sagenb/issues/221


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2020-08-19 12:34:43

Resolution: invalid
