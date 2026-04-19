def f1_micro(y_true, y_pred) -> float:
    correct = 0
    
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            correct += 1
    
    total = len(y_true)
    
    TP = correct
    FP = total - correct
    FN = total - correct
    
    return (2 * TP) / (2 * TP + FP + FN)