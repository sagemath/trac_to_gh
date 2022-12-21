# Issue 1512: write sage --> open_office converter

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-14 21:20:43

Assignee: was


```

William Stein wrote:
> On Dec 14, 2007 9:28 AM, Ted Kosan <ted.kosan`@`gmail.com> wrote:
>> Jason wrote:
>>
>>> What about writing an openoffice function that converts an expression to
>>> openoffice equation format?  For example, the above output is:
>>>
>>> {cos(1)} over {sin(1)} - {(sin(1)^2 + cos(1)^2) cdot (x-1)} over
>>> {sin(1)^2} + {(cos(1) cdot sin(1)^2 + cos(1)^3) cdot ((x-1)^2)} over
>>> {sin(1)^3}
>>>
>>> (just paste that into the equation editor of openoffice and the equation
>>> pops up in your document).
>>>
>>> The syntax is looser than latex, but I think it's probably doable and
>>> probably just a modification of the latex function.  While it might be
>>> nice to insist on everyone downloading a latex macro and learning a bit
>>> of latex, having an openoffice export function makes Sage that much more
>>> accessible.
>> I am in the process of writing educational materials which show high
>> school students how to use SAGE with OpenOffice to create technical
>> documents and an OpenOffice export function would be very helpful for
>> this.  Does anyone have a feel for how difficult it would be to write
>> a function like this?
>
> What needs to be done is to write in Python a latex --> open office format
> converter, probably with a bunch of regexp's, etc.  How hard is that?

To get someone started, here are the rules I used above, with a bit of
extra grouping (the {} brace pairs) to make sure things work out all right.

\frac{a}{b} -> {{a} over {b}}

\sin -> sin

\cos -> cos

\cdot -> cdot

also, I saw that:

\left( -> left (
\right) -> right )

etc.

Whoever does it might click through the openoffice equation toolbar
which gives the openoffice code for the various symbols.
```



---

Comment by tkosan created at 2007-12-16 08:35:38

Changing assignee from was to tkosan.


---

Comment by schilly created at 2008-01-18 21:55:29

Doesn't use OOo MathML inside the ODF document? You can import MathML in OOo this way:

Writer -> Insert -> Object -> Formula - then there: Open -> MathML 1.01

So I would suggest to write a *formula to MathML converter*, since this could be also used inside e.g. HTML pages. (firefox renders them ...)


---

Comment by tkosan created at 2008-02-21 07:43:27

Resolution: wontfix


---

Comment by tkosan created at 2008-02-21 07:43:27

The next major release of OpenOffice will have LaTeX capabilities so a LaTeX to open_office converter will not be needed.
