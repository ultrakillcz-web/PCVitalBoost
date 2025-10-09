import os
import sys
import subprocess
import shutil

class PCVitalBoostBuilder:
    def __init__(self):
        self.app_name = "PCVitalBoost"
        self.version = "1.1.0"
        self.main_file = "PCVitalBoost_v1.1_ADVANCED.py"

    def build(self):
        print(f"=== BUILD {self.app_name} v{self.version} ===")

        # Limpar builds anteriores
        print("Limpando...")
        for dir_name in ["build", "dist", "__pycache__"]:
            if os.path.exists(dir_name):
                shutil.rmtree(dir_name)

        # Instalar dependências
        print("Instalando dependências...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller", "psutil"])

        # Verificar arquivo principal
        if not os.path.exists(self.main_file):
            print(f"ERRO: {self.main_file} não encontrado!")
            return False

        # Criar executável
        print("Criando executável...")
        cmd = [
            "pyinstaller", "--onefile", "--windowed", "--clean",
            f"--name={self.app_name}_v1.1", self.main_file
        ]

        result = subprocess.run(cmd, capture_output=True)
        if result.returncode != 0:
            print("ERRO na criação do executável")
            return False

        # Criar pacote
        print("Criando pacote...")
        exe_path = f"dist/{self.app_name}_v1.1.exe"
        package_dir = f"release/{self.app_name}_v1.1_Portable"
        os.makedirs(package_dir, exist_ok=True)

        # Copiar executável
        shutil.copy2(exe_path, f"{package_dir}/{self.app_name}.exe")

        # Criar README
        readme = f"""# PCVitalBoost v{self.version}

## Como Usar
1. Execute PCVitalBoost.exe
2. Para melhor resultado, execute como administrador

## Melhorias v1.1
- Interface 1200x900 sem sobreposição
- Botão Copiar Log funcional
- Comandos avançados: SFC, DISM, CHKDSK
- Limpeza profunda com recent e prefetch
- Correções de rede (netsh, ipconfig)
- Otimização de energia (powercfg)
- Barra de progresso real
- Relatório HTML detalhado

Desenvolvido por Sistema Inteligente - 2025
"""

        with open(f"{package_dir}/README.md", "w", encoding="utf-8") as f:
            f.write(readme)

        # Criar batch para admin
        batch_content = """@echo off
echo PCVitalBoost v1.1 - Modo Administrador
echo.
echo Execute como administrador para melhor funcionamento
pause
powershell -Command "Start-Process -FilePath '%~dp0PCVitalBoost.exe' -Verb RunAs"
"""

        with open(f"{package_dir}/PCVitalBoost_Admin.bat", "w") as f:
            f.write(batch_content)

        print("\n=== BUILD CONCLUÍDO ===")
        print(f"Executável: {package_dir}/PCVitalBoost.exe")
        print("Batch Admin: PCVitalBoost_Admin.bat")
        return True

if __name__ == "__main__":
    builder = PCVitalBoostBuilder()
    success = builder.build()

    if success:
        print("\n✅ SUCESSO! Arquivos prontos em release/")
    else:
        print("\n❌ BUILD FALHOU")

    input("Pressione Enter para sair...")
