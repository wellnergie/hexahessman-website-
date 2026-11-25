#!/usr/bin/env python3
"""
WELLNERGIE — static site generator.
Run:  python3 build.py
Outputs HTML into ./site (assets, css and js already live there).
Product content is taken from wellnergie.com product pages; edit PRODUCTS below to change it.
"""
import json, os, html, pathlib

ROOT = pathlib.Path(__file__).parent
SITE = ROOT / "site"
IMAGES = json.load(open(ROOT / "site_images.json"))
WIX = "https://www.wellnergie.com"
import time
ASSET_VER = str(int(time.time()))

# ----------------------------------------------------------------------------
# Product catalogue (content preserved from wellnergie.com)
# ----------------------------------------------------------------------------
WAVE_INTRO = ("Through the combination of technology and Wellnergie wave, the team at Wellnergie transformed and "
              "leveraged the energy of earth nature to bring together a family of products that proved effective in "
              "improving your physical vitality. The Wellnergie wave penetration range is 15cm in diameter transferred "
              "to human body and allows the biological cells to achieve the highest vibration level.")
BAND_INFO = ("Wellnergie Energy Weband {name} is developed by using {material}, which includes natural minerals such as "
             "tourmaline, germanium, Negative ion & far-infrared powder and high-quality titanium metal. Bio-wave will be "
             "released when in contact with it. When our energy wristband is in contact with the human body, it releases "
             "Bio-wave which is most beneficial to humans.")
BAND_FUNCS = ["Promotes cellular vitality", "Strengthen blood circulation and Eliminate fatigue",
              "Elevate and improve body immunity", "Speed up body self-healing process",
              "Block harmful electromagnetic waves and radiation from electrical appliances / mobile phone",
              "Protect against free radical"]
BAND_LEAD = ("Beyond just gold and silver, Wellnergie WeBand {name} is wellness & health. Infused with energy through "
             "negative ions, the WeBand strengthens blood circulation, eliminating fatigue & improving immunity. The WeBand "
             "can increase strength by up to 35%, and improve endurance by up to 60%, and blocks harmful electromagnetic "
             "waves from phones & appliances.")

DOT = {"Black": "#1f1f1f", "Blue": "#1f3f9a", "Purple": "#7a1f6e", "Brown": "#6b4a2b", "Beige": "#d9c9ae", "White": "#f4f4f4",
       "Orange": "#e8641c", "Red": "#c8202a", "Green": "#1f6b3a", "Silver": "#c9c9c9", "Rose Gold": "#d8a48f",
       "Silver Gold": "#d9c99a"}

