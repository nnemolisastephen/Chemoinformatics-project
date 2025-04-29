## Src Tyrosine Phosphatase Protein (SHP2) Inhibitor Activity Predictor with Natural Language
<img align="center" src="images/shp2-visual.png" width="1000">
  
  SHP2 is a hot therapeutic target. SHP2 is a 68kDa protein with 593 amino acids that plays an important role in cell growth, 
  proliferation and differentiation, migration, and death. Its extensive role in RAS-MAPK and associated signaling pathways makes 
  SHP2 a critical target in the treatment of cancers associated with different RAS oncogenes. Finding high-efficacy inhibitors has been the goal of drug discovery.
  In this project, I leveraged machine learning and a large language model to develop an application that can predict the activity of a compound against 
  SHP2 while also explaining to the user whether the compound meets the Lipinski rule of five.

## 📌 Features
**You must have your canonical smile for the application to make prediction.**
A canonical SMILES string is a unique, unambiguous representation of a chemical structure within the SMILES format. Example: CC1(CCN(CC1)C2=CN=C(C(=N2)N)C3=C(C(=CC=C3)Cl)Cl)N
One of the popular database to get a canonical smile for your compound is [www.pubchem.com](https://pubchem.ncbi.nlm.nih.gov/). 

## 📦 Tech Stack
| Category        |     Technologies Used |
|------------------|-----------------|
| **Frontend**     | Streamlit  |
| **Backend**      | Python  |
| **AI Model**     | Groq Llama-3 70B |
| **Environment Management** | dotenv |

## Model Training
The residual plot shows that our model can perform well on unseen data
<img width="377" alt="image" src="https://github.com/user-attachments/assets/b8412922-52d2-4a28-b1c4-282c0c593a05" />


## 🚀 Installation of Dependencies and Setup

### 1️⃣ Cloning the Repo/ Installation
```sh
git clone https://github.com/nnemolisastephen/Chemoinformatics-project
cd Chemoinformatics-project
pip install -r requirements.txt
```
### 2️⃣ Run the Application
```sh
streamlit run app.py
```
## 🤝 Contribution
You can open an issue or fork the repo. Pull requests are welcome!

## 📞 Contact
Feel free to reach out [Nnemolisa Stephen](https://github.com/nnemolisastephen) if you have any question.
