# Obligatorio 2024 - Inteligencia Artificial

## Universidad ORT Uruguay
**Mayo 2024**

## Proyecto de Innovación en Movilidad, Automatización y Estrategia

### Descripción del Proyecto

Una empresa líder en tecnología ha contratado a un equipo de expertos en IA para abordar desafíos fundamentales en movilidad urbana, automatización industrial y estrategia. Para esto, el equipo cuenta con tres simuladores diseñados específicamente para estos desafíos.

---

## Desafíos

### 1. Taxi

Para mejorar la movilidad urbana, se está evaluando una nueva flota de taxis que optimizan el consumo de combustible y reducen los tiempos de viaje.

- **Técnica:** Q-Learning  
- **Simulador:** [Aulas]  
- **Ambiente:** Taxi  
- **Referencia:** [Taxi Gymnasium](https://gymnasium.farama.org/environments/toy_text/taxi/)

### 2. Pendulum

En una fábrica de relojes, una máquina de ensamblaje usa un péndulo que es más eficiente si pasa por un sensor magnético. Se busca reducir el tiempo de ensamblaje a un minuto.

- **Técnica:** Q-Learning  
- **Simulador:** [Aulas]  
- **Ambiente:** Pendulum  
- **Referencia:** [Pendulum Gymnasium](https://gymnasium.farama.org/environments/classic_control/pendulum/)

### 3. Coin Game

El equipo desea construir un agente capaz de vencer al líder en el juego Coin Game, proporcionando vibraciones al jugador para indicarle el mejor movimiento.

- **Técnica:** Minimax o Expectimax (a decidir por el equipo).  
- **Simulador:** [Aulas]  
- **Ambiente:** [Aulas]  

---

## Alpha-beta Pruning

Para la tercera parte (Coin Game), se debe completar una de las siguientes tareas:

1. **Implementar** la técnica de optimización alpha-beta pruning.
2. **Leer y comentar** el artículo sobre alpha-beta pruning respondiendo preguntas guía, como:
   - ¿Cuál es el objetivo del autor?
   - ¿Cuál es el desafío de los árboles de juego en computadoras?
   - ¿Cómo funciona el algoritmo Minimax?
   - ¿Cómo ayuda alpha-beta pruning en Tic-Tac-Toe?

**Referencia:** [Artículo sobre Alpha-Beta Pruning](https://www.whitman.edu/documents/academics/majors/mathematics/2019/Felstiner-Guichard.pdf)

---

## 📌 Auditoría y Entrega

El equipo de auditoría evaluará la performance de las soluciones. Para ello, la entrega debe incluir:

- 📂 Código fuente en **Python** (.py, .ipynb, .html).
- 📦 Modelos computados (.pkl o similar).
- 📄 Informe en formato **PDF** con:
  - **Resumen** del enfoque utilizado en cada tarea.
  - **Bitácora** con interacción con el simulador, parámetros utilizados, tiempo de ejecución y resultados obtenidos.
  - **Gráficos** y comentarios sobre el desempeño de las soluciones.
  - **Notas de advertencia**, en caso de haber encontrado dificultades.

---

## 🔧 Dependencias

- Se debe utilizar **gymnasium versión 0.28.1**.

## ⚠️ Recomendación

> **Hacerlo con tiempo!** Las ejecuciones pueden ser largas.

---

## 📅 Fecha de Entrega

**🗓️ 08-07-2024**

🚀 ¡Buena suerte! 🎯

