#main.py
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

options = Options()
options.add_argument("--disable-notifications")

current_resultRvote= 20



def starter():
    """ Commence la mainloop de Tkinter ici """
    app = StdoutTkinter()
    app.mainloop()
 
## Commence la Boucle de Tkinter, pour lire le stdout
thread = threading.Thread(target=starter)
thread.start()
 


#Paramètres fenetre TK
master = tk.Tk()
master.title("Authentification gurushots")
master.minsize(380, 250)
master.maxsize(180, 180)
master.config(background="black")
master.wm_attributes("-topmost", 1)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

#Ferme la fenetre TK et poursuivre le programme
def destroy():
    master.destroy()

#Stockage du login dans current_resultR1
def returnEntryR1(arg=None):
    global current_resultR1
    result = myEntryR1.get()
    current_resultR1 = result
    print(current_resultR1)
    myEntryR1.delete(0,END)

#Stockage du password dans current_resultR2
def returnEntryR2(arg=None):
    global current_resultR2
    result = myEntryR2.get()
    current_resultR2 = result
    print(current_resultR2)
    myEntryR2.delete(0,END)

#Stockage du nombre de votes souhaités
def returnEntryRvote(arg=None):
    global current_resultRvote
    result = myEntryRvote.get()
    current_resultRvote = result
    print("Nombre de vote par concours: "+current_resultRvote)
    myEntryRvote.delete(0,END)



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



 #Texte Vote
label_titleRvote = Label(master, text="Nombre de votes par concours", font="Courrier, 8", bg="black", fg='white')
label_titleRvote.pack()

# Zone de saisie nb votes
myEntryRvote = Entry(master, width=20)
myEntryRvote.focus()
myEntryRvote.bind("<Return>",returnEntryRvote)
myEntryRvote.pack()


# Bouton valider  votes
enterEntryRvote = Button(master, text= "Valider", command=returnEntryRvote)
enterEntryRvote.pack(fill=X)


 #Texte Password
label_titleR3 = Label(master, text="Appuyez sur les  boutons 'Valider' avant de lancer le programme", font="Courrier, 8", bg="black", fg='white')
label_titleR3.pack()

# Bouton Lancement programme
enterEntryR2 = Button(master, text= "Lancer le programme", command=destroy)
enterEntryR2.pack(fill=X)

master.mainloop()




def removepop():
    try:
        #element = driver.find_element_by_css_selector("[ng-click='dialog.hide()']")
        element = driver.find_element_by_css_selector("[ng-click='dialog.abort()']")
        print (" Pop Pop à fermer !")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        print("Votes terminés !")
        # time.sleep(1)
        # element = WebDriverWait(driver, 2).until(
        #      EC.presence_of_element_located((By.LINK_TEXT, "CLOSE")) 
        # )
        # element.click()

        # print(" Fermeture POPUP !")
        # element = WebDriverWait(driver, 2).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "md-primary-md-confirm-button-md-button-md-ink-ripple-md-default-theme")) 
        # )
        # element.click()
        time.sleep(1)    
        print('Validation du concours N° '+ str(valeur1))
        time.sleep(2)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, str(loginidv)))
            #EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-click='$ctrl.submit()']")) 
        )
        element.click()
        print('Sortie du concours N° '+str(valeur1))
        print('_____________________________________________________')
        time.sleep(2)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, str(loginidw)))
            #EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-class='::$ctrl.mode === 'guru_top_pick' ? 'modal-vote__btn--blue' : 'jLhyvw'']")) 
        )
        element.click()
        time.sleep(2)
        moteur()
    except: 
        pass


#Fonction qui sert dans la page des votes, elle clique sur Let's Go et et lance le vote en cliquant sur les images, à la fin elle valide par 2 boutons



def voteur():
    time.sleep(3)
    print('Lancement du moteur ...')
    time.sleep(1)
    element = driver.find_element_by_class_name('modal-vote__greeting')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    print("Démarrage des votes pour le concours N° " + str(valeur1+1))
    photovar = 0
    # photovar2 = "vote-photo-"
    photovar2 = "#vote-photo-"
    for _ in " "*int(current_resultRvote):
        photovar += 1
        if photovar == 21:
            time.sleep(3)
        elif photovar == 31:
            time.sleep(3)
        elif photovar == 41:
            time.sleep(3)
        elif photovar == 51:
            time.sleep(3)
        elif photovar == 61:
            time.sleep(3)
        else:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, photovar2+str(photovar))) 
            )
            element.click()          
            print("O ", end='\r')
            # incrémentale sur la même ligne : print("Vote "+str(photovar)+"/"+str(current_resultRvote), end='\r')
    time.sleep(1)
    print("O ")
    print("Votes terminés !")




    # time.sleep(1)
    # element = WebDriverWait(driver, 2).until(
    #      EC.presence_of_element_located((By.LINK_TEXT, "CLOSE")) 
    # )
    # element.click()

    # print(" Fermeture POPUP !")
    # element = WebDriverWait(driver, 2).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "md-primary-md-confirm-button-md-button-md-ink-ripple-md-default-theme")) 
    # )
    # element.click()
    time.sleep(2)    
    print('Validation du concours N° '+ str(valeur1+1))
    time.sleep(2)
    element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, str(loginidv)))
            #EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-click='$ctrl.submit()']")) 
    )
    element.click()
    time.sleep(1)    
    print('Sortie du concours N° '+str(valeur1+1))
    print('_____________________________________________________')
    time.sleep(2)
    element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, str(loginidw)))
            #EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-class='::$ctrl.mode === 'guru_top_pick' ? 'modal-vote__btn--blue' : 'jLhyvw'']")) 
    )
    element.click()
    time.sleep(2)

