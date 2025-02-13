N’aurais-tu l’impression de réussir que si tu gravis régulièrement les échelons hiérarchiques ?import streamlit as st
import google.generativeai as genai

# Configure Gemini API with Streamlit Secrets
# This assumes you have the API keys stored in Streamlit secrets
# For example, in your Streamlit app's settings (Secrets section), you'd have:
# api_keys:
#   key1: "YOUR_API_KEY_1"
#   key2: "YOUR_API_KEY_2"
#   key3: "YOUR_API_KEY_3"
#   key4: "YOUR_API_KEY_4"
#   key5: "YOUR_API_KEY_5"


# List of 5 API keys
api_keys = [
    st.secrets["api_keys"]["key1"],
    st.secrets["api_keys"]["key2"],
    st.secrets["api_keys"]["key3"],
    st.secrets["api_keys"]["key4"],
    st.secrets["api_keys"]["key5"],
]

# Track the last used API key index
api_key_index = 0

# Function to set API key and configure the model in order
def configure_api_key():
    global api_key_index
    while api_key_index < len(api_keys):
        try:
            key = api_keys[api_key_index]  # Select the current API key
            genai.configure(api_key=key)
            model = genai.GenerativeModel('gemini-1.5-flash')  # Configure the model with the API key
            return model
        except Exception as e:
            st.error(f"Failed to configure API with key {key}: {e}")
            api_key_index += 1  # Move to the next API key
            continue
    # If all keys fail, show a message and return None
    st.error("Sorry, the service is temporarily unavailable. Please try again later.")
    return None  # If all keys fail

# Initialize the model using the first working API key
model = None

# Schein Career Anchors Test Questions
questions = [
    "Aimerais-tu être tellement expert dans ton métier que tout le monde te demande des conseils ?",
    "Rêves-tu d’une activité professionnelle où on te confierait des missions impossibles ou des challenges à relever ?",
    "Préfères-tu un poste stable même si tu n’as pas autant de liberté et d’indépendance que tu le souhaiterais ?",
    "Rêves-tu de devenir ton propre patron mais ne sais pas encore comment ?",
    "Les métiers où tu réussis le mieux sont-ils ceux où tu as l’impression d’aider les autres ?",
    "Ce que tu préfères, c'est résoudre un problème difficile ?",
    "L’idéal pour toi, est-ce de trouver un travail où tu puisses préserver ta vie personnelle et familiale ?",
    "Pour toi, réussir dans la vie, est-ce avoir la possibilité de progresser régulièrement pour devenir un spécialiste ?",
    "Préfères-tu les responsabilités de management à celles de spécialiste ?",
    "Rêves-tu d’un métier où tu es libre d’organiser ton travail comme tu veux, sans avoir à compter tes heures au bureau ?",
    "Pour toi, est-ce que le plus important est de travailler dans une entreprise stable et sécurisante ?",
    "Ton objectif principal dans la vie est-il de créer quelque chose par toi-même, où tu es le maître d’œuvre ?",
    "Refuserais-tu une promotion si elle t’empêchait de servir les autres ?",
    "Es-tu pleinement heureux lorsque tu réussis quelque chose qui t’a demandé un gros effort ?",
    "Le plus important pour toi, est-ce ta famille et tes loisirs ? Refuses-tu les responsabilités qui te demandent une trop grande disponibilité ?",
    "Préfères-tu te spécialiser dans ton métier plutôt que de t’éloigner du terrain pour accéder à plus de responsabilités ?",
    "N’aimes-tu pas les métiers trop rigides, où il y a peu de liberté ?",
    "Cherches-tu un travail où tu es constamment en compétition avec d'autres ?",
    "Préfèrerais-tu être à ton compte plutôt que travailler comme salarié ?",
    "Es-tu prêt à sacrifier une partie de ta liberté pour un emploi stable et sécurisé ?",
    "Est-ce que tu aurais l’impression de réussir uniquement si tu montes régulièrement dans la hiérarchie ?",
    "Préfères-tu garder ton indépendance dans ton travail, même si cela signifie progresser moins vite dans l’entreprise ?",
    "Rêves-tu d’un métier qui te permette de contribuer réellement à améliorer le monde et l’entreprise ?",
    "Es-tu prêt à sacrifier une promotion pour préserver ton équilibre entre vie professionnelle et vie personnelle ?"
]


