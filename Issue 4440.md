# Issue 4440: Automatic Identation

Issue created by migration from Trac.

Original creator: ahupfer

Original creation time: 2008-11-04 19:26:07

Assignee: ahupfer

CC:  jason

The patch provides automatic indentation for python after colons and same level identation.
It works up to four levels of identation.


---

Comment by mabshoff created at 2008-11-04 20:24:39

There is already an attempt to do this at #1684. 

Cheers,

Michael


---

Comment by boothby created at 2008-11-05 00:29:21

The restriction to 4 indentation levels is decidedly strange, given that the patch itself has a 6-deep indentation.  This can be written more elegantly:


```
var indenting, id, tab;
indenting = RegExp("\n( *)","g");
while(indenting.test(text[0])) {
  id   = indexing.lastIndex;
  tab  = RegExp.lastMatch.substring(1);
}
if( id == second_last_break && second_last_break != -1) {
    get_cell(id).value = text[0] + tab + text[1]; 
    set_cursor_position(cell, position + tab.length);
}
```


The above code hasn't been tested, but should be a good start.


---

Attachment


---

Comment by ahupfer created at 2008-11-21 13:48:46

Improved identation support with unlimited ident. Tested with Firefox, Safari, Chrome.
Works not, but doesn't break Internet Explorer and Opera.


---

Comment by was created at 2008-11-27 17:33:22

REVIEW

This is *REALLY* nice and *almost* works.  It has one bug, which is that if you enter a blank line, the auto-indent is off by one.  E.g., I got the following when I entered a blank line after the first print statement:

```
if True:
    print "hi"
    
   print "mom"
```


I should have got either

```
if True:
    print "hi"
    
    print "mom"
```

or 

```
if True:
    print "hi"

print "mom"
```


Which is a design decision.  To be more like the Python/Ipython command line, one would get the latter.  To be more like an IDE, maybe the former.  I don't care which, just that the current behavior (which is neither) is buggy.

That said, if this bit rots forever that would be bad.  I would almost rather have the buggy patch than no patch at all, since even with the bug it's pretty nice functionality.

It would however by nice if there were a way to turn it off.  That will have to wait until Timothy Clemans user management features get in.


---

Attachment


---

Comment by boothby created at 2009-01-21 23:58:49

I fixed the bug was reported.  I've tested this in firefox on windows only.  Also, I made the regexp significantly uglier to make it more robust (sadly), and so commented the snot out of it.


---

Comment by jason created at 2009-01-22 19:26:55

Notes from Tom:
  * Fold the patches into one patch
  * Make the iphone check *after* the resize code


---

Comment by jason created at 2009-01-22 19:33:17

This feature seems to work well.  I can see it being annoying if there happens to be a semi-colon at the end of the line for a language other than python.  For that reason, there should be a way to turn this off.  I think it's probably not going to be a huge problem, though, so I think this ought to go in (after the two fixes above are done), and a feature ticket created to make an option for the user to turn this off.


---

Comment by jason created at 2009-01-22 19:33:45

Positive review pending the above changes in "Notes from Tom"


---

Comment by boothby created at 2009-01-23 09:28:46

Replaces previous two patches


---

Attachment


---

Comment by jason created at 2009-01-28 17:19:45

Very nice.  This addresses wstein's comment above and now does the second option.

Positive review.


---

Comment by mabshoff created at 2009-01-28 18:04:14

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 18:04:14

Merged 4440-indentation.patch in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by jason created at 2009-02-17 23:03:15

This causes a serious bug: #5293.  I vote we remove this patch from 3.3 and work on it.


---

Comment by jason created at 2009-02-17 23:03:30

Changing status from closed to reopened.


---

Comment by jason created at 2009-02-17 23:03:30

Resolution changed from fixed to 


---

Comment by jason created at 2009-02-17 23:04:14

mabshoff says that he will revert this patch for now.  I hope that it is fixed and gets back in soon!  It's a great piece of functionality!


---

Comment by jason created at 2009-02-17 23:05:08

(to get a positive review, we need to fix the issue at #5293)


---

Comment by mabshoff created at 2009-02-20 06:47:45

Reinstated due to positive review of the fix at #5293.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 07:24:49

Merged in Sage 3.3.rc3 again :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 07:24:49

Resolution: fixed
