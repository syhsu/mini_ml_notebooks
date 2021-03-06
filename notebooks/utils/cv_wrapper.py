from sklearn.model_selection import LeaveOneGroupOut, KFold


class LeaveOneGroupOutKFold_CVWrapper:
    """A wrapper for nested cross validation using LeaveOneGroupOut & KFold"""

    def __init__(self, outer_cv: LeaveOneGroupOut, inner_cv: KFold):
        self.outer_cv = outer_cv
        self.inner_cv = inner_cv
        self.nested_scores = {}
        self.nested_models = {}

    def run(self, model, X, y, groups, save_model=False):
        for inx, (train_index, test_index) in enumerate(
            self.outer_cv.split(X, y, groups)
        ):
            X_inner = X[train_index]
            y_inner = y[train_index]

            best_model = None
            best_score = 0

            for inner_train_index, inner_test_index in self.inner_cv.split(X_inner):
                model.fit(X_inner[inner_train_index], y_inner[inner_train_index])
                current_score = model.score(
                    X_inner[inner_test_index], y_inner[inner_test_index]
                )
                if current_score > best_score:
                    best_model = model
                    best_score = current_score

            if save_model:
                self.nested_models[inx] = best_model
            self.nested_scores[inx] = best_model.score(X[test_index], y[test_index])
