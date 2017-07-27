\documentclass[a4paper]{article}

%% Language and font encodings
\usepackage[english]{babel}
\usepackage[utf8x]{inputenc}
\usepackage[T1]{fontenc}

%% Sets page size and margins
\usepackage[a4paper,top=3cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}

%% Useful packages
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage[colorinlistoftodos]{todonotes}
\usepackage[colorlinks=true, allcolors=blue]{hyperref}

\title{Metodos computacionales - Tarea 3}
\author{Nataly Pulido Fernandez - 20121633}

\begin{document}
\maketitle


\

\begin{figure}
\section{Ecuacion de onda en 2 dimenciones}

Se tiene una onda que se propaga en un contenedor cuadrado con una rendija a 1/3 de uno de los lados y ademas, se tiene una perturbacion de la superficie del liquido. Es las imagenes que se presentan posteriormente se observa la propagacion de la onda en un tiempo de 30 segundo y asimismo, se observa la propagacion de la onda en un tiempo de 30 segundos, sin embargo es de notarse que la amplitud de las mismas varia con el tiempo
\centering
\includegraphics[width=0.5\textwidth]{Resultado_60.png}
\caption{\label{fig:60}Propagacion de onda en t=60.}
\end{figure}

\begin{figure}
\centering
\includegraphics[width=0.5\textwidth]{Resultado_30.png}
\caption{\label{fig:30}Propagacion de onda en t=30.}
\end{figure}


\begin{figure}
\section{Sistema Solar}

Se soluciono la ecuacion de la ecuacion de movimiento de los cuerpos del sistema solar usando el metodo de Leap Frog. Asimismo, se calculo la fuerza sobre cada uno de los objetos. Finalmente se tiene una grafica que se muestra posteriormente en donde se observa las orbitas de los planetas. 
\centering
\includegraphics[width=1.0\textwidth]{Resultados_hw3.pdf}
\caption{\label{fig:Orbitas}Orbitas de los planetas del sistema solar.}
\end{figure}



\end{document}
