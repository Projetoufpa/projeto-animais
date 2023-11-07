import folium

animais_nomes = ["cavalo","iguana","aranha"]

animais_coordendas = [[-1.474940, -48.457060],[-1.474103, -48.453316],[-1.475401, -48.457232]]

animais_mapa = folium.map(location = [ -1.475262, -48.456728], zoom_start =  5 , control_scales = true)
folium.tilelayer("cartodbpositron").add_to(animais_mapa)

animais_mapa