# Issue 7749: Add names.gz to the Sloane OEIS

Issue created by migration from Trac.

Original creator: ssivek

Original creation time: 2009-12-22 18:15:56

Assignee: tbd

Add access to the names.gz file (http://www.research.att.com/~njas/sequences/names.gz) to sloane.py so that users can access sequence names while offline.

Change the output from Python ints to Sage (see SloaneEncyclopedia[111111] for an example).


---

Comment by ssivek created at 2009-12-22 18:20:01

I plan to add a function SloaneEncyclopedia.sequence_name(n), rather than changing the output of __getitem__ or anything like that, to avoid backwards compatibility issues.

This will require the patch from ticket #7692.


---

Attachment

I've uploaded a patch that does exactly what the ticket description says.  Note that the names.gz database file remains optional, in the sense that users can choose not to install it (e.g. by "SloaneEncyclopedia.install(names_url=None)").  This way, if you apply this patch with the stripped.gz database file already installed the only thing that shouldn't work is SloaneEncyclopedia.sequence_name(), which should raise an error when names.gz is not installed.  The only way to install names.gz is to install stripped.gz from scratch as well, though, to avoid renumbering and other possible incompatibility issues between different versions of the OEIS.


---

Comment by ssivek created at 2009-12-23 04:11:39

Changing status from new to needs_review.


---

Comment by jsp created at 2009-12-23 14:36:22

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2009-12-23 14:36:22

Worked for me. Looks good. All tests passed.



```
3 items had no tests:
    __main__
    __main__.change_warning_output
    __main__.warning_function
16 items passed all tests:
  13 tests in __main__.example_0
   2 tests in __main__.example_1
   2 tests in __main__.example_10
   3 tests in __main__.example_11
   2 tests in __main__.example_12
   2 tests in __main__.example_13
   4 tests in __main__.example_14
   3 tests in __main__.example_15
   2 tests in __main__.example_2
   2 tests in __main__.example_3
   2 tests in __main__.example_4
   2 tests in __main__.example_5
   2 tests in __main__.example_6
   2 tests in __main__.example_7
   2 tests in __main__.example_8
   2 tests in __main__.example_9
47 tests in 19 items.
47 passed and 0 failed.
Test passed.
	 [11.8 s]

```


So positive review.

Jaap


---

Comment by mhansen created at 2010-01-03 21:22:54

Resolution: fixed
