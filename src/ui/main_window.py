"""
Interface de usuário do PCVitalBoost
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import MDList, OneLineIconListItem
from kivy.metrics import dp

import logging

logger = logging.getLogger(__name__)


class MainScreen(MDScreen):
    """Tela principal do aplicativo"""
    
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.app_instance = app_instance
        self.build_ui()
        
    def build_ui(self):
        """Constrói a interface da tela principal"""
        layout = BoxLayout(orientation='vertical')
        
        # Barra superior
        toolbar = MDTopAppBar(
            title="PCVitalBoost",
            md_bg_color=(0.2, 0.6, 0.8, 1),
            left_action_items=[["menu", lambda x: self.toggle_nav_drawer()]]
        )
        layout.add_widget(toolbar)
        
        # Área de conteúdo
        content = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        # Informações do sistema
        info_card = self.create_info_card()
        content.add_widget(info_card)
        
        # Botões de ação
        actions_layout = GridLayout(cols=2, spacing=dp(10), size_hint_y=None, height=dp(200))
        
        btn_update_drivers = MDRaisedButton(
            text="Atualizar Drivers",
            on_release=self.update_drivers
        )
        actions_layout.add_widget(btn_update_drivers)
        
        btn_update_programs = MDRaisedButton(
            text="Atualizar Programas",
            on_release=self.update_programs
        )
        actions_layout.add_widget(btn_update_programs)
        
        btn_optimize = MDRaisedButton(
            text="Otimizar Sistema",
            on_release=self.optimize_system
        )
        actions_layout.add_widget(btn_optimize)
        
        btn_clean = MDRaisedButton(
            text="Limpar Sistema",
            on_release=self.clean_system
        )
        actions_layout.add_widget(btn_clean)
        
        content.add_widget(actions_layout)
        
        # Área de resultados
        self.results_label = MDLabel(
            text="Bem-vindo ao PCVitalBoost!",
            halign="center",
            size_hint_y=None,
            height=dp(100)
        )
        content.add_widget(self.results_label)
        
        layout.add_widget(content)
        self.add_widget(layout)
    
    def create_info_card(self):
        """Cria card com informações do sistema"""
        from src.modules import SystemOptimizer
        
        optimizer = SystemOptimizer()
        info = optimizer.get_system_info()
        
        card = MDCard(
            orientation='vertical',
            padding=dp(15),
            size_hint_y=None,
            height=dp(150)
        )
        
        info_text = f"""
Informações do Sistema:
CPU: {info['cpu_count']} núcleos - {info['cpu_percent']:.1f}% em uso
Memória: {info['total_memory']:.1f} GB - {info['memory_percent']:.1f}% em uso
Disco: {info['disk_usage']:.1f}% em uso
        """
        
        label = MDLabel(
            text=info_text.strip(),
            theme_text_color="Secondary"
        )
        card.add_widget(label)
        
        return card
    
    def toggle_nav_drawer(self):
        """Alterna drawer de navegação"""
        logger.info("Toggle navigation drawer")
        
    def update_drivers(self, instance):
        """Atualiza drivers do sistema"""
        logger.info("Atualizando drivers...")
        self.results_label.text = "Verificando drivers..."
        
        from src.modules import DriverUpdater
        updater = DriverUpdater()
        drivers = updater.check_drivers()
        
        if drivers:
            self.results_label.text = f"Encontrados {len(drivers)} drivers para atualizar"
        else:
            self.results_label.text = "Todos os drivers estão atualizados!"
    
    def update_programs(self, instance):
        """Atualiza programas instalados"""
        logger.info("Atualizando programas...")
        self.results_label.text = "Verificando programas..."
        
        from src.modules import ProgramUpdater
        updater = ProgramUpdater()
        programs = updater.check_programs()
        
        if programs:
            self.results_label.text = f"Encontrados {len(programs)} programas para atualizar"
        else:
            self.results_label.text = "Todos os programas estão atualizados!"
    
    def optimize_system(self, instance):
        """Otimiza o sistema"""
        logger.info("Otimizando sistema...")
        self.results_label.text = "Otimizando sistema..."
        
        from src.modules import SystemOptimizer
        optimizer = SystemOptimizer()
        result = optimizer.optimize_memory()
        
        self.results_label.text = result['message']
    
    def clean_system(self, instance):
        """Limpa arquivos desnecessários"""
        logger.info("Limpando sistema...")
        self.results_label.text = "Escaneando arquivos..."
        
        from src.modules import SystemCleaner
        cleaner = SystemCleaner()
        junk = cleaner.scan_for_junk()
        
        total_mb = junk['total_size'] / (1024**2)
        self.results_label.text = f"Encontrados {total_mb:.2f} MB de arquivos desnecessários"


class PCVitalBoostUI(MDApp):
    """Aplicativo principal"""
    
    def build(self):
        """Constrói a interface do aplicativo"""
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        return MainScreen(self)
