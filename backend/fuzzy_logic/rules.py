from .variables import (
    connectivity, speed, server_access, wifi_signal, dns_errors,
    isp_failure, cable_damage, router_problem, dns_config, wifi_coverage
)
from skfuzzy import control as ctrl

# Reglas para falla ISP
rule1 = ctrl.Rule(
    connectivity['nula'] & speed['lenta'],
    isp_failure['alta']
)
rule2 = ctrl.Rule(
    connectivity['baja'] & speed['lenta'],
    isp_failure['media']
)
rule3 = ctrl.Rule(
    connectivity['media'] & speed['moderada'],
    isp_failure['baja']
)

# Reglas para cable dañado
rule4 = ctrl.Rule(
    server_access['inaccesible'] & speed['moderada'],
    cable_damage['alta']
)
rule5 = ctrl.Rule(
    server_access['lento'] & speed['lenta'],
    cable_damage['media']
)
rule6 = ctrl.Rule(
    server_access['fluido'] & speed['rápida'],
    cable_damage['baja']
)

# Reglas para problema en router
rule7 = ctrl.Rule(
    connectivity['nula'] & wifi_signal['débil'],
    router_problem['alta']
)
rule8 = ctrl.Rule(
    connectivity['baja'] & wifi_signal['aceptable'],
    router_problem['media']
)
rule9 = ctrl.Rule(
    connectivity['buena'] & wifi_signal['fuerte'],
    router_problem['baja']
)

# Reglas para configuración DNS
rule10 = ctrl.Rule(
    dns_errors['frecuente'] & connectivity['baja'],
    dns_config['alta']
)
rule11 = ctrl.Rule(
    dns_errors['ocasional'] & connectivity['media'],
    dns_config['media']
)
rule12 = ctrl.Rule(
    dns_errors['nula'] & connectivity['buena'],
    dns_config['baja']
)

# Reglas para cobertura Wi-Fi
rule13 = ctrl.Rule(
    wifi_signal['débil'] & connectivity['baja'],
    wifi_coverage['alta']
)
rule14 = ctrl.Rule(
    wifi_signal['aceptable'] & connectivity['media'],
    wifi_coverage['media']
)
rule15 = ctrl.Rule(
    wifi_signal['fuerte'] & connectivity['buena'],
    wifi_coverage['baja']
)

# Reglas adicionales para casos combinados
rule16 = ctrl.Rule(
    connectivity['nula'] & server_access['inaccesible'] & dns_errors['frecuente'],
    [isp_failure['alta'], cable_damage['alta'], dns_config['alta']]
)
rule17 = ctrl.Rule(
    wifi_signal['débil'] & speed['lenta'] & server_access['lento'],
    [wifi_coverage['alta'], cable_damage['media'], router_problem['media']]
)

# Crear el sistema de control
network_diagnosis_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
    rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17
])

# Crear el simulador
network_diagnosis = ctrl.ControlSystemSimulation(network_diagnosis_ctrl) 