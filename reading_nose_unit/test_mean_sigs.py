from mean_sightings import get_sightings

filename = 'sightings_tab_sm.csv'

def test_water_is_correct():
    watrec, watmean = get_sightings(filename,'Water')
    assert watrec==2, "Number of records for water is wrong"
    assert watmean==17, 'Mean for water is 17'

def test_clay_is_correct():
    clayrec, claymean = get_sightings(filename,'Clay')
    assert clayrec==2, "Number of records for clay is wrong"
    assert claymean==25.5, 'Mean for clay is 25.5'

def test_not_present():
    notrec, notmean = get_sightings(filename,'Not present')
    assert notrec==0, "Number of records for Not present is null"
    assert notmean==0, 'Mean for Not present is null'

