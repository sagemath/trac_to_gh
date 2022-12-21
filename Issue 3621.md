# Issue 3621: [with patch, needs review] Finance -- Fix Stock.historical(), addition of enddate input

Issue created by migration from Trac.

Original creator: cswiercz

Original creation time: 2008-07-09 00:34:15

Assignee: cswiercz

CC:  jkantor

Keywords: finance, historical, stock, Stock

There was an issue with Stock.historical() only returning stock information from Jan 1, 1990 onward and no earlier. The addition of an explicit enddate to the Google Finance query seems to fix this. Fix is demonstrated in the doctests of Stock.historical()

Uses the datetime.date python module.


---

Comment by cswiercz created at 2008-07-09 00:35:18

Changing status from new to assigned.


---

Comment by cswiercz created at 2008-07-09 16:56:11

Replying to [ticket:3621 cswiercz]:
> There was an issue with Stock.historical() only returning stock information from Jan 1, 1990 onward and no earlier. The addition of an explicit enddate to the Google Finance query seems to fix this. Fix is demonstrated in the doctests of Stock.historical()
> 
> Uses the datetime.date python module.

This ticket depends on #3356.


---

Comment by brettnak created at 2008-07-18 21:38:41

Changing status from assigned to new.


---

Comment by brettnak created at 2008-07-18 21:38:41

Changing assignee from cswiercz to cswiercz, brettnak.


---

Comment by brettnak created at 2008-07-21 02:51:47

add_load_file1.patch - Split up .historical into three parts.  Added a .load_file() function that will load data from a specified file if the file formatted correctly.
eg. 'date,open,high,low,close,volume\n...'


---

Comment by brettnak created at 2008-07-21 03:00:46

.load_file() does not work for large files due to python's .read() size limitations.  Next patch will read the file by line to get around this.


---

Comment by cswiercz created at 2008-07-28 02:24:25

Changing status from new to assigned.


---

Comment by cswiercz created at 2008-07-28 02:24:25

Changing assignee from cswiercz, brettnak to cswiercz.


---

Comment by was created at 2008-07-29 18:29:02

REFEREE REPORT:

Great work!  Now be professionals and fix everything below :-)

 * The function `_load_from_csv(self, R)` in stock.py is missing a doctest

 * I like the Day --> OHCL change. 

 * Member functions in the Sage library should never be upper case, so

```
    def Open(self, *args, **kwds):
```

must become

```
    def open(self, *args, **kwds):
```


 * The doctest for Open contains `\code{self.google()`.  Since the docstring is a string that \c gets turned into a weird character.  You have to do either `\\code{self.google()` or (better) just replace `"""` at the top by `r"""`.  Same for `def Close`, etc.  

 * This doctest SUCKS:

```
+            sage: finance.Stock('goog').load_from_file('/Users/cswiercz/GOOG-minutely.txt')[:5]    # optional -- requires s
ource file
+            [
```

We actually *do* test all optional doctests sometimes, and do expect them to pass on a reasonably configured machine.   I suggest the following workaround.  Make a subdirectory of SAGE_ROOT/examples called "finance".  Put your file in there.  Do hg ci in there to add it to the examples repo.  Post a patch using "hg export tip" in that repo.  If you get stuck, let me know.   Then in the doctest just put SAGE_ROOT + 'examples/finance/your_filename.txt'.   And you won't have to make it optional, which is always a plus. 

 * This code in your patch (in the function load_from_file) contains a bug:

```
+        try:
+            R = file_obj.read();
+        except IOError:
+            raise IOError, msg + "Bad path or file name"
```


You mean to write:

```
+        try:
+            R = file_obj.read();
+        except IOError, msg :
+            raise IOError, msg + "Bad path or file name"
```

A doctest should illustrate this exception maybe, so you would have caught this bug.

 * 5 Doctests in stock.py fail:

