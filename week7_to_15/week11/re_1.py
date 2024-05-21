class ClassificationReport:
    def __init__(self, num_class):
        self.num_class = num_class

    def confusion_matrix(self, pred, target): # pred는 예측값, target은 실제값
        matrix = [{'TP': 0, 'FP': 0, 'FN': 0, 'TN': 0} for _ in range(self.num_class)]

        for p, t in zip(pred, target):
            if p == t:
                matrix[t]['TP'] += 1
                for i in range(self.num_class):
                    if i != t:
                        matrix[i]['TN'] += 1
            else:
                matrix[t]['FN'] += 1
                matrix[p]['FP'] += 1
        return matrix

    def precision(self, TP, FP):
        if TP + FP == 0:
            return 0
        return TP / (TP + FP)
    
    def recall(self, TP, FN):
        if TP + FN == 0:
            return 0
        return TP / (TP + FN)
    
    def f_measure(self, precision, recall):
        if precision + recall == 0:
            return 0
        return 2 * (precision * recall) / (precision + recall)
    
    def support(self, target, class_label):
        count = 0
        for t in target:
            if t == class_label:
                count += 1
        return count
            

    def multiclass_evaluation(self, pred, target):
        f_measure_, precision_, recall_ = [], [], []

        cnfs_mat = self.confusion_matrix(pred, target)
        for i in range(self.num_class):
            TP = cnfs_mat[i]['TP']
            FP = cnfs_mat[i]['FP']
            FN = cnfs_mat[i]['FN']
            precision_.append(self.precision(TP, FP))
            recall_.append(self.recall(TP, FN))
            f_measure_.append(self.f_measure(precision_[i], recall_[i]))
        accuracy_ = sum([cnfs_mat[i]['TP'] for i in range(self.num_class)]) / len(pred)
        support_ = [self.support(target, i) for i in range(self.num_class)]
        return accuracy_, precision_, recall_, f_measure_, support_


cr = ClassificationReport(4)
pred = [0, 1, 2, 3, 0, 1, 2, 3]
target = [0, 1, 2, 3, 1, 2, 3, 0] 

print(cr.confusion_matrix(pred, target))