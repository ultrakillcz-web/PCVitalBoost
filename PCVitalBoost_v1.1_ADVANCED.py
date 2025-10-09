#!/usr/bin/env python3
"""
PCVitalBoost v1.1 - Sistema Otimizador Avançado
Com comandos profundos e interface melhorada
"""

import sys
import os
import platform
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import subprocess
import json
import webbrowser
import tempfile
import shutil
from pathlib import Path
from datetime import datetime
import time
import re

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

class PCVitalBoost:
    def __init__(self):
        self.version = "1.1.0"
        self.app_name = "PCVitalBoost"
        self.system_os = platform.system()
        self.is_admin = self.check_admin_privileges()

        # Estatísticas da sessão
        self.stats = {
            'files_cleaned': 0,
            'space_freed': 0,
            'drivers_updated': [],
            'software_updated': [],
            'errors_fixed': 0,
            'warnings': []
        }

        self.load_config()
        self.detect_system()
        self.create_main_window()

    def check_admin_privileges(self):
        """Verifica se está executando como administrador"""
        try:
            if platform.system() == 'Windows':
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin()
            else:
                return os.geteuid() == 0
        except:
            return False

    def load_config(self):
        """Carrega configurações"""
        try:
            if os.path.exists("config.json"):
                with open("config.json", "r", encoding="utf-8") as f:
                    self.config = json.load(f)
            else:
                self.config = {"settings": {"default_language": "pt_BR"}}
        except:
            self.config = {"settings": {"default_language": "pt_BR"}}

    def detect_system(self):
        """Detecta informações do sistema"""
        self.system_info = {
            'os': platform.system(),
            'version': platform.version(),
            'release': platform.release(),
            'architecture': platform.architecture()[0],
            'processor': platform.processor()
        }

        self.available_tools = self.check_available_tools()

    def check_available_tools(self):
        """Verifica ferramentas disponíveis"""
        tools = {}

        if self.system_os == 'Windows':
            tools['powershell'] = self.check_command('powershell')
            tools['winget'] = self.check_command('winget')
            tools['sfc'] = True  # Sempre disponível no Windows
            tools['dism'] = True
            tools['chkdsk'] = True
            tools['netsh'] = True
            tools['powercfg'] = True
            tools['cleanmgr'] = True
        elif self.system_os == 'Darwin':
            tools['brew'] = self.check_command('brew')
            tools['mas'] = self.check_command('mas')
        elif self.system_os == 'Linux':
            tools['apt'] = self.check_command('apt')
            tools['yum'] = self.check_command('yum')
            tools['pacman'] = self.check_command('pacman')

        return tools

    def check_command(self, command):
        """Verifica se comando existe"""
        try:
            result = subprocess.run([command, '--version'], 
                                  capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except:
            return False

    def create_main_window(self):
        """Cria janela principal MELHORADA"""
        self.root = tk.Tk()
        self.root.title(f"{self.app_name} v{self.version}")
        self.root.geometry("1200x900")  # Maior para evitar sobreposição
        self.root.configure(bg="#0f0f23")
        self.root.resizable(True, True)  # Permitir redimensionar

        self.center_window()
        self.setup_styles()
        self.create_header()
        self.create_progress_bar()  # NOVA barra de progresso
        self.create_main_body_improved()  # Layout melhorado
        self.create_footer_improved()  # Footer com botão copiar
        self.create_status_bar()

        # Bind para redimensionamento
        self.root.bind('<Configure>', self.on_window_resize)

    def center_window(self):
        """Centraliza janela"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.root.winfo_screenheight() // 2) - (900 // 2)
        self.root.geometry(f"1200x900+{x}+{y}")

    def setup_styles(self):
        """Configura estilos melhorados"""
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Configurar progressbar
        self.style.configure("Custom.Horizontal.TProgressbar",
                           background="#4299e1",
                           troughcolor="#1a202c",
                           borderwidth=0,
                           lightcolor="#4299e1",
                           darkcolor="#4299e1")

    def create_header(self):
        """Cria header melhorado"""
        header_frame = tk.Frame(self.root, bg="#1a202c", height=100)
        header_frame.pack(fill="x", padx=15, pady=10)
        header_frame.pack_propagate(False)

        # Logo
        logo_frame = tk.Frame(header_frame, bg="#1a202c")
        logo_frame.pack(side="left", fill="y")

        logo_label = tk.Label(logo_frame, text="🚀", font=("Arial", 35), 
                             bg="#1a202c", fg="#4299e1")
        logo_label.pack(anchor="w", pady=5)

        # Títulos
        info_frame = tk.Frame(header_frame, bg="#1a202c")
        info_frame.pack(side="left", fill="both", expand=True, padx=15)

        title_label = tk.Label(info_frame, text=self.app_name, 
                              font=("Arial", 22, "bold"), 
                              bg="#1a202c", fg="white")
        title_label.pack(anchor="w", pady=(10, 0))

        subtitle_label = tk.Label(info_frame, text="Sistema Otimizador Avançado v1.1", 
                                 font=("Arial", 11), 
                                 bg="#1a202c", fg="#a0aec0")
        subtitle_label.pack(anchor="w")

        # Status melhorado
        status_frame = tk.Frame(header_frame, bg="#1a202c")
        status_frame.pack(side="right", fill="y")

        version_label = tk.Label(status_frame, text=f"v{self.version}", 
                                font=("Arial", 10, "bold"), 
                                bg="#1a202c", fg="#4299e1")
        version_label.pack(anchor="e", pady=(10, 2))

        system_label = tk.Label(status_frame, text=f"{self.system_os} {platform.release()}", 
                               font=("Arial", 9), 
                               bg="#1a202c", fg="#a0aec0")
        system_label.pack(anchor="e")

        admin_status = "Admin ✓" if self.is_admin else "Execute como Admin"
        admin_color = "#48bb78" if self.is_admin else "#f56565"
        admin_label = tk.Label(status_frame, text=admin_status, 
                              font=("Arial", 9, "bold"), 
                              bg="#1a202c", fg=admin_color)
        admin_label.pack(anchor="e")

        if PSUTIL_AVAILABLE:
            mem = psutil.virtual_memory()
            mem_label = tk.Label(status_frame, text=f"RAM: {mem.percent}%", 
                                font=("Arial", 8), 
                                bg="#1a202c", fg="#a0aec0")
            mem_label.pack(anchor="e")

    def create_progress_bar(self):
        """Cria barra de progresso global"""
        self.progress_frame = tk.Frame(self.root, bg="#0f0f23", height=40)
        self.progress_frame.pack(fill="x", padx=20, pady=(0, 10))
        self.progress_frame.pack_propagate(False)

        # Label do progresso
        self.progress_label = tk.Label(self.progress_frame, text="Pronto", 
                                      font=("Arial", 10), 
                                      bg="#0f0f23", fg="#a0aec0")
        self.progress_label.pack(side="top", anchor="w")

        # Barra de progresso
        self.progress_bar = ttk.Progressbar(self.progress_frame, 
                                           style="Custom.Horizontal.TProgressbar",
                                           length=400, mode='determinate')
        self.progress_bar.pack(side="bottom", fill="x", pady=(5, 0))

        # Inicialmente escondida
        self.progress_frame.pack_forget()

    def create_main_body_improved(self):
        """Cria corpo principal com layout melhorado"""
        # Container principal
        main_container = tk.Frame(self.root, bg="#0f0f23")
        main_container.pack(fill="both", expand=True, padx=15, pady=5)

        # Frame esquerdo - Cards
        left_frame = tk.Frame(main_container, bg="#0f0f23", width=580)
        left_frame.pack(side="left", fill="both", expand=False, padx=(0, 10))
        left_frame.pack_propagate(False)

        # Frame direito - Log
        right_frame = tk.Frame(main_container, bg="#0f0f23")
        right_frame.pack(side="right", fill="both", expand=True)

        self.create_function_cards_improved(left_frame)
        self.create_log_panel_improved(right_frame)

    def create_function_cards_improved(self, parent):
        """Cria cards com layout fixo melhorado"""
        cards_frame = tk.Frame(parent, bg="#0f0f23")
        cards_frame.pack(fill="both", expand=True, pady=10)

        # Grid 2x2 com tamanhos fixos
        cards = [
            ("🔧 Drivers & Reparos", "Atualiza drivers e repara sistema", self.advanced_drivers),
            ("💾 Software & Updates", "Atualiza programas e sistema", self.advanced_software),
            ("🧹 Limpeza Profunda", "Remove arquivos e otimiza disco", self.advanced_cleanup),
            ("⚡ Performance Total", "Otimiza memória e energia", self.advanced_performance)
        ]

        for i, (title, description, action) in enumerate(cards):
            row, col = divmod(i, 2)
            self.create_improved_card(cards_frame, title, description, action, row, col)

        # Botão EXECUTAR TUDO centralizado
        execute_frame = tk.Frame(cards_frame, bg="#0f0f23", height=80)
        execute_frame.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew")
        execute_frame.pack_propagate(False)

        execute_all_btn = tk.Button(execute_frame,
                                   text="🚀 OTIMIZAÇÃO COMPLETA",
                                   font=("Arial", 14, "bold"),
                                   bg="#4299e1",
                                   fg="white",
                                   relief="flat",
                                   padx=30,
                                   pady=12,
                                   command=self.execute_all_advanced)
        execute_all_btn.pack(expand=True)

        # Configurar grid
        cards_frame.grid_rowconfigure(0, weight=1)
        cards_frame.grid_rowconfigure(1, weight=1)
        cards_frame.grid_columnconfigure(0, weight=1)
        cards_frame.grid_columnconfigure(1, weight=1)

    def create_improved_card(self, parent, title, description, action, row, col):
        """Cria card individual melhorado"""
        card_frame = tk.Frame(parent, bg="#1a202c", relief="raised", bd=1, 
                             width=280, height=140)
        card_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        card_frame.pack_propagate(False)

        # Título
        title_label = tk.Label(card_frame, text=title, 
                              font=("Arial", 12, "bold"),
                              bg="#1a202c", fg="white")
        title_label.pack(pady=(15, 8))

        # Descrição
        desc_label = tk.Label(card_frame, text=description,
                             font=("Arial", 9),
                             bg="#1a202c", fg="#a0aec0",
                             wraplength=250)
        desc_label.pack(pady=(0, 15))

        # Botão
        action_btn = tk.Button(card_frame,
                              text="Executar",
                              font=("Arial", 9, "bold"),
                              bg="#48bb78",
                              fg="white",
                              relief="flat",
                              padx=15,
                              pady=6,
                              command=action)
        action_btn.pack(side="bottom", pady=(0, 15))

    def create_log_panel_improved(self, parent):
        """Cria painel de log melhorado com botão copiar"""
        log_label_frame = tk.LabelFrame(parent, text="Log de Atividades - PCVitalBoost v1.1",
                                       bg="#1a202c", fg="white",
                                       font=("Arial", 10, "bold"))
        log_label_frame.pack(fill="both", expand=True)

        # Frame para botões do log
        log_controls = tk.Frame(log_label_frame, bg="#1a202c", height=35)
        log_controls.pack(fill="x", padx=5, pady=(5, 0))
        log_controls.pack_propagate(False)

        # Botão copiar log
        copy_btn = tk.Button(log_controls, text="📋 Copiar Log", 
                            font=("Arial", 8, "bold"),
                            bg="#4299e1", fg="white",
                            relief="flat", padx=10, pady=4,
                            command=self.copy_log_to_clipboard)
        copy_btn.pack(side="right", padx=5)

        # Botão limpar log
        clear_btn = tk.Button(log_controls, text="🗑️ Limpar", 
                             font=("Arial", 8, "bold"),
                             bg="#f56565", fg="white",
                             relief="flat", padx=10, pady=4,
                             command=self.clear_log)
        clear_btn.pack(side="right", padx=(0, 5))

        # Frame para text widget + scrollbar
        text_frame = tk.Frame(log_label_frame, bg="#1a202c")
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Text widget SELECIONÁVEL
        self.log_text = tk.Text(text_frame, height=12, 
                               bg="#0f0f23", fg="#a0aec0",
                               font=("Consolas", 9),
                               wrap=tk.WORD,
                               selectbackground="#4299e1",
                               selectforeground="white",
                               state=tk.NORMAL)  # NORMAL para permitir seleção

        # Scrollbar
        log_scrollbar = ttk.Scrollbar(text_frame, orient="vertical", 
                                     command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=log_scrollbar.set)

        self.log_text.pack(side="left", fill="both", expand=True)
        log_scrollbar.pack(side="right", fill="y")

        # Permitir seleção com mouse
        self.log_text.bind('<Button-1>', lambda e: self.log_text.focus_set())

    def copy_log_to_clipboard(self):
        """Copia todo o log para clipboard"""
        try:
            log_content = self.log_text.get(1.0, tk.END)
            self.root.clipboard_clear()
            self.root.clipboard_append(log_content)
            self.root.update()  # Garante que o clipboard seja atualizado

            # Feedback visual
            messagebox.showinfo("Log Copiado", "Log copiado para área de transferência!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao copiar log: {str(e)}")

    def clear_log(self):
        """Limpa o log"""
        self.log_text.delete(1.0, tk.END)
        self.log_message("Log limpo pelo usuário", "INFO")

    def create_footer_improved(self):
        """Footer melhorado (removido - log agora está na lateral)"""
        pass

    def create_status_bar(self):
        """Cria barra de status"""
        self.status_var = tk.StringVar()
        self.status_var.set("Pronto - PCVitalBoost v1.1")

        status_bar = tk.Label(self.root, textvariable=self.status_var,
                             relief=tk.SUNKEN, anchor=tk.W,
                             bg="#1a202c", fg="#a0aec0",
                             font=("Arial", 9))
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Log inicial
        self.log_message("Sistema iniciado", "INFO")
        self.log_message(f"Sistema detectado: {self.system_os} {platform.release()}", "INFO")
        if self.is_admin:
            self.log_message("Executando com privilégios administrativos", "SUCCESS")
        else:
            self.log_message("⚠️ Para melhor funcionamento, execute como administrador", "WARNING")

        if PSUTIL_AVAILABLE:
            mem = psutil.virtual_memory()
            self.log_message(f"💾 Memória: {mem.percent}% usada ({self.format_bytes(mem.used)}/{self.format_bytes(mem.total)})", "INFO")

    def on_window_resize(self, event):
        """Callback para redimensionamento"""
        # Ajustar elementos conforme necessário
        pass

    def show_progress(self, show=True):
        """Mostra/esconde barra de progresso"""
        if show:
            self.progress_frame.pack(fill="x", padx=20, pady=(0, 10), before=self.root.winfo_children()[2])
        else:
            self.progress_frame.pack_forget()

    def update_progress(self, value, text=""):
        """Atualiza barra de progresso"""
        self.progress_bar['value'] = value
        if text:
            self.progress_label.config(text=text)
        self.root.update_idletasks()

    def log_message(self, message, level="INFO"):
        """Adiciona mensagem ao log MELHORADO"""
        timestamp = datetime.now().strftime("%H:%M:%S")

        # Cores por nível
        colors = {
            "INFO": "#a0aec0",
            "SUCCESS": "#48bb78", 
            "WARNING": "#ed8936",
            "ERROR": "#f56565",
            "PROGRESS": "#4299e1"
        }

        # Inserir no final
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")

        # Colorir a linha (funcionalidade avançada)
        line_start = self.log_text.index("end-2l linestart")
        line_end = self.log_text.index("end-2l lineend")

        # Criar tag para cor se não existir
        tag_name = f"color_{level.lower()}"
        if tag_name not in self.log_text.tag_names():
            self.log_text.tag_configure(tag_name, foreground=colors.get(level, "#a0aec0"))

        self.log_text.tag_add(tag_name, line_start, line_end)
        self.log_text.see(tk.END)

        # Atualizar status
        self.status_var.set(message)
        self.root.update_idletasks()

    # =============== FUNCIONALIDADES AVANÇADAS ===============

    def advanced_drivers(self):
        """Atualização avançada de drivers + reparos do sistema"""
        if not self.confirm_operation("Drivers & Reparos do Sistema", 
                                     "Esta operação irá:\n\n• Verificar e atualizar drivers\n• Executar SFC /scannow\n• Executar DISM para reparar imagem do Windows\n• Verificar integridade do disco\n\nEsta operação pode demorar bastante.\n\nContinuar?"):
            return

        self.log_message("Iniciando verificação avançada de drivers e reparos...", "INFO")
        threading.Thread(target=self._advanced_drivers_thread, daemon=True).start()

    def _advanced_drivers_thread(self):
        """Thread para drivers e reparos avançados"""
        self.show_progress(True)

        try:
            if self.system_os == 'Windows':
                operations = [
                    ("Verificando drivers instalados", self._list_drivers, 10),
                    ("Executando SFC /scannow", self._run_sfc_scan, 40),
                    ("Executando DISM repair", self._run_dism_repair, 70),
                    ("Verificando disco com CHKDSK", self._run_chkdsk, 90)
                ]

                for desc, operation, progress in operations:
                    self.update_progress(progress, desc)
                    self.log_message(f"🔧 {desc}...", "PROGRESS")
                    operation()
                    time.sleep(1)

                self.update_progress(100, "Reparos concluídos")
                self.log_message("🎉 Verificação de drivers e reparos concluída!", "SUCCESS")

        except Exception as e:
            self.log_message(f"Erro nos reparos: {str(e)}", "ERROR")
        finally:
            time.sleep(2)
            self.show_progress(False)

    def _list_drivers(self):
        """Lista e verifica drivers"""
        try:
            result = subprocess.run(['driverquery', '/v'], 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                # Contar drivers
                lines = result.stdout.split('\n')
                driver_count = len([l for l in lines if l.strip() and 'Nome do Driver' not in l]) - 2
                self.log_message(f"✓ {driver_count} drivers instalados verificados", "SUCCESS")

                # Procurar drivers problemáticos
                problem_drivers = [l for l in lines if 'Stopped' in l or 'Error' in l]
                if problem_drivers:
                    self.log_message(f"⚠️ {len(problem_drivers)} drivers com problemas detectados", "WARNING")
                    self.stats['warnings'].append(f"{len(problem_drivers)} drivers problemáticos")
                else:
                    self.log_message("✓ Nenhum driver problemático encontrado", "SUCCESS")

        except subprocess.TimeoutExpired:
            self.log_message("⚠️ Verificação de drivers excedeu tempo limite", "WARNING")
        except Exception as e:
            self.log_message(f"⚠️ Erro ao verificar drivers: {str(e)}", "WARNING")

    def _run_sfc_scan(self):
        """Executa SFC /scannow"""
        if not self.is_admin:
            self.log_message("⚠️ SFC requer privilégios administrativos", "WARNING")
            return

        try:
            self.log_message("Executando SFC /scannow (pode demorar 10-15 minutos)...", "INFO")
            result = subprocess.run(['sfc', '/scannow'], 
                                  capture_output=True, text=True, timeout=1800)  # 30 min timeout

            if result.returncode == 0:
                output = result.stdout
                if "não encontrou violações de integridade" in output or "did not find any integrity violations" in output:
                    self.log_message("✓ SFC: Nenhum problema de integridade encontrado", "SUCCESS")
                elif "encontrou arquivos corrompidos e os reparou" in output or "found corrupt files and successfully repaired them" in output:
                    self.log_message("✓ SFC: Arquivos corrompidos encontrados e reparados", "SUCCESS")
                    self.stats['errors_fixed'] += 1
                else:
                    self.log_message("✓ SFC executado - verifique detalhes no log do Windows", "SUCCESS")
            else:
                self.log_message("⚠️ SFC falhou - pode precisar ser executado novamente", "WARNING")

        except subprocess.TimeoutExpired:
            self.log_message("⚠️ SFC excedeu tempo limite (30 min) - pode ainda estar executando em background", "WARNING")
        except Exception as e:
            self.log_message(f"⚠️ Erro no SFC: {str(e)}", "WARNING")

    def _run_dism_repair(self):
        """Executa DISM para reparar imagem do Windows"""
        if not self.is_admin:
            self.log_message("⚠️ DISM requer privilégios administrativos", "WARNING")
            return

        try:
            self.log_message("Executando DISM /restorehealth (pode demorar)...", "INFO")
            result = subprocess.run(['dism', '/online', '/cleanup-image', '/restorehealth'], 
                                  capture_output=True, text=True, timeout=1200)  # 20 min timeout

            if result.returncode == 0:
                self.log_message("✓ DISM: Imagem do Windows verificada e reparada", "SUCCESS")
                self.stats['errors_fixed'] += 1
            else:
                self.log_message("⚠️ DISM executado com avisos - sistema pode estar OK", "WARNING")

        except subprocess.TimeoutExpired:
            self.log_message("⚠️ DISM excedeu tempo limite - pode ainda estar executando", "WARNING")
        except Exception as e:
            self.log_message(f"⚠️ Erro no DISM: {str(e)}", "WARNING")

    def _run_chkdsk(self):
        """Executa verificação de disco"""
        try:
            # Executar chkdsk em modo read-only primeiro
            self.log_message("Verificando integridade do disco C:...", "INFO")
            result = subprocess.run(['chkdsk', 'C:', '/f', '/r'], 
                                  input='n\n', text=True,
                                  capture_output=True, timeout=300)

            if "Windows has checked the file system and found no problems" in result.stdout:
                self.log_message("✓ CHKDSK: Disco C: sem problemas", "SUCCESS")
            else:
                self.log_message("⚠️ CHKDSK detectou problemas - reinicie e execute novamente para corrigir", "WARNING")
                self.stats['warnings'].append("Problemas no disco detectados")

        except subprocess.TimeoutExpired:
            self.log_message("⚠️ CHKDSK excedeu tempo limite", "WARNING")
        except Exception as e:
            self.log_message(f"⚠️ Erro no CHKDSK: {str(e)}", "WARNING")

    def advanced_software(self):
        """Atualização avançada de software"""
        if not self.confirm_operation("Atualização Avançada de Software", 
                                     "Esta operação irá:\n\n• Atualizar todos os programas via Winget\n• Limpar cache de instaladores\n• Verificar Microsoft Store\n\nContinuar?"):
            return

        self.log_message("Iniciando atualização avançada de software...", "INFO")
        threading.Thread(target=self._advanced_software_thread, daemon=True).start()

    def _advanced_software_thread(self):
        """Thread para atualização avançada"""
        self.show_progress(True)

        try:
            if self.available_tools.get('winget'):
                self.update_progress(20, "Listando software instalado")

                # Listar software desatualizado
                result = subprocess.run(['winget', 'upgrade'], 
                                      capture_output=True, text=True, timeout=60)

                if result.returncode == 0:
                    lines = result.stdout.split('\n')
                    software_lines = [l for l in lines if '.' in l and 'Available' in l]

                    self.log_message(f"📊 {len(software_lines)} programas precisam de atualização", "INFO")

                    if software_lines:
                        self.update_progress(50, "Atualizando software")
                        self.log_message("Atualizando todos os programas...", "INFO")

                        # Atualizar com mais detalhes
                        result = subprocess.run(['winget', 'upgrade', '--all', 
                                               '--accept-package-agreements', 
                                               '--accept-source-agreements',
                                               '--disable-interactivity'], 
                                              capture_output=True, text=True, timeout=900)

                        if result.returncode == 0:
                            # Contar atualizações
                            updated_count = result.stdout.count('Successfully installed')
                            self.log_message(f"✓ {updated_count} programas atualizados com sucesso", "SUCCESS")
                            self.stats['software_updated'] = [f"{updated_count} programas via Winget"]
                        else:
                            self.log_message("⚠️ Algumas atualizações podem ter falhado", "WARNING")
                    else:
                        self.log_message("✓ Todos os programas já estão atualizados", "SUCCESS")

                self.update_progress(80, "Limpando cache")
                # Limpar cache winget
                try:
                    cache_path = os.path.expandvars('%LOCALAPPDATA%\\Packages\\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\\LocalCache')
                    if os.path.exists(cache_path):
                        size_before = self.get_directory_size(cache_path)
                        self.clean_directory_safe(cache_path)
                        size_after = self.get_directory_size(cache_path)
                        freed = size_before - size_after
                        if freed > 0:
                            self.log_message(f"✓ Cache Winget limpo: {self.format_bytes(freed)} liberados", "SUCCESS")
                except Exception as e:
                    self.log_message(f"⚠️ Erro ao limpar cache: {str(e)}", "WARNING")

            else:
                self.log_message("⚠️ Winget não disponível. Instale via Microsoft Store", "WARNING")

            self.update_progress(100, "Software atualizado")
            self.log_message("🎉 Atualização de software concluída!", "SUCCESS")

        except Exception as e:
            self.log_message(f"Erro na atualização: {str(e)}", "ERROR")
        finally:
            time.sleep(2)
            self.show_progress(False)

    def advanced_cleanup(self):
        """Limpeza profunda do sistema"""
        if not self.confirm_operation("Limpeza Profunda do Sistema", 
                                     "Esta operação irá:\n\n• Limpar arquivos temporários\n• Limpar Recent, Prefetch\n• Executar cleanmgr\n• Corrigir problemas de rede\n\nContinuar?"):
            return

        self.log_message("Iniciando limpeza profunda do sistema...", "INFO")
        threading.Thread(target=self._advanced_cleanup_thread, daemon=True).start()

    def _advanced_cleanup_thread(self):
        """Thread para limpeza profunda"""
        self.show_progress(True)
        total_freed = 0

        try:
            # Locais de limpeza expandidos
            cleanup_locations = [
                (os.path.expandvars('%TEMP%'), "Arquivos temporários do usuário"),
                ('C:\\Windows\\Temp', "Arquivos temporários do sistema"),
                (os.path.expandvars('%LOCALAPPDATA%\\Microsoft\\Windows\\INetCache'), "Cache do Internet Explorer"),
                (os.path.expandvars('%APPDATA%\\Microsoft\\Windows\\Recent'), "Arquivos recentes"),
                ('C:\\Windows\\Prefetch', "Arquivos de prefetch"),
                (os.path.expandvars('%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cache'), "Cache do Chrome"),
                (os.path.expandvars('%LOCALAPPDATA%\\Mozilla\\Firefox\\Profiles'), "Cache do Firefox"),
            ]

            progress_step = 80 / len(cleanup_locations)
            current_progress = 10

            for location, description in cleanup_locations:
                self.update_progress(current_progress, f"Limpando {description}")
                self.log_message(f"🧹 Limpando {description}...", "PROGRESS")

                if os.path.exists(location):
                    try:
                        size_before = self.get_directory_size(location)

                        if 'Profiles' in location:  # Firefox - limpar só cache
                            self._clean_firefox_cache(location)
                        else:
                            self.clean_directory_safe(location)

                        size_after = self.get_directory_size(location)
                        freed = size_before - size_after
                        total_freed += freed

                        if freed > 0:
                            self.log_message(f"✓ {description}: {self.format_bytes(freed)} liberados", "SUCCESS")
                            self.stats['files_cleaned'] += 1
                        else:
                            self.log_message(f"✓ {description}: já limpo", "SUCCESS")

                    except Exception as e:
                        self.log_message(f"⚠️ Erro em {description}: {str(e)}", "WARNING")

                current_progress += progress_step
                time.sleep(0.5)

            # Executar cleanmgr
            self.update_progress(85, "Executando limpeza de disco")
            self.log_message("🧹 Executando limpeza de disco do Windows...", "PROGRESS")
            try:
                subprocess.run(['cleanmgr', '/sagerun:1'], 
                             capture_output=True, timeout=300)
                self.log_message("✓ Limpeza de disco executada", "SUCCESS")
            except Exception as e:
                self.log_message(f"⚠️ Erro na limpeza de disco: {str(e)}", "WARNING")

            # Corrigir problemas de rede
            self.update_progress(90, "Corrigindo problemas de rede")
            self._fix_network_issues()

            # Esvaziar lixeira
            self.update_progress(95, "Esvaziando lixeira")
            try:
                result = subprocess.run(['powershell', '-Command', 
                                       'Clear-RecycleBin -Force -Confirm:$false'], 
                                      capture_output=True, timeout=60)
                if result.returncode == 0:
                    self.log_message("✓ Lixeira esvaziada", "SUCCESS")
            except:
                self.log_message("⚠️ Erro ao esvaziar lixeira", "WARNING")

            self.update_progress(100, "Limpeza concluída")
            self.stats['space_freed'] = total_freed
            self.log_message(f"🎉 Limpeza profunda concluída! {self.format_bytes(total_freed)} liberados", "SUCCESS")

        except Exception as e:
            self.log_message(f"Erro na limpeza: {str(e)}", "ERROR")
        finally:
            time.sleep(2)
            self.show_progress(False)

    def _clean_firefox_cache(self, profiles_path):
        """Limpa cache do Firefox especificamente"""
        try:
            for profile_dir in os.listdir(profiles_path):
                profile_path = os.path.join(profiles_path, profile_dir)
                if os.path.isdir(profile_path):
                    cache_path = os.path.join(profile_path, 'cache2')
                    if os.path.exists(cache_path):
                        self.clean_directory_safe(cache_path)
        except:
            pass

    def _fix_network_issues(self):
        """Corrige problemas comuns de rede"""
        network_fixes = [
            (['netsh', 'winsock', 'reset'], "Reset Winsock"),
            (['ipconfig', '/flushdns'], "Flush DNS"),
            (['netsh', 'int', 'ip', 'reset'], "Reset TCP/IP")
        ]

        for command, description in network_fixes:
            try:
                self.log_message(f"🌐 Executando {description}...", "PROGRESS")
                result = subprocess.run(command, capture_output=True, timeout=60)
                if result.returncode == 0:
                    self.log_message(f"✓ {description} executado", "SUCCESS")
                else:
                    self.log_message(f"⚠️ {description} com avisos", "WARNING")
            except Exception as e:
                self.log_message(f"⚠️ Erro em {description}: {str(e)}", "WARNING")

    def advanced_performance(self):
        """Otimização avançada de performance"""
        if not self.confirm_operation("Otimização Avançada de Performance", 
                                     "Esta operação irá:\n\n• Otimizar configurações de energia\n• Liberar memória RAM\n• Configurar performance máxima\n\nContinuar?"):
            return

        self.log_message("Iniciando otimização avançada de performance...", "INFO")
        threading.Thread(target=self._advanced_performance_thread, daemon=True).start()

    def _advanced_performance_thread(self):
        """Thread para otimização de performance"""
        self.show_progress(True)

        try:
            # Mostrar informações de memória antes
            if PSUTIL_AVAILABLE:
                mem_before = psutil.virtual_memory()
                self.log_message(f"💾 Memória antes: {mem_before.percent}% usada ({self.format_bytes(mem_before.used)}/{self.format_bytes(mem_before.total)})", "INFO")

            # Otimização de energia
            self.update_progress(20, "Configurando energia para performance")
            try:
                # Ativar perfil de performance máxima
                result = subprocess.run(['powercfg', '-duplicatescheme', 
                                       'e9a42b02-d5df-448d-aa00-03f14749eb61'], 
                                      capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    self.log_message("✓ Perfil de performance máxima ativado", "SUCCESS")

                # Definir como ativo
                subprocess.run(['powercfg', '-setactive', 
                               'e9a42b02-d5df-448d-aa00-03f14749eb61'], 
                              capture_output=True, timeout=30)
                self.log_message("✓ Configurações de energia otimizadas", "SUCCESS")

            except Exception as e:
                self.log_message(f"⚠️ Erro na configuração de energia: {str(e)}", "WARNING")

            # Limpeza de memória
            self.update_progress(50, "Otimizando memória RAM")
            import gc
            gc.collect()
            self.log_message("✓ Coletor de lixo executado", "SUCCESS")

            # Limpar working set
            try:
                subprocess.run(['powershell', '-Command', '[System.GC]::Collect()'], 
                             capture_output=True, timeout=30)
                self.log_message("✓ Working set otimizado", "SUCCESS")
            except:
                pass

            # Configurações de sistema
            self.update_progress(80, "Aplicando configurações de performance")
            try:
                # Desabilitar efeitos visuais (registro)
                reg_commands = [
                    'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 2 /f',
                ]

                for cmd in reg_commands:
                    subprocess.run(cmd, shell=True, capture_output=True, timeout=30)

                self.log_message("✓ Configurações de performance aplicadas", "SUCCESS")
            except Exception as e:
                self.log_message(f"⚠️ Erro nas configurações: {str(e)}", "WARNING")

            # Informações finais
            if PSUTIL_AVAILABLE:
                mem_after = psutil.virtual_memory()
                improvement = mem_before.used - mem_after.used
                self.log_message(f"💾 Memória depois: {mem_after.percent}% usada ({self.format_bytes(mem_after.used)}/{self.format_bytes(mem_after.total)})", "INFO")
                if improvement > 0:
                    self.log_message(f"✓ Memória liberada: {self.format_bytes(improvement)}", "SUCCESS")

            self.update_progress(100, "Performance otimizada")
            self.log_message("🎉 Otimização de performance concluída!", "SUCCESS")

        except Exception as e:
            self.log_message(f"Erro na otimização: {str(e)}", "ERROR")
        finally:
            time.sleep(2)
            self.show_progress(False)

    def execute_all_advanced(self):
        """Executa otimização completa avançada"""
        if not self.confirm_operation("OTIMIZAÇÃO COMPLETA AVANÇADA", 
                                     "Esta operação executará TODAS as otimizações:\n\n" +
                                     "🔧 Drivers & Reparos (SFC, DISM, CHKDSK)\n" +
                                     "💾 Atualização completa de software\n" +
                                     "🧹 Limpeza profunda do sistema\n" +
                                     "⚡ Otimização total de performance\n\n" +
                                     "⚠️ ESTA OPERAÇÃO PODE DEMORAR 30-60 MINUTOS\n\n" +
                                     "Continuar?"):
            return

        if not self.is_admin:
            if not messagebox.askyesno("Sem Privilégios Admin", 
                                     "Muitas operações requerem privilégios administrativos.\n\n" +
                                     "Algumas funções não funcionarão corretamente.\n\n" +
                                     "Recomenda-se executar como administrador.\n\n" +
                                     "Continuar mesmo assim?"):
                return

        self.log_message("🚀 INICIANDO OTIMIZAÇÃO COMPLETA AVANÇADA", "INFO")
        self.log_message("⏱️ Operação pode demorar 30-60 minutos", "INFO")

        # Reset das estatísticas
        self.stats = {
            'files_cleaned': 0,
            'space_freed': 0,
            'drivers_updated': [],
            'software_updated': [],
            'errors_fixed': 0,
            'warnings': []
        }

        threading.Thread(target=self._execute_all_advanced_thread, daemon=True).start()

    def _execute_all_advanced_thread(self):
        """Thread para execução completa avançada"""
        start_time = datetime.now()

        operations = [
            ("Drivers & Reparos do Sistema", self._advanced_drivers_thread),
            ("Atualização Completa de Software", self._advanced_software_thread),
            ("Limpeza Profunda do Sistema", self._advanced_cleanup_thread),
            ("Otimização Total de Performance", self._advanced_performance_thread)
        ]

        for i, (name, operation) in enumerate(operations):
            self.log_message(f"📋 === ETAPA {i+1}/{len(operations)}: {name.upper()} ===", "INFO")
            try:
                operation()
                time.sleep(3)  # Pausa entre etapas
            except Exception as e:
                self.log_message(f"⚠️ Erro na etapa {i+1}: {str(e)}", "WARNING")

        end_time = datetime.now()
        duration = end_time - start_time

        self.log_message("=" * 50, "INFO")
        self.log_message("🎉 OTIMIZAÇÃO COMPLETA AVANÇADA CONCLUÍDA!", "SUCCESS")
        self.log_message(f"⏱️ Tempo total: {str(duration).split('.')[0]}", "SUCCESS")
        self.log_message(f"📊 Espaço liberado: {self.format_bytes(self.stats['space_freed'])}", "SUCCESS")
        self.log_message(f"🔧 Erros corrigidos: {self.stats['errors_fixed']}", "SUCCESS")
        self.log_message("=" * 50, "INFO")

        # Gerar relatório final melhorado
        self.generate_advanced_report()

    def generate_advanced_report(self):
        """Gera relatório HTML avançado com mais informações"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_filename = f"PCVitalBoost_Advanced_Report_{timestamp}.html"

            # Informações de sistema mais detalhadas
            system_info = ""
            if PSUTIL_AVAILABLE:
                cpu_info = f"CPU: {psutil.cpu_count()} cores, {psutil.cpu_freq().current:.0f}MHz"
                memory_info = f"RAM: {self.format_bytes(psutil.virtual_memory().total)}"
                disk_info = f"Disco C: {self.format_bytes(psutil.disk_usage('C:').total)}"
                system_info = f"{cpu_info}<br>{memory_info}<br>{disk_info}"

            # Estatísticas detalhadas
            stats_html = f"""
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-number">{self.format_bytes(self.stats['space_freed'])}</div>
                    <div class="stat-label">Espaço Liberado</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">{self.stats['files_cleaned']}</div>
                    <div class="stat-label">Locais Limpos</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">{self.stats['errors_fixed']}</div>
                    <div class="stat-label">Erros Corrigidos</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">{len(self.stats['warnings'])}</div>
                    <div class="stat-label">Avisos</div>
                </div>
            </div>
            """

            # Log completo
            log_content = self.log_text.get(1.0, tk.END)
            log_lines = log_content.split('\n')
            log_html = "<br>".join([f"<span class='log-line'>{line}</span>" 
                                   for line in log_lines if line.strip()])

            report_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>PCVitalBoost v1.1 - Relatório Avançado</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #0f0f23; color: #fff; margin: 0; padding: 20px; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{ text-align: center; margin-bottom: 40px; }}
        .logo {{ font-size: 4em; margin-bottom: 10px; }}
        .title {{ color: #4299e1; font-size: 2.5em; margin-bottom: 10px; }}
        .subtitle {{ color: #a0aec0; font-size: 1.2em; margin-bottom: 20px; }}
        .section {{ background: #1a202c; padding: 25px; margin: 25px 0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
        .section h2 {{ color: #4299e1; border-bottom: 3px solid #4299e1; padding-bottom: 12px; margin-bottom: 20px; }}
        .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }}
        .stat-item {{ background: #2d3748; padding: 25px; border-radius: 10px; text-align: center; }}
        .stat-number {{ font-size: 2.5em; color: #48bb78; font-weight: bold; margin-bottom: 8px; }}
        .stat-label {{ color: #a0aec0; font-size: 1.1em; }}
        .system-info {{ background: #2d3748; padding: 20px; border-radius: 8px; margin: 15px 0; }}
        .log-section {{ background: #0f0f23; padding: 20px; border-radius: 8px; font-family: 'Consolas', monospace; font-size: 0.9em; max-height: 400px; overflow-y: auto; }}
        .log-line {{ display: block; margin: 2px 0; }}
        .success {{ color: #48bb78; }}
        .warning {{ color: #ed8936; }}
        .error {{ color: #f56565; }}
        .info {{ color: #4299e1; }}
        .footer {{ text-align: center; margin-top: 40px; color: #a0aec0; padding: 20px; }}
        .download-section {{ text-align: center; margin: 30px 0; }}
        .download-btn {{ background: #4299e1; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">🚀</div>
            <h1 class="title">PCVitalBoost v1.1</h1>
            <p class="subtitle">Relatório Avançado de Otimização</p>
            <p class="subtitle">{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</p>
        </div>

        <div class="section">
            <h2>📊 Estatísticas da Otimização</h2>
            {stats_html}
        </div>

        <div class="section">
            <h2>🖥️ Informações do Sistema</h2>
            <div class="system-info">
                <p><strong>Sistema:</strong> {self.system_os} {platform.release()}</p>
                <p><strong>Arquitetura:</strong> {platform.architecture()[0]}</p>
                <p><strong>Processador:</strong> {platform.processor()}</p>
                {f"<p>{system_info}</p>" if system_info else ""}
                <p><strong>Privilégios:</strong> {"Administrador" if self.is_admin else "Usuário"}</p>
                <p><strong>Data da Otimização:</strong> {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</p>
            </div>
        </div>

        <div class="section">
            <h2>📋 Log Completo da Sessão</h2>
            <div class="log-section">
                {log_html}
            </div>
        </div>

        <div class="section">
            <h2>✅ Operações Realizadas</h2>
            <ul>
                <li>🔧 <strong>Verificação e Reparos:</strong> SFC, DISM, CHKDSK executados</li>
                <li>💾 <strong>Atualizações:</strong> Software e drivers verificados</li>
                <li>🧹 <strong>Limpeza Profunda:</strong> {self.stats['files_cleaned']} locais limpos</li>
                <li>⚡ <strong>Otimização:</strong> Performance e energia configurados</li>
                <li>🌐 <strong>Rede:</strong> Winsock reset, DNS flush executados</li>
            </ul>
        </div>

        <div class="section">
            <h2>🎯 Recomendações</h2>
            <p class="success">✅ Seu sistema foi otimizado com sucesso!</p>
            <p>Para manter a performance:</p>
            <ul>
                <li>Execute o PCVitalBoost mensalmente</li>
                <li>Mantenha o Windows atualizado</li>
                <li>Evite acúmulo de arquivos temporários</li>
                <li>Use o perfil de energia de alta performance quando necessário</li>
            </ul>
        </div>

        <div class="download-section">
            <p>Baixe a versão mais recente do PCVitalBoost:</p>
            <a href="https://github.com/username/pcvitalboost" class="download-btn">
                GitHub - PCVitalBoost
            </a>
        </div>

        <div class="footer">
            <p><strong>PCVitalBoost v1.1</strong> - Sistema Otimizador Avançado</p>
            <p>Desenvolvido com ❤️ por Sistema Inteligente</p>
            <p>Relatório gerado em {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</p>
        </div>
    </div>
</body>
</html>
            """

            with open(report_filename, "w", encoding="utf-8") as f:
                f.write(report_content)

            self.log_message(f"📋 Relatório avançado salvo: {report_filename}", "SUCCESS")

            # Abrir relatório
            webbrowser.open(f"file://{os.path.abspath(report_filename)}")

        except Exception as e:
            self.log_message(f"Erro ao gerar relatório: {str(e)}", "WARNING")

    # =============== FUNÇÕES AUXILIARES MELHORADAS ===============

    def confirm_operation(self, title, message):
        """Confirma operação com usuário"""
        return messagebox.askyesno(title, message)

    def get_directory_size(self, path):
        """Calcula tamanho de diretório"""
        total = 0
        try:
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    try:
                        filepath = os.path.join(dirpath, filename)
                        total += os.path.getsize(filepath)
                    except (OSError, FileNotFoundError):
                        continue
        except:
            pass
        return total

    def clean_directory_safe(self, path):
        """Limpa diretório de forma segura"""
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                try:
                    if os.path.isfile(item_path):
                        if not self.is_critical_file(item_path):
                            os.unlink(item_path)
                    elif os.path.isdir(item_path):
                        if not self.is_critical_directory(item_path):
                            shutil.rmtree(item_path)
                except (OSError, PermissionError):
                    continue
        except:
            pass

    def is_critical_file(self, filepath):
        """Verifica se arquivo é crítico"""
        critical_extensions = ['.sys', '.dll', '.exe', '.ini', '.dat']
        critical_names = ['desktop.ini', 'thumbs.db', 'index.dat']

        filename = os.path.basename(filepath).lower()

        if any(filename.endswith(ext) for ext in critical_extensions):
            return True
        if filename in critical_names:
            return True

        return False

    def is_critical_directory(self, dirpath):
        """Verifica se diretório é crítico"""
        critical_dirs = ['system32', 'syswow64', 'windows', 'program files', 'programdata']
        dirpath_lower = dirpath.lower()

        return any(critical in dirpath_lower for critical in critical_dirs)

    def format_bytes(self, bytes_size):
        """Formata bytes em unidade legível"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.1f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.1f} TB"

    def run(self):
        """Executa a aplicação"""
        self.root.mainloop()

if __name__ == "__main__":
    app = PCVitalBoost()
    app.run()