```
sage -t --optional devel/sage-review/sage/finance/stock.py
**********************************************************************
File "/Users/was/s/tmp/stock.py", line 274:
    sage: finance.Stock('vmw').Open()    # optional -- requires internet
Expected:
    [52.1100, 60.9900, 59.0000, 56.0500, 57.2500 ... 38.5300, 36.1800, 32.6300, 36.7000, 34.5000]
Got:
    [52.1100, 60.9900, 59.0000, 56.0500, 57.2500 ... 36.1800, 32.6300, 36.7000, 34.5000, 34.0000]
**********************************************************************
File "/Users/was/s/tmp/stock.py", line 308:
    sage: c.google(startdate='Feb+1,+2008', enddate='Mar+1,+2008')    # optional -- requires internet
Expected:
    [
     31-Jan-08 55.60 57.35 55.52 56.67    2607800,
      1-Feb-08 56.98 58.14 55.06 57.85    2489400,
      4-Feb-08 58.00 60.47 56.91 58.05    1840300,
      5-Feb-08 57.60 59.30 57.17 59.30    1711700,
      6-Feb-08 60.32 62.00 59.50 61.52    2209700
    ]
Got:
    [
     31-Jan-08 55.60 57.35 55.52 56.67    2607800,
      1-Feb-08 56.98 58.14 55.06 57.85    2489400,
      4-Feb-08 58.00 60.47 56.91 58.05    1840300,
      5-Feb-08 57.60 59.30 57.17 59.30    1711700,
      6-Feb-08 60.32 62.00 59.50 61.52    2209700,
      7-Feb-08 60.50 62.75 59.56 60.80    1521700,
      8-Feb-08 60.90 61.39 60.07 60.27     956400,
     11-Feb-08 61.22 62.24 60.90 61.42    1132600,
     12-Feb-08 62.00 63.00 61.56 62.26     989000,
     13-Feb-08 63.00 63.50 62.18 62.93     919500,
     14-Feb-08 63.10 63.33 61.25 62.10    1333000,
     15-Feb-08 61.20 62.57 59.25 59.81    1598200,
     19-Feb-08 60.99 61.50 56.50 57.38    1685900,
     20-Feb-08 56.23 59.83 56.23 59.45     913600,
     21-Feb-08 59.46 60.00 57.50 57.91    1124000,
     22-Feb-08 58.00 58.48 55.00 56.55    1449100,
     25-Feb-08 56.55 58.60 56.01 58.29     907900,
     26-Feb-08 59.30 60.70 57.43 60.18    2050400,
     27-Feb-08 60.00 60.50 58.42 59.86    1285200,
     28-Feb-08 59.79 60.96 59.16 59.95     984500,
     29-Feb-08 59.26 59.95 58.32 58.67     842200
    ]
**********************************************************************
File "/Users/was/s/tmp/stock.py", line 321:
    sage: finance.Stock('vmw').Close()    # optional -- requires internet
Expected:
    [57.7100, 56.9900, 55.5500, 57.3300, 65.9900 ... 36.9400, 37.9700, 37.0000, 34.7500, 34.0700]
Got:
    [57.7100, 56.9900, 55.5500, 57.3300, 65.9900 ... 37.9700, 37.0000, 34.7500, 34.0700, 34.6900]
**********************************************************************
File "/Users/was/s/tmp/stock.py", line 352:
    sage: finance.Stock('goog').load_from_file('/Users/cswiercz/GOOG-minutely.txt')[:5]    # optional -- requires source file
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[1]>", line 1, in <module>
        finance.Stock('goog').load_from_file('/Users/cswiercz/GOOG-minutely.txt')[:Integer(5)]    # optional -- requires source file###line 352:
    sage: finance.Stock('goog').load_from_file('/Users/cswiercz/GOOG-minutely.txt')[:5]    # optional -- requires source file
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/finance/stock.py", line 375, in load_from_file
        file_obj = open(file, 'r')
    IOError: [Errno 2] No such file or directory: '/Users/cswiercz/GOOG-minutely.txt'
**********************************************************************
File "/Users/was/s/tmp/stock.py", line 366:
    sage: finance.Stock('goog').load_from_file('/Users/cswiercz/GOOG-minutely.txt')[:5]    # optional -- requires source file
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[2]>", line 1, in <module>
        finance.Stock('goog').load_from_file('/Users/cswiercz/GOOG-minutely.txt')[:Integer(5)]    # optional -- requires source file###line 366:
    sage: finance.Stock('goog').load_from_file('/Users/cswiercz/GOOG-minutely.txt')[:5]    # optional -- requires source file
      File "/Users/was/s/local/lib/python2.5/site-packages/sage/finance/stock.py", line 375, in load_from_file
        file_obj = open(file, 'r')
    IOError: [Errno 2] No such file or directory: '/Users/cswiercz/GOOG-minutely.txt'
**********************************************************************
File "/Users/was/s/tmp/stock.py", line 407:
    sage: finance.Stock('aapl').google()[:2]    # optional -- requires internet
Expected:
    [
      2-Jan-90 8.81 9.38 8.75 9.31    6542800,
      3-Jan-90 9.50 9.50 9.38 9.38    7428400
    ]
Got:
    [
     30-Jul-07 144.33 145.45 139.57 141.43   39535300,
     31-Jul-07 142.97 143.48 131.52 131.76   62942600
    ]
**********************************************************************
File "/Users/was/s/tmp/stock.py", line 211:
    sage: sage.finance.stock.Stock("AAPL", 22144).google()[:5] #optional -- requires internet
Expected:
        [
          2-Jan-90 8.81 9.38 8.75 9.31    6542800,
          3-Jan-90 9.50 9.50 9.38 9.38    7428400,
          4-Jan-90 9.56 9.69 9.31 9.41    7911200,
          5-Jan-90 9.44 9.56 9.25 9.44    4404000,
          8-Jan-90 9.38 9.50 9.25 9.50    3627600
        ]
Got:
    [
     30-Jul-07 144.33 145.45 139.57 141.43   39535300,
     31-Jul-07 142.97 143.48 131.52 131.76   62942600,
      1-Aug-07 133.64 135.38 127.77 135.00   62505600,
      2-Aug-07 136.65 136.96 134.15 136.49   30451600,
      3-Aug-07 135.26 135.95 131.50 131.85   24256700
    ]
**********************************************************************
5 items had failures:
   1 of   6 in __main__.example_10
   2 of   6 in __main__.example_11
   2 of   3 in __main__.example_12
   1 of   2 in __main__.example_14
   1 of   5 in __main__.example_9
***Test Failed*** 7 failures.
For whitespace errors, see the file /Users/was/s/tmp/.doctest_stock.py
```



