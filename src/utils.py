def analysis(self):
        while True:
            choice = input("What EDA now? Type 1 (shape), 2 (head), 3 (tail), 4(columns) 5(info) 6(stats) 0 (exit): ")
            if choice == "1":
                print(self.data.shape)
            elif choice == "2":
                print(self.data.head())
            elif choice == "3":
                print(self.data.tail())
            elif choice == "4":
                print(self.data.columns)
            elif choice == "5":
                print(self.data.info())
            elif choice == "6":
                print(self.data.describe(include='all'))
            elif choice == "0":
                print("Exiting EDA...")
                break
            else:
                print("Invalid choice, please select 1, 2, 3 or 0.")


def visualization(self):
        features = list(self.data.columns)  # Access data using sel
        print("1 - Feature Distribution")
        print("2 - Feature vs Feature")
        print("3 - Correlation")
        print("4 - Outlier Detection (Boxplot)")

        choose = input("Which graph to plot: ")
        if choose == "1":
            # Plot feature distribution
            self.data.hist(figsize=(12, 8), bins=50, color='skyblue', edgecolor='black')
            plt.suptitle("Feature Distributions", fontsize=16)
            plt.show()
        elif choose == "2":
            # Plot Feature vs Feature relationship
            print("Best suggestion: Copy the feature names and then paste them to avoid errors.")
            first = input("Enter 1st Feature: \n")
            second = input("Enter 2nd Feature: \n")
            if first in features and second in features:
                plt.figure(figsize=(12, 5))
                sns.histplot(data=self.data, x=first, hue=second, multiple='stack', bins=50, palette='pastel', edgecolor='black')
                plt.title(f'{first} vs {second}')
                plt.xlabel(first)
                plt.ylabel('Count')
                plt.show()
            else:
                print("Feature not found. Exiting visualization.")
        elif choose == "3":
            # Plot correlation heatmap
            print("Please choose whether you want to see the correlation of:")
            print("1 - Entire data")
            print("2 - Just two columns")
            corr = input("Choose visualization option: ")
            if corr == "1":
                try:
                    plt.figure(figsize=(10, 8))
                    sns.heatmap(self.data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
                    plt.title('Correlation Heatmap of All Features')
                    plt.show()
                except Exception as e:
                    print(e)
            elif corr == "2":
                print("Best suggestion: Copy the feature names and then paste them to avoid errors.")
                f1 = input("Enter 1st Feature: \n")
                f2 = input("Enter 2nd Feature: \n")
                if f1 in features and f2 in features:
                    try:
                        correl = self.data[[f1, f2]].corr()
                        sns.heatmap(correl, annot=True, cmap='coolwarm', square=True, linewidths=1, fmt=".2f")
                        plt.title(f'Correlation: {f1} vs {f2}')
                        plt.show()
                    except Exception as e:
                        print(e)
                else:
                    print("One or both features not found. Exiting correlation visualization.")
        elif choose == "4":
            # Plot boxplot for outlier detection
            plt.figure(figsize=(12, 6))
            sns.boxplot(data=self.data, palette="Set2")
            plt.xticks(rotation=45)
            plt.title("Boxplot of Features")
            plt.show()
        else:
         print("Invalid choice. Please select a valid option (1, 2, 3, or 4).")



def clean(self):
        features = list(self.data.columns)
        while True:
            print("\nCLEANING OPTIONS:")
            print("1 - Show Missing Values")
            print("2 - Show Duplicates")
            print("3 - Drop Columns")
            print("4 - Encoding")
            print("5 - Normalize Data")
            print("6 - Scale Specific Column")
            print("7 - Save the Data")
            print("8 - Remove Outliers")
            print("0 - Exit Cleaning Menu")

            choice = input("Select option: ")

            if choice == "1":
                print(self.data.isnull().sum())
                print("Total missing values:", self.data.isnull().sum().sum())
                action = input("Do you want to handle missing values? (yes/no): ")
                if action.lower() == "yes":
                    print("\nChoose how you want to handle missing values:")
                    print("1 - Replace with a specific value")
                    print("2 - Remove rows with missing values")
                    print("3 - Forward fill or Backward fill")

                    method = input("Enter your choice (1/2/3): ")

                    if method == "1":
                        value = input("Enter the value to fill missing values: ")
                        self.data.fillna(value, inplace=True)
                        print(f"Missing values replaced with '{value}'.")

                    elif method == "2":
                        self.data.dropna(inplace=True)
                        print("Rows with missing values removed.")

                    elif method == "3":
                        print("Choose filling method:")
                        print("1 - Forward Fill")
                        print("2 - Backward Fill")
                        filling = input("Enter your choice (1/2): ")
                        if filling == "1":
                            self.data.fillna(method='ffill', inplace=True)
                            print("Missing values filled using forward fill.")
                        elif filling == "2":
                            self.data.fillna(method='bfill', inplace=True)
                            print("Missing values filled using backward fill.")
                        else:
                            print("Invalid filling choice.")

                    else:
                        print("Invalid choice.")

            elif choice == "2":
                print(self.data.duplicated().sum())
                print("Total duplicates:", self.data.duplicated().sum())
                action = input("Do you want to handle duplicates? (yes/no): ")
                if action.lower() == "yes":
                    method = input("Type 1 to remove duplicate rows or 2 to replace duplicates with value: ")
                    if method == "1":
                        self.data.drop_duplicates(inplace=True)
                        print("Duplicate rows removed.")
                    elif method == "2":
                        print("Replacing duplicates is not a common operation. Skipping replacement.")
                    else:
                        print("Invalid choice.")

            elif choice == "3":
                col = input("Enter column name to drop: ")
                if col in features:
                    self.data.drop(columns=[col], inplace=True)
                    print(f"Column '{col}' dropped.")
                else:
                    print("Column not found.")

            elif choice == "4":
                print("Currently we are only doing One Hot Encoding (OHE).")
                self.data = pd.get_dummies(self.data, drop_first=True)
                print("Encoding completed.")

            elif choice == "5":
                scaler = MinMaxScaler()
                num_cols = self.data.select_dtypes(include=['int64', 'float64']).columns
                self.data[num_cols] = scaler.fit_transform(self.data[num_cols])
                print("Normalization completed.")

            elif choice == "6":
                col = input("Enter column name to scale: ")
                if col in features:
                    if self.data[col].dtype == 'object':
                        print("Cannot scale categorical feature.")
                    else:
                        scaler = MinMaxScaler()
                        self.data[[col]] = scaler.fit_transform(self.data[[col]])
                        print(f"Scaling completed for '{col}'.")
                else:
                    print("Column not found.")

            elif choice == "7":
                name = input("Enter file name to save (without .csv): ")
                self.data.to_csv(f"{name}.csv", index=False)
                print(f"Data saved as {name}.csv")

            elif choice == "8":
                col = input("Enter column name to remove outliers: ")
                if col in features:
                    if self.data[col].dtype == 'object':
                        print("Cannot remove outliers from categorical column.")
                    else:
                        plt.figure(figsize=(8, 4))
                        sns.boxplot(x=self.data[col])
                        plt.title(f"Boxplot Before Removing Outliers: {col}")
                        plt.show()

                        Q1 = self.data[col].quantile(0.25)
                        Q3 = self.data[col].quantile(0.75)
                        IQR = Q3 - Q1
                        lower_bound = Q1 - 1.5 * IQR
                        upper_bound = Q3 + 1.5 * IQR

                        self.data = self.data[(self.data[col] >= lower_bound) & (self.data[col] <= upper_bound)]

                        plt.figure(figsize=(8, 4))
                        sns.boxplot(x=self.data[col])
                        plt.title(f"Boxplot After Removing Outliers: {col}")
                        plt.show()

                        print(f"Outliers removed from '{col}'.")
                else:
                    print("Column not found.")

            elif choice == "0":
                print("Exiting Cleaning Menu...")
                break

            else:
                print("Invalid choice, try again.")