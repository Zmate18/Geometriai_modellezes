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

## Terület becslése

A Bézier-görbe által körbezárt területet a **saru formula** (*shoelace formula*) segítségével becsülöm. A módszer lényege, hogy a görbét kis szakaszokra bontom, majd az így kapott pontokat egy sokszöggé zárom, és erre alkalmazom a következő képletet:

```math
A = \frac{1}{2} \left| \sum_{i=0}^{n-1} (x_i y_{i+1} - x_{i+1} y_i) \right|
```

ahol $(x_i, y_i)$ a sokszög pontjai, és $n$ a pontok száma. Az utolsó pont $x_n, y_n$ megegyezik az első ponttal a zárás miatt.

### Példa mérések

A pontosság a görbét alkotó szegmensek számától (`steps`) függ. Az alábbi táblázat bemutatja, hogyan közelít a terület az `steps` növelésével:

| Steps | Becsült terület (px²) |
|-------|-----------------------|
| 10    | 39506                 |
| 50    | 39983                 |
| 100   | 39996                 |
| 200   | 39999                 |
| 500   | 40000                 |
| 1000  | 40000                 |

Látható, hogy a becsült terület értéke már viszonylag alacsony `steps` szám esetén is közelít a végleges értékhez. 100 lépéstől kezdve az eltérés minimális, 500 és 1000 lépésnél pedig a becsült terület eléri a stabil 40000 px² értéket.

## Használat

1. **Telepítés:**

```bash
pip install -r requirements.txt
```
2. **Program futtatása:**

```bash
python main.py
```
