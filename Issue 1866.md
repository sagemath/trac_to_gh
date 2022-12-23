# Issue 1866: bug in doctesting -- long time not respected in some contexts

Issue created by migration from https://trac.sagemath.org/ticket/1866

Original creator: was

Original creation time: 2008-01-20 16:47:15

Assignee: failure

CC:  mjo


```
On Jan 20, 2008 7:28 AM, Lars Fischer <> wrote:
> 
> Hello,
> 
> I think I have found a bug:
> chapter 2.4.1 of the Programming guide states, that comments like "#
> long time (!)"  prevents the example from being tested.

Yep, that is a bug.  I've made it. 

> 
> But:
> sage -t quadratic-modules.sage
> sage -t  quadratic-modules.sage
> Example 13 (line 433)
> TIMEOUT!!
> IN:
>  phi.level()
>  phi = fqmodule([11,33]);
>  phi.tau_invariant()
>  phi = fqmodule([11,33]); # long time (!)
>  phi.sigma_invariant()    # long time (!)
> OUT:
> 
> 
> This applies to sage 2.10.
> 
> I think the reason is:
> sage -t calls
> sage-sage and then
> sage-test, which in turns calls
> sage-doctest_tex, if extension is ".sage" instead of sage-doctest.
> 
> At least sage-doctest looks for "long time" inside comment_modifiers()
> and sage-doctest_tex doesnot.
> 
> With best regards,
> Lars Fischer

```


My first thought on reading the above is "get rid of handling .sage files in a special way in order to automatically fix all such issues".   That's what I did with .tex files a while ago. 


---

Comment by mabshoff created at 2008-12-10 07:50:20

I think the issue has been fixed in Sage 3.2.x since we no longer treat .sage files special. Can you verify this?

Cheers,

Michael


---

Comment by mjo created at 2011-12-14 20:21:44

Changing status from new to needs_review.


---

Comment by mjo created at 2011-12-14 20:21:44

This is fixed. A simple test case:


```
$ cat sage_extension_tests.sage 
r"""

A test case for *.sage files.

::

    sage: 1
    1

::

    sage: 2 # long time
    2

::

    sage: 3
    3

"""
```


I see that the long test is skipped normally:


```
$ sage -t -verbose sage_extension_tests.sage
...
5 passed and 0 failed.
```


And executed when -long is passed:


```
$ sage -t -verbose -long sage_extension_tests.sage
...
6 passed and 0 failed.
```



---

Comment by mhansen created at 2011-12-17 20:08:40

Resolution: invalid
