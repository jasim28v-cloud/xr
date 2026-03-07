import requests
import re
from datetime import datetime

def run():
    # روابط القناة والمعلومات الأساسية
    url = "https://t.me/s/kg33d"
    channel_url = "https://t.me/kg33d"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.encoding = 'utf-8'
        
        # استخراج كافة الروابط (VLESS, VMESS, TROJAN, SS)
        links = re.findall(r'(?:vless|vmess|trojan|ss|ssr)://[^\s<"\'\s]+', response.text)
        
        clean_links = []
        for l in links:
            c = l.replace('&amp;', '&').split('<')[0].split('"')[0].strip()
            if c not in clean_links: clean_links.append(c)
        
        # التوقيت الحالي
        now_date = datetime.now().strftime("%Y-%m-%d")
        now_time = datetime.now().strftime("%I:%M %p")
        
        # بناء البطاقات مع تمييز الألوان لكل نوع
        cards = ""
        for i, link in enumerate(clean_links):
            proto = link.split('://')[0].upper()
            # اختيار اللون حسب البروتوكول
            theme_color = "#00f2fe" # VLESS
            if proto == "VMESS": theme_color = "#f472b6"
            elif proto == "TROJAN": theme_color = "#fbbf24"
            elif proto == "SS": theme_color = "#a78bfa"
            
            cards += f'''
            <div class="card" style="border-right: 4px solid {theme_color}">
                <div class="card-header">
                    <span class="badge" style="background: {theme_color}; color: #0f172a;">{proto}</span>
                    <button class="btn-copy" onclick="copy('{link}')">نسخ 📋</button>
                </div>
                <div class="link-box">{link}</div>
                <button class="btn-qr" style="background: {theme_color}; color: #0f172a;" onclick="qr('q{i}','{link}')">إظهار الباركود 🔳</button>
                <div id="q{i}" class="qr-area"></div>
            </div>'''

        html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>X-Ray Elite Hub | منصة السيرفرات العالمية</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --p: #00f2fe; --bg: #030712; --c: #111827; }}
        body {{ background: var(--bg); color: white; font-family: 'Tajawal', sans-serif; padding: 20px; display: flex; flex-direction: column; align-items: center; margin: 0; }}
        
        .header {{ text-align: center; margin-bottom: 30px; margin-top: 20px; }}
        h1 {{ color: var(--p); margin: 0; font-size: 28px; text-shadow: 0 0 15px rgba(0,242,254,0.4); }}
        
        .join-btn {{ display: inline-block; background: #24A1DE; color: white; padding: 12px 25px; border-radius: 50px; text-decoration: none; font-weight: bold; margin-top: 15px; box-shadow: 0 4px 15px rgba(36,161,222,0.3); transition: 0.3s; font-size: 14px; }}
        .join-btn:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(36,161,222,0.5); }}

        .status-bar {{ font-size: 11px; color: #94a3b8; background: rgba(255,255,255,0.05); padding: 8px 20px; border-radius: 50px; margin-top: 15px; border: 1px solid #1f2937; }}
        
        .info-box {{ background: var(--c); border-radius: 15px; padding: 18px; width: 100%; max-width: 480px; margin-bottom: 25px; border-right: 5px solid var(--p); box-shadow: 0 4px 15px rgba(0,0,0,0.4); }}
        
        .card {{ background: var(--c); border-radius: 15px; padding: 18px; margin-bottom: 20px; width: 100%; max-width: 480px; transition: 0.3s; box-shadow: 0 8px 20px rgba(0,0,0,0.3); }}
        .card:hover {{ transform: translateY(-5px); border-color: white; }}
        
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }}
        .badge {{ padding: 4px 15px; border-radius: 8px; font-weight: bold; font-size: 12px; }}
        
        .btn-copy {{ background: #f3f4f6; border: none; padding: 7px 18px; border-radius: 10px; cursor: pointer; font-family: 'Tajawal'; font-weight: bold; font-size: 12px; transition: 0.2s; }}
        .btn-copy:hover {{ background: var(--p); }}

        .link-box {{ background: rgba(0,0,0,0.5); padding: 12px; border-radius: 12px; font-size: 10px; color: #94a3b8; word-break: break-all; direction: ltr; margin-bottom: 15px; border: 1px solid #1f2937; line-height: 1.5; }}
        
        .btn-qr {{ width: 100%; border: none; padding: 12px; border-radius: 12px; font-weight: bold; cursor: pointer; font-family: 'Tajawal'; transition: 0.3s; }}
        
        .qr-area {{ display: none; background: white; padding: 20px; margin-top: 15px; border-radius: 15px; text-align: center; animation: fadeIn 0.4s ease; }}
        .qr-area img {{ margin: 0 auto; border: 5px solid white; }}
        
        footer {{ text-align: center; margin: 50px 0; border-top: 1px solid #1f2937; padding-top: 20px; width: 100%; max-width: 480px; }}
        .footer-date {{ color: var(--p); font-weight: bold; font-size: 13px; }}
        
        @keyframes fadeIn {{ from {{ opacity: 0; transform: scale(0.95); }} to {{ opacity: 1; transform: scale(1); }} }}
    </style>
</head>
<body>
    <div class="header">
        <h1>X-Ray Elite Hub 🚀</h1>
        <a href="{channel_url}" class="join-btn" target="_blank">انضم للقناة الرسمية 📢</a>
        <div class="status-bar">آخر تحديث: {now_date} | {now_time} | السيرفرات المتوفرة: {len(clean_links)}</div>
    </div>

    <div class="info-box">
        <h4 style="margin:0 0 10px 0; color:var(--p);">📖 دليل الاستخدام السريع:</h4>
        <p style="font-size: 13px; margin: 5px 0;">• <b>للنسخ:</b> اضغط "نسخ" ثم Import في تطبيق VPN.</p>
        <p style="font-size: 13px; margin: 5px 0;">• <b>للباركود:</b> اضغط زر الباركود الملون للمسح بالكاميرا.</p>
    </div>

    <div style="width:100%; max-width:480px;">
        {cards if clean_links else '<div class="card" style="text-align:center">جاري البحث عن سيرفرات جديدة...</div>'}
    </div>

    <footer>
        <div class="footer-date">🕒 تم التحديث في: {now_date} - {now_time}</div>
        <div style="color: #4b5563; font-size: 11px; margin-top: 10px;">جميع الحقوق محفوظة | مستودع XR المطور</div>
    </footer>

    <script>
        function copy(t) {{ navigator.clipboard.writeText(t).then(() => alert("تم النسخ بنجاح ✅")); }}
        function qr(id, l) {{
            var el = document.getElementById(id);
            if(!el.innerHTML) new QRCode(el, {{text:l, width:180, height:180}});
            el.style.display = (el.style.display == 'block') ? 'none' : 'block';
        }}
    </script>
</body>
</html>'''
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run()