PRODUCTS = [
    dict(slug="wetube", cat="wetube", cat_label="WeTube",
         name="WeTube Signature", full="WELLNERGIE Signature Wetube With Negative Ion Energy",
         price=209, badge=None, hero=2, order=[2, 0, 1, 3, 4, 5, 6],
         short="Our flagship product. WeTube channels the power of anions to cleanse water, turning it from harmful acidic water to clean, detoxified alkaline water.",
         description=[
             "Our flagship product, WeTube channels the power of anions to cleanse water, turning it from harmful acidic water to clean, detoxified alkaline water. It is also infused with Wellnergie wave, to reduce discomfort, improve sleep quality, block electromagnetic waves, and more.",
             "It involves both science and technology in the research and development of improving water degradation. The R & D team gathered the skills and knowledge of our specialists of this scientific field and taken over ten years of constant testing to develop \"WeTube\".",
             "High grade materials are combined with Nano technology, through the application of cross scientific technology from various sectors like physics, chemistry and medical science, to create a safe, durable, elegant product."],
         functions=["Block harmful electromagnetic waves and radiation", "Strengthen blood circulation, and promotes cellular vitality",
                    "Protect against free radicals", "Re-arrange smaller water molecules to increase the absorption rate of oxygen and nutrients into the cells",
                    "Improve metabolic and detoxification process", "Remove residual chlorine and the smell from water",
                    "Delay aging and enhancing physical vitality", "Enhance PH balance to create slight alkaline water as acidic body is the source of all diseases"],
         specs=[("Materials", "Germanium, Far-Infrared, Tourmaline, Negative Ions"), ("Technology", "Nano Energy Technology / Wellnergie Wave"),
                ("Penetration", "Up to 15cm"), ("Usage", "In water (purifier) or placed near / under the body")],
         options=[], quantity=True),

    dict(slug="weband-luxury", cat="weband", cat_label="WeBand",
         name="WeBand Luxury", full="WELLNERGIE Weband Luxury (Negative Ion Energy)",
         price=199, badge=None, hero=3, order=[3, 2, 5, 4, 0, 1],
         short="Matte plate design on biological silica gel. Energy Level 4000+, lasting up to 4 years.",
         description=[BAND_LEAD.format(name="Luxury"), WAVE_INTRO, BAND_INFO.format(name="Luxury", material="biological silica gel")],
         functions=["Energy Level 4000+, last for 4years"] + BAND_FUNCS,
         specs=[("Plate Design", "Matte"), ("Material", "Biological silica gel"), ("Colour", "Black, Blue, Purple, Brown")],
         options=[("Color", [("Black", 2), ("Blue", 3), ("Purple", 5), ("Brown", 4)])]),

    dict(slug="weband-magnet", cat="weband", cat_label="WeBand",
         name="WeBand Magnet", full="WELLNERGIE Weband Magnet With Negative Ion Energy",
         price=349, badge="New Arrival", hero=9, order=[9, 10, 11, 3, 2, 4, 1, 0, 5, 6, 7, 8],
         short="Magnetic clasp with a matte plate. Energy Level 5000+, lasting up to 5 years.",
         description=[BAND_LEAD.format(name="Magnet"), WAVE_INTRO, BAND_INFO.format(name="Magnet", material="biological silica gel")],
         functions=["Energy Level 5000+, last for 5years"] + BAND_FUNCS,
         specs=[("Plate Design", "Matte"), ("Material", "Biological silica gel"), ("Colour", "Black, Blue, Beige")],
         options=[("Color", [("Black", 9), ("Blue", 10), ("Beige", 11)])]),

    dict(slug="weband-stylish-ii", cat="weband", cat_label="WeBand",
         name="WeBand Stylish II", full="WELLNERGIE Weband Stylish II (Negative Ion Energy)",
         price=159, badge=None, hero=2, order=[2, 3, 4, 5, 0, 1, 6, 7],
         short="Second generation of WeBand S2, infused with stronger Wellnergie Wave and a higher density of negative ions.",
         description=[
             "Second generation of Weband S2, infused with stronger Wellnergie Wave and higher density of negative ions. The enhancement module which located at whole wristband contains Multiple Mineral Powder and Wellnergie Wave helps to boost the energy that emits out to the body for better absorption. Light and comfortable to wear, provide maximum benefit and protection to your body.",
             WAVE_INTRO, BAND_INFO.format(name="S2", material="biological silica gel")],
         functions=["Energy Level 3000+, last for 3years"] + BAND_FUNCS,
         specs=[("Plate Design", "Matte"), ("Material", "Biological silica gel"), ("Colour", "Black, White, Orange, Red")],
         options=[("Color", [("Black", 2), ("White", 3), ("Orange", 5), ("Red", 4)])]),

    dict(slug="weband-classic", cat="weband", cat_label="WeBand",
         name="WeBand Classic", full="WELLNERGIE WeBand Classic with Negative Ion Energy",
         price=99, badge="New Arrival", hero=0, order=[0, 1, 2, 3, 4],
         short="Developed using biological silica gel infused with energy through negative ions. Available in two sizes.",
         description=[
             "Wellnergie WeBand Classic is developed using biological silica gel infused with energy through negative ions. It promotes healthy blood circulation, eliminating fatigue & improving immunity.",
             "It includes natural minerals such as tourmaline, germanium, Negative ion & far-infrared powder and high-quality titanium metal. Bio-wave will be released when in contact with it. When our energy is in contact with the human body, it releases Bio-wave which is most beneficial to humans.",
             "It can increase strength by up to 35%, and improve endurance by up to 60%, and blocks harmful electromagnetic waves from phones & appliances."],
         functions=["Promotes cellular vitality", "Strengthen blood circulation and Eliminate fatigue", "Elevate and improve body immunity",
                    "Speed up body self-healing process", "Block harmful electromagnetic waves and radiation from electrical appliances / mobile phone",
                    "Protect against free radical"],
         specs=[("Material", "Biological silica gel"), ("Colour", "Black, Red"), ("Size", "195mm, 175mm")],
         options=[("Color", [("Black", None), ("Red", None)]), ("Size", [("195mm", None), ("175mm", None)])]),

    dict(slug="weband-executive", cat="weband", cat_label="WeBand",
         name="WeBand Executive", full="【1 EXE】WELLNERGIE WeBand Executive With Negative Ion Energy (Model E1-E11)",
         price=399, badge=None, hero=2, order=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 0],
         short="Stainless steel alloy bracelet. Energy Level 6000+, lasting up to 8 years. Package includes 1 x WeBand Executive.",
         description=[BAND_LEAD.format(name="Executive"), WAVE_INTRO, BAND_INFO.format(name="Executive", material="stainless steel alloy").replace("energy wristband", "energy")],
         functions=["Energy Level 6000+, last for 8 years", "Promotes cellular vitality", "Strengthens blood circulation", "Supports Immune Function",
                    "Reduce body discomfort", "Improve sleep quality", "Speed up body self-healing process",
                    "Block harmful electromagnetic waves and radiation from electrical appliances / mobile phone", "Protect against free radical"],
         specs=[("Design", "E1, E3, E4, E5 (Model E1-E11)"), ("Material", "Stainless Steel Alloy"), ("Package", "1 x Weband Executive")],
         options=[("Design", [("T1 Silver Gold", 2), ("T3 Silver", 3), ("T4 Rose Gold", 4), ("T5 Silver", 5), ("E6 Silver", 6), ("E7 Silver", 7),
                              ("E8 Black", 8), ("E9 Silver", 9), ("E10 Black", 10), ("T11 Silver", 11)])]),

    dict(slug="weband-executive-duo", cat="weband", cat_label="WeBand",
         name="WeBand Executive — Pair", full="【2 EXE】WELLNERGIE WeBand Executive With Negative Ion Energy (Model E1-E11)",
         price=798, badge="Bundle", hero=6, order=[6, 7, 8, 9, 10, 11, 12, 13, 14, 4, 3, 5, 0, 1, 2],
         short="Two WeBand Executive bracelets, with 2 x WeBand Classic included in the package.",
         description=[BAND_LEAD.format(name="Executive").replace("WeBand Executive is", "WeBand is"), WAVE_INTRO, BAND_INFO.format(name="Executive", material="stainless steel alloy").replace("energy wristband", "energy")],
         functions=["Energy Level 6000+, last for 8 years", "Promotes cellular vitality", "Strengthens blood circulation", "Supports Immune Function",
                    "Reduce body discomfort", "Improve sleep quality", "Speed up body self-healing process",
                    "Block harmful electromagnetic waves and radiation from electrical appliances / mobile phone", "Protect against free radical"],
         specs=[("Design", "E1, E3, E4, E5 (Model E1-E11)"), ("Material", "Stainless Steel Alloy"), ("Package", "2 x Weband Executive, 2 x Weband Classic")],
         options=[("Design", [("T1 Silver Gold", 6), ("T3 Silver", 7), ("T4 Rose Gold", 8), ("T5 Silver", 9), ("T11 Silver", 10), ("E6 Silver", 11),
                              ("E7 Silver", 12), ("E8 Black", 13), ("E10 Black", 14)])]),

    dict(slug="wespec", cat="wespec", cat_label="WeSpec",
         name="WeSpec Glasses", full="WELLNERGIE Glasses with Negative Ion Energy & Blue Light Protection",
         price=209, badge=None, hero=8, order=[8, 9, 10, 7, 0, 1, 2, 3, 4, 5, 6],
         short="Wellnergie Wave infused into the TR90 frame, with PC lenses that absorb blue light to reduce discomfort to the eyes.",
         description=[
             WAVE_INTRO,
             "Wellnergie WeSpec has strong Wellnergie Waves infused into the framing materials of the spectacles. It helps to strengthens blood circulation around the eyes to remove overall tiredness, reduce dark eye circles and general fatigue. It strengthens blood circulation, eliminating fatigue & improving immunity.",
             "PC lens that utilizes international technology to prove the absorption of blue light to reduce discomfort to eyes. TR90 is a high-performing material that is extremely light-weight, tough and resistant to high temperatures.",
             "It includes natural minerals such as tourmaline, germanium, Negative ion & far-infrared powder and high-quality titanium metal. It can increase strength by up to 35%, and improve endurance by up to 60%, and blocks harmful electromagnetic waves from phones & appliances. Bio-wave will be released when in contact with it.",
             "Wear the product for your eyes. Wait for at least 30 minutes for the effects to work. The longer you wear the product, the better blood circulation and effects the WeSpec will provide."],
         functions=["Strengthens blood circulation around the eyes", "Removes overall tiredness and reduces dark eye circles", "Blue light absorption to reduce discomfort to eyes",
                    "Eliminates fatigue & improves immunity", "Blocks harmful electromagnetic waves from phones & appliances"],
         specs=[("Colour", "Green, Red, Orange"), ("Material", "PC Lens, TR90"), ("Type", "Standard, Small")],
         options=[("Colour", [("Green", 8), ("Orange", 9), ("Red", 10)]), ("Type", [("Standard", None), ("Small", None)])]),

    dict(slug="hexabee-socks", cat="wellness", cat_label="Wellness",
         name="HexaBee Socks", full="HexaBee - Negative Ions & Far Infrared Socks",
         price=13, badge=None, hero=4, order=[4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3],
         short="Made with nanoZ Technology long fibre composite: lighter, thinner and stronger than conventional materials.",
         description=[
             "NanoZ Technology: Pioneering technology from Japan. Made with nanoZ Technology long fiber composite, known for being lighter, thinner, and stronger than conventional materials.",
             "Specially designed for high-stress areas like the heads, heels, and soles of socks, minimizing piling. Long-term wear supports health benefits, including promotes healthy blood circulation.",
             "Effectively prevents the spread and regrowth of bacteria. Soft, moisture-wicking design helps reduce foot odor and ankle pain. Sock sole constructed from nanoZ Technology and magnetic fibers for enhanced breathability."],
         functions=["Low-temp Far-Infrared Radiation", "Antibacterial & Skin-friendly", "Moisture Absorption & Breathability",
                    "Promotes healthy blood circulation", "Reduces foot odor and ankle pain"],
         specs=[("Technology", "nanoZ Technology (Japan)"), ("Material", "Long fiber composite with magnetic fibers"), ("Colour", "White, Black"), ("Size", "Select at checkout")],
         options=[("Colour", [("White", 6), ("Black", 5)])]),

    dict(slug="graphene-patch", cat="wellness", cat_label="Wellness",
         name="Graphene Heat Relief Patch", full="Graphene Essential Oil Heat Relief Patch",
         price=26, badge="Hot Item", hero=0, order=[0, 2, 3, 1, 4, 5, 6, 7],
         short="Graphene essential oil pain relief patch. 10 pieces per pack, each patch lasts up to 12 hours.",
         description=[
             "Clean the affected area. Take out a patch and peel off the protective film. Apply the adhesive side to the affected area. Use the required number of patches for the location. Each patch can be used for 12 hours. It is recommended to have a 12-hour interval before the next use to reduce skin irritation. If you have sensitive skin, consider reducing the usage time.",
             "Precautions: For external use only; do not ingest. Single use only; cannot be reused. Do not apply to broken skin or unhealed wounds. If slight itching or redness occurs, apply an external anti-allergic ointment and only continue use once symptoms disappear. Pregnant women and infants should not use this product. Children should use it under a physician's guidance."],
         functions=["Joint & Muscle Pain", "Lower Back / Leg & Neck Vertebrae Pain", "Adhesive Capsulitis & Arthritis", "Lumbar Nerve Compression",
                    "Tendonitis & Tennis Elbow", "Various of Heavy Impact Injuries", "Lumbar Disc Herniation", "Anti-inflammatory Analgesic"],
         specs=[("Model Specification", "110mm x 150mm"), ("Package Quantity", "10 pieces per pack"), ("Valid Period", "Three years")],
         options=[], quantity=True),

    dict(slug="webottle", cat="wetube", cat_label="WeTube",
         name="WeBottle 800ml", full="WELLNERGIE WeBottle with Protector 800ml",
         price=35, badge=None, hero=0, order=[0, 1, 2, 3],
         short="Tritan BPA-free water bottle with infuser, designed for use with WeTube. WeTube not included.",
         description=["Tristan BPA Free Plastic Water Bottle with Infuser. Large capacity, convenient to carry. Suitable for the usage of WeTube. *WeTube not included*"],
         functions=["Large capacity, convenient to carry", "Food grade PP material, safe and non-toxic, BPA Free", "Water leakage prevention design", "Suitable for the usage of WeTube"],
         specs=[("Volume", "800ml"), ("Colour", "Blue"), ("Includes", "Protector (WeTube not included)")],
         options=[], quantity=True),

    dict(slug="weprotector", cat="wetube", cat_label="WeTube",
         name="WeProtector", full="WELLNERGIE WeProtector for WeTube (*WeTube Not Included*)",
         price=15, badge=None, hero=0, order=[0, 1, 2],
         short="Extra protection for your WeTube. Can be inserted in the WeBottle for water filtration. WeTube not included.",
         description=["Provides extra protection for WELLNERGIE WETUBE. Can be inserted in WELLNERGIE WEBOTTLE for water filtration purpose."],
         functions=["Provides extra protection for WELLNERGIE WETUBE", "Can be inserted in WELLNERGIE WEBOTTLE for water filtration purpose"],
         specs=[("Material", "Food grade PP material"), ("Safety", "Safe and non-toxic, BPA Free")],
         options=[], quantity=True),
]
WIX_SLUG = {
    "wetube": "1-wetube-wellnergie-signature-wetube-water-purifier-with-negative-ion-energy",
    "weprotector": "weprotector",
    "weband-classic": "1-classic-wellnergie-weband-enhanced-fitness-bracelet-with-negative-ion-energy",
    "wespec": "wellnergie-wespec-glasses-with-negative-ion-energy-blue-light-protection",
    "hexabee-socks": "hexabee-negative-ions-far-infrared-socks",
    "weband-executive-duo": "2-for-520-weband-executive-t1-t6",
    "weband-executive": "limited-deals-weband-executive-t1-t6",
    "weband-magnet": "1-magnet-wellnergie-weband-magnet-with-negative-ion-energy",
    "webottle": "limited-deals-webottles-orange",
    "weband-luxury": "1-luxury-wellnergie-weband-luxury-matte-with-negative-ion-energy",
    "weband-stylish-ii": "s2-x-1-wellnergie-weband-stylish-ii-with-negative-ion-energy",
    "graphene-patch": "graphene-essential-oil-heat-relief-patch",
}
BY_SLUG = {p["slug"]: p for p in PRODUCTS}

