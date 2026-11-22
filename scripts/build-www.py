#!/usr/bin/env python3
"""يبني www/index.html من src/index.source.html (نسخة تعمل دون إنترنت: مكتبات وخطوط محلية)."""
import re,sys,os
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(root+'/src/index.source.html',encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s,a[:60]
    s=s.replace(a,b)
s=re.sub(r'<link rel="preconnect"[^>]*>\n','',s)
s=re.sub(r'<link href="https://fonts.googleapis.com[^>]*>\n','<link rel="stylesheet" href="fonts/fonts.css">\n<link rel="manifest" href="manifest.webmanifest">\n<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">\n<meta name="theme-color" content="#0b6e6e">\n',s)
rep('<meta name="viewport" content="width=device-width, initial-scale=1">','<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">')
rep('https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js','lib/xlsx.full.min.js')
rep('https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js','lib/html2canvas.min.js')
rep('https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js','lib/jspdf.umd.min.js')
rep('https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js','lib/qrcode.min.js')
rep('https://cdnjs.cloudflare.com/ajax/libs/jsQR/1.4.0/jsQR.min.js','lib/jsQR.min.js')
rep('https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js','lib/pdf.min.js')
rep('https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js','lib/pdf.worker.min.js')
rep("if(document.getElementById(id))return res();","if(window.GB_LOCAL||document.getElementById(id))return res();")
rep("<script>\n(function(){","<script>window.GB_LOCAL=1;</script>\n<script>\n(function(){") if "<script>\n(function(){" in s else None
rep("renderSyncBadge();if(pinData())","if('serviceWorker' in navigator&&/^https?:$/.test(location.protocol)&&!isNative()){navigator.serviceWorker.register('sw.js').catch(function(){})}\nrenderSyncBadge();if(pinData())")
rep("*{box-sizing:border-box}","*{box-sizing:border-box}\nbody{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}")
open(root+'/www/index.html','w',encoding='utf-8').write(s)
print('built www/index.html',len(s)//1024,'KB')
