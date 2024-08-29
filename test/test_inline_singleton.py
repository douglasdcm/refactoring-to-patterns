from src.inline_singleton import BlackjackRefac, HitStayResponseRefac


def test_refac():
    input = "H"
    bj = BlackjackRefac()
    hs = HitStayResponseRefac()
    bj.set_player_response(hs)
    bj.play()
    actual = bj.obtain_hit_stay_response(input)
    assert actual.should_hit() is True
