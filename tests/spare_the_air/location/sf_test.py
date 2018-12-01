def test_get_burn_status(mock_requests):
    from spare_the_air.location.sf import get_burn_status

    text = get_burn_status()

    assert(
        text.startswith('It\'s OK to burn') or
        text.startswith('It\'s not legal to burn')
    )
