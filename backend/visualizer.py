import matplotlib.pyplot as plt
import io
import base64
from typing import List, Dict, Optional

def generate_bar_chart(data: List[Dict], x_key: str, y_key: str, title: str = "") -> Optional[str]:
    """
    Generates a bar chart from a list of dictionaries and returns base64 encoded image string.
    - x_key: column to be used on x-axis (e.g., item_id or category)
    - y_key: column to be used on y-axis (e.g., total_sales or units_sold)
    """

    try:
        x = [str(row[x_key]) for row in data if row.get(x_key) is not None and row.get(y_key) is not None]
        y = [row[y_key] for row in data if row.get(x_key) is not None and row.get(y_key) is not None]

        if not x or not y:
            return None

        plt.figure(figsize=(10, 5))
        bars = plt.bar(x, y, color='teal')
        plt.xlabel(x_key.replace('_', ' ').title())
        plt.ylabel(y_key.replace('_', ' ').title())
        plt.title(title if title else f"{y_key.title()} by {x_key.title()}")
        plt.xticks(rotation=45, ha='right')

        # Annotate bars with values
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), round(bar.get_height(), 2),
                     ha='center', va='bottom', fontsize=9)

        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        buffer.close()
        plt.close()

        return image_base64

    except Exception as e:
        print(f"Error generating bar chart: {e}")
        return None
