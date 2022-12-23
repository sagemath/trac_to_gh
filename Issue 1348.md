# Issue 1348: Incorporate Jan Groenewald's documentation fixes

Issue created by migration from https://trac.sagemath.org/ticket/1348

Original creator: mabshoff

Original creation time: 2007-12-01 10:08:57

Assignee: tba


```
On to the good stuff:

General comments and questions regarding this document should be sent by
email to wst...@gmail.com. If you are able to provide suggested text,
either to replace existing incorrect or unclear material, or additional
text to supplement what's already available, we'd appreciate the
contribution.
</snip>
^^ Fix that notice to point to sage-support

In the tutorial, all main page titles at the top seem to
be lower case only. e.g.

2.10.2 systems of des using laplace transforms
Should read Systems of DEs...
(Firefox on Feisty)

2.10.2, few lines on: equatoins should read equations

3.9 saving and loading complete sessions
Some of the yellow blocks of unix shell code around section 3,
which should be <pre> is displaying with italics and font errors.
In secion 3.9 for instance, the first yellow code block, only
~/tmp is in verbatim font, then follows italic, larger, sagesage: ...
When I view page source I get (should that not all be class="verbatim"?):
<div class="verbatim"><pre>~/tmp<span class="math"> sage sage: E =
EllipticCurve('11a') sage: M = ModularSymbols(37) sage: a = 389 sage: t
# M.T(2003).matrix(); t.charpoly().factor()  _4
12)^2 * (x + 54)^2 </pre>...

3.10 the notebook interface:
"displaces the SAGE notebook webpage."
should read
"displays the SAGE notebook webpage."

4.2 GAP
SAGE comes with GAP 4.4.7 for computational discrete mathematics,
especially group theory.
Should read "4.4.10" by now.

4.2 GAP (occurs elswhere too) The last line, <code><span
class="math">SAGE_ROOT/local/lib/gap-4.4.7/pkg</code>.
the _R is rendered as a subscript. The text is large and italic.
Should be verbatim.

4.4 maxima
The yellow code blocks show "sage.:" as the sage prompt,
not "sage:".

5.1 loading and attaching sage files
In particular, attach has the side effect of (auto-reload), very handy
when debugging code, while load does not.
^^ What are the parentheses for?

6.1.2 how some python annoyances are resolved in sage
Integer division: The expression 2/3 has much different behavior in
Python than in any standard math system. In Python, if m  and n  are
ints then m/n  is also an int, namely the quotient of m  divided by n .
Therefore 2/3=0 . This illustrates how Python is similar to C in many
ways (arrays are also indexed starting at 0). There has been talk in the
Python community about changing Python so 2/3 returns the floating point
number 0.6666..., and making 2//3 return 0 .
^^^^^^^^^ my comment:
"from __future__ import" division will import the future behaviour,
apparantly as of python3.0, which is / real division and // integer
division.

6.3 how do i reference sage?
If you write a paper using SAGE, please reference computations done with
SAGE by including
[SAGE], SAGE Mathematical Software, Version 2.6, http://www.sagemath.org
^^^
How about a function bibtex() similar to latex() which gives a bibtex
entry? Coudl default to bibtex(sage) but could also provide
bibtex(pari), bibtex(gp), bibtex(Singular), etc.

If you happen to have just read straight through this tutorial, and have
some sense of how long it took you, please let me know (email
wst...@gmail.com).
^^^ Uhm, I did an hour or two yesterday and an hour or two today.
Not sure. It's much more of a showcase() than a tutorial(). It has a
heavy algebraic slant, and most students start learning more numerical
work. ODE and Statistics examples would be great (I know, I know, submit
them, I'm trying to learn SAGE!). We teach almost exclusively scipy
at www.aims.ac.za now, but some lecturers still teach Maxima, Octave,
and R, even Singular and GAP, and I would like to see them unified via SAGE,
probably. 
```



---

Comment by mhansen created at 2007-12-06 09:15:13

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2007-12-06 09:15:13

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-07 21:41:18

I'm going to split off the last suggestion into a separate ticket.


---

Attachment


---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2007-12-09 10:31:23

Resolution: fixed


---

Comment by mabshoff created at 2007-12-09 10:31:23

Merged in 2.9.alpha2.


---

Comment by mvngu created at 2010-03-04 23:52:19

Replying to [comment:3 mhansen]:
> I'm going to split off the last suggestion into a separate ticket.

See #1422 for a ticket to implement such a BibTeX function.
