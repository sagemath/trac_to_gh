# Issue 8435: SageNB 0.7.5.2

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-03-04 11:11:52

Assignee: was

CC:  jhpalmieri mhansen mvngu robert.marik acleone

Candidates: #5601, #7911, #8141, #8324, #8265, #8387.


---

Comment by mpatel created at 2010-03-04 11:12:22

I'll make a new package after I wake up.


---

Comment by mpatel created at 2010-03-04 22:44:31

Changing status from new to needs_review.


---

Attachment

Selenium Failures


---

Comment by mvngu created at 2010-03-06 23:54:24

The upgraded package [sagenb-0.7.5.2.spkg](http://sage.math.washington.edu/home/mpatel/trac/8435/sagenb-0.7.5.2.spkg) works for me. All doctests passed. I'm not familiar with the SageNB package, so I invite someone more knowledgeable to review the code changes.


---

Comment by robert.marik created at 2010-03-07 18:33:18

I have two other problems (after intallation and sage -t -sagenb)

```
sage -t  "local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/misc/sageinspect.py"
**********************************************************************
File "/opt/sage-4.3.3/local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/misc/sageinspect.py", line 688:
    sage: sage_getsourcelines(matrix, True)[1]
Expected:
    34
Got:
    33
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_13
***Test Failed*** 1 failures.

sage -t  "local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/notebook/interact.py"
**********************************************************************
File "/opt/sage-4.3.3/local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/notebook/interact.py", line 2720:
    sage: color_selector('purple', widget = 'colorpicker')
Expected:
    Interact color selector labeled None, with default RGB color (0.50..., 0.0, 0.50...), widget 'colorpicker', and visible input box
Got:
    Interact color selector labeled None, with default RGB color (0.5, 0.0, 1.0), widget 'colorpicker', and visible input box
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_109
***Test Failed*** 1 failures.

```

to Minh: I think that allmost nobody else than mpatel has deep knowledges of SageNB code :(.


---

Comment by mhansen created at 2010-03-07 18:36:41

Replying to [comment:6 robert.marik]:
> to Minh: I think that allmost nobody else than mpatel has deep knowledges of SageNB code :(. 

I don't think that's true.  I think that William, Tim Dumol, and myself are all pretty comfortable with the code.  I think it's more of any issue that other people haven't put time in trying to work on it.


---

Comment by jhpalmieri created at 2010-03-07 18:41:43

Replying to [comment:6 robert.marik]:
> I have two other problems (after intallation and sage -t -sagenb)

Which version of Sage is this?  Those doctest failures sound like consequences of patches to keep up with changes in Sage 4.3.4.alpha0, so you might get errors if you run this version of sagenb with an older version of Sage.


---

Comment by robert.marik created at 2010-03-07 20:28:03

Replying to [comment:7 mhansen]:
> 
> I don't think that's true.  I think that William, Tim Dumol, and myself ....

Oh sorry, I forgot ...

And yes, I tested on the last released Sage - Sage 4.3.3. So sorry for the noise.

Robert


---

Comment by jhpalmieri created at 2010-03-09 05:54:32

Replying to [comment:5 mvngu]:
> The upgraded package [sagenb-0.7.5.2.spkg](http://sage.math.washington.edu/home/mpatel/trac/8435/sagenb-0.7.5.2.spkg) works for me. All doctests passed. I'm not familiar with the SageNB package, so I invite someone more knowledgeable to review the code changes.

I think that if all of the relevant tickets have received positive reviews, then people have presumably reviewed the code changes.  So perhaps passing doctests should be good enough for this ticket to be given a positive review.  Opinions?  (Now sagenb-0.7.5.3 is available, so it should be tested.)


---

Comment by mvngu created at 2010-03-09 05:59:15

Replying to [comment:11 jhpalmieri]:
> I think that if all of the relevant tickets have received positive reviews, then people have presumably reviewed the code changes.  So perhaps passing doctests should be good enough for this ticket to be given a positive review.

I think that is reasonable. In most cases, it is safe for a new SageNB spkg to go into an alpha release. But I would refrain from putting a new SageNB spkg into an rc release. Anyway, John's argument convinces me.


---

Comment by jhpalmieri created at 2010-03-09 06:35:00

Replying to [comment:12 mvngu]:
> I think that is reasonable. In most cases, it is safe for a new SageNB spkg to go into an alpha release. But I would refrain from putting a new SageNB spkg into an rc release.

This sounds sensible.


---

Comment by mpatel created at 2010-03-09 06:45:49

The Selenium tests passed for me with Firefox 3.5.8 on Linux, but let me know.


---

Comment by acleone created at 2010-03-09 07:14:06

Strange - I get the same Selenium failures on 0.7.5.3 as the ones listed above.

My setup:
 * FF 3.5.8 on Ubuntu 32-bit 9.10
 * Selenium Server 1.0.3 run with `java -jar selenium-server.jar`
 * `sagenb-0.7.5.3/src/sagenb/sagenb/testing$ sage -python run_tests.py`
 * sage version 4.3.4.alpha0
 * SAGENB_VERSION is '0.7.5.3'
 * All doctests pass (`sage -t -sagenb`).


---

Comment by mpatel created at 2010-03-09 07:19:04

You're right. I just upgraded to Selenium 1.0.3 (from 1.0.1) and now they don't all pass.  I'll investigate.

To run the [Selenium](http://seleniumhq.org/) tests with Firefox, check that Java is installed and [download Selenium RC](http://seleniumhq.org/download/):

```sh
wget http://selenium.googlecode.com/files/selenium-remote-control-1.0.3.zip
mkdir selenium
cd selenium
unzip selenium-remote-control-1.0.3.zip
cd selenium-server-1.0.3
java -jar selenium-server.jar
```

To run the SageNB tests, I usually do the following, e.g., in a script:

```python
sage: import sagenb.testing.run_tests as rt
sage: brow = '*firefox3 /usr/lib64/firefox-3.5.8/firefox'  
sage: rt.setup_tests('localhost', False, brow)
sage: rt.run_any()
```

The `setup_tests` step may not be necessary, but I think it helps to give the path to the actual Firefox binary.  See docstrings for a few examples.


---

Comment by mpatel created at 2010-03-09 07:23:34

A possibly outdated [comment](http://trac.sagemath.org/sage_trac/ticket/6855#comment:12) about earlier tests with other browsers.


---

Comment by mhansen created at 2010-03-09 08:04:38

Resolution: fixed


---

Comment by mhansen created at 2010-03-09 08:04:38

I'm going to merge 0.7.5.3 into alpha1 since it seems like the issue is more with the Selenium code than the actual SageNB code.  A ticket can be opened for that.


---

Comment by mpatel created at 2010-03-09 08:53:13

I agree.  The tests fail because the new Se creates _two_ worksheets when we call `selenium.open('/new_worksheet')`.  I don't know if this is a Se bug.
