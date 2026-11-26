from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random
W,H,FRAMES=960,440,48
random.seed(23)
def font(size,bold=False):
 p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
 try:return ImageFont.truetype(p,size)
 except OSError:return ImageFont.load_default()
MONO=font(13); SMALL=font(10); TITLE=font(17,True)
def frame_image(n):
 im=Image.new("RGB",(W,H)); px=im.load()
 for y in range(H):
  t=y/H; c=(int(7+5*t),int(13+8*t),int(23+12*t))
  for x in range(W):px[x,y]=c
 d=ImageDraw.Draw(im,"RGBA")
 for x in range(20,W,32):d.line((x,0,x,H),fill=(68,126,157,15))
 for y in range(18,H,32):d.line((0,y,W,y),fill=(68,126,157,15))
 for k in range(9):
  x=(k*137+n*3)%W; d.ellipse((x,22,x+3,25),fill=(65,224,190,120))
 d.rounded_rectangle((24,18,936,58),10,fill="#0d1b2b",outline="#21445a")
 d.ellipse((43,32,55,44),fill="#36dda2")
 d.text((68,29),"DIGANTH  /  DEV ENVIRONMENT",font=TITLE,fill="#d9f4ff")
 d.text((690,32),"SESSION: ACTIVE",font=SMALL,fill="#66e5b5"); d.ellipse((900,33,910,43),fill="#43e6a7")
 # terminal
 d.rounded_rectangle((24,76,292,345),12,fill="#0b1725",outline="#24536a",width=2)
 d.rounded_rectangle((24,76,292,111),12,fill="#11263a",outline="#24536a")
 d.text((42,87),"TERMINAL  //  zsh",font=SMALL,fill="#a9c8d9")
 for i,col in enumerate(("#ff6b79","#ffc45d","#45d89b")):d.ellipse((245+i*13,89,252+i*13,96),fill=col)
 lines=[("$ git status","#70dcf1"),("On branch main","#8ce4b4"),("working tree clean","#8ce4b4"),("$ mvn clean install","#70dcf1"),("[INFO] compiling modules","#a8c8da"),("[INFO] tests passed","#8ce4b4"),("$ git push origin main","#70dcf1"),("Enumerating objects...","#a8c8da"),("Writing objects: 100%","#8ce4b4")]
 for i,(txt,col) in enumerate(lines[:min(len(lines),2+n//5)]):
  yy=132+i*22
  if yy<326:d.text((42,yy),txt,font=SMALL,fill=col)
 if (n//5)%2==0:d.rectangle((42,323,50,336),fill="#4be6ae")
 # editor
 d.rounded_rectangle((309,76,676,345),12,fill="#0b1827",outline="#286078",width=2)
 d.rounded_rectangle((309,76,676,111),12,fill="#102438",outline="#286078")
 d.text((328,87),"APPLICATION.JAVA",font=SMALL,fill="#b7d5e6"); d.text((598,87),"● RUN",font=SMALL,fill="#52e3a7")
 code=[("public class Application {","#74c9ff"),("  public static void main","#c4a7ff"),("      (String[] args) {","#c4a7ff"),("    Developer dev =","#e5edf7"),("      new Developer();","#e5edf7"),("    dev.build(\"ideas\");","#72e3bd"),("    dev.test();","#72e3bd"),("    dev.deploy();","#72e3bd"),("  }","#c4a7ff"),("}","#74c9ff")]
 for i,(txt,col) in enumerate(code):
  yy=128+i*20; d.text((331,yy),f"{i+1:02}",font=SMALL,fill="#56768b"); d.text((360,yy),txt,font=SMALL,fill=col)
 a=(n//6)%len(code); d.rounded_rectangle((354,125+a*20,658,143+a*20),3,outline=(54,218,185,130),width=1)
 # telemetry
 d.rounded_rectangle((693,76,936,345),12,fill="#0b1725",outline="#24536a",width=2)
 d.rounded_rectangle((693,76,936,111),12,fill="#11263a",outline="#24536a")
 d.text((711,87),"SYSTEM TELEMETRY",font=SMALL,fill="#b7d5e6")
 d.text((711,129),"BUILD PIPELINE",font=SMALL,fill="#63dfb1")
 d.rounded_rectangle((711,147,916,157),5,fill="#1c3445")
 prog=(n*4)%210; d.rounded_rectangle((711,147,711+max(8,prog),157),5,fill="#39d99b")
 d.text((711,178),"NETWORK ACTIVITY",font=SMALL,fill="#63dfb1")
 pts=[]
 for i in range(28):
  x=711+i*7.2; y=226+math.sin((i+n*.65)*.62)*14+math.sin((i+n*.3)*1.4)*5; pts.append((x,y))
 d.line(pts,fill="#43dcb8",width=2)
 for x,y in pts[::5]:d.ellipse((x-2,y-2,x+2,y+2),fill="#8bfff0")
 d.text((711,259),"CPU   34%",font=SMALL,fill="#a8c8da"); d.text((817,259),"RAM   62%",font=SMALL,fill="#a8c8da")
 d.text((711,300),"DEPLOYMENT",font=SMALL,fill="#a8c8da"); d.text((815,300),"READY",font=SMALL,fill="#5be6ac")
 # animated data glyphs on the far edges
 chars="01{}[]<>/;#"
 for col in range(34):
  x=12+col*28; head=(n*5+col*19)%500-50
  for j in range(4):
   yy=(head-j*18)%460
   if 58<yy<370 and (x<22 or x>938):d.text((x,yy),random.choice(chars),font=SMALL,fill=(51,210,168,max(20,105-j*23)))
 # footer
 d.rounded_rectangle((24,365,936,420),10,fill="#0d1b2a",outline="#21445a")
 d.text((45,378),"●  LIVE CODING SESSION",font=SMALL,fill="#5be6ac")
 d.text((45,397),"CODE  →  DEBUG  →  TEST  →  DEPLOY",font=SMALL,fill="#a9c8d9")
 scan=24+(n*21)%912; d.line((scan,365,scan,419),fill=(63,222,190,65),width=2)
 for i in range(24):
  x=580+i*12; h=5+int((math.sin(n*.25+i*.7)+1)*6)
  d.rounded_rectangle((x,392-h,x+5,392+h),2,fill=(57,216,177,160))
 glow=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
 gd.rounded_rectangle((305,72,680,349),15,outline=(49,211,224,60),width=5)
 glow=glow.filter(ImageFilter.GaussianBlur(9))
 return Image.alpha_composite(im.convert("RGBA"),glow).convert("P",palette=Image.Palette.ADAPTIVE)
frames=[frame_image(i) for i in range(FRAMES)]
frames[0].save("developer-live-environment.gif",save_all=True,append_images=frames[1:],duration=95,loop=0,optimize=True,disposal=2)
