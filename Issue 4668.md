# Issue 4668: libSingular's header have too tight permissions

archive/issues_004668.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @malb\n\n\n```\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/CCRing.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/clapconv.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/clapsing.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/dbm_sl.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/dError.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/digitech.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/distrib.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/eigenval.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/F4.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/f5gb.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/fast_maps.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/fast_mult.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/febase.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/fegetopt.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/ffields.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/fglmgauss.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/fglm.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/fglmvec.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/GMPrat.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/gnumpc.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/gnumpfl.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/gring.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/htmlhelp.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/hutil.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/Ideal.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/ideals.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/IIntvec.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/int64vec.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/intvec.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/kbuckets.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/khstd.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/kmatrix.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/kstd1.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/kstdfac.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/kutil.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/longalg.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/longrat.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/maps.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/matpol.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/mmalloc.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/mod_raw.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/modulop.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/mpr_base.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/mpr_complex.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/mpr_global.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/mpr_inout.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/mpr_numeric.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/multicnt.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/npolygon.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/Number.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/numbers.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/omSingularConfig.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/page.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/pInline0.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/pInline1.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/pInline2.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/p_MemAdd.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/p_MemCmp.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/p_MemCopy.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Mult_q.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Numbers.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/Poly.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/polys.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/polys-impl.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/PowerSeries.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/p_polys.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Procs_Dynamic.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Procs.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Procs_Impl.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Procs_Set.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Procs_Static.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/prCopy.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/prCopyMacros.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/pShallowCopyDelete.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/ratgring.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/ringgb.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/ring.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/rintegers.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/rmodulo2m.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/rmodulon.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/run.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/sbuckets.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/sca.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/semic.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/shiftgb.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/shortfl.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/si_gmp.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/silink.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/sing_dbm.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/sparsmat.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/spectrum.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/splist.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/stairc.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/structs.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/stype.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/syz.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/testpoly.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/tgbgauss.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/tgb.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/tgb_internal.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/timer.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/units.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/walkMain.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/walkProc.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/walkSupport.h' for reading: Permission denied\ncp: cannot open `sage-3.2.1.rc1/local/include/singular/weight.h' for reading: Permission denied\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4668\n\n",
    "created_at": "2008-12-01T07:00:10Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "libSingular's header have too tight permissions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4668",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @malb


```
cp: cannot open `sage-3.2.1.rc1/local/include/singular/CCRing.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/clapconv.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/clapsing.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/dbm_sl.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/dError.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/digitech.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/distrib.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/eigenval.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/F4.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/f5gb.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/fast_maps.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/fast_mult.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/febase.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/fegetopt.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/ffields.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/fglmgauss.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/fglm.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/fglmvec.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/GMPrat.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/gnumpc.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/gnumpfl.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/gring.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/htmlhelp.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/hutil.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/Ideal.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/ideals.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/IIntvec.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/int64vec.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/intvec.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/kbuckets.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/khstd.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/kmatrix.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/kstd1.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/kstdfac.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/kutil.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/longalg.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/longrat.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/maps.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/matpol.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/mmalloc.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/mod_raw.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/modulop.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/mpr_base.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/mpr_complex.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/mpr_global.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/mpr_inout.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/mpr_numeric.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/multicnt.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/npolygon.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/Number.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/numbers.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/omSingularConfig.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/page.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/pInline0.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/pInline1.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/pInline2.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/p_MemAdd.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/p_MemCmp.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/p_MemCopy.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Mult_q.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Numbers.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/Poly.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/polys.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/polys-impl.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/PowerSeries.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/p_polys.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Procs_Dynamic.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Procs.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Procs_Impl.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Procs_Set.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/p_Procs_Static.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/prCopy.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/prCopyMacros.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/pShallowCopyDelete.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/ratgring.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/ringgb.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/ring.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/rintegers.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/rmodulo2m.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/rmodulon.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/run.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/sbuckets.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/sca.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/semic.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/shiftgb.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/shortfl.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/si_gmp.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/silink.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/sing_dbm.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/sparsmat.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/spectrum.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/splist.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/stairc.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/structs.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/stype.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/syz.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/testpoly.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/tgbgauss.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/tgb.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/tgb_internal.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/timer.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/units.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/walkMain.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/walkProc.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/walkSupport.h' for reading: Permission denied
cp: cannot open `sage-3.2.1.rc1/local/include/singular/weight.h' for reading: Permission denied
```


Issue created by migration from https://trac.sagemath.org/ticket/4668





---

archive/issue_comments_035095.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-01T07:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4668#issuecomment-35095",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035096.json:
```json
{
    "body": "A cleaned up spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/rc1/singular-3-0-4-4-20080711.p2.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T07:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4668#issuecomment-35096",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

A cleaned up spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/rc1/singular-3-0-4-4-20080711.p2.spkg

Cheers,

Michael



---

archive/issue_comments_035097.json:
```json
{
    "body": "Yep, looks good. Michael fixed the permissions within the spkg itself, and cleaned up one or two things to boot. Positive review.",
    "created_at": "2008-12-01T07:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4668#issuecomment-35097",
    "user": "https://github.com/craigcitro"
}
```

Yep, looks good. Michael fixed the permissions within the spkg itself, and cleaned up one or two things to boot. Positive review.



---

archive/issue_comments_035098.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-01T07:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4668#issuecomment-35098",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035099.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T07:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4668#issuecomment-35099",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.rc1

Cheers,

Michael