SOCIALS = [
    ("Facebook", "https://www.facebook.com/Wellnergie/",
     '<svg viewBox="0 0 24 24"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.6 1.6-1.6h1.7V4.4c-.3 0-1.3-.1-2.5-.1-2.5 0-4.1 1.5-4.1 4.2v2.3H7.4V14h2.8v8h3.3z"/></svg>'),
    ("Instagram", "https://www.instagram.com/wellnergie/",
     '<svg viewBox="0 0 24 24"><path d="M12 7.3a4.7 4.7 0 1 0 0 9.4 4.7 4.7 0 0 0 0-9.4zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm5.9-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM12 3.9c2.6 0 2.9 0 4 .1 1 0 1.5.2 1.9.3.5.2.8.4 1.1.7.4.4.6.7.7 1.2.1.4.3.9.3 1.9.1 1 .1 1.4.1 4s0 2.9-.1 4c0 1-.2 1.5-.3 1.9-.2.5-.4.8-.7 1.1-.4.4-.7.6-1.2.7-.4.1-.9.3-1.9.3-1 .1-1.4.1-4 .1s-2.9 0-4-.1c-1 0-1.5-.2-1.9-.3-.5-.2-.8-.4-1.1-.7-.4-.4-.6-.7-.7-1.2-.1-.4-.3-.9-.3-1.9-.1-1-.1-1.4-.1-4s0-2.9.1-4c0-1 .2-1.5.3-1.9.2-.5.4-.8.7-1.1.4-.4.7-.6 1.2-.7.4-.1.9-.3 1.9-.3 1-.1 1.4-.1 4-.1M12 2.2c-2.7 0-3 0-4 .1-1.1 0-1.8.2-2.4.5-.7.2-1.2.6-1.8 1.1-.5.6-.9 1.1-1.1 1.8-.3.6-.5 1.3-.5 2.4-.1 1-.1 1.3-.1 4s0 3 .1 4c0 1.1.2 1.8.5 2.4.2.7.6 1.2 1.1 1.8.6.5 1.1.9 1.8 1.1.6.3 1.3.5 2.4.5 1 .1 1.3.1 4 .1s3 0 4-.1c1.1 0 1.8-.2 2.4-.5.7-.2 1.2-.6 1.8-1.1.5-.6.9-1.1 1.1-1.8.3-.6.5-1.3.5-2.4.1-1 .1-1.3.1-4s0-3-.1-4c0-1.1-.2-1.8-.5-2.4-.2-.7-.6-1.2-1.1-1.8-.6-.5-1.1-.9-1.8-1.1-.6-.3-1.3-.5-2.4-.5-1-.1-1.3-.1-4-.1z"/></svg>'),
    ("YouTube", "https://www.youtube.com/channel/UCH2cXZnySNUCifJ7l15ldNw",
     '<svg viewBox="0 0 24 24"><path d="M23 7.2c-.3-1-1-1.8-2-2C19.2 4.7 12 4.7 12 4.7s-7.2 0-9 .5c-1 .3-1.8 1-2 2C.5 9 .5 12 .5 12s0 3 .5 4.8c.3 1 1 1.8 2 2 1.8.5 9 .5 9 .5s7.2 0 9-.5c1-.3 1.8-1 2-2 .5-1.8.5-4.8.5-4.8s0-3-.5-4.8zM9.7 15.1V8.9l6 3.1-6 3.1z"/></svg>'),
    ("TikTok", "https://www.tiktok.com/@wellnergie_sg",
     '<svg viewBox="0 0 24 24"><path d="M16.6 5.8c-.9-1-1.4-2.3-1.4-3.6h-3.2v13.4a2.8 2.8 0 0 1-2.8 2.7 2.8 2.8 0 0 1-2.8-2.8c0-1.9 1.8-3.3 3.7-2.7V9.5c-3.8-.5-7.1 2.4-7.1 6.1 0 3.6 3 6.2 6.2 6.2 3.4 0 6.2-2.8 6.2-6.2V8.8c1.4 1 3 1.5 4.7 1.5V7.1s-2-.1-3.5-1.3z"/></svg>'),
    ("Shopee", "https://shopee.sg/wellnergie", '<img src="{rel}assets/icons/shopee.png" alt="">'),
    ("Lazada", "https://www.lazada.sg/shop/wellnergie-sg", '<img src="{rel}assets/icons/lazada.png" alt="">'),
]
PAYMENTS = [("PayNow", "paynow"), ("DBS PayLah!", "paylah"), ("Visa", "visa"), ("Mastercard", "mastercard")]


