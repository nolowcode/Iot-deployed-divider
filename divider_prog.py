import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
D0=10
D1=11
led=32
beep=15
trig=12
echo=13
trig_r=18
echo_r=19
rs,en,d4,d5,d6,d7=38,40,31,33,35,37
M1_1=3
M1_2=5
M2_1=7
M2_2=8
GPIO.setup(D0,GPIO.IN)
GPIO.setup(D1,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(beep,GPIO.OUT)
GPIO.setup(rs,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(d4,GPIO.OUT)
GPIO.setup(d5,GPIO.OUT)
GPIO.setup(d6,GPIO.OUT)
GPIO.setup(d7,GPIO.OUT)
GPIO.setup(M1_1,GPIO.OUT)
GPIO.setup(M1_2,GPIO.OUT)
GPIO.setup(M2_1,GPIO.OUT)
GPIO.setup(M2_2,GPIO.OUT)
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(trig_r,GPIO.OUT)
GPIO.setup(echo_r,GPIO.IN)

def lcd(upper,lower):
  def enable():
    GPIO.output(en,1)
    time.sleep(0.010)
    GPIO.output(en,0)
    time.sleep(0.010)

  def cmd(x):
    GPIO.output(rs,0)
    GPIO.output(d4,0)
    GPIO.output(d5,0)
    GPIO.output(d6,0)
    GPIO.output(d7,0)
    if(x & 0x10 == 0x10):
      GPIO.output(d4,1)
    if(x & 0x20 == 0x20):
      GPIO.output(d5,1)
    if(x & 0x40 == 0x40):
      GPIO.output(d6,1)
    if(x & 0x80 == 0x80):
      GPIO.output(d7,1)
    enable()
    GPIO.output(d4,0)
    GPIO.output(d5,0)
    GPIO.output(d6,0)
    GPIO.output(d7,0)
    if(x & 0x01 == 0x01):
      GPIO.output(d4,1)
    if(x & 0x02 == 0x02):
      GPIO.output(d5,1)
    if(x & 0x04 == 0x04):
      GPIO.output(d6,1)
    if(x & 0x08 == 0x08):
      GPIO.output(d7,1)
    enable()
  def data(y):
    GPIO.output(rs,1)
    GPIO.output(d4,0)
    GPIO.output(d5,0)
    GPIO.output(d6,0)
    GPIO.output(d7,0)
    if(y & 0x10 == 0x10):
      GPIO.output(d4,1)
    if(y & 0x20 == 0x20):
      GPIO.output(d5,1)
    if(y & 0x40 == 0x40):
      GPIO.output(d6,1)
    if(y & 0x80 == 0x80):
      GPIO.output(d7,1)
    enable()
    GPIO.output(d4,0)
    GPIO.output(d5,0)
    GPIO.output(d6,0)
    GPIO.output(d7,0)
    if(y & 0x01 == 0x01):
      GPIO.output(d4,1)
    if(y & 0x02 == 0x02):
      GPIO.output(d5,1)
    if(y & 0x04 == 0x04):
      GPIO.output(d6,1)
    if(y & 0x08 == 0x08):
      GPIO.output(d7,1)
    enable()
  
  def init():
    cmd(0x33)
    cmd(0x32)
    cmd(0x28)
    cmd(0x06)
    cmd(0x0E)
    cmd(0x01)

  def str1(z):
    for i in range(len(z)):
      data(ord(z[i]));

  init()
  cmd(0x80)
  str1("Right:"+str(upper)+"%")
  cmd(0xC0)
  str1("Left:"+str(lower)+"%")
  time.sleep(5)

def lcd_divider(upper,lower):
  def enable():
    GPIO.output(en,1)
    time.sleep(0.010)
    GPIO.output(en,0)
    time.sleep(0.010)

  def cmd(x):
    GPIO.output(rs,0)
    GPIO.output(d4,0)
    GPIO.output(d5,0)
    GPIO.output(d6,0)
    GPIO.output(d7,0)
    if(x & 0x10 == 0x10):
      GPIO.output(d4,1)
    if(x & 0x20 == 0x20):
      GPIO.output(d5,1)
    if(x & 0x40 == 0x40):
      GPIO.output(d6,1)
    if(x & 0x80 == 0x80):
      GPIO.output(d7,1)
    enable()
    GPIO.output(d4,0)
    GPIO.output(d5,0)
    GPIO.output(d6,0)
    GPIO.output(d7,0)
    if(x & 0x01 == 0x01):
      GPIO.output(d4,1)
    if(x & 0x02 == 0x02):
      GPIO.output(d5,1)
    if(x & 0x04 == 0x04):
      GPIO.output(d6,1)
    if(x & 0x08 == 0x08):
      GPIO.output(d7,1)
    enable()
  def data(y):
    GPIO.output(rs,1)
    GPIO.output(d4,0)
    GPIO.output(d5,0)
    GPIO.output(d6,0)
    GPIO.output(d7,0)
    if(y & 0x10 == 0x10):
      GPIO.output(d4,1)
    if(y & 0x20 == 0x20):
      GPIO.output(d5,1)
    if(y & 0x40 == 0x40):
      GPIO.output(d6,1)
    if(y & 0x80 == 0x80):
      GPIO.output(d7,1)
    enable()
    GPIO.output(d4,0)
    GPIO.output(d5,0)
    GPIO.output(d6,0)
    GPIO.output(d7,0)
    if(y & 0x01 == 0x01):
      GPIO.output(d4,1)
    if(y & 0x02 == 0x02):
      GPIO.output(d5,1)
    if(y & 0x04 == 0x04):
      GPIO.output(d6,1)
    if(y & 0x08 == 0x08):
      GPIO.output(d7,1)
    enable()
  
  def init():
    cmd(0x33)
    cmd(0x32)
    cmd(0x28)
    cmd(0x06)
    cmd(0x0E)
    cmd(0x01)

  def str1(z):
    for i in range(len(z)):
      data(ord(z[i]));

  init()
  cmd(0x80)
  str1(str(upper))
  cmd(0xC0)
  str1(str(lower))
    

def motor_left():
  GPIO.output(M1_1,0)
  GPIO.output(M1_2,1)
  GPIO.output(M2_1,0)
  GPIO.output(M2_2,1)
  time.sleep(1)

def motor_right():
  GPIO.output(M1_1,1)
  GPIO.output(M1_2,0)
  GPIO.output(M2_1,1)
  GPIO.output(M2_2,0)
  time.sleep(1)
  
def motor_off():
  GPIO.output(M1_1,0)
  GPIO.output(M1_2,0)
  GPIO.output(M2_1,0)
  GPIO.output(M2_2,0)


def ir_sense():
  r_on = 0.0
  l_on = 0.0
  for i in range (0,250):
    a=GPIO.input(D0)
    b=GPIO.input(D1)
    if a==0:
      r_on += 1
    if b==0:
      l_on += 1    
    print (a)
    print (b)
    i+=1
    time.sleep(0.04)
  r_dense=r_on/2.5
  l_dense=l_on/2.5 
  print ("Reflected time in right ir is:"+str(r_dense))
  print ("Reflected time in left ir is:"+str(l_dense))
  return r_dense,l_dense;

def ultra_l():
    stop=0.0
    GPIO.output(trig,1)
    time.sleep(0.0001)
    GPIO.output(trig,0)
    while (GPIO.input(echo)==0):
      start=time.time()
    while (GPIO.input(echo)==1):
      stop=time.time()
    elapsed=stop-start
    distance=(elapsed*17150)
    distance=round(distance+1.15,2)
    print(distance)
    return distance

def ultra_r():
    stop=0.0
    GPIO.output(trig_r,1)
    time.sleep(0.0001)
    GPIO.output(trig_r,0)
    while (GPIO.input(echo_r)==0):
      start=time.time()
    while (GPIO.input(echo_r)==1):
      stop=time.time()
    elapsed=stop-start
    distance=(elapsed*17150)
    distance=round(distance+1.15,2)
    print(distance)
    return distance

def motor():
  if r_dens > l_dens:
    lcd_divider("Moving direction","<- <- <- <- <-")
    j=0
    while 1:
      dis_l=ultra_l()
      if dis_l < 7:
        motor_off()
        GPIO.output(beep,1)
        time.sleep(0.5)
      elif dis_l >7:
        GPIO.output(beep,0)
        motor_left()
        j=j+1
      if j==3:
        break 
    motor_off()
  elif l_dens > r_dens:
    lcd_divider("Moving direction","-> -> -> -> ->")
    j=0
    while 1:
      dis_r=ultra_r()
      if dis_r < 7:
        motor_off()
        GPIO.output(beep,1)
        time.sleep(0.5)
      elif dis_r >7:
        GPIO.output(beep,0)
        motor_right()
        j=j+1
      if j==3:
        break 
    motor_off()

r_dens,l_dens=ir_sense()
lcd(r_dens,l_dens)
motor()