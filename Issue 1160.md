# Issue 1160: *major* bug in using the sage notebook as a maxima notebook

Issue created by migration from https://trac.sagemath.org/ticket/1160

Original creator: was

Original creation time: 2007-11-12 23:32:32

Assignee: was


```
On Nov 12, 2007 10:20 PM, Moreira <fjm@fc.up.pt> wrote:
> After changing system to Maxima in a worksheet, evaluations of cells
> do not appear. If I write "3+1" in a cell and press SHIFT+ENTER the
> green bar remains. If I interrupt the computation (option in drop down
> menus) then,  the result appears immediately after I press the ok
> button in the  alert message saying "Unable to immediately interrupt
> calculation"
> 
> The same happens if SAGE is chosen as the active system and I begin
> the cell with %maxima.
> 
> However,  writing "maxima(3+1)" the result  appears as expected.
> 
> This happens to me running a vmware image of sage on windows XP and
> accessing SAGE notebook with firefox 2.09. I also tried the notebook
> interface at
> https://sage.math.washington.edu:8103/
> and I obtained the same "behaviour".
> 
> If I  choose other systems (like sh, html,gp)  everything works fine..
> 
> Is anybody experiencing this kind of  behaviour or is only a bug with
> me?!

Yes, I see exactly the same bug.   This is a rather serious bug actually,
and I'm really glad you reported it!  
```



---

Comment by was created at 2007-12-02 03:53:53

Changing status from new to assigned.


---

Comment by was created at 2007-12-02 04:10:03

OK, a lead -- this is caused by line 254 of server/support.py, which calls

```
   maxima.chdir(...)
```

which hangs.


---

Attachment


---

Comment by mabshoff created at 2007-12-02 05:51:56

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 05:51:56

Merged in 2.8.15.alpha2.


---

Attachment


---

Attachment


---

Comment by was created at 2007-12-02 18:49:47

Changing status from closed to reopened.


---

Comment by was created at 2007-12-02 18:49:47

Resolution changed from fixed to 


---

Comment by mabshoff created at 2007-12-02 18:55:06

Merged trac1160-maxima-fix.patch in 2.8.15.rc0.


---

Comment by mabshoff created at 2007-12-02 18:55:06

Resolution: fixed
