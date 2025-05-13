from .variables import (
    connectivity, speed, server_access, wifi_signal, dns_errors,
    isp_failure, cable_damage, router_problem, dns_config, wifi_coverage,
    linguistic_to_numeric, recommendations
)
from .rules import network_diagnosis

class NetworkDiagnosisSystem:
    def __init__(self):
        self.simulator = network_diagnosis

    def _get_numeric_value(self, symptom_type, linguistic_value):
        """Convierte un valor lingüístico a su equivalente numérico."""
        return linguistic_to_numeric[symptom_type][linguistic_value]

    def _get_recommendation(self, cause, value):
        """Obtiene la recomendación basada en la causa y su valor."""
        if value < 33:
            level = 'baja'
        elif value < 66:
            level = 'media'
        else:
            level = 'alta'
        return recommendations[cause][level]

    def diagnose(self, symptoms):
        """
        Realiza el diagnóstico basado en los síntomas proporcionados.
        
        Args:
            symptoms (dict): Diccionario con los síntomas y sus valores lingüísticos
                {
                    'conectividad': 'nula'|'baja'|'media'|'buena',
                    'velocidad': 'lenta'|'moderada'|'rápida',
                    'acceso_servidor': 'inaccesible'|'lento'|'fluido',
                    'señal_wifi': 'débil'|'aceptable'|'fuerte',
                    'errores_dns': 'frecuente'|'ocasional'|'nula'
                }
        
        Returns:
            dict: Diagnóstico con causas y recomendaciones
        """
        # Convertir valores lingüísticos a numéricos
        self.simulator.input['conectividad'] = self._get_numeric_value('conectividad', symptoms['conectividad'])
        self.simulator.input['velocidad'] = self._get_numeric_value('velocidad', symptoms['velocidad'])
        self.simulator.input['acceso_servidor'] = self._get_numeric_value('acceso_servidor', symptoms['acceso_servidor'])
        self.simulator.input['señal_wifi'] = self._get_numeric_value('señal_wifi', symptoms['señal_wifi'])
        self.simulator.input['errores_dns'] = self._get_numeric_value('errores_dns', symptoms['errores_dns'])

        # Computar el resultado
        self.simulator.compute()

        # Obtener resultados, usando 0 si la salida no existe
        results = {}
        for cause in ['falla_isp', 'cable_dañado', 'problema_router', 'config_dns', 'cobertura_wifi']:
            valor = float(self.simulator.output[cause]) if cause in self.simulator.output else 0.0
            recomendacion = self._get_recommendation(cause, valor)
            results[cause] = {
                'valor': valor,
                'recomendacion': recomendacion
            }

        # Ordenar resultados por valor (de mayor a menor)
        sorted_results = dict(sorted(
            results.items(),
            key=lambda x: x[1]['valor'],
            reverse=True
        ))

        return {
            'diagnostico': sorted_results,
            'causa_principal': next(iter(sorted_results)),
            'valor_principal': next(iter(sorted_results.values()))['valor'],
            'recomendacion_principal': next(iter(sorted_results.values()))['recomendacion']
        } 