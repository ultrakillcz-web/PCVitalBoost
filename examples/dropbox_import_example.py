#!/usr/bin/env python3
"""
Exemplo de uso do módulo DropboxImporter
Este script demonstra como importar arquivos do Dropbox
"""

import sys
import os

# Adiciona o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.modules import DropboxImporter


def example_dropbox_import():
    """Exemplo: Importar arquivo do Dropbox"""
    print("\n=== Importando do Dropbox ===")
    
    # Nota: Para usar este exemplo, você precisa:
    # 1. Criar uma aplicação no Dropbox App Console (https://www.dropbox.com/developers/apps)
    # 2. Definir DROPBOX_APP_KEY e DROPBOX_APP_SECRET como variáveis de ambiente
    # Ou passar diretamente:
    # importer = DropboxImporter(app_key='sua_chave', app_secret='seu_segredo')
    
    try:
        importer = DropboxImporter()
        
        # Verifica se já está autenticado
        if not importer.is_authenticated():
            print("Iniciando autenticação...")
            if importer.authenticate():
                print("\nPor favor, autorize o aplicativo no navegador que foi aberto.")
                print("Após autorizar, você receberá um código.")
                auth_code = input("Cole o código de autorização aqui: ").strip()
                
                if importer.complete_authentication(auth_code):
                    print("✓ Autenticação bem-sucedida!")
                else:
                    print("✗ Falha na autenticação")
                    return
            else:
                print("✗ Erro ao iniciar autenticação")
                print("Certifique-se de definir DROPBOX_APP_KEY")
                return
        else:
            print("✓ Já autenticado no Dropbox")
        
        # Obter informações da conta
        account_info = importer.get_account_info()
        if account_info:
            print(f"\nConta: {account_info['name']}")
            print(f"Email: {account_info['email']}")
        
        # Listar arquivos na raiz
        print("\nListando arquivos...")
        files = importer.list_files()
        
        if files:
            print(f"Encontrados {len(files)} itens:")
            for i, file in enumerate(files[:10], 1):  # Mostra primeiros 10
                file_type = "📁" if file['type'] == 'folder' else "📄"
                name = file['name']
                size = f" ({file['size']} bytes)" if file.get('size') else ""
                print(f"{i}. {file_type} {name}{size}")
            
            # Exemplo de importação de arquivo
            # Filtra apenas arquivos (não pastas)
            file_list = [f for f in files if f['type'] == 'file']
            
            if file_list:
                print("\nPara importar um arquivo:")
                print("1. Escolha um número da lista acima")
                choice = input("Número do arquivo para importar (ou 'n' para pular): ").strip()
                
                if choice.lower() != 'n' and choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(files):
                        selected_file = files[idx]
                        if selected_file['type'] == 'file':
                            print(f"\nImportando {selected_file['name']}...")
                            local_path = importer.import_file(selected_file['path'])
                            
                            if local_path:
                                print(f"✓ Arquivo importado com sucesso!")
                                print(f"Localização: {local_path}")
                            else:
                                print("✗ Falha ao importar arquivo")
                        else:
                            print("✗ Item selecionado é uma pasta, não um arquivo")
                    else:
                        print("✗ Número inválido")
            else:
                print("\nNenhum arquivo disponível para importar (apenas pastas)")
        else:
            print("Nenhum arquivo encontrado no Dropbox")
        
        # Opção de desconectar
        disconnect = input("\nDeseja desconectar do Dropbox? (s/n): ").strip().lower()
        if disconnect == 's':
            importer.disconnect()
            print("✓ Desconectado do Dropbox")
            
    except ImportError as e:
        print(f"\n✗ Erro: {e}")
        print("Execute: pip install dropbox")
    except Exception as e:
        print(f"\n✗ Erro: {e}")


def main():
    """Função principal"""
    print("PCVitalBoost - Exemplo de Importação do Dropbox")
    print("=" * 60)
    
    example_dropbox_import()
    
    print("\n" + "=" * 60)
    print("Exemplo concluído!")


if __name__ == '__main__':
    main()
