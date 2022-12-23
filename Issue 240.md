# Issue 240: in notebook when refresh browser or first get page cell update list isn't sent out with running cells

Issue created by migration from https://trac.sagemath.org/ticket/240

Original creator: was

Original creation time: 2007-02-03 10:15:45

Assignee: boothby

in notebook when refresh browser or first get page cell update list isn't sent out with running cells. This means that if cell x is in the middle of running, and you refresh your browser, it is *impossible* to see what cell x is outputing. 

Helena Verrill found this bug. 


---

Comment by was created at 2007-02-03 19:00:19


```
It seems there are potentially a number of sources of the problem.
Any ideas?     One hint is that if you comment out this line (1462 in js.py)
 
         // active_cell_list = delete_from_array(active_cell_list, id);
 
then the problem mostly goes away.  Of course there are other problems then :-).
 
Anyway, it seems as though the server is maybe returning 'd' when it shouldn't.
 }}}


---

Comment by was created at 2007-08-19 02:06:59

Resolution: fixed


---

Comment by was created at 2007-08-19 02:06:59

This is now fixed.
