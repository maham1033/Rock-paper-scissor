from tkinter import *
from PIL import Image,ImageTk
from random import randint

 # main window
root =  Tk()
root.title("ROCK SCISSOR PAPER")
root.configure(background="#9b59b6")

#picture
rock_image = ImageTk.PhotoImage(Image.open("rock_user.jpg"))
paper_image = ImageTk.PhotoImage(Image.open("paper_user.jpg")) 
scissor_image = ImageTk.PhotoImage(Image.open("scissor_user.jpg")) 
rock_image_comp = ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_image_comp = ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_image_comp = ImageTk.PhotoImage(Image.open("scissor.jpg"))

#insert picture
user_label = Label(root,image=scissor_image,bg="#9b59b6")
comp_label = Label(root,image=scissor_image_comp)
user_label.grid(row=1,column=4)
comp_label.grid(row=1,column=0)


#scores
playerScore=Label(root,text=0,font=50,bg="#9b59b6",fg="white")
computerScore=Label(root,text=0,font=50,bg="#9b59b6",fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=30,text="USER",bg="#9b59b6",fg="white")
comp_indicator= Label(root,font=30,text="COMPUTER",
                      bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg = Label(root, font=50,bg= "#9b59b6", fg="white",text="you loose")
msg.grid(row=3, column=2)

#update message
def updateMessage(x):
    msg['text'] = x

    #update user score
def updateUserScore():
        score=int(playerScore["text"])
        score += 1
        playerScore["text"] = str(score)

#update computer score

def updateCompScore():
        score=int(computerScore["text"])
        score += 1
        computerScore["text"] = str(score)

#check winner
def checkWin(player,computer):
    if player == computer:
        updateMessage("Its a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("you loose")
            updateCompScore()
        else:
             updateMessage("you win")
             updateUserScore
    elif player == "paper":
        if computer == "scissor":
            updateMessage("you loose")
            updateCompScore()
        else:
            updateMessage("you win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("you loose")
            updateCompScore()
        else:
            updateMessage("you win")
            updateCompScore()
    
    else:
        pass
        

#update choices

choices = ["rock","paper","scissor"]


def updatechoice(x):

#for computer
  compChoice = choices[randint(0,2)]
  if compChoice == "rock":
      comp_label.configure(image=rock_image_comp)
  elif compChoice == "paper":
      comp_label.configure(image=paper_image_comp)
  else :
      comp_label.configure(image=scissor_image_comp)


    #for user
  if x=="rock":
       user_label.configure(image=rock_image)
  elif x=="paper":
        user_label.configure(image=paper_image)
  else:
        user_label.configure(image=scissor_image)

  checkWin(x,compChoice)
# buttons
rock = Button(root,width=10,height=2, text="ROCK",
              bg="#FF3E4D",fg="white",command=lambda:updatechoice("rock")).grid(row=2,column=1)
paper = Button(root,width=10,height=2, text="PAPER",
              bg="#FAD02E",fg="white",command=lambda:updatechoice("paper")).grid(row=2,column=2)
scissor= Button(root,width=10,height=2, text="SCISSOR",
             bg="#0ABDE3",fg="white",command=lambda:updatechoice("scissor")).grid(row=2,column=3)

root.mainloop()