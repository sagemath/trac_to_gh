# Issue 5656: add hint to lift() function to docstring of groebner_basis()

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-04-01 11:25:00

Assignee: malb

Keywords: docstring, doc, Groebner basis

On [sage-support]:
> > On Tuesday 31 March 2009, Florian wrote:
> > Hello everyone,
> > 
> > I've been trying to figure out whether the following 
> > functionality is implemented, but so far I could not. I was 
> > hoping that anyone would know if it existed and in that case 
> > what the syntax is.
> > 
> > Suppose you computed the reduced Groebner Basis G of an ideal 
> > I= (f1,...,fn) in some polynomial ring R, and suppose that 
> > that Groebner Basis turned out to be G=(1). Is there a 
> > function that finds some, maybe even all, combinations of 
> > coefficients h1,...,hn such that h1*f1+...+hn*fn=1?
> > 
> > This is basically a byproduct of e.g. the Buchberger 
> > Algorithm. The question is whether this information can be 
> > accessed.

Martin answers ... and William Stein replies:
> Martin, since this is a frequently asked question, do you think
> something about this should be added to the groebner_basis 
> docstring?  The groebner_basis docstring is 3 pages right now, so 
> this shouldn't be too far down there.


---

Attachment


---

Attachment

revision of Martin's patch


---

Comment by burcin created at 2009-06-04 13:58:22

I posted a revised version of Martin's patch, attachment:trac_5656-gb_lift-revised.patch, the changes are:

 * fix places where !`` was used for math instead of `
 * provide a link to the .lift() method
 * remove the long lines in the INPUT section


---

Comment by mhansen created at 2009-06-04 18:28:25

Resolution: fixed


---

Comment by mhansen created at 2009-06-04 18:28:25

Merged trac_5656-gb_lift-revised.patch in 4.0.1.rc1.
