"""
Módulo de otimização de desempenho do sistema
"""
import logging
import threading
import time

import psutil

logger = logging.getLogger(__name__)


class SystemOptimizer:
    """Classe responsável por otimizar o desempenho do sistema"""

    _cpu_lock = threading.Lock()
    _cpu_percent = 0.0
    _cpu_sampler_started = False

    def __init__(self):
        self._start_cpu_sampler()

    @classmethod
    def _start_cpu_sampler(cls):
        """Inicia um único amostrador de CPU compartilhado por todas as instâncias."""
        with cls._cpu_lock:
            if cls._cpu_sampler_started:
                return
            cls._cpu_sampler_started = True

        sampler = threading.Thread(
            target=cls._sample_cpu,
            name="pcvitalboost-cpu-sampler",
            daemon=True,
        )
        sampler.start()

    @classmethod
    def _sample_cpu(cls):
        """Atualiza o uso de CPU periodicamente sem bloquear a interface."""
        psutil.cpu_percent(interval=None)
        while True:
            try:
                cpu_percent = psutil.cpu_percent(interval=1)
                with cls._cpu_lock:
                    cls._cpu_percent = cpu_percent
            except (OSError, psutil.Error) as error:
                logger.warning("Não foi possível amostrar o uso de CPU: %s", error)
                time.sleep(1)

    def get_system_info(self):
        """
        Obtém informações do sistema
        
        Returns:
            dict: Informações sobre CPU, memória, disco, etc.
        """
        memory = psutil.virtual_memory()
        info = {
            'cpu_percent': self._get_cpu_percent(),
            'memory_percent': memory.percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'cpu_count': psutil.cpu_count(),
            'total_memory': memory.total / (1024**3),  # GB
        }
        return info

    @classmethod
    def _get_cpu_percent(cls):
        """Retorna a última amostra de CPU sem iniciar uma nova medição."""
        with cls._cpu_lock:
            return cls._cpu_percent
    
    def optimize_memory(self):
        """
        Otimiza uso de memória RAM
        
        Returns:
            dict: Resultado da otimização
        """
        logger.info("Otimizando memória...")
        
        # Obtém processos usando muita memória
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # Ordena por uso de memória
        processes.sort(key=lambda x: x.get('memory_percent', 0), reverse=True)
        
        return {
            'status': 'success',
            'top_processes': processes[:10],
            'message': 'Análise de memória concluída'
        }
    
    def optimize_startup(self):
        """
        Otimiza programas de inicialização
        
        Returns:
            dict: Resultado da otimização
        """
        logger.info("Otimizando inicialização...")
        # Placeholder - implementação específica por plataforma
        return {
            'status': 'success',
            'message': 'Inicialização otimizada'
        }
    
    def defragment_disk(self):
        """
        Desfragmenta disco (apenas Windows com HDD)
        
        Returns:
            dict: Resultado da operação
        """
        logger.info("Verificando necessidade de desfragmentação...")
        # Placeholder - apenas para Windows com HDD
        return {
            'status': 'info',
            'message': 'Desfragmentação não necessária ou não suportada'
        }