---

Comment by cswiercz created at 2008-07-31 21:43:14

Faulty formatting with part5.patch? Following error message when applying the patch.



```
sage: hg_sage.apply("http://trac.sagemath.org/sage_trac/attachment/ticket/3621/sage-3621-part6.patch")
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/3621/sage-3621-part6.patch?format=raw
Loading: [...]
cd "/Users/cswiercz/sage/devel/sage" && hg status
cd "/Users/cswiercz/sage/devel/sage" && hg status
cd "/Users/cswiercz/sage/devel/sage" && hg import   "/Users/cswiercz/.sage/temp/D_69_91_144_189.dhcp4.washington.edu/1527/tmp_5.patch"
applying /Users/cswiercz/.sage/temp/D_69_91_144_189.dhcp4.washington.edu/1527/tmp_5.patch
patching file sage/finance/stock.py
Hunk #1 FAILED at 2
Hunk #2 FAILED at 13
Hunk #3 FAILED at 47
Hunk #4 FAILED at 137
Hunk #5 FAILED at 160
Hunk #6 FAILED at 174
Hunk #7 FAILED at 189
Hunk #8 FAILED at 202
Hunk #9 FAILED at 221
Hunk #10 FAILED at 277
10 out of 10 hunks FAILED -- saving rejects to file sage/finance/stock.py.rej
abort: patch failed to apply
```



---

Comment by brettnak created at 2008-07-31 22:15:14

Patch 6 is a duplicate of patch 5.  Part 6 is supposed to add a new doctest.  I will add that shortly.


