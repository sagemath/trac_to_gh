# Issue 3102: debugging output in p-adics with print mode "digits"

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-05-04 21:54:08

Assignee: mabshoff

Someone apparently forgot to uncomment some debugging code:


```
sage: K = Qp(7, print_mode="digits")
sage: K(1/2)     # ok
...33333333333333333334
sage: K(1/42)    # hmmmmmmmm
['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '6']
-1
['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5']
['6']
...5555555555555555555.6
sage: 
```




---

Comment by dmharvey created at 2008-05-04 21:54:19

Changing assignee from mabshoff to somebody.


---

Comment by dmharvey created at 2008-05-04 21:54:19

Changing component from Cygwin to basic arithmetic.


---

Attachment


---

Comment by cremona created at 2008-09-08 20:05:44

Well, the patch applied fine and doctests pass.  BUT  when I manually type in

```
            sage: K = Qp(7, print_mode="digits")
            sage: repr(K(1/2))
```

I do NOT get what the doctest says I should:

```
            '...3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|4'
```

but instead I get this:

```
'...33333333333333333334'
```


I don't know why the vertial lines a re missing, or whether they should be there;  but I do know that the doctester ignores what comes after three dots ... so any p-adics print mode which includes the dots is going to be rather hard to doctest.


---

Comment by gfurnish created at 2008-09-09 00:16:18

I think this is working as intended -- The other p-adic print statements also have the lines (see line 68).  It seems to be something specific to testing the printer so that it generates different output in doctests and runtime.  It looks like it may be enabling the bars global state early in the tests and never disabling it.


---

Comment by cremona created at 2008-09-09 08:28:57

But in line 68 you have just set the print-mode to "bars", while here you have set the mode to "digits".

I just don't understand the concept of output being different during doctests and runtime!

Regarding your last sentence: each test should be independent of earlier ones surely, starting in a separate Sage session?  How can it be correct to explicitly set the print_mode to "digits" but have a doctest showing that apparantly "bars" is output?

I still find this too confusing.


---

Comment by was created at 2008-09-24 17:35:52

Replying to [comment:6 cremona]:
> But in line 68 you have just set the print-mode to "bars", while here you have set the mode to "digits".
> 
> I just don't understand the concept of output being different during doctests and runtime!
> 
> Regarding your last sentence: each test should be independent of earlier ones surely, starting in a separate Sage session?  How can it be correct to explicitly set the print_mode to "digits" but have a doctest showing that apparantly "bars" is output?
> 
> I still find this too confusing.


John Cremona is definitely right here.


---

Attachment

followup -- apply the above patch *and* this one.


---

Comment by was created at 2008-11-27 07:03:04

I attached a tiny patch that addresses and clarifies some of the issues discussed above.  See #4637 for a ticket for the bug that the above exposes.


---

Comment by craigcitro created at 2008-11-27 07:11:59

Second patch looks good, too.


---

Comment by mabshoff created at 2008-11-28 07:31:58

Merged both patches in Sage 3.2.1.rc0


---

Comment by mabshoff created at 2008-11-28 07:31:58

Resolution: fixed
