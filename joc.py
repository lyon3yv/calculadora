historial = []

def calcular_numero_pensado(resultado_usuario):
    numero_secreto = (resultado_usuario - 6) / 2
    return int(numero_secreto)

def juego_truco_clasico():
    print("\n--- [1] EL MAG MATEMÀTIC (CLÀSSIC) ---")
    print("Segueix els passos mentalment o amb una calculadora.")
    input("1) Pensa un número enter qualsevol (Prem ENTER quan el tinguis)...")
    input("2) Multiplica'l per 3 (Prem ENTER)...")
    input("3) Al que ha quedat suma-li 14 (Prem ENTER)...")
    input("4) Al resultat suma-li el número que havies pensat al principi (Prem ENTER)...")
    input("5) Al que ha quedat resta-li 2 (Prem ENTER)...")
    input("6) El resultat divideix-lo entre 4 (Prem ENTER)...")
    
    final = int(input("-> Escriu quin número t'ha quedat ara mateix: "))
    adivinado = final - 3
    
    print("\n=========================================")
    print("✨ EL NÚMERO QUE HAVIES PENSAT ÉS EL:", adivinado, "✨")
    print("=========================================")
    
    historial.append("Truc Clàssic -> Número endevinat: " + str(adivinado))

def juego_adivino_tu_mente():
    print("\n--- [2] LECTOR DE MENTS ALGEBRAIC ---")
    print("Fes aquestes operacions ràpides de cap:")
    input("• Pensa un número secret (Prem ENTER)...")
    input("• Multiplica'l per 2 (Prem ENTER)...")
    input("• Suma-li 10 al resultat (Prem ENTER)...")
    input("• Resta-li 4 (Prem ENTER)...")
    
    res = float(input("-> Quin resultat t'ha donat al final?: "))
    
    secreto = calcular_numero_pensado(res)
    
    print("\n=========================================")
    print("🔮 Estaves pensant exactament en el número:", secreto)
    print("=========================================")
    
    historial.append("Lector de Ments -> Número descobert: " + str(secreto))

def modo_dos_jugadores(j1, j2):
    print("\n--- [3] DUEL D'ENDEVINAR:", j1, "VS", j2, "---")
    print(" Torn de", j1, "(El creador del repte)")
    secreto = int(input("• Escriu el número secret (de l'1 al 100) sense que miri " + j2 + ": "))
    
    for linea in range(40):
        print("")
        
    print("=========================================")
    print("Pantalla netejada! Torn de", j2)
    print("Intenta endevinar el número secret en el mínim d'intents.")
    print("=========================================")
    
    intentos = 0
    adivinado = False
    
    while not adivinado:
        intento = int(input("\n>> " + j2 + ", introdueix el teu número: "))
        intentos += 1
        
        if intento < 1 or intento > 100:
            print("[!] Avís: recorda que el número està entre 1 i 100.")
        elif intento > secreto:
            print("[-] T'has passat! El número secret és MÉS PETIT que", intento)
        elif intento < secreto:
            print("[+] T'has quedat curt! El número secret és MÉS GRAN que", intento)
        else:
            print("\n🎉 BRUTAL! Has encertat el número secret (", secreto, ")! 🎉")
            print("-> Ho has aconseguit en", intentos, "intents.")
            adivinado = True
            
    registro = "Duel (" + j1 + " vs " + j2 + ") -> Guanyat en " + str(intentos) + " intents"
    historial.append(registro)

def mostrar_historial():
    print("\n--- [4] HISTORIAL DE PARTIDES ---")
    if len(historial) == 0:
        print("Encara no s'ha jugat cap partida.")
    else:
        print("Total de partides jugades:", len(historial))
        for partida in historial:
            print(" •", partida)


funcionar = True

while funcionar:
    print("""
=========================================
        JOC D'ENDEVINAR EL NÚMERO 
=========================================
Opcions de joc:

  1. El Mag Matemàtic (Truc del projecte)
  2. Lector de Ments (Fórmula ràpida)
  3. Mode 2 Jugadors (Pistes: Major / Menor)
  4. Veure historial de partides
  5. Sortir
=========================================
""")
    opcio = input(">> Escull una opció (1-5): ")
    
    opcio = opcio.strip()
    
    if opcio == "1":
        juego_truco_clasico()
        
    elif opcio == "2":
        juego_adivino_tu_mente()
        
    elif opcio == "3":
        print("\n--- CONFIGURACIÓ DE JUGADORS ---")
        nom1 = input("• Nom del Jugador 1 (pensa el número): ").capitalize()
        nom2 = input("• Nom del Jugador 2 (endevina el número): ").capitalize()
        
        modo_dos_jugadores(nom1, nom2)
        
    elif opcio == "4":
        mostrar_historial()
        
    elif opcio == "5":
        print("\n=========================================")
        print("Fins aviat! Gràcies per jugar.")
        print("=========================================")
        funcionar = False
        
    else:
        print("\n[!] Opció no vàlida. Tria un número de l'1 al 5.")
        
    print("-----------------------------------------")
