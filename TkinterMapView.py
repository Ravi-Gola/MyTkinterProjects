import tkinter
from tkintermapview import TkinterMapView

"""create tkinter window"""
root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("map_view_example.py")

"""create map widget:"""
map_widget = TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

"""we set zoom ranges from 0 to 19(highest zoom level):"""
map_widget.set_zoom(15)

"""we set the position by using two method first through position(in digit) and through address shown below and also we add red marker by passing 
argument marker=True"""
# map_widget.set_position(48.860381, 2.338594,marker=True)  # Paris, France
# var=map_widget.set_address("Mathura, Uttar Pradesh, india",marker=True)
# print(var.position,var.text) # we use position and text func for get position and text of any address

"""another method of set a position marker by using text :"""
# marker_2 = map_widget.set_marker(52.516268, 13.377695, text="Brandenburger Tor")
# marker_3 = map_widget.set_marker(52.55, 13.4, text="52.55, 13.4")
# marker_4 = map_widget.set_marker(52.60, 13.41 ,text="52.60,13.41")
# marker_5 = map_widget.set_marker(52.65, 13.42 ,text="52.65,13.42")

""" we can add two or more than two paths together by using set_path:"""
# path_1 = map_widget.set_path([marker_2.position, marker_3.position,marker_4.position])
# path_1.add_position(marker_4.position, marker_5.position)
# path_1.delete()

"""we can change text by using set_text func:"""
# marker_2.set_text("Colosseo in Rome")  # set new text

"""we can delete the marker by using delete:"""
# marker_2.delete()

"""tile servers"""
# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google satellite
# map_widget.set_tile_server("http://c.tile.stamen.com/watercolor/{z}/{x}/{y}.png")  # painting style
# map_widget.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png")  # black and white
# map_widget.set_tile_server("https://tiles.wmflabs.org/hikebike/{z}/{x}/{y}.png")  # detailed hiking
# map_widget.set_tile_server("https://tiles.wmflabs.org/osm-no-labels/{z}/{x}/{y}.png")  # no labels

"""overlay tile server"""
# map_widget.set_overlay_tile_server("http://tiles.openseamap.org/seamark//{z}/{x}/{y}.png")  # sea-map overlay
# map_widget.set_overlay_tile_server("http://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png")  # railway infrastructure

root_tk.mainloop()