TESTIMONIALS = [
    ("ZHxdD1mOGmQ", "She Couldn't Walk Properly for 4 Years... Until This Happened."),
    ("MA1rnawQoiY", "Father with Diabetic Neuropathy & Parkinson's Disease · 父亲糖尿神经病变&帕金森病"),
    ("jwXRjwnlvzE", "90 Years Old. Dependent on a Walking Cane... Until This Happened. · 90岁，长期依靠拐杖……直到这一刻！"),
    ("DiZSkhG7GmI", "Aden · 脊椎里有6颗螺丝，曾经连翻身或站起来都很难"),
    ("tMFSLfi0GJY", "Serene Lee, 51 · From Cerebellar Disorder to Better Balance & Less Dizziness"),
    ("4zoc9toKu1E", "Jusni, 47 · Stroke 4 years, hand can't raise up"),
    ("gwrqLy4lRxI", "Immediate Relief for Arthritis & Stiff Knees · 坐轮椅关节炎和膝盖僵硬女士当场改善"),
    ("nQ092DRO3Bs", "A Healthier Mom, A Happier Home"),
]
PLAY = '<span class="play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span>'

def t_card(vid, title, rel="", cls="t-card"):
    return (f'<a class="{cls}" href="https://www.youtube.com/watch?v={vid}" data-video="{vid}" target="_blank" rel="noopener">'
            f'<span class="t-thumb"><img src="{rel}assets/testimonials/{vid}.jpg" alt="" loading="lazy">{PLAY}</span>'
            f'<span class="t-cap">{esc(title)}</span></a>')

def testimonial_marquee(rel=""):
    cards = "".join(t_card(v, t, rel) for v, t in TESTIMONIALS)
    return f'<div class="marquee" data-marquee><div class="marquee-track">{cards}</div></div>'

LIGHTBOX = '''<div class="lightbox" hidden><button class="lightbox-close" aria-label="Close video">Close ×</button><div class="lightbox-frame"></div></div>'''


GOOGLE_RATING = "5.0"
GOOGLE_COUNT = 90
GOOGLE_REVIEW_URL = "https://g.page/r/CU4uqJhePw_nEAI/review"
GOOGLE_MAPS_URL = "https://maps.google.com/?cid=16649596022932647502"
# (name, stars, when, text) — copied from the Google Business Profile. Add more entries here.
GOOGLE_REVIEWS = [
    ("sim Sim", 5, "5 months ago", "Very good Singapore product. This is my 2nd purchase as it had help me relieve my pain. The boss Thomas Tan is also very friendly and professional and let me tried the products before buying. I also bought the filter (wetube) for my water consumption. It taste better and smoother. Thanks so much"),
    ("Lourde Ammal", 5, "5 months ago", "Yes, today I come to free try the wellnergie products at yishun office, it really work to reduce my knee and body pain. Thanks Thomas service me better. Will introduce to my friends who have some problems as me."),
    ("蔡蔡莉萍", 5, "2 months ago", "Good energy product I have meet, 15min can see the effect, good explain easy to understand, recommend recommend, hope can make new product on the necklace, new spec and back support product"),
]
STAR = '<svg viewBox="0 0 24 24"><path d="M12 2.5l2.9 6.2 6.8.8-5 4.6 1.3 6.7L12 17.5l-6 3.3 1.3-6.7-5-4.6 6.8-.8z"/></svg>'
GLOGO = '<svg viewBox="0 0 24 24" class="g-logo"><path fill="#4285F4" d="M21.6 12.2c0-.7-.1-1.4-.2-2H12v3.9h5.4c-.2 1.2-.9 2.3-2 3v2.5h3.2c1.9-1.7 3-4.3 3-7.4z"/><path fill="#34A853" d="M12 22c2.7 0 5-.9 6.6-2.4l-3.2-2.5c-.9.6-2 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3.1v2.6C4.8 19.8 8.1 22 12 22z"/><path fill="#FBBC05" d="M6.4 13.9c-.2-.6-.3-1.2-.3-1.9s.1-1.3.3-1.9V7.5H3.1C2.4 8.9 2 10.4 2 12s.4 3.1 1.1 4.5l3.3-2.6z"/><path fill="#EA4335" d="M12 5.9c1.5 0 2.8.5 3.8 1.5l2.9-2.9C17 2.9 14.7 2 12 2 8.1 2 4.8 4.2 3.1 7.5l3.3 2.6c.8-2.4 3-4.2 5.6-4.2z"/></svg>'

def stars(n, cls="stars"):
    return f'<span class="{cls}" aria-label="{n} out of 5 stars">' + "".join(f'<i class="{"on" if k < n else ""}">{STAR}</i>' for k in range(5)) + "</span>"

def google_reviews(rel=""):
    cards = "".join(
        f'<div class="g-card"><div class="g-head"><span class="g-avatar">{esc(n[0].upper())}</span><div><div class="g-name">{esc(n)}</div><div class="g-when">{esc(w)}</div></div>{GLOGO}</div>{stars(s)}<p class="g-text">{esc(t)}</p></div>'
        for n, s, w, t in GOOGLE_REVIEWS)
    return f"""<section class="section google-reviews" style="padding-top:0">
  <div class="wrap section-head reveal">
    <div><span class="eyebrow">Google Reviews</span><h2 class="h2">Rated {GOOGLE_RATING} on Google.</h2>
      <div class="g-summary">{GLOGO}<strong>{GOOGLE_RATING}</strong>{stars(5)}<span class="muted">Based on {GOOGLE_COUNT} Google reviews</span></div></div>
    <div class="g-actions"><a class="btn" href="{GOOGLE_MAPS_URL}" target="_blank" rel="noopener">See all reviews</a></div>
  </div>
  <div class="marquee" data-marquee><div class="marquee-track">{cards}</div></div>
</section>"""

def social_icons(cls="", rel=""):
    items = ""
    for n, u, ic in SOCIALS:
        ic = ic.replace("{rel}", rel)
        extra = " brand-img" if ic.startswith("<img") else ""
        items += f'<li><a class="soc{extra}" href="{u}" target="_blank" rel="noopener" aria-label="{n}" title="{n}">{ic}</a></li>'
    return f'<ul class="social-icons {cls}">{items}</ul>'

def payment_icons(rel=""):
    return '<span class="payments">' + "".join(f'<img src="{rel}assets/icons/{f}.png" alt="{n}" title="{n}">' for n, f in PAYMENTS) + "</span>"


def esc(s): return html.escape(s, quote=True)
def act(c): return ' class="is-active"' if c else ""
def img(p, i, rel=""): return f"{rel}{IMAGES[p['slug']][i]}"
def price(p): return f"SGD {p['price']:.2f}"

# ----------------------------------------------------------------------------
# Shared chrome
# ----------------------------------------------------------------------------
ICON_SEARCH = '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>'
ICON_BAG = '<svg viewBox="0 0 24 24"><path d="M6 8h12l1 13H5L6 8z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>'
ICON_MENU = '<svg viewBox="0 0 24 24"><path d="M3 7h18M3 12h18M3 17h18"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

NAV = [("Home", "index.html"), ("Technology", "technology.html"), ("Shop", "shop.html"), ("About Us", "about.html")]

def head(title, rel, desc="Wellnergie — Greatest Gift of Health. Founded in Singapore in 2019, a wellness technology company built on Wellnergie Wave Technology: WeTube, WeBand, WeSpec and more."):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | Wellnergie</title>
<meta name="description" content="{esc(desc)}">
<link rel="icon" href="{rel}assets/logo/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}css/style.css?v={ASSET_VER}">
</head>"""

def header(rel, active, light=False):
    links = "".join(f'<a href="{rel}{h}"{act(n == active)}>{n}</a>' for n, h in NAV)
    drawer = "".join(f'<a href="{rel}{h}">{n}</a>' for n, h in NAV + [("Testimonials", "testimonials.html"), ("FAQ", "faq.html"), ("Contact Us", "contact.html")])
    return f"""
<header class="site-header{' is-light' if light else ''}">
  <div class="wrap">
    <a class="brand" href="{rel}index.html" aria-label="Wellnergie home">
      <img class="logo-white" src="{rel}assets/logo/mark-white.png" alt="">
      <img class="logo-dark" src="{rel}assets/logo/mark-dark.png" alt="">
      <span class="brand-word">Wellnergie</span>
    </a>
    <nav class="nav" aria-label="Primary">{links}</nav>
    <div class="header-tools">
      <a href="{rel}shop.html" aria-label="Search products">{ICON_SEARCH}</a>
      <a href="{WIX}/cart-page" aria-label="Cart" target="_blank" rel="noopener">{ICON_BAG}</a>
      <button class="menu-toggle" aria-label="Open menu">{ICON_MENU}</button>
    </div>
  </div>
