# Giriş (hero) hikâyeli animasyon sahnelerini üretir: figure HTML + CSS + JS.
# Her sahne: sorun -> Wirbel ekibi gelir -> pano/çözüm kurulur -> sonuç.
L = "#033246"; B = "#7A3848"; S = "#F2A900"; G = "#B9C0BD"; P = "#E3E6E2"; W = "#FFFFFF"
KOYU = "#5D6A72"; YESIL = "#2FA35A"; KIRMIZI = "#C0392B"; TEN = "#F1C9A5"

def st(t=None, l=None, extra=""):
    v = []
    if t is not None: v.append(f"--t:{t}s")
    if l is not None: v.append(f"--l:{l}")
    if extra: v.append(extra)
    return f' style="{";".join(v)}"' if v else ""

def g(cls, inner, t=None, l=None, extra=""):
    return f'<g class="{cls}"{st(t, l, extra)}>{inner}</g>'

def zemin(renk="#D9DEDB"):
    return f'<rect x="0" y="252" width="520" height="48" fill="{renk}"/>'

def kisi(x, y, govde, kask=False, mutlu_t=None, uzgun=False, el_yukari=False):
    """Basit insan figürü. y = ayak hizası. uzgun=True ise üzgün yüz, mutlu_t'de mutlu yüze döner."""
    hy = y - 50
    s = (f'<line x1="{x-4}" y1="{y-14}" x2="{x-6}" y2="{y}" stroke="{L}" stroke-width="4" stroke-linecap="round"/>'
         f'<line x1="{x+4}" y1="{y-14}" x2="{x+6}" y2="{y}" stroke="{L}" stroke-width="4" stroke-linecap="round"/>'
         f'<rect x="{x-10}" y="{y-40}" width="20" height="28" rx="6" fill="{govde}"/>')
    if el_yukari:
        s += f'<line x1="{x+9}" y1="{y-36}" x2="{x+20}" y2="{y-50}" stroke="{govde}" stroke-width="5" stroke-linecap="round"/>'
    s += f'<circle cx="{x}" cy="{hy}" r="10" fill="{TEN}" stroke="{L}" stroke-width="1.2"/>'
    if kask:
        s += f'<path d="M{x-11} {hy-2} Q{x} {hy-17} {x+11} {hy-2} Z" fill="{S}" stroke="#C98A00" stroke-width="1"/>'
    s += f'<circle cx="{x-3.5}" cy="{hy-1}" r="1.3" fill="{L}"/><circle cx="{x+3.5}" cy="{hy-1}" r="1.3" fill="{L}"/>'
    mutlu = f'<path d="M{x-4} {hy+3} Q{x} {hy+8} {x+4} {hy+3}" fill="none" stroke="{L}" stroke-width="1.5" stroke-linecap="round"/>'
    uz = f'<path d="M{x-4} {hy+6} Q{x} {hy+2} {x+4} {hy+6}" fill="none" stroke="{L}" stroke-width="1.5" stroke-linecap="round"/>'
    if uzgun:
        s += g("g-out", uz, t=mutlu_t) + g("g-in", mutlu, t=mutlu_t)
    else:
        s += mutlu
    return s

def teknisyen(x, y, t):
    """Wirbel ekibi: sağdan yürüyerek gelir."""
    return g("g-walk", kisi(x, y, B, kask=True), t=t)

