import pypokedex
import tkinter as tk
import PIL.Image
from PIL import ImageTk
from io import BytesIO
import urllib3


def lade_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f'{pokemon.dex} - {pokemon.name}')
    pokemon_types.config(text=f'{pokemon.types}')


# Hauptfenster

Fenster = tk.Tk(__name__)
Fenster.geometry("600x525")
Fenster.title("Dj Spyro0815's  Pokedex")
Fenster.config(padx=10, pady=10)


Überschrift_Label = tk.Label(Fenster, text="Dj Spyro0815's Pokedex")
Überschrift_Label.config(font=('Consolas', 32), fg='FireBrick')


pokemon_image = tk.Label(Fenster)


pokemon_information = tk.Label(Fenster)
pokemon_information.config(font=('Consolas', 20))


pokemon_types = tk.Label(Fenster)
pokemon_types.config(font=('Consolas', 20))


label_id_name = tk.Label(Fenster, text="Name oder ID eintragen")
label_id_name.config(font=("Consolas", 20), fg='FireBrick')


text_id_name = tk.Text(Fenster, height=1)
text_id_name.config(font=("Consolas", 20), fg='FireBrick')


btn_load = tk.Button(Fenster, text="Lade Pokemon", command=lade_pokemon)
btn_load.config(font=('Consolas', 20), bg='Firebrick', fg='Gold')


Überschrift_Label.pack(side="top", padx=10, pady=15)
pokemon_image.pack(side="top", padx=10, pady=10)
pokemon_information.pack(side="top", padx=10, pady=10)
pokemon_types.pack(side="top", padx=10, pady=10)
label_id_name.pack(side="top", padx=10, pady=10)
text_id_name.pack(side="top", padx=10, pady=10)
btn_load.pack(side="top", padx=10, pady=10)


if __name__ == '__main__':
    Fenster.mainloop()
