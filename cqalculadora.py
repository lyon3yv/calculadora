import math

funcionar = True

while funcionar:
    print("""
=========================================
              CALCULADORA 🖩
=========================================
Opcions:

  1. Sumar ➕
  2. Restar ➖
  3. Multiplicar ✖️
  4. Dividir ➗
  5. Potència
  6. Arrel quadrada (math.sqrt)
  7. Àrea i perímetre d'un rectangle ▭
  8. Àrea i longitud d'un cercle ⭕
  9. Àrea d'un triangle
  10. Volum d'un cilindre
  11. Volum d'una esfera
  12. Volum i àrea d'un con
  13. Teorema de Pitàgores (math.hypot)
  14. Equació lineal (ax + b = 0) ♾️
  15. Equació de segon grau (ax² + bx + c = 0)
  16. Mitjana de tres nombres
  17. Calcular un percentatge (%)
  18. Calcular IVA i descomptes
  19. Regla de tres simple
  20. Convertir Celsius a Fahrenheit
  21. Convertir km/h a m/s
  22. Factorial d'un nombre (math.factorial)
  23. Taula de multiplicar
  24. Comprovar si és parell o senar
  25. Trigonometria: Sinus, Cosinus i Tangent
  26. Convertir Graus i Radians
  27. Logaritmes (base 10, neperià i qualsevol base)
  28. Màxim Comú Divisor (MCD) i Mínim Comú Múltiple (MCM)
  29. Arrodoniment (alça, baixa) i Valor Absolut
  30. Distància entre dos punts (x1, y1) i (x2, y2)
  31. Física: Moviment Rectilini Uniforme (MRU)
  32. Física: Llei d'Ohm (Voltatge, Intensitat, Resistència)
  33. Física: Densitat, Massa i Volum
  34. Energia Cinètica i Potencial
  35. Sortir 🔚
=========================================
""")
    opcio = int(input(">> Escull una opció (1-35): "))
    
    if opcio == 1:
        print("\n--- [1] SUMA ➕ ---")
        n1 = float(input("• Primer nombre: "))
        n2 = float(input("• Segon nombre: "))
        resultat = n1 + n2
        print("-> El resultat de la suma és:", resultat)
        
    elif opcio == 2:
        print("\n--- [2] RESTA ➖ ---")
        n1 = float(input("• Primer nombre: "))
        n2 = float(input("• Segon nombre: "))
        resultat = n1 - n2
        print("-> El resultat de la resta és:", resultat)
        
    elif opcio == 3:
        print("\n--- [3] MULTIPLICACIÓ ✖️ ---")
        n1 = float(input("• Primer nombre: "))
        n2 = float(input("• Segon nombre: "))
        resultat = n1 * n2
        print("-> El resultat de la multiplicació és:", resultat)
        
    elif opcio == 4:
        print("\n--- [4] DIVISIÓ ➗ ---")
        dividend = float(input("• Dividend: "))
        divisor = float(input("• Divisor: "))
        if divisor == 0:
            print("[!] Error: no es pot dividir entre zero.")
        else:
            resultat = dividend / divisor
            residu = dividend % divisor
            divisio_entera = dividend // divisor
            print("-> El resultat de la divisió és:", resultat)
            print("-> La divisió entera és:", divisio_entera)
            print("-> El residu de la divisió és:", residu)
            
    elif opcio == 5:
        print("\n--- [5] POTÈNCIA ---")
        base = float(input("• Base: "))
        exponent = float(input("• Exponent: "))
        resultat = math.pow(base, exponent)
        print("-> El resultat de la potència és:", resultat)
        
    elif opcio == 6:
        print("\n--- [6] ARREL QUADRADA ---")
        nombre = float(input("• Nombre: "))
        if nombre < 0:
            print("[!] Error: no es pot fer l'arrel quadrada d'un nombre negatiu.")
        else:
            resultat = math.sqrt(nombre)
            print("-> L'arrel quadrada és:", resultat)
            
    elif opcio == 7:
        print("\n--- [7] ÀREA I PERÍMETRE DEL RECTANGLE ▭ ---")
        base = float(input("• Base (en cm): "))
        altura = float(input("• Altura (en cm): "))
        area = base * altura
        perimetre = 2 * base + 2 * altura
        print("-> L'àrea del rectangle és:", area, "cm²")
        print("-> El perímetre del rectangle és:", perimetre, "cm")
        
    elif opcio == 8:
        print("\n--- [8] ÀREA I LONGITUD DEL CERCLE ⭕ ---")
        radi = float(input("• Radi (en cm): "))
        area = math.pi * math.pow(radi, 2)
        longitud = 2 * math.pi * radi
        print("-> L'àrea del cercle és:", area, "cm²")
        print("-> La longitud de la circumferència és:", longitud, "cm")
        
    elif opcio == 9:
        print("\n--- [9] ÀREA DEL TRIANGLE ---")
        base = float(input("• Base (en cm): "))
        altura = float(input("• Altura (en cm): "))
        area = (base * altura) / 2
        print("-> L'àrea del triangle és:", area, "cm²")

    elif opcio == 10:
        print("\n--- [10] VOLUM D'UN CILINDRE ---")
        radi = float(input("• Radi de la base (en cm): "))
        altura = float(input("• Altura (en cm): "))
        volum = math.pi * math.pow(radi, 2) * altura
        print("-> El volum del cilindre és:", volum, "cm³")

    elif opcio == 11:
        print("\n--- [11] VOLUM D'UNA ESFERA ---")
        radi = float(input("• Radi de l'esfera (en cm): "))
        volum = (4 / 3) * math.pi * math.pow(radi, 3)
        print("-> El volum de l'esfera és:", volum, "cm³")

    elif opcio == 12:
        print("\n--- [12] VOLUM I ÀREA D'UN CON ---")
        radi = float(input("• Radi de la base (en cm): "))
        altura = float(input("• Altura del con (en cm): "))
        generatriu = math.hypot(radi, altura)
        volum = (1 / 3) * math.pi * math.pow(radi, 2) * altura
        area_total = math.pi * radi * (radi + generatriu)
        print("-> La generatriu del con és:", generatriu, "cm")
        print("-> El volum del con és:", volum, "cm³")
        print("-> L'àrea total del con és:", area_total, "cm²")
        
    elif opcio == 13:
        print("\n--- [13] TEOREMA DE PITÀGORES ---")
        catet1 = float(input("• Primer catet (en cm): "))
        catet2 = float(input("• Segon catet (en cm): "))
        hipotenusa = math.hypot(catet1, catet2)
        print("-> La hipotenusa és:", hipotenusa, "cm")
        
    elif opcio == 14:
        print("\n--- [14] EQUACIÓ LINEAL (ax + b = 0) ♾️ ---")
        a = float(input("• Valor de a: "))
        b = float(input("• Valor de b: "))
        if a == 0:
            if b == 0:
                print("-> L'equació té infinites solucions (0 = 0).")
            else:
                print("[!] L'equació no té solució.")
        else:
            x = -b / a
            print("-> La solució és x =", x)
            
    elif opcio == 15:
        print("\n--- [15] EQUACIÓ DE SEGON GRAU (ax² + bx + c = 0) ---")
        a = float(input("• Valor de a: "))
        b = float(input("• Valor de b: "))
        c = float(input("• Valor de c: "))
        if a == 0:
            print("[!] Si a = 0, no és de segon grau. Utilitza l'opció 14.")
        else:
            discriminant = math.pow(b, 2) - (4 * a * c)
            if discriminant < 0:
                print("[!] L'equació no té solucions reals (discriminant negatiu).")
            elif discriminant == 0:
                x = -b / (2 * a)
                print("-> L'equació té una única solució: x =", x)
            else:
                x1 = (-b + math.sqrt(discriminant)) / (2 * a)
                x2 = (-b - math.sqrt(discriminant)) / (2 * a)
                print("-> Primera solució: x1 =", x1)
                print("-> Segona solució: x2 =", x2)
                
    elif opcio == 16:
        print("\n--- [16] MITJANA DE TRES NOMBRES ---")
        n1 = float(input("• Primer nombre: "))
        n2 = float(input("• Segon nombre: "))
        n3 = float(input("• Tercer nombre: "))
        mitjana = (n1 + n2 + n3) / 3
        print("-> La mitjana aritmètica és:", mitjana)

    elif opcio == 17:
        print("\n--- [17] CALCULAR UN PERCENTATGE ---")
        total = float(input("• Quantitat total: "))
        percentatge = float(input("• Percentatge a calcular (%): "))
        resultat = (total * percentatge) / 100
        print("-> El", percentatge, "% de", total, "és:", resultat)

    elif opcio == 18:
        print("\n--- [18] CALCULAR IVA I DESCOMPTES ---")
        preu = float(input("• Preu inicial: "))
        percentatge = float(input("• Percentatge d'IVA o descompte (%): "))
        variacio = (preu * percentatge) / 100
        preu_amb_iva = preu + variacio
        preu_amb_descompte = preu - variacio
        print("-> Preu sumant el percentatge (IVA):", preu_amb_iva)
        print("-> Preu restant el percentatge (Descompte):", preu_amb_descompte)

    elif opcio == 19:
        print("\n--- [19] REGLA DE TRES SIMPLE (Si A -> B, llavors C -> X) ---")
        a = float(input("• Valor A: "))
        b = float(input("• Valor B: "))
        c = float(input("• Valor C: "))
        if a == 0:
            print("[!] Error: el valor A no pot ser zero.")
        else:
            x = (b * c) / a
            print("-> El valor de X és:", x)

    elif opcio == 20:
        print("\n--- [20] CONVERTIR CELSIUS A FAHRENHEIT ---")
        celsius = float(input("• Temperatura en graus Celsius (°C): "))
        fahrenheit = (celsius * 1.8) + 32
        print("-> La temperatura en Fahrenheit és:", fahrenheit, "°F")

    elif opcio == 21:
        print("\n--- [21] CONVERTIR KM/H A M/S ---")
        kmh = float(input("• Velocitat en km/h: "))
        ms = kmh / 3.6
        print("-> La velocitat en m/s és:", ms, "m/s")

    elif opcio == 22:
        print("\n--- [22] FACTORIAL D'UN NOMBRE ---")
        n = int(input("• Introdueix un nombre enter positiu: "))
        if n < 0:
            print("[!] Error: no existeix el factorial d'un nombre negatiu.")
        else:
            resultat = math.factorial(n)
            print("-> El factorial de", n, "és:", resultat)

    elif opcio == 23:
        print("\n--- [23] TAULA DE MULTIPLICAR ---")
        n = float(input("• De quin nombre vols la taula?: "))
        multiplicador = 1
        while multiplicador <= 10:
            resultat = n * multiplicador
            print(n, "x", multiplicador, "=", resultat)
            multiplicador = multiplicador + 1

    elif opcio == 24:
        print("\n--- [24] COMPROVAR SI ÉS PARELL O SENAR ---")
        n = int(input("• Introdueix un nombre enter: "))
        if n % 2 == 0:
            print("-> El nombre", n, "és PARELL.")
        else:
            print("-> El nombre", n, "és SENAR (imparell).")
            
        if n > 0:
            print("-> A més, és un nombre POSITIU.")
        elif n < 0:
            print("-> A més, és un nombre NEGATIU.")
        else:
            print("-> El nombre és ZERO.")

    elif opcio == 25:
        print("\n--- [25] TRIGONOMETRIA (SINUS, COSINUS, TANGENT) ---")
        graus = float(input("• Introdueix l'angle en graus: "))
        radians = math.radians(graus)
        sinus = math.sin(radians)
        cosinus = math.cos(radians)
        tangent = math.tan(radians)
        print("-> Sinus de", graus, "°:", sinus)
        print("-> Cosinus de", graus, "°:", cosinus)
        print("-> Tangent de", graus, "°:", tangent)

    elif opcio == 26:
        print("\n--- [26] CONVERTIR GRAUS I RADIANS ---")
        print("1. Passar de Graus a Radians")
        print("2. Passar de Radians a Graus")
        subopcio = int(input("• Tria una opció (1 o 2): "))
        if subopcio == 1:
            graus = float(input("• Angle en graus: "))
            radians = math.radians(graus)
            print("-> Equival a:", radians, "radians")
        elif subopcio == 2:
            radians = float(input("• Angle en radians: "))
            graus = math.degrees(radians)
            print("-> Equival a:", graus, "graus")
        else:
            print("[!] Subopció no vàlida.")

    elif opcio == 27:
        print("\n--- [27] LOGARITMES ---")
        nombre = float(input("• Nombre (ha de ser major que 0): "))
        if nombre <= 0:
            print("[!] Error: el nombre ha de ser estrictament positiu.")
        else:
            log_10 = math.log10(nombre)
            log_neperia = math.log(nombre)
            print("-> Logaritme en base 10:", log_10)
            print("-> Logaritme neperià (ln):", log_neperia)
            base = float(input("• Si vols una altra base, escriu-la (o posa 10): "))
            if base <= 0 or base == 1:
                print("[!] La base ha de ser major que 0 i diferent d'1.")
            else:
                log_base = math.log(nombre, base)
                print("-> Logaritme en base", base, "és:", log_base)

    elif opcio == 28:
        print("\n--- [28] MÀXIM COMÚ DIVISOR (MCD) I MÍNIM COMÚ MÚLTIPLE (MCM) ---")
        a = int(input("• Primer nombre enter: "))
        b = int(input("• Segon nombre enter: "))
        mcd = math.gcd(a, b)
        print("-> El Màxim Comú Divisor (MCD) és:", mcd)
        if mcd != 0:
            mcm = abs(a * b) // mcd
            print("-> El Mínim Comú Múltiple (MCM) és:", mcm)

    elif opcio == 29:
        print("\n--- [29] ARRODONIMENT I VALOR ABSOLUT ---")
        n = float(input("• Introdueix un nombre amb decimals (positiu o negatiu): "))
        valor_absolut = math.fabs(n)
        arrodonit_alca = math.ceil(n)
        arrodonit_baixa = math.floor(n)
        truncat = math.trunc(n)
        print("-> Valor absolut:", valor_absolut)
        print("-> Arrodonit a l'alça (ceil):", arrodonit_alca)
        print("-> Arrodonit a la baixa (floor):", arrodonit_baixa)
        print("-> Part entera truncada (trunc):", truncat)

    elif opcio == 30:
        print("\n--- [30] DISTÀNCIA ENTRE DOS PUNTS ---")
        x1 = float(input("• Coordenada x1: "))
        y1 = float(input("• Coordenada y1: "))
        x2 = float(input("• Coordenada x2: "))
        y2 = float(input("• Coordenada y2: "))
        distancia = math.hypot(x2 - x1, y2 - y1)
        print("-> La distància entre els dos punts és:", distancia)

    elif opcio == 31:
        print("\n--- [31] FÍSICA: MOVIMENT RECTILINI UNIFORME (v = d / t) ---")
        print("1. Calcular Velocitat (v)")
        print("2. Calcular Distància (d)")
        print("3. Calcular Temps (t)")
        subopcio = int(input("• Què vols calcular? (1-3): "))
        if subopcio == 1:
            d = float(input("• Distància (en metres): "))
            t = float(input("• Temps (en segons): "))
            if t == 0:
                print("[!] El temps no pot ser zero.")
            else:
                v = d / t
                print("-> La velocitat és:", v, "m/s")
        elif subopcio == 2:
            v = float(input("• Velocitat (en m/s): "))
            t = float(input("• Temps (en segons): "))
            d = v * t
            print("-> La distància recorreguda és:", d, "metres")
        elif subopcio == 3:
            d = float(input("• Distància (en metres): "))
            v = float(input("• Velocitat (en m/s): "))
            if v == 0:
                print("[!] La velocitat no pot ser zero.")
            else:
                t = d / v
                print("-> El temps emprat és:", t, "segons")
        else:
            print("[!] Opció no vàlida.")

    elif opcio == 32:
        print("\n--- [32] FÍSICA: LLEI D'OHM (V = I * R) ---")
        print("1. Calcular Voltatge (V)")
        print("2. Calcular Intensitat (I)")
        print("3. Calcular Resistència (R)")
        subopcio = int(input("• Què vols calcular? (1-3): "))
        if subopcio == 1:
            i = float(input("• Intensitat (en Ampers): "))
            r = float(input("• Resistència (en Ohms): "))
            v = i * r
            print("-> El voltatge és:", v, "Volts (V)")
        elif subopcio == 2:
            v = float(input("• Voltatge (en Volts): "))
            r = float(input("• Resistència (en Ohms): "))
            if r == 0:
                print("[!] La resistència no pot ser zero.")
            else:
                i = v / r
                print("-> La intensitat és:", i, "Ampers (A)")
        elif subopcio == 3:
            v = float(input("• Voltatge (en Volts): "))
            i = float(input("• Intensitat (en Ampers): "))
            if i == 0:
                print("[!] La intensitat no pot ser zero.")
            else:
                r = v / i
                print("-> La resistència és:", r, "Ohms (Ω)")
        else:
            print("[!] Opció no vàlida.")

    elif opcio == 33:
        print("\n--- [33] FÍSICA: DENSITAT (d = m / V) ---")
        massa = float(input("• Massa (en grams): "))
        volum = float(input("• Volum (en cm³): "))
        if volum == 0:
            print("[!] Error: el volum no pot ser zero.")
        else:
            densitat = massa / volum
            print("-> La densitat és:", densitat, "g/cm³")

    elif opcio == 34:
        print("\n--- [34] FÍSICA: ENERGIA CINÈTICA I POTENCIAL ---")
        massa = float(input("• Massa del cos (en kg): "))
        velocitat = float(input("• Velocitat (en m/s): "))
        altura = float(input("• Altura (en metres): "))
        gravetat = 9.81
        energia_cinetica = 0.5 * massa * math.pow(velocitat, 2)
        energia_potencial = massa * gravetat * altura
        energia_mecanica = energia_cinetica + energia_potencial
        print("-> Energia Cinètica (Ec):", energia_cinetica, "Joules (J)")
        print("-> Energia Potencial (Ep):", energia_potencial, "Joules (J)")
        print("-> Energia Mecànica Total (Em):", energia_mecanica, "Joules (J)")
        
    elif opcio == 35:
        print("\n=========================================")
        print("Fins aviat! Gràcies per fer servir la calculadora.🔚")
        print("=========================================")
        funcionar = False
        
    else:
        print("[!] Opció no vàlida. Tria un nombre de l'1 al 35.")
        
    print("-----------------------------------------\n")