###LOGIN###
#########################A SUPPRIMER #########################A SUPPRIMER #########################A SUPPRIMER #########################A SUPPRIMER
username = (current_resultR1)
password = (current_resultR2)
time.sleep(1)
#########################A SUPPRIMER #########################A SUPPRIMER #########################A SUPPRIMER
#chrome driver en local
driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'))
# PATH = "C:\Program Files\chromedriver\chromedriver.exe"
#Lance le driver Chrome par le PATH selectionné précédemment
# driver = webdriver.Chrome(PATH)
#Maximise la fenetre à tout l'écran
driver.maximize_window()
#Démarrage de la page Web Gurushots
driver.get("https://Gurushots.com/challenges/my-challenges/current")
time.sleep(1)
try:
    element = driver.find_element_by_link_text("SIGN IN")
    my_str1 =(element.get_attribute('class'))
    idchanged = my_str1[:-1]
    print("Détection de l'ID aléatoire de Gurushots : "+idchanged)
    loginid =(idchanged+"h")
    time.sleep(1)
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, str(loginid)))
    )
    element.click()
    print('Connexion en cours')

    time.sleep(1)
    element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "email"))
    )
    element.send_keys(username)
    print('Login OK')
    time.sleep(1)

    element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "password"))
    )
    element.send_keys(password)
    print('Password OK')
    time.sleep(1)   

    element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "modal-login__submit"))
    )
    element.click()
    print('Connexion validée')
    time.sleep(3)
    valeur1 = 0
    element = driver.find_element_by_css_selector("[ui-view='header']")
    my_str1 =(element.get_attribute('class'))
    idchanged = my_str1[:-1]
    loginidv =(idchanged+"v")
    loginidw =(idchanged+"w")
    time.sleep(1)
except:
        driver.quit()




#Remontter le nom du challenge actuel dans la boucle
def findtext():
        findtext =driver.find_element_by_xpath("//div[@class='modal-vote__greeting__text']").text
        print(findtext)


#Moteur , on verifie d'abord si il n'y a pas de POP up de fin de concours et ensuite on "pass" 
def moteur():
    try:
        global valeur1
        time.sleep(2)
# On cherche le nombre d'icone de vote clickable sur la page et on affiche le nombre, on stock le nombre dans count
        meci = driver.find_elements_by_class_name('icon-voting')
        time.sleep(1)
        count = len(meci)
        time.sleep(1)
        print('Il y a actuellement '+ str(count)+ '  concours Gurushots')
        time.sleep(1)
# Ensuite on creer une loop de vote pour chaque element de la loop on lance les votes avec voteur()   
        for items in meci:
                time.sleep(1)
                element = driver.find_element_by_css_selector("[ui-view='header']")
                my_str1 =(element.get_attribute('class'))
                idchanged = my_str1[:-1]
                time.sleep(2)
                print("Mise à jour ID Gurushots: "+idchanged)     
                element = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'icon-voting'))
            )
                time.sleep(1)
                driver.find_elements_by_class_name('icon-voting')[valeur1].click()
                time.sleep(1)

# On récuperer le nom du challenge qui s'affiche à l'écran pour le stocker dans findtext

                findtext =driver.find_element_by_xpath("//div[@class='modal-vote__challenge-title']").text
                print("=================================================")
#C'est valeur1+1 car cela commence à zero
                print('N°' +str(valeur1+1)+'/'+str(count)+ ' ' +(findtext))
                print("=================================================")
                voteur()
                time.sleep(1)
                valeur1 += 1
    except:
# Si exeption et que la valeur actuel est supérieur au nombre de challenge detectés, c'est que c'est terminé, alors on relance les vote et on remet à zero valeur1 
        if valeur1 > count:
            valeur1 = 0
            time.sleep(2)
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('Votes terminés, relancement de Gurushots')
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            driver.get("https://gurushots.com/challenges/my-challenges/current")
            time.sleep(6)
            moteur()

        else:
            valeur1 += 1
            removepop()
            element = driver.find_element_by_class_name('modal-vote__close')
            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
            print('Passage au concours suivant')
            print('_____________________________________________________')
            time.sleep(2)
            moteur()
# Enfin on finit toujours par relancer les votes quand la loop est terminée
    finally:
        valeur1 = 0
        time.sleep(2)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Votes terminés, redémarrage à Zéro des votes Gurushots')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        driver.get("https://Gurushots.com/challenges/my-challenges/current")
        time.sleep(6)
        moteur()

# Fermeture des pop up concours terminés
try:
    element = driver.find_element_by_class_name('icon-right-arrow')
    print ("Pop Pop Concours à fermer 1")
    time.sleep(1)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element = driver.find_element_by_class_name('c-modal-broadcast--closed__close-btn')
    print ("Pop Pop Concours à fermer 2")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    element = driver.find_element_by_class_name('demo__close')
    print ("Pop Pop Concours à fermer 3")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    element = driver.find_element_by_class_name('icon-right-arrow')
    print ("Pop Pop Concours à fermer 3")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    element = driver.find_element_by_class_name('c-modal-broadcast--closed__close-btn')
    print ("Pop Pop Concours à fermer 3")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    moteur()
    
except Exception:
    pass
    moteur()

 
thread.join()

