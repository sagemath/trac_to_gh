# Issue 4945: LaTeX for gp elements shouldn't use verbatim environment

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-01-06 16:56:57

Assignee: cwitty

Keywords: jsmath

Gary wrote: 
 
When using the SAGE notebook with typeset on, the command 

``` 
  gp(2+2) 
}}} 
gives the error `'Unknown environment "verbatim"'`. 
 
Typing 
{{{ 
  gp(2+2) 
}}} 
in the SAGE command line works fine. I think it is a latex output 
error. 
 
I can confirm this bug. It is caused by the generic latex method for Expect elements: 
 
{{{ 
sage: latex(gp(2+2)) 
\begin{verbatim}4\end{verbatim} 
}}} 
 
which apparently doesn't play well with jsMath. 
 
`search_src("begin{verbatim}")` returns 43 hits.


---

Comment by jhpalmieri created at 2009-01-06 18:53:30

| search_src("begin{verbatim}") returns 43 hits
Most of those are in docstrings, so we don't need to worry about them.  I think the only relevant instances are interfaces/expect.py, misc/latex.py, misc/log.py.  I don't understand how verbatim is used in the last two.  The attached patch seems to fix the problem in the first one: `latex(gp(2+2))` works in the notebook now.

(The solution here is to change verbatim to verb -- search misc/all.py for 'verbatim' to see very similar code) and then to use the jsMath 'verb' extension.)


---

Comment by malb created at 2009-01-06 20:00:50

The extra \require{verb} worries me, since it is included each time an element is LaTeXified. Shouldn't it be in some header?

Cheers,
Martin


---

Comment by jhpalmieri created at 2009-01-06 20:11:14

Replying to [comment:2 malb]:
> The extra \require{verb} worries me, since it is included each time an element is LaTeXified. Shouldn't it be in some header?

Yes, maybe it should.  I couldn't figure out where, though.

(For more on the jsMath verb extension, including different ways of loading it, see [this web page](http://www.math.union.edu/~dpvc/jsMath/authors/verb.html).)


---

Comment by jhpalmieri created at 2009-01-06 20:54:28

I just posted a slightly different version of the patch.  It doesn't address malb's issue, but it is a little cleaner: it only includes '\require{verb}' if in notebook mode.


---

Comment by jhpalmieri created at 2009-01-07 00:10:46

Okay, here's a patch which (I think) addresses malb's issue.


---

Attachment

Patch looks good.


---

Comment by mabshoff created at 2009-01-12 02:17:47

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-12 02:17:47

Resolution: fixed
