from langgraph.graph import StateGraph, END

def analyze(state):
    state["use_rag"] = True
    return state

def retrieve(state, retriever):
    state["docs"] = retriever.get_relevant_documents(state["query"])
    return state

def generate(state, chain):
    result = chain({"query": state["query"]})
    state["answer"] = result["result"]
    return state

def build_graph(retriever, chain):
    graph = StateGraph(dict)

    graph.add_node("analyze", analyze)
    graph.add_node("retrieve", lambda s: retrieve(s, retriever))
    graph.add_node("generate", lambda s: generate(s, chain))

    graph.set_entry_point("analyze")
    graph.add_edge("analyze", "retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", END)

    return graph.compile()