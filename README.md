## Src Tyrosine Phosphatase Protein (SHP2) Inhibitor Activity Predictor with Natural Language
## 📍Introduction
<p align="left">
  <img src="https://github.com/user-attachments/assets/b973cbc4-c710-4289-82c3-e7be462ab038" alt="SHP2 project image" width="250" align="right">
  SHP2 is a hot therapeutic target. SHP2 is a 68kDa protein with 593 amino acids that plays an important role in cell growth, 
  proliferation and differentiation, migration, and death. Its extensive role in RAS-MAPK and associated signaling pathways makes 
  SHP2 a critical target in the treatment of cancers associated with different RAS oncogenes. Finding high-efficacy inhibitors has been the goal of drug discovery.
  In this project, I leveraged machine learning and a large language model to develop an application that can predict the activity of a compound against 
  SHP2 while also explaining to the user whether the compound meets the Lipinski rule of five.
</p>

## 📌 Features
**This application requires that you have your canonical smile to make prediction.**

A canonical SMILES string is a unique, unambiguous representation of a chemical structure within the SMILES format. 
Example: CC1(CCN(CC1)C2=CN=C(C(=N2)N)C3=C(C(=CC=C3)Cl)Cl)N
One of the popular database to get a canonical smile for your compound is [www.pubchem.com](https://pubchem.ncbi.nlm.nih.gov/). 

## 📦 Tech Stack
| Category        |     Technologies Used |
|------------------|-----------------|
| **Frontend**     | Streamlit  |
| **Backend**      | Python  |
| **AI Model**     | Gemma2-9b-It |
| **Environment Management** | dotenv |
| **RDkit** | Chemoinformatics library |

## 🧠Model Training
The residual plot shows that our model can perform well on unseen data

<img width="377" alt="image" src="https://github.com/user-attachments/assets/b8412922-52d2-4a28-b1c4-282c0c593a05" />


## 🚀 Installation of Dependencies and Setup

### 1️⃣ Cloning the Repo/ Installation
```sh
git clone https://github.com/nnemolisastephen/Chemoinformatics-project
cd Chemoinformatics-project
```
### 2️⃣ Run the Application
```sh
streamlit run new_app.py
```
## 🤝 Contribution
You can open an issue or fork the repo. Pull requests are welcome!

## 📞 Contact
Feel free to reach out [Nnemolisa Stephen](https://github.com/nnemolisastephen) if you have any question.