</header>
<div class="nav-drawer">
  <button class="drawer-close">Close</button>
  {drawer}
</div>"""

def footer(rel):
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <a class="brand" href="{rel}index.html"><img src="{rel}assets/logo/logo-white.png" alt="Wellnergie"></a>
        <p class="tagline">Greatest Gift of Health.</p>
        <p style="margin-top:18px;font-size:14px">A'POSH BIZHUB, 1 Yishun Industrial Street 1, #05-29,<br>Singapore 768160</p>
      </div>
      <div class="col">
        <h4>Explore</h4>
        <ul>
          <li><a href="{rel}shop.html">Shop / Products</a></li>
          <li><a href="{rel}technology.html">Technology</a></li>
          <li><a href="{rel}testimonials.html">Testimonials</a></li>
          <li><a href="{rel}about.html">About Us</a></li>
          <li><a href="{rel}contact.html">Contact Us</a></li>
          <li><a href="{rel}faq.html">FAQ</a></li>
        </ul>
      </div>
      <div class="col">
        <h4>Follow Us</h4>
        {social_icons("on-dark", rel)}
        <ul style="margin-top:18px">
          <li><a href="https://shopee.sg/wellnergie" target="_blank" rel="noopener">Shop on Shopee</a></li>
          <li><a href="https://www.lazada.sg/shop/wellnergie-sg" target="_blank" rel="noopener">Shop on Lazada</a></li>
        </ul>
      </div>
      <div class="col">
        <h4>New to Wellnergie?</h4>
        <p style="font-size:14px">Enter your email below to receive the latest updates on our new collections and product launches!</p>
        <form class="newsletter">
          <input type="email" placeholder="Email address" required aria-label="Email address">
          <button class="btn" type="submit">Join</button>
        </form>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© Wellnergie. Wellnergie — Greatest Gift of Health.</span>
      <span class="pay-line">Payment: HitPay (PayNow &amp; Credit Card) {payment_icons(rel)}</span>
      <span><a href="{WIX}/terms-and-conditions">Terms and Conditions</a> &nbsp;|&nbsp; <a href="{WIX}/general-terms-of-use">General Terms of Use</a></span>
    </div>
  </div>
</footer>
<script src="{rel}js/main.js?v={ASSET_VER}"></script>
</body></html>"""

def card_title(p):
    import re as _re
    return _re.sub(r"^【[^】]*】\s*", "", p["full"]).replace("  ", " ")

def product_card(p, rel=""):
    imgs = IMAGES[p["slug"]]
    seq = [imgs[i] for i in p["order"]]
    badge = f'<span class="badge{" gold" if p["badge"] in ("Hot Item", "Bundle") else ""}">{p["badge"]}</span>' if p["badge"] else ""
    if p.get("compare"):
        badge = '<span class="badge sale">Sale</span>' + badge
    dots = "".join(("<i class=\"on\"></i>" if k == 0 else "<i></i>") for k in range(min(len(seq), 8)))
    if p.get("rating"):
        rating = f'<div class="rating">{stars(p["rating"])}<span>{p["reviews"]} review{"s" if p["reviews"] != 1 else ""}</span></div>'
    else:
        rating = f'<div class="rating">{stars(5)}<span>{GOOGLE_RATING} (Google)</span></div>'
    cmp_html = f'<s>SGD {p["compare"]:.2f}</s>' if p.get("compare") else ""
    return f"""<a class="product-card reveal" href="{rel}product/{p['slug']}.html" data-cat="{p['cat']}" data-images="{'|'.join(rel + s for s in seq)}">
  <div class="thumb">{badge}<img src="{rel}{seq[0]}" alt="{esc(p['name'])}" loading="lazy"><span class="dots">{dots}</span></div>
  <div class="info">
    <div class="vendor">Wellnergie</div>
    <div class="name">{esc(card_title(p))}</div>
    {rating}
    <div class="price">{cmp_html}<strong>{price(p)}</strong></div>
  </div>
</a>"""

# ----------------------------------------------------------------------------
# Pages
# ----------------------------------------------------------------------------
def page_home():
    slides = [
        dict(img="assets/hero/hero-weband.jpg", pos="72% 40%", eyebrow="WeBand Collection",
             h1="Wellness<br>Refined", accent="Made for movement",
             lede="",
             cta=("Discover our technology", "technology.html")),
        dict(img="assets/hero/hero-wetube.jpg", pos="70% 40%", eyebrow="WeTube Signature",
             h1="Greatest Gift<br>of Health", accent="Wellness + Energy",
             lede="",
             cta=("Explore WeTube", "product/wetube.html")),
        dict(img="assets/hero/hero-wespec.jpg", pos="72% 40%", eyebrow="WeSpec Glasses",
             h1="Wellness for<br>Every Generation", accent="Greatest Gift of Health",
             lede="",
             cta=("Explore WeSpec", "product/wespec.html")),
    ]
    slides_html = ""
    for k, s in enumerate(slides):
        slides_html += f"""
  <div class="slide{' is-active' if k == 0 else ''}" style="--pos:{s['pos']}">
    <div class="slide-bg"><img src="{s['img']}" alt="" {'fetchpriority="high"' if k == 0 else 'loading="lazy"'}></div>
    <div class="slide-content"><div class="wrap"><div class="inner">
      <span class="eyebrow">{s['eyebrow']}</span>
      <h1 class="display">{s['h1']}</h1>
      <span class="accent">{s['accent']}</span>
      <a class="btn btn-light btn-lg" href="{s['cta'][1]}">{s['cta'][0]}</a>
    </div></div></div>
  </div>"""
    dots = "".join(f'<button aria-label="Go to slide {k+1}"{act(k == 0)}></button>' for k in range(len(slides)))

    featured = [BY_SLUG[s] for s in ("wetube", "weband-luxury", "wespec", "weband-executive", "weband-magnet", "weband-stylish-ii", "weband-classic", "hexabee-socks")]
    cards = "\n".join(product_card(p) for p in featured)

    return head("Home", "") + '<body class="has-hero">' + header("", "Home") + f"""
<section class="hero" aria-roledescription="carousel">
  {slides_html}
  <div class="hero-nav wrap">
    <div class="hero-dots">{dots}</div>
    <div class="hero-arrows">
      <button class="hero-prev" aria-label="Previous slide"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg></button>
      <button class="hero-next" aria-label="Next slide"><svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg></button>
    </div>
  </div>
</section>


<section class="section">
  <div class="wrap statement wide reveal">
    <h2 class="h2">Born from a simple wish to give the gift of better health.</h2>
    <p class="lede">Wellnergie was born from a simple wish to give the gift of better health to the people we love.</p>
    <p class="lede" style="margin-top:14px">Founded in Singapore in 2019, Wellnergie is a wellness technology company built on over 20 years of research, experimentation and technological development.</p>
    <p class="lede" style="margin-top:14px">Our journey began with a vision to explore natural therapy through the fusion of carefully selected natural materials and innovative energy based technology, creating thoughtful wellness solutions designed for everyday life.</p>
    <p class="lede" style="margin-top:14px">At the heart of our work is Wellnergie Wave Technology, our proprietary technology developed to transfer energy waves through our products and support the body's natural wellbeing.</p>
    <a class="btn" style="margin-top:32px" href="about.html">Our story</a>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head reveal"><div><h2 class="h2">Our Products</h2></div></div>
    <div class="grid grid-big">{cards}</div>
  </div>
</section>

<section class="section">
  <div class="wrap split reveal">
    <div class="split-media contain"><img src="{img(BY_SLUG['wetube'], 2)}" alt="WeTube" loading="lazy"></div>
    <div class="split-body">
      <span class="eyebrow">WeTube</span>
      <h2 class="h2">Our flagship, <span class="accent">refined.</span></h2>
      <p class="lede">Our flagship product, WeTube channels the power of anions to cleanse water, turning it from harmful acidic water to clean, detoxified alkaline water. It is also infused with Wellnergie wave, to reduce discomfort, improve sleep quality, block electromagnetic waves, and more.</p>
      <a class="btn" href="product/wetube.html">Shop WeTube</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split reverse reveal">
    <div class="split-media"><img src="assets/hero/card-wrist.jpg" alt="WeBand" loading="lazy"></div>
    <div class="split-body">
      <span class="eyebrow">WeBand</span>
      <h2 class="h2">Beyond just gold <span class="accent">and silver.</span></h2>
      <p class="lede">Beyond just gold and silver, Wellnergie WeBand is wellness &amp; health. Infused with energy through negative ions, the WeBand strengthens blood circulation, eliminating fatigue &amp; improving immunity.</p>
      <p class="lede">The WeBand can increase strength by up to 35%, and improve endurance by up to 60%, and blocks harmful electromagnetic waves from phones &amp; appliances.</p>
      <a class="btn" href="shop.html#weband">Shop WeBand</a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap wave-callout reveal">
    <div>
      <span class="eyebrow" style="color:var(--gold-soft)">Our Technology</span>
      <h2 class="h2" style="margin:12px 0 18px">How <span class="accent">Wellnergie Wave</span> works.</h2>
      <p>Wellnergie Wave Technology is designed to enable our products to transfer energy waves toward the body during use.</p>
      <p style="margin-top:12px">The wave is designed to interact within an effective range of approximately 12 to 15 cm from the material, allowing the product and the body to remain connected without requiring direct contact in every application.</p>
      <a class="btn-pill light" style="margin-top:28px" href="technology.html">Discover our technology <span>›</span></a>
    </div>
    <ul>
      <li>Over 20 years of research, experimentation and technological development</li>
      <li>Materials science, physics and chemistry with carefully selected natural mineral materials</li>
      <li>Proprietary process to create specific energy characteristics</li>
      <li>Effective range of approximately 12 to 15 cm from the material</li>
      <li>Designed to support blood circulation and everyday physical wellbeing, including strength, flexibility and vitality</li>
    </ul>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap statement reveal">
    <h2 class="h2">Real results. Experience it.</h2>
    <a class="btn-pill" style="margin-top:28px" href="testimonials.html">Watch testimonials <span>›</span></a>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap statement wide reveal">
    <h2 class="h2">One technology. Three generations.<br><span class="accent">Greatest Gift of Health</span></h2>
    <p class="lede">Health and wellbeing matter at every age. Wellnergie products are designed to be suitable for everyday wellness across three generations of the family, from younger adults to parents and grandparents.</p>
    <p class="lede" style="margin-top:14px">We believe wellness should be something families can share. Everyone deserves the opportunity to feel their best and enjoy daily life with greater comfort and vitality.</p>
    <p class="accent-line">To live well, feel well and enjoy more of life together.</p>
  </div>
</section>

<section class="section contact-block">
  <div class="wrap statement reveal">
    <h2 class="h3 contact-title">Contact Us</h2>
    <p class="lede" style="margin-inline:auto;text-align:center">For product inquiries, partnership opportunities,<br>or general questions, please contact us using the form below.</p>
    <a class="btn-pill" style="margin-top:28px" href="contact.html">Contact Us <span>›</span></a>
  </div>
</section>
{LIGHTBOX}
""" + footer("")

