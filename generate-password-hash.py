#!/usr/bin/env python3
"""
Script pour générer des hash bcrypt pour Ralph LRS
Usage: python3 generate-password-hash.py "votre_mot_de_passe"
"""

import sys
import bcrypt

def generate_bcrypt_hash(password):
    """Génère un hash bcrypt pour le mot de passe donné"""
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate-password-hash.py 'votre_mot_de_passe'")
        sys.exit(1)
    
    password = sys.argv[1]
    hash_result = generate_bcrypt_hash(password)
    print(f"\nHash bcrypt généré :")
    print(hash_result)
    print("\nCopiez ce hash dans votre fichier auth.json")