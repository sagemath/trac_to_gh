# Issue 821: K.fractional_ideal(...)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-04 04:59:48

Assignee: was

Change K.ideal to K.fractional_ideal for number fields. 


```
On 10/3/07, Soroosh Yazdani <syazdani`@`math.berkeley.edu> wrote:
> 
> I think what you're saying makes sense. Maybe introduce a method
> fractionalideal, specific to number fields?

It should be 

    K.fractional_ideal(...)

I agree.  I've opened a trac ticket (and accepted it):
   

> 
> Soroosh
> On Wed, Oct 03, 2007 at 10:44:49AM -0400, David Harvey wrote:
> > I find this very confusing:
> >
> > sage: F.<a> = QuadraticField(-5)
> > sage: F.ideal(6)
> > Fractional ideal (6) of Number Field in a with defining polynomial
> > x^2 + 5
> >
> > sage: QQ.ideal(6)
> > Principal ideal (1) of Rational Field
> >
> > This means that if I write code that can work over an arbitrary
> > number field, I have to write special cases for Q. I think it's a bad
> > idea to use the name "ideal" for the method that gives an ideal of
> > the ring of integers. I think we should give this a different name.
> >
> > Any thoughts?
> >
> > david
> >
> >
> >
> 

```



---

Comment by was created at 2007-10-04 04:59:54

Changing status from new to assigned.


---

Comment by was created at 2007-11-03 15:30:20

This is much harder than it looks...


---

Comment by AlexGhitza created at 2008-02-17 02:13:50

I think this has been done already; in sage-2.10.1, number fields have a method .fractional_ideal(), and .ideal() is simply an alias for it.


---

Comment by was created at 2008-02-27 18:50:34


```
10:47 < mhansen_> wstein: Is #821 fixed?
10:49 < wstein> mhansen_ -- 821 is not fixed.
10:49 < wstein> I think it would be trivial to fix.
10:49 < wstein> I would be ok with just making it so this works:
10:49 < wstein> sage: QQ.fractional_ideal(6)
10:50 < wstein> I.e., adding fractional_ideal = ideal in the rational_field.py code.
10:50 < wstein> Then the ticket could be closed.

```



---

Comment by was created at 2008-02-27 18:52:21

It might also be good to deprecate the ideal function for a number field completely, since it is confusing that the result is not an ideal of the number field, but a fractional ideal of the ring of integers.  We could fully support ideals of K, but that could be really confusing and bug prone.  The best thing would be to make

```
 def ideal(self, ...):
```

for number fields raise a clear exception (ValueError or NotImplementedError) that said "use fractional_ideal" instead.


---

Comment by mabshoff created at 2008-04-20 05:52:43

Fixed some time before Sage 3.0.rc0: 

```
[07:00] <mabshoff> wstein: what is your take on #821 ?
[07:10] <wstein> close #821.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 05:52:43

Resolution: fixed
