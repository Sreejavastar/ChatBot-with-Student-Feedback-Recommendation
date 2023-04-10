import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_ADVICE0 = "Sure! How can I help you?"
R_ADVICE1 = "The chatbot can evaluate the quality and relevance of the sources used in your assignment, as well as how well you integrate them into your argument. The chatbot may suggest additional sources that could strengthen your argument or provide feedback on how you can better incorporate sources to support your points."
R_ADVICE2 = "The chatbot can provide feedback on the clarity of your writing by identifying areas where your sentences may be too long or complex, or where you may be using ambiguous or confusing language. The chatbot can suggest revisions or provide specific examples to help you improve the clarity of your writing."
R_ADVICE3 = "The chatbot can identify areas of weakness in your writing and provide specific feedback on how to improve those areas. For example, the chatbot may identify that you need to work on improving your grammar, or that you need to focus on improving the coherence of your argument."
R_ADVICE4 = "The chatbot may suggest resources such as writing guides or online writing courses that can help you improve your writing skills. The chatbot may also recommend specific tools or software that can help you identify and correct errors in your writing."
R_ADVICE5 = "The chatbot can identify common errors or patterns in your writing, such as grammatical errors or inconsistencies in your argument. The chatbot can provide feedback on these errors and suggest strategies for avoiding them in the future!"
R_ADVICE6 = "The chatbot can provide feedback on the structure and organization of your assignment by identifying areas where the flow of ideas may be unclear or where the structure could be improved. The chatbot may suggest revisions or provide specific examples to help you improve the overall structure and organization of your assignment."
R_ADVICE7 = "The chatbot can provide feedback on the strength of your argument by identifying areas where additional evidence or analysis may be needed to support your claims. The chatbot can suggest revisions or provide specific examples to help you make your argument stronger."
R_ADVICE8 = "The chatbot can provide feedback on the use of transitions in your writing by identifying areas where the flow of ideas may be disrupted or where transitions could be improved. The chatbot may suggest revisions or provide specific examples to help you improve your use of transitions between paragraphs and ideas."
R_ADVICE9 = "I don't have access to the specific answers to your individual assignment. However, I can provide some general guidance that may be helpful. You can also Google it using this link:https://www.google.com/"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return