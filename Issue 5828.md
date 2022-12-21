# Issue 5828: number fields -- serious bug in coercion to a relative extension of degree 1

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-20 03:58:47

Assignee: was

CC:  robertwb mstreng


```


On Sun, Apr 19, 2009 at 10:16 AM, Utpal Sarkar <doetoe`@`gmail.com> wrote:
>
> Hi,
>
> I found some strange behaviour of the Hilbert class field of a
> quadratic number field when the class number is 1, so the Hilbert
> class field is equal to the ground field:
> sage: K.<w> = QuadraticField(-5); KX.<X> = K[]; H.<h> =
> K.hilbert_class_field()
> sage: (X + w + 1).base_extend(H)
> X + w + 1
> No problem: the Hilbert class field is a proper extension, and the
> polynomial remains the same.
>
> sage: K.<w> = QuadraticField(-1); KX.<X> = K[]; H.<h> =
> K.hilbert_class_field()
> sage: (X + w + 1).base_extend(H)
> X + 1
> In this case the Hilbert class field is equal to K, and the part of
> the polynomial that is not in QQ disappears.

You've found a bug in the coercion in the special case of a relative extension of degree 1.
Here's some simpler code to illustrate it:

sage: K.<w> = QuadraticField(-1)
sage: KX.<X> = K[]
sage: H.<h> = K.extension(X-1)
sage: H(w)
0

The internal function responsible for the bug is:

sage: H._NumberField_relative__base_inclusion(w)
0
```



---

Comment by davidloeffler created at 2009-07-21 08:04:40

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:04:40

Changing assignee from was to davidloeffler.


---

Comment by lftabera created at 2010-07-02 13:27:17

Changing status from new to needs_review.


---

Comment by lftabera created at 2010-07-02 13:27:17

This is solved now (4.4.4)


```
sage: K.<w> = QuadraticField(-1)
sage: KX.<X> = K[]
sage: H.<h> = K.extension(X-1)
sage: H(w)
w
sage: H._NumberField_relative__base_inclusion(w)
w
```



```
sage: K.<w> = QuadraticField(-1);
sage: KX.<X> = K[]
sage: H.<h> =K.hilbert_class_field()
sage: (X + w + 1).base_extend(H)
X + w + 1
```


The bug should be closed, at most add the attached doctest.


---

Comment by mstreng created at 2010-07-22 17:54:41

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2010-07-22 17:54:41

The tests should be indented, and you should only have "::" only on the last line before the test.
The patch now has

```
        TESTS::

        Check that #5828 is solved::

        sage: K.<w> = QuadraticField(-1)
        sage: KX.<X> = K[]
        sage: H.<h> = K.extension(X-1)
        sage: H(w)
        w
```

but I think it should be

```
        TESTS:

        Check that #5828 is solved::

            sage: K.<w> = QuadraticField(-1)
            sage: KX.<X> = K[]
            sage: H.<h> = K.extension(X-1)
            sage: H(w)
            w
```



---

Comment by mstreng created at 2010-07-22 17:54:41

Changing priority from critical to minor.


---

Attachment

You are right, 

I have updated the patch accordingly.

Thanks


---

Comment by lftabera created at 2010-07-26 12:52:15

Changing status from needs_work to needs_review.


---

Comment by mstreng created at 2010-07-31 13:29:01

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-09 09:41:18

Resolution: fixed
