# Issue 2887: notebook -- greatly optimize by implementing a cached version of get_element

Issue created by migration from https://trac.sagemath.org/ticket/2887

Original creator: was

Original creation time: 2008-04-12 00:20:11

Assignee: boothby

Tom Boothby just did this and here's his code. 

```
var cell_element_cache = [];
function get_cell2(id) {
   var v = cell_element_cache[id];
   if(v == undefined)
       v = cell_element_cache[id] = get_cell(id)
   return v;
}

```




---

Comment by was created at 2008-04-12 04:00:43

I saw benchmarks that show a 5 times speedup for something.  I don't know if
this will be user-visible, but it might be on some machines.  The code itself
works fine and looks good.  I say apply.


---

Attachment

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-12 09:58:26

Resolution: fixed
