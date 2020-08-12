import pytest


@pytest.fixture()
def daily_forecast_for_7_days_sample():
    return {
        "lat":33.44,
        "lon":-94.04,
        "timezone":"America/Chicago",
        "timezone_offset":-18000,
        "daily":[
            {"dt":1597255200,"sunrise":1597232217,"sunset":1597280726,"temp":{"day":302.32,"min":294.08,"max":306.6,"night":297.53,"eve":304.8,"morn":294.08},"feels_like":{"day":307.03,"night":301.59,"eve":310.08,"morn":297.28},"pressure":1016,"humidity":72,"dew_point":296.75,"wind_speed":1.24,"wind_deg":160,"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":82,"pop":1,"rain":7.02,"uvi":10.35},
            {"dt":1597341600,"sunrise":1597318660,"sunset":1597367063,"temp":{"day":307.63,"min":296.26,"max":309.77,"night":300.5,"eve":306.76,"morn":296.26},"feels_like":{"day":310.87,"night":302.67,"eve":310.61,"morn":299.77},"pressure":1013,"humidity":51,"dew_point":296.16,"wind_speed":2.75,"wind_deg":230,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":0,"pop":0.21,"uvi":10.31},
            {"dt":1597428000,"sunrise":1597405102,"sunset":1597453399,"temp":{"day":305.5,"min":297.07,"max":308.76,"night":300.34,"eve":306.11,"morn":297.07},"feels_like":{"day":307.65,"night":302.16,"eve":310.2,"morn":299.66},"pressure":1011,"humidity":58,"dew_point":296.44,"wind_speed":4.43,"wind_deg":180,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":34,"pop":0.8,"rain":0.26,"uvi":9.84},
            {"dt":1597514400,"sunrise":1597491545,"sunset":1597539734,"temp":{"day":308.09,"min":296.95,"max":309.09,"night":299.37,"eve":306.37,"morn":296.95},"feels_like":{"day":312.44,"night":302.2,"eve":311.36,"morn":299.92},"pressure":1012,"humidity":50,"dew_point":296.19,"wind_speed":1.23,"wind_deg":107,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":0,"pop":0.07,"uvi":9.59},
            {"dt":1597600800,"sunrise":1597577988,"sunset":1597626067,"temp":{"day":310.06,"min":297.14,"max":310.21,"night":300.19,"eve":307.73,"morn":297.14},"feels_like":{"day":314.9,"night":302.37,"eve":312.31,"morn":301.15},"pressure":1014,"humidity":45,"dew_point":296.2,"wind_speed":0.57,"wind_deg":141,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":10,"pop":0.33,"rain":0.23,"uvi":9.29},
            {"dt":1597687200,"sunrise":1597664430,"sunset":1597712400,"temp":{"day":298.73,"min":294.99,"max":303.56,"night":294.99,"eve":300.77,"morn":296.35},"feels_like":{"day":301.81,"night":296.09,"eve":302.06,"morn":297.1},"pressure":1017,"humidity":78,"dew_point":294.7,"wind_speed":1.91,"wind_deg":29,"weather":[{"id":502,"main":"Rain","description":"heavy intensity rain","icon":"10d"}],"clouds":100,"pop":1,"rain":15.6,"uvi":9.81},
            {"dt":1597773600,"sunrise":1597750872,"sunset":1597798732,"temp":{"day":303.55,"min":292.35,"max":305.61,"night":295.28,"eve":302.3,"morn":292.35},"feels_like":{"day":304.38,"night":295.49,"eve":303.87,"morn":293.49},"pressure":1016,"humidity":45,"dew_point":290.44,"wind_speed":2.28,"wind_deg":56,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":16,"pop":0,"uvi":9.38},
            {"dt":1597860000,"sunrise":1597837315,"sunset":1597885063,"temp":{"day":305.01,"min":293.7,"max":305.46,"night":296.1,"eve":302.89,"morn":293.7},"feels_like":{"day":307.03,"night":296.45,"eve":304.78,"morn":295.26},"pressure":1014,"humidity":46,"dew_point":292.26,"wind_speed":1.59,"wind_deg":132,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":29,"pop":0,"uvi":8.87}
        ]
    }
