# Geometriai modellezés beadandó
## Bezier görbe raszteres megjelenítése
Ez az alkalmazás lehetőséget nyújt Bézier görbék szerkesztésére és raszteres megjelenítésére. A program vizuálisan jeleníti meg a görbét, valamint kiszámolja annak hosszát és a görbe által bezárt terület közelítő értékét.

## Használt technológiák

- **Python 3**
- **Pygame** – grafikus megjelenítéshez
- **pygame_gui** – UI elemek kezeléséhez
- **NumPy** – Bézier görbe számításokhoz

## Funkciók

- Interaktív kontrollpont mozgatás egérrel
- Bézier görbe kiszámítása és kirajzolása a de Casteljau-algoritmus alapján
- A görbe mentén számított hossz megjelenítése
- A görbe által bezárt terület közelítő becslése
- UI panel a pontsűrűség (interpolációs lépések száma) beállításához
- Kontrollpontok visszaállítása alaphelyzetbe gombbal

## Használat

1. **Telepítés:**

```bash
pip install -r requirements.txt
```
2. **Program futtatása:**

```bash
python main.py
```