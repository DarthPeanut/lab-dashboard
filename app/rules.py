# In app/rules.py

# A more robust list of dictionaries, where each dictionary contains a
# canonical name for a test, a list of possible aliases found in reports,
# and the normal range.
NORMAL_RANGES = [
    {
        "name": "Hemoglobin",
        "aliases": ["Hemoglobin", "HGB", "Haemoglobin"],
        "range": {"min": 13.5, "max": 17.5}
    },
    {
        "name": "White Blood Cell Count",
        "aliases": ["Total Leucocyte Count", "WBC", "White Blood Cell Count"],
        "range": {"min": 4.0, "max": 11.0} 
    },
    {
        "name": "Red Blood Cell Count",
        "aliases": ["RBC Count", "RBC"],
        "range": {"min": 4.5, "max": 5.9}
    },
    {
        "name": "Platelet Count",
        "aliases": ["Platelet Count", "PLT"],
        "range": {"min": 150000, "max": 450000}
    },
    {
        "name": "Hematocrit",
        "aliases": ["Hct", "Hematocrit"],
        "range": {"min": 40, "max": 52}
    },
    {
        "name": "MCV",
        "aliases": ["MCV"],
        "range": {"min": 80, "max": 100}
    },
    {
        "name": "MCH",
        "aliases": ["MCH"],
        "range": {"min": 27, "max": 34}
    },
    {
        "name": "MCHC",
        "aliases": ["MCHC"],
        "range": {"min": 31.5, "max": 36}
    },
    {
        "name": "Neutrophils",
        "aliases": ["Neutrophils", "NEU%"],
        "range": {"min": 40, "max": 80}
    },
    {
        "name": "Lymphocytes",
        "aliases": ["Lymphocytes", "LYM%"],
        "range": {"min": 20, "max": 40}
    },
    # Add other tests here in the same format...
]