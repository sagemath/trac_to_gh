# Issue 4509: doctests for planarity code

archive/issues_004509.json:
```json
{
    "body": "Assignee: ekirkman\n\nCC:  @rlmill @rbeezer\n\nI'm still seeing the same segfault that I worked around in the patch on #4505.  Here is code that triggers it for me.\n\n```\n        sage: import networkx.generators.atlas  # long time\n        sage: atlas_graphs = [Graph(i) for i in networkx.generators.atlas.graph_atlas_g()] # long time\n        sage: a = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time\n        sage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time\n```\n\nI've added that as a doctest to the planarity code.\n\nFor me, the segfault usually happens on the second run (the \"b =\" line), but occasionally happens on the first run.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4509\n\n",
    "closed_at": "2010-04-15T05:19:27Z",
    "created_at": "2008-11-13T06:00:16Z",
    "labels": [
        "component: graph theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "doctests for planarity code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4509",
    "user": "https://github.com/jasongrout"
}
```
Assignee: ekirkman

CC:  @rlmill @rbeezer

I'm still seeing the same segfault that I worked around in the patch on #4505.  Here is code that triggers it for me.

```
        sage: import networkx.generators.atlas  # long time
        sage: atlas_graphs = [Graph(i) for i in networkx.generators.atlas.graph_atlas_g()] # long time
        sage: a = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
        sage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
