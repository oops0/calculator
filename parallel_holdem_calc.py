import multiprocessing
import time
import holdem_argparser
import holdem_functions
import tkinter
from tkinter import *

class calcGUI:
    def __init__(self, master):
        self.master = master
        master.title = "Short Deck"
        
        self.label = Label(master, text="Short Deck")
        
        self.calc_click = Button(master, text="Calculate", command=self.calc_click)
        self.calc_click.grid(columnspan=6)
        
        self.p1hand = StringVar()
        self.p2hand = StringVar()
        self.board_cards = StringVar()
        
        self.p1text = Entry(master, textvariable=self.p1hand)
        self.p1text.grid()
        self.p2text = Entry(master, textvariable=self.p2hand)
        self.p2text.grid()
        self.boardtext = Entry(master, textvariable=self.board_cards)
        self.boardtext.grid()
        
        self.v = IntVar()
        self.radio_btn = Radiobutton(master, text="P1", variable=self.v, value=1)
        self.radio_btn.grid()
        self.radio_btn = Radiobutton(master, text="P2", variable=self.v, value=2)
        self.radio_btn.grid()
        self.radio_btn = Radiobutton(master, text="Board", variable=self.v, value=3)
        self.radio_btn.grid()
        self.v.set(1)
        
        self.Ac_button = Button(master, text="Ac", command=self.Ac_click)
        self.Ac_button.grid(row=1, column=1)
        self.Ad_button = Button(master, text="Ad", command=self.Ad_click)
        self.Ad_button.grid(row=1, column=2)
        self.Ah_button = Button(master, text="Ah", command=self.Ah_click)
        self.Ah_button.grid(row=1, column=3)
        self.As_button = Button(master, text="As", command=self.As_click)
        self.As_button.grid(row=1, column=4)
    
        self.Kc_button = Button(master, text="Kc", command=self.Kc_click)
        self.Kc_button.grid(row=2, column=1)
        self.Kd_button = Button(master, text="Kd", command=self.Kd_click)
        self.Kd_button.grid(row=2, column=2)
        self.Kh_button = Button(master, text="Kh", command=self.Kh_click)
        self.Kh_button.grid(row=2, column=3)
        self.Ks_button = Button(master, text="Ks", command=self.Ks_click)
        self.Ks_button.grid(row=2, column=4)
        
        self.Qc_button = Button(master, text="Qc", command=self.Qc_click)
        self.Qc_button.grid(row=3, column=1)
        self.Qd_button = Button(master, text="Qd", command=self.Qd_click)
        self.Qd_button.grid(row=3, column=2)
        self.Qh_button = Button(master, text="Qh", command=self.Qh_click)
        self.Qh_button.grid(row=3, column=3)
        self.Qs_button = Button(master, text="Qs", command=self.Qs_click)
        self.Qs_button.grid(row=3, column=4)
        
        self.Jc_button = Button(master, text="Jc", command=self.Jc_click)
        self.Jc_button.grid(row=4, column=1)
        self.Jd_button = Button(master, text="Jd", command=self.Jd_click)
        self.Jd_button.grid(row=4, column=2)
        self.Jh_button = Button(master, text="Jh", command=self.Jh_click)
        self.Jh_button.grid(row=4, column=3)
        self.Js_button = Button(master, text="Js", command=self.Js_click)
        self.Js_button.grid(row=4, column=4)
        
        self.Tc_button = Button(master, text="Tc", command=self.Tc_click)
        self.Tc_button.grid(row=5, column=1)
        self.Td_button = Button(master, text="Td", command=self.Td_click)
        self.Td_button.grid(row=5, column=2)
        self.Th_button = Button(master, text="Th", command=self.Th_click)
        self.Th_button.grid(row=5, column=3)
        self.Ts_button = Button(master, text="Ts", command=self.Ts_click)
        self.Ts_button.grid(row=5, column=4)
        
        self.Ninec_button = Button(master, text="9c", command=self.Ninec_click)
        self.Ninec_button.grid(row=6, column=1)
        self.Nined_button = Button(master, text="9d", command=self.Nined_click)
        self.Nined_button.grid(row=6, column=2)
        self.Nineh_button = Button(master, text="9h", command=self.Nineh_click)
        self.Nineh_button.grid(row=6, column=3)
        self.Nines_button = Button(master, text="9s", command=self.Nines_click)
        self.Nines_button.grid(row=6, column=4)
        
        self.Eightc_button = Button(master, text="8c", command=self.Eightc_click)
        self.Eightc_button.grid(row=7, column=1)
        self.Eightd_button = Button(master, text="8d", command=self.Eightd_click)
        self.Eightd_button.grid(row=7, column=2)
        self.Eighth_button = Button(master, text="8h", command=self.Eighth_click)
        self.Eighth_button.grid(row=7, column=3)
        self.Eights_button = Button(master, text="8s", command=self.Eights_click)
        self.Eights_button.grid(row=7, column=4)
        
        self.Sevenc_button = Button(master, text="7c", command=self.Sevenc_click)
        self.Sevenc_button.grid(row=8, column=1)
        self.Sevend_button = Button(master, text="7d", command=self.Sevend_click)
        self.Sevend_button.grid(row=8, column=2)
        self.Sevenh_button = Button(master, text="7h", command=self.Sevenh_click)
        self.Sevenh_button.grid(row=8, column=3)
        self.Sevens_button = Button(master, text="7s", command=self.Sevens_click)
        self.Sevens_button.grid(row=8, column=4)
        
        self.Sixc_button = Button(master, text="6c", command=self.Sixc_click)
        self.Sixc_button.grid(row=9, column=1)
        self.Sixd_button = Button(master, text="6d", command=self.Sixd_click)
        self.Sixd_button.grid(row=9, column=2)
        self.Sixh_button = Button(master, text="6h", command=self.Sixh_click)
        self.Sixh_button.grid(row=9, column=3)
        self.Sixs_button = Button(master, text="6s", command=self.Sixs_click)
        self.Sixs_button.grid(row=9, column=4)
    
    def calc_click(self):
        input = open('input.txt', 'w+')
        inputtext = self.p1hand.get() + " " + self.p2hand.get()
        boardlen = len(self.board_cards.get())
        if(boardlen > 0):
          inputtext = inputtext + "|" + self.board_cards.get()
        input.write(inputtext)
        
        if(boardlen == 2 or boardlen == 5):
          print('Invalid board')
          return
        
        thing = input.read()
        print(thing)
        hole_cards, num, exact, board, file_name = None, 100000, True, None, "input.txt"
        run(hole_cards, num, exact, board, file_name, True)
        
        self.Ac_button.config(relief=RAISED)
        self.Ad_button.config(relief=RAISED)
        self.Ah_button.config(relief=RAISED)
        self.As_button.config(relief=RAISED)
        
        self.Kc_button.config(relief=RAISED)
        self.Kd_button.config(relief=RAISED)
        self.Kh_button.config(relief=RAISED)
        self.Ks_button.config(relief=RAISED)
        
        self.Qc_button.config(relief=RAISED)
        self.Qd_button.config(relief=RAISED)
        self.Qh_button.config(relief=RAISED)
        self.Qs_button.config(relief=RAISED)
        
        self.Jc_button.config(relief=RAISED)
        self.Jd_button.config(relief=RAISED)
        self.Jh_button.config(relief=RAISED)
        self.Js_button.config(relief=RAISED)
        
        self.Tc_button.config(relief=RAISED)
        self.Td_button.config(relief=RAISED)
        self.Th_button.config(relief=RAISED)
        self.Ts_button.config(relief=RAISED)
        
        self.Ninec_button.config(relief=RAISED)
        self.Nined_button.config(relief=RAISED)
        self.Nineh_button.config(relief=RAISED)
        self.Nines_button.config(relief=RAISED)
        
        self.Eightc_button.config(relief=RAISED)
        self.Eightd_button.config(relief=RAISED)
        self.Eighth_button.config(relief=RAISED)
        self.Eights_button.config(relief=RAISED)
        
        self.Sevenc_button.config(relief=RAISED)
        self.Sevend_button.config(relief=RAISED)
        self.Sevenh_button.config(relief=RAISED)
        self.Sevens_button.config(relief=RAISED)
        
        self.Sixc_button.config(relief=RAISED)
        self.Sixd_button.config(relief=RAISED)
        self.Sixh_button.config(relief=RAISED)
        self.Sixs_button.config(relief=RAISED)
        
        self.p1hand.set("")
        self.p2hand.set("")
        self.board_cards.set("")
        self.v.set(1)
    
    def Ac_click(self):
        state = str(self.Ac_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Ac")
            self.v.set(2)
          else:
            self.p1hand.set("Ac")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Ac")
            self.v.set(3)
          else:
            self.p2hand.set("Ac")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Ac")
          else:
            self.board_cards.set("Ac")
        
        self.Ac_button.config(relief=SUNKEN)
        
    def Ad_click(self):
        state = str(self.Ad_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Ad")
            self.v.set(2)
          else:
            self.p1hand.set("Ad")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Ad")
            self.v.set(3)
          else:
            self.p2hand.set("Ad")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Ad")
          else:
            self.board_cards.set("Ad")
        
        self.Ad_button.config(relief=SUNKEN)
        
    def Ah_click(self):
        state = str(self.Ah_button['relief'])
        if(state == 'sunken'):
          return
  
        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Ah")
            self.v.set(2)
          else:
            self.p1hand.set("Ah")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Ah")
            self.v.set(3)
          else:
            self.p2hand.set("Ah")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Ah")
          else:
            self.board_cards.set("Ah")
        
        self.Ah_button.config(relief=SUNKEN)
      
    def As_click(self):
        state = str(self.As_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " As")
            self.v.set(2)
          else:
            self.p1hand.set("As")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " As")
            self.v.set(3)
          else:
            self.p2hand.set("As")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " As")
          else:
            self.board_cards.set("As")
        
        self.As_button.config(relief=SUNKEN)
        
    def Kc_click(self):
        state = str(self.Kc_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Kc")
            self.v.set(2)
          else:
            self.p1hand.set("Kc")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Kc")
            self.v.set(3)
          else:
            self.p2hand.set("Kc")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Kc")
          else:
            self.board_cards.set("Kc")
        
        self.Kc_button.config(relief=SUNKEN)
        
    def Kd_click(self):
        state = str(self.Kd_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Kd")
            self.v.set(2)
          else:
            self.p1hand.set("Kd")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Kd")
            self.v.set(3)
          else:
            self.p2hand.set("Kd")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Kd")
          else:
            self.board_cards.set("Kd")
        
        self.Kd_button.config(relief=SUNKEN)
        
    def Kh_click(self):
        state = str(self.Kh_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Kh")
            self.v.set(2)
          else:
            self.p1hand.set("Kh")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Kh")
            self.v.set(3)
          else:
            self.p2hand.set("Kh")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Kh")
          else:
            self.board_cards.set("Kh")
        
        self.Kh_button.config(relief=SUNKEN)
        
    def Ks_click(self):
        state = str(self.Ks_button['relief'])
        if(state == 'sunken'):
          return
  
        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Ks")
            self.v.set(2)
          else:
            self.p1hand.set("Ks")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Ks")
            self.v.set(3)
          else:
            self.p2hand.set("Ks")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Ks")
          else:
            self.board_cards.set("Ks")
        
        self.Ks_button.config(relief=SUNKEN)
      
    def Qc_click(self):
        state = str(self.Qc_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Qc")
            self.v.set(2)
          else:
            self.p1hand.set("Qc")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Qc")
            self.v.set(3)
          else:
            self.p2hand.set("Qc")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Qc")
          else:
            self.board_cards.set("Qc")
        
        self.Qc_button.config(relief=SUNKEN)
        
    def Qd_click(self):
        state = str(self.Qd_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Qd")
            self.v.set(2)
          else:
            self.p1hand.set("Qd")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Qd")
            self.v.set(3)
          else:
            self.p2hand.set("Qd")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Qd")
          else:
            self.board_cards.set("Qd")
        
        self.Qd_button.config(relief=SUNKEN)
        
    def Qh_click(self):
        state = str(self.Qh_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Qh")
            self.v.set(2)
          else:
            self.p1hand.set("Qh")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Qh")
            self.v.set(3)
          else:
            self.p2hand.set("Qh")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Qh")
          else:
            self.board_cards.set("Qh")
        
        self.Qh_button.config(relief=SUNKEN)
        
    def Qs_click(self):
        state = str(self.Qs_button['relief'])
        if(state == 'sunken'):
          return
 
        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Qs")
            self.v.set(2)
          else:
            self.p1hand.set("Qs")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Qs")
            self.v.set(3)
          else:
            self.p2hand.set("Qs")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Qs")
          else:
            self.board_cards.set("Qs")
        
        self.Qs_button.config(relief=SUNKEN)
       
    def Jc_click(self):
        state = str(self.Jc_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Jc")
            self.v.set(2)
          else:
            self.p1hand.set("Jc")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Jc")
            self.v.set(3)
          else:
            self.p2hand.set("Jc")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Jc")
          else:
            self.board_cards.set("Jc")
        
        self.Jc_button.config(relief=SUNKEN)
                    
    def Jd_click(self):
        state = str(self.Jd_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Jd")
            self.v.set(2)
          else:
            self.p1hand.set("Jd")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Jd")
            self.v.set(3)
          else:
            self.p2hand.set("Jd")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Jd")
          else:
            self.board_cards.set("Jd")
        
        self.Jd_button.config(relief=SUNKEN)
        
    def Jh_click(self):
        state = str(self.Jh_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Jh")
            self.v.set(2)
          else:
            self.p1hand.set("Jh")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Jh")
            self.v.set(3)
          else:
            self.p2hand.set("Jh")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Jh")
          else:
            self.board_cards.set("Jh")
        
        self.Jh_button.config(relief=SUNKEN)
        
    def Js_click(self):
        state = str(self.Js_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Js")
            self.v.set(2)
          else:
            self.p1hand.set("Js")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Js")
            self.v.set(3)
          else:
            self.p2hand.set("Js")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Js")
          else:
            self.board_cards.set("Js")
        
        self.Js_button.config(relief=SUNKEN)
                    
    def Tc_click(self):
        state = str(self.Tc_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Tc")
            self.v.set(2)
          else:
            self.p1hand.set("Tc")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Tc")
            self.v.set(3)
          else:
            self.p2hand.set("Tc")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Tc")
          else:
            self.board_cards.set("Tc")
        
        self.Tc_button.config(relief=SUNKEN)
                    
    def Td_click(self):
        state = str(self.Td_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Td")
            self.v.set(2)
          else:
            self.p1hand.set("Td")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Td")
            self.v.set(3)
          else:
            self.p2hand.set("Td")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Td")
          else:
            self.board_cards.set("Td")
        
        self.Td_button.config(relief=SUNKEN)
        
    def Th_click(self):
        state = str(self.Th_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Th")
            self.v.set(2)
          else:
            self.p1hand.set("Th")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Th")
            self.v.set(3)
          else:
            self.p2hand.set("Th")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Th")
          else:
            self.board_cards.set("Th")
        
        self.Th_button.config(relief=SUNKEN)
        
    def Ts_click(self):
        state = str(self.Ts_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " Ts")
            self.v.set(2)
          else:
            self.p1hand.set("Ts")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " Ts")
            self.v.set(3)
          else:
            self.p2hand.set("Ts")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " Ts")
          else:
            self.board_cards.set("Ts")
        
        self.Ts_button.config(relief=SUNKEN)
        
    def Ninec_click(self):
        state = str(self.Ninec_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 9c")
            self.v.set(2)
          else:
            self.p1hand.set("9c")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 9c")
            self.v.set(3)
          else:
            self.p2hand.set("9c")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 9c")
          else:
            self.board_cards.set("9c")
        
        self.Ninec_button.config(relief=SUNKEN)
        
    def Nined_click(self):
        state = str(self.Nined_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 9d")
            self.v.set(2)
          else:
            self.p1hand.set("9d")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 9d")
            self.v.set(3)
          else:
            self.p2hand.set("9d")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 9d")
          else:
            self.board_cards.set("9d")
        
        self.Nined_button.config(relief=SUNKEN)
        
    def Nineh_click(self):
        state = str(self.Nineh_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 9h")
            self.v.set(2)
          else:
            self.p1hand.set("9h")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 9h")
            self.v.set(3)
          else:
            self.p2hand.set("9h")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 9h")
          else:
            self.board_cards.set("9h")
        
        self.Nineh_button.config(relief=SUNKEN)
        
    def Nines_click(self):
        state = str(self.Nines_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 9s")
            self.v.set(2)
          else:
            self.p1hand.set("9s")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 9s")
            self.v.set(3)
          else:
            self.p2hand.set("9s")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 9s")
          else:
            self.board_cards.set("9s")
        
        self.Nines_button.config(relief=SUNKEN)
        
    def Eightc_click(self):
        state = str(self.Eightc_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 8c")
            self.v.set(2)
          else:
            self.p1hand.set("8c")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 8c")
            self.v.set(3)
          else:
            self.p2hand.set("8c")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 8c")
          else:
            self.board_cards.set("8c")
        
        self.Eightc_button.config(relief=SUNKEN)
        
    def Eightd_click(self):
        state = str(self.Eightd_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 8d")
            self.v.set(2)
          else:
            self.p1hand.set("8d")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 8d")
            self.v.set(3)
          else:
            self.p2hand.set("8d")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 8d")
          else:
            self.board_cards.set("8d")
        
        self.Eightd_button.config(relief=SUNKEN)
        
    def Eighth_click(self):
        state = str(self.Eighth_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 8h")
            self.v.set(2)
          else:
            self.p1hand.set("8h")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 8h")
            self.v.set(3)
          else:
            self.p2hand.set("8h")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 8h")
          else:
            self.board_cards.set("8h")
        
        self.Eighth_button.config(relief=SUNKEN)
        
    def Eights_click(self):
        state = str(self.Eights_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 8s")
            self.v.set(2)
          else:
            self.p1hand.set("8s")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 8s")
            self.v.set(3)
          else:
            self.p2hand.set("8s")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 8s")
          else:
            self.board_cards.set("8s")
        
        self.Eights_button.config(relief=SUNKEN)
        
    def Sevenc_click(self):
        state = str(self.Sevenc_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 7c")
            self.v.set(2)
          else:
            self.p1hand.set("7c")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 7c")
            self.v.set(3)
          else:
            self.p2hand.set("7c")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 7c")
          else:
            self.board_cards.set("7c")
        
        self.Sevenc_button.config(relief=SUNKEN)
        
    def Sevend_click(self):
        state = str(self.Sevend_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 7d")
            self.v.set(2)
          else:
            self.p1hand.set("7d")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 7d")
            self.v.set(3)
          else:
            self.p2hand.set("7d")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 7d")
          else:
            self.board_cards.set("7d")
        
        self.Sevend_button.config(relief=SUNKEN)
        
    def Sevenh_click(self):
        state = str(self.Sevenh_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 7h")
            self.v.set(2)
          else:
            self.p1hand.set("7h")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 7h")
            self.v.set(3)
          else:
            self.p2hand.set("7h")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 7h")
          else:
            self.board_cards.set("7h")
        
        self.Sevenh_button.config(relief=SUNKEN)
        
    def Sevens_click(self):
        state = str(self.Sevens_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 7s")
            self.v.set(2)
          else:
            self.p1hand.set("7s")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 7s")
            self.v.set(3)
          else:
            self.p2hand.set("7s")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 7s")
          else:
            self.board_cards.set("7s")
        
        self.Sevens_button.config(relief=SUNKEN)
        
    def Sixc_click(self):
        state = str(self.Sixc_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 6c")
            self.v.set(2)
          else:
            self.p1hand.set("6c")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 6c")
            self.v.set(3)
          else:
            self.p2hand.set("6c")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 6c")
          else:
            self.board_cards.set("6c")
        
        self.Sixc_button.config(relief=SUNKEN)
        
    def Sixd_click(self):
        state = str(self.Sixd_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 6d")
            self.v.set(2)
          else:
            self.p1hand.set("6d")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 6d")
            self.v.set(3)
          else:
            self.p2hand.set("6d")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 6d")
          else:
            self.board_cards.set("6d")
        
        self.Sixd_button.config(relief=SUNKEN)
        
    def Sixh_click(self):
        state = str(self.Sixh_button['relief'])
        if(state == 'sunken'):
          return

        if(self.v.get() == 1):
          if(len(self.p1hand.get()) == 5):
            return
          elif(len(self.p1hand.get()) == 2):
            self.p1hand.set(str(self.p1hand.get()) + " 6h")
            self.v.set(2)
          else:
            self.p1hand.set("6h")
        elif(self.v.get() == 2):
          if(len(self.p2hand.get()) == 5):
            return
          elif(len(self.p2hand.get()) == 2):
            self.p2hand.set(str(self.p2hand.get()) + " 6h")
            self.v.set(3)
          else:
            self.p2hand.set("6h")
        else:
          boardlen = len(self.board_cards.get())
          if(boardlen >= 11):
            return
          elif(boardlen > 0):
            self.board_cards.set(self.board_cards.get() + " 6h")
          else:
            self.board_cards.set("6h")
        
        self.Sixh_button.config(relief=SUNKEN)
                    
    def Sixs_click(self):
      state = str(self.Sixs_button['relief'])
      if(state == 'sunken'):
        return

      if(self.v.get() == 1):
        if(len(self.p1hand.get()) == 5):
          return
        elif(len(self.p1hand.get()) == 2):
          self.p1hand.set(str(self.p1hand.get()) + " 6s")
          self.v.set(2)
        else:
          self.p1hand.set("6s")
      elif(self.v.get() == 2):
        if(len(self.p2hand.get()) == 5):
          return
        elif(len(self.p2hand.get()) == 2):
          self.p2hand.set(str(self.p2hand.get()) + " 6s")
          self.v.set(3)
        else:
          self.p2hand.set("6s")
      else:
        boardlen = len(self.board_cards.get())
        if(boardlen >= 11):
          return
        elif(boardlen > 0):
          self.board_cards.set(self.board_cards.get() + " 6s")
        else:
          self.board_cards.set("6s")
        
        self.Sixs_button.config(relief=SUNKEN)

def main():
    #hole_cards, num, exact, board, file_name = holdem_argparser.parse_args()
    #run(hole_cards, num, exact, board, file_name, True)
    top = tkinter.Tk()
    calc_gui = calcGUI(top)
    top.mainloop()

def calculate(board, exact, num, input_file, hole_cards, verbose):
    args = holdem_argparser.LibArgs(board, exact, num, input_file, hole_cards)
    hole_cards, n, e, board, filename = holdem_argparser.parse_lib_args(args)
    return run(hole_cards, n, e, board, filename, verbose)

def run(hole_cards, num, exact, board, file_name, verbose):
    if file_name:
        input_file = open(file_name, 'r')
        for line in input_file:
            if line is not None and len(line.strip()) == 0:
                continue
            hole_cards, board = holdem_argparser.parse_file_args(line)
            deck = holdem_functions.generate_deck(hole_cards, board)
            run_simulation(hole_cards, num, exact, board, deck, verbose)
            print ("-----------------------------------")
        input_file.close()
    else:
        deck = holdem_functions.generate_deck(hole_cards, board)
        return run_simulation(hole_cards, num, exact, board, deck, verbose)

def run_simulation(hole_cards, num, exact, given_board, deck, verbose):
    num_players = len(hole_cards)
    # Choose whether we're running a Monte Carlo or exhaustive simulation
    board_length = 0 if given_board is None else len(given_board)
    # Create data structures to manage multiple processes:
    # 1) winner_list: number of times each player wins a hand
    # 2) result_histograms: a list for each player that shows the number of
    #    times each type of poker hand (e.g. flush, straight) was gotten
    num_processes = multiprocessing.cpu_count()
    num_poker_hands = len(holdem_functions.hand_rankings)
    num_histograms = num_processes * num_players * num_poker_hands
    winner_list = multiprocessing.Array('i', num_processes * (num_players + 1))
    result_histograms = multiprocessing.Array('i', num_histograms)
    # When a board is given, exact calculation is much faster than Monte Carlo
    # simulation, so default to exact if a board is given
    if exact or given_board is not None:
        generate_boards = holdem_functions.generate_exhaustive_boards
    else:
        generate_boards = holdem_functions.generate_random_boards
    if (None, None) in hole_cards:
        hole_cards_list = list(hole_cards)
        unknown_index = hole_cards.index((None, None))
        deck_list = list(deck)
        pool = multiprocessing.Pool(processes=num_processes,
                                    initializer=unknown_simulation_init,
                                    initargs=(hole_cards_list, unknown_index,
                                              deck_list, generate_boards,
                                              num, board_length, given_board,
                                              winner_list, result_histograms))
        pool.map(unknown_simulation, holdem_functions.generate_hole_cards(deck))
    else:
        find_winner(generate_boards, deck, hole_cards, num, board_length,
                    given_board, winner_list, result_histograms)
    # Go through each parallel data structure and aggregate results
    combined_winner_list, combined_histograms = [0] * (num_players + 1), []
    for _ in range(num_players):
        combined_histograms.append([0] * len(holdem_functions.hand_rankings))
    for index, element in enumerate(winner_list):
        combined_winner_list[index % (num_players + 1)] += element
    for index, element in enumerate(result_histograms):
        combined_histograms[int((index / num_poker_hands) % num_players)][int((index % num_poker_hands))] += element
    if verbose:
        holdem_functions.print_results(hole_cards, combined_winner_list,
                                       combined_histograms)
    return holdem_functions.find_winning_percentage(combined_winner_list)

def unknown_simulation_init(hole_cards_list, unknown_index, deck_list,
                            generate_boards, num, board_length, given_board,
                            combined_winner_list, combined_result_histograms):
    unknown_simulation.hole_cards_list = hole_cards_list
    unknown_simulation.unknown_index = unknown_index
    unknown_simulation.deck = deck_list
    unknown_simulation.generate_boards = generate_boards
    unknown_simulation.num = num
    unknown_simulation.board_length = board_length
    unknown_simulation.given_board = given_board
    unknown_simulation.combined_winner_list = combined_winner_list
    unknown_simulation.combined_result_histograms = combined_result_histograms

def unknown_simulation(new_hole_cards):
    # Extract parameters
    hole_cards_list = unknown_simulation.hole_cards_list
    unknown_index = unknown_simulation.unknown_index
    deck = unknown_simulation.deck[:]
    generate_boards = unknown_simulation.generate_boards
    num = unknown_simulation.num
    board_length = unknown_simulation.board_length
    given_board = unknown_simulation.given_board
    combined_winner_list = unknown_simulation.combined_winner_list
    combined_result_histograms = unknown_simulation.combined_result_histograms
    # Set simulation variables
    num_players = len(hole_cards_list)
    result_histograms, winner_list = [], [0] * (num_players + 1)
    for _ in range(num_players):
        result_histograms.append([0] * len(holdem_functions.hand_rankings))
    hole_cards_list[unknown_index] = new_hole_cards
    deck.remove(new_hole_cards[0])
    deck.remove(new_hole_cards[1])
    # Find winner
    holdem_functions.find_winner(generate_boards, deck, tuple(hole_cards_list),
                                 num, board_length, given_board, winner_list,
                                 result_histograms)
    # Write results to parallel data structure for future tabulation
    proc_name = multiprocessing.current_process().name
    proc_id = int(proc_name.split("-")[-1]) % multiprocessing.cpu_count()
    for index, result in enumerate(winner_list):
        combined_winner_list[proc_id * (num_players + 1) + index] += result
    for histogram_index, histogram in enumerate(result_histograms):
        for index, result in enumerate(histogram):
            combined_result_histograms[len(holdem_functions.hand_rankings) *
                                       (proc_id * num_players + histogram_index)
                                       + index] += result

def find_winner(generate_boards, deck, hole_cards, num, board_length,
                given_board, winner_list, result_histograms):
    num_processes = multiprocessing.cpu_count()
    # Create threadpool and use it to perform hand detection over all boards
    pool = multiprocessing.Pool(processes=num_processes,
                                initializer=simulation_init,
                                initargs=(given_board, hole_cards, winner_list,
                                          result_histograms))
    pool.map(simulation, generate_boards(deck, num, board_length))

# Initialize shared variables for simulation
def simulation_init(given_board, hole_cards, winner_list, result_histograms):
    simulation.given_board = given_board
    simulation.hole_cards = hole_cards
    simulation.winner_list = winner_list
    simulation.result_histograms = result_histograms

# Separated function for each thread to execute while running
def simulation(remaining_board):
    # Extract variables shared through inheritance
    given_board, hole_cards = simulation.given_board, simulation.hole_cards
    winner_list = simulation.winner_list
    result_histograms = simulation.result_histograms
    # Generate a new board
    if given_board:
        board = given_board[:]
        board.extend(remaining_board)
    else:
        board = remaining_board
    num_players = len(hole_cards)
    # Extract process id from the name of the current process
    # Names are of the format: PoolWorker-1 - PoolWorker-n
    proc_name = multiprocessing.current_process().name
    proc_id = int(proc_name.split("-")[-1]) % multiprocessing.cpu_count()
    # Create results data structure which tracks results of comparisons
    result_list = []
    for _ in range(num_players):
        result_list.append([])
    # Find the best possible poker hand given the created board and the
    # hole cards and save them in the results data structures
    suit_histogram, histogram, max_suit = (
        holdem_functions.preprocess_board(board))
    for index, hole_card in enumerate(hole_cards):
        result_list[index] = (
            holdem_functions.detect_hand(hole_card, board, suit_histogram,
                                         histogram, max_suit))
    # Find the winner of the hand and tabulate results
    winner_index = holdem_functions.compare_hands(result_list)
    winner_list[proc_id * (num_players + 1) + winner_index] += 1
    # Increment what hand each player made
    for index, result in enumerate(result_list):
        result_histograms[len(holdem_functions.hand_rankings) *
                          (proc_id * num_players + index) + result[0]] += 1

if __name__ == '__main__':
    start = time.time()
    main()
    print ("\nTime elapsed(seconds): ", time.time() - start)
