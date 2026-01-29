import pandas as pd
import numpy as np
from decimal import Decimal
from tableautes import tableautes

df = pd.DataFrame({
    "date": pd.date_range("2025-01-01", periods=10, freq="D"),
    "price": np.random.randint(80, 120, 10)
})

stats = {
    "average": Decimal(str(df.price.mean())),
    "max": Decimal(str(df.price.max())),
    "min": Decimal(str(df.price.min()))
}

print(tableautes(df, headers="keys", tablefmt="pretty"))
print(stats)
