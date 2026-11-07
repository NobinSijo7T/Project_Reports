import os
from PIL import Image
import numpy as np

for i in range(1, 35):
    ref_p = f"pdf_renders/page_{i:02d}.png"
    rep_p = f"report_renders/page_{i:02d}.png"
    if os.path.exists(ref_p) and os.path.exists(rep_p):
        im_ref = Image.open(ref_p).convert('L')
        im_rep = Image.open(rep_p).convert('L')
        
        # resize if slightly different
        if im_ref.size != im_rep.size:
            im_rep = im_rep.resize(im_ref.size)
            
        arr_ref = np.array(im_ref, dtype=np.float32)
        arr_rep = np.array(im_rep, dtype=np.float32)
        
        # compute mean absolute difference
        diff = np.abs(arr_ref - arr_rep).mean()
        # compute correlation
        corr = np.corrcoef(arr_ref.flatten(), arr_rep.flatten())[0, 1]
        print(f"Page {i:02d}: diff={diff:5.2f}, correlation={corr:.4f}")