def page_shop():
    cards = "\n".join(product_card(p) for p in PRODUCTS)
    return head("Shop / Products", "") + "<body>" + header("", "Shop", light=True) + f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Shop</span>
    <h1 class="h1">Our Products</h1>
    <p class="lede">A refined collection made to move with you.</p>
  </div>
</section>
<section id="weband" class="section shop-area" style="padding-top:0">
  <div class="wrap">
    <div class="chips" style="margin-bottom:30px">
      <button class="is-active" data-filter="all">All</button>
      <button data-filter="weband">WeBand</button>
      <button data-filter="wetube">WeTube</button>
      <button data-filter="wespec">WeSpec</button>
      <button data-filter="wellness">Wellness</button>
    </div>
    <div class="grid">{cards}</div>
  </div>
</section>
""" + footer("")

def page_product(p):
    rel = "../"
    imgs = IMAGES[p["slug"]]
    order = p["order"]
    thumbs = "".join(f'<button data-src="{rel}{imgs[i]}"{act(k == 0)} aria-label="Photo {k+1}"><img src="{rel}{imgs[i]}" alt="" loading="lazy"></button>' for k, i in enumerate(order))
    opts = ""
    for label, vals in p["options"]:
        sw = ""
        for k, (v, idx) in enumerate(vals):
            colour = next((c for c in DOT if v.endswith(c) or v == c), None)
            dot = f'<i style="--dot:{DOT[colour]}"></i>' if colour else ""
            data = f' data-img="{rel}{imgs[idx]}"' if idx is not None else ""
            sw += f'<button class="swatch{" is-active" if k == 0 else ""}"{data}>{dot}{esc(v)}</button>'
        opts += f'<div class="option"><div class="label">{label}</div><div class="swatches">{sw}</div></div>'
    desc = "".join(f"<p>{esc(d)}</p>" for d in p["description"])
    funcs = "".join(f"<li>{esc(f)}</li>" for f in p["functions"])
    specs = "".join(f"<tr><td>{esc(k)}</td><td>{esc(v)}</td></tr>" for k, v in p["specs"])
    related = [q for q in PRODUCTS if q["slug"] != p["slug"] and q["cat"] == p["cat"]][:4]
    if len(related) < 4:
        related += [q for q in PRODUCTS if q["slug"] != p["slug"] and q not in related][:4 - len(related)]
    rel_cards = "\n".join(product_card(q, rel) for q in related)
    buy = f"{WIX}/product-page/{WIX_SLUG[p['slug']]}"
    cmp_html = f'<s>SGD {p["compare"]:.2f}</s>' if p.get("compare") else ""
    return head(p["name"], rel, p["short"]) + "<body>" + header(rel, "Shop", light=True) + f"""
<section class="wrap product-layout">
  <div class="gallery">
    <div class="gallery-thumbs">{thumbs}</div>
    <div class="gallery-main">
      <img src="{rel}{imgs[order[0]]}" alt="{esc(p['name'])}">
      <button class="g-prev" aria-label="Previous photo"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg></button>
      <button class="g-next" aria-label="Next photo"><svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg></button>
    </div>
  </div>
  <div class="product-summary">
    <div class="breadcrumb"><a href="{rel}index.html">Home</a><span>/</span><a href="{rel}shop.html">Shop</a><span>/</span><span>{p['cat_label']}</span></div>
    <div class="vendor">Wellnergie{' · ' + p['badge'] if p['badge'] else ''}</div>
    <h1 class="h1">{esc(card_title(p))}</h1>
    <div class="price">{cmp_html}<span>{price(p)}</span></div>
    <a class="rating" href="{GOOGLE_MAPS_URL}" target="_blank" rel="noopener">{stars(5)}<span>{GOOGLE_RATING} · {GOOGLE_COUNT} Google reviews</span></a>
    <p class="short">{esc(p['short'])}</p>
    {opts}
    <div class="option"><div class="label">Quantity</div>
      <div class="qty"><button data-dir="down" aria-label="Decrease">−</button><input type="number" value="1" min="1" aria-label="Quantity"><button data-dir="up" aria-label="Increase">+</button></div></div>
    <div class="buy-col">
      <a class="btn btn-solid" href="{buy}" target="_blank" rel="noopener">Add to cart</a>
      <a class="btn" href="{buy}" target="_blank" rel="noopener">Buy it now</a>
    </div>
    <div class="marketplaces">More payment options: <a href="https://shopee.sg/wellnergie" target="_blank" rel="noopener">Shopee</a> <a href="https://www.lazada.sg/shop/wellnergie-sg" target="_blank" rel="noopener">Lazada</a> {payment_icons(rel)}</div>
    <div class="tabs">
      <div class="tab-bar" role="tablist">
        <button class="is-active" data-tab="t-desc">Description</button>
        <button data-tab="t-func">Functions</button>
        <button data-tab="t-spec">Specification</button>
        <button data-tab="t-faq">Care &amp; FAQ</button>
      </div>
      <div class="tab-panel is-active" id="t-desc">{desc}</div>
      <div class="tab-panel" id="t-func"><ul class="check-list">{funcs}</ul></div>
      <div class="tab-panel" id="t-spec"><table class="spec-table">{specs}</table></div>
      <div class="tab-panel" id="t-faq"><p>Clean with water and let dry naturally. Do not use detergent. See our <a href="{rel}faq.html" style="text-decoration:underline">FAQ</a> for more common queries.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head"><div><span class="eyebrow">You may also like</span><h2 class="h2">Complete the set.</h2></div><a class="link-arrow" href="{rel}shop.html">All products {ARROW}</a></div>
    <div class="grid">{rel_cards}</div>
  </div>
