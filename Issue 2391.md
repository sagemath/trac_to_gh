# Issue 2391: module docstring bug running filename.sage from the command line

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-05 00:41:57

Assignee: was


```


On Thu, Feb 28, 2008 at 9:36 AM, Kate <kate01123`@`gmail.com> wrote:
> 
>  What gives with the following session below?
>  More specifically, what happens to the file docstring
>  when the file has a .sage extension?

There is a bug in the .sage --> .py conversion process that
your example below illustrates.  We are tracking this at


>  
>  =============== begin shell session ===============
>  
>  $ cat > sanity
>  #!/usr/bin/env sage
>  r"""Here is a docstring for this file."""
>  print __doc__
>  <control-d>
>  $ cat sanity
>  #!/usr/bin/env sage
>  r"""Here is a docstring for this file."""
>  print __doc__
>  $ chmod +x sanity
>  $ ./sanity
>  Here is a docstring for this file.
>  $ cp sanity madness.sage
>  $ ./madness.sage
>  None
>  $
>  
>  =============== end shell session ===============
>  
>  Kate

```



---

Attachment

this fixes the bug and vastly improves the documentation of sage-preparse


---

Comment by mhansen created at 2008-03-05 05:40:01

Works for me against 2.10.3.rc1.  Apply to hg_scripts.


---

Comment by mabshoff created at 2008-03-05 05:47:32

Merged in Sage 2.10.3.rc2


---

Comment by mabshoff created at 2008-03-05 05:47:32

Resolution: fixed
