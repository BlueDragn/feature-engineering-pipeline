
def handle_missing_values(df):
    # Implementation for handling missing values
    # Database currently has no missing values.
    # Placeholder for future handling if needed.
    df = df.copy()
    return df


def create_age_group(row):
    if row['Age'] > 45:
        return 'Senior'
    elif row['Age'] >= 26:
        return 'Adult'
    else:
        return 'Youth'



def create_income_band(row):
    if row['Annual Income (k$)'] > 80:
        return 'High'
    elif row['Annual Income (k$)'] <= 80:
        return 'Medium'
    else:
        return 'Low'

def create_high_income_flag(row):
    if row['Annual Income (k$)'] > 80:
        return 1
    else:
        return 0

def create_high_spending_flag(row):
    if row['Spending Score (1-100)'] > 60:
        return 1
    else:
        return 0


def build_features(df):
    df = handle_missing_values(df)
    df = df.drop(columns=['CustomerID'])
    df['Age_Group'] = df.apply(create_age_group, axis=1)
    df['Income_Band'] = df.apply(create_income_band, axis=1)
    df['High_Income_Flag'] = df.apply(create_high_income_flag, axis=1)
    df['High_Spending_Flag'] = df.apply(create_high_spending_flag, axis=1)
    return df
