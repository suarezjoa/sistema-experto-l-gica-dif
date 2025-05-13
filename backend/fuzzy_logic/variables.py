import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Universo de discurso para cada variable
connectivity_universe = np.arange(0, 101, 1)
speed_universe = np.arange(0, 101, 1)
server_access_universe = np.arange(0, 101, 1)
wifi_signal_universe = np.arange(0, 101, 1)
dns_errors_universe = np.arange(0, 101, 1)
cause_universe = np.arange(0, 101, 1)

# Variables lingüísticas para síntomas
connectivity = ctrl.Antecedent(connectivity_universe, 'conectividad')
speed = ctrl.Antecedent(speed_universe, 'velocidad')
server_access = ctrl.Antecedent(server_access_universe, 'acceso_servidor')
wifi_signal = ctrl.Antecedent(wifi_signal_universe, 'señal_wifi')
dns_errors = ctrl.Antecedent(dns_errors_universe, 'errores_dns')

# Variables lingüísticas para causas
isp_failure = ctrl.Consequent(cause_universe, 'falla_isp')
cable_damage = ctrl.Consequent(cause_universe, 'cable_dañado')
router_problem = ctrl.Consequent(cause_universe, 'problema_router')
dns_config = ctrl.Consequent(cause_universe, 'config_dns')
wifi_coverage = ctrl.Consequent(cause_universe, 'cobertura_wifi')

# Funciones de membresía para conectividad
connectivity['nula'] = fuzz.trimf(connectivity_universe, [0, 0, 25])
connectivity['baja'] = fuzz.trimf(connectivity_universe, [0, 25, 50])
connectivity['media'] = fuzz.trimf(connectivity_universe, [25, 50, 75])
connectivity['buena'] = fuzz.trimf(connectivity_universe, [50, 75, 100])

# Funciones de membresía para velocidad
speed['lenta'] = fuzz.trimf(speed_universe, [0, 0, 50])
speed['moderada'] = fuzz.trimf(speed_universe, [25, 50, 75])
speed['rápida'] = fuzz.trimf(speed_universe, [50, 100, 100])

# Funciones de membresía para acceso al servidor
server_access['inaccesible'] = fuzz.trimf(server_access_universe, [0, 0, 33])
server_access['lento'] = fuzz.trimf(server_access_universe, [0, 33, 66])
server_access['fluido'] = fuzz.trimf(server_access_universe, [33, 66, 100])

# Funciones de membresía para señal Wi-Fi
wifi_signal['débil'] = fuzz.trimf(wifi_signal_universe, [0, 0, 50])
wifi_signal['aceptable'] = fuzz.trimf(wifi_signal_universe, [25, 50, 75])
wifi_signal['fuerte'] = fuzz.trimf(wifi_signal_universe, [50, 100, 100])

# Funciones de membresía para errores DNS
dns_errors['frecuente'] = fuzz.trimf(dns_errors_universe, [0, 0, 50])
dns_errors['ocasional'] = fuzz.trimf(dns_errors_universe, [25, 50, 75])
dns_errors['nula'] = fuzz.trimf(dns_errors_universe, [50, 100, 100])

# Funciones de membresía para todas las causas
for cause in [isp_failure, cable_damage, router_problem, dns_config, wifi_coverage]:
    cause['baja'] = fuzz.trimf(cause_universe, [0, 0, 50])
    cause['media'] = fuzz.trimf(cause_universe, [25, 50, 75])
    cause['alta'] = fuzz.trimf(cause_universe, [50, 100, 100])

# Diccionario de mapeo de valores lingüísticos a numéricos
linguistic_to_numeric = {
    'conectividad': {
        'nula': 0,
        'baja': 25,
        'media': 50,
        'buena': 75
    },
    'velocidad': {
        'lenta': 25,
        'moderada': 50,
        'rápida': 75
    },
    'acceso_servidor': {
        'inaccesible': 0,
        'lento': 33,
        'fluido': 66
    },
    'señal_wifi': {
        'débil': 25,
        'aceptable': 50,
        'fuerte': 75
    },
    'errores_dns': {
        'frecuente': 25,
        'ocasional': 50,
        'nula': 75
    }
}

# Diccionario de recomendaciones basadas en causas
recommendations = {
    'falla_isp': {
        'baja': 'Contactar al proveedor de internet para verificar el servicio.',
        'media': 'Verificar con el proveedor de internet y considerar un plan de respaldo.',
        'alta': 'Contactar inmediatamente al proveedor de internet y activar plan de contingencia.'
    },
    'cable_dañado': {
        'baja': 'Revisar visualmente los cables y conexiones.',
        'media': 'Reemplazar cables sospechosos y verificar conectores.',
        'alta': 'Reemplazar inmediatamente los cables y verificar toda la infraestructura física.'
    },
    'problema_router': {
        'baja': 'Reiniciar el router y verificar su funcionamiento.',
        'media': 'Actualizar firmware del router y revisar configuración.',
        'alta': 'Reemplazar el router o contactar soporte técnico especializado.'
    },
    'config_dns': {
        'baja': 'Verificar configuración DNS en dispositivos.',
        'media': 'Actualizar servidores DNS y limpiar caché.',
        'alta': 'Reconfigurar completamente los servidores DNS y verificar resolución de nombres.'
    },
    'cobertura_wifi': {
        'baja': 'Reposicionar el router para mejor cobertura.',
        'media': 'Instalar repetidores o puntos de acceso adicionales.',
        'alta': 'Rediseñar la infraestructura de red inalámbrica con puntos de acceso estratégicos.'
    }
} 