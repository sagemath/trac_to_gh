# Issue 5355: QQbar should have a coercion from number fields with embedding

Issue created by migration from https://trac.sagemath.org/ticket/5355

Original creator: cwitty

Original creation time: 2009-02-24 04:14:09

Assignee: cwitty

If a number field comes with an embedding into the complex numbers, QQbar should allow coercions (or at least conversions) from that number field.


---

Comment by cremona created at 2009-05-20 19:54:04

This should not be hard.  Here is what I propose:

    * Given a number field K and an emebedding of K into RR or CC, return the corresponding embedding of K into QQbar.  This just requires selecting from K.embeddings(QQbar) the one which maps K.gen() to the element of QQbar closest to the image of K.gen() under the given embedding.  As a variation, if the given embedding was into RR then the output could be an embedding into AA>

    * As a default we could give no embedding and then use K.gen().complex_embedding() instead.

Using the default there would be a coercion possible from K to QQbar; but the  first version would allow the user flexibility.


---

Comment by mmezzarobba created at 2014-02-16 14:12:09

Related: #12715


---

Comment by vdelecroix created at 2016-03-11 20:24:36

We do have

```
sage: K.<a> = NumberField(x^3 - 7, embedding=AA(7)**(1/3))
sage: AA.has_coerce_map_from(K)
True
sage: K.<a> = NumberField(x^3 - 7, embedding=QQbar(7)**(1/3) * QQbar.zeta(3))
sage: QQbar.has_coerce_map_from(K)
True
```

Isn't it enough? What should be simplified is to automatized the embedding into `AA`/`QQbar`. And it is more or less the purpose of #19356.


---

Comment by jipilab created at 2019-04-22 13:48:56

Changing keywords from "" to "qqbar, coercion".


---

Comment by nbruin created at 2019-04-22 20:44:38

There are memory-leak implications on this: Coercions are normally cached on the codomain (in this case QQbar). Having a coercion from a number field K to QQbar would imply a reference from QQbar to K. Some effort is made to not make that reference a strong one right from the start (this is why the coercion framework tries to use weak references to the domain), but you'd have to test this quite carefully. Thanks to the complicated interactions with the (weak) dictionaries, I expect that some indirect memory leaks would be introduced.


---

Comment by mkoeppe created at 2019-04-22 22:42:18

Replying to [comment:3 vdelecroix]:
> We do have
> {{{
> sage: K.<a> = NumberField(x^3 - 7, embedding=AA(7)**(1/3))
> sage: AA.has_coerce_map_from(K)
> True
> sage: K.<a> = NumberField(x^3 - 7, embedding=QQbar(7)**(1/3) * QQbar.zeta(3))
> sage: QQbar.has_coerce_map_from(K)
> True
> }}}
> Isn't it enough? What should be simplified is to automatized the embedding into `AA`/`QQbar`. And it is more or less the purpose of #19356.
To automate the embedding, what should be the interface, perhaps something like this?

```
K.<a> = NumberField(x^3 - 7, embedding=1.9, embedding_field=AA)
```

