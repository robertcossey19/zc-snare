import numpy as np, soundfile as sf, scipy.signal as sg, json, sys
SR=44100; PRE=int(0.02*SR); LEN=int(1.0*SR); W=int(0.04*SR)
def envdb(y,fr):
    n=len(y)//fr; return 10*np.log10((y[:n*fr].reshape(n,fr)**2).mean(1)+1e-14)
def candidates(m):
    fr=int(0.0025*SR)
    c=envdb(sg.sosfilt(sg.butter(4,[2000,9000],btype='band',fs=SR,output='sos'),m),fr)
    b=envdb(sg.sosfilt(sg.butter(4,[150,320],btype='band',fs=SR,output='sos'),m),fr)
    s=envdb(sg.sosfilt(sg.butter(4,[40,100],btype='band',fs=SR,output='sos'),m),fr)
    n=len(c); gain=np.full(n,-99.0)
    for i in range(16,n-6): gain[i]=c[i:i+4].max()-c[i-16:i-3].mean()
    pk,_=sg.find_peaks(gain,height=5,distance=int(0.08/0.0025))
    return [dict(t=int(p*fr), cg=float(gain[p]), bg=float(b[p:p+12].max()-b[p-16:p-3].mean()), sg=float(s[p:p+12].max()-s[p-16:p-3].mean()), bs=float(b[p:p+12].max()-s[p:p+12].max()), lvl=float(c[p:p+4].max())) for p in pk]
def frac_shift(x,d):
    n=len(x); X=np.fft.rfft(x); f=np.fft.rfftfreq(n); y=np.fft.irfft(X*np.exp(-2j*np.pi*f*d),n)
    m=int(np.ceil(abs(d)))+2   # FFT shift is circular: blank the samples that wrapped round from the other end of the segment
    if d>0: y[:m]=0
    elif d<0: y[-m:]=0
    return y
