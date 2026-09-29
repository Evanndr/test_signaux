#!/usr/bin/python3
import signal as sig
import time
import sys
import os
import random
import subprocess

pid = os.getpid()
print("pid=", pid)


print("Attente d'un Joueur...")
pid_adversaire = None

while not pid_adversaire:
	# Récupère les PIDs exécutant ce script via pgrep (Attention y'a un conflit avec plumz)
	resultat = subprocess.run(["pgrep", "-f", os.path.basename(__file__)], capture_output=True, text=True)
		
	# Transforme la chaîne reçue en liste de PIDs
	tous_les_pids = resultat.stdout.split()
		
	# Filtre pour ne garder que le PID qui n'est pas le nôtre
	pids_adversaires = [p for p in tous_les_pids if int(p) != pid]

	if pids_adversaires:
		# On a trouvé l'autre joueur
		pid_adversaire = int(pids_adversaires[0])
	else:
		# On est tout seul, on attend 1 seconde avant de revérifier
		time.sleep(1)


def synchroniser():
	#Attend que les millisecondes passent à 000 (début de la seconde suivante).
	t_actuel = time.time()
	# Calcule le temps restant jusqu'à la prochaine seconde entière
	temps_attente = 1.0 - (t_actuel % 1.0) #Le modulo (c'est le %) isole les milisecondes
	time.sleep(temps_attente)

victoire = 0
égalité = 0
défaite = 0


def pierre(s, frame):
	global victoire, égalité, défaite, choix # Global permet d'utiliser des variables définies en dehors de la fonction
	if choix == 0:
		défaite += 1
		print(f"Adversaire joue Pierre, je joue Ciseaux. Perdu\n {victoire} Victoires  {égalité} Egalités  {défaite} Défaites")
	if choix == 1:
		égalité +=1
		print(f"Adversaire joue Pierre, je joue Pierre. Egalité\n {victoire} Victoires  {égalité} Egalités  {défaite} Défaites")
	if choix == 2:
		victoire +=1
		print(f"Adversaire joue Pierre, je joue Feuille. Gagné\n {victoire} Victoires  {égalité} Egalités  {défaite} Défaites")


def feuille(s, frame):
	global victoire, égalité, défaite, choix # Global permet d'utiliser des variables définies en dehors de la fonction
	if choix == 0:
		victoire += 1
		print(f"Adversaire joue Feuille, je joue Ciseaux. Gagné\n {victoire} Victoires  {égalité} Egalités  {défaite} Défaites")
	if choix == 1:
		défaite +=1
		print(f"Adversaire joue Feuille, je joue Pierre. Perdu\n {victoire} Victoires  {égalité} Egalités  {défaite} Défaites")
	if choix == 2:
		égalité +=1
		print(f"Adversaire joue Feuille, je joue Feuille. Egalité\n {victoire} Victoires  {égalité} Egalités  {défaite} Défaites")


def ciseaux(s, frame):
	global victoire, égalité, défaite, choix # Global permet d'utiliser des variables définies en dehors de la fonction
	if choix == 0:
		égalité += 1
		print(f"Adversaire joue Ciseaux, je joue Ciseaux. Egalité\n {victoire} Victoires  {égalité} Egalités  {défaite} Défaites")
	if choix == 1:
		victoire +=1
		print(f"Adversaire joue Ciseaux, je joue Pierre. Gagné\n {victoire} Victoires  {égalité} Egalités  {défaite} Défaites")
	if choix == 2:
		défaite +=1
		print(f"Adversaire joue Ciseaux, je joue Feuille. Perdu\n {victoire} Victoires  {égalité} Egalités  {défaite} Défaites")


sig.signal(sig.SIGUSR1, pierre) #Attend de recevoir un signal SIGUSR1, une fois recu on appelle la fonction pierre)
sig.signal(sig.SIGUSR2, feuille) #Attend de recevoir un signal SIGUSR2, une fois recu on appelle la fonction feuille)
sig.signal(sig.SIGALRM, ciseaux) #Attend de recevoir un signal SIGALRM, une fois recu on appelle la fonction ciseaux)

while True:
	choix = random.randint(0, 2)
	synchroniser()
	if choix == 0:
		os.kill(pid_adversaire, sig.SIGALRM)
	elif choix == 1:
		os.kill(pid_adversaire, sig.SIGUSR1)
	else:
		os.kill(pid_adversaire, sig.SIGUSR2)
	time.sleep(1)

