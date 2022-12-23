# Issue 3152: notebook -- improve gap-mode help interface

Issue created by migration from https://trac.sagemath.org/ticket/3152

Original creator: was

Original creation time: 2008-05-10 21:28:29

Assignee: boothby


```
On 7/26/07, Dan Christensen <jdc@uwo.ca> wrote:
> Some other minor issues about using GAP within the notebook, under
> 2.7.1.  I've put my entire worksheet in GAP mode using the menu at
> the top.  The following things don't work correctly:
> 0) If I type something that gives an error in GAP, the error
> message is buried in a python exception/backtrace.
> 
> 1) If I type "?SymmetricGroup" (which works within GAP), all I see
> is
> 
>    Help: Showing `Reference: SymmetricGroup'
>    Page from 104
> 
> It's similar with other "?foo" commands.
> 
> 2) If I type "SymmetricGroup?" and hit tab, it shows me help about
> sage's wrapped SymmetricGroup function.  I don't think this will
> be helpful for functions not wrapped by sage.
```



---

Comment by kcrisman created at 2012-06-29 02:30:49

#5043 is conceivably related.


---

Comment by iandrus created at 2012-06-29 07:54:37

I just tried with and without the patch for #5043 and 0 and 1 are unchanged.  2 works correctly, but it's not due to the patch at #5043.


---

Comment by kcrisman created at 2014-12-19 04:32:43

https://github.com/sagemath/sagenb/issues/317


---

Comment by kcrisman created at 2014-12-19 04:32:49

Changing priority from major to minor.


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid
