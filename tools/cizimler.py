# Wirbel "Yaptığımız işler" temsili çizimleri (SVG) üretir.
# Gerçek proje fotoğraflarındaki pano düzenleri referans alınmıştır; müşteri işi gösterilmez.
L = "#033246"   # lacivert
B = "#7A3848"   # bordo
S = "#F2A900"   # sarı
G = "#B9C0BD"   # gri çizgi
P = "#E3E6E2"   # pano gri
W = "#FFFFFF"

def svg(body, title):
    return (f'<svg viewBox="0 0 400 300" role="img" aria-label="{title}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="400" height="300" fill="#F4F5F3"/>{body}</svg>')

def kasa(x=70, y=18, w=260, h=270):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{P}" stroke="{L}" stroke-width="2.5"/>'
            f'<rect x="{x+10}" y="{y+10}" width="{w-20}" height="{h-20}" fill="#EEF0EE" stroke="{G}"/>')

def kanal(x, y, w, h=12):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#D3D8D6" stroke="#9AA4A0" stroke-width="1"/>'
    for i in range(int(x)+6, int(x+w)-4, 8):
        s += f'<line x1="{i}" y1="{y+2}" x2="{i}" y2="{y+h-2}" stroke="#9AA4A0" stroke-width="1"/>'
    return s

def ray(x, y, w):
    return f'<rect x="{x}" y="{y-3}" width="{w}" height="6" fill="#AEB6B3"/>'

def mcb(x, y, n=1):
    s = ''
    for i in range(n):
        xx = x + i*12
        s += (f'<rect x="{xx}" y="{y-16}" width="11" height="32" rx="1" fill="{W}" stroke="{L}" stroke-width="1"/>'
              f'<rect x="{xx+3}" y="{y-6}" width="5" height="9" fill="{L}"/>')
    return s

def kontaktor(x, y, label=True):
    s = (f'<rect x="{x}" y="{y-17}" width="18" height="34" rx="2" fill="#5D7186" stroke="{L}" stroke-width="1"/>'
         f'<rect x="{x+3}" y="{y-6}" width="12" height="10" fill="#C9D3DC"/>')
    if label: s += f'<rect x="{x+4}" y="{y+8}" width="10" height="5" fill="{S}"/>'
    return s

def mks(x, y):  # motor koruma şalteri
    return (f'<rect x="{x}" y="{y-18}" width="20" height="36" rx="2" fill="#4A5763" stroke="{L}" stroke-width="1"/>'
            f'<circle cx="{x+10}" cy="{y-3}" r="6" fill="#2C3640" stroke="#8E9BA6"/>'
            f'<line x1="{x+10}" y1="{y-8}" x2="{x+10}" y2="{y+2}" stroke="{S}" stroke-width="2"/>'
            f'<rect x="{x+4}" y="{y+8}" width="12" height="5" fill="{S}"/>')

def klemens(x, y, n, renkler=None):
    s = ''
    for i in range(n):
        c = "#9AA4A0"
        if renkler and i in renkler: c = renkler[i]
        s += f'<rect x="{x+i*6}" y="{y-12}" width="5" height="24" fill="{c}" stroke="#6E7874" stroke-width=".6"/>'
    return s

def kablolar(x1, x2, y1, y2, adim=12, renk=None):
    s = ''
    i = 0
    for x in range(int(x1), int(x2), adim):
        c = renk or (["#C0392B", "#2E5E9E", "#C0392B", "#1B232B"][i % 4])
        s += f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{c}" stroke-width="1.6"/>'
        i += 1
    return s

def led(cx, cy, renk, cls=""):
    return f'<circle class="{cls}" cx="{cx}" cy="{cy}" r="2.4" fill="{renk}"/>'

# ---------- 1. PLC kontrol panosu ----------
def plc_panosu():
    b = kasa()
    b += kanal(85, 38, 230)
    b += ray(85, 76, 230) + mcb(92, 76, 5)
    b += (f'<rect x="160" y="57" width="70" height="38" rx="2" fill="{W}" stroke="{L}" stroke-width="1.5"/>'
          f'<rect x="166" y="63" width="30" height="16" fill="#BFD9C9" stroke="{L}" stroke-width=".8"/>'
          f'<text x="170" y="75" font-family="Barlow,Arial" font-size="9" fill="{L}" font-weight="700">PLC</text>')
    for i in range(6): b += led(203+i*4, 66, S if i % 2 else "#2FA35A", "ci-yanip" if i == 1 or i == 4 else "")
    b += f'<rect x="240" y="60" width="26" height="34" rx="2" fill="#2E3A44" stroke="{L}"/><rect x="245" y="66" width="16" height="4" fill="#5FD38A"/>'
    b += mcb(274, 76, 3)
    b += kanal(85, 98, 230)
    b += ray(85, 138, 230)
    for i in range(10): b += kontaktor(92+i*22, 138)
    b += kanal(85, 160, 230)
    b += kablolar(96, 310, 172, 212, 9)
    b += ray(85, 222, 230) + klemens(92, 222, 36, {3: "#7FB069", 11: "#7FB069", 19: "#7FB069", 27: "#7FB069", 7: "#2E5E9E", 15: "#2E5E9E"})
    b += kanal(85, 240, 230)
    return svg(b, "PLC kontrol panosu temsili çizimi")

