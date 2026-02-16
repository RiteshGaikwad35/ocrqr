import barcode
from barcode.writer import ImageWriter

barcode_data = "ritesh gaikwad"

writer_options = {
    "write_text": False,     
    "module_width": 0.2,     
    "module_height": 30.0,   
    "quiet_zone": 6.5,       
    "font_size": 0,         
    "text_distance": 0
}


code128 = barcode.get("code128", barcode_data, writer=ImageWriter())

code128.save("test_barcode", options=writer_options)

print("Clean barcode saved as test_barcode.png")