def fabrika(x, y, w, h, pencere_cls="", pt=None, pencere_extra=""):
    s = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{P}" stroke="{L}" stroke-width="2.2"/>')
    # testere çatı
    n = 4; dw = w / n
    path = f"M{x} {y}"
    for i in range(n):
        path += f" L{x+i*dw+dw*0.75:.0f} {y-26} L{x+(i+1)*dw:.0f} {y-26} L{x+(i+1)*dw:.0f} {y}"
    s += f'<path d="{path}" fill="#CBD1CE" stroke="{L}" stroke-width="2"/>'
    s += f'<rect x="{x+w-30}" y="{y-58}" width="14" height="34" fill="#9AA4A0" stroke="{L}" stroke-width="1.5"/>'
    cols = int((w - 20) // 34)
    for r in range(2):
        for c in range(cols):
            wx = x + 14 + c * 34; wy = y + 14 + r * 32
            s += f'<rect class="{pencere_cls}" x="{wx}" y="{wy}" width="22" height="20" fill="{KOYU}" stroke="{L}" stroke-width="1"{st(pt, extra=pencere_extra) if pt is not None else ""}/>'
    return s

def pano(x, y, w=40, h=66, tip="plc", t=None):
    """Küçük pano ikonu (kurulum anı için)."""
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#ECEEED" stroke="{L}" stroke-width="2"/>'
    if tip == "plc":
        s += f'<rect x="{x+6}" y="{y+8}" width="{w-12}" height="14" fill="{W}" stroke="{L}"/><text x="{x+9}" y="{y+19}" font-family="Barlow,Arial" font-size="8" font-weight="700" fill="{L}">PLC</text>'
        for i in range(4): s += f'<circle class="g-blink" cx="{x+9+i*7}" cy="{y+30}" r="2" fill="{YESIL if i%2==0 else S}"{st(t+0.6 if t else 0, extra=f"animation-delay:calc(var(--t) + {i*0.2}s)")}/>'
        for i in range(4): s += f'<rect x="{x+6+i*7}" y="{y+40}" width="5" height="12" fill="#5D7186"/>'
    elif tip == "motor":
        for i in range(4): s += f'<rect x="{x+5+i*8}" y="{y+8}" width="6" height="16" fill="#4A5763"/><rect x="{x+6+i*8}" y="{y+20}" width="4" height="3" fill="{S}"/>'
        for i in range(4): s += f'<rect x="{x+5+i*8}" y="{y+30}" width="6" height="14" fill="#5D7186"/>'
        for i in range(4): s += f'<circle class="g-blink" cx="{x+8+i*8}" cy="{y+54}" r="2" fill="{YESIL}"{st(t+0.6 if t else 0, extra=f"animation-delay:calc(var(--t) + {i*0.25}s)")}/>'
    elif tip == "komp":
        s += f'<rect x="{x+5}" y="{y+6}" width="{w-10}" height="14" fill="#0E1A22"/>'
        s += g("g-in", f'<text x="{x+7}" y="{y+16}" font-family="monospace" font-size="7.5" fill="#5FD38A">cos 0.99</text>', t=(t or 0)+0.8)
        for i in range(4): s += f'<rect x="{x+6+i*8}" y="{y+40}" width="6" height="20" rx="2" fill="#C9D0D3" stroke="#6E7874" stroke-width=".6"/>'
        for i in range(4): s += f'<rect x="{x+6+i*8}" y="{y+25}" width="6" height="10" fill="#5D7186"/>'
    return s

def baslik(metin, t, renk=YESIL, x=260):
    w = 10 + len(metin) * 7.2
    return g("g-pop",
             f'<rect x="{x-w/2:.0f}" y="10" width="{w:.0f}" height="26" rx="13" fill="{renk}"/>'
             f'<text x="{x}" y="28" text-anchor="middle" font-family="Barlow,Arial" font-size="13.5" font-weight="600" fill="#fff">{metin}</text>', t=t)

def uyari(metin, t, x=260, renk=B, cls="g-pop"):
    w = 10 + len(metin) * 7.2
    return g(cls, f'<rect x="{x-w/2:.0f}" y="10" width="{w:.0f}" height="26" rx="13" fill="{renk}"/>'
                  f'<text x="{x}" y="28" text-anchor="middle" font-family="Barlow,Arial" font-size="13.5" font-weight="600" fill="#fff">{metin}</text>', t=t)

def motor(cx, cy, t):
    return (f'<rect x="{cx-22}" y="{cy-16}" width="34" height="32" rx="5" fill="#5D7186" stroke="{L}" stroke-width="1.8"/>'
            f'<rect x="{cx+12}" y="{cy-4}" width="10" height="8" fill="#8E9BA6" stroke="{L}"/>'
            f'<circle cx="{cx-5}" cy="{cy}" r="11" fill="#1B232B"/>'
            + g("g-spin", f'<path d="M{cx-5} {cy-9} V{cy+9} M{cx-14} {cy} H{cx+4} M{cx-11} {cy-6} L{cx+1} {cy+6} M{cx+1} {cy-6} L{cx-11} {cy+6}" stroke="{S}" stroke-width="2"/>', t=t))

def fatura(x, y, ceza, renk, t_in=None, t_out=None, cls=""):
    inner = (f'<rect x="{x}" y="{y}" width="74" height="92" rx="2" fill="{W}" stroke="{L}" stroke-width="1.5"/>'
             f'<text x="{x+37}" y="{y+16}" text-anchor="middle" font-family="Barlow,Arial" font-size="11" font-weight="700" fill="{L}">FATURA</text>'
             f'<line x1="{x+8}" y1="{y+24}" x2="{x+66}" y2="{y+24}" stroke="{G}"/><line x1="{x+8}" y1="{y+32}" x2="{x+56}" y2="{y+32}" stroke="{G}"/>'
             f'<text x="{x+37}" y="{y+52}" text-anchor="middle" font-family="Barlow,Arial" font-size="10" fill="{L}">Reaktif ceza</text>'
             f'<text x="{x+37}" y="{y+74}" text-anchor="middle" font-family="Barlow,Arial" font-size="17" font-weight="700" fill="{renk}">{ceza}</text>')
    return inner

def akim_yolu(d, t, w=3):
    return f'<path class="g-flow" d="{d}" fill="none" stroke="{S}" stroke-width="{w}" stroke-dasharray="7 9"{st(t)}/>'

def ciz_yolu(d, t, l, renk=L, w=2.2):
    return f'<path class="g-draw" d="{d}" fill="none" stroke="{renk}" stroke-width="{w}"{st(t, l)}/>'

def tesis_isigi(t):
    return f'<rect class="g-glow" x="0" y="0" width="520" height="252" fill="{S}"{st(t)}/>'

# ---------------- SAHNELER ----------------
def sahne_plc():
    b = zemin()
    b += uyari("Hat duruyor", 0.2, cls="g-popout", x=170)
    b += fabrika(20, 120, 260, 132, "g-lit", pt=4.0)
    # konveyör
    b += f'<rect x="24" y="236" width="252" height="10" rx="5" fill="#9AA4A0" stroke="{L}" stroke-width="1.2"/>'
    for i in range(3):
        b += g("g-belt", f'<rect x="30" y="218" width="22" height="18" fill="#D9B27A" stroke="#8A6A3A"/>', t=4.2, extra=f"animation-delay:calc(var(--t) + {i*1.1}s)")
    b += teknisyen(400, 252, 0.8)
    b += g("g-drop", pano(318, 176, tip="plc", t=2.6), t=2.4)
    b += ciz_yolu("M318 200 H280", 3.2, 40)
    b += akim_yolu("M318 200 H280", 3.6)
    b += baslik("PLC panosu kuruldu, hat çalışıyor ✓", 4.8)
    return b

def sahne_motor():
    b = zemin()
    b += uyari("Pompalar çalışmıyor", 0.2, cls="g-popout", x=200)
    # boru hattı
    b += f'<path d="M30 168 H330" stroke="#8E9BA6" stroke-width="10" fill="none"/>'
    b += f'<path class="g-flow" d="M30 168 H330" fill="none" stroke="#5DADE2" stroke-width="4" stroke-dasharray="10 10"{st(5.2)}/>'
    for i, x in enumerate([70, 150, 230, 310]):
        b += f'<line x1="{x-5}" y1="168" x2="{x-5}" y2="214" stroke="#8E9BA6" stroke-width="6"/>'
        b += motor(x, 228, 4.2 + i * 0.35)
    b += teknisyen(450, 252, 0.8)
    b += g("g-drop", pano(372, 176, tip="motor", t=2.6), t=2.4)
    b += ciz_yolu("M372 196 H350 V140 H65 V212 M145 140 V212 M225 140 V212 M305 140 V212", 3.2, 700, renk=KIRMIZI, w=1.8)
    b += baslik("4 motor tek panodan kontrol ediliyor ✓", 5.0)
    return b

def sahne_komp():
    b = zemin()
    b += fabrika(250, 140, 200, 112)
    b += kisi(90, 252, "#5D7186", uzgun=True, mutlu_t=5.2, el_yukari=True)
    b += g("g-out", fatura(104, 112, "1.000 TL", KIRMIZI), t=5.0)
    b += g("g-in", fatura(104, 112, "0 TL", YESIL), t=5.2)
    b += uyari("Reaktif ceza!", 0.4, cls="g-popout", x=140)
    b += teknisyen(480, 252, 1.2)
    b += g("g-drop", pano(176, 186, tip="komp", t=3.0), t=2.8)
    b += ciz_yolu("M216 210 H250", 3.6, 34)
    b += baslik("Yeni faturada ceza yok ✓", 5.6, x=300)
    b += g("g-pop", f'<text x="70" y="168" font-size="20">✨</text>', t=5.6)
    return b

def sahne_trafo():
    b = zemin()
    b += fabrika(20, 130, 240, 122, "g-flick", pt=1.0)
    b += tesis_isigi(6.0)
    # müşteri ve buton
    b += kisi(300, 252, "#5D7186", uzgun=True, mutlu_t=6.2, el_yukari=True)
    b += (f'<rect x="318" y="196" width="26" height="56" fill="#ECEEED" stroke="{L}" stroke-width="1.5"/>'
          f'<circle class="g-press" cx="331" cy="212" r="8" fill="{YESIL}" stroke="#1E6E3C"{st(0.8)}/>'
          f'<text x="331" y="240" text-anchor="middle" font-family="Barlow,Arial" font-size="8" font-weight="700" fill="{L}">START</text>')
    b += uyari("⚠ Güç yetersiz!", 1.6, cls="g-popout2", x=150)
    # eski trafo
    b += g("g-out", f'<rect x="400" y="196" width="46" height="56" rx="3" fill="#9FAEA9" stroke="{L}" stroke-width="2"/>'
                    f'<text x="423" y="221" text-anchor="middle" font-family="Barlow,Arial" font-size="8" font-weight="700" fill="{L}">DÜŞÜK</text><text x="423" y="232" text-anchor="middle" font-family="Barlow,Arial" font-size="8" font-weight="700" fill="{L}">KAPASİTE</text>'
                    f'<path d="M404 200 L442 248 M442 200 L404 248" stroke="{KIRMIZI}" stroke-width="3"{st(2.2)} class="g-in"/>', t=4.0)
    b += teknisyen(480, 252, 3.4)
    b += g("g-drop", f'<rect x="384" y="168" width="78" height="84" rx="4" fill="#9FAEA9" stroke="{L}" stroke-width="2.4"/>'
                     + "".join(f'<rect x="{392+i*10}" y="190" width="5" height="54" fill="#B7C3BF" stroke="#6E7874" stroke-width=".7"/>' for i in range(7))
                     + f'<rect x="392" y="174" width="62" height="12" fill="{L}"/><text x="423" y="184" text-anchor="middle" font-family="Barlow,Arial" font-size="8.5" font-weight="700" fill="#fff">YENİ TRAFO</text>', t=4.4)
    b += akim_yolu("M384 230 H344 M318 230 H260", 5.6)
    b += baslik("Güç artırıldı, tesis tam kapasite ✓", 6.4)
    return b

def sahne_paratoner():
    b = zemin()
    b += fabrika(90, 130, 260, 122, "g-lit", pt=0)
    b += f'<rect class="g-dark" x="0" y="0" width="520" height="300" fill="#1B2A36"{st(3.8)}/>'
    # cihaz ekranları
    for i in range(3):
        b += f'<rect x="{150+i*60}" y="210" width="30" height="22" fill="#0E1A22" stroke="{L}"/><rect class="g-okscreen" x="{154+i*60}" y="214" width="22" height="14" fill="{YESIL}"/>'
    b += teknisyen(450, 252, 0.6)
    b += ciz_yolu("M220 104 V58", 1.8, 46, w=3.5)
    b += g("g-in", f'<path d="M213 66 L220 52 L227 66" fill="none" stroke="{L}" stroke-width="3"/>', t=2.2)
    b += ciz_yolu("M220 104 L350 130 H362 V276", 2.4, 320, renk=B, w=3)
    b += ciz_yolu("M346 286 H378 M352 292 H372", 3.0, 40, renk=B, w=3)
    b += f'<path class="g-bolt" d="M200 -4 L184 26 H198 L180 52 L222 18 H206 L220 -4 Z" fill="{S}" stroke="#C98A00"{st(4.4)}/>'
    b += f'<rect class="g-flash" x="0" y="0" width="520" height="300" fill="#fff"{st(4.4)}/>'
    b += akim_yolu("M220 58 V104 L350 130 H362 V286", 4.6, 4)
    for r in range(3):
        b += f'<ellipse class="g-ripple" cx="362" cy="290" rx="{14+r*12}" ry="{4+r*3}" fill="none" stroke="{S}" stroke-width="2"{st(5.0+r*0.25)}/>'
    b += baslik("Yıldırım toprağa aktı, cihazlar güvende ✓", 5.8)
    return b

def sahne_sarj():
    def arac(x, y, renk):
        return (f'<path d="M{x} {y} L{x+6} {y-22} Q{x+10} {y-32} {x+24} {y-34} L{x+46} {y-36} Q{x+62} {y-52} {x+82} {y-52} L{x+108} {y-52} Q{x+122} {y-50} {x+132} {y-36} Q{x+146} {y-32} {x+150} {y-20} L{x+150} {y} Z" fill="{renk}" stroke="{L}" stroke-width="2"/>'
                f'<path d="M{x+52} {y-37} Q{x+64} {y-48} {x+80} {y-48} L{x+92} {y-48} L{x+92} {y-37} Z M{x+98} {y-48} L{x+106} {y-48} Q{x+118} {y-46} {x+126} {y-37} L{x+98} {y-37} Z" fill="#CFE0EA" stroke="{L}" stroke-width="1.2"/>'
                f'<circle cx="{x+34}" cy="{y+2}" r="13" fill="#1B232B"/><circle cx="{x+34}" cy="{y+2}" r="5" fill="#9AA4A0"/>'
                f'<circle cx="{x+118}" cy="{y+2}" r="13" fill="#1B232B"/><circle cx="{x+118}" cy="{y+2}" r="5" fill="#9AA4A0"/>')
    def istasyon(x):
        return (f'<rect x="{x}" y="150" width="26" height="62" rx="5" fill="{W}" stroke="{L}" stroke-width="1.8"/>'
                f'<rect x="{x+4}" y="158" width="18" height="12" fill="#0F3B57"/>'
                f'<rect x="{x-6}" y="128" width="38" height="16" rx="8" fill="{KIRMIZI}"/><text x="{x+13}" y="140" text-anchor="middle" font-family="Barlow,Arial" font-size="10" font-weight="700" fill="#fff">DOLU</text>')
    # A: otopark
    a = f'<rect x="0" y="0" width="520" height="252" fill="#E6E9E7"/>' + zemin("#C9CFCC")
    for bx, renk in [(20, "#8E9BA6"), (190, "#B0A08A"), (360, "#9C6B6B")]:
        a += f'<g transform="translate({bx} 60) scale(.62)">{arac(0, 250, renk)}</g>' + istasyon(bx + 100)
    a += g("g-drive", f'<g transform="translate(150 0)">{arac(0, 250, "#5D7186")}</g>', t=0.2)
    a += f'<g class="g-bubble"{st(1.8)}><rect x="150" y="56" width="132" height="32" rx="16" fill="{W}" stroke="{L}" stroke-width="1.5"/><text x="216" y="77" text-anchor="middle" font-family="Barlow,Arial" font-size="13" font-weight="600" fill="{B}">Hepsi dolu… 😕</text></g>'
    sahneA = g("g-sceneA", a, t=4.0)
    # B: villa
    bb = f'<rect x="0" y="0" width="520" height="252" fill="#EAF1F5"/>' + zemin("#BFD3A8")
    bb += (f'<path d="M250 110 L380 50 L510 110 Z" fill="{B}" stroke="{L}" stroke-width="2"/>'
           f'<rect x="266" y="110" width="228" height="142" fill="{W}" stroke="{L}" stroke-width="2.2"/>'
           f'<rect x="290" y="134" width="40" height="34" fill="#CFE0EA" stroke="{L}"/><rect x="430" y="134" width="40" height="34" fill="#CFE0EA" stroke="{L}"/>'
           f'<rect x="360" y="180" width="40" height="72" fill="#C9A27A" stroke="{L}"/>')
    bb += teknisyen(240, 252, 4.6)
    bb += g("g-drop", f'<rect x="284" y="178" width="28" height="44" rx="6" fill="{W}" stroke="{L}" stroke-width="2"/>'
                      f'<rect x="290" y="186" width="16" height="9" rx="2" fill="#0F3B57"/>'
                      f'<path d="M298 198 l-4 7 h5 l-4 7" stroke="{S}" stroke-width="2" fill="none"/>', t=5.4)
    bb += g("g-drive2", f'<g transform="translate(20 0)">{arac(0, 250, "#5D7186")}</g>', t=5.8)
    bb += ciz_yolu("M298 222 C298 246 200 250 180 236", 6.8, 140, renk="#1B232B", w=4)
    bb += (f'<g class="g-in"{st(6.9)}><rect x="40" y="70" width="70" height="30" rx="6" fill="{W}" stroke="{L}" stroke-width="1.5"/>'
           f'<rect x="48" y="78" width="48" height="14" rx="2" fill="none" stroke="{L}" stroke-width="1.5"/><rect x="96" y="82" width="4" height="6" fill="{L}"/>'
           f'<rect class="g-fill" x="50" y="80" width="44" height="10" fill="{YESIL}"{st(7.1)}/></g>')
    bb += baslik("Evinizde kendi şarj istasyonunuz ✓", 8.0)
    sahneB = g("g-sceneB", bb, t=4.0)
    return sahneA + sahneB

SAHNELER = [
    ("PLC", 8, sahne_plc, "PLC panosu kurulumu: duran üretim hattı panonun kurulmasıyla çalışmaya başlıyor"),
    ("Motor", 8, sahne_motor, "Motor kontrol panosu: dört pompa motoru tek panodan sırayla devreye giriyor"),
    ("Kompanzasyon", 9, sahne_komp, "Kompanzasyon: reaktif ceza yazan fatura, pano kurulduktan sonra sıfırlanıyor"),
    ("Trafo", 9, sahne_trafo, "Güç artırımı: güç yetersizliği yeni trafo ile gideriliyor ve tesis aydınlanıyor"),
    ("Paratoner", 8, sahne_paratoner, "Paratoner: yıldırım toprağa aktarılıyor, cihazlar zarar görmüyor"),
    ("Şarj", 10, sahne_sarj, "Şarj istasyonu: otoparktaki istasyonlar dolu, villaya kurulan istasyonla araç evde şarj oluyor"),
]

def figure():
    sah = "".join(f'<g class="sahne" data-sure="{s}" aria-label="{a}">{f()}</g>' for _, s, f, a in SAHNELER)
    lis = "".join(f'<li>{ad}<i></i></li>' for ad, *_ in SAHNELER)
    return f'''    <figure class="sema" id="anim" data-reveal style="--i:1">
      <svg viewBox="0 0 520 300" role="img" aria-labelledby="animBaslik">
        <title id="animBaslik">Çözüm hikâyeleri: PLC panosu, motor kontrol panosu, kompanzasyon, trafo ve güç artırımı, paratoner ve araç şarj istasyonu kurulumları</title>
        <defs><clipPath id="anim-kirp"><rect width="520" height="300"/></clipPath></defs>
        <g clip-path="url(#anim-kirp)">{sah}</g>
      </svg>
      <div class="anim-alt">
        <ol class="asamalar" aria-label="Senaryolar">{lis}</ol>
        <button type="button" class="dur" aria-pressed="false">Durdur</button>
      </div>
    </figure>
'''

CSS = r'''
/* Hikâyeli giriş animasyonu */
.sahne{opacity:0;transition:opacity .5s;pointer-events:none}
.sahne.aktif{opacity:1}
.sahne [class*="g-"]{transform-box:fill-box;transform-origin:center}
.aktif .g-in{animation:g-in .55s var(--yumusak) var(--t,0s) both}
.aktif .g-out{animation:g-out .45s ease var(--t,0s) both}
.aktif .g-pop{animation:g-pop .5s cubic-bezier(.3,1.6,.5,1) var(--t,0s) both}
.aktif .g-popout{animation:g-pop .5s cubic-bezier(.3,1.6,.5,1) var(--t,0s) both,g-out .4s ease 2.2s forwards}
.aktif .g-popout2{animation:g-pop .5s cubic-bezier(.3,1.6,.5,1) var(--t,0s) both,g-out .4s ease 3.8s forwards}
.aktif .g-walk{animation:g-walk 1.1s var(--yumusak) var(--t,0s) both}
.aktif .g-drop{animation:g-drop .7s cubic-bezier(.3,1.4,.5,1) var(--t,0s) both}
.aktif .g-lit{animation:g-lit .6s ease var(--t,0s) both}
.aktif .g-flick{animation:g-flick 2.4s steps(1) var(--t,0s) both,g-lit .6s ease 6s forwards}
.aktif .g-glow{animation:g-glow 1.2s ease var(--t,0s) both}
.aktif .g-belt{animation:g-show .3s var(--t,0s) both,g-belt 3.3s linear var(--t,0s) infinite}
.aktif .g-spin{animation:g-spin .7s linear var(--t,0s) infinite}
.aktif .g-blink{animation:g-blink 1s ease-in-out var(--t,0s) infinite}
.aktif .g-draw{stroke-dasharray:var(--l);animation:g-draw .9s var(--yumusak) var(--t,0s) both}
.aktif .g-flow{animation:g-show .3s var(--t,0s) both,g-flow 1s linear var(--t,0s) infinite}
.aktif .g-press{animation:g-press .5s ease var(--t,0s) both}
.aktif .g-dark{animation:g-dark 3.2s ease var(--t,0s) both}
.aktif .g-bolt{animation:g-bolt 1s steps(1) var(--t,0s) both}
.aktif .g-flash{animation:g-flash .6s ease var(--t,0s) both}
.aktif .g-ripple{animation:g-ripple 1s ease-out var(--t,0s) both}
.aktif .g-okscreen{animation:g-blink 1.6s ease-in-out 4.6s infinite}
.aktif .g-sceneA{animation:g-out .6s ease var(--t,0s) forwards}
.aktif .g-sceneB{animation:g-in .6s ease var(--t,0s) both}
.aktif .g-drive{animation:g-drive 1.8s var(--yumusak) var(--t,0s) both}
.aktif .g-drive2{animation:g-drive 1.4s var(--yumusak) var(--t,0s) both}
.aktif .g-bubble{animation:g-pop .5s cubic-bezier(.3,1.6,.5,1) var(--t,0s) both}
.aktif .g-fill{animation:g-fill 1.6s linear var(--t,0s) both}
.g-out{opacity:1}.g-in,.g-pop,.g-sceneB{opacity:1}
@keyframes g-in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes g-out{to{opacity:0}}
@keyframes g-show{from{opacity:0}to{opacity:1}}
@keyframes g-pop{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:none}}
@keyframes g-walk{from{opacity:0;transform:translateX(120px)}to{opacity:1;transform:none}}
@keyframes g-drop{from{opacity:0;transform:translateY(-60px)}to{opacity:1;transform:none}}
@keyframes g-lit{from{fill:#5D6A72}to{fill:#F2C14E}}
@keyframes g-flick{0%{fill:#5D6A72}8%{fill:#F2C14E}14%{fill:#5D6A72}22%{fill:#F2C14E}28%{fill:#5D6A72}36%{fill:#F2C14E}42%,100%{fill:#3A444B}}
@keyframes g-glow{from{opacity:0}40%{opacity:.18}to{opacity:.06}}
@keyframes g-belt{from{transform:translateX(0)}to{transform:translateX(230px)}}
@keyframes g-spin{to{transform:rotate(360deg)}}
@keyframes g-blink{50%{opacity:.3}}
@keyframes g-draw{from{stroke-dashoffset:var(--l)}to{stroke-dashoffset:0}}
@keyframes g-flow{to{stroke-dashoffset:-32}}
@keyframes g-press{0%{transform:none}40%{transform:scale(.75);fill:#7BE09C}100%{transform:none}}
@keyframes g-dark{0%{opacity:0}20%,70%{opacity:.55}100%{opacity:0}}
@keyframes g-bolt{0%{opacity:0}1%,30%{opacity:1}31%,45%{opacity:0}46%,70%{opacity:1}71%,100%{opacity:0}}
@keyframes g-flash{0%{opacity:0}10%{opacity:.85}100%{opacity:0}}
@keyframes g-ripple{0%{opacity:0;transform:scale(.4)}15%{opacity:1}100%{opacity:0;transform:scale(1.6)}}
@keyframes g-drive{from{transform:translateX(-420px)}to{transform:none}}
@keyframes g-fill{from{transform:scaleX(.05)}to{transform:scaleX(1)}}
.sahne .g-fill{transform-origin:left center}
.g-glow,.g-dark,.g-flash,.g-bolt,.g-ripple{opacity:0}
.anim-alt{display:flex;align-items:flex-end;gap:14px;margin-top:10px}
.asamalar{list-style:none;display:grid;grid-template-columns:repeat(6,1fr);gap:6px;flex:1}
.asamalar li{font-size:12.5px;color:var(--gri);line-height:1.3;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.asamalar li.aktif{color:var(--lacivert);font-weight:600}
.asamalar i{display:block;height:4px;margin-top:5px;background:var(--cizgi);position:relative;overflow:hidden}
.asamalar i::after{content:"";position:absolute;inset:0;background:var(--sari);transform-origin:left;transform:scaleX(0)}
.asamalar li.bitti i::after{transform:scaleX(1)}
.asamalar li.aktif i::after{animation:dolum var(--sure,8s) linear forwards}
@keyframes dolum{to{transform:scaleX(1)}}
@media (max-width:520px){.asamalar{grid-template-columns:repeat(3,1fr);row-gap:8px}.asamalar li{font-size:11px;text-overflow:clip}}
.dur{font:inherit;font-size:13px;font-weight:600;color:var(--lacivert);background:#fff;border:1px solid var(--cizgi);border-radius:3px;padding:5px 12px;cursor:pointer;min-height:36px}
.durdu .sahne *,.durdu .asamalar i::after{animation-play-state:paused!important}
@media (prefers-reduced-motion:reduce){
  .sahne *{animation:none!important}
  .sahne .g-out,.sahne .g-sceneA,.sahne .g-popout,.sahne .g-popout2,.sahne .g-glow,.sahne .g-dark,.sahne .g-flash,.sahne .g-bolt,.sahne .g-ripple{display:none}
  .asamalar li.aktif i::after{animation:none;transform:scaleX(1)}
}
'''

JS = r'''(function(){
  var f=document.getElementById('anim'); if(!f) return;
  var s=[].slice.call(f.querySelectorAll('.sahne')), l=[].slice.call(f.querySelectorAll('.asamalar li')), b=f.querySelector('.dur');
  var i=-1, t, bas, kalan=0, durdu=false;
  function sure(n){ return (parseFloat(s[n].getAttribute('data-sure'))||8)*1000; }
  function goster(n){
    s.forEach(function(x){x.classList.remove('aktif')});
    l.forEach(function(x,k){x.classList.remove('aktif'); x.classList.toggle('bitti',k<n)});
    void f.offsetWidth;
    f.style.setProperty('--sure', sure(n)+'ms');
    s[n].classList.add('aktif'); l[n].classList.add('aktif');
  }
  function ileri(){ i=(i+1)%s.length; goster(i); kalan=sure(i); bas=Date.now(); t=setTimeout(ileri,kalan); }
  function durum(d){ durdu=d; f.classList.toggle('durdu',d); b.textContent=d?'Oynat':'Durdur'; b.setAttribute('aria-pressed',d?'true':'false'); }
  var az=window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(az){ i=2; goster(2); bas=Date.now(); kalan=sure(2); durum(true); }
  else {
    var pl=document.querySelector('.preloader');
    if(pl && getComputedStyle(pl).display!=='none'){ var basladi=false; var go=function(){ if(!basladi){ basladi=true; ileri(); } }; document.addEventListener('wb-hazir', go); setTimeout(go, 2600); }
    else ileri();
  }
  b.addEventListener('click',function(){
    if(!durdu){ clearTimeout(t); kalan-=Date.now()-bas; durum(true); }
    else { durum(false); bas=Date.now(); t=setTimeout(ileri,Math.max(kalan,0)); }
  });
  l.forEach(function(li,k){ li.style.cursor='pointer'; li.addEventListener('click',function(){ clearTimeout(t); durum(false); i=k-1; ileri(); }); });
})();
'''

if __name__ == "__main__":
    import json, sys
    json.dump({"figure": figure(), "css": CSS, "js": JS}, open(sys.argv[1], "w"), ensure_ascii=False)
