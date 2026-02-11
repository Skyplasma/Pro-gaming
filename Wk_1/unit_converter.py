metre = float(input("distance in metres? "))
kilometre = metre / 1000
inches = metre / 0.0254
if metre > float(0):
    print(f"metres 2dp:{round(metre,2)}")
    print(f"Km 2dp:{round(kilometre,2)}")
    print(f"Inches 2dp:{round(inches,2)}")

else:
    print("Negative Input, Exiting Program.")
