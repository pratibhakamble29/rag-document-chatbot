
def retrieve_answer(vectorstore, question):

    docs = vectorstore.similarity_search(
        question,
        k=1
    )

    if docs:
        return docs[0].page_content

    return "No relevant information found."