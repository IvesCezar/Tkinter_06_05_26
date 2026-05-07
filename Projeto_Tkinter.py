from tkinter import *
from tkinter import messagebox

cliente = Tk()
cliente.title("Token de Atendimento")
cliente.geometry("400x300")
cliente.configure(bg="lightblue")

contador = 1
fila = []
senha_atual = StringVar()
senha_atual.set("---")

adin = Toplevel(cliente)
adin.title("Administrador")
adin.geometry("300x200")    
admin.configure(bg="lightgray")

Label(admin, text="Senhas:",font=("Arial", 14)). pack(pady=10)

lista_admin = Listbox(admin, widht=20, height=10)
lista_admin.pack(pady=10)

painel = Toplvele(cliente)
painel.title("Painel de solicitações")
painel.geometry("300x200")
painel.configure(bg="lightyellow")
Label(painel, text="Senha Atual:", font=("Arial", 14)).pack(pady=10)

Label(painel, textvariable=senha_atual, font=("Arial", 24)).pack(pady=10)
def gerar_senha():
    global contador
    senha = f"S{contador:03d}"
    fila.append(senha)
    lista_admin.insert(END, senha)
    contador += 1
    messagebox.showinfo("Senha Gerada", f"Sua senha é: {senha}")
def chamar_proximo():
    if fila:
        senha = fila.pop(0)
        senha_atual.set(senha)
        lista_admin.delete(0)
    else:
        messagebox.showinfo("Fila Vazia", "Não há mais senhas na fila.")
        