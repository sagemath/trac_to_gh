# Issue 246: height of a notebook cell

Issue created by migration from https://trac.sagemath.org/ticket/246

Original creator: ifti

Original creation time: 2007-02-06 17:45:31

Assignee: boothby

When I paste a huge string into a notebook cell, the height of the cell
doesn't increase appropriately and scrolling through the string using
my cursor and maneuvering the tiny scroll bar are painful.

I was wondering if there is any way to increase the height of cells in the
SAGE notebook. If the answer is negative, it should be a todo.



---

Comment by TimothyClemans created at 2007-03-02 18:51:47

It would be nice if I could type in the number of lines in the notebook of a cell text area. I'm finding that I want this now.

cell.py

```
480 <textarea class="%s" rows=%s cols=100000 columns=100000
481 id = 'cell_input_%s'
482 onKeyPress = 'return input_keypress(%s,event);'
483 oninput = 'cell_input_resize(this);'
484 onFocus = 'return cell_focus(%s)'
485 onBlur = 'return cell_blur(%s)'
486 >%s</textarea> 
```


There is a javascript app for this at http://www.peterbe.com/Changing-textarea-size.


---

Comment by mhansen created at 2008-04-15 07:25:26

This ticket has been fixed based on the current behavior of the notebook since the cell doesn't scroll and instead wraps the text down to the next line.


---

Comment by mhansen created at 2008-04-15 07:25:26

Resolution: fixed
