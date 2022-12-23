# Issue 4575: [with patch, needs review] Option to show nestet lists as html tables

Issue created by migration from https://trac.sagemath.org/ticket/4575

Original creator: whuss

Original creation time: 2008-11-21 09:19:56

Assignee: whuss

The attached patch adds the option table_form to the show() command.

If table_form = True, nested lists are shown in the notebook as nicely
formatted html tables.


---

Attachment

REFEREE REPORT:

Positive review.  Code looks solid and the result is really pretty to look at. 

1. Line 945 contains a trivial typo:

```
935	    Print a nestet list as a html table. 
```


2. The patch isn't a mercurial patch, so... :-(


---

Comment by mabshoff created at 2008-11-28 06:47:20

I turned this diff into a patch with credit to Wilfried and fixed the typo. I also fixed the typo in the summary :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-28 06:48:13

Resolution: fixed


---

Comment by mabshoff created at 2008-11-28 06:48:13

Merged in Sage 3.2.1.rc0


---

Comment by mhansen created at 2008-11-29 18:11:59

I don't agree with William's positive review on this for some design reasons.  First off, it is only useful from the notebook as it just spits out HTML while all other cases of show work fine from the command-line.  Tacking random things and keywords onto show is not a maintainable solution especially since the new functionality is completely orthogonal to what's already there.

Instead this should be some function in a module for creating HTML output of objects.


---

Comment by mabshoff created at 2008-11-29 18:15:56

Replying to [comment:4 mhansen]:
> I don't agree with William's positive review on this for some design reasons.  First off, it is only useful from the notebook as it just spits out HTML while all other cases of show work fine from the command-line.  Tacking random things and keywords onto show is not a maintainable solution especially since the new functionality is completely orthogonal to what's already there.
> 
> Instead this should be some function in a module for creating HTML output of objects.

Ok, let's take this discussion to sage-devel. I might reverse this patch since Jaap oberved a doctest failure that seems impossible to happen. Another reason to reverse this is that we do not want to ship a show with this option if we are going to break it anyway.

Your idea certainly sounds cleaner.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-11-29 18:41:43

I've attached a patch which implements my idea.  I added a comment about html.nested_list, Since the user would have to read the docstring to the previous keyword anyway.


---

Comment by was created at 2008-11-29 19:02:38

I'm ok with revoking my positive review.  I like Mike's suggestion better.


---

Comment by mabshoff created at 2008-11-29 21:14:40

Ok, can we then get a review on Mike's patch? Since it applies on to of Wilfried's patch we should attempt to get it into 3.2.1.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 05:42:55

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-11-30 05:42:55

Due to the problems with extra mbox{} popping up reported by Jaap, John and also me on some boxen I will revert this patch in 3.2.1.rc1. See also 

http://groups.google.com/group/sage-devel/t/3a6575cb49cd61a8

Reopened. Hopefully Mike Hansen's approach will be merged in 3.2.2.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 05:42:55

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-11-30 05:44:27


```
sage -t  "devel/sage/sage/misc/functional.py"               
********************************************************************** 
File "/home/jaap/work/downloads/sage-3.2.1.alpha2/devel/sage/sage/misc/functiona l.py", line 891: 
     sage: show([(i, j, i == j) for i in [0..1] for j in [0..1]], table_form = True) 
Expected: 
     <html> 
     <div class="notruncate"> 
     <table class="table_form"> 
     <tbody> 
     <tr class ="row-a"> 
     <td><span class="math">0</span></td> 
     <td><span class="math">0</span></td> 
     <td><span class="math">\mbox{\rm True}</span></td> 
     </tr> 
     <tr class ="row-b"> 
     <td><span class="math">0</span></td> 
     <td><span class="math">1</span></td> 
     <td><span class="math">\mbox{\rm False}</span></td> 
     </tr> 
     <tr class ="row-a"> 
     <td><span class="math">1</span></td> 
     <td><span class="math">0</span></td> 
     <td><span class="math">\mbox{\rm False}</span></td> 
     </tr> 
     <tr class ="row-b"> 
     <td><span class="math">1</span></td> 
     <td><span class="math">1</span></td> 
     <td><span class="math">\mbox{\rm True}</span></td> 
     </tr> 
     </tbody> 
     </table> 
     </div> 
     </html> 
Got: 
     <html> 
     <div class="notruncate"> 
     <table class="table_form"> 
     <tbody> 
     <tr class ="row-a"> 
     <td><span class="math">0</span></td> 
     <td><span class="math">0</span></td> 
     <td><span class="math">True</span></td> 
     </tr> 
     <tr class ="row-b"> 
     <td><span class="math">0</span></td> 
     <td><span class="math">1</span></td> 
     <td><span class="math">False</span></td> 
     </tr> 
     <tr class ="row-a"> 
     <td><span class="math">1</span></td> 
     <td><span class="math">0</span></td> 
     <td><span class="math">False</span></td> 
     </tr> 
     <tr class ="row-b"> 
     <td><span class="math">1</span></td> 
     <td><span class="math">1</span></td> 
     <td><span class="math">True</span></td> 
     </tr> 
     </tbody> 
     </table> 
     </div> 
     </html> 
********************************************************************** 
1 items had failures: 
    1 of   5 in __main__.example_53 
***Test Failed*** 1 failures. 
For whitespace errors, see the file /home/jaap/downloads/sage-3.2.1.alpha2/tmp/.doctest_functional.py 
         [11.5 s] 
exit code: 1024 
```



