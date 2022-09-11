#guru
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import tkinter as tk
from tkinter import *
import time
import os
import threading
from redirection_stdout import StdoutTkinter
import smtplib
from string import Template


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
current_resultRvote= 15

def starter():
    """ Commence la mainloop de Tkinter ici """
    app = StdoutTkinter()
    app.mainloop()
 
## Commence la Boucle de Tkinter, pour lire le stdout
thread = threading.Thread(target=starter)
thread.start()
 
#Paramètres fenetre TK
master = tk.Tk()
master.title("Authentification Gurushots")
master.minsize(380, 250)
master.maxsize(180, 180)
master.config(background="black")
master.wm_attributes("-topmost", 1)

#Ferme la fenetre TK et poursuivre le programme
def destroy():
    master.destroy()
#Stockage du login dans current_resultR1
def returnEntryR1(arg=None):
    global current_resultR1
    result = myEntryR1.get()
    current_resultR1 = result
    print("✔ Login validé")
    myEntryR1.delete(0,END)
#Stockage du password dans current_resultR2
def returnEntryR2(arg=None):
    global current_resultR2
    result = myEntryR2.get()
    current_resultR2 = result
    print("✔ Mot de passe validé")
    myEntryR2.delete(0,END)
#Stockage du nombre de votes souhaités
def returnEntryRvote(arg=None):
    global current_resultRvote
    result = myEntryRvote.get()
    current_resultRvote = result
    print("Vous avez choisi "+current_resultRvote+" votes par concours.")
    myEntryRvote.delete(0,END)

########################################################################################################################
#Texte LOGIN
label_titleR1 = Label(master, text="Login/Email Gurushots", font="Courrier, 8", bg="black", fg='white')
label_titleR1.pack()
# Zone de saisie LOGIN
myEntryR1 = Entry(master, width=20)
myEntryR1.focus()
myEntryR1.bind("<Return>",returnEntryR1, )
myEntryR1.pack()
# Bouton valider Login
enterEntryR1 = Button(master, text= "Valider", command=returnEntryR1)
enterEntryR1.pack(fill=X)

 #Texte Password
label_titleR2 = Label(master, text="Mot de passe Gurushots", font="Courrier, 8", bg="black", fg='white')
label_titleR2.pack()
# Zone de saisie Password
myEntryR2 = Entry(master, width=20)
myEntryR2.focus()
myEntryR2.bind("<Return>",returnEntryR2)
myEntryR2.pack()
# Bouton valider  Password
enterEntryR2 = Button(master, text= "Valider", command=returnEntryR2)
enterEntryR2.pack(fill=X)

 #Texte nombre de Votes
label_titleRvote = Label(master, text="Nombre de votes par concours", font="Courrier, 8", bg="black", fg='white')
label_titleRvote.pack()
# Zone de saisie nb votes
myEntryRvote = Entry(master, width=20)
myEntryRvote.focus()
myEntryRvote.bind("<Return>",returnEntryRvote)
myEntryRvote.pack()
# Bouton valider nb de votes
enterEntryRvote = Button(master, text= "Valider", command=returnEntryRvote)
enterEntryRvote.pack(fill=X)

 #Texte supplémentaire
label_titleR3 = Label(master, text="Appuyez sur les  boutons 'Valider' avant de lancer le programme", font="Courrier, 8", bg="black", fg='white')
label_titleR3.pack()

# Bouton Lancement programme
enterEntryR2 = Button(master, text= "Lancer le programme", command=destroy)
enterEntryR2.pack(fill=X)
master.mainloop()
########################################################################################################################


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def removestartpop():
    try:
        element = driver.find_element_by_class_name('icon-right-arrow')
        print(' ', end='\r')
        print ("✔ Fermeture d'un Popup x1")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        element = driver.find_element_by_class_name('c-modal-broadcast--closed__close-btn')
        print ("✔ Fermeture d'un Popup x2")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_class_name('demo__close')
        print ("✔ Fermeture d'un Popup x3")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_class_name('icon-right-arrow')
        print ("✔ Fermeture d'un Popup x4")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        element = driver.find_element_by_class_name('c-modal-broadcast--closed__close-btn')
        print ("✔ Fermeture d'un Popup x5")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        voteur()
    except Exception:
        pass
        voteur()

username = (current_resultR1)
password = (current_resultR2)
photovar2 = "#vote-photo-"
modal = "modal-vote__greeting"

# Si vous placer le driver.exe dans un dossier "driver" décommenter ci-dessous et commenter celle d'après.
# driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'),options=chrome_options)
driver = webdriver.Chrome(('C:/Gurushots/driver/chromedriver.exe'),options=chrome_options)
driver.maximize_window()
driver.get("https://Gurushots.com/challenges/my-challenges/current")
time.sleep(1)
element = driver.find_element_by_link_text("SIGN IN")
my_str1 =(element.get_attribute('class'))
idchanged = my_str1[:-1]
print("ID  : "+idchanged)
loginid =(idchanged+"h")
time.sleep(1)
print('Connexion en cours')
element = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.CLASS_NAME, str(loginid)))
)
element.click()
time.sleep(1)
element = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.NAME, "email"))
)
element.send_keys(username)
element = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.NAME, "password"))
)
element.send_keys(password)
element = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.CLASS_NAME, "modal-login__submit"))
)
element.click()
print('✔ Connexion validée')
time.sleep(4)

def voteur():
    try:
        numeros_concours = 0
        element = driver.find_element_by_css_selector("[ui-view='header']")
        my_str1 =(element.get_attribute('class'))
        idchanged = my_str1[:-1]
        loginidv =(idchanged+"v")
        loginidw =(idchanged+"w")
        meci = driver.find_elements_by_class_name('icon-voting')
        count = len(meci)
        time.sleep(3)
        for items in meci:   
                photovar = 0
                driver.find_elements_by_class_name('icon-voting')[numeros_concours].click()
                findtext =driver.find_element_by_xpath("//div[@class='modal-vote__challenge-title']").text
                print('N°' +str(numeros_concours+1)+'/'+str(count)+ ' ' +(findtext))
                time.sleep(1)
                numeros_concours += 1
                try: 
                    element = WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.CLASS_NAME, (modal)))
                    )
                    element.click()
                    print("<", end='\r')
                    for _ in " "*int(current_resultRvote):
                        photovar += 1
                        element = WebDriverWait(driver, 6).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, photovar2+str(photovar))) 
                        )
                        element.click()
                        print("✔", end='\r')
                    print(">")
                    element = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, str(loginidv)))
                    )
                    element.click()
                    element = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, str(loginidw)))
                    )
                    element.click()
                except:
                    driver.get("https://Gurushots.com/challenges/my-challenges/current")
                    print('>', end='\r')
                    print('\n  ⚠ Impossible de voter, passage au concours suivant ⚠ ')
                    time.sleep(8)
    except:
        numeros_concours = 0
        print(' ', end='\r')
        print(' ☑ Votes terminés, redémarrage à Zéro des votes Gurushots ☑')
        driver.get("https://Gurushots.com/challenges/my-challenges/current")
        time.sleep(8)
        removestartpop()
while True:
    try:
        removestartpop()
    except Exception:
        pass
        removestartpop()

thread.join()