# Sistema Experto de Diagnóstico de Fallas en Red

Este sistema experto utiliza lógica difusa para diagnosticar problemas en redes de oficina basándose en síntomas observables.

## Características

- Diagnóstico de fallas en red usando lógica difusa
- Interfaz web simple y intuitiva
- API REST para integración con otros sistemas
- Motor de inferencia difusa con operadores AND, OR, NOT
- Defuzzificación por método del centroide
- Recomendaciones de acción basadas en el diagnóstico

## Requisitos

- Python 3.8+
- Node.js 14+ (para el frontend)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd sistema-experto-l-gica-dif
```

2. Configurar el backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configurar el frontend:
```bash
cd frontend
npm install
```

## Ejecución

1. Iniciar el backend:
```bash
cd backend
python app.py
```

2. Iniciar el frontend:
```bash
cd frontend
npm start
```

3. Acceder a la aplicación en: http://localhost:3000

## Estructura del Proyecto

```
sistema-experto-l-gica-dif/
├── backend/
│   ├── app.py
│   ├── fuzzy_logic/
│   │   ├── __init__.py
│   │   ├── variables.py
│   │   ├── rules.py
│   │   └── inference.py
│   ├── api/
│   │   └── routes.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
└── README.md
```

## Uso

1. Ingrese los síntomas observados en la interfaz web
2. El sistema procesará la información usando lógica difusa
3. Se mostrará el diagnóstico y las recomendaciones de acción

## Casos de Prueba

El sistema incluye 5 casos de prueba predefinidos que demuestran diferentes escenarios de fallas en red.

## Tecnologías Utilizadas

- Backend: Python, Flask, scikit-fuzzy
- Frontend: React, Material-UI
- Lógica Difusa: scikit-fuzzy 