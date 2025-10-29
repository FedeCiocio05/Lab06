import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostra_auto(self, e):
        #try/except attorno alla chiamata al model per catturare errori DB
        try:
            auto = self._model.get_automobili()
        except Exception as e:
            self._view.alert.show_alert(f"❌ Errore durante la lettura delle automobili: {e}")
            return
        #pulizia lista
        self._view.lista_auto.controls.clear()
        for a in auto:
            self._view.lista_auto.controls.append(ft.Text(f'{a}'))
        self._view.update()

    def mostra_modelli(self, e):
        modello = self._view.input_modello_auto.value
        #validazione input (modello non vuoto) prima di chiamare il Model
        if not modello:
            self._view.alert.show_alert("ℹ️ Inserisci un modello da cercare.")
            return
        #try/except per gestire eccezioni DB
        try:
            auto_m = self._model.cerca_automobili_per_modello(modello)
        except Exception as e:
            self._view.alert.show_alert(f"❌ Errore durante la ricerca: {e}")
            return
        # pulizia lista
        self._view.lista_auto_ricerca.controls.clear()
        if not auto_m:
            self._view.lista_auto_ricerca.controls.append(ft.Text(f"Nessuna auto trovata per modello '{modello}'."))
        else:
            for a in auto_m:
                self._view.lista_auto_ricerca.controls.append(ft.Text(f'{a}'))
        self._view.update()
    # TODO