---

Comment by whuss created at 2008-12-03 20:27:54

Replying to [comment:4 mhansen]:
> I don't agree with William's positive review on this for some design reasons.  First off, it is only useful from the notebook as it just spits out HTML while all other cases of show work fine from the command-line.

I agree, It should also do something useful on the command-line.

> Tacking random things and keywords onto show is not a maintainable solution especially since the new functionality is completely orthogonal to what's already there.

> Instead this should be some function in a module for creating HTML output of objects.

This is probably cleaner implementation wise, but I don't think html.nested_list()
is a good userinterface. Why should the user of the notebook need to know the
implementation detail that the output is produced using HTML? And the output of the
function is not really html anyway, but html + latex.

It is also inconsistent, since

sage: html(sin(x)/x)

produces acii art, and not html + jsmath.

There are already at least five functions that produce jsmath output in the notebook,
which all behave differently:

*show():*
    Produces latex in display mode.
    And works with graphic objects of course.

*view():*
    Produces latex in inline mode (which is hard to read in the notebook).
    This has many options that only work on the commandline and with xdvi.
    For graphic objects it returns a string representation.

*typeset():*
    Same behaviour as view() but has no options.

*pretty_print():*
    produces latex in inline mode.

    If used on the graphics objects, it shows it like show().
    But it doesn't accept any options, as show() does.

*jsmath():*
    produces latex in display mode.
    For graphic objects it returns a string representation,
    but inside latex math-mode.

    The docstring says that there is a option mode
    which changes between display and inline mode.

    Unfortunately this only works in doctest mode.
    In the notebook I get:

```
    sage: jsmath(x^2, 'inline')
    Traceback (click to the left for traceback)
    ...
    TypeError: __call__() takes exactly 2 arguments (3 given)
```

Is there a deeper reason why Sage has all these functions? Or have
they just accumulated over the years? A few of these should probably
be deprecated.

In my opinion show() is the best of these, because also x.show() works,
so it is consistent. It's short and easy to remember.
It just needs better documentation.

Would a mode flag for show() like the one for jsmath() be okay? Then
it could be extended in the future without adding additional keywords.

Grettings,
Wilfried


---

Comment by mabshoff created at 2008-12-03 22:12:52

Wilfried,

please post the summary you made above to sage-devel so we can have some design discussion.

Cheers,

Michael


---

Comment by jason created at 2009-04-20 18:53:59

What is the status of this?  I'm needing it pretty often, and end up writing my own every time:


```
def html_table(data):
    html("<table border=1>")
    for row in gg:
        html("<tr>")
        for cell in row:
            html("<td>")
            show(cell)
            html("</td>")
        html("</tr>")
    html("</table>")
```


