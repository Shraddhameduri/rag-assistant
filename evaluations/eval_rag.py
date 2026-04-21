from langchain.evaluation import load_evaluator

def evaluate(answer, reference):
    evaluator = load_evaluator("qa")
    return evaluator.evaluate_strings(
        prediction=answer,
        reference=reference
    )