# In app/parser.py

import re
from . import rules

def process_lab_text(text: str):
    results = []
    lines = text.strip().split('\n')
    found_tests = set() # Keep track of tests we've already found

    
    for line in lines:
        
        for test_rule in rules.NORMAL_RANGES:
            canonical_name = test_rule["name"]
            
            
            if canonical_name in found_tests:
                continue

            
            for alias in test_rule["aliases"]:
                match = re.search(rf'^{re.escape(alias)}\b.*?\b(\d+\.?\d*)\b', line, re.IGNORECASE)
                
                if match:
                    try:
                        value_str = match.group(1)
                        value = float(value_str)
                        normal_range = test_rule["range"]
                        
                        flag = "NORMAL"
                        if value < normal_range["min"]:
                            flag = "LOW"
                        elif value > normal_range["max"]:
                            flag = "HIGH"

                        results.append({"name": canonical_name, "value": value, "flag": flag})
                        found_tests.add(canonical_name) # Mark this test as found
                        
                        
                        break
                    except (ValueError, IndexError):
                        continue
            
            
            if canonical_name in found_tests and any(res['name'] == canonical_name for res in results):
                break

    return results