# ---------- 2. Motor kontrol panosu ----------
def motor_panosu():
    b = kasa()
    b += kanal(85, 38, 230) + ray(85, 74, 230)
    for i in range(7): b += mks(92+i*25, 74)
    b += kanal(85, 96, 230) + ray(85, 132, 230)
    for i in range(7): b += kontaktor(93+i*25, 132)
    b += kanal(85, 154, 230)
    # sürücü
    b += (f'<rect x="268" y="112" width="40" height="70" rx="3" fill="#2E3A44" stroke="{L}" stroke-width="1.5"/>'
          f'<rect x="274" y="120" width="28" height="12" fill="#0E1A22"/><text class="ci-hz" x="277" y="129.5" font-family="monospace" font-size="8" fill="#5FD38A">50.0</text>'
          f'<g class="ci-fan" style="transform-origin:288px 160px"><circle cx="288" cy="160" r="12" fill="#1B232B" stroke="#8E9BA6"/>'
          f'<path d="M288 149 V171 M277 160 H299 M280 152 L296 168 M296 152 L280 168" stroke="#8E9BA6" stroke-width="2"/></g>')
    b += kablolar(96, 260, 168, 212, 10)
    b += ray(85, 222, 230) + klemens(92, 222, 36, {2: "#7FB069", 9: "#7FB069", 16: "#7FB069", 23: "#7FB069"})
    b += kanal(85, 240, 230)
    return svg(b, "Motor kontrol panosu temsili çizimi")

# ---------- 3. Pano kapağı / operatör paneli ----------
def kapak():
    b = (f'<rect x="80" y="14" width="240" height="276" rx="5" fill="#ECEEED" stroke="{L}" stroke-width="2.5"/>'
         f'<rect x="300" y="130" width="8" height="34" rx="2" fill="#9AA4A0"/>')
    b += (f'<rect x="150" y="32" width="100" height="62" rx="3" fill="#1B232B"/><rect x="156" y="38" width="88" height="50" fill="#0F3B57"/>'
          f'<rect x="162" y="46" width="40" height="5" fill="#5FD38A"/><rect class="ci-bar" x="162" y="58" width="76" height="6" fill="{S}" style="transform-origin:162px 61px"/>'
          f'<rect x="162" y="70" width="22" height="10" fill="#2FA35A"/><rect x="190" y="70" width="22" height="10" fill="{B}"/>')
    for r in range(2):
        y = 122 + r*80
        for i in range(8):
            x = 104 + i*25
            b += f'<circle class="ci-lamba{" ci-yan" if (i+r) % 3 == 0 else ""}" cx="{x}" cy="{y}" r="6.5" fill="#2FA35A" stroke="#1E6E3C"/>'
            b += f'<circle cx="{x}" cy="{y+20}" r="6.5" fill="#C0392B" stroke="#7E241C" opacity="{.95 if (i+r)%4==1 else .45}"/>'
            b += (f'<circle cx="{x}" cy="{y+44}" r="8" fill="#2C3640"/>'
                  f'<rect x="{x-1.5}" y="{y+36}" width="3" height="16" rx="1" fill="#B9C0BD" transform="rotate({-30 if i%2 else 30} {x} {y+44})"/>'
                  f'<rect x="{x-8}" y="{y+56}" width="16" height="4" fill="{W}" stroke="{G}" stroke-width=".5"/>')
    b += f'<circle cx="286" cy="58" r="14" fill="{S}"/><circle cx="286" cy="58" r="9" fill="#C0392B" stroke="#7E241C"/>'
    return svg(b, "Kumanda panosu kapağı ve operatör ekranı temsili çizimi")

