# Desafío Python

### Comparaión

Funciones puras
```
* Mi sistema ejecuta únicamente funciones/validaciones que yo defino y controlo.
* Es adaptable con el uso de Regex Simple.
* Utilizó nombres que se relacionan con mi proceso, lo que con lleva claridad.
* Mi sistema trabaja con conversiones que muestran su eficiencia.
```
Enfoque EVAL()
```
* "eval()" recibe y ejecuta cualquier código Python.
* Se complica al momento de la validación, lo que nos lleva a estar propenso a errores.
* Para una validacion no tiene pasos claros, oculta la lógica.
* Es lento por lo que invoca el compilador de Python.
```
En conclusión es difícil customizar eval a nuestra necesidad lo cual lo hace difícil de mantener y capturar errores.

### NormalizeAmountOperation

* Actualmente es flexible para cualquier campo numérico, ya que tomamos el valor del campo y lo procesamos, retornando siempre un flotante.
* En el caso de que el campo a normalizar no exista, de igual forma agregamos "campoNoExistente: None" al registro. Sin embargo, esto no es del todo correcto si pensamos en el estado de la operación, ya que podría considerarse un registro corrupto. Por lo tanto, se debería definir una estructura o interfaz para cada tipo de registro y, antes de cualquier operación, validar que coincida con la estructura o el patrón definido.
