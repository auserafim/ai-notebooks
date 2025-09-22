class dataset_cleaner:
    def __init__(self, dataframe):
        self.df = dataframe
    def dropping_unknown_values_at_rows(self, col, target_value):
        self.df =  self.df[self.df[col] != target_value]
        return self
    def dropping_useless_columns(self, col_list):
        return self.df.drop(labels=col_list, axis=1, inplace=True)
    def filling_unknown(self, value=9):
        return self.df.fillna(9)
    def filling_with_most_frequent(self):
        imputer = SimpleImputer(strategy='most_frequent')
        self.df[self.df.columns] = imputer.fit_transform(self.df)
    def probability_ratio_encoding(self, cat_cols, target_col, smoothing=1):
        """
        Probability ratio encoding
        """
        self.encoder = TargetEncoder(cols=cat_cols, smoothing=smoothing)
        self.df = self.encoder.fit_transform(self.df, self.df[target_col])
        print("Performed probability ratio encoding.")
        return self
    def label_encoding(self, cat_cols):
        le = LabelEncoder()
        for col in categorical_features:
            self.df[col] = le.fit_transform(df[col])
    def transform_into_category(self, columns_to_transform):
        for col in columns_to_transform:
            if col in self.df.columns:
                if self.df[col].dtype == 'float64':
                    self.df[col] = self.df[col].astype('category')
            self.df[col] = self.df[col].astype('category')
    def convert_to_int(self, col):
        self.df[col] = self.df[col].astype(int)