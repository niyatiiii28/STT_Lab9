import mlrun
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from mlrun.frameworks.sklearn import apply_mlrun

def train_model(
    context: mlrun.MLClientCtx,
    dataset: mlrun.DataItem,
    n_estimators: int = 100,
    max_depth: int = 3,
    model_name: str = "cancer_classifier"
):
    """Train a random forest classifier"""
    # Prepare dataset
    df = dataset.as_df()
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Train-test split (10% test data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    
    # Define and train the model
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    
    # Apply MLRun tracking
    model = apply_mlrun(
        model=model,
        model_name=model_name,
        X_test=X_test,
        y_test=y_test
    )
    
    model.fit(X_train, y_train)
    
    return model