</section>
""" + footer(rel)

def page_technology():
    materials = ["Tourmaline", "Negative Ion / Far-Infrared Powder", "Germanium", "Titanium / Bio-Silica Gel"]
    mats = "".join(f'<div class="material reveal"><span class="num">0{k+1}</span><div><h3>{esc(n)}</h3></div></div>' for k, n in enumerate(materials))
    return head("Technology", "") + "<body>" + header("", "Technology", light=True) + f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Our Technology</span>
    <h1 class="h1">The science behind</h1>
    <span class="accent">Wellnergie.</span>
    <p class="lede">At Wellnergie, we bring together knowledge from materials science, physics and chemistry with carefully selected natural mineral materials.</p>
    <p class="lede" style="margin-top:14px">Through more than two decades of experimentation and development, we have refined our approach and established Wellnergie Wave Technology, which forms the technological foundation of our products.</p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap split reveal">
    <div class="split-media contain"><img src="{img(BY_SLUG['wetube'], 4)}" alt="WeTube materials" loading="lazy"></div>
    <div class="split-body">
      <span class="eyebrow">Energy and Natural Materials</span>
      <h2 class="h2">Natural minerals, <span class="accent">refined.</span></h2>
      <p class="lede">Natural minerals possess distinctive physical characteristics. Our research explores how suitable materials can be selected, processed and developed for energy based applications.</p>
      <p class="lede">Through our proprietary process, selected materials are treated to create specific energy characteristics that can be incorporated into our products.</p>
      <p class="lede">This combination of natural materials and Wellnergie Wave Technology is at the heart of the Wellnergie approach.</p>
    </div>
  </div>
</section>

<section class="section" style="background:var(--ivory-2)">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">Carefully selected natural materials</span><h2 class="h2">What our products are made from.</h2></div></div>
    <div class="materials">{mats}</div>
  </div>
</section>

<section class="section">
  <div class="wrap split reverse reveal">
    <div class="split-media"><img src="assets/hero/hero-weband.jpg" alt="WeBand worn every day" loading="lazy" style="object-position:70% 40%"></div>
    <div class="split-body">
      <span class="eyebrow">How Wellnergie Wave Works</span>
      <h2 class="h2">Energy waves, <span class="accent">toward the body.</span></h2>
      <p class="lede">Wellnergie Wave Technology is designed to enable our products to transfer energy waves toward the body during use.</p>
      <p class="lede">The wave is designed to interact within an effective range of approximately 12 to 15 cm from the material, allowing the product and the body to remain connected without requiring direct contact in every application.</p>
      <p class="lede">Through this energy based approach, our products are designed to support blood circulation and everyday physical wellbeing, including strength, flexibility and vitality.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap wave-callout reveal">
    <div>
      <span class="eyebrow" style="color:var(--gold-soft)">Technology With a Purpose</span>
      <h2 class="h2" style="margin:12px 0 18px">Technology should ultimately <span class="accent">serve people.</span></h2>
      <p>We believe technology should ultimately serve people.</p>
      <p style="margin-top:12px">Our goal is to transform complex research into practical products that can naturally fit into everyday life, making our technology simple to use while supporting a proactive approach to wellness.</p>
      <a class="btn btn-light" style="margin-top:28px" href="shop.html">Shop the collection</a>
    </div>
    <ul>
      <li>Over 20 years of research, experimentation and technological development</li>
      <li>Materials science, physics and chemistry with carefully selected natural mineral materials</li>
      <li>Proprietary process to create specific energy characteristics</li>
      <li>Effective range of approximately 12 to 15 cm from the material</li>
      <li>Simple to use, supporting a proactive approach to wellness</li>
    </ul>
  </div>
</section>

<section class="section statement" style="padding-top:0">
  <div class="wrap reveal">
    <h2 class="h2">Talk to our team today</h2>
    <p class="lede">Find out how our products can help enhance you and your loved ones' vitality.</p>
    <a class="btn" style="margin-top:28px" href="contact.html">Contact us</a>
  </div>
</section>
""" + footer("")

def page_about():
    return head("About Us", "") + "<body>" + header("", "About Us", light=True) + f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Our Story</span>
    <h1 class="h1">It started with family</h1>
    <span class="accent">Greatest Gift of Health.</span>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap split reveal">
    <div class="split-media"><img src="assets/hero/hero-wetube.jpg" alt="Wellnergie" loading="lazy" style="object-position:60% 40%"></div>
    <div class="split-body">
      <p class="lede">Wellnergie began with our founder, Mr Thomas Tan, and his desire to help his parents.</p>
      <p class="lede">For many years, he witnessed his parents experience long term health challenges. Seeing the people he loved struggle with their wellbeing inspired him to search for another way to support a healthier and more comfortable life.</p>
      <p class="lede">That personal search became the beginning of Wellnergie.</p>
      <span class="eyebrow" style="display:block;margin-top:34px">From a Personal Wish to a Greater Mission</span>
      <p class="lede" style="margin-top:12px">Working alongside technical and research teams, our founder began exploring the relationship between energy, natural materials and the human body.</p>
      <p class="lede">Through years of research, experimentation and refinement, we developed our approach to natural therapy, bringing together carefully selected natural materials and energy based technology to create innovative wellness solutions for everyday life.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap vm reveal">
    <div><span class="eyebrow">Our Mission</span><p>To bring innovative wellness technology to people around the world, thoughtfully designed to support a healthier, more balanced and elevated way of living.</p></div>
    <div><span class="eyebrow">Our Vision — Building a Healthier Future Together</span><p>To pursue excellence in quality, advance wellness technology and build Wellnergie into a trusted international wellness brand.</p></div>
  </div>
</section>

<section class="section" style="background:var(--ivory-2)">
  <div class="wrap split reverse reveal">
    <div class="split-media contain" style="aspect-ratio:1/.8"><img src="assets/logo/mark-colour.png" alt="Wellnergie WE logo" loading="lazy" style="padding:14%"></div>
    <div class="split-body">
      <span class="eyebrow">Why Wellnergie</span>
      <h2 class="h2">Wellness <span class="accent">+ Energy</span></h2>
      <p class="lede">The name Wellnergie combines the two ideas at the heart of our brand.</p>
      <p class="lede"><strong>Wellness</strong> represents our purpose and our desire to help people live healthier, more energetic and fulfilling lives.</p>
      <p class="lede"><strong>Energy</strong> represents our technological direction and our exploration of energy based applications using natural materials.</p>
      <p class="lede">Together, they form Wellnergie.</p>
      <p class="lede">Our WE logo represents the first letters of Wellness and Energy. The rising sun above the letters symbolises light, vitality, renewal and positive energy reaching people around the world.</p>
      <p class="accent" style="font-size:28px;margin-top:20px">It reflects our belief that health brings light into life.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap statement reveal">
    <span class="eyebrow">Our Philosophy</span>
    <h2 class="h2">Health is not just number one. <span class="accent">It is the only one.</span></h2>
    <p class="lede">Modern life can place significant demands on our bodies. Stress, irregular routines, poor sleep, sedentary lifestyles and demanding schedules can all affect how we feel each day.</p>
    <p class="lede" style="margin-top:14px">Sometimes these effects may be mild and easy to overlook, but they can still influence our comfort, energy and quality of life. We believe this is why everyday wellness matters.</p>
    <p class="accent-line">Taking care of ourselves should not begin only when something goes wrong. It should be part of how we live every day.</p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap wave-callout reveal">
    <div>
      <span class="eyebrow" style="color:var(--gold-soft)">Our Values</span>
      <h2 class="h2" style="margin:12px 0 18px">Health first. <span class="accent">People always.</span></h2>
      <p>Wellnergie was created from a desire to help the people we love.</p>
      <p style="margin-top:12px">That spirit remains at the heart of our company. We believe business should create value for people and contribute positively to society.</p>
    </div>
    <div>
      <p>Since our beginning in Singapore, we have continued to develop, learn and grow.</p>
      <p style="margin-top:12px">As more people discover our products and place their trust in Wellnergie, we remain committed to the same purpose that started it all: helping people live healthier, more energetic lives.</p>
      <a class="btn btn-light" style="margin-top:28px" href="shop.html">Shop the collection</a>
    </div>
  </div>
