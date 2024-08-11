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
for l in range (1,7):
    l2 = f'{l:0>2d}'
    datafile=data+'ref'+y+m+d+h+'+'+l2
    if not os.path.exists(datafile):
        indir=refdir+'archive/'+y+'/'+m+'/'+d+'/'+h+'/'
        infile=indir+'ICMSHHARM+00'+l2
        os.system('cp '+infile+' '+datafile)
    mf = epygram.formats.resource(datafile,'r',fmt='FA')
    refghinew = mf.readfield('SURFRAYT SOLA DE')
    refdhinew = mf.readfield('SURFRAYT DIR SUR')
    refdninew = mf.readfield('SURFDIR NORM IRR')
    if l>1:
        refghi = refghinew - refghiold
        refghi.operation('/', 3600)
        fig, ax = refghi.cartoplot(minmax=(0,1000))
        outplot=figures+'refghi_'+y+m+d+h+'+'+l2
        fig.savefig(outplot+'.png')
        refdhi = refdhinew - refdhiold
        refdhi.operation('/', 3600)
        fig, ax = refdhi.cartoplot(minmax=(0,1000))
        outplot=figures+'refdhi_'+y+m+d+h+'+'+l2
        fig.savefig(outplot+'.png')
        refdni = refdninew - refdniold
        refdni.operation('/', 3600)
        fig, ax = refdni.cartoplot(minmax=(0,1000))
        outplot=figures+'refdni_'+y+m+d+h+'+'+l2
        fig.savefig(outplot+'.png')
    refT2m   = mf.readfield('CLSTEMPERATURE')
    refT2m.operation('-', 273.15)
    fig, ax = refT2m.cartoplot(minmax=(-60,50),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'refT2m_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    refTsurf = mf.readfield('SURFTEMPERATURE')
    refTsurf.operation('-', 273.15)
    fig, ax = refTsurf.cartoplot(minmax=(-60,50),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'refTsurf_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    #refu10m = mf.readfield('CLSVENT.ZONAL')
    #fig, ax = refu10m.cartoplot()
    #outplot=figures+'refu10m_'+y+m+d+h+'+'+l2
    #fig.savefig(outplot+'.png')
    #refv10m = mf.readfield('CLSVENT.MERIDIEN')
    #fig, ax = refv10m.cartoplot()
    #outplot=figures+'refv10m_'+y+m+d+h+'+'+l2
    #fig.savefig(outplot+'.png')
    datafile=data+'exp'+y+m+d+h+'+'+l2
    if not os.path.exists(datafile):
        indir=expdir+'archive/'+y+'/'+m+'/'+d+'/'+h+'/'
        infile=indir+'ICMSHHARM+00'+l2
        os.system('cp '+infile+' '+datafile)
    mf = epygram.formats.resource(datafile,'r',fmt='FA')
    expghinew = mf.readfield('SURFRAYT SOLA DE')
    expdhinew = mf.readfield('SURFRAYT DIR SUR')
    expdninew = mf.readfield('SURFDIR NORM IRR')
    if l>1:
        expghi = expghinew - expghiold
        expghi.operation('/', 3600)
        fig, ax = expghi.cartoplot(minmax=(0,1000))
        outplot=figures+'expghi_'+y+m+d+h+'+'+l2
        fig.savefig(outplot+'.png')
        expdhi = expdhinew - expdhiold
        expdhi.operation('/', 3600)
        fig, ax = expdhi.cartoplot(minmax=(0,1000))
        outplot=figures+'expdhi_'+y+m+d+h+'+'+l2
        fig.savefig(outplot+'.png')
        expdni = expdninew - expdniold
        expdni.operation('/', 3600)
        fig, ax = expdni.cartoplot(minmax=(0,1000))
        outplot=figures+'expdni_'+y+m+d+h+'+'+l2
        fig.savefig(outplot+'.png')
    expT2m  = mf.readfield('CLSTEMPERATURE')
    expT2m.operation('-', 273.15)
    fig, ax = expT2m.cartoplot(minmax=(-60,50),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'expT2m_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    expTsurf = mf.readfield('SURFTEMPERATURE')
    expTsurf.operation('-', 273.15)
    fig, ax = expTsurf.cartoplot(minmax=(-60,50),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'expTsurf_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    #expu10m = mf.readfield('CLSVENT.ZONAL')
    #fig, ax = expu10m.cartoplot()
    #outplot=figures+'expu10m_'+y+m+d+h+'+'+l2
    #fig.savefig(outplot+'.png')
    #expv10m = mf.readfield('CLSVENT.MERIDIEN')
    #fig, ax = expv10m.cartoplot()
    #outplot=figures+'expv10m_'+y+m+d+h+'+'+l2
    #fig.savefig(outplot+'.png')
    refghiold=refghinew
    refdhiold=refdhinew
    refdniold=refdninew
    expghiold=expghinew
    expdhiold=expdhinew
    expdniold=expdninew
    if l>1:
        ghidiff = expghi - refghi
        fig, ax = ghidiff.cartoplot(minmax=(-1000,1000),colormap='seismic')
        outplot=figures+'ghidiff_'+y+m+d+h+'+'+l2
        fig.savefig(outplot+'.png')
        dhidiff = expdhi - refdhi
        fig, ax = dhidiff.cartoplot(minmax=(-1000,1000),colormap='seismic')
        outplot=figures+'dhidiff_'+y+m+d+h+'+'+l2
        fig.savefig(outplot+'.png')
        dnidiff = expdni - refdni
        fig, ax = dnidiff.cartoplot(minmax=(-1000,1000),colormap='seismic')
        outplot=figures+'dnidiff_'+y+m+d+h+'+'+l2
        fig.savefig(outplot+'.png')
    Tsurfdiff = expTsurf - refTsurf
    fig, ax = Tsurfdiff.cartoplot(minmax=(-30,30),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'Tsurfdiff_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
    T2mdiff = expT2m - refT2m
    fig, ax = T2mdiff.cartoplot(minmax=(-30,30),colormap='seismic',center_cmap_on_0=True)
    outplot=figures+'T2mdiff_'+y+m+d+h+'+'+l2
    fig.savefig(outplot+'.png')
