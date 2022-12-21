# Issue 2894: notebook -- cache elements to improve the speed of get_cell()

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-04-12 07:51:42

Assignee: mabshoff

The following code takes .004ms/call, which is about 5 times faster than the existing get_cell():


```
var cell_element_cache = [];
function get_cell2(id) {
    var v = cell_element[id];
    if(v == undefined)
        v = cell_element[id] = get_cell(id)
    return v;
}
```


It follows that we should update get_cell to the 5-times faster version, since get_cell is called  quite frequently in the notebook code.

as tested with


```
var t0;
var e;
var n = cell_id_list[cell_id_list.length-1];
var N = 100000.;
t0 = time_now();
for(i=0;i<N;i++)
   e = get_cell(n);
t1 = time_now();
alert((t1-t0)/N);
```



---

Comment by boothby created at 2008-04-12 07:52:06

Changing type from defect to enhancement.


---

Comment by boothby created at 2008-04-12 07:52:06

Changing component from Cygwin to notebook.


---

Comment by boothby created at 2008-04-12 07:52:06

Changing assignee from mabshoff to boothby.


---

Comment by boothby created at 2008-04-12 07:52:06

Changing priority from major to minor.


---

Attachment


---

Comment by mabshoff created at 2008-04-12 12:44:38

Hi Tom,

this patch is identical to #2887 where William posted your code except for the added comment by you. Since #2887 has been credited to you I will merge the extra comment and close this as fixed.

Thought?

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-12 12:44:38

Resolution: fixed


---

Comment by mabshoff created at 2008-04-12 12:50:48

Since #2887 was merged only merge the extra comment from the previous patch


---

Attachment

Merged trac_2887-comment-from-2894.patch in Sage 3.0.alpha4
