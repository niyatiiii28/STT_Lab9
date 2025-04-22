from kfp import dsl
import mlrun

@dsl.pipeline(name="breast-cancer-pipeline")
def pipeline():
    """Pipeline for training and deploying a breast cancer classifier"""
    # Step 1: Data Ingestion
    data_prep_task = mlrun.run_function(
        "data-prep",
        handler="data_prep",
        outputs=["dataset"]
    )

    # Step 2: Model Training with Hyperparameter Tuning
    train_task = mlrun.run_function(
        "train-model",
        handler="train_model",
        inputs={"dataset": data_prep_task.outputs["dataset"]},
        hyperparams={
            "n_estimators": [10, 100, 200],
            "max_depth": [2, 5, 10]
        },
        selector="max.accuracy",
        outputs=["model", "confusion-matrix", "feature-selection"]
    )

    # Step 3: Model Deployment
    mlrun.deploy_function(
        "serving",
        models={"breast-cancer-model": train_task.outputs["model"]}
    )