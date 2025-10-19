"""
Testes para o módulo DropboxImporter
"""
import sys
import os
import unittest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestDropboxImporter(unittest.TestCase):
    """Testes para o módulo DropboxImporter"""
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def setUp(self, mock_dropbox):
        """Configura teste"""
        self.mock_dropbox = mock_dropbox
        from src.modules.dropbox_importer import DropboxImporter
        self.DropboxImporter = DropboxImporter
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def test_initialization(self, mock_dropbox):
        """Testa inicialização do módulo"""
        with patch.dict(os.environ, {'DROPBOX_APP_KEY': 'test_key'}):
            importer = self.DropboxImporter()
            self.assertIsNotNone(importer)
            self.assertEqual(importer.app_key, 'test_key')
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def test_initialization_with_params(self, mock_dropbox):
        """Testa inicialização com parâmetros"""
        importer = self.DropboxImporter(app_key='custom_key', app_secret='custom_secret')
        self.assertEqual(importer.app_key, 'custom_key')
        self.assertEqual(importer.app_secret, 'custom_secret')
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', False)
    def test_initialization_without_dropbox_sdk(self):
        """Testa que lança erro se SDK não está disponível"""
        # Este teste verifica que a classe DropboxImporter lança ImportError
        # quando DROPBOX_AVAILABLE é False
        # Como já foi importada, vamos apenas verificar que levanta o erro ao instanciar
        try:
            from src.modules.dropbox_importer import DropboxImporter
            # Força o módulo a pensar que dropbox não está disponível
            with patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', False):
                with self.assertRaises(ImportError):
                    # Cria nova instância que deve verificar DROPBOX_AVAILABLE
                    importer = DropboxImporter(app_key='test_key')
        except ImportError:
            # Se já falhou ao importar, o teste passou
            pass
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def test_is_authenticated_false(self, mock_dropbox):
        """Testa verificação de autenticação quando não autenticado"""
        importer = self.DropboxImporter(app_key='test_key')
        self.assertFalse(importer.is_authenticated())
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def test_is_authenticated_true(self, mock_dropbox):
        """Testa verificação de autenticação quando autenticado"""
        importer = self.DropboxImporter(app_key='test_key')
        importer.dbx = Mock()
        self.assertTrue(importer.is_authenticated())
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    @patch('src.modules.dropbox_importer.DropboxOAuth2FlowNoRedirect')
    @patch('src.modules.dropbox_importer.webbrowser.open')
    def test_authenticate(self, mock_webbrowser, mock_flow_class, mock_dropbox):
        """Testa início do processo de autenticação"""
        mock_auth_flow = Mock()
        mock_auth_flow.start.return_value = 'https://www.dropbox.com/oauth2/authorize'
        mock_flow_class.return_value = mock_auth_flow
        
        importer = self.DropboxImporter(app_key='test_key')
        result = importer.authenticate()
        
        self.assertTrue(result)
        mock_webbrowser.assert_called_once()
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    @patch('src.modules.dropbox_importer.DropboxOAuth2FlowNoRedirect')
    def test_complete_authentication(self, mock_flow_class, mock_dropbox):
        """Testa conclusão do processo de autenticação"""
        mock_auth_flow = Mock()
        mock_oauth_result = Mock()
        mock_oauth_result.access_token = 'test_token'
        mock_auth_flow.finish.return_value = mock_oauth_result
        mock_flow_class.return_value = mock_auth_flow
        
        importer = self.DropboxImporter(app_key='test_key')
        
        with patch.object(importer, '_save_token'):
            result = importer.complete_authentication('test_code')
        
        self.assertTrue(result)
        self.assertEqual(importer.access_token, 'test_token')
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def test_list_files_not_authenticated(self, mock_dropbox):
        """Testa listagem de arquivos sem autenticação"""
        importer = self.DropboxImporter(app_key='test_key')
        files = importer.list_files()
        self.assertEqual(files, [])
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def test_list_files_authenticated(self, mock_dropbox):
        """Testa listagem de arquivos com autenticação"""
        # Mock arquivo e pasta
        mock_file = Mock()
        mock_file.name = 'test.txt'
        mock_file.path_display = '/test.txt'
        mock_file.size = 1024
        mock_file.client_modified = None
        
        mock_folder = Mock()
        mock_folder.name = 'Documents'
        mock_folder.path_display = '/Documents'
        
        mock_result = Mock()
        mock_result.entries = [mock_file, mock_folder]
        
        mock_dbx = Mock()
        mock_dbx.files_list_folder.return_value = mock_result
        
        # Mock classes de tipos de arquivo
        file_meta_class = type('FileMetadata', (), {})
        folder_meta_class = type('FolderMetadata', (), {})
        mock_dropbox.files.FileMetadata = file_meta_class
        mock_dropbox.files.FolderMetadata = folder_meta_class
        
        # Adiciona tipo aos mocks
        mock_file.__class__ = file_meta_class
        mock_folder.__class__ = folder_meta_class
        
        importer = self.DropboxImporter(app_key='test_key')
        importer.dbx = mock_dbx
        
        files = importer.list_files()
        
        self.assertEqual(len(files), 2)
        self.assertEqual(files[0]['name'], 'test.txt')
        self.assertEqual(files[0]['type'], 'file')
        self.assertEqual(files[1]['name'], 'Documents')
        self.assertEqual(files[1]['type'], 'folder')
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def test_download_file_not_authenticated(self, mock_dropbox):
        """Testa download de arquivo sem autenticação"""
        importer = self.DropboxImporter(app_key='test_key')
        result = importer.download_file('/test.txt', '/tmp/test.txt')
        self.assertFalse(result)
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def test_download_file_authenticated(self, mock_dropbox):
        """Testa download de arquivo com autenticação"""
        mock_dbx = Mock()
        mock_dbx.files_download_to_file.return_value = None
        
        importer = self.DropboxImporter(app_key='test_key')
        importer.dbx = mock_dbx
        
        with patch('pathlib.Path.mkdir'):
            result = importer.download_file('/test.txt', '/tmp/test.txt')
        
        self.assertTrue(result)
        mock_dbx.files_download_to_file.assert_called_once()
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def test_import_file(self, mock_dropbox):
        """Testa importação de arquivo"""
        mock_dbx = Mock()
        mock_dbx.files_download_to_file.return_value = None
        
        importer = self.DropboxImporter(app_key='test_key')
        importer.dbx = mock_dbx
        
        with patch('pathlib.Path.mkdir'):
            result = importer.import_file('/test.txt')
        
        self.assertIsNotNone(result)
        self.assertIn('test.txt', result)
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def test_get_account_info(self, mock_dropbox):
        """Testa obtenção de informações da conta"""
        mock_account = Mock()
        mock_account.name.display_name = 'Test User'
        mock_account.email = 'test@example.com'
        mock_account.account_id = '12345'
        
        mock_dbx = Mock()
        mock_dbx.users_get_current_account.return_value = mock_account
        
        importer = self.DropboxImporter(app_key='test_key')
        importer.dbx = mock_dbx
        
        info = importer.get_account_info()
        
        self.assertIsNotNone(info)
        self.assertEqual(info['name'], 'Test User')
        self.assertEqual(info['email'], 'test@example.com')
    
    @patch('src.modules.dropbox_importer.DROPBOX_AVAILABLE', True)
    @patch('src.modules.dropbox_importer.dropbox')
    def test_disconnect(self, mock_dropbox):
        """Testa desconexão"""
        importer = self.DropboxImporter(app_key='test_key')
        importer.access_token = 'test_token'
        importer.dbx = Mock()
        
        with patch.object(Path, 'exists', return_value=False):
            importer.disconnect()
        
        self.assertIsNone(importer.access_token)
        self.assertIsNone(importer.dbx)


if __name__ == '__main__':
    unittest.main()