</section>
""" + footer("")

def page_faq():
    weband = [("Is the WeBand waterproof?", "It is made of a special waterproof silicone compound that is resistant to high and low temperatures. Even bathing or swimming can be worn. Avoid contact with chemical components Shower Gel."),
              ("Will the negative ions in the product last for indefinite period?", "The negative ions emitted by the product have a certain time effect. After being exposed to skin heat and air, the negative ions content will not change much within 3 years under normal wear and maintenance, and the negative ions content will gradually decrease with use after 3 years."),
              ("Is the WeBand suitable for everyone to wear?", "Pregnant women, patients with severe heart disease, and those who use medical electronic devices embedded in the body such as cardiac pacemakers, and patients with severe cardiovascular and cerebrovascular diseases, is recommended to consult a doctor before using our product."),
              ("How do I maintain the WeBand for daily usage? Can the product be cleaned?", "You can use clean water for cleaning. Let dry naturally. If it stick to dust during wearing, use tape or stickers to remove the dust."),
              ("Can I wear the WeBand while sleeping?", "It is better to wear it while sleeping. Helps sleep quality."),
              ("Are there any side effects to wearing the WeBand?", "The main raw materials of negative ion energy products are made of safe food appliance grade silicone, similar to baby pacifiers or human body silicone supplement materials, so please feel free to wear it.")]
    wetube = [("What shall I do for first time use?", "Please wash with water a few times and discard the water. (For external usage, do not need to wash, use directly. Best to keep it dry)"),
              ("How long can the WeTube negative ions last?", "WETUBE energy function can last for 2 years as a water purifier and 4 years as a wearable product. It will depend on the frequency of usage, water conditions, and maintenance of the WETUBE."),
              ("How do I maintain the WeTube for daily usage? Can it be cleaned with any detergent?", "You can just use clean water for cleaning and let it dry naturally. Do not use any detergent to wash it."),
              ("Are there any side effects on the usage of WeTube?", "The main raw materials of negative ion energy products are from natural earth materials like Ion energy stone, Tourmaline, Maifan, Volcanic, negative Ion stone, Far-infrared stone which are non-toxic. The tube is made of Porcelain is a material that is strong, smooth, and non-toxic but breakable. It has a high level of mechanical resistance, low porosity, and high density, which, on a daily basis, provide it with durability, innocuity, soft touch and beauty."),
              ("How can I prevent my WeTube from break?", "Store your WETUBE in a safe place, away from young kids which may cause it to accidentally fall to the floor. WETUBE will not break easily in hot water and hot sun.")]
    def acc(items): return '<div class="accordion">' + "".join(f"<details><summary>{esc(q)}</summary><div class='body'><p>{esc(a)}</p></div></details>" for q, a in items) + "</div>"
    return head("FAQ", "") + "<body>" + header("", "", light=True) + f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h1 class="h1">Common Queries</h1>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap narrow">
    <div class="faq-tabs"><button class="is-active" data-panel="faq-weband">WeBand</button><button data-panel="faq-wetube">WeTube</button></div>
    <div class="faq-panel is-active" id="faq-weband">{acc(weband)}</div>
    <div class="faq-panel" id="faq-wetube">{acc(wetube)}</div>
    <div style="margin-top:48px" class="reveal">
      <span class="eyebrow">Need more help?</span>
      <p class="lede" style="margin-top:10px">Send us a message today through the contact form, or call us at <a href="tel:+6591828291">+65 9182 8291</a> / <a href="tel:+6597519272">+65 9751 9272</a>.</p>
      <a class="btn" style="margin-top:24px" href="contact.html">Contact us</a>
    </div>
  </div>
</section>
""" + footer("")

def page_testimonials():
    featured = t_card(*TESTIMONIALS[0], cls="t-card t-featured")
    rest = "".join(t_card(v, t) for v, t in TESTIMONIALS[1:])
    return head("Testimonials", "") + "<body>" + header("", "", light=True) + f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Testimonials</span>
    <h1 class="h1">Hear what people say about Wellnergie</h1>
    <span class="accent">Real stories, in their own words.</span>
    <p class="lede">Wellnergie was created from a desire to help the people we love. Watch how our products have become part of everyday wellness for our customers and their families.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="reveal">{featured}</div>
    <div class="t-grid" style="margin-top:22px">{rest}</div>
  </div>
</section>
{google_reviews()}
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="statement">
      <p class="lede" style="margin-inline:auto">More stories on our YouTube channel and social media.</p>
      <div class="social-links" style="margin-top:20px">
        <a class="btn" href="https://www.youtube.com/channel/UCH2cXZnySNUCifJ7l15ldNw" target="_blank" rel="noopener">Visit our YouTube channel</a>
        <a class="btn btn-solid" href="shop.html">Shop the collection</a>
      </div>
    </div>
  </div>
</section>
{LIGHTBOX}
""" + footer("")

def page_contact():
    return head("Contact Us", "") + "<body>" + header("", "", light=True) + f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Contact Us</span>
    <h1 class="h1">Give the gift of health</h1>
    <span class="accent">to your loved ones.</span>
    <p class="lede">Contact us for more information.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap contact-grid">
    <form class="form reveal">
      <div class="row">
        <label>Name<input name="name" required></label>
        <label>Contact Number<input name="phone" type="tel"></label>
      </div>
      <label>Email Address<input name="email" type="email" required></label>
      <label>Reason for Contact
        <select name="reason"><option>General Enquiry</option><option>Product Enquiry</option><option>Order Support</option><option>Appointment</option><option>Partnership</option></select>
      </label>
      <label>Enter Your Message<textarea name="message"></textarea></label>
      <div><button class="btn btn-solid" type="submit">Submit</button></div>
    </form>
    <div class="info-blocks reveal">
      <div class="info-block"><div class="label">Address</div><p>1 Yishun Industrial Street 1<br>A'posh Bizhub #05-29<br>Singapore 768160</p></div>
      <div class="info-block"><div class="label">Operation Hours</div><p>Monday – Friday, 10.30am – 5pm<br>Closed on Weekends &amp; PHs</p><p class="muted" style="font-size:14px;margin-top:6px">Please WhatsApp / Call 8879 1727 for appointment</p></div>
      <div class="info-block"><div class="label">WhatsApp</div><p><a href="https://wa.me/6588791727">+65 8879 1727</a><br><a href="https://wa.me/6597519272">+65 9751 9272</a></p></div>
      <div class="info-block"><div class="label">Call</div><p><a href="tel:+6588791727">+65 8879 1727</a><br><a href="tel:+6597519272">+65 9751 9272</a></p></div>
      <div class="info-block"><div class="label">Email</div><p><a href="mailto:wellnergie@gmail.com">wellnergie@gmail.com</a><br><a href="mailto:wellnergieonline@gmail.com">wellnergieonline@gmail.com</a></p></div>
    </div>
  </div>
</section>
""" + footer("")

# ----------------------------------------------------------------------------
def write(path, content):
    path = SITE / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))

if __name__ == "__main__":
    write("index.html", page_home())
    write("shop.html", page_shop())
    write("technology.html", page_technology())
    write("about.html", page_about())
    write("faq.html", page_faq())
    write("testimonials.html", page_testimonials())
    write("contact.html", page_contact())
    for p in PRODUCTS:
        write(f"product/{p['slug']}.html", page_product(p))
