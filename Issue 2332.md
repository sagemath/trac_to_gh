# Issue 2332: notebook -- the evaluate link doesn't

Issue created by migration from https://trac.sagemath.org/ticket/2332

Original creator: was

Original creation time: 2008-02-27 12:50:54

Assignee: boothby

Problems with the evaluate link that appears in the active notebook cell have
been reported by several people on the Sage mailing lists.  Here's the latest
bug report, which has some interesting ideas about possible solutions. 


```

On Tue, Feb 26, 2008 at 8:24 AM, Francis Clarke <> wrote:
> 
>  The "evaluate" links for the notebook introduced in SAGE 2.9.2 have
>  never worked for me (Mac OS X 10.4.11, SAGE 2.9.2 -- 2.10.2 + either
>  Safari or Firefox).  The links appears when they should and seem to be
>  correct, e.g., (reformatted):
>  
>     <a href  = "javascript:evaluate_cell(115,0)"
>        class = "eval_button"
>        id    = "eval_button115"
>        alt   = "Click here or press shift-return to evaluate">
>     evaluate
>     </a>
>  
>  but clicking on the link has no effect.  This is a pity, as it's a
>  (potentially) very nice feature.  The cells evaluate perfectly well
>  with shift-return.

I just want to point out that the evaluate link *does* work for me
and most people in Firefox.   It does not work for me in Safari.
I don't understand why it doesn't work, but all your hints in this
email will help.  Thanks!  We're tracking this issue at 
 

>  
>  Looking at this link, and cell.py line 575, where it's created, I fail
>  to see what is wrong.  Perhaps the javascript function evaluate_cell
>  (defined in js.py) can't be found in this context?
>  
>  One thing I did notice is the attribute
>     alt="Click here or press shift-return to evaluate"
>  There is no alt attribute for the A element in HTML 4.01, so it has no
>  effect here.  Probably 'alt' should be replaced by 'title'.  Though,
>  of course, this isn't the cause of my main problem.
>  
>  
>  A couple of other details from cell.py noticed in passing:
>  
>  line  64: math_parse is defined in html.py not cell.py
>  
>  line 577: has no effect.  Presumably it should have been commented out
>  along with lines 579--584.
>  

```



---

Comment by bill.p created at 2008-03-12 14:20:41

Replying to [ticket:2332 was]:
> Problems with the evaluate link that appears in the active notebook cell have
> been reported by several people on the Sage mailing lists.  Here's the latest
> bug report, which has some interesting ideas about possible solutions. 
> 
> {{{
> 
> On Tue, Feb 26, 2008 at 8:24 AM, Francis Clarke <> wrote:
> > 
> >  The "evaluate" links for the notebook introduced in SAGE 2.9.2 have
> >  never worked for me (Mac OS X 10.4.11, SAGE 2.9.2 -- 2.10.2 + either
> >  Safari or Firefox).  The links appears when they should and seem to be
> >  correct, e.g., (reformatted):
> >  
> >     <a href  = "javascript:evaluate_cell(115,0)"
> >        class = "eval_button"
> >        id    = "eval_button115"
> >        alt   = "Click here or press shift-return to evaluate">
> >     evaluate
> >     </a>
> >  
> >  but clicking on the link has no effect.  This is a pity, as it's a
> >  (potentially) very nice feature.  The cells evaluate perfectly well
> >  with shift-return.
> 
> I just want to point out that the evaluate link *does* work for me
> and most people in Firefox.   It does not work for me in Safari.
> I don't understand why it doesn't work, but all your hints in this
> email will help.  Thanks!  We're tracking this issue at 
>  
> 
> >  
> >  Looking at this link, and cell.py line 575, where it's created, I fail
> >  to see what is wrong.  Perhaps the javascript function evaluate_cell
> >  (defined in js.py) can't be found in this context?
> >  
> >  One thing I did notice is the attribute
> >     alt="Click here or press shift-return to evaluate"
> >  There is no alt attribute for the A element in HTML 4.01, so it has no
> >  effect here.  Probably 'alt' should be replaced by 'title'.  Though,
> >  of course, this isn't the cause of my main problem.
> >  
> >  
> >  A couple of other details from cell.py noticed in passing:
> >  
> >  line  64: math_parse is defined in html.py not cell.py
> >  
> >  line 577: has no effect.  Presumably it should have been commented out
> >  along with lines 579--584.
> >  
> 
> }}}
I found Justin's suggested mod: extend the timeout in cell_blur, to be effective.
Maybe Williams machines are faster than my little laptop. Tried 200ms but that was
unreliable, 250ms seems to work OK.

I await Justin's proposed mods....

Bill


---

Attachment


---

Comment by was created at 2008-03-17 04:28:02

Rock solid (for me and my superfast laptop)!


---

Comment by mabshoff created at 2008-03-17 04:29:50

Merged in Sage 2.10.4.final


---

Comment by mabshoff created at 2008-03-17 04:29:50

Resolution: fixed