# ---------- 4. Kompanzasyon panosu ----------
def kompanzasyon():
    b = kasa()
    b += (f'<rect x="155" y="34" width="90" height="46" rx="3" fill="#2E3A44" stroke="{L}" stroke-width="1.5"/>'
          f'<rect x="162" y="40" width="76" height="22" fill="#0E1A22"/><text x="168" y="56" font-family="monospace" font-size="12" fill="#5FD38A" class="ci-cos">cos 0.99</text>')
    for i in range(6): b += led(168+i*12, 70, "#2FA35A" if i < 4 else "#5D6A72", "ci-yanip" if i == 3 else "")
    b += kanal(85, 88, 230) + ray(85, 120, 230)
    for i in range(8): b += kontaktor(96+i*27, 120)
    b += kanal(85, 142, 230) + ray(85, 168, 230) + mcb(96, 168, 16)
    for i in range(8):
        x = 100 + i*27
        b += (f'<rect x="{x-8}" y="196" width="18" height="62" rx="5" fill="#C9D0D3" stroke="#6E7874"/>'
              f'<rect x="{x-8}" y="196" width="18" height="10" rx="3" fill="#8E9BA6"/>'
              f'<line x1="{x+1}" y1="206" x2="{x+1}" y2="256" stroke="{W}" stroke-width="2" opacity=".6"/>')
    return svg(b, "Kompanzasyon panosu temsili çizimi")

# ---------- 5. Trafo ve güç artırımı ----------
def trafo():
    b = '<rect x="0" y="246" width="400" height="54" fill="#D9DEDB"/>'
    b += f'<path d="M20 30 L180 30 M20 44 L180 44 M20 58 L180 58" stroke="{L}" stroke-width="1.5"/>'
    b += f'<path class="ci-akim" d="M20 30 L180 30" stroke="{S}" stroke-width="3" stroke-dasharray="10 14"/>'
    for i, y in enumerate([30, 44, 58]):
        b += f'<line x1="{140+i*14}" y1="{y}" x2="{140+i*14}" y2="104" stroke="{L}" stroke-width="1.5"/>'
        b += f'<rect x="{135+i*14}" y="{y-2}" width="10" height="5" fill="{W}" stroke="{L}"/>'
    b += (f'<rect x="100" y="104" width="130" height="142" rx="4" fill="#9FAEA9" stroke="{L}" stroke-width="2.5"/>'
          f'<rect x="112" y="116" width="106" height="16" fill="#B7C3BF" stroke="{L}"/>')
    for i in range(9): b += f'<rect x="{110+i*12}" y="140" width="6" height="96" fill="#B7C3BF" stroke="#6E7874" stroke-width=".8"/>'
    b += f'<path d="M165 170 l-8 16 h10 l-8 16" stroke="{S}" stroke-width="3" fill="none"/>'
    b += (f'<rect x="262" y="120" width="104" height="126" rx="3" fill="#ECEEED" stroke="{L}" stroke-width="2.2"/>'
          f'<rect x="276" y="134" width="76" height="30" fill="#1B232B"/><text x="282" y="155" font-family="monospace" font-size="13" fill="#5FD38A" class="ci-kw">250 kW</text>'
          f'<rect x="276" y="176" width="34" height="56" fill="{W}" stroke="{G}"/><rect x="318" y="176" width="34" height="56" fill="{W}" stroke="{G}"/>'
          f'<circle cx="293" cy="196" r="8" fill="none" stroke="{L}"/><circle cx="335" cy="196" r="8" fill="none" stroke="{L}"/>')
    b += f'<path class="ci-akim" d="M230 210 H262" stroke="{S}" stroke-width="3" stroke-dasharray="6 8"/>'
    return svg(b, "Trafo ve güç artırımı temsili çizimi")

# ---------- 6. Elektrik altyapısı ----------
def altyapi():
    b = (f'<rect x="0" y="0" width="400" height="92" fill="#E9EEF1"/>'
         f'<rect x="0" y="92" width="400" height="208" fill="#B79A78"/>'
         f'<rect x="0" y="92" width="400" height="14" fill="#8B8F8C"/>')
    for i in range(26):
        b += f'<circle cx="{(i*53)%400}" cy="{120+(i*37)%160}" r="{2+(i%3)}" fill="#9C805F"/>'
    b += (f'<path d="M120 106 L140 270 H260 L280 106 Z" fill="#C8AE8C"/>'
          f'<rect x="140" y="236" width="120" height="34" fill="#E1D3B0"/>')
    for i in range(4):
        x = 160 + i*26
        b += f'<circle cx="{x}" cy="250" r="9" fill="#C0392B" stroke="#7E241C"/><circle cx="{x}" cy="250" r="4" fill="#1B232B"/>'
    b += f'<rect x="140" y="214" width="120" height="6" fill="{B}" opacity=".85"/><text x="160" y="211" font-family="Barlow,Arial" font-size="9" fill="{L}" font-weight="600">İKAZ BANDI</text>'
    b += (f'<rect x="30" y="22" width="80" height="70" fill="{W}" stroke="{L}" stroke-width="2"/>'
          f'<rect x="44" y="40" width="20" height="18" fill="#BFD3E2" stroke="{L}"/><rect x="74" y="40" width="20" height="18" fill="#BFD3E2" stroke="{L}"/>'
          f'<rect x="300" y="36" width="56" height="56" rx="3" fill="#ECEEED" stroke="{L}" stroke-width="2"/><rect x="310" y="46" width="36" height="8" fill="{L}"/>')
    b += f'<path class="ci-akim" d="M110 80 H150 V250 M250 250 V80 H300" fill="none" stroke="{S}" stroke-width="3" stroke-dasharray="8 10"/>'
    return svg(b, "Elektrik altyapısı ve kablo döşemesi temsili çizimi")

