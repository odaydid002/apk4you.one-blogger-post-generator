from tkinter import *
import os
def submit():
    g = open('yourCode.txt','w')
    g.close
    tagcode=''
    h=open('tags.txt','r')
    tag=''
    tagList = ['']
    for lines in h:
        tag = lines.replace(',','')
        tagList.append(tag)
    for t in tagList:
        code = ("\n <div>"+'<h2 style="text-align: left;"><span style="font-size: 16px; font-weight: normal; padding-bottom: 0px;"><a href="https://letmegooglethat.com/?q='+t.replace(' ','+')+'" target="_blank">'+str(t)+'</a></span></h2> </div>')
        tagcode += code
    title = titled.get()
    titled.delete(0,'end')
    mainImg = mainImgd.get()
    mainImgd.delete(0,'end')
    s1Img = s1Imgd.get()
    s1Imgd.delete(0,'end')
    s2Img = s2Imgd.get()
    s2Imgd.delete(0,'end')
    s3Img = s3Imgd.get()
    s3Imgd.delete(0,'end')
    description = descriptiond.get()
    descriptiond.delete(0,'end')
    link = linkd.get()
    check = ''
    for i in range(0,8):
        check += link[i]
    if check == 'https://' or check == 'HTTPS://' or check == 'Https://':
        pass
    else:
        link = 'https://' + link  
    linkd.delete(0,'end')
    labelsub = Label(window,text="Code Created Successful!",fg='white',font=('Arial',12),bg='#1f1f1f')
    labelsub.grid(column=1,row=9)
    titleCode = '\n <div> <h1 style="text-align: center;"><span style="color: #f3f3f3; font-family: Anton; letter-spacing: 1px;">'+str(title)+' </span></h1></div><br />'
    mainCode = ' <div> \n <div class="separator" style="clear: both; text-align: center;"> \n <a href="'+str(mainImg)+'" \n style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="1080" data-original-width="1920" height="296" src="'+str(mainImg)+'" \n width="526" /></a> \n </div><br /> \n <p style="text-align: left;"><span style="color: #eeeeee; font-family: Play; font-size: medium;">'+ str(description) +'</span></p>    \n <p    \n style="text-align: left;"></p>        \n <div class="separator" style="clear: both; text-align: center;">            \n <a href="'+str(s1Img)+'"            \n style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="422" data-original-width="750" height="180" src="'+str(s1Img)+'"                \n width="320" /></a>                   \n </div><br />       \n <div class="separator" style="clear: both; text-align: center;">            \n <a href="'+str(s2Img)+'"           \n style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="422" data-original-width="750" height="180" src="'+str(s2Img)+'" \n width="320" /></a> \n </div><br /> \n <div class="separator" style="clear: both; text-align: center;"> \n <a href=" '+str(s3Img)+' " \n style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="422" data-original-width="750" height="180" src="'+str(s3Img)+'" \n width="320" /></a> \n </div>\n <br /> </div>'
    downloadCode = '\n <div> <div style="align-items: center; display: flex; flex-direction: row; justify-content: center;"> \n <div id="app"></div> \n <br /> \n <div id="container99" >  \n <a atribut="_blank" href="'+str(link)+'" style="text-decoration: none;">  \n   <button class="glow-on-hover" style="background-color: red;" type="button">  \n    <span style="color: white;"> Download </span>  \n   </button>  \n </a> \n</div> \n</div> \n <script>  \n var content = document.getElementById("container99");  \n content.style.display="none"; \n  setTimeout(function(){ \n    content.style.display="block"; \n  }, 20000); \n </script> \n \n <script> \n  const FULL_DASH_ARRAY = 283; \n const WARNING_THRESHOLD = 10; \n const ALERT_THRESHOLD = 5; \n \n const COLOR_CODES = {   \n info: {   \n  color: "green"  \n },  \n warning: {   \n  color: "orange",   \n threshold: WARNING_THRESHOLD \n  }, \n alert: {   \n  color: "red",   \n  threshold: ALERT_THRESHOLD \n  } \n }; \n \n const TIME_LIMIT = 20; \n let timePassed = 0; \n let timeLeft = TIME_LIMIT; \n let timerInterval = null; \n let remainingPathColor = COLOR_CODES.info.color; \n \n document.getElementById("app").innerHTML = ` \n <div class="base-timer">  \n  <svg class="base-timer__svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"> \n <g class="base-timer__circle">     \n  <circle class="base-timer__path-elapsed" cx="50" cy="50" r="45"></circle> \n <path \n  id="base-timer-path-remaining" \n stroke-dasharray="283" \n class="base-timer__path-remaining ${remainingPathColor}" \n d=" \n   M 50, 50 \n  m -45, 0 \n a 45,45 0 1,0 90,0 \n  a 45,45 0 1,0 -90,0  \n  "  \n  ></path> \n  </g> \n  </svg> \n  <span id="base-timer-label" class="base-timer__label">${formatTime(  \n   timeLeft \n  )}</span> \n </div>  \n `; \n \n startTimer(); \n \n function onTimesUp() {  \n clearInterval(timerInterval); \n } \n \n function startTimer() { \n  timerInterval = setInterval(() => {   \n  timePassed = timePassed += 1;   \n  timeLeft = TIME_LIMIT - timePassed;   \n  document.getElementById("base-timer-label").innerHTML = formatTime(    \n   timeLeft   \n  );   \n  setCircleDasharray(); \n  setRemainingPathColor(timeLeft);    \n  if (timeLeft === 0) {   \n    onTimesUp();   \n  }  \n }, 1000);  \n } \n function formatTime(time) {  \n const minutes = Math.floor(time / 60); \n let seconds = time % 60; \n  \n if (seconds < 10) {  \n   seconds = `0${seconds}`; \n  } \n \n  return `${minutes}:${seconds}`; \n } \n \n function setRemainingPathColor(timeLeft) {  \n const { alert, warning, info } = COLOR_CODES;  \n if (timeLeft <= alert.threshold) {   \n  document \n    .getElementById("base-timer-path-remaining") \n     .classList.remove(warning.color); \n   document \n    .getElementById("base-timer-path-remaining") \n     .classList.add(alert.color);  \n } else if (timeLeft <= warning.threshold) {  \n   document \n     .getElementById("base-timer-path-remaining")  \n     .classList.remove(info.color);  \n   document  \n     .getElementById("base-timer-path-remaining")  \n     .classList.add(warning.color); \n  } \n } \n \n function calculateTimeFraction() {  \n const rawTimeFraction = timeLeft / TIME_LIMIT; \n  return rawTimeFraction - (1 / TIME_LIMIT) * (1 - rawTimeFraction); \n } \n function setCircleDasharray() { \n const circleDasharray = `${(   \n  calculateTimeFraction() * FULL_DASH_ARRAY \n  ).toFixed(0)} 283`;  \n document   \n  .getElementById("base-timer-path-remaining")  \n  .setAttribute("stroke-dasharray", circleDasharray); \n } \n </script> \n </div>'
    Tags = '\n <div> <div><h3><span style="color: white;"><i><u>More Links:</u></i></span></h3></div> </div>'
    tagCode = tagcode
    post = str(titleCode) + str(mainCode) + str(downloadCode) + str(Tags) + str(tagCode)
    e = open('yourCode.txt','r+')
    e.write('\n'+post)
    e.close
    g.close
    yourCode.grid(row=8,column=0)

