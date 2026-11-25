import pytest
from audit_tools import calc_vat


def test_calc_vat_success():
    assert calc_vat(100.0) == 20.0


def test_calc_vat_negative_amount():
    with pytest.raises(ValueError):
        calc_vat(-50.0)