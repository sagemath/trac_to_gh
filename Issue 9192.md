# Issue 9192: Tab-completion misses some elements

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-06-09 02:18:04

Assignee: jason


```
sage.crypto.bl[tab]
```

This should give

```
sage.crypto.block_cipher
```

But does not.  In fact, 

```
sage.crypto.[tab]
```

only gives 10 of the 13 things which appear when you do

```
from sage.crypto.[tab]
```

