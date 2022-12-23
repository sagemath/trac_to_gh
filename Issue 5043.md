# Issue 5043: gap_console help broken

Issue created by migration from https://trac.sagemath.org/ticket/5043

Original creator: was

Original creation time: 2009-01-21 05:42:07

Assignee: was


```


On Tue, Jan 20, 2009 at 8:03 PM, davidp <davidp@reed.edu> wrote:
>
> I will be teaching abstract algebra this semester and want to
> introduce my students to Sage and GAP.  I have installed
> gap_packages-4.4.10_6, but I am still having trouble with
> documentation:
>
> ----------------------------------------------------------------------
> | Sage Version 3.2.3, Release Date: 2009-01-05                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: gap_console()
> GAP4, Version: 4.4.10 of 02-Oct-2007, i686-pc-linux-gnu-gcc
> gap> ?SymmetricGroup
> Help: Showing `Reference: SymmetricGroup'
> Record: '<rec>.tempfile' must have an assigned value at
> str := OutputTextFile( $SAGE.tempfile, false );
>  called from
> HELP_VIEWER_INFO.(viewer).show( data ); called from
> HELP_PRINT_MATCH( i ); called from
> HELP_SHOW_MATCHES( books, str, true ) called from
> <function>( <arguments> ) called from read-eval-loop
> Entering break read-eval-print loop ...
> you can 'quit;' to quit to outer loop, or
> you can 'return;' after assigning a value to continue
> brk>
>
>
> I am running Sage on a thinkpad with Fedora 10.
>
> Any suggestions would be appreciated.

The above happens because the default GAP workspace evidently that messes up the help system.  I think this is a bug (?), probably in GAP. 

You can do the following instead:

sage: gap_console(False)
...

Or

sage: gap.SymmetricGroup?            # <--- i like this


William
```



---

Comment by was created at 2009-01-21 10:18:00


```
#
# SAGE support utilities to read into the GAP session.
#
$SAGE := rec();

$SAGE.OldPager := Pager;


$SAGE.NewPager :=
         function( data )
   local   str,  lines,  line, fn, start;

   str := OutputTextFile($SAGE.tempfile,false);
   start := 1;

but never sets $SAGE.tempfile anywhere.

Steve
- Show quoted text -


On 21 Jan 2009, at 06:39, William Stein wrote:

    On Tue, Jan 20, 2009 at 8:03 PM, davidp <davidp@reed.edu> wrote:


        I will be teaching abstract algebra this semester and want to
        introduce my students to Sage and GAP.  I have installed
        gap_packages-4.4.10_6, but I am still having trouble with
        documentation:

        ----------------------------------------------------------------------
        | Sage Version 3.2.3, Release Date: 2009-01-05                       |
        | Type notebook() for the GUI, and license() for information.        |
        ----------------------------------------------------------------------
        sage: gap_console()
        GAP4, Version: 4.4.10 of 02-Oct-2007, i686-pc-linux-gnu-gcc
        gap> ?SymmetricGroup
        Help: Showing `Reference: SymmetricGroup'
        Record: '<rec>.tempfile' must have an assigned value at
        str := OutputTextFile( $SAGE.tempfile, false );
        called from
        HELP_VIEWER_INFO.(viewer).show( data ); called from
        HELP_PRINT_MATCH( i ); called from
        HELP_SHOW_MATCHES( books, str, true ) called from
        <function>( <arguments> ) called from read-eval-loop
        Entering break read-eval-print loop ...
        you can 'quit;' to quit to outer loop, or
        you can 'return;' after assigning a value to continue
        brk>


        I am running Sage on a thinkpad with Fedora 10.

        Any suggestions would be appreciated.


    The above happens because the default GAP workspace evidently that
    messes up the help system.  I think this is a bug (?), probably in
    GAP.

    You can do the following instead:

    sage: gap_console(False)

    which will give you a gap session that by default has less
    functionality loaded than otherwise.

    ...

    Or

    sage: gap.SymmetricGroup?            # <--- i like this

    I've made this bug trac #5043:

             http://trac.sagemath.org/sage_trac/ticket/5043

    I've also cc'd Steve Linton in case he has any remarks.

    -- William


Steve Linton    School of Computer Science  &
```



---

Attachment


---

Attachment


---

Comment by iandrus created at 2012-06-05 18:02:52

Changing status from new to needs_review.


---

Comment by iandrus created at 2012-06-05 18:02:52

Since a console session and a session driven through expect are somewhat different, I think it makes sense to source a different file.  I could have made it so that `console.g` reads in `sage.g` if it wasn't already loaded, but I didn't see much use for the stuff in `sage.g` when interacting directly with GAP.  

This means there could be problems (I haven't tested) if someone calls `SaveWorkspace` and overwrites Sage's workspace with one in which `$SAGE` is not set.  However, it is currently possible to do that anyway though perhaps not quite as easily.  A much simpler way to mess things up is calling `$SAGE.StartInteract()` which screws with the expect interaction.


---

Comment by kcrisman created at 2012-06-29 02:30:52

Ivan, do you think this might help #3152 as well?


---

Comment by iandrus created at 2012-06-29 07:55:33

Replying to [comment:3 kcrisman]:
> Ivan, do you think this might help #3152 as well?

I just tested and sadly it doesn't.


---

Comment by kcrisman created at 2012-07-05 15:41:36

This does fix the problem as stated, and of course the behavior with `False` remains the same.  The code makes sense, though I had to learn a little bit about how GAP does these things and our interface.

The issue with saving... I mean, when this is called, `$SAGE` is set, right?  So I'm not sure that this is really causing any new problems.  What use case are you worried about?  The `-L` isn't even called if we do `gap_console(False)`, and if one does `True` (default) then everything is the same as it was... I'm missing something here.  Unless you think of what the case was where this is really different from the previous behavior, positive review.

Patchbot, apply [attachment:trac_5043-extcode-gap-console-help.patch] to the extcode repository and [attachment:trac_5043-gap-console-help.patch] to the Sage library.


---

Comment by kcrisman created at 2012-07-05 15:41:36

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-07-07 22:29:10

Resolution: fixed
