# Issue 2385: [with patch, needs review] Multivariate Polynomial coefficients

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2008-03-04 16:19:35

Assignee: was

This patch adds a polynomial_coefficient method which aims to replace the coefficient method for mpolynomials.

Some problems with the coefficient function are:

```
sage: R.<x,y,z>=ZZ[]
sage: f=(x^2-2)*(y-1); f
x^2*y - x^2 - 2*y + 2
sage: f.coefficient(R(1))
2
sage: f.coefficient(x^2)
y - 1
sage: f.polynomial_coefficient({x:0})
-2*y + 2
```

Note that ZZ and QQ are not consistent in this either:

```
sage: R.<x,y,z>=QQ[]
sage: f=(x^2-2)*(y-1); f
x^2*y - x^2 - 2*y + 2
sage: f.coefficient(R(1))
x^2*y - x^2 - 2*y + 2
```


Some of the problems are that there is no way to state that I want all the terms which do not have x.  The polynomial_coefficient method fixes that by taking a dictionary with degrees.

I don't think the patch I posted is the end of the story on this.  I believe that the coefficient method should be a synomyn for polynomial_coefficient or monomial_coefficient.  I'm not sure which.  I'm also not sure what the best parameters are for polynomial_coefficient.  The dictionary syntax is my preferred, but I'm aware that some people may not like dictionaries quite as much as I do.


---

Comment by jbmohler created at 2008-03-04 16:24:47

Changing component from algebraic geometry to commutative algebra.


---

Comment by jbmohler created at 2008-03-04 16:24:47

Perhaps I should also mention that I commented out the gens method (in both implementations).  I'm not aware of any reason that the ParentWithGens caching implementation of this is not the preferred option.


---

Comment by jbmohler created at 2008-03-04 16:24:47

Changing assignee from was to malb.


---

Comment by cremona created at 2008-03-06 18:01:43

One comment:  if I ever asked a polynomial for a specific coefficient, I would expect the result to be in the base ring *not* in the polynomial ring.  Why did you do that?


---

Comment by jbmohler created at 2008-03-10 18:07:28

I'm not sure what you meant by "specific coefficient".  Did you mean situation !#1 or !#2 below?

```
sage: R.<x,y,z>=ZZ[]
sage: f=(x^2+1)*(y-1)
# Situation 1
sage: f.monomial_coefficient(x^2)
-1
sage: f.monomial_coefficient(x^2).parent()
Integer Ring
# Situation 2
sage: f.polynomial_coefficient({x:2})
y - 1
sage: f.polynomial_coefficient({x:2}).parent()
Multivariate Polynomial Ring in x, y, z over Integer Ring
```


I took the word specific to imply situation 1 which seems to me the code does what you say it should do.

If you are meaning situation 2, then I didn't put the result in the ring ZZ[y,z] simply because I didn't really appreciate it in my computational context.  One reason not to create the new ring ZZ[y,z] would be speed concerns both at creation and with later arithmetic.  That is, it could be that I really do want to do arithmetic with this coefficient in the large ring and this is a moderately expensive coercion -- certainly something you would not want to do inside of a tight loop.

However, the parent of the result of polynomial_coefficient is a very legitimate point to discuss.  I think my speed concerns are valid and sufficient argument, but this is one of the reasons that I don't think this patch is the final word on this point.


---

Comment by cremona created at 2008-03-10 19:10:17

Sorry not to be more specific.

In your example, the ring is Z[x,y,z] and I would expect the coefficient of any monomial `x<sup>a*y</sup>b*z^c` to be an integer (where here a,b,c may be 0).  In particular, if I asked for the coefficient of `x^a` I would only expect the integer coefficient of `x<sup>a*y</sup>0*z^0` and *not* a polynomial in y,z (together with an implied identification of Z[x,y,z] with Z[y,z][x]).

In other words, ever polynomial ring has a base (coefficient) ring and I would expect the polynomial_coefficient() function to return an element of that ring.

You are providing more functionality than that (in your Situation 2).  I can certainly imagine situations where that is what I would need, but then I would expect the result to be an element of a ring in fewer variables.  I agree that this function should not create further rings unless necessary (such as ZZ[y,z] in this case) -- but the user might be prepared to create that themselves (as a subring?), and then how would the result of your f.polynomial_coefficient({x:2}) be coerced into it?


---

Comment by jbmohler created at 2008-03-10 21:31:57

So, the crux of the matter (at least, my reading) is that the name of the function 'polynomial_coefficient' led you to believe it answered a fundamentally different question than I made the function to answer.  That is, I think you should be looking at 'monomial_coefficient' -- it does exactly what you want.

I understand your confusion and I don't like the names of these functions either.  I'm somewhat stumped about better alternatives though.  Please make suggestions.


---

Comment by cremona created at 2008-03-10 22:57:55

I now understand -- and apologise, since I had not fully appreciated the crucial distinction between the existing function monomial_coefficient() and the new one polynomial_coefficient().

Now I understand this distinction, it is important that other Sage users and developers do too -- and that means including some more cross-referencing in the docstrings.  At the very least there should be "see also polynomial_coefficient()" to the doc for monomial_coefficient(), as well as  vice versa (which I can see in your patch, but not the former).

Also, can you give a more precise but succinct definition of your polynomial_coefficient() function, more than just examples?

Lastly, in your docstrings you descibe the parameter as a "list" while it is in fact a Python dict.  That needs changing.

Sorry to be so picky -- the basic idea is certainly a good one.


---

Attachment

Thanks very much for the comments.  I think that documentation is the principal hurdle this patch faces so I want to get it right!  I posted a new patch to address your comments.

Replying to [comment:6 cremona]:
> Also, can you give a more precise but succinct definition of your polynomial_coefficient() function, more than just examples?

Well, I actually thought my description was pretty good.  It's sort of difficult to get succinct.  Feel free to post better alternatives to the first paragraph of polynomial_coefficient doc-string.


---

Comment by cremona created at 2008-03-12 09:21:06

Having read it again, I now think that it is extremely clear, and am happy to give the whole thing a positive review.

I get the feeling that my review of this just served to delay adoption of the patch.  If so, sorry!


---

Comment by mabshoff created at 2008-03-12 22:04:40

Merged in Sage 2.10.4.alpha0


---

Comment by mabshoff created at 2008-03-12 22:04:40

Resolution: fixed
