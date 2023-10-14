# CY Tech - Traitement du signal

Dépôt pour notre projet pour le cours de "Traitement du Signal" de CY Tech. 

Auteurs : Aïcha Lehbib, Ahmed Ouinekh, Charles-Meldhine Madi Mnemoi, Jalis Aït-Ouakli, Youssef Saïdi

# Configuration de l'environnement de développment

## Aparté pour les utilisateurs Windows

**Version courte :** Ouvrez un terminal (`Windows + R` puis tapez `cmd`), installez Ubuntu avec `wsl --install -d Ubuntu`. 

Puis, dans Ubuntu, installez `make` avec `sudo apt install make -y`.

<details>
  <summary>Version longue</summary>
Si vous utilisez Windows, commencez par installer Ubuntu à travers WSL2.

Cela vous permettra d'utiliser les commandes et outils Linux (ce qui va grandement faciliter l'installation) tout en continuant à utiliser Windows (et avec quasiment aucune perte de performance comparée à l'utilisation d'une machine virtuelle).

WSL2 devrait déjà être installé sur les PC CY Tech. Pour vous en assurer, lancez un terminal et tapez `wsl --list`. 

Si la commande renvoie une erreur, suivez les instructions sur https://docs.microsoft.com/fr-fr/windows/wsl/install pour installer WSL2.

Sinon, installez Ubuntu avec `wsl --install -d Ubuntu` puis définissez votre nom d'utilisateur et votre mot de passe.

Enfin, installez `make` dans Ubuntu : `sudo apt install make -y`
</details>

## Cloner ce dépôt Git

Si ce n'est pas encore fait, configurez vos comptes Git et GitHub.

- Générez une clé SSH : 
  - `ssh-keygen -t ed25519 -C "Clé SSH pour le dépôt cytech_spaks (https://github.com/cmnemoi/cytech_sparks)"`
  - Appuyez sur `Entrée` jusqu'à que la clé soit générée
- Ajoutez la clé SSH à votre agent SSH : `eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519`
- Affichez la clé SSH générée : `cat ~/.ssh/id_ed25519.pub` et copiez-la 
- Ajoutez la clé SSH à votre compte GitHub :
  - Tutoriel : https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
  - Lien direct : https://github.com/settings/ssh/new

Puis clonez ce dépôt Git : `git clone git@github.com:cmnemoi/cytech_sparks.git && cd cytech_sparks` (entrez `yes` si on vous demande de confirmer l'ajout de la clé SSH à la liste des clés connues)

**Les utilisteurs de WSL2 sous Windows doivent absolument cloner le dépôt *dans* WSL2 et non dans leurs dossiers Windows !**

Sinon tout sera extrêmement lent. Vous pouvez utiliser la fonction [WSL Remote](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) de VSCode pour travailler efficacement.

## Lancer les scripts d'installation

Installez l'application en tapant `make` dans le terminal. Si tout va bien elle devrait se lancer automatiquement.

Vous pouvez y accéder à l'adresse http://localhost:8501/ dans votre navigateur.

Vous êtes prêts à travailler !
