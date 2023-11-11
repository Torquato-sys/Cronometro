import time

def contador(segundos): #função definida
    for i in range(segundos):
        min, seg = divmod(segundos-i, 60) # Calcular tempo que falta;
        texto = f"{min:02d}:{seg:02d}" # Texto a ser exibido
        print(texto, end='\r') #função do (end='\r') o mesmo se encarrega de substituir o print anterior para não se acumular de vairos prints na tela;
        time.sleep(1)

contador(10)