# Issue 5355: QQbar should have a coercion from number fields with embedding

archive/issues_005355.json:
```json
{
    "body": "Assignee: cwitty\n\nIf a number field comes with an embedding into the complex numbers, QQbar should allow coercions (or at least conversions) from that number field.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5355\n\n",
    "created_at": "2009-02-24T04:14:09Z",
    "labels": [
        "component: coercion"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "QQbar should have a coercion from number fields with embedding",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5355",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

If a number field comes with an embedding into the complex numbers, QQbar should allow coercions (or at least conversions) from that number field.

Issue created by migration from https://trac.sagemath.org/ticket/5355





---

archive/issue_comments_041175.json:
```json
{
    "body": "This should not be hard.  Here is what I propose:\n\n* Given a number field K and an emebedding of K into RR or CC, return the corresponding embedding of K into QQbar.  This just requires selecting from K.embeddings(QQbar) the one which maps K.gen() to the element of QQbar closest to the image of K.gen() under the given embedding.  As a variation, if the given embedding was into RR then the output could be an embedding into AA>\n\n* As a default we could give no embedding and then use K.gen().complex_embedding() instead.\n\nUsing the default there would be a coercion possible from K to QQbar; but the  first version would allow the user flexibility.",
    "created_at": "2009-05-20T19:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5355#issuecomment-41175",
    "user": "https://github.com/JohnCremona"
}
```

This should not be hard.  Here is what I propose:

* Given a number field K and an emebedding of K into RR or CC, return the corresponding embedding of K into QQbar.  This just requires selecting from K.embeddings(QQbar) the one which maps K.gen() to the element of QQbar closest to the image of K.gen() under the given embedding.  As a variation, if the given embedding was into RR then the output could be an embedding into AA>

* As a default we could give no embedding and then use K.gen().complex_embedding() instead.

Using the default there would be a coercion possible from K to QQbar; but the  first version would allow the user flexibility.



---

archive/issue_comments_041176.json:
```json
{
    "body": "Related: #12715",
    "created_at": "2014-02-16T14:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5355#issuecomment-41176",
    "user": "https://github.com/mezzarobba"
}
```

Related: #12715



---

archive/issue_comments_041177.json:
```json
{
    "body": "We do have\n\n```\nsage: K.<a> = NumberField(x^3 - 7, embedding=AA(7)**(1/3))\nsage: AA.has_coerce_map_from(K)\nTrue\nsage: K.<a> = NumberField(x^3 - 7, embedding=QQbar(7)**(1/3) * QQbar.zeta(3))\nsage: QQbar.has_coerce_map_from(K)\nTrue\n```\nIsn't it enough? What should be simplified is to automatized the embedding into `AA`/`QQbar`. And it is more or less the purpose of #19356.",
    "created_at": "2016-03-11T20:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5355#issuecomment-41177",
    "user": "https://github.com/videlec"
}
```

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

archive/issue_comments_041178.json:
```json
{
    "body": "Changing keywords from \"\" to \"qqbar, coercion\".",
    "created_at": "2019-04-22T13:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5355#issuecomment-41178",
    "user": "https://github.com/jplab"
}
```

Changing keywords from "" to "qqbar, coercion".



---

archive/issue_comments_041179.json:
```json
{
    "body": "There are memory-leak implications on this: Coercions are normally cached on the codomain (in this case QQbar). Having a coercion from a number field K to QQbar would imply a reference from QQbar to K. Some effort is made to not make that reference a strong one right from the start (this is why the coercion framework tries to use weak references to the domain), but you'd have to test this quite carefully. Thanks to the complicated interactions with the (weak) dictionaries, I expect that some indirect memory leaks would be introduced.",
    "created_at": "2019-04-22T20:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5355#issuecomment-41179",
    "user": "https://github.com/nbruin"
}
```

There are memory-leak implications on this: Coercions are normally cached on the codomain (in this case QQbar). Having a coercion from a number field K to QQbar would imply a reference from QQbar to K. Some effort is made to not make that reference a strong one right from the start (this is why the coercion framework tries to use weak references to the domain), but you'd have to test this quite carefully. Thanks to the complicated interactions with the (weak) dictionaries, I expect that some indirect memory leaks would be introduced.



---

archive/issue_comments_041180.json:
```json
{
    "body": "Replying to [comment:3 vdelecroix]:\n> We do have\n> \n> ```\n> sage: K.<a> = NumberField(x^3 - 7, embedding=AA(7)**(1/3))\n> sage: AA.has_coerce_map_from(K)\n> True\n> sage: K.<a> = NumberField(x^3 - 7, embedding=QQbar(7)**(1/3) * QQbar.zeta(3))\n> sage: QQbar.has_coerce_map_from(K)\n> True\n> ```\n> Isn't it enough? What should be simplified is to automatized the embedding into `AA`/`QQbar`. And it is more or less the purpose of #19356.\n\nTo automate the embedding, what should be the interface, perhaps something like this?\n\n```\nK.<a> = NumberField(x^3 - 7, embedding=1.9, embedding_field=AA)\n```",
    "created_at": "2019-04-22T22:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5355#issuecomment-41180",
    "user": "https://github.com/mkoeppe"
}
```

Replying to [comment:3 vdelecroix]:
> We do have
> 
> ```
> sage: K.<a> = NumberField(x^3 - 7, embedding=AA(7)**(1/3))
> sage: AA.has_coerce_map_from(K)
> True
> sage: K.<a> = NumberField(x^3 - 7, embedding=QQbar(7)**(1/3) * QQbar.zeta(3))
> sage: QQbar.has_coerce_map_from(K)
> True
> ```
> Isn't it enough? What should be simplified is to automatized the embedding into `AA`/`QQbar`. And it is more or less the purpose of #19356.

To automate the embedding, what should be the interface, perhaps something like this?

```
K.<a> = NumberField(x^3 - 7, embedding=1.9, embedding_field=AA)
```
