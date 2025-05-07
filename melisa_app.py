from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/komut')
def komut():
    text = request.args.get("text", "")
    print(f"[API] Gelen komut: {text}")

    try:
        sonuc = subprocess.run(
            ["python", "1_2.py", text],
            capture_output=True,
            text=True
        )
        return sonuc.stdout.strip() or "Komut işlendi."
    except Exception as e:
        return f"Hata: {e}"

# BU KISIM OLMADAN SUNUCU ÇALIŞMAZ ⬇️
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
