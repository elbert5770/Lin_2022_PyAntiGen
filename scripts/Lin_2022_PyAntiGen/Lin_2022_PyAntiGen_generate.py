"""
Example model builder. Outputs go to antimony_models/Example/ and generated/Example/.
"""
import os
import sys

# Use location: import Model_* from the same folder as this script (model folder)
_project_dir = os.path.dirname(os.path.abspath(__file__))
if _project_dir not in sys.path:
    sys.path.insert(0, _project_dir)
MODEL_NAME = os.path.basename(_project_dir)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from framework.pyantigen import PyAntiGen
from modules.Abeta.APP_reactions_Lin2022 import APP_reactions_Lin2022_Module
from modules.Abeta.Abeta_aggregation_Lin2022 import Abeta_aggregation_Lin2022_Module
from modules.Tissue_Flows.cns_flows_Lin2022_modular import CNS_flows_Lin2022_Module
from modules.Antibody.Antibody_PK_Lin2022_modular import Antibody_PK_Lin2022_Module
from modules.Abeta.Abeta_antibody_binding_Lin2022_modular import Abeta_antibody_binding_Lin2022_Module
from modules.Abeta.Abeta_ADCP_clearance_Lin2022 import Abeta_ADCP_clearance_Lin2022_Module

if __name__ == "__main__":
    Isotopes = ['']
    model = PyAntiGen(name=MODEL_NAME, isotopes=Isotopes)

    SpeciesList_Abeta_peptides = ['AB42']
    No_Isotope_SpeciesList = ['Antibody', 'FcR']

    Antibody_PK_Lin2022_Module(model, Species='Antibody', No_Isotope_SpeciesList=No_Isotope_SpeciesList)

    for Species in SpeciesList_Abeta_peptides:
        APP_reactions_Lin2022_Module(model, Species=Species, No_Isotope_SpeciesList=No_Isotope_SpeciesList)
        Abeta_aggregation_Lin2022_Module(model, Species=Species, No_Isotope_SpeciesList=No_Isotope_SpeciesList)
        CNS_flows_Lin2022_Module(model, Species=Species, No_Isotope_SpeciesList=No_Isotope_SpeciesList)
        Abeta_antibody_binding_Lin2022_Module(model, Species=Species, No_Isotope_SpeciesList=No_Isotope_SpeciesList)
        Abeta_ADCP_clearance_Lin2022_Module(model, Species=Species, No_Isotope_SpeciesList=No_Isotope_SpeciesList)


    print(f"Reactions generated: {model.counter}")
    print(f"Rules generated: {len(model.rules)}")
    model.generate(__file__)
    print("\nModel generated successfully.")
    print("Next steps:")
    print(f"  1. Optionally edit parameters in antimony_models/{MODEL_NAME}/{MODEL_NAME}_parameters.csv")
    print(f"  2. From scripts/{MODEL_NAME}/, run: python {MODEL_NAME}_run.py")