def extract(x, cthr=0.5, verbose=True, gmin=0.3, gmax=2.5, sel_rel=None):
    m=x.mean(1); rows=candidates(m)
    if sel_rel is not None:   # restrict to one velocity band (dB re 75th pct of body-carrying candidates) so quiet hits get their own template
        body=[r for r in rows if r['bg']>3 and r['bs']>-3]; ref=np.percentile([r['lvl'] for r in body],75)
        rows=[r for r in body if sel_rel[0]<=r['lvl']-ref<sel_rel[1]]
        if len(rows)<12: raise ValueError(f'only {len(rows)} candidates in band {sel_rel}')
    sos=sg.butter(4,[2000,9000],btype='band',fs=SR,output='sos'); sosw=sg.butter(2,[100,10000],btype='band',fs=SR,output='sos')
    segs=[]; meta=[]
    for r in rows:
        a=r['t']-int(0.03*SR)
        if a<0 or a+LEN+PRE+2000>len(x): continue
        raw=x[a:a+LEN+PRE+2000]; h=np.abs(sg.sosfilt(sos,raw.mean(1)))[:int(0.06*SR)]; k=int(np.argmax(h>0.5*h.max())); st=k-PRE
        if st<0: continue
        segs.append(raw[st:st+LEN]); r['a']=a+st; meta.append(r)
    segs=np.array(segs)
    sc=np.array([r['lvl'] if (r['bg']>3 and r['bs']>-3) else -999 for r in meta]); top=np.argsort(-sc)[:60] if sel_rel is None else np.argsort(-np.array([r['bg'] for r in meta]))[:60]
    T=np.median(segs[top],axis=0)
    for it in range(4):
        tw=sg.sosfilt(sosw,T.mean(1)[:W+PRE]); n=len(segs); lags=np.zeros(n); corr=np.zeros(n); gains=np.zeros(n)
        for j,s in enumerate(segs):
            sm=sg.sosfilt(sosw,s.mean(1)[:W+PRE]); c=sg.correlate(tw,sm,mode='full'); L=len(sm)-1
            lo=L-int(0.004*SR); hi=L+int(0.004*SR); kk=lo+int(np.argmax(c[lo:hi]))
            y0,y1,y2=c[kk-1],c[kk],c[kk+1]; den=(y0-2*y1+y2); dk=0.5*(y0-y2)/den if den!=0 else 0
            lags[j]=kk-L+dk; corr[j]=c[kk]/(np.sqrt((tw**2).sum()*(sm**2).sum())+1e-12)
        al=np.empty_like(segs)
        for j in range(n):
            for ch in range(2): al[j,:,ch]=frac_shift(segs[j,:,ch],lags[j])
        b=T[:W+PRE].mean(1)
        for j in range(n): gains[j]=np.dot(al[j,:W+PRE].mean(1),b)/np.dot(b,b)
        ok=(corr>cthr)&(gains>gmin)&(gains<gmax)
        if ok.sum()>10:
            sgv=np.array([r['sg'] for r in meta]); med=np.median(sgv[ok]); ok&=(sgv<med+6)
        res=np.array([((al[j]/max(gains[j],1e-3)-T)**2).mean() for j in range(n)])
        # template weights are continuous in corr (logistic, 0.05 wide) instead of a hard corr>cthr cut, and in band mode the template
        # always rests on at least the 8 best-correlating hits: a hard cut let a few borderline flips (float noise between machines)
        # cascade into a template collapsing onto 1-2 hits (verified: -100 dBFS noise changed a band from 28 aligned hits to 16)
        soft=1/(1+np.exp(-(corr-cthr)/0.05))*((gains>gmin)&(gains<gmax))
        if ok.sum()>10: soft=soft*np.where(sgv<med+6,1.0,0.0)
        if sel_rel is not None:
            floor_=np.zeros(n,bool); floor_[np.argsort(-corr)[:min(8,n)]]=True; soft=np.where(floor_,np.maximum(soft,0.5),soft)
        w=soft/(res+1e-9); w/=w.sum()
        T=np.tensordot(w,al/np.maximum(gains,1e-3)[:,None,None],axes=(0,0))
        if verbose: print(f' it{it}: kept {ok.sum()}/{n} corr med {np.median(corr[ok]):.2f} gain sd dB {np.std(20*np.log10(gains[ok])):.1f}')
    if ok.sum()<2: raise ValueError(f'only {int(ok.sum())} hits aligned')
    kept=al[ok]/np.maximum(gains,1e-3)[ok][:,None,None]
    stats={}
    for a,b_,lab in [(0,0.01,'0-10ms'),(0.01,0.05,'10-50'),(0.05,0.15,'50-150'),(0.15,0.4,'150-400'),(0.4,0.9,'400-900')]:
        ia=PRE+int(a*SR); ib=PRE+int(b_*SR); eT=(T[ia:ib]**2).mean(); eI=(kept[:,ia:ib]**2).mean(); N=len(kept)
        C=max((eT-eI/N)/(1-1/N),1e-12); I=max(eI-C,1e-12); stats[lab]=(round(10*np.log10(C*N/I),1),round(10*np.log10(C/I),1),round(10*np.log10(C),1))
        if verbose: print(f'   {lab}: template SNR {stats[lab][0]} dB, single-hit SNR {stats[lab][1]} dB, coherent lvl {stats[lab][2]} dBFS')
    return T, kept, dict(gains=gains[ok].tolist(),corr=corr[ok].tolist(),res=res[ok].tolist(),times=[meta[j]['a']/SR for j in np.where(ok)[0]],starts=[int(meta[j]['a']) for j in np.where(ok)[0]],lags=lags[ok].tolist(),stats=stats)
if __name__=='__main__':
    path,name=sys.argv[1],sys.argv[2]; cthr=float(sys.argv[3]) if len(sys.argv)>3 else 0.5
    x,sr=sf.read(path); assert sr==SR
    T,kept,meta=extract(x,cthr); print(name,'kept',len(kept))
    sf.write(f'x/T_{name}.wav',(T/np.abs(T).max()*0.9).astype(np.float32),SR); np.save(f'x/T_{name}.npy',T); np.save(f'x/kept_{name}.npy',kept); json.dump(meta,open(f'x/meta_{name}.json','w'))
