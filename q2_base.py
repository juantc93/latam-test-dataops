
def q2_base(file_path):
    
    import pandas as pd
    import emoji
    from collections import Counter
    import re
    
    df = pd.read_json(file_path, lines=True)\
    .assign(date=lambda x: x.date.dt.date,
            username=lambda x: x.user.apply(lambda y: y.get("username")))
    
    return Counter(
        (
            (
                i.chars for i in emoji.analyze(("|").join(list(df.content.values)))
                )
            )
            )\
            .most_common(10)

