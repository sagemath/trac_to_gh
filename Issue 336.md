# Issue 336: Create an option to clear all cell output

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2007-03-27 18:20:31

Assignee: boothby

I am homeschooled and doing programming in the notebook for credit. I would like to clear all of the output on my worksheets so I can print the code for the worksheet without the computer generated output.


---

Comment by was created at 2008-05-10 19:54:36

The attached patch does the following:

```
Fix trac #336 -- "delete all output" for the Sage notebook worksheets.  Also:
   1. Changed "Revisions" to "Undo" in the notebook, since it is clearer.
   2. Added several new functions needed to implement #336 and fully documented
      and doctested all of them.  This meant improving the functions that
      support writing doctests for the notebook, and doctesting those 
      functions too.  Doctesting of the notebook is thus actually *greatly*
      improved by this patch.
   3. Made some fixes to doctests also so that parallel doctesting works.    
      In particular, avoid clashes in temp notebook names. 
   4. Created a cell "evaluated" function to keep track of whether or not
      cells have been evaluated.  I did this in order to non-hackishly 
      implement "delete all output".  It will also be very useful for other
      tickets.   I added a lot of doctesting related to this too. 
   5. Added a worksheet function user_can_edit to double check that the
      given user can edit the worksheet; this is used by the "delete all output" 
      code as a double check that invalid users can't delete all output. 
```


To test it do the following:
 1. apply the patch and build
 2. Make a worksheet and selected "Action -> Delete all output"
 3. Note that all output is gone.  Click refresh to see that the server got the message
 4. Doctest the sage/server/notebook directory.  It has a bunch of new doctests.
 5. Read over the patch itself to see how it's all implemented:
        * some javascript to delete the output from the DOM
        * some server-side python code to do the actual deleting
        * some general server-side code to improving doctesting of the notebook.
        * general doc improvements.


---

Attachment


---

Comment by TimothyClemans created at 2008-05-11 03:37:46

One doctest failure


```
File "/home/tclemans/sage-3.0/tmp/notebook.py", line 133:
    sage: os.listdir('notebook-test')
Expected:
    ['backups', 'nb.sobj', 'objects', 'worksheets']
Got:
    ['worksheets', 'objects', 'backups', 'nb.sobj']
```



---

Attachment

Positive review with doctestfix patch. I didn't really do 5 except I did look at the doctest stuff.


---

Comment by mabshoff created at 2008-05-11 07:25:47

Resolution: fixed


---

Comment by mabshoff created at 2008-05-11 07:25:47

Merged in Sage 3.0.2.alpha0
