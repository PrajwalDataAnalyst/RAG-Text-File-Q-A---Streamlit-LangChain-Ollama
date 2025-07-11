def get_top_result(vectorstore, query: str):
    results = vectorstore.similarity_search(query)
    return results[0].page_content if results else "No relevant content found."
