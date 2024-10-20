from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import math

# Carrega o arquivo .kv
GUI = Builder.load_file("tela.kv")

class ConversorGR(App):
    def build(self):
        return GUI

    def on_start(self):
        # Chama o menu ao iniciar o aplicativo
        self.root.ids.menu_label.text = "Selecione uma opção:"

    def opcao1(self):
        deg = float(self.root.ids.input_text.text)  # Recebe o valor do campo de entrada
        resultado = (deg * math.pi) / 180.0
        self.root.ids.result_label.text = f"O ângulo mede, aproximadamente, {resultado:.4f} rad."

    def opcao2(self):
        rad = float(self.root.ids.input_text.text)  # Recebe o valor do campo de entrada
        resultado = (rad * 180.0) / math.pi
        self.root.ids.result_label.text = f"O ângulo mede, aproximadamente, {resultado:.4f} graus."

# Executa o app
ConversorGR().run()