```

I've added that as a doctest to the planarity code.

For me, the segfault usually happens on the second run (the "b =" line), but occasionally happens on the first run.

Issue created by migration from https://trac.sagemath.org/ticket/4509





---

archive/issue_comments_033363.json:
```json
{
    "body": "Attachment [long-doctest-segfault.patch](tarball://root/attachments/some-uuid/ticket4509/long-doctest-segfault.patch) by @jasongrout created at 2008-11-13 06:01:22\n\nI think this might depend on one or more of #4505 or #4506.",
    "created_at": "2008-11-13T06:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33363",
    "user": "https://github.com/jasongrout"
}
```

Attachment [long-doctest-segfault.patch](tarball://root/attachments/some-uuid/ticket4509/long-doctest-segfault.patch) by @jasongrout created at 2008-11-13 06:01:22

I think this might depend on one or more of #4505 or #4506.



---

archive/issue_comments_033364.json:
```json
{
    "body": "With #4505, #4506 and #4507 applied I get the following for the first run only, i.e. no need to run the doctests twice:\n\n```\n==21687== Invalid read of size 4\n==21687==    at 0x2221C301: _CreateFwdArcLists (graphEmbed.c:147)\n==21687==    by 0x2221D7FD: gp_Embed (graphEmbed.c:976)\n==21687==    by 0x22219199: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:692)\n==21687==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)\n==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)\n==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)\n==21687==    by 0x412379: Py_Main (main.c:134)\n==21687==  Address 0xe2d9390 is 8 bytes before a block of size 192 alloc'd\n==21687==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)\n==21687==    by 0x222220F0: gp_InitGraph (graphStructure.c:99)\n==21687==    by 0x22217E00: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:573)\n==21687==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)\n==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)\n==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)\n==21687==    by 0x412379: Py_Main (main.c:134)\n==21687== \n==21687== Invalid read of size 4\n==21687==    at 0x2221C307: _CreateFwdArcLists (graphEmbed.c:153)\n==21687==    by 0x2221D7FD: gp_Embed (graphEmbed.c:976)\n==21687==    by 0x22219199: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:692)\n==21687==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)\n==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)\n==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)\n==21687==    by 0x412379: Py_Main (main.c:134)\n==21687==  Address 0x21995e54 is 12 bytes before a block of size 1,344 alloc'd\n==21687==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)\n==21687==    by 0x222220F0: gp_InitGraph (graphStructure.c:99)\n==21687==    by 0x22217E00: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:573)\n==21687==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)\n==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)\n==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)\n==21687==    by 0x412379: Py_Main (main.c:134)\n==21687== \n==21687== Invalid write of size 4\n==21687==    at 0x2221C352: _CreateFwdArcLists (graphEmbed.c:164)\n==21687==    by 0x2221D7FD: gp_Embed (graphEmbed.c:976)\n==21687==    by 0x22219199: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:692)\n==21687==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)\n==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)\n==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)\n==21687==    by 0x412379: Py_Main (main.c:134)\n==21687==  Address 0x21995e50 is 16 bytes before a block of size 1,344 alloc'd\n==21687==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)\n==21687==    by 0x222220F0: gp_InitGraph (graphStructure.c:99)\n==21687==    by 0x22217E00: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:573)\n==21687==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)\n==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)\n==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)\n==21687==    by 0x412379: Py_Main (main.c:134)\n==21687== \n==21687== Invalid write of size 4\n==21687==    at 0x2221C369: _CreateFwdArcLists (graphEmbed.c:165)\n==21687==    by 0x2221D7FD: gp_Embed (graphEmbed.c:976)\n==21687==    by 0x22219199: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:692)\n==21687==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)\n==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)\n==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)\n==21687==    by 0x412379: Py_Main (main.c:134)\n==21687==  Address 0x21995e54 is 12 bytes before a block of size 1,344 alloc'd\n==21687==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)\n==21687==    by 0x222220F0: gp_InitGraph (graphStructure.c:99)\n==21687==    by 0x22217E00: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:573)\n==21687==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)\n==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)\n==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)\n==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)\n==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)\n==21687==    by 0x412379: Py_Main (main.c:134)\n```\n\nI am now digging into which graphs cause the trouble.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T06:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33364",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With #4505, #4506 and #4507 applied I get the following for the first run only, i.e. no need to run the doctests twice:

```
==21687== Invalid read of size 4
==21687==    at 0x2221C301: _CreateFwdArcLists (graphEmbed.c:147)
==21687==    by 0x2221D7FD: gp_Embed (graphEmbed.c:976)
==21687==    by 0x22219199: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:692)
==21687==    by 0x415832: PyObject_Call (abstract.c:1861)
==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==21687==    by 0x412379: Py_Main (main.c:134)
==21687==  Address 0xe2d9390 is 8 bytes before a block of size 192 alloc'd
==21687==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)
==21687==    by 0x222220F0: gp_InitGraph (graphStructure.c:99)
==21687==    by 0x22217E00: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:573)
==21687==    by 0x415832: PyObject_Call (abstract.c:1861)
==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==21687==    by 0x412379: Py_Main (main.c:134)
==21687== 
==21687== Invalid read of size 4
==21687==    at 0x2221C307: _CreateFwdArcLists (graphEmbed.c:153)
==21687==    by 0x2221D7FD: gp_Embed (graphEmbed.c:976)
==21687==    by 0x22219199: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:692)
==21687==    by 0x415832: PyObject_Call (abstract.c:1861)
==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==21687==    by 0x412379: Py_Main (main.c:134)
==21687==  Address 0x21995e54 is 12 bytes before a block of size 1,344 alloc'd
==21687==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)
==21687==    by 0x222220F0: gp_InitGraph (graphStructure.c:99)
==21687==    by 0x22217E00: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:573)
==21687==    by 0x415832: PyObject_Call (abstract.c:1861)
==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==21687==    by 0x412379: Py_Main (main.c:134)
==21687== 
==21687== Invalid write of size 4
==21687==    at 0x2221C352: _CreateFwdArcLists (graphEmbed.c:164)
==21687==    by 0x2221D7FD: gp_Embed (graphEmbed.c:976)
==21687==    by 0x22219199: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:692)
==21687==    by 0x415832: PyObject_Call (abstract.c:1861)
==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==21687==    by 0x412379: Py_Main (main.c:134)
==21687==  Address 0x21995e50 is 16 bytes before a block of size 1,344 alloc'd
==21687==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)
==21687==    by 0x222220F0: gp_InitGraph (graphStructure.c:99)
==21687==    by 0x22217E00: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:573)
==21687==    by 0x415832: PyObject_Call (abstract.c:1861)
==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==21687==    by 0x412379: Py_Main (main.c:134)
==21687== 
==21687== Invalid write of size 4
==21687==    at 0x2221C369: _CreateFwdArcLists (graphEmbed.c:165)
==21687==    by 0x2221D7FD: gp_Embed (graphEmbed.c:976)
==21687==    by 0x22219199: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:692)
==21687==    by 0x415832: PyObject_Call (abstract.c:1861)
==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==21687==    by 0x412379: Py_Main (main.c:134)
==21687==  Address 0x21995e54 is 12 bytes before a block of size 1,344 alloc'd
==21687==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)
==21687==    by 0x222220F0: gp_InitGraph (graphStructure.c:99)
==21687==    by 0x22217E00: __pyx_pf_4sage_6graphs_9planarity_is_planar (planarity.c:573)
==21687==    by 0x415832: PyObject_Call (abstract.c:1861)
==21687==    by 0x482DB9: PyEval_EvalFrameEx (ceval.c:3784)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x484AF1: PyEval_EvalFrameEx (ceval.c:494)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x48491B: PyEval_EvalFrameEx (ceval.c:3659)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x483F76: PyEval_EvalFrameEx (ceval.c:3669)
==21687==    by 0x485DB1: PyEval_EvalCodeEx (ceval.c:2836)
==21687==    by 0x486051: PyEval_EvalCode (ceval.c:494)
==21687==    by 0x4A751D: PyRun_FileExFlags (pythonrun.c:1273)
==21687==    by 0x4A77AF: PyRun_SimpleFileExFlags (pythonrun.c:879)
==21687==    by 0x412379: Py_Main (main.c:134)
```

I am now digging into which graphs cause the trouble.

Cheers,

Michael



---

archive/issue_comments_033365.json:
```json
{
    "body": "Attachment [planarity-segfault-trip-gdb.patch](tarball://root/attachments/some-uuid/ticket4509/planarity-segfault-trip-gdb.patch) by @jasongrout created at 2008-11-13 06:15:51\n\nplanarity-segfault-trip-gdb.patch is a patch which supplies a poor man's assert: we see the problem when Jfirst is -1 *and* when the random memory location happens to be 2.  The patch causes a segfault whenever Jfirst is -1.",
    "created_at": "2008-11-13T06:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33365",
    "user": "https://github.com/jasongrout"
}
```

Attachment [planarity-segfault-trip-gdb.patch](tarball://root/attachments/some-uuid/ticket4509/planarity-segfault-trip-gdb.patch) by @jasongrout created at 2008-11-13 06:15:51

planarity-segfault-trip-gdb.patch is a patch which supplies a poor man's assert: we see the problem when Jfirst is -1 *and* when the random memory location happens to be 2.  The patch causes a segfault whenever Jfirst is -1.



---

archive/issue_comments_033366.json:
```json
{
    "body": "```\n[00:30] <mabshoff> jason--: looks like there is nothing major in the planarity code leak wise.\n[00:30] <jason--> that's good.\n[00:30] <jason--> can you post a note to that effect?\n[00:31] <mabshoff> Maybe 100 bytes or so for running all 1200 graphs five times.\n```",
    "created_at": "2008-11-13T06:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33366",
    "user": "https://github.com/jasongrout"
}
```

```
[00:30] <mabshoff> jason--: looks like there is nothing major in the planarity code leak wise.
[00:30] <jason--> that's good.
[00:30] <jason--> can you post a note to that effect?
[00:31] <mabshoff> Maybe 100 bytes or so for running all 1200 graphs five times.
```



---

archive/issue_comments_033367.json:
```json
{
    "body": "The issue pops up seemingly randomly, i.e. under valgrind there are complete runs that are ok while with others some tests cause the problem, but seemingly never the same test, i.e. the order is seemingly random. Jason has a theory what needs to happen for the issue to be triggered.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T07:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33367",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue pops up seemingly randomly, i.e. under valgrind there are complete runs that are ok while with others some tests cause the problem, but seemingly never the same test, i.e. the order is seemingly random. Jason has a theory what needs to happen for the issue to be triggered.

Cheers,

Michael



---

archive/issue_comments_033368.json:
```json
{
    "body": "From an email to John Boyer:\n\nGoing back to the graphEmbed.c file, the _CreateFwdArcLists function, it seems that theGraph->G[I].link[1] is -1 (i.e., is NIL) exactly when the vertex I has degree 0.  Do you assume that the input graph does not have any isolated vertices?\n\nI think the reason we get random segfaults is because when Jfirst is -1, the if statement in this function is true depending on values associated with G[-1], which is a random value outside of our array.\n\nI see two possible fixes.  If you have a different fix, we would love to hear it.\n\n1. insert the lines:\n\n```\nif(Jfirst<0) {\n    continue;\n}\n```\nright after Jfirst is assigned (i.e., Jfirst = theGraph->G[I].link[1];)\n\nI believe this skips vertices that have degree 0.  Will the algorithm work correctly with this modification?\n\n\n2. Delete any vertices of degree 0 from the graph before calling the algorithm.  Of course, this does not change the planarity of the graph.    However, I couldn't find this limitation documented anywhere, and your paper says that the algorithm works for disconnected graphs.  Am I correct in assuming that incorrect handling of degree 0 vertices is the problem here?\n\nDo you have any suggestions for which fix would be better?  If fix #1 works, I prefer that one, as it is less preparation work before calling your code.",
    "created_at": "2008-11-13T16:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33368",
    "user": "https://github.com/jasongrout"
}
```

From an email to John Boyer:

Going back to the graphEmbed.c file, the _CreateFwdArcLists function, it seems that theGraph->G[I].link[1] is -1 (i.e., is NIL) exactly when the vertex I has degree 0.  Do you assume that the input graph does not have any isolated vertices?

I think the reason we get random segfaults is because when Jfirst is -1, the if statement in this function is true depending on values associated with G[-1], which is a random value outside of our array.

I see two possible fixes.  If you have a different fix, we would love to hear it.

1. insert the lines:

```
if(Jfirst<0) {
    continue;
}
```
right after Jfirst is assigned (i.e., Jfirst = theGraph->G[I].link[1];)

I believe this skips vertices that have degree 0.  Will the algorithm work correctly with this modification?


2. Delete any vertices of degree 0 from the graph before calling the algorithm.  Of course, this does not change the planarity of the graph.    However, I couldn't find this limitation documented anywhere, and your paper says that the algorithm works for disconnected graphs.  Am I correct in assuming that incorrect handling of degree 0 vertices is the problem here?

Do you have any suggestions for which fix would be better?  If fix #1 works, I prefer that one, as it is less preparation work before calling your code.



---

archive/issue_comments_033369.json:
```json
{
    "body": "Changing assignee from @rlmill to ekirkman.",
    "created_at": "2008-11-15T02:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33369",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Changing assignee from @rlmill to ekirkman.



---

archive/issue_comments_033370.json:
```json
{
    "body": "Hi.  I just responded to Jason's email, but I'll post here too.  The Boyer/Myrvold algorithm requires the graph be connected so for the workaround we need to look at each of the connected components of the graph.  I can make a patch on Sunday, but I'd be happy to review anything you guys come up with before then.",
    "created_at": "2008-11-15T02:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33370",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Hi.  I just responded to Jason's email, but I'll post here too.  The Boyer/Myrvold algorithm requires the graph be connected so for the workaround we need to look at each of the connected components of the graph.  I can make a patch on Sunday, but I'd be happy to review anything you guys come up with before then.



---

archive/issue_events_010220.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-15T11:04:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4509#event-10220"
}
```



---

archive/issue_comments_033371.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33371",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_033372.json:
```json
{
    "body": "If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33372",
    "user": "https://github.com/williamstein"
}
```

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_033373.json:
```json
{
    "body": "Works for me and valgrinds clean: \n\n```\nboothby@sage:/scratch/boothby/sage-4.3$ ./sage -valgrind\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n/mnt/usb1/scratch/boothby/sage-4.3/local/bin/sage-ipython\nLog file is /home/boothby/.sage/valgrind/sage-memcheck.%p\nUsing default flags:\n--leak-resolution=high --log-file=/home/boothby/.sage/valgrind/sage-memcheck.%p --leak-check=full --num-callers=25 --suppressions=/mnt/usb1/scratch/boothby/sage-4.3/local/lib/valgrind/sage.supp\nPython 2.6.2 (r262, Jan 17 2010, 13:56:28) \n[GCC 4.4.1] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\nprint \"hello world\"\nsage: print \"hello world\"\nhello world\nsage: import networkx.generators.atlas  # long time\nsage: atlas_graphs = [Graph(i) for i in networkx.generators.atlas.graph_atlas_g()] # long time\nsage: a = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time\nsage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time\nsage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time\nsage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time\nsage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time\n```\n| Sage Version 4.3, Release Date: 2009-12-24                         |\n| Type notebook() for the GUI, and license() for information.        |\nI recommend we add the first patch and not the second, because it is unnecessary.",
    "created_at": "2010-01-18T05:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33373",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Works for me and valgrinds clean: 

```
boothby@sage:/scratch/boothby/sage-4.3$ ./sage -valgrind
----------------------------------------------------------------------
----------------------------------------------------------------------
/mnt/usb1/scratch/boothby/sage-4.3/local/bin/sage-ipython
Log file is /home/boothby/.sage/valgrind/sage-memcheck.%p
Using default flags:
--leak-resolution=high --log-file=/home/boothby/.sage/valgrind/sage-memcheck.%p --leak-check=full --num-callers=25 --suppressions=/mnt/usb1/scratch/boothby/sage-4.3/local/lib/valgrind/sage.supp
Python 2.6.2 (r262, Jan 17 2010, 13:56:28) 
[GCC 4.4.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
print "hello world"
sage: print "hello world"
hello world
sage: import networkx.generators.atlas  # long time
sage: atlas_graphs = [Graph(i) for i in networkx.generators.atlas.graph_atlas_g()] # long time
sage: a = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
sage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
sage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
sage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
sage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
```
| Sage Version 4.3, Release Date: 2009-12-24                         |
| Type notebook() for the GUI, and license() for information.        |
I recommend we add the first patch and not the second, because it is unnecessary.



---

archive/issue_comments_033374.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T01:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33374",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_033375.json:
```json
{
    "body": "there we go.\n\nI repeat, only apply the first patch.",
    "created_at": "2010-01-20T01:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33375",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

there we go.

I repeat, only apply the first patch.



---

archive/issue_comments_033376.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T01:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33376",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_033377.json:
```json
{
    "body": "Replying to [comment:6 jason]:\n> From an email to John Boyer:\n> \n> Going back to the graphEmbed.c file, the _CreateFwdArcLists function, it seems that theGraph->G[I].link[1] is -1 (i.e., is NIL) exactly when the vertex I has degree 0.  Do you assume that the input graph does not have any isolated vertices?\n> \n> I think the reason we get random segfaults is because when Jfirst is -1, the if statement in this function is true depending on values associated with G[-1], which is a random value outside of our array.\n> \n> I see two possible fixes.  If you have a different fix, we would love to hear it.\n> \n> 1. insert the lines:\n> \n> ```\n> if(Jfirst<0) {\n>     continue;\n> }\n> ```\n> right after Jfirst is assigned (i.e., Jfirst = theGraph->G[I].link[1];)\n> \n> I believe this skips vertices that have degree 0.  Will the algorithm work correctly with this modification?\n> \n> \n> 2. Delete any vertices of degree 0 from the graph before calling the algorithm.  Of course, this does not change the planarity of the graph.    However, I couldn't find this limitation documented anywhere, and your paper says that the algorithm works for disconnected graphs.  Am I correct in assuming that incorrect handling of degree 0 vertices is the problem here?\n> \n> Do you have any suggestions for which fix would be better?  If fix #1 works, I prefer that one, as it is less preparation work before calling your code. \n\n\nHere is the email I got in reply from John Boyer on 08 Dec 2008:\n\n\n  I'll say up front that you're absolutely right that my reference implementation does not pay any real attention to isolated vertices as they have nothing really to do with the correctness of the algorithm.  As you mentioned, it is trivial to filter out degree 0 vertices. For the same reason, anything short of a biconnected graph is really not important to correctness from the theoretic perspective.\n\n  However, from the perspective of efficient implementation, it is advantageous that a graph doesn't have to be preprocessed to boil it down to biconnected components, and I paid a lot of attention to seamless handling of separable and indeed disconnected graphs, but the random graph generators (my own and from nauty) draw the line at zero degree vertices.  Still, we may as well handle the disconnected graph \"edge case\" of a singleton vertex (wow, two graph theoretic puns in the same paragraph).\n\n  So, I'll try to have a look at the fix you propose in the next short while and get back to you. That being said, from the lack of follow-on mail, I assume the fix you created is working out for you.  But please do let me know if any other issues have arisen, and again my apologies for my delayed response.\n\n\nAnd here's another email I received from John on 25 May 2009:\n\n  I know you haven't heard from me in a little while, but I have actually been hard at work on my planarity code (in my spare time of course).\n\n  I looked into whether there would need to be any other changes needed to the core planar graph embedding code beyond what you proposed, and nothing jumped out at me. Unfortunately, that's not the same thing as making sure.\n\n  Well, turns out that for a few years now I have been developing other algorithm extensions, such as outerplanar graph embedding, outerplanar obstruction isolation, search for subgraphs homeomorphic to K{2,3} and K{3,3}, and even graph drawing by visibility representation.  Problem was, I would always take the \"greedy\" approach of augmenting a copy of the core planarity code.  It seemed about time to pull all of this work together into one package and at the same time resurrect the connection to McKay's nauty \"makeg\" program so I could ensure that none of the work I was doing to pull all these things together was actually breaking anything.\n\n  And of course, the bit you're interested in is that doing this also made it reasonable to see what I could do about removing the \"-c\" from the call to makeg, thereby ensuring proper operation on disconnected graphs, esp. those with isolated vertices.\n\n  I also did lots of internal maintenance work to characterize certain code patterns with macros to further enhance knowledge of what is going on under the hood, so to speak.\n\n  Unfortunately (or perhaps fortunately), I can no longer recall whether any other changes were actually required of the code you adopted into Sage in order to serve disconnected graphs.  I don't think so, but the only code on which I am comfortable with claiming support for disconnected graphs is the new \"version 2.0\" code.\n\n  The reason I say it is possibly fortunate is that it should be precious little effort for you to consider adopting this new code since I kept backwards compatibility at a high priority.  You are quite unlikely to have done anything that is not supported under the new code, though I can help you if there are *any* issues.  Best of all, you can actually get the code because I've made it publicly available from a Google Code project.\n\n  http://code.google.com/p/planarity\n\n  Now that I've completed the work of pulling together the algorithms I've created to date and ensuring they are well behaved on all graphs with fewer than 12 vertices, I've created a tag for version 2.0.0, so you can grab that rather than grabbing the trunk.\n\n  Let me know if this is something you are interested in pursuing. \n\n\nSo it sounds like we can maybe look at adding the new planarity code to Sage too?",
    "created_at": "2010-01-20T01:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33377",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:6 jason]:
> From an email to John Boyer:
> 
> Going back to the graphEmbed.c file, the _CreateFwdArcLists function, it seems that theGraph->G[I].link[1] is -1 (i.e., is NIL) exactly when the vertex I has degree 0.  Do you assume that the input graph does not have any isolated vertices?
> 
> I think the reason we get random segfaults is because when Jfirst is -1, the if statement in this function is true depending on values associated with G[-1], which is a random value outside of our array.
> 
> I see two possible fixes.  If you have a different fix, we would love to hear it.
> 
> 1. insert the lines:
> 
> ```
> if(Jfirst<0) {
>     continue;
> }
> ```
> right after Jfirst is assigned (i.e., Jfirst = theGraph->G[I].link[1];)
> 
> I believe this skips vertices that have degree 0.  Will the algorithm work correctly with this modification?
> 
> 
> 2. Delete any vertices of degree 0 from the graph before calling the algorithm.  Of course, this does not change the planarity of the graph.    However, I couldn't find this limitation documented anywhere, and your paper says that the algorithm works for disconnected graphs.  Am I correct in assuming that incorrect handling of degree 0 vertices is the problem here?
> 
> Do you have any suggestions for which fix would be better?  If fix #1 works, I prefer that one, as it is less preparation work before calling your code. 


Here is the email I got in reply from John Boyer on 08 Dec 2008:


  I'll say up front that you're absolutely right that my reference implementation does not pay any real attention to isolated vertices as they have nothing really to do with the correctness of the algorithm.  As you mentioned, it is trivial to filter out degree 0 vertices. For the same reason, anything short of a biconnected graph is really not important to correctness from the theoretic perspective.

  However, from the perspective of efficient implementation, it is advantageous that a graph doesn't have to be preprocessed to boil it down to biconnected components, and I paid a lot of attention to seamless handling of separable and indeed disconnected graphs, but the random graph generators (my own and from nauty) draw the line at zero degree vertices.  Still, we may as well handle the disconnected graph "edge case" of a singleton vertex (wow, two graph theoretic puns in the same paragraph).

  So, I'll try to have a look at the fix you propose in the next short while and get back to you. That being said, from the lack of follow-on mail, I assume the fix you created is working out for you.  But please do let me know if any other issues have arisen, and again my apologies for my delayed response.


And here's another email I received from John on 25 May 2009:

  I know you haven't heard from me in a little while, but I have actually been hard at work on my planarity code (in my spare time of course).

  I looked into whether there would need to be any other changes needed to the core planar graph embedding code beyond what you proposed, and nothing jumped out at me. Unfortunately, that's not the same thing as making sure.

  Well, turns out that for a few years now I have been developing other algorithm extensions, such as outerplanar graph embedding, outerplanar obstruction isolation, search for subgraphs homeomorphic to K{2,3} and K{3,3}, and even graph drawing by visibility representation.  Problem was, I would always take the "greedy" approach of augmenting a copy of the core planarity code.  It seemed about time to pull all of this work together into one package and at the same time resurrect the connection to McKay's nauty "makeg" program so I could ensure that none of the work I was doing to pull all these things together was actually breaking anything.

  And of course, the bit you're interested in is that doing this also made it reasonable to see what I could do about removing the "-c" from the call to makeg, thereby ensuring proper operation on disconnected graphs, esp. those with isolated vertices.

  I also did lots of internal maintenance work to characterize certain code patterns with macros to further enhance knowledge of what is going on under the hood, so to speak.

  Unfortunately (or perhaps fortunately), I can no longer recall whether any other changes were actually required of the code you adopted into Sage in order to serve disconnected graphs.  I don't think so, but the only code on which I am comfortable with claiming support for disconnected graphs is the new "version 2.0" code.

  The reason I say it is possibly fortunate is that it should be precious little effort for you to consider adopting this new code since I kept backwards compatibility at a high priority.  You are quite unlikely to have done anything that is not supported under the new code, though I can help you if there are *any* issues.  Best of all, you can actually get the code because I've made it publicly available from a Google Code project.

  http://code.google.com/p/planarity

  Now that I've completed the work of pulling together the algorithms I've created to date and ensuring they are well behaved on all graphs with fewer than 12 vertices, I've created a tag for version 2.0.0, so you can grab that rather than grabbing the trunk.

  Let me know if this is something you are interested in pursuing. 


So it sounds like we can maybe look at adding the new planarity code to Sage too?



---

archive/issue_comments_033378.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-23T23:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33378",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_033379.json:
```json
{
    "body": "I got a hunk failure when applying [long-doctest-segfault.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4509/long-doctest-segfault.patch) to Sage 4.3.1:\n\n```\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4509/long-doctest-segfault.patch && hg qpush\nadding long-doctest-segfault.patch to series file\napplying long-doctest-segfault.patch\npatching file sage/graphs/planarity.pyx\nHunk #1 FAILED at 40\n1 out of 1 hunks FAILED -- saving rejects to file sage/graphs/planarity.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh long-doctest-segfault.patch\n[mvngu@sage sage-main]$ cat sage/graphs/planarity.pyx.rej\n--- planarity.pyx\n+++ planarity.pyx\n@@ -41,12 +41,23 @@\n         (see g.get_embedding())\n         circular -- if True, test for circular planarity\n\n-    EXAMPLE:\n+    EXAMPLES:\n         sage: G = Graph(graphs.DodecahedralGraph(), implementation='networkx')\n         sage: from sage.graphs.planarity import is_planar\n         sage: is_planar(G)\n         True\n         sage: Graph('@').is_planar()\n+        True\n+\n+    TESTS:\n+        We try checking the planarity of all graphs on 7 or fewer\n+        vertices.  In fact, to try to track down a segfault, we do it\n+        twice.\n+        sage: import networkx.generators.atlas  # long time\n+        sage: atlas_graphs = [Graph(i) for i in networkx.generators.atlas.graph_atlas_g()] # long time\n+        sage: a = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time\n+        sage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time\n+        sage: a == b # long time\n         True\n     \"\"\"\n     # First take care of a trivial case.  We ignore the set_pos,\n```\nI have rebased [long-doctest-segfault.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4509/long-doctest-segfault.patch) against Sage 4.3.1. Only apply [trac_4509-doctest-rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4509/trac_4509-doctest-rebase.patch), which needs some reviewing to make sure I didn't mess anything during the rebase. The docstring needs some adjusting, i.e. proper formatting to conform with Sphinx, but that belongs to another ticket.",
    "created_at": "2010-01-23T23:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33379",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I got a hunk failure when applying [long-doctest-segfault.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4509/long-doctest-segfault.patch) to Sage 4.3.1:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4509/long-doctest-segfault.patch && hg qpush
adding long-doctest-segfault.patch to series file
applying long-doctest-segfault.patch
patching file sage/graphs/planarity.pyx
Hunk #1 FAILED at 40
1 out of 1 hunks FAILED -- saving rejects to file sage/graphs/planarity.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh long-doctest-segfault.patch
[mvngu@sage sage-main]$ cat sage/graphs/planarity.pyx.rej
--- planarity.pyx
+++ planarity.pyx
@@ -41,12 +41,23 @@
         (see g.get_embedding())
         circular -- if True, test for circular planarity

-    EXAMPLE:
+    EXAMPLES:
         sage: G = Graph(graphs.DodecahedralGraph(), implementation='networkx')
         sage: from sage.graphs.planarity import is_planar
         sage: is_planar(G)
         True
         sage: Graph('@').is_planar()
+        True
+
+    TESTS:
+        We try checking the planarity of all graphs on 7 or fewer
+        vertices.  In fact, to try to track down a segfault, we do it
+        twice.
+        sage: import networkx.generators.atlas  # long time
+        sage: atlas_graphs = [Graph(i) for i in networkx.generators.atlas.graph_atlas_g()] # long time
+        sage: a = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
+        sage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
+        sage: a == b # long time
         True
     """
     # First take care of a trivial case.  We ignore the set_pos,
```
I have rebased [long-doctest-segfault.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4509/long-doctest-segfault.patch) against Sage 4.3.1. Only apply [trac_4509-doctest-rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4509/trac_4509-doctest-rebase.patch), which needs some reviewing to make sure I didn't mess anything during the rebase. The docstring needs some adjusting, i.e. proper formatting to conform with Sphinx, but that belongs to another ticket.



---

archive/issue_comments_033380.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-23T23:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33380",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033381.json:
```json
{
    "body": "rebased vs. Sage 4.3.4.alpha1; apply on this",
    "created_at": "2010-03-10T06:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33381",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

rebased vs. Sage 4.3.4.alpha1; apply on this



---

archive/issue_comments_033382.json:
```json
{
    "body": "Attachment [trac_4509-doctest-rebase.patch](tarball://root/attachments/some-uuid/ticket4509/trac_4509-doctest-rebase.patch) by @aghitza created at 2010-04-03 06:09:36\n\nLooks good and applies cleanly to 4.3.5.  Let's put it out of its misery.",
    "created_at": "2010-04-03T06:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33382",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_4509-doctest-rebase.patch](tarball://root/attachments/some-uuid/ticket4509/trac_4509-doctest-rebase.patch) by @aghitza created at 2010-04-03 06:09:36

Looks good and applies cleanly to 4.3.5.  Let's put it out of its misery.



---

archive/issue_comments_033383.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-03T06:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33383",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_033384.json:
```json
{
    "body": "Merged trac_4509-doctest-rebase.patch in 4.4.alpha0",
    "created_at": "2010-04-15T05:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33384",
    "user": "https://github.com/jhpalmieri"
}
```

Merged trac_4509-doctest-rebase.patch in 4.4.alpha0



---

archive/issue_comments_033385.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T05:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4509#issuecomment-33385",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_010221.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T05:19:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4509",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4509#event-10221"
}
```
