from . import rules

def process_lab_text(text: str):
    results = []
    lines = text.strip().split('\n')

    
    for line in lines:
       
        try:
            # Split the line into a name and a value.
            name, value_str = line.split(':')

            
            name = name.strip()
            value = float(value_str.strip())

            
            normal_range = rules.NORMAL_RANGES.get(name)
            flag = "NORMAL" # Assume it's normal unless proven otherwise.

           
            if normal_range:
                if value < normal_range["min"]:
                    flag = "LOW"
                elif value > normal_range["max"]:
                    flag = "HIGH"

            
            results.append({"name": name, "value": value, "flag": flag})

        except ValueError:
            continue

    return results