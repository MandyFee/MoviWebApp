# Teil 1

#1. Falsche Eingabe bei get_number_of_websites()
#Aktion: Gib etwas anderes als eine Zahl ein (z. B. "abc" oder " ").
#Fehler:
#ValueError: invalid literal for int() with base 10: 'abc'

#2. 0 oder negative Zahl als Eingabe
#Aktion: Gib 0 oder -3 als Anzahl ein.
#Folge: Es werden keine URLs gesammelt → urls = None.
#Fehler (später in for url in urls:):
#TypeError: 'NoneType' object is not iterable

#3. Keine gültigen HTTPS-URLs eingeben
#Aktion: Gib nur http://... oder Müll ein. Dann wird die Liste urls leer → None.
#Fehler:
#TypeError: 'NoneType' object is not iterable

#4. Weniger als 3 gültige URLs eingeben
#Aktion: Nur 1 oder 2 gültige URLs eingeben.
#Fehler in top_3 = [...]:
#IndexError: list index out of range

#5. Ungültige oder unerreichbare URL
#Aktion: Gib z. B. https://asdasdasdasd12345.com ein.
#Fehler beim requests.get(url):
#requests.exceptions.ConnectionError: ...

#6. HTTP-Status nicht in HTTP_RESPONSES
#Aktion: Nimm eine echte Seite, die z. B. 404 Not Found liefert.
#Fehler in HTTP_RESPONSES[response.status_code]:
#KeyError: 404

#7. Keine URLs erfolgreich geprüft
#Aktion: Wenn keine gültige URL durchkommt, bleibt response_times leer.
#Fehler bei sum(only_response_times) / len(only_response_times):
#ZeroDivisionError: division by zero

# Teil 2
#!/usr/bin/env python3
"""
Website-Speed-Checker (anfängerfreundlich)
- Sichere Eingaben (keine Abstürze bei Text/Zahlen)
- Akzeptiert http und https (fügt https:// hinzu, wenn Scheme fehlt)
- Sauberes Fehler-Handling für Netzwerkfehler/Timeouts
- Funktioniert auch mit weniger als 3 erfolgreichen Ergebnissen
"""

import time
import requests
from typing import List, Tuple, Optional

HTTP_RESPONSES = {
    200: ('OK', 'Request fulfilled, document follows'),
    301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
    302: ('Found', 'Object moved temporarily -- see URI list'),
    403: ('Forbidden', 'Request forbidden -- authorization will not help'),
    404: ('Not Found', 'The requested resource could not be found'),
    429: ('Too Many Requests', 'Rate limit exceeded'),
    500: ('Internal Server Error', 'Server got itself in trouble'),
    502: ('Bad Gateway', 'Invalid response from upstream server'),
    503: ('Service Unavailable', 'Server cannot handle the request'),
    504: ('Gateway Timeout', 'Upstream server timed out'),
}

def prompt_positive_int(prompt: str) -> int:
    """Fragt so lange nach einer positiven ganzen Zahl, bis eine gültige Eingabe erfolgt."""
    while True:
        s = input(prompt).strip()
        try:
            n = int(s)
            if n <= 0:
                print("Bitte gib eine Zahl größer als 0 ein.\n")
                continue
            return n
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein (z. B. 3).\n")

def normalize_url(u: str) -> str:
    """Trimmt die Eingabe und fügt https:// hinzu, falls kein Schema vorhanden ist."""
    u = u.strip()
    if not u:
        return ""
    if not (u.startswith("http://") or u.startswith("https://")):
        u = "https://" + u
    return u

def get_multiple_url_inputs(num_websites: int) -> List[str]:
    """Sammelt genau num_websites URLs (keine Duplikate, einfache Plausibilitätsprüfung)."""
    urls: List[str] = []
    while len(urls) < num_websites:
        raw = input(f"Bitte die URL für Website {len(urls) + 1} eingeben: ")
        url = normalize_url(raw)
        if not url:
            print("Leere Eingabe – bitte erneut versuchen.\n")
            continue
        # sehr einfache Plausibilitätsprüfung
        host_part = url.split("://", 1)[-1]
        if "." not in host_part:
            print("Das sieht nicht wie eine gültige Adresse aus. Beispiel: example.com oder https://example.com\n")
            continue
        if url in urls:
            print("Diese URL wurde bereits eingegeben.\n")
            continue
        urls.append(url)
    return urls

def measure_response_time(url: str, timeout: int = 10) -> Optional[Tuple[int, float]]:
    """Misst die Antwortzeit für eine URL. Gibt (Statuscode, Sekunden) zurück oder None bei Fehler."""
    try:
        start = time.time()
        resp = requests.get(url, timeout=timeout)
        elapsed = time.time() - start
        status_code = resp.status_code
        status_text, status_desc = HTTP_RESPONSES.get(status_code, (str(status_code), "Unbekannter Statuscode"))
        print(f"Antwort von {url}: {status_code} – {status_text} ({status_desc}) in {elapsed:.4f} s")
        return status_code, elapsed
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abruf von {url}: {e.__class__.__name__}: {e}")
        return None

def main():
    print("=== Website-Speed-Checker (anfängerfreundlich) ===")
    num_websites = prompt_positive_int("Wie viele Websites möchtest du prüfen? ")

    urls = get_multiple_url_inputs(num_websites)

    results: List[Tuple[str, float]] = []
    for url in urls:
        res = measure_response_time(url)
        if res is not None:
            _, t = res
            results.append((url, t))

    if results:
        # Sortieren nach Zeit (schnellste zuerst)
        results.sort(key=lambda x: x[1])

        # Top bis zu 3 anzeigen
        print("\nTop-Speed-Ranking:")
        for i, (url, t) in enumerate(results[:3], start=1):
            print(f"{i}. {url} – {t:.4f} Sekunden")

        # Durchschnitt berechnen
        avg = sum(t for _, t in results) / len(results)
        print(f"\nDurchschnittliche Antwortzeit (über {len(results)} erfolgreiche Abrufe): {avg:.4f} Sekunden")
    else:
        print("\nKeine erfolgreichen Abrufe. Bitte überprüfe deine Eingaben oder deine Internetverbindung.")

if __name__ == "__main__":
    main()

# muster lösung
