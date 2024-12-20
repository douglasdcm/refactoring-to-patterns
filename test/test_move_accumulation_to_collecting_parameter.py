from src.move_accumulation_to_collecting_parameter import run_refac


def test_run_refac():
    xml1, xml2 = run_refac()
    assert xml1 == xml2