# New page content
def new_page():

    st.image(r"Logo.png")
    st.markdown("""
       ### 📊  Découvrez vos Ancres de Carrière avec IFCAR Solutions
       Chez **IFCAR Solutions**, nous comprenons l'importance de connaître vos motivations profondes et vos valeurs professionnelles. C'est pourquoi nous vous proposons un **test d'ancres de carrière gratuit**, conçu pour être **intuitif**, **rapide**, et **perspicace**.

       ### 🚀 Pourquoi faire notre test ?

       - **Comprenez vos priorités** : Identifiez les éléments essentiels à votre épanouissement professionnel.
       - **Alignez vos choix de carrière** : Prenez des décisions plus éclairées en fonction de vos ancres.
       - **Développez votre potentiel** : Optimisez votre parcours en accord avec vos valeurs fondamentales.

       ### 🎯 Pourquoi choisir IFCAR Solutions ?

       Forts de **12 ans d'expérience dans le recrutement**, nous aidons les individus à trouver des carrières qui leur correspondent vraiment. Notre test d'ancres de carrière témoigne de notre engagement à fournir des outils pertinents et efficaces pour une orientation professionnelle réussie.

       📌 **Passez notre test d'ancres de carrière dès aujourd'hui** et prenez le contrôle de votre avenir professionnel !
       """)

    # Add buttons linking to external resources
    st.markdown("---")  # Add a separator
    st.markdown("##### Ressources Utiles:")

    col1, col2, col3, col4 = st.columns(4)  # Create three columns

    with col1:
        st.link_button("Nos offres d'emploi", "https://ifcarjob.com/offres-demploi")

    with col2:
        st.link_button("Analyser vos CV", "https://cvanalyserapp.streamlit.app/")

    with col3:
        st.link_button("Déposez vos CV", "mailto:cv@ifcarjob.com")

    with col4:
        st.link_button("Notre page Linkedin", "https://www.linkedin.com/company/ifcarsolutions/")


# Main application
def main():
    st.sidebar.title("Pages")
    page = st.sidebar.radio("Aller à", ["Test d'orientation des carrières", "À propos de nous"])

    if page == "Test d'orientation des carrières":
        career_anchors_page()
    elif page == "À propos de nous":
        new_page()

def career_anchors_page():
    global model  # Declare that you're using the global model variable
    st.image(r"Logo.png")

    st.title("Test d'orientation des carrières")
    st.markdown("Pour chacune des 24 questions, donnez une note allant de 1 à 5 par rapport à ce qui vous semble être vrai pour vous. Plus le chiffre sera élevé, plus la phrase correspondra à ce que vous ressentez.")

    # Initialize session state
    if 'responses' not in st.session_state:
        st.session_state['responses'] = {}

    # Collect user information
    name = st.text_input("Nom et Prénom *")

    if not name:
        st.warning("Veuillez remplir le champ du nom.")
        return

    # Collect responses
    for i, question in enumerate(questions):
        key = f"Q{i+1}"
        st.markdown(f"### {i+1}. {question}")  # Make questions bigger
        

        # Implement the radio buttons for 1 to 5 scale
        st.session_state['responses'][key] = st.radio(
            "Sélectionnez votre réponse:",
            options=['Pas du tout vrai', 'Pas vraiment', 'Neutre', 'En partie vrai', 'Tout à fait vrai'],
            index=None,  # Default to the middle (3)
            horizontal=True,  # Ensures all options appear on the same line
            key=key
        )

    if st.button("Soumettre les réponses"):
        # Prepare the prompt for Gemini
        prompt = f"Analysez les réponses suivantes au test des ancres de carrière de Schein pour Moi, qui s'appelle {name} :\n\n"
        for q, response in st.session_state['responses'].items():
            prompt += f"{q}: {response}\n"

        prompt += "\nIdentifiez les top trois ancres de carrière dominantes pour {name} et estimez le pourcentage d'importance de chaque ancre dans le profil de {name}.\n"
        prompt += "Présentez les résultats sous forme de liste, où chaque élément indique l'ancre et son pourcentage d'importance (par exemple: Autonomie: 60%).\n"
        prompt += "Ne mentionnez pas les numéros de questions spécifiques dans votre analyse.\n"
        prompt += "Après la liste des pourcentages, fournissez pour les trois ancre dominante une explication en deux lignes maximum.\n"
        prompt += "Ensuite, proposez trois pistes de développement professionnel sous forme de liste à puces, adaptées à ces ancres."
        prompt += "Limitez votre réponse à 200 mots."



        # Send to Gemini API
        try:
            # Configure the model if it's not already configured (or has failed)
            if model is None:
                model = configure_api_key()

            if model is not None:  # only proceed if the model is configured
                response = model.generate_content(prompt)
                st.subheader("Résultats de l'analyse")
                st.write(response.text)
            else:
                st.error("Failed to configure the Gemini API after trying all available keys. Please check your secrets or try again later.")
        except Exception as e:
            st.error(f"Une erreur s'est produite lors de l'analyse: {e}")
            model = None  # Reset the model if there's an error, so it tries to reconfigure next time

        st.markdown("---")  # Add a separator
        st.markdown("##### Ressources Utiles:")

        col1, col2, col3, col4 = st.columns(4)  # Create three columns

        with col1:
            st.link_button("Nos offres d'emploi", "https://ifcarjob.com/offres-demploi")

        with col2:
            st.link_button("Analyser vos CV", "https://cvanalyserapp.streamlit.app/")

        with col3:
            st.link_button("Déposez vos CV", "mailto:cv@ifcarjob.com")

        with col4:
            st.link_button("Notre page Linkedin", "https://www.linkedin.com/company/ifcarsolutions/")





if __name__ == "__main__":
    main()
