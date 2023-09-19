# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:45:22 2023

@author: cesar
"""

def modus_ponens(P, Q):
    """
    Implementación de Modus Ponens.
    
    Argumentos:
    P (bool): Premisa P
    Q (bool): Premisa Q
    
    Retorna:
    bool: El resultado de la conclusión basada en Modus Ponens
    """
    if P:
        if Q:
            return True
        else:
            print("Q es falso, Modus Ponens no se aplica.")
            return None
    else:
        print("P es falso, Modus Ponens no se aplica.")
        return None

# Ejemplo de uso
P = True
Q = True

print("Premisa P es verdadera.")
print("Premisa Q es verdadera.")
print("Aplicando Modus Ponens...")
resultado = modus_ponens(P, Q)

if resultado is not None:
    print("Conclusión: Q es verdadero por Modus Ponens.")
else:
    print("No se pudo aplicar Modus Ponens debido a premisas falsas.")
