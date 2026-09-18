"""
Interface de usuário do PCVitalBoost
"""
import logging
import threading

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp

logger = logging.getLogger(__name__)


class MainScreen(MDScreen):
    """Tela principal do aplicativo"""
    
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.app_instance = app_instance
        self._current_operation = None
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
        actions_layout = GridLayout(cols=2, spacing=dp(10), size_hint_y=None, height=dp(300))
        
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
        
        btn_import_dropbox = MDRaisedButton(
            text="Importar do Dropbox",
            on_release=self.import_from_dropbox
        )
        actions_layout.add_widget(btn_import_dropbox)
        
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
        card = MDCard(
            orientation='vertical',
            padding=dp(15),
            size_hint_y=None,
            height=dp(150)
        )
        label = MDLabel(text="Carregando informações do sistema...",
                        theme_text_color="Secondary")
        card.add_widget(label)
        self._run_in_background(
            self._get_system_info,
            lambda info: self._set_system_info(label, info),
            lambda error: self._show_error(label, "Erro ao carregar informações", error),
        )
        return card

    @staticmethod
    def _get_system_info():
        """Obtém informações do sistema fora da thread da interface."""
        from src.modules import SystemOptimizer

        return SystemOptimizer().get_system_info(wait_for_cpu_sample=True)

    @staticmethod
    def _set_system_info(label, info):
        """Atualiza o card de informações na thread da interface."""
        label.text = (
            "Informações do Sistema:\n"
            f"CPU: {info['cpu_count']} núcleos - {info['cpu_percent']:.1f}% em uso\n"
            f"Memória: {info['total_memory']:.1f} GB - "
            f"{info['memory_percent']:.1f}% em uso\n"
            f"Disco: {info['disk_usage']:.1f}% em uso"
        )

    def _run_in_background(self, work, on_success, on_error):
        """Executa uma operação demorada sem bloquear o thread da interface."""
        def worker():
            try:
                result = work()
            except Exception as error:
                logger.error("Operação em segundo plano falhou", exc_info=True)
                Clock.schedule_once(lambda _dt, error=error: on_error(error), 0)
            else:
                Clock.schedule_once(lambda _dt, result=result: on_success(result), 0)

        threading.Thread(target=worker, daemon=True).start()

    def _start_action(self, name, status_message, work, on_success, error_prefix):
        """Inicia uma ação de manutenção e evita operações concorrentes."""
        if self._current_operation is not None:
            self.results_label.text = "Aguarde a conclusão da operação em andamento."
            return

        self._current_operation = name
        self.results_label.text = status_message

        def complete(result):
            if self._current_operation != name:
                return
            self._current_operation = None
            on_success(result)

        def fail(error):
            if self._current_operation != name:
                return
            self._current_operation = None
            self._show_error(self.results_label, error_prefix, error)

        self._run_in_background(work, complete, fail)

    @staticmethod
    def _show_error(label, prefix, error):
        """Exibe uma falha de operação de forma clara para o usuário."""
        label.text = f"{prefix}: {error}"

    @staticmethod
    def _check_drivers():
        """Verifica drivers fora da thread da interface."""
        from src.modules import DriverUpdater

        return DriverUpdater().check_drivers()

    @staticmethod
    def _check_programs():
        """Verifica programas fora da thread da interface."""
        from src.modules import ProgramUpdater

        return ProgramUpdater().check_programs()

    @staticmethod
    def _optimize_memory():
        """Analisa a memória fora da thread da interface."""
        from src.modules import SystemOptimizer

        return SystemOptimizer().optimize_memory()

    @staticmethod
    def _scan_for_junk():
        """Escaneia arquivos fora da thread da interface."""
        from src.modules import SystemCleaner

        return SystemCleaner().scan_for_junk()
    
    def toggle_nav_drawer(self):
        """Alterna drawer de navegação"""
        logger.info("Toggle navigation drawer")
        
    def update_drivers(self, instance):
        """Atualiza drivers do sistema"""
        logger.info("Atualizando drivers...")
        self._start_action(
            "drivers",
            "Verificando drivers...",
            self._check_drivers,
            lambda drivers: setattr(
                self.results_label,
                "text",
                f"Encontrados {len(drivers)} drivers para atualizar"
                if drivers else "Todos os drivers estão atualizados!",
            ),
            "Erro ao verificar drivers",
        )
    
    def update_programs(self, instance):
        """Atualiza programas instalados"""
        logger.info("Atualizando programas...")
        self._start_action(
            "programas",
            "Verificando programas...",
            self._check_programs,
            lambda programs: setattr(
                self.results_label,
                "text",
                f"Encontrados {len(programs)} programas para atualizar"
                if programs else "Todos os programas estão atualizados!",
            ),
            "Erro ao verificar programas",
        )
    
    def optimize_system(self, instance):
        """Otimiza o sistema"""
        logger.info("Otimizando sistema...")
        self._start_action(
            "otimizacao",
            "Otimizando sistema...",
            self._optimize_memory,
            lambda result: setattr(self.results_label, "text", result["message"]),
            "Erro ao otimizar sistema",
        )
    
    def clean_system(self, instance):
        """Limpa arquivos desnecessários"""
        logger.info("Limpando sistema...")
        self._start_action(
            "limpeza",
            "Escaneando arquivos...",
            self._scan_for_junk,
            lambda junk: setattr(
                self.results_label,
                "text",
                f"Encontrados {junk['total_size'] / (1024**2):.2f} MB "
                "de arquivos desnecessários",
            ),
            "Erro ao escanear arquivos",
        )
    
    def import_from_dropbox(self, instance):
        """Importa arquivo do Dropbox"""
        logger.info("Importando do Dropbox...")
        self.results_label.text = "Conectando ao Dropbox..."
        
        try:
            from src.modules import DropboxImporter
            
            # Cria instância do importador
            importer = DropboxImporter()
            
            if not importer.is_authenticated():
                self.results_label.text = "Autenticação necessária. Verifique o navegador..."
                # Inicia processo de autenticação
                if importer.authenticate():
                    self.results_label.text = "Por favor, autorize o aplicativo no navegador e cole o código na próxima tela"
                else:
                    self.results_label.text = "Erro ao iniciar autenticação. Verifique DROPBOX_APP_KEY"
            else:
                # Já autenticado, lista arquivos
                account_info = importer.get_account_info()
                if account_info:
                    self.results_label.text = f"Conectado como: {account_info['name']}\nListando arquivos..."
                    files = importer.list_files()
                    if files:
                        self.results_label.text = f"Encontrados {len(files)} arquivos no Dropbox"
                    else:
                        self.results_label.text = "Nenhum arquivo encontrado no Dropbox"
                else:
                    self.results_label.text = "Erro ao obter informações da conta"
                    
        except ImportError as e:
            logger.error(f"Erro ao importar módulo Dropbox: {e}")
            self.results_label.text = "Dropbox SDK não instalado. Execute: pip install dropbox"
        except Exception as e:
            logger.error(f"Erro ao importar do Dropbox: {e}")
            self.results_label.text = f"Erro: {str(e)}"


class PCVitalBoostUI(MDApp):
    """Aplicativo principal"""
    
    def build(self):
        """Constrói a interface do aplicativo"""
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        return MainScreen(self)
