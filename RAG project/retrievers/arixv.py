from langchain_community.retrievers import ArxivRetriever

#create the retriever
retrivers=ArxivRetriever(
    load_max_docs=2, # numbers of papers to retrieve
    load_all_available_meta=True
)

#query arxiv
docs=retrivers.invoke("large language model")

#print result

for i, doc in enumerate(docs):
    print(f"\nResult{i+1}")
    print("title:",doc.metadata.get("Title"))
    print("Authors:",doc.metadata.get("Authors"))
    print("Summary:",doc.page_content[:500])

    