(it looks nicer if you have #5836 applied)


---

Comment by jason created at 2009-04-20 19:57:11

Note that since #5836 fixes images to show exactly where the call to show() happens, I think it would be great if the fix on this ticket called show(thing in cell) instead of latex(thing in cell).  For text, show outputs latex, so I think it will just expand what you can do (i.e., put graphics in tables and have it show those pictures).


---

Comment by jason created at 2009-04-20 20:02:23

More comments:

 * It would be simpler to have the row classes use itertools.cycle, instead of the modular arithmetic (smaller code size, anyway, and standard python tools)
 * It would be fantastic to be able to easily specify styles, like borders, background colors, heading rows, etc.

and again, the call to latex should be replaced with a call to show() after #5836 is applied.


---

Comment by whuss created at 2009-04-21 14:19:50

contains all previous patches


---

Attachment

Replying to [comment:15 jason]:
> More comments:
> 
>  * It would be simpler to have the row classes use itertools.cycle, instead of the modular arithmetic (smaller code size, anyway, and standard python tools)
>  * It would be fantastic to be able to easily specify styles, like borders, background colors, heading rows, etc.
> 
> and again, the call to latex should be replaced with a call to show() after #5836 is applied.

I attached a new patch, which needs on #5836 to be applied. The command is now called html.table(). itertools.cycle is used, there is a option to use the first row as a heading,
strings are put into the table cells unmodified and also graphic objects are placed into
the table correctly.

It was not possible to just use show() unmodified because this results in nested notebook
cells which render the notebook unusable.


---

Comment by jason created at 2009-04-22 11:03:58

was: this last patch changes show so that show(..., linkmode=True) *returns* a string, rather than just prints a string.  How do you feel about it?

I think it makes things cleaner to do things like the patch does.  There ought to be some way of programmatically getting the output that show would have printed so you can do something with it, like wrap it in td tags as in the patch.


---

Comment by jason created at 2009-05-30 06:55:41

This is a great piece of functionality.  I'm sure I'll use it a lot.

I'm bothered a bit that the cells are automatically "shown" (instead of just printed).  I think I would have called it show.table() and just made it check to make sure we were running in the notebook.  But I also see that this discussion has been had above.  Oh well.  I'm willing to concede the naming for a positive review so that this gets in.

I give this a positive review.  However, we should wait for a couple of days to see if William has something to say about the changes to show().  If he hasn't weighed in on the issue after a while, change this to positive review.


---

Comment by jason created at 2009-05-30 07:06:10

apply on top of previous patch


---

Attachment

The referee patch contains slight doctest fixes so that doctests pass (there were some issues with the latex spacing).


---

Comment by was created at 2009-05-30 13:39:02

I'm ok with the api addition to show.


---

Comment by mhansen created at 2009-06-01 06:26:01

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 06:26:01

Resolution: fixed


---

Comment by mvngu created at 2009-06-04 14:26:20

Replying to [ticket:4575 whuss]:
> The attached patch adds the option table_form to the show() command.
> 
> If table_form = True, nested lists are shown in the notebook as nicely
> formatted html tables.
Can someone upload a screenshot that shows an example of a nicely formatted HTML table. Code sample would be good as well, if relevant. I plan to showcase this ticket in the release tour, and having a visual is worth a thousand words.


---

Attachment


---

Attachment

Replying to [comment:22 mvngu]:
> Can someone upload a screenshot that shows an example of a nicely formatted HTML table. Code sample would be good as well, if relevant. I plan to showcase this ticket in the release tour, and having a visual is worth a thousand words.

The first picture is produced by:


```
sage: functions = [sin(x), cos(x), tan(x), acos(x)]
sage: t = [[f, taylor(f, x, 0, 10)] for f in functions]
sage: html.table([["Function", "Series"]] + t, header = True)
```


It is also possible to put graphic objects into the table:


```
sage: f = 1/x*sin(x)
sage: t = [["Function", "Plot"],[f, plot(f, x, -4*pi, 4*pi)]]
sage: html.table(t, header = True)
```


I hope this helps.


---

Comment by mvngu created at 2009-06-04 15:05:32

Replying to [comment:23 whuss]:
> The first picture is produced by:
<SNIP>
> It is also possible to put graphic objects into the table:
<SNIP>
> I hope this helps.
Holy bitbucket! Those images look drop-dead gorgeous! Thanks, Wilfried.


---

Comment by jason created at 2009-06-04 19:30:28

Also, you can try 


```
html.table([["Graph", "Vertices", "Edges"]] + [(g.plot(), g.order(), g.size()) for g in graphs(3)], header=True)
```


(sorry, I don't have the patch applied right now, so I can't post a screenshot.  It'd be nice if alpha.sagenb.org was updated...)


---

Comment by jhpalmieri created at 2009-06-27 17:27:47

See #6433 for a related issue.
