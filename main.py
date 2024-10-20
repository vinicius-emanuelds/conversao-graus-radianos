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

    def converter(self):
        # Verifica o tipo de conversão selecionada
        conversion_type = self.root.ids.conversion_type.text
        input_value = self.root.ids.input_value.text

        if input_value:  # Verifica se há um valor de entrada
            try:
                input_value = float(input_value)  # Tenta converter para float
                if conversion_type == 'Graus para Radianos':
                    resultado = (input_value * math.pi) / 180.0
                    self.root.ids.output_label.text = f"O ângulo mede, aproximadamente, {resultado:.4f} rad."
                elif conversion_type == 'Radianos para Graus':
                    resultado = (input_value * 180.0) / math.pi
                    self.root.ids.output_label.text = f"O ângulo mede, aproximadamente, {resultado:.2f} graus."
                else:
                    self.root.ids.output_label.text = "Selecione um tipo de conversão válido."
            except ValueError:
                self.root.ids.output_label.text = "Insira um número válido."
        else:
            self.root.ids.output_label.text = "Insira um valor para converter."

# Executa o app
ConversorGR().run()
