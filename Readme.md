# Gestor de Inventario - Talento Tech

## Instrucciones de Instalación

1. Clona este repositorio en tu máquina local.
   ```bash
   git clone https://github.com/RodrigoBedoya22/Proyecto-Final-Gestor-Inventario-Talento-Tech.git
   ```
2. Crea un entorno virtual ejecutando `python -m venv venv`.
3. Activa el entorno virtual:
   * En Windows: `venv\Scripts\activate`
       **NOTA:** Si estas usando windows muy probablemente te salte un error, deberas ejecutar el siguiente comando:
       ```powershell
       Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
       ```
       Esto pasa porque windows no permite la activacion de entorno virtuales por defecto (no sé por que la verdad)
   * En Linux/Mac: `source venv/bin/activate`
5. Instala las dependencias necesarias (Si ya se posee el modulo Colorama, entonces saltearse este paso):
   ```bash
   pip install -r requirements.txt
   ```
6. Con el entorno virtual activo y las dependencias descargadas, ejecutar:
   ```python
   python Proyecto-final.py
   ```
   Y con esto estaria funcionando.

