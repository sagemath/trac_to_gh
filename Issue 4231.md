# Issue 4231: magma -- long input too verbose in some cases

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-01 16:18:13

Assignee: was

CC:  georgsweber


```
> temp2 := Derivative(temp[1],w) + Derivative(temp[2],x) +
> Derivative(temp[3],y) + Derivative(temp[4],z);
> ---
> I get the funny error message:
> ---
> Loading
> "/home/r1/kedlaya/.sage//temp/DWORK.MIT.EDU/5272//interface//tmp5272"
> ---
> but I think the calculation goes through. I'm guessing this is because
> Magma is returning a long output which gets saved to  a temporary
> file. But does the notebook user really need to see this message? I
> don't.
>
> Incidentally, if I change the last line to the following two lines:
> ---
> temp2 := Derivative(temp[1],w) + Derivative(temp[2],x);
> temp2 := temp2 + Derivative(temp[3],y) + Derivative(temp[4],z);
> ---
> then I don't get any error message.

I believe that Sage uses temp files for inputs larger than a certain
size.  It seems this long input passed that size and you're seeing a
"verbose loading" message.  Not really an error message, but I'm sure
William can add it to his list of Magma interface things to do.

```



---

Comment by was created at 2008-10-01 16:18:24

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2008-10-04 04:46:34

NOTE: I forgot some # optionals, yet again for the doctests.  Those will be in #4240, which should be done within a day.


---

Comment by GeorgSWeber created at 2008-10-05 10:05:07

The first half of the patch does indeed fix the issue reported.

The second half of this patch adds a doctest showing that the patch really works,
more precisely this doctest fails without the patch.

However the new doctest fails also (earlier) if no local magma install may be found.

I'd vote nevertheless to take this patch in right now; and then apply #4240 as soon as possible. Other solution would imply having to change the patch(es) in #4240 accordingly, which seems to be superfluous work.


---

Comment by mabshoff created at 2008-10-11 09:00:36

Better luck next time since I don't want to break the followup patch - which is not ready for review and either way itself needs to add a couple #optional tags anyway.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-12 15:33:49

Resolution: fixed


---

Comment by mabshoff created at 2008-10-12 15:33:49

Merged in Sage 3.1.3.rc0