def openCode():
    os.system('start yourCode.txt')
    window.destroy()
    
window = Tk()

window.geometry("640x360")
window.title("Apk4you")


os.system('start tags.txt')
h=open('tags.txt','w')

icon = PhotoImage(file=("icon.png"))
window.iconphoto(True,icon)
window.config(background="#1f1f1f")

label1=Label(window,text='Title',fg='White',font=('Arial',14),bg="#1f1f1f")
label1.grid(row=0,column=0)

titled = Entry()
titled.config(font=("Arial",25),bg="#404040",fg='white')
titled.grid(row=0,column=1)

label2=Label(window,text='Main Image URL',fg='White',font=('Arial',14),bg="#1f1f1f")
label2.grid(row=1,column=0)

mainImgd = Entry()
mainImgd.config(font=("Arial",25))
mainImgd.config(bg=("#404040"))
mainImgd.config(fg=('white'))
mainImgd.grid(row=1,column=1)

label3=Label(window,text='Screenshot1',fg='White',font=('Arial',14),bg="#1f1f1f")
label3.grid(row=2,column=0)

s1Imgd = Entry()
s1Imgd.config(font=("Arial",25))
s1Imgd.config(bg=("#404040"))
s1Imgd.config(fg=('white'))
s1Imgd.grid(row=2,column=1)

label4=Label(window,text='Screenshot2',fg='White',font=('Arial',14),bg="#1f1f1f")
label4.grid(row=3,column=0)

s2Imgd = Entry()
s2Imgd.config(font=("Arial",25))
s2Imgd.config(bg=("#404040"))
s2Imgd.config(fg=('white'))
s2Imgd.grid(row=3,column=1)

label5=Label(window,text='Screenshot3',fg='White',font=('Arial',14),bg="#1f1f1f")
label5.grid(row=4,column=0)

s3Imgd = Entry()
s3Imgd.config(font=("Arial",25))
s3Imgd.config(bg=("#404040"))
s3Imgd.config(fg=('white'))
s3Imgd.grid(row=4,column=1)

label6=Label(window,text='Download Link',fg='White',font=('Arial',14),bg="#1f1f1f")
label6.grid(row=5,column=0)

linkd = Entry()
linkd.config(font=("Arial",25))
linkd.config(bg=("#404040"))
linkd.config(fg=('white'))
linkd.grid(row=5,column=1)

label7=Label(window,text='Description',fg='White',font=('Arial',14),bg="#1f1f1f")
label7.grid(row=6,column=0)

descriptiond = Entry()
descriptiond.config(font=("Arial",25))
descriptiond.config(bg=("#404040"))
descriptiond.config(fg=('white'))
descriptiond.grid(row=6,column=1)

submit = Button(window,text="Post",command=submit)
submit.grid(row=8,column=1)
yourCode = Button(window,text="Your Code",command=openCode)

window.mainloop()

