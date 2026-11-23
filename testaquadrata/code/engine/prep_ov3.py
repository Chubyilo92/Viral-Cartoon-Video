import cv2,numpy as np,json
from PIL import Image
I='img_all/';meta={}
def make(name,src,mfn,box,order,n=30,rad=4,dil=3,outclean=None):
    im=cv2.imread(I+src+'.jpg');h,w=im.shape[:2];x0,y0,x1,y1=int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h)
    m=np.zeros((h,w),np.uint8);sub=im[y0:y1,x0:x1].astype(int);B,G,R=sub[...,0],sub[...,1],sub[...,2]
    m[y0:y1,x0:x1]=mfn(R,G,B).astype(np.uint8)*255
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((2,2),np.uint8))
    clean=cv2.inpaint(im,cv2.dilate(m,np.ones((dil*2+1,dil*2+1),np.uint8)),rad,cv2.INPAINT_TELEA)
    cv2.imwrite('img/'+(outclean or src+'_clean')+'.jpg',clean,[cv2.IMWRITE_JPEG_QUALITY,92])
    if n:
        soft=cv2.GaussianBlur(cv2.dilate(m,np.ones((5,5),np.uint8)),(5,5),0);yy,xx=np.mgrid[y0:y1,x0:x1];o=order((xx-x0)/(x1-x0),(yy-y0)/(y1-y0))
        rgb=cv2.cvtColor(im[y0:y1,x0:x1],cv2.COLOR_BGR2RGB)
        for k in range(1,n+1):
            a=soft[y0:y1,x0:x1].copy();a[o>k/n]=0;Image.fromarray(np.dstack([rgb,a])).save(f'{I}ov/{name}_{k:02d}.png',compress_level=3)
        meta[name]=dict(n=n,box=[x0/w,y0/h,x1/w,y1/h])
red=lambda R,G,B:(R>100)&(R-G>40)&(R-B>30)
make('ultima','e3_wall_ultima',red,(.03,.15,.75,.78),lambda u,v:u,n=30)
make(None,'e3_wall_testaq',red,(.30,.44,.66,.72),None,n=0,rad=6,dil=5)
json.dump(meta,open(I+'ov/meta.json','w'));print(meta)