# ---------- 7. Jeneratör ve transfer panosu ----------
def jenerator():
    b = '<rect x="0" y="250" width="400" height="50" fill="#D9DEDB"/>'
    b += (f'<rect x="30" y="130" width="200" height="120" rx="6" fill="#3F6E57" stroke="{L}" stroke-width="2.5"/>'
          f'<rect x="44" y="146" width="80" height="58" rx="3" fill="#355C49"/>')
    for i in range(7): b += f'<rect x="{50+i*10}" y="152" width="5" height="46" fill="#2A4A3A"/>'
    b += (f'<rect x="140" y="146" width="74" height="40" rx="3" fill="#1B232B"/><text x="148" y="171" font-family="monospace" font-size="12" fill="#5FD38A">400 V</text>'
          f'<rect x="200" y="96" width="14" height="36" fill="#6E7874"/>')
    for i in range(3):
        b += f'<circle class="ci-duman ci-d{i}" cx="207" cy="88" r="{6+i*2}" fill="#B9C0BD" opacity=".6"/>'
    b += (f'<rect x="262" y="70" width="100" height="180" rx="3" fill="#ECEEED" stroke="{L}" stroke-width="2.2"/>'
          f'<text x="296" y="92" font-family="Barlow,Arial" font-size="13" fill="{L}" font-weight="700">ATS</text>'
          f'<rect x="276" y="104" width="72" height="34" fill="#1B232B"/><text x="282" y="125" font-family="monospace" font-size="10" fill="#5FD38A">ŞEBEKE</text>')
    b += led(286, 152, "#2FA35A", "ci-yanip") + led(300, 152, "#5D6A72") + led(314, 152, S)
    b += (f'<rect x="280" y="166" width="24" height="40" fill="#4A5763"/><rect x="316" y="166" width="24" height="40" fill="#4A5763"/>'
          f'<rect x="288" y="176" width="8" height="18" fill="{S}"/><rect x="324" y="176" width="8" height="18" fill="#9AA4A0"/>')
    b += f'<path class="ci-akim" d="M230 200 H262" stroke="{S}" stroke-width="3" stroke-dasharray="6 8"/>'
    return svg(b, "Jeneratör ve otomatik transfer panosu temsili çizimi")

# ---------- 8. Paratoner ----------
def paratoner():
    b = '<rect x="0" y="246" width="400" height="54" fill="#B79A78"/>'
    b += (f'<rect x="110" y="96" width="180" height="150" fill="{W}" stroke="{L}" stroke-width="2.5"/>'
          f'<path d="M98 100 L200 50 L302 100 Z" fill="#D8DCDA" stroke="{L}" stroke-width="2.5"/>')
    for r in range(2):
        for i in range(3):
            b += f'<rect x="{132+i*50}" y="{118+r*56}" width="32" height="34" fill="#BFD3E2" stroke="{L}"/>'
    b += (f'<line x1="200" y1="50" x2="200" y2="10" stroke="{L}" stroke-width="3"/>'
          f'<path d="M193 18 L200 4 L207 18" fill="none" stroke="{L}" stroke-width="2.5"/>'
          f'<path d="M200 50 L300 100 L300 246 L300 286" fill="none" stroke="{B}" stroke-width="3"/>'
          f'<line x1="300" y1="286" x2="300" y2="296" stroke="{B}" stroke-width="5"/>'
          f'<path d="M282 296 H318" stroke="{B}" stroke-width="3"/>')
    b += f'<path class="ci-simsek" d="M60 0 L44 44 H62 L46 90 L92 32 H70 L84 0 Z" fill="{S}" stroke="#C98A00"/>'
    return svg(b, "Paratoner ve topraklama temsili çizimi")

