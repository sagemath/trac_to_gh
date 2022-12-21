# Issue 6292: Converting elements in AbelianGroup to gap element

Issue created by migration from Trac.

Original creator: jlefebvre

Original creation time: 2009-06-15 04:08:59

Assignee: joyner

Keywords: AbelianGroup

Some trouble in converting elements in AbelianGroup to gap elements
For example we can do this;

```
sage: G = SymmetricGroup(5)
sage: g = G.list()[2]
sage: H = gap(G)
sage: g in H
True
```

But not this;

```
sage: G = AbelianGroup([2,2])
sage: g = G.list()[2]
sage: H = gap(G)
sage: g in H
[...]
TypeError: Gap produced error output
Variable: 'f0' must have a value
```



Similarly we can't go back the other way around.
That is we can do this;

```
sage: G = SymmetricGroup(5)
sage: H = gap(G)
sage: r = H.ConjugacyClasses()[2].Representative()
sage: type(r)
<class 'sage.interfaces.gap.GapElement'>
sage: r in G
True
sage: G(r)
(1,2)
```


But not this

```
sage: G = AbelianGroup([2,2])
sage: H = gap(G)
sage: r = H.ConjugacyClasses()[2].Representative()
sage: r
f1
sage: r in G
False
sage: G(r)
[...]
TypeError: Argument x (= f1) is of wrong type.
```