---

Comment by brettnak created at 2008-08-02 21:32:16

Changing assignee from cswiercz to cswiercz, brettnak.


---

Comment by brettnak created at 2008-08-02 21:32:16

Changing status from assigned to new.


---

Comment by cswiercz created at 2008-08-05 21:01:02

Changing status from new to assigned.


---

Comment by cswiercz created at 2008-08-05 21:01:02

Changing assignee from cswiercz, brettnak to cswiercz.


---

Comment by mabshoff created at 2008-08-06 01:00:13

I am not so sure you guys should give each other positive reviews in this form. I would also either prefer clear instructions on which patches to merge in what order or alternatively a new unified patch. I do not want a bundle.

Cheers,

Michael


---

Comment by cswiercz created at 2008-08-06 14:53:01

Replying to [comment:16 mabshoff]:
> I am not so sure you guys should give each other positive reviews in this form. I would also either prefer clear instructions on which patches to merge in what order or alternatively a new unified patch. I do not want a bundle.

The patches should be merged in order as posted, that is:


all_updates_and_cid.patch


add_load_file1.patch


add_close.patch


load_file_bug_fix.patch


sage-3621-part5.patch


sage-3621-example.patch


sage-3621-part6.patch


sage-3621-part7.patch


sage-3621-part8.patch


sage-3621-part9.patch


sage-3621-part10.patch



Shall I set it back to [with patch, needs review]?


---

Comment by mabshoff created at 2008-08-06 17:08:58

Replying to [comment:17 cswiercz]:
> Replying to [comment:16 mabshoff]:
> > I am not so sure you guys should give each other positive reviews in this form. I would also either prefer clear instructions on which patches to merge in what order or alternatively a new unified patch. I do not want a bundle.
> 
> The patches should be merged in order as posted, that is:
> 
> 
> all_updates_and_cid.patch
> 
> 
> add_load_file1.patch
> 
> 
> add_close.patch
> 
> 
> load_file_bug_fix.patch
> 
> 
> sage-3621-part5.patch
> 
> 
> sage-3621-example.patch
> 
> 
> sage-3621-part6.patch
> 
> 
> sage-3621-part7.patch
> 
> 
> sage-3621-part8.patch
> 
> 
> sage-3621-part9.patch
> 
> 
> sage-3621-part10.patch

Thanks.

> Shall I set it back to [with patch, needs review]?

I am talking with William about this, but it seems unclear to me who gave a review to what. For example: Chris posted sage-3621-part10.patch and also gave that patch a positive review. It seems like a minor patch, but we should follow procedure here.

Cheers,

Michael


---

Comment by cswiercz created at 2008-08-06 17:18:31

Replying to [comment:18 mabshoff]:
> > Shall I set it back to [with patch, needs review]?
> 
> I am talking with William about this, but it seems unclear to me who gave a review to what. For example: Chris posted sage-3621-part10.patch and also gave that patch a positive review. It seems like a minor patch, but we should follow procedure here.

To make the situation a bit clearer, Brett asked if I could review his patches. (part6.patch - part9.patch) I found a minor bug and added my own patch at the very end. (part10.patch) My patch was just a small change to a doctest, which I tested thoroughly. I realize just now that it was kinda silly to review this ticket myself since all of the code throughout these patches was done by both of us, equally. Anyway, I'm fine with setting it back to "needs review" and waiting for someone to take a look at it. It's your call. :)

--
Chris


---

Comment by cswiercz created at 2008-08-07 22:12:42

Alas, several issues need to be resolved and some features need to be added:

 * Yahoo doesn't like explicit exchange declarations. (i.e. `finance.Stock("NASDAQ:GOOG")` returns zero.) Parse the input and store the exchange and symbol separately.

 * Yahoo should be implemented as a backup to Google Finance historical queries if Google Finance happens to return zero.

 * Fix some issues regarding explicit exchange declarations in general. (i.e. `finance.Stock("HKG:0700").historical()` returns zero.) Improve the way queries handle exchange / symbol relationships. For example, only default to `"NASDAQ"` if no exchange is given.

 * Rename `Stock.google()` back to `Stock.historical()`

 * Consolidate the ten+ patches above.

