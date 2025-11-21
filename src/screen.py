import tkinter as tk
import spam_detector

def analizar_email():
    texto = entrada_email.get()
    if texto == "":
        etiqueta_resultado.config(text="Por favor escriba un email")
        return

    resultado = spam_detector.predecir_spam(texto, modelo, vectorizer)

    if resultado =="Spam":
        etiqueta_resultado.config(text = "Spam", fg = "Red")
    else:
        etiqueta_resultado.config(text="No spam", fg = "green")
def main():     
    global modelo, vectorizer, entrada_email, etiqueta_resultado
    print("Entrenando medelo...")
    modelo, vectorizer = spam_detector.entrenar_modelo()
    accuracy = spam_detector.evaluar_modelo(modelo, vectorizer)
    print(f"Precision dele modelo: {accuracy:.2f}")

    ventana = tk.Tk()
    ventana.title("Detector de Spam")
    ventana.geometry("500x300")

    titulo = tk.Label(ventana, text="Dectector de spam", font= ("Arial", 16, "bold"))
    titulo.pack(pady=20)

    instruccion = tk.Label(ventana, text="Escribe un email para analizar")
    instruccion.pack()

    entrada_email = tk.Entry(ventana, width=50)
    entrada_email.pack(pady=10)

    boton = tk.Button(ventana, text="Analizar", command= analizar_email,
                      bg = "#4CAF50", fg="white", padx=20, pady=5)
    boton.pack(pady=10)

    etiqueta_resultado = tk.Label(ventana, text="", font=("Arial,14"))
    etiqueta_resultado.pack(pady=20)

    ventana.mainloop()

if __name__ == "__main__":
    main()
