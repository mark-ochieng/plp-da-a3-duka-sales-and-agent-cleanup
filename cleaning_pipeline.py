
import pandas as pd
import numpy as np


def clean_agent_data(txns, agents):
    """
    Clean mobile-money agent transactions and merge agent information.

    Returns:
        clean_df: Cleaned transaction DataFrame.
        log: Dictionary recording the cleaning actions and affected rows.
    """

    # Work on copies to avoid changing the original datasets
    df = txns.copy()
    agent_data = agents.copy()

    log = {
        "original_transaction_rows": len(df)
    }

    # 1. Remove duplicate transaction IDs
    duplicate_count = df["txn_id"].duplicated().sum()
    df = df.drop_duplicates(subset="txn_id", keep="first").copy()
    log["duplicate_rows_removed"] = int(duplicate_count)

    # 2. Standardize transaction type labels
    original_types = df["txn_type"].copy()

    df["txn_type"] = (
        df["txn_type"]
        .astype("string")
        .str.strip()
        .str.lower()
        .map({
            "deposit": "Deposit",
            "withdrawal": "Withdrawal"
        })
    )

    log["transaction_types_standardized"] = int(
        (original_types != df["txn_type"]).sum()
    )

    # 3. Convert amounts to numeric values
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    missing_amounts = df["amount"].isna().sum()
    median_amount = df["amount"].median()

    df["amount_imputed"] = df["amount"].isna()

    df["amount"] = df["amount"].fillna(median_amount)

    log["missing_amounts_imputed"] = int(missing_amounts)
    log["imputation_value"] = float(median_amount)

    # 4. Identify outliers using the IQR method
    q1 = pd.to_numeric(txns["amount"], errors="coerce").quantile(0.25)
    q3 = pd.to_numeric(txns["amount"], errors="coerce").quantile(0.75)
    iqr = q3 - q1
    upper_bound = q3 + (1.5 * iqr)

    df["is_outlier"] = df["amount"] > upper_bound

    log["iqr_upper_bound"] = float(upper_bound)
    log["outliers_flagged"] = int(df["is_outlier"].sum())

    # 5. Standardize transaction dates
    df["txn_date"] = df["txn_date"].astype("string").str.replace(
        "/", "-", regex=False
    )

    df["txn_date"] = pd.to_datetime(
        df["txn_date"], errors="coerce"
    )

    log["invalid_dates"] = int(df["txn_date"].isna().sum())

    # 6. Merge transactions with agent information
    df = df.merge(
        agent_data[["agent_id", "county"]],
        on="agent_id",
        how="left",
        validate="many_to_one"
    )

    log["unknown_agents"] = int(df["county"].isna().sum())

    # Format dates as ISO YYYY-MM-DD strings
    df["txn_date"] = df["txn_date"].dt.strftime("%Y-%m-%d")

    log["final_transaction_rows"] = len(df)

    return df, log