# ---------- 9. Araç şarj istasyonu ----------
def sarj():
    b = (f'<rect x="0" y="0" width="400" height="236" fill="#E6E9E7"/><rect x="0" y="236" width="400" height="64" fill="#C9CFCC"/>'
         f'<line x1="0" y1="236" x2="400" y2="236" stroke="#9AA4A0" stroke-width="2"/>')
    b += (f'<rect x="300" y="72" width="56" height="88" rx="10" fill="{W}" stroke="{L}" stroke-width="2.5"/>'
          f'<rect x="312" y="86" width="32" height="18" rx="3" fill="#0F3B57"/>'
          f'<path d="M330 112 l-7 13 h8 l-7 13" stroke="{S}" stroke-width="2.5" fill="none"/>'
          f'<rect class="ci-sarjled" x="314" y="146" width="28" height="4" rx="2" fill="#2FA35A"/>')
    b += f'<path d="M328 160 C328 220 250 214 238 176" fill="none" stroke="#1B232B" stroke-width="5" stroke-linecap="round"/>'
    # genel araç silueti (markasız)
    b += (f'<path d="M34 214 L44 176 Q50 160 70 156 L104 150 Q122 128 152 124 L198 122 Q222 122 240 140 L256 156 Q276 160 280 176 L282 214 Z" fill="#7C8C98" stroke="{L}" stroke-width="2.5"/>'
          f'<path d="M112 152 Q128 134 152 132 L182 131 L184 152 Z M192 131 L204 131 Q222 132 236 152 L194 152 Z" fill="#CFE0EA" stroke="{L}" stroke-width="1.5"/>'
          f'<circle cx="92" cy="216" r="22" fill="#1B232B"/><circle cx="92" cy="216" r="9" fill="#9AA4A0"/>'
          f'<circle cx="236" cy="216" r="22" fill="#1B232B"/><circle cx="236" cy="216" r="9" fill="#9AA4A0"/>')
    b += (f'<rect x="150" y="62" width="70" height="30" rx="6" fill="{W}" stroke="{L}" stroke-width="1.5"/>'
          f'<rect x="158" y="70" width="48" height="14" rx="2" fill="none" stroke="{L}" stroke-width="1.5"/><rect x="206" y="74" width="4" height="6" fill="{L}"/>'
          f'<rect class="ci-pil" x="160" y="72" width="44" height="10" fill="#2FA35A" style="transform-origin:160px 77px"/>')
    return svg(b, "Elektrikli araç şarj istasyonu temsili çizimi")

ISLER = [
    ("plc", "PLC kontrol panoları", "PLC, güç kaynağı, kontaktör ve klemens düzeniyle makine kumanda panoları.", plc_panosu),
    ("motor", "Motor kontrol panoları", "Motor koruma şalterleri, kontaktörler ve hız kontrol sürücülü çıkışlar.", motor_panosu),
    ("kapak", "Kumanda kapağı ve operatör ekranı", "Lamba, buton, selektör ve dokunmatik ekranla anlaşılır kullanım.", kapak),
    ("kompanzasyon", "Kompanzasyon panoları", "Reaktif güç rölesi, kademe kontaktörleri ve kondansatör grupları.", kompanzasyon),
    ("trafo", "Trafo ve güç artırımı", "Trafo bağlantısı, güç artırımı ve ana dağıtım panosu yenileme.", trafo),
    ("altyapi", "Elektrik altyapısı", "Kablo kanalı, yeraltı kablo döşemesi ve bina dağıtım hatları.", altyapi),
    ("jenerator", "Jeneratör ve ATS panoları", "Şebeke kesildiğinde jeneratöre otomatik geçiş yapan transfer panoları.", jenerator),
    ("paratoner", "Paratoner ve topraklama", "Yakalama ucu, iniş iletkeni ve topraklama elektrodu montajı.", paratoner),
    ("sarj", "Araç şarj istasyonları", "Ev, site ve işletmeler için uygun korumalı şarj istasyonu kurulumu.", sarj),
]

if __name__ == "__main__":
    import json, sys
    out = [{"id": i, "baslik": t, "metin": m, "svg": f()} for i, t, m, f in ISLER]
    json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False)
    # tek sayfa önizleme
    html = "<html><body style='margin:0;background:#fff;display:grid;grid-template-columns:repeat(3,400px);gap:8px;padding:8px'>" + "".join(f"<div>{o['svg']}<p style='font:14px sans-serif'>{o['baslik']}</p></div>" for o in out) + "</body></html>"
    open(sys.argv[1].replace(".json", ".html"), "w").write(html)
