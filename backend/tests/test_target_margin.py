"""Unit tests: saran harga jual dari target margin (harga = HPP / (1 - margin))."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault("MONGO_URL", "mongodb://localhost:27017")
os.environ.setdefault("DB_NAME", "test_hpp")
from core import compute_hpp, suggest_price


def mat(price):
    return {"id": "m1", "name": "Bahan", "last_price": price, "conversion_factor": 1, "usage_unit": "pcs", "purchase_unit": "pcs"}


def test_suggest_price_formula():
    s = suggest_price(7000, 30)
    assert s["suggested_price"] == 10000  # 7000 / 0.7
    assert s["suggested_price_rounded"] == 10000
    assert s["suggested_profit_per_unit"] == 3000
    # margin dari harga jual: 3000/10000 = 30%
    assert round(s["suggested_profit_per_unit"] / s["suggested_price"] * 100, 6) == 30


def test_suggest_price_rounding_up_to_100():
    s = suggest_price(990, 30)
    assert round(s["suggested_price"], 4) == 1414.2857
    assert s["suggested_price_rounded"] == 1500


def test_suggest_price_invalid_margin():
    assert suggest_price(1000, 100)["suggested_price"] is None
    assert suggest_price(1000, -5)["suggested_price"] is None
    assert suggest_price(None, 30)["suggested_price"] is None
    assert suggest_price(1000, None) == {}


def test_compute_hpp_with_and_without_target_margin():
    items = [{"material_id": "m1", "qty": 1, "unit": "pcs", "waste_pct": 0}]
    r = compute_hpp(items, [], 10, 0, {"m1": mat(50000)}, {})
    assert "suggested_price" not in r
    r = compute_hpp(items, [], 10, 0, {"m1": mat(50000)}, {}, target_margin=20)
    assert r["hpp_per_unit"] == 5000
    assert r["suggested_price"] == 6250  # 5000 / 0.8
    assert r["target_margin_pct"] == 20
