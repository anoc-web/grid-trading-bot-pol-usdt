# ============================================
# BOT DE GRID TRADING PARA POL/USDT
# Versión simplificada para aprender
# ============================================

import json
import time
import logging
from datetime import datetime

# Configuración del bot
class GridTradingBot:
    def __init__(self, config_file='config.json'):
        """
        Inicializa el bot con la configuración
        """
        print("🚀 Iniciando bot de grid trading...")
        self.cargar_configuracion(config_file)
        self.ordenes_activas = []
        self.ganancias_totales = 0
        
    def cargar_configuracion(self, archivo):
        """
        Carga la configuración desde un archivo JSON
        """
        try:
            with open(archivo, 'r') as f:
                self.config = json.load(f)
            print(f"✅ Configuración cargada: {self.config}")
        except FileNotFoundError:
            print(f"❌ Archivo {archivo} no encontrado. Usando configuración por defecto.")
            self.config = {
                "par": "POL/USDT",
                "precio_actual": 0.11,
                "grid_inferior": 0.09,
                "grid_superior": 0.13,
                "numero_ordenes": 10,
                "inversion_total": 50
            }
    
    def calcular_niveles_grid(self):
        """
        Calcula los niveles de compra y venta
        """
        inferior = self.config['grid_inferior']
        superior = self.config['grid_superior']
        num_ordenes = self.config['numero_ordenes']
        
        # Calcular el espaciado entre niveles
        espaciado = (superior - inferior) / (num_ordenes - 1)
        
        niveles = []
        for i in range(num_ordenes):
            precio = inferior + (i * espaciado)
            niveles.append({
                'nivel': i + 1,
                'precio': round(precio, 4),
                'tipo': 'compra' if precio < self.config.get('precio_actual', 0.11) else 'venta'
            })
        
        return niveles
    
    def simular_operacion(self):
        """
        Simula una operación del grid (para pruebas sin dinero real)
        """
        print("\n" + "="*50)
        print("📊 SIMULACIÓN DE GRID TRADING")
        print("="*50)
        
        print(f"\n📈 Par: {self.config['par']}")
        print(f"💰 Precio actual: ${self.config['precio_actual']}")
        print(f"📉 Rango del grid: ${self.config['grid_inferior']} - ${self.config['grid_superior']}")
        print(f"📊 Número de órdenes: {self.config['numero_ordenes']}")
        print(f"💵 Inversión total: ${self.config['inversion_total']} USDT")
        
        # Calcular niveles
        niveles = self.calcular_niveles_grid()
        
        print("\n📋 NIVELES DEL GRID:")
        print("-" * 40)
        print(f"{'Nivel':<6} {'Precio':<10} {'Tipo':<10} {'Cantidad':<10}")
        print("-" * 40)
        
        for nivel in niveles:
            cantidad_por_orden = self.config['inversion_total'] / self.config['numero_ordenes']
            print(f"{nivel['nivel']:<6} ${nivel['precio']:<9} {nivel['tipo']:<10} ${cantidad_por_orden:.2f}")
        
        # Simular ganancia
        ganancia_simulada = self.config['inversion_total'] * 0.005  # 0.5% de ganancia
        self.ganancias_totales += ganancia_simulada
        
        print("\n" + "="*50)
        print(f"💰 GANANCIA ESTIMADA: ${ganancia_simulada:.2f} (0.5%)")
        print(f"📈 GANANCIAS TOTALES: ${self.ganancias_totales:.2f}")
        print("="*50)
        
        return ganancia_simulada
    
    def ejecutar(self):
        """
        Bucle principal del bot
        """
        print("\n🔄 Bot en funcionamiento...")
        contador = 0
        
        try:
            while contador < 5:  # Solo 5 iteraciones para prueba
                print(f"\n⏱️  Iteración {contador + 1} - {datetime.now().strftime('%H:%M:%S')}")
                
                # Simular que el precio cambia ligeramente
                self.config['precio_actual'] = round(
                    self.config['precio_actual'] * (1 + (contador * 0.001)), 4
                )
                
                ganancia = self.simular_operacion()
                
                print("⏳ Esperando 5 segundos...")
                time.sleep(5)
                contador += 1
                
        except KeyboardInterrupt:
            print("\n🛑 Bot detenido por el usuario")
        
        print("\n📊 RESUMEN FINAL:")
        print(f"💰 Ganancias totales: ${self.ganancias_totales:.2f}")

# Punto de entrada principal
if __name__ == "__main__":
    print("="*50)
    print("🤖 BOT DE GRID TRADING - POL/USDT")
    print("="*50)
    
    # Crear y ejecutar el bot
    bot = GridTradingBot()
    bot.ejecutar()
