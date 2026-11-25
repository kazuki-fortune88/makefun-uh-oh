#!/usr/bin/env python3
"""Uh-oh kecil si agen.

Program mungil ini cuma melakukan satu hal: menyimpan satu kata
lucu ke dalam sebuah berkas bernama entry.txt. Kata itu adalah
nama berkas yang terdengar seperti program sungguhan, padahal
isinya hanya lelucon satu baris. Tidak ada logika rumit, tidak
ada jaringan, tidak ada yang lain -- tulis, lalu selesai.
"""

import os

WORD = "Dunno.exe"


def main():
    """Tulis WORD ke entry.txt di folder output, tanpa newline."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
