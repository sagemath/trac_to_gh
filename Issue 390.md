# Issue 390: update cremona's elliptic curves tables

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-06-22 12:04:37

Assignee: was


```
William Stein 	
to Chris
	
show details
	 5:03 am 
There is a bug in the Cremona tables -- he actually missed some
curves, and I think that is one of them.  I need to update the
SAGE cremona table to match the latest official version of the tables.
I meant to do this but just haven't had the time.
- Hide quoted text -

On 6/20/07, Chris Wuthrich <christian.wuthrich`@`gmail.com> wrote:
>  There is a curve 90288bb1 in Cremona's table (magma has it also in
> its tables), but sage does not know it ?? Why ?
>  On the other hand sage knows a curve of conductor 119997 in the
> tables, which made me think that the upper limit on the conductor was
> 120'000.
>
>  Chris.
```



---

Comment by mabshoff created at 2007-08-23 12:52:51

Is this still an issue?

Cheers,

Michael


---

Comment by was created at 2007-10-20 06:38:11

Done, finally.


---

Comment by was created at 2007-10-20 06:38:11

Resolution: fixed