I'm taking care of this right now! :)

--

Chris


---

Attachment

Replacement patch for all patches listed above. Combines all changes.


---

Comment by mabshoff created at 2008-08-08 22:36:37

sage-3621-combined.patch is joined work by William, Chris and Brett.

Cheers,

Michael


---

Attachment

Added Yahoo Finance as a backup to Google Finance historical requests. Additional refinements.


---

Comment by mabshoff created at 2008-08-25 06:25:51

Josh, 

can you review those two patches?

Cheers,

Michael


---

Comment by boothby created at 2008-09-11 21:55:51

Something's up with the first patch -- the file *SAGE_ROOT/examples/finance/AAPL-minutely.csv* is located at *SAGE_ROOT/finance/AAPL-minutely.csv* when I apply the patch to a fresh 3.1.2.rc1.


```
boothby`@`eight:~/sage-3.1.2.rc1$ ./sage -t devel/sage/sage/finance/stock.py
sage -t  devel/sage/sage/finance/stock.py                   **********************************************************************
File "/home/boothby/sage-3.1.2.rc1/tmp/stock.py", line 417:
    sage: finance.Stock('aapl').load_from_file(SAGE_ROOT + '/examples/finance/AAPL-minutely.csv')
Expected:
    [
    2008-06-02T05:01:00 188.00 188.00 188.00 188.00        687,
    2008-06-02T05:00:00 188.00 188.11 188.00 188.00       2877,
    2008-06-02T04:55:00 188.00 188.00 188.00 188.00       1000,
    2008-06-02T04:54:00 187.75 188.00 187.75 188.00       2000,
    2008-06-02T04:23:00 187.80 187.80 187.80 187.80        100
    ]
Got:
    Bad path or file name
**********************************************************************
File "/home/boothby/sage-3.1.2.rc1/tmp/stock.py", line 431:
    sage: finance.Stock('goog').load_from_file(SAGE_ROOT + '/examples/finance/AAPL-minutely.csv')
Expected:
    [
    2008-06-02T05:01:00 188.00 188.00 188.00 188.00        687,
    2008-06-02T05:00:00 188.00 188.11 188.00 188.00       2877,
    2008-06-02T04:55:00 188.00 188.00 188.00 188.00       1000,
    2008-06-02T04:54:00 187.75 188.00 187.75 188.00       2000,
    2008-06-02T04:23:00 187.80 187.80 187.80 187.80        100
    ]
Got:
    Bad path or file name
**********************************************************************
1 items had failures:
   2 of   5 in __main__.example_12
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/boothby/sage-3.1.2.rc1/tmp/.doctest_stock.py
	 [1.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage/sage/finance/stock.py
Total time for all tests: 1.2 seconds
```



---

Comment by boothby created at 2008-09-11 22:13:49

Oops, my bad -- William already commented on that.


---

Comment by boothby created at 2008-09-11 22:14:29

apply to repository in SAGE_ROOT/examples


---

Attachment

removes creation of example file from original


---

Attachment

All (including optional) tests pass!


---

Attachment


---

Comment by was created at 2008-11-28 03:35:07

REFEREE REPORT:

Positive Review.   This is superb code.

I had to make a few minor changes since for some reason google changed their database.  I also updated some of the # optional tags for the new system. 

Michael, to apply this you must:
1. Apply 3621-combined.patch and sage-3621-trivial_referee_followup.patch to the Sage library.

2. Apply 3621–example.patch to the repo in SAGE_ROOT/examples/.

That's it.

 -- William


---

Comment by mabshoff created at 2008-11-28 08:35:56

Merged the patches William mentioned above in 3.2.1.rc0.

The credit situation: 

 * authors: Chris Swierczewski, Brett Nakashima, William Stein
 * reviewers: William Stein, Tom Boothby

Please let me know if I got anything wrong

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-28 08:35:56

Resolution: fixed
