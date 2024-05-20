```py
def confusion_matrix(self, pred, target):
        cnfs_mat = [{'TP': 0, 'FP': 0, 'FN': 0, 'TN': 0} for _ in range(self.num_class)]
        # TP is True Positive, FP is False Positive, FN is False Negative, TN is True Negative
        
        for class_idx in range(self.num_class): # num_class is the number of classes
            for idx in range(len(target)):
                print(target[idx], pred[idx])
                true_val = int(target[idx]) if isinstance(target, pd.Series) else target[idx]
                pred_val = int(pred[idx]) if isinstance(pred, pd.Series) else pred[idx]

                if pred_val[idx] == class_idx and true_val[idx] == class_idx:
                    cnfs_mat[class_idx]['TP'] += 1
                elif pred_val[idx] == class_idx and true_val[idx] != class_idx:
                    cnfs_mat[class_idx]['FP'] += 1
                elif pred_val[idx] != class_idx and true_val[idx] == class_idx:
                    cnfs_mat[class_idx]['FN'] += 1
                else:
                    cnfs_mat[class_idx]['TN'] += 1

        return cnfs_mat


```


```py
   def multiclass_evaluation(self, pred, target):
        f_measure_, precision_, recall_ = [], [], []

        cnfs_mat = self.confusion_matrix(pred, target)
        for class_idx in range(self.num_class):
            TP = cnfs_mat[class_idx]['TP']
            FP = cnfs_mat[class_idx]['FP']
            FN = cnfs_mat[class_idx]['FN']
            TN = cnfs_mat[class_idx]['TN']

            prc = self.precision(TP, FP, FN, TN)
            rc = self.recall(TP, FP, FN, TN)
            fm = self.f_measure(prc, rc)

            precision_.append(prc)
            recall_.append(rc)
            f_measure_.append(fm)

            print(f'class {class_idx} precision: {prc} recall:{rc} f_measure:{fm}')
```