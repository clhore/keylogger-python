# keylogger-python

  En este caso el script enviara un gmail al destinantario cuando pase el tiempo que hallamos definido o cuando le pulsen el numero de teclas que hallamos definido. Este script no crea singun archivo de log.txt ya que almacena todas las pulsaciones en un variable global. Esto tuede hacer que algunas pulsaciones se pierdan al no ser enviadas antes de apagar el equipo.

# Compiled in WINDOWS
  Descarga y descomprime `keylogger.zip` y ejecuta el comado:
  
    pyinstaller --onefile --hidden-import pynput.keyboard._win32 --hidden-import pynput.mouse._win32 .\gmail.pyw
  
  ![](https://i.imgur.com/3ffbhaE.png)
  
  `gmail.exe` is created in the path `\keylogger\disk\gmail.exe` the `gmail.exe` contains all the necessary libraries to function.
  
  ![](https://i.imgur.com/zYM8IDh.png)
