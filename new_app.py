import streamlit as st
import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors, AllChem
import pickle
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

def llm_explanation(smiles,pic50,descriptors):
    prompt = f"""
    The molecule with SMILES: {smiles} has the predicted pIC50 value of {pic50:.2f}.

    In not less than 300 words, explain this prediction as an expert in Medicinal Chemistry and 
    also explain what implication the predicted value might have with respect to drug discovery and development.

    Also, briefly describe what the following molecular descriptor indicate about the compounds and 
    whether the molecular descriptor obey the Lipinski Rule of 5:
    
    - Molecular Weight: {descriptors['MW']}
    - LogP: {descriptors['LogP']}
    - HBD (Hydrogen Bond Donors): {descriptors['HBD']}
    - HBA (Hydrogen Bond Acceptors) : {descriptors['HBA']}
    - Rotatable Bonds: {descriptors['RotBonds']}
    """
    
    try:
        chat = ChatGroq(
            groq_api_key="Replace with your groq api key here",
            model_name="Gemma2-9b-It"
        )
        response = chat([HumanMessage(content=prompt)])
        return response.content
    
    except Exception as e:
        return f"LLM Explanation failed: {e}"

def load_model():
    with open("shp3_model_2.pkl","rb") as f:
        return pickle.load(f)
    
def calculate_features(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        descriptors = {
            "MW": Descriptors.ExactMolWt(mol),
            "HBD": Descriptors.NumHDonors(mol),
            "HBA": Descriptors.NumHAcceptors(mol),
            "TPSA": Descriptors.TPSA(mol),
            "LogP": Descriptors.MolLogP(mol),
            "RotBonds": Descriptors.NumRotatableBonds(mol)
        }

        fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, 1024)
        fingerprint_bits = list(fp.ToBitString())
        fingerprint_features = {f'bit_{i}': int(b) for i, b in enumerate(fingerprint_bits)}

        return {**descriptors, **fingerprint_features}
    return None

def main():
    st.title(" Src Tyrosine Phosphatase Protein (SHP2) Inhibitor Activity Predictor with Natural Language")

    smiles_input = st.text_area("Enter SMILES string:", height=100)

    if st.button("Predict"):
        if smiles_input:
            try:
                # Calculate molecular features
                features = calculate_features(smiles_input)

                if features:
                    # Load model components
                    model_components = load_model()
                    df = pd.DataFrame([features])
                    df = df[model_components['feature_names']]

                    # Scale features and make prediction
                    scaled_features = model_components['scaler'].transform(df)
                    prediction = model_components['randomized_rf'].predict(scaled_features)[0]

                    st.success(f"✅ Predicted pIC50: {prediction:.2f}")

                    # Display molecular descriptors
                    st.subheader("🔬 Molecular Descriptors")
                    descriptors_df = pd.DataFrame({k: [v] for k, v in features.items() if not k.startswith('bit_')})
                    st.write(descriptors_df)

                    st.subheader("Explanation of the results")
                    explanation = llm_explanation(
                        smiles=smiles_input,
                        pic50=prediction,
                        descriptors={k : features[k] for k in ['MW', 'LogP', 'HBD', 'HBA', 'TPSA','RotBonds']}
                    )
                    st.write(explanation)

                else:
                    st.error("Invalid SMILES string")
            except Exception as e:
                st.error(f"An error occured: {str(e)}")
        else:
            st.warning("Please enter a SMILES string")

if __name__ == "__main__":
    main()