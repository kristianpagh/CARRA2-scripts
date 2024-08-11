#!/usr/local/apps/python3/3.8.8-01/bin/python3

import epygram
import os
epygram.init_env()

ref='C2rf_noprod'
exp='C2ga_noprod'
comp='glalb_comp'
refdir='/ec/res4/scratch/nhp/hm_home/'+ref+'/'
expdir='/ec/res4/scratch/nhp/hm_home/'+exp+'/'
data='/perm/nhp/'+comp+'/data/'
figures='/perm/nhp/'+comp+'/figures/'
y='2023'
m='07'
d='01'
h='12'
for l in range (0,7):
    l2 = f'{l:0>2d}'
    datafile=data+'ref'+y+m+d+h+'+'+l2+'.sfx'
    if not os.path.exists(datafile):
        indir=refdir+'archive/'+y+'/'+m+'/'+d+'/'+h+'/'
        infile=indir+'ICMSHSELE+00'+l2+'.sfx'
        os.system('cp '+infile+' '+datafile)
    mf = epygram.formats.resource(datafile,'r',fmt='FA')
    refshflux = mf.readfield('SFX.H')
    fig, ax = refshflux.cartoplot(minmax=(-1000,1000),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'refshflux_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    refleflux = mf.readfield('SFX.LE')
    fig, ax = refleflux.cartoplot(minmax=(-1000,1000),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'refleflux_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    refgflux  = mf.readfield('SFX.GFLUX')
    fig, ax = refgflux.cartoplot(minmax=(-1000,1000),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'refgflux_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    refisbaalb = mf.readfield('SFX.TALB_ISBA')
    fig, ax = refisbaalb.cartoplot(minmax=(0,1),colormap='gray')
    outplot=figures+'refisbaalb_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    refw10m = mf.readfield('SFX.W10M')
    fig, ax = refw10m.cartoplot(minmax=(0,40))
    outplot=figures+'refw10m'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    refisbasnowfrac = mf.readfield('SFX.PSN_ISBA')
    fig, ax = refisbasnowfrac.cartoplot(minmax=(0,1),colormap='gray')
    outplot=figures+'refisbasnowfrac'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    refisbaswe = mf.readfield('SFX.WSN_T_ISBA')
    fig, ax = refisbaswe.cartoplot(minmax=(0,3500),colormap='nipy_spectral')
    outplot=figures+'refisbaswe'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    refisbasnowdepth = mf.readfield('SFX.DSN_T_ISBA')
    fig, ax = refisbasnowdepth.cartoplot(minmax=(0,12),colormap='nipy_spectral')
    outplot=figures+'refisbasnowdepth'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    datafile=data+'exp'+y+m+d+h+'+'+l2+'.sfx'
    if not os.path.exists(datafile):
        indir=expdir+'archive/'+y+'/'+m+'/'+d+'/'+h+'/'
        infile=indir+'ICMSHSELE+00'+l2+'.sfx'
        os.system('cp '+infile+' '+datafile)
    mf = epygram.formats.resource(datafile,'r',fmt='FA')
    expshflux = mf.readfield('SFX.H')
    fig, ax = expshflux.cartoplot(minmax=(-1000,1000),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'expshflux_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    expleflux = mf.readfield('SFX.LE')
    fig, ax = expleflux.cartoplot(minmax=(-1000,1000),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'expleflux_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    expgflux  = mf.readfield('SFX.GFLUX')
    fig, ax = expgflux.cartoplot(minmax=(-1000,1000),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'expgflux_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    expisbaalb = mf.readfield('SFX.TALB_ISBA')
    fig, ax = expisbaalb.cartoplot(minmax=(0,1),colormap='gray')
    outplot=figures+'expisbaalb_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    expw10m = mf.readfield('SFX.W10M')
    fig, ax = expw10m.cartoplot(minmax=(0,40))
    outplot=figures+'expw10m'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    expisbasnowfrac = mf.readfield('SFX.PSN_ISBA')
    fig, ax = expisbasnowfrac.cartoplot(minmax=(0,1),colormap='gray')
    outplot=figures+'expisbasnowfrac'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    expisbaswe = mf.readfield('SFX.WSN_T_ISBA')
    fig, ax = expisbaswe.cartoplot(minmax=(0,3500),colormap='nipy_spectral')
    outplot=figures+'expisbaswe'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    expisbasnowdepth = mf.readfield('SFX.DSN_T_ISBA')
    fig, ax = expisbasnowdepth.cartoplot(minmax=(0,12),colormap='nipy_spectral')
    outplot=figures+'expisbasnowdepth'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    shfluxdiff = expshflux - refshflux
    fig, ax = shfluxdiff.cartoplot(minmax=(-1000,1000),colormap='seismic')
    outplot=figures+'shfluxdiff_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    lefluxdiff = expleflux - refleflux
    fig, ax = lefluxdiff.cartoplot(minmax=(-1000,1000),colormap='seismic')
    outplot=figures+'lefluxdiff_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    gfluxdiff = expgflux - refgflux
    fig, ax = gfluxdiff.cartoplot(minmax=(-1000,1000),colormap='seismic')
    outplot=figures+'gfluxdiff_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    isbaalbdiff = expisbaalb - refisbaalb 
    fig, ax = isbaalbdiff.cartoplot(minmax=(-1,1),colormap='seismic')
    outplot=figures+'isbaalbdiff_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    w10mdiff = expw10m - refw10m 
    fig, ax = w10mdiff.cartoplot(minmax=(-15,15),colormap='seismic')
    outplot=figures+'w10mdiff_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    isbasnowfracdiff = expisbasnowfrac - refisbasnowfrac 
    fig, ax = isbasnowfracdiff.cartoplot(minmax=(-1,1),colormap='seismic')
    outplot=figures+'isbasnowfracdiff_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    isbaswediff = expisbaswe - refisbaswe 
    fig, ax = isbaswediff.cartoplot(minmax=(-3500,3500),colormap='seismic')
    outplot=figures+'isbaswediff_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    isbasnowdepthdiff = expisbasnowdepth - refisbasnowdepth 
    fig, ax = isbasnowdepthdiff.cartoplot(minmax=(-12,12),colormap='seismic')
    outplot=figures+'isbasnowdepthdiff_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
