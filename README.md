# vehicles

ANTES QUE NADA, ANEXO LINK RENDER:
https://vehicles-1kbb.onrender.com****
https://dashboard.render.com/web/srv-d0bfs5pr0fns73ddudg0
# Exported from Render on 2025-05-04T05:49:48Z
services:
- type: web
  name: vehicles
  runtime: python
  repo: https://github.com/Al3kHT/vehicles
  plan: free
  region: oregon
  buildCommand: pip install -r requirements.txt
  startCommand: streamlit run app.py
version: "1"

SE CREO EL ENTORNO CORRECTAMENTE, CON LOS PAQUETES DE PANDAS, PLOTLY Y STREAMLIT
Recordatorio. Para instalar desde requirements.txt con conda, el comando correcto es:
conda env create --name vehicles_myenv --file requirements.txt 

O, si el entorno ya existe:

conda install --name vehicles_myenv --file requirements.txt

SE CREO EL ARCHIVO REQUIREMENTS, PERO LAS LIBRERIAS Y PAQUETES SE INSTALARON COMO ACONTINUACION INICIALMENTE:
conda install plotly::plotly_express # instala plotly
conda install anaconda::pandas # instala pandas
conda install conda-forge::streamlit # instala streamlit

SOLUCION DE REQUERIMIENTOS, EXPORTAR LOS YA INSTALADOS:

Exportar el entorno actual (mejor práctica)
Para asegurarse de que requirements.txt refleje exactamente las versiones de las librerías usadas en vehicles_myenv, se puede exportar el entorno en uso:
Por medio de Anaconda Prompt y activando el entorno:

conda activate vehicles_myenv

Exportando las dependencias a un archivo:

conda list --export > requirements.txt
Se tendra algo como:
pandas=1.5.3
plotly=5.14.1
streamlit=1.20.0
...
Esto con el fin de garantizar compatibilidad.
Recordar siempre;
git add 
git commit -m 
git push origin main

Para confirmar que el archivo funciona, prueba recrear un entorno nuevo:

Crea un entorno de prueba:
conda create --name test_env --file requirements.txt
Activar y verificar:

conda activate test_env
python -c "import pandas, plotly.express, streamlit"
De no haber errores, todo ocurre con normalidad.
