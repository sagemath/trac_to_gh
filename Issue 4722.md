# Issue 4722: BUG - number field K.hilbert_class_polynomial() is a *lie*

Issue created by migration from https://trac.sagemath.org/ticket/4722

Original creator: was

Original creation time: 2008-12-05 23:04:07

Assignee: was

I'm in a talk right now, and the speaker (Marco from Holland) just pointed out that
Sage's K.hilbert_class_polynomial() function, for K quadratic imaginary, is a *LIE*.
It returns a poly that defines that Hilbert class field, but it is *not* the Hilbert Class Polynomial.

Observe:


```
sage: K.<a> =QuadraticField(-97)
sage: K.hilbert_class_polynomial()
x^4 + 9*x^2 - 6*x + 1
sage: magma(K.discriminant()).HilbertClassPolynomial()
$.1^4 - 750062398364686994581728000*$.1^3 - 20542159225989612130996373047535232000000*$.1^2 + 208224136957169320201407896480139264000000000*$.1 - 1121692648948590091501551223636881408000000000000
```


Solution: change the name of this function and add documentation clarifying this, say including the above example.

The difference is *very* important, given the use of the Hilbert class polynomial in computing elliptic curves with a given number of rational points. 


---

Comment by was created at 2008-12-05 23:06:56

Who to blame?  Either me or David Kohel, since this was done before Sage was under revision control.


---

Comment by kohel created at 2008-12-06 01:08:34

Replying to [comment:1 was]:
> Who to blame?  Either me or David Kohel, since this was done before Sage was under revision control.  

Not me. This is a wrapper for the Pari/gp function quadhilbert.  

I find this unanswered question about what it returns:

http://pari.math.u-bordeaux.fr/archives/pari-users-0402/msg00000.html

Certainly it does not return the hilbert class polynomial (minimal 
polynomial of the j-invariant), rather it returns a "nicer" polynomial 
over QQ which generates the Hilbert class field over K.

I agree that a name change is in order to avoid this confusion, but 
I don't have a suggestion other than 

hilbert_class_field_[relative_]defining_polynomial

which is a bit long, but descriptive.  Note that the hilbert_class_field 
does not have this as a defining polynomial (hence the relative_), 
since it is formed as a compositum of the quadratic and degree h 
extensions rather than a relative extension.

The documentation should also be corrected to say that Schertz's method 
is used (only) for D < 0.  A reference to Schertz's methods and whatever 
method (Stark units?) is used for D > 0 would be desirable.


---

Comment by mabshoff created at 2008-12-06 01:13:29

Hi,

There was a coding sprint project at SD 10 by Eduardo Ocampo-Alvarez and Andrey Timofeev that dealt with the Hilbert class polynomial. Those two guys mentioned to me toward the end of the sprint that the Sage implementation had issues and that they also had fast code written in Sage/Cython, but they never send the code in for review. Maybe someone with a better understanding then me with the math involved should ping them and get them to put their code up for review [and before anyone asks: no, the code isn't linked from the Days 10 coding sprint page :(].

Cheers,

Michael


---

Attachment


---

Comment by AlexGhitza created at 2008-12-11 10:12:05

Looks good.


---

Comment by mabshoff created at 2008-12-11 11:10:07

Merged in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-11 11:10:07

Resolution: fixed
