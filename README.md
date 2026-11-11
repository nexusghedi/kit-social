# Kit social Nexus APS

Immagini e testi pronti per WhatsApp, Facebook e Instagram degli eventi in programma di Nexus APS (Ghedi).

Pagina: https://nexusghedi.github.io/kit-social/ (non indicizzata dai motori di ricerca).

- `index.html`: la pagina, con i dati degli eventi nell'array `EVENTI`.
- `img/`: immagini esportate dal canvas (WhatsApp 1:1, carosello 4:5, storie 9:16).
- Le parti tra [quadre] bloccano l'invio finché non vengono completate.

## Materiali di stampa
- `stampa/`: PDF pronti (volantini A5 2 per foglio, locandine A4 bacheca e A3, pieghevoli, programmi) e `stampa/anteprime/`.
- `strumenti/pdf.js`: rende una tavola del canvas (559×794 px = A5) in PDF vettoriale alla misura voluta (`node pdf.js tavola.html cartella_blob out.pdf larghezza_mm altezza_mm zoom`, con `F=` cartella dei font).
- `strumenti/compose.py`: impagina 2 A5 su A4 orizzontale (con linea di taglio) e i pieghevoli 4+1 / 2+3.
- `risorse/`: loghi Nexus e Arkè.
