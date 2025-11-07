# lachlan gaeth
# 7/11/25
# v1

dc_selected = "You have selected distance conversion. \n"
mass_selected = "You have selected mass conversion. \n"
time_selected = "You have selected time conversion. \n"
distance_error = "Please insert a distance greater than zero."
mass_error = "Please insert a mass larger than zero."
time_error = "Please inset a time over zero."
code_open_error = "Please insert one of the numbers above!\n"

keep_going = ""
while keep_going == "":
    try:
        code_open = int(input("Welcome to ultimate conversion, what tpye of conversion would you like to do? \n"
        "type number corrolating to desired conversion: \n"
        "1 = Distance conversion \n"
        "2 = Mass conversion \n"
        "3 = time conversion \n"
        "Enter your chosen conversion type below. \n"))
    
        if code_open == 1:
            print(dc_selected)
            metric_unit_beginning = int(input("What metric unit is your distance in? \n" \
            "type number corrolating to metric unit being used: \n" \
            "1 = mm \n" \
            "2 = cm \n" \
            "3 = m \n" \
            "4 = km \n" \
            "Enter chosen metric unit type below. \n"))
            if metric_unit_beginning == 1 :
                print("Your beginning metric unit is mm \n")
            elif metric_unit_beginning == 2 :
                print("Your beginning metric unit is cm \n")
            elif metric_unit_beginning == 3 :
                print("Your beginning metric unit is m \n")
            elif metric_unit_beginning == 2 :
                print("Your beginning metric unit is km \n")
            beginning_distance = float(input("please insert your distance below to be converted \n"))
            metric_unit_finish = int(input("What metric unit do you want to convert to? \n" \
            "type number corrolating to metric unit that you with to convert to \n" \
            "1 = mm \n" \
            "2 = cm \n" \
            "3 = m \n" \
            "4 = km \n" \
            "Enter chosen metric unit type below. \n"))
            if metric_unit_finish == 1 :
                print("The metric unit you want to convert to is mm \n")
            elif metric_unit_finish == 2 :
                print("The metric unit you want to convert to is cm \n")
            elif metric_unit_finish == 3 :
                print("The metric unit you want to convert to is m \n")
            elif metric_unit_finish == 4 :
                print("The metric unit you want to convert to is km \n")
            keep_going = "code stop"

            mm_mm = beginning_distance
            mm_cm = beginning_distance / 10
            mm_m = beginning_distance / 1000
            mm_km = beginning_distance / 1000000
            cm_mm = beginning_distance * 10
            cm_cm = beginning_distance
            cm_m = beginning_distance / 100
            cm_km = beginning_distance / 100000
            m_mm = beginning_distance * 1000
            m_cm = beginning_distance * 100
            m_m = beginning_distance
            m_km = beginning_distance / 1000
            km_mm = beginning_distance * 1000000
            km_cm = beginning_distance * 100000
            km_m = beginning_distance * 1000
            km_km = beginning_distance

            if metric_unit_beginning == 1 and metric_unit_finish == 1 :
                print(f"The conversion comes out to {mm_mm}mm")
            
            elif metric_unit_beginning == 1 and metric_unit_finish == 2 :
                print(f"The conversion comes out to {mm_cm}cm")
            
            elif metric_unit_beginning == 1 and metric_unit_finish == 3 :
                print(f"The conversion come out to {mm_m}m")
            
            elif metric_unit_beginning == 1 and metric_unit_finish == 4 :
                print(f"The conversion comes out to {mm_km}km")
            
            elif metric_unit_beginning == 2 and metric_unit_finish == 1 :
                print(f"The conversion comes out to {cm_mm}mm")
            
            elif metric_unit_beginning == 2 and metric_unit_finish == 2 :
                print(f"The conversion comes out to {cm_cm}cm")
            
            elif metric_unit_beginning == 2 and metric_unit_finish == 3 :
                print(f"The conversion comes out to {cm_m}m")
            
            elif metric_unit_beginning == 2 and metric_unit_finish == 4 :
                print(f"The conversion comes out to {cm_km}km")
            
            elif metric_unit_beginning == 3 and metric_unit_finish == 1 :
                print(f"The conversion comes out to {m_mm}mm")
            
            elif metric_unit_beginning == 3 and metric_unit_finish == 2 :
                print(f"The conversion comes out to {m_cm}cm")

            elif metric_unit_beginning == 3 and metric_unit_finish == 3 :
                print(f"The conversion comes out to {m_m}m")
            
            elif metric_unit_beginning == 3 and metric_unit_finish == 4 :
                print(f"The conversion comes out to {m_km}km")
            
            elif metric_unit_beginning == 4 and metric_unit_finish == 1 :
                print(f"The conversion comes out to {km_mm}mm")
            
            elif metric_unit_beginning == 4 and metric_unit_finish == 2 :
                print(f"The conversion comes out to {km_cm}cm")
            
            elif metric_unit_beginning == 4 and metric_unit_finish == 3 :
                print(f"The conversion comes out to {km_m}m")
            
            elif metric_unit_beginning == 4 and metric_unit_finish == 4 :
                print(f"The conversion comes out to {km_km}km")

                
        elif code_open == 2:
            print(mass_selected)
            keep_going = "code stop"

        elif code_open == 3:
            print(time_selected)
            keep_going = "code stop"
        
        else:
            print(code_open_error)
    
    except ValueError:
            print(f"{code_open_error},You must enter a number.")

    keep_going = input("Press <Enter> to do another calculation, or any other key to quit. Thanks! \n")