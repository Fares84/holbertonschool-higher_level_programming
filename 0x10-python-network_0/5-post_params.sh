#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1" # d: option pour définir un paramètre de valeur-clé de corps
