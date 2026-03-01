"""
Data migration: seed the F1 2025 season data.

Creates:
- 4 Engine Suppliers (Economy): Honda RBPT, Ferrari, Mercedes, Renault
- 10 Constructors (Regime): all 10 F1 2025 teams
- 3 F1 Special events: World Champion, Monaco Maestro, Pole Position
- 20 F1 2025 drivers (Ball) with stats, nationalities, car numbers and special abilities

Image fields (wild_card, collection_card, Economy.icon, Regime.background) are set to
empty strings. Upload actual artwork through the admin panel after running migrations.
"""

from typing import TYPE_CHECKING

from django.db import migrations

if TYPE_CHECKING:
    from django.apps.registry import Apps
    from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def seed_f1_data(apps: "Apps", schema_editor: "BaseDatabaseSchemaEditor"):
    Economy = apps.get_model("bd_models", "Economy")
    Regime = apps.get_model("bd_models", "Regime")
    Ball = apps.get_model("bd_models", "Ball")
    Special = apps.get_model("bd_models", "Special")

    # ------------------------------------------------------------------
    # Engine Suppliers  (Economy)
    # ------------------------------------------------------------------
    honda, _ = Economy.objects.get_or_create(name="Honda RBPT", defaults={"icon": ""})
    ferrari_eng, _ = Economy.objects.get_or_create(name="Ferrari", defaults={"icon": ""})
    mercedes_eng, _ = Economy.objects.get_or_create(name="Mercedes", defaults={"icon": ""})
    renault_eng, _ = Economy.objects.get_or_create(name="Renault", defaults={"icon": ""})

    # ------------------------------------------------------------------
    # Constructors  (Regime — card background per team)
    # ------------------------------------------------------------------
    red_bull, _ = Regime.objects.get_or_create(name="Red Bull Racing", defaults={"background": ""})
    ferrari, _ = Regime.objects.get_or_create(name="Ferrari", defaults={"background": ""})
    mclaren, _ = Regime.objects.get_or_create(name="McLaren", defaults={"background": ""})
    mercedes, _ = Regime.objects.get_or_create(name="Mercedes", defaults={"background": ""})
    aston_martin, _ = Regime.objects.get_or_create(name="Aston Martin", defaults={"background": ""})
    alpine, _ = Regime.objects.get_or_create(name="Alpine", defaults={"background": ""})
    williams, _ = Regime.objects.get_or_create(name="Williams", defaults={"background": ""})
    haas, _ = Regime.objects.get_or_create(name="Haas", defaults={"background": ""})
    racing_bulls, _ = Regime.objects.get_or_create(name="Racing Bulls", defaults={"background": ""})
    kick_sauber, _ = Regime.objects.get_or_create(name="Kick Sauber", defaults={"background": ""})

    # ------------------------------------------------------------------
    # F1 Special events
    # ------------------------------------------------------------------
    Special.objects.get_or_create(
        name="World Champion",
        defaults={
            "catch_phrase": "A true legend of the sport!",
            "rarity": 0.05,
            "emoji": "🏆",
            "tradeable": True,
            "hidden": False,
            "credits": "F1Dex Team",
        },
    )
    Special.objects.get_or_create(
        name="Monaco Maestro",
        defaults={
            "catch_phrase": "King of the streets of Monaco!",
            "rarity": 0.08,
            "emoji": "🎰",
            "tradeable": True,
            "hidden": False,
            "credits": "F1Dex Team",
        },
    )
    Special.objects.get_or_create(
        name="Pole Position",
        defaults={
            "catch_phrase": "Fastest in qualifying — lights out!",
            "rarity": 0.12,
            "emoji": "⚡",
            "tradeable": True,
            "hidden": False,
            "credits": "F1Dex Team",
        },
    )

    # ------------------------------------------------------------------
    # F1 2025 Drivers  (Ball)
    # health  = consistency / reliability score
    # attack  = raw pace / aggression score
    # rarity  = collectible rarity weight (0–1; higher = rarer to spawn)
    # ------------------------------------------------------------------
    drivers = [
        # ── Red Bull Racing (Honda RBPT) ────────────────────────────────
        {
            "country": "Max Verstappen",
            "nationality": "Dutch",
            "car_number": 1,
            "championships": 4,
            "health": 95,
            "attack": 100,
            "rarity": 0.9,
            "regime": red_bull,
            "economy": honda,
            "capacity_name": "Tire Whisperer",
            "capacity_description": (
                "Exceptional tire management; conserves rubber while maintaining blistering pace on worn tyres."
            ),
            "catch_names": "verstappen;max;the dutchman",
        },
        {
            "country": "Liam Lawson",
            "nationality": "New Zealander",
            "car_number": 30,
            "championships": 0,
            "health": 70,
            "attack": 75,
            "rarity": 0.3,
            "regime": red_bull,
            "economy": honda,
            "capacity_name": "Fearless Charger",
            "capacity_description": (
                "No fear when attacking; maximum aggression in any wheel-to-wheel situation."
            ),
            "catch_names": "lawson;liam",
        },
        # ── Ferrari ─────────────────────────────────────────────────────
        {
            "country": "Charles Leclerc",
            "nationality": "Monegasque",
            "car_number": 16,
            "championships": 0,
            "health": 90,
            "attack": 92,
            "rarity": 0.7,
            "regime": ferrari,
            "economy": ferrari_eng,
            "capacity_name": "Saturday King",
            "capacity_description": (
                "Devastating one-lap qualifying pace that consistently puts him at the front of the grid."
            ),
            "catch_names": "leclerc;charles;sharl",
        },
        {
            "country": "Lewis Hamilton",
            "nationality": "British",
            "car_number": 44,
            "championships": 7,
            "health": 88,
            "attack": 90,
            "rarity": 0.95,
            "regime": ferrari,
            "economy": ferrari_eng,
            "capacity_name": "Rain Master",
            "capacity_description": (
                "Performance elevates in wet conditions; arguably unbeatable when the track is soaked."
            ),
            "catch_names": "hamilton;lewis;sir lewis",
        },
        # ── McLaren (Mercedes) ───────────────────────────────────────────
        {
            "country": "Lando Norris",
            "nationality": "British",
            "car_number": 4,
            "championships": 0,
            "health": 88,
            "attack": 90,
            "rarity": 0.6,
            "regime": mclaren,
            "economy": mercedes_eng,
            "capacity_name": "Smooth Operator",
            "capacity_description": (
                "Silky smooth driving style with exceptional precision; rarely makes errors under pressure."
            ),
            "catch_names": "norris;lando",
        },
        {
            "country": "Oscar Piastri",
            "nationality": "Australian",
            "car_number": 81,
            "championships": 0,
            "health": 83,
            "attack": 85,
            "rarity": 0.4,
            "regime": mclaren,
            "economy": mercedes_eng,
            "capacity_name": "Ice Nerve",
            "capacity_description": (
                "Unflappable composure under pressure; delivers his best when the stakes are at their highest."
            ),
            "catch_names": "piastri;oscar",
        },
        # ── Mercedes ────────────────────────────────────────────────────
        {
            "country": "George Russell",
            "nationality": "British",
            "car_number": 63,
            "championships": 0,
            "health": 85,
            "attack": 87,
            "rarity": 0.55,
            "regime": mercedes,
            "economy": mercedes_eng,
            "capacity_name": "Strategy Master",
            "capacity_description": (
                "Excels at reading the race and extracting maximum benefit from strategic opportunities."
            ),
            "catch_names": "russell;george",
        },
        {
            "country": "Kimi Antonelli",
            "nationality": "Italian",
            "car_number": 12,
            "championships": 0,
            "health": 72,
            "attack": 80,
            "rarity": 0.35,
            "regime": mercedes,
            "economy": mercedes_eng,
            "capacity_name": "Future Star",
            "capacity_description": (
                "Blessed with raw natural speed; tipped to become Formula 1 champion within years."
            ),
            "catch_names": "antonelli;kimi;andrea;andrea kimi",
        },
        # ── Aston Martin (Mercedes) ──────────────────────────────────────
        {
            "country": "Fernando Alonso",
            "nationality": "Spanish",
            "car_number": 14,
            "championships": 2,
            "health": 87,
            "attack": 88,
            "rarity": 0.85,
            "regime": aston_martin,
            "economy": mercedes_eng,
            "capacity_name": "El Plan",
            "capacity_description": (
                "A tactical genius who can extract the maximum possible result from any piece of machinery."
            ),
            "catch_names": "alonso;fernando;nando;el nano",
        },
        {
            "country": "Lance Stroll",
            "nationality": "Canadian",
            "car_number": 18,
            "championships": 0,
            "health": 68,
            "attack": 70,
            "rarity": 0.3,
            "regime": aston_martin,
            "economy": mercedes_eng,
            "capacity_name": "Sunday Racer",
            "capacity_description": (
                "Consistently stronger on race day than in qualifying; comes alive when the lights go out."
            ),
            "catch_names": "stroll;lance",
        },
        # ── Alpine (Renault) ─────────────────────────────────────────────
        {
            "country": "Pierre Gasly",
            "nationality": "French",
            "car_number": 10,
            "championships": 0,
            "health": 75,
            "attack": 78,
            "rarity": 0.45,
            "regime": alpine,
            "economy": renault_eng,
            "capacity_name": "Underdog Spirit",
            "capacity_description": (
                "Consistently punches above his car's weight class; excels in adverse conditions."
            ),
            "catch_names": "gasly;pierre",
        },
        {
            "country": "Jack Doohan",
            "nationality": "Australian",
            "car_number": 7,
            "championships": 0,
            "health": 65,
            "attack": 70,
            "rarity": 0.25,
            "regime": alpine,
            "economy": renault_eng,
            "capacity_name": "Wild Card",
            "capacity_description": (
                "Shows flashes of brilliant natural speed; a wildcard capable of surprising anyone."
            ),
            "catch_names": "doohan;jack",
        },
        # ── Williams (Mercedes) ──────────────────────────────────────────
        {
            "country": "Alexander Albon",
            "nationality": "Thai",
            "car_number": 23,
            "championships": 0,
            "health": 76,
            "attack": 78,
            "rarity": 0.4,
            "regime": williams,
            "economy": mercedes_eng,
            "capacity_name": "Comeback Kid",
            "capacity_description": (
                "Incredible determination and resilience; always returns stronger after every setback."
            ),
            "catch_names": "albon;alexander;alex",
        },
        {
            "country": "Carlos Sainz",
            "nationality": "Spanish",
            "car_number": 55,
            "championships": 0,
            "health": 84,
            "attack": 85,
            "rarity": 0.55,
            "regime": williams,
            "economy": mercedes_eng,
            "capacity_name": "Smooth Carlos",
            "capacity_description": (
                "Exceptionally smooth driving style that preserves tyres and consistently scores big points."
            ),
            "catch_names": "sainz;carlos;chili",
        },
        # ── Haas (Ferrari) ───────────────────────────────────────────────
        {
            "country": "Oliver Bearman",
            "nationality": "British",
            "car_number": 87,
            "championships": 0,
            "health": 68,
            "attack": 72,
            "rarity": 0.3,
            "regime": haas,
            "economy": ferrari_eng,
            "capacity_name": "Rising Star",
            "capacity_description": (
                "Stunned the paddock with an impressive debut in 2024; destined for regular F1 success."
            ),
            "catch_names": "bearman;oliver;oli",
        },
        {
            "country": "Esteban Ocon",
            "nationality": "French",
            "car_number": 31,
            "championships": 0,
            "health": 73,
            "attack": 74,
            "rarity": 0.35,
            "regime": haas,
            "economy": ferrari_eng,
            "capacity_name": "Never Say Die",
            "capacity_description": (
                "Relentless fighting spirit; pushes the car to its absolute limits and never gives up."
            ),
            "catch_names": "ocon;esteban",
        },
        # ── Racing Bulls (Honda RBPT) ────────────────────────────────────
        {
            "country": "Yuki Tsunoda",
            "nationality": "Japanese",
            "car_number": 22,
            "championships": 0,
            "health": 76,
            "attack": 80,
            "rarity": 0.45,
            "regime": racing_bulls,
            "economy": honda,
            "capacity_name": "Samurai Spirit",
            "capacity_description": (
                "Short fuse but blindingly fast; takes no prisoners in wheel-to-wheel combat on track."
            ),
            "catch_names": "tsunoda;yuki",
        },
        {
            "country": "Isack Hadjar",
            "nationality": "French",
            "car_number": 6,
            "championships": 0,
            "health": 65,
            "attack": 70,
            "rarity": 0.25,
            "regime": racing_bulls,
            "economy": honda,
            "capacity_name": "F2 Champion",
            "capacity_description": (
                "Arrives with championship pedigree from Formula 2; ready to prove himself at the top."
            ),
            "catch_names": "hadjar;isack",
        },
        # ── Kick Sauber (Ferrari) ────────────────────────────────────────
        {
            "country": "Nico Hulkenberg",
            "nationality": "German",
            "car_number": 27,
            "championships": 0,
            "health": 74,
            "attack": 76,
            "rarity": 0.4,
            "regime": kick_sauber,
            "economy": ferrari_eng,
            "capacity_name": "Hulk Smash",
            "capacity_description": (
                "Aggressive and direct racing style; never backs down from any battle on track."
            ),
            "catch_names": "hulkenberg;nico;hulk",
        },
        {
            "country": "Gabriel Bortoleto",
            "nationality": "Brazilian",
            "car_number": 5,
            "championships": 0,
            "health": 66,
            "attack": 71,
            "rarity": 0.25,
            "regime": kick_sauber,
            "economy": ferrari_eng,
            "capacity_name": "Senna's Legacy",
            "capacity_description": (
                "Carries the Brazilian racing spirit to F1; raw speed and fearless commitment define him."
            ),
            "catch_names": "bortoleto;gabriel",
        },
    ]

    for d in drivers:
        Ball.objects.get_or_create(
            country=d["country"],
            defaults={
                "nationality": d["nationality"],
                "car_number": d["car_number"],
                "championships": d["championships"],
                "health": d["health"],
                "attack": d["attack"],
                "rarity": d["rarity"],
                "emoji_id": 0,
                "wild_card": "",
                "collection_card": "",
                "credits": "F1Dex Team",
                "capacity_name": d["capacity_name"],
                "capacity_description": d["capacity_description"],
                "capacity_logic": {},
                "enabled": True,
                "tradeable": True,
                "regime": d["regime"],
                "economy": d["economy"],
                "catch_names": d["catch_names"],
            },
        )


class Migration(migrations.Migration):
    dependencies = [("bd_models", "0015_f1_driver_fields")]

    operations = [
        migrations.RunPython(seed_f1_data, reverse_code=migrations.RunPython.noop),
